# figs_new_a.py — Figures 2-5: core spreads, Cicero suite, Tree of Life, wheel
from helpers import T, R, Ln, PTH, Circ, Head, SVG


# ------------------------------- Figure 2: the three core daily spreads --------
def build_fig_core():
    b = []
    b.append(T(60, 100, "LEVEL 0 · THE ATOMIC PROBE", "#e8c4a0", 11, 600, "start"))
    b.append(R(375, 112, 90, 60, "#e8c4a0", 2))
    b.append(T(420, 141, "1", "#c4a0e8", 14, 600))
    b.append(T(420, 192, "single card or jumper · the immediate sensor", "#8a8692", 9))
    b.append(T(420, 208, "if it answers the question, stop here", "#e4e0e8", 8.5, italic=True))
    b.append(Ln(420, 222, 420, 236, "#e8c4a0", 2))
    b.append(Head(420, 244, 0, 1, "#e8c4a0"))

    b.append(T(60, 268, "LEVEL 1 · THE 3-CARD DAILY STREAM", "#c4a0e8", 11, 600, "start"))
    for i, (cx, lab) in enumerate([(225, "PASSING"), (375, "PRESENT"), (525, "APPROACHING")]):
        b.append(R(cx, 282, 90, 60))
        b.append(T(cx + 45, 311, str(i + 1), "#c4a0e8", 13, 600))
        b.append(T(cx + 45, 360, lab, "#e4e0e8", 8.5, 600))
    b.append(Ln(317, 312, 363, 312, "#e8c4a0", 1.5))
    b.append(Head(371, 312, 1, 0, "#e8c4a0"))
    b.append(Ln(467, 312, 513, 312, "#e8c4a0", 1.5))
    b.append(Head(521, 312, 1, 0, "#e8c4a0"))
    b.append(T(420, 380, "read as one sentence — background, verb, horizon", "#8a8692", 9))
    b.append(Ln(420, 392, 420, 406, "#c4a0e8", 2))
    b.append(Head(420, 414, 0, 1, "#c4a0e8"))

    b.append(T(60, 438, "LEVEL 2 · THE 7-CARD CAUSAL ARCADIA", "#e8c4a0", 11, 600, "start"))
    labels = [("ORIGIN", "SEED"), ("RISING", "DRIVE"), ("HIDDEN", "FOIL"),
              ("CORE", "PIVOT"), ("NEXT", "STEP"), ("OUTSIDE", "WEATHER"),
              ("MANIFEST", "HARVEST")]
    for i, (l1, l2) in enumerate(labels):
        cx = 56 + i * 106
        pivot = (i == 3)
        b.append(R(cx, 452, 92, 60, "#e8c4a0" if pivot else "#c4a0e8",
                   2.5 if pivot else 1.5))
        b.append(T(cx + 46, 481, str(i + 1), "#e8c4a0" if pivot else "#c4a0e8", 13, 600))
        b.append(T(cx + 46, 532, l1, "#e4e0e8", 7.5, 600))
        b.append(T(cx + 46, 543, l2, "#e4e0e8", 7.5, 600))
    b.append(Ln(316, 556, 408, 562, "#8a8692", 1))
    b.append(Ln(524, 556, 432, 562, "#8a8692", 1))
    b.append(T(420, 568, "▲", "#e8c4a0", 10, 600))
    b.append(T(420, 594, "everything turns on Card 4 — compare 1↔7 seed vs harvest · "
                         "2↔6 drive vs weather · 3↔5 foil vs step", "#8a8692", 8.5))
    return SVG(840, 612, "THE THREE CORE DAILY &amp; NARRATIVE SPREADS",
               "English 52-Card &amp; Marseille Streams · Levels 0 – 2", "\n".join(b))


# ------------------------------- Figure 3: the Cicero suite (A, B, C) ----------
def build_fig_cicero():
    b = []
    b.append(Ln(296, 70, 296, 615, "#2a2830", 1, "4 4"))
    b.append(Ln(592, 70, 592, 615, "#2a2830", 1, "4 4"))
    # Panel A — Tetra-Bus
    b.append(T(150, 92, "SPREAD A · THE TETRA-BUS", "#e8c4a0", 11, 600))
    b.append(T(150, 106, "4 Cards · 1D Pipeline Trace", "#8a8692", 8.5))
    cardsA = [("1 · FIRE — WILL", "Atziluth · The Creative Spark"),
              ("2 · WATER — HEART", "Briah · The Emotional Vessel"),
              ("3 · AIR — MIND", "Yetzirah · The Logical Blueprint"),
              ("4 · EARTH — FLESH", "Assiah · The Physical Soil")]
    for i, (t1, t2) in enumerate(cardsA):
        y = 126 + i * 80
        b.append(R(95, y, 110, 50))
        b.append(T(150, y + 20, t1, "#e8c4a0", 10.5, 600))
        b.append(T(150, y + 35, t2, "#8a8692", 7.5))
        if i < 3:
            b.append(Ln(150, y + 50, 150, y + 66, "#8a8692", 1.5))
            b.append(Head(150, y + 74, 0, 1, "#8a8692", 4))
    b.append(T(150, 462, "find the break in the line —", "#8a8692", 8.5, italic=True))
    b.append(T(150, 476, "where the project stalls between spark and soil",
               "#8a8692", 8.5, italic=True))
    # Panel B — Pillar Balancer
    b.append(T(446, 92, "SPREAD B · THE PILLAR BALANCER", "#e8c4a0", 11, 600))
    b.append(T(446, 106, "7 Cards · Three Pillars", "#8a8692", 8.5))
    b.append(T(373, 124, "SEVERITY", "#8a8692", 9, 600))
    b.append(T(453, 124, "MILDNESS", "#e8c4a0", 9, 600))
    b.append(T(533, 124, "MERCY", "#8a8692", 9, 600))
    b.append(Ln(373, 182, 373, 246, "#2a2830", 1, "4 3"))
    b.append(Ln(453, 182, 453, 192, "#2a2830", 1, "4 3"))
    b.append(Ln(453, 238, 453, 248, "#2a2830", 1, "4 3"))
    b.append(Ln(533, 182, 533, 246, "#2a2830", 1, "4 3"))
    pil = [(336, 136, "2 · GEBURAH", "Boundary", "#c4a0e8"),
           (336, 246, "5 · HOD", "Craft Mind", "#c4a0e8"),
           (416, 136, "1 · KETHER", "The High Ideal", "#e8c4a0"),
           (416, 192, "4 · TIPHARETH", "Heart Center", "#e8c4a0"),
           (416, 248, "7 · MALKUTH", "Ground", "#e8c4a0"),
           (496, 136, "3 · CHESED", "Bounty", "#c4a0e8"),
           (496, 246, "6 · NETZACH", "Passion", "#c4a0e8")]
    for x, y, t1, t2, col in pil:
        b.append(R(x, y, 75, 46, col, 2 if col == "#e8c4a0" else 1.5))
        b.append(T(x + 37, y + 18, t1, col, 8.5, 600))
        b.append(T(x + 37, y + 32, t2, "#8a8692", 7))
    b.append(T(446, 336, "compare Left (discipline) vs Right (expansion);",
               "#8a8692", 8.5, italic=True))
    b.append(T(446, 350, "the Middle Pillar is the path back to equilibrium",
               "#8a8692", 8.5, italic=True))
    # Panel C — 10-Card Guidance AST
    b.append(T(751, 92, "SPREAD C · THE 10-CARD GUIDANCE AST", "#e8c4a0", 11, 600))
    b.append(T(751, 106, "The Structural Life Cross", "#8a8692", 8.5))
    b.append(Ln(706, 176, 706, 200, "#8a8692", 1.2))
    b.append(Ln(706, 260, 706, 284, "#8a8692", 1.2))
    b.append(Ln(664, 230, 676, 230, "#8a8692", 1.2))
    b.append(Ln(736, 230, 744, 230, "#8a8692", 1.2))
    b.append(Ln(851, 150, 851, 338, "#2a2830", 1, "4 3"))
    b.append(R(604, 210, 60, 40))
    b.append(T(634, 228, "5 · PASSING", "#c4a0e8", 8, 600))
    b.append(T(634, 240, "the receding", "#8a8692", 7))
    b.append(R(676, 136, 60, 40))
    b.append(T(706, 154, "3 · CROWN", "#c4a0e8", 8, 600))
    b.append(T(706, 166, "the ideal", "#8a8692", 7))
    b.append(R(676, 284, 60, 40))
    b.append(T(706, 302, "4 · ROOT", "#c4a0e8", 8, 600))
    b.append(T(706, 314, "the deep ground", "#8a8692", 7))
    b.append(R(744, 210, 60, 40))
    b.append(T(774, 228, "6 · APPROACH", "#c4a0e8", 8, 600))
    b.append(T(774, 240, "the entering", "#8a8692", 7))
    b.append(R(676, 200, 60, 60, "#e8c4a0", 2.5))
    b.append(T(706, 226, "1 · CORE", "#e8c4a0", 9, 600))
    b.append(T(706, 240, "the condition", "#8a8692", 7))
    b.append(R(662, 232, 88, 30, "#c4a0e8", 1.5, fill="#1c1a26"))
    b.append(T(706, 251, "2 · THE CROSSING", "#c4a0e8", 8, 600))
    staff = [(300, "7", "SELF-AGENCY"), (252, "8", "ENVIRONMENT"),
             (204, "9", "HOPES/FEARS"), (156, "10", "INTEGRATION")]
    for y, n, lab in staff:
        b.append(R(824, y, 54, 34))
        b.append(T(851, y + 14, n, "#c4a0e8", 8.5, 600))
        b.append(T(851, y + 26, lab, "#8a8692", 6.5))
    b.append(T(751, 372, "staff, bottom to top: 7 Self-Agency · 8 Environment", "#8a8692", 8))
    b.append(T(751, 386, "9 Hopes &amp; Fears · 10 Integration &amp; Harvest", "#8a8692", 8))
    b.append(T(751, 412, "start at the cross (1+2), then the spine (4→3),",
               "#8a8692", 8.5, italic=True))
    b.append(T(751, 426, "then time (5→6), then climb the staff (7→10)",
               "#8a8692", 8.5, italic=True))
    b.append(T(450, 618, "classical Golden Dawn architecture · Cicero system · the 78-card deck",
               "#8a8692", 9))
    return SVG(900, 640, "THE CICERO ARCHITECTURAL SPREAD SUITE",
               "The Six Classical Golden Dawn Spreads · Panels A – C", "\n".join(b))


# ------------------------------- Figure 4: the 10-Sephiroth Tree of Life -------
def build_fig_tree():
    b = []
    b.append(Ln(360, 134, 360, 197))
    b.append(Ln(145, 197, 575, 197))
    b.append(Ln(145, 224, 145, 300))
    b.append(Ln(575, 224, 575, 300))
    b.append(PTH("M 145 354 L 145 407 L 295 407"))
    b.append(PTH("M 575 354 L 575 407 L 425 407"))
    b.append(Ln(360, 434, 360, 480))
    b.append(Ln(145, 480, 575, 480))
    b.append(PTH("M 145 514 L 145 567 L 295 567"))
    b.append(PTH("M 575 514 L 575 567 L 425 567"))
    b.append(Ln(360, 594, 360, 620))
    b.append('<rect fill="#0f0e12" height="34" rx="4" stroke="#2a2830" '
             'stroke-dasharray="4 3" stroke-width="1" width="120" x="300" y="240"></rect>')
    nodes = [(295, 80, "1 · KETHER", "The Crown Aim", "#e8c4a0", 2),
             (80, 170, "3 · BINAH", "Form &amp; Mother", "#e8c4a0", 2),
             (510, 170, "2 · CHOKMAH", "Creative Spark", "#e8c4a0", 2),
             (80, 300, "5 · GEBURAH", "Boundary · Pruning", "#c4a0e8", 1.5),
             (510, 300, "4 · CHESED", "Loving Bounty", "#c4a0e8", 1.5),
             (295, 380, "6 · TIPHARETH", "The Heart Center", "#c4a0e8", 1.5),
             (80, 460, "8 · HOD", "Logic &amp; Craft", "#c4a0e8", 1.5),
             (510, 460, "7 · NETZACH", "Passion &amp; Arts", "#c4a0e8", 1.5),
             (295, 540, "9 · YESOD", "Subconscious Loom", "#c4a0e8", 1.5),
             (295, 620, "10 · MALKUTH", "Physical Soil · Body", "#e8c4a0", 2)]
    for x, y, t1, t2, col, sw in nodes:
        b.append(R(x, y, 130, 54, col, sw))
        b.append(T(x + 65, y + 21, t1, col, 10, 600))
        b.append(T(x + 65, y + 37, t2, "#8a8692", 7.5))
    b.append(T(360, 257, "DA'AT · THE THRESHOLD", "#8a8692", 8, 600))
    b.append(T(360, 269, "the invisible knowing", "#8a8692", 6.5))
    b.append(T(360, 694, "read in four tiers — Supernals (1–3) · Ethical (4–6) "
                         "· Astral (7–9) · Ground (10)", "#8a8692", 9))
    return SVG(720, 708, "SPREAD D · THE 10-SEPHIROTH TREE OF LIFE",
               "Deal in the Lightning Flash: 1 → 2 → 3 → … → 10", "\n".join(b))


# ------------------------------- Figure 5: the 12-house astrological wheel -----
def build_fig_wheel():
    b = []
    b.append(Circ(360, 340, 250, "#2a2830", 1.5, dash="6 4"))
    b.append(Circ(360, 340, 118, "#2a2830", 1, dash="3 4"))
    b.append(Ln(110, 340, 610, 340, "#2a2830", 1))
    b.append(Ln(360, 90, 360, 590, "#2a2830", 1))
    houses = [(62, 316, "1 · ASCENDANT", "Self &amp; Vitality", True),
              (96, 441, "2 · FUEL", "Material Wealth", False),
              (187, 533, "3 · MIND", "Daily Craft", False),
              (312, 566, "4 · NADIR", "Home &amp; Hearth", True),
              (437, 533, "5 · JOY", "Play &amp; Erotic", False),
              (528, 441, "6 · ROUTINE", "Work &amp; Service", False),
              (562, 316, "7 · DESCENDANT", "Partners &amp; Dyads", True),
              (528, 191, "8 · DEPTHS", "Shared Resources", False),
              (437, 100, "9 · HORIZONS", "Philosophy · Art", False),
              (312, 66, "10 · MIDHEAVEN", "Public Vocation", True),
              (187, 100, "11 · GUILD", "Chosen Family", False),
              (96, 191, "12 · REST", "Solitude · Peace", False)]
    for x, y, t1, t2, axis in houses:
        col = "#e8c4a0" if axis else "#c4a0e8"
        b.append(R(x, y, 96, 48, col, 2 if axis else 1.5))
        b.append(T(x + 48, y + 21, t1, col, 8.5, 600))
        b.append(T(x + 48, y + 35, t2, "#8a8692", 7))
    b.append(T(360, 645, "read by opposite axes — 1↔7 identity · 4↔10 security "
                         "· 3↔9 learning", "#8a8692", 9))
    return SVG(720, 660, "SPREAD E · THE 12-HOUSE ASTROLOGICAL WHEEL",
               "A 360° Horizon of the Whole Life · Deal Counter-Clockwise from House 1",
               "\n".join(b))
