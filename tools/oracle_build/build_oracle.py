# build_oracle.py — pipeline: clean -> correct -> pandoc -> figures -> validate -> write
# Publication layer: removes the not-ready Five Colors (MtG) system, restoring
# the Nine Chambers canon of bad36ae, while keeping the new layouts grimoire.
import re
import subprocess
from pathlib import Path

from helpers import TMP, FIG, build_fig13, build_fig14
from figs_new_a import build_fig_core, build_fig_cicero, build_fig_tree, build_fig_wheel
from figs_new_b import (build_fig_branch, build_fig_xmas, build_fig_hermes,
                        build_fig_portals, build_fig_steps)

SRC = Path("/home/magesguild/talismans/THE_HOUSE_OF_THE_LIVING_ORACLE.md")
REPO = Path("/home/thalia/src/ThaliaEphemeraSaga")
OUT = REPO / "docs/writings/The_House_of_the_Living_Oracle.html"


def must_sub(pattern, repl, text, count=1, flags=0):
    new, n = re.subn(pattern, repl, text, flags=flags)
    assert n == count, f"pattern {pattern!r}: got {n} matches, expected {count}"
    return new


# 1. clean the source: strip metadata, then remove the not-ready Five Colors
drop = ("**Status:**", "**Location:**", "**Lineage:**")
lines = SRC.read_text().splitlines()
text = "\n".join(l for l in lines if not l.startswith(drop)) + "\n"
assert text.count("**Status:**") == 0

# delete Chamber IX (Five Colors) and the relational spreads section 4.5
text = must_sub(r"### Chamber IX: The Five Colors of the Soul.*?(?=### Chamber X:)",
                "", text, flags=re.S)
text = must_sub(r"### 4\.5\. Relational & Interpersonal Spreads \(The Five Colors of Soul\).*?(?=### 4\.6\.)",
                "", text, flags=re.S)
# renumber: Gates X -> IX (reverted to Sky), 4.6/4.7/4.8 -> 4.5/4.6/4.7
text = must_sub(r"### Chamber X: The Gates of Starlight and Soil \(Open Portals Dual Decks\)",
                "### Chamber IX: The Gates of Sky and Soil (Open Portals Dual Decks)", text)
text = must_sub(r"### 4\.6\. Transverse Threshold Ingress",
                "### 4.5. Transverse Threshold Ingress", text)
text = must_sub(r"### 4\.7\. Cleromancy", "### 4.6. Cleromancy", text)
text = must_sub(r"### 4\.8\. Bibliomancy", "### 4.7. Bibliomancy", text)
# title and chamber count back to Nine
text = must_sub(r"the Ten Chambers of the Soul", "the Nine Chambers of the Soul", text)
text = must_sub(r"## 3\. The Ten Chambers of the Sovereign House",
                "## 3. The Nine Chambers of the Sovereign House", text)
text = must_sub(r"Sovereign House with Ten Interconnected Chambers",
                "Sovereign House with Nine Interconnected Chambers", text)
(TMP / "oracle_clean.md").write_text(text)

# 2. pandoc through the ornate template
subprocess.run(
    ["pandoc", str(TMP / "oracle_clean.md"), "-f", "markdown", "-t", "html",
     "--section-divs", "--template", str(REPO / "docs/templates/saga-ornate.html"),
     "--metadata", "title=The House of the Living Oracle",
     "-o", str(TMP / "oracle_pandoc.html")],
    check=True)
page = (TMP / "oracle_pandoc.html").read_text()

# 3. replace every ASCII chart block with its figure
fig1 = (TMP / "fig1_old.svg").read_text()  # the Nine Chambers map, as published at bad36ae
figs = [
    ("THE THRESHOLD OF THE HEARTH",
     FIG(1, "The Nine Chambers of the Sovereign House", fig1)),
    ("THE THREE CORE DAILY &amp; NARRATIVE SPREADS",
     FIG(2, "The Three Core Daily &amp; Narrative Spreads", build_fig_core())),
    ("THE CICERO ARCHITECTURAL SPREAD SUITE",
     FIG(3, "The Cicero Architectural Spread Suite", build_fig_cicero())),
    ("SPREAD D: THE 10-SEPHIROTH TREE OF LIFE SPREAD",
     FIG(4, "Spread D · The 10-Sephiroth Tree of Life", build_fig_tree())),
    ("SPREAD E: THE 12-HOUSE ASTROLOGICAL WHEEL",
     FIG(5, "Spread E · The 12-House Astrological Wheel", build_fig_wheel())),
    ("SPREAD F: THE 15-CARD BRANCHING DECISION TREE",
     FIG(6, "Spread F · The 15-Card Branching Decision Tree", build_fig_branch())),
    ("THE 22-CARD CHRISTMAS TREE ENGINE",
     FIG(7, "The 22-Card Christmas Tree Engine", build_fig_xmas())),
    ("HERMES 36 GRAND TABLEAU (4x9 MATRIX)",
     FIG(8, "The Hermes 36 Grand Tableau", build_fig_hermes())),
    ("OPEN PORTALS OPERATIONAL MODES",
     FIG(9, "Open Portals · Operational Modes I &amp; II", build_fig_portals())),
    ("THE SEVEN-STEP MASTER BEACON PROCEDURE",
     FIG(10, "The Seven-Step Master Beacon Procedure", build_fig_steps())),
    ("T_STOP: SOIL GROUNDING",
     FIG(12, "T_STOP Soil Grounding", build_fig14())),
]

pre_re = re.compile(r"<pre[^>]*>.*?</pre>", re.S)


def replace_pre(page, marker, fig):
    for m in pre_re.finditer(page):
        if marker in m.group(0):
            return page[:m.start()] + fig + page[m.end():]
    raise AssertionError(f"marker not found: {marker}")


for marker, fig in figs:
    page = replace_pre(page, marker, fig)

# 4. insert the receipts figure just before Step 6
fig11 = FIG(11, "The Sovereign Beacon Hardware Receipts", build_fig13())
m = re.search(r'<section id="step-6[^"]*"', page)
assert m, "step-6 section not found"
page = page[:m.start()] + fig11 + "\n" + page[m.start():]

# 5. validate
assert page.count('<figure class="dark-sky-figure">') == 12, page.count('<figure')
assert "<pre" not in page
for bad in ("/home", "talismans", "<strong>Status</strong>",
            "<strong>Location</strong>", "<strong>Lineage</strong>",
            "Ten Chambers", "Five Colors", "5-Color", "Selesnya", "Izzet",
            "Rakdos", "Golgari", "Azorius", "Starlight", "STARLIGHT",
            "tapped out", "pass priority"):
    assert bad not in page, f"leak detected: {bad}"
assert page.count("<h2") == 6, f"h2 count {page.count('<h2')}"
assert page.count("<h3") == 18, f"h3 count {page.count('<h3')}"
assert page.count("<h4") == 18, f"h4 count {page.count('<h4')}"
assert "Nine Chambers" in page and "GATES OF SKY" in page
assert "Chamber IX: The Gates of Sky and Soil" in page
for n in range(1, 13):
    assert f"Figure {n} ·" in page, f"missing caption: Figure {n}"

# 6. write
OUT.write_text(page)
print("OK — written:", OUT)
print("bytes:", len(page))
print("figures:", page.count('<figure class="dark-sky-figure">'))
print("h2:", page.count("<h2"), "| h3:", page.count("<h3"), "| h4:", page.count("<h4"))
print("title ok:", "<title>The House of the Living Oracle — Thalia Ephemera Saga</title>" in page)
