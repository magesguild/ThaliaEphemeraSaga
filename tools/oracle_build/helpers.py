# helpers.py — shared SVG primitives + surgery on yesterday's figures
import re
from pathlib import Path

TMP = Path(__file__).resolve().parent
FF = "Georgia, serif"


def T(x, y, s, fill="#e4e0e8", size=10, weight=400, anchor="middle", italic=False):
    fam = "Georgia, italic" if italic else FF
    return (f'<text fill="{fill}" font-family="{fam}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" x="{x}" y="{y}">{s}</text>')


def R(x, y, w, h, stroke="#c4a0e8", sw=1.5, fill="#16141c", rx=6):
    return (f'<rect fill="{fill}" height="{h}" rx="{rx}" stroke="{stroke}" '
            f'stroke-width="{sw}" width="{w}" x="{x}" y="{y}"></rect>')


def RDASH(x, y, w, h, stroke="#e8c4a0", sw=1.5, fill="none", rx=6, dash="5 4"):
    return (f'<rect fill="{fill}" height="{h}" rx="{rx}" stroke="{stroke}" '
            f'stroke-dasharray="{dash}" stroke-width="{sw}" width="{w}" x="{x}" y="{y}"></rect>')


def Ln(x1, y1, x2, y2, stroke="#8a8692", sw=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line{d} stroke="{stroke}" stroke-width="{sw}" x1="{x1}" '
            f'x2="{x2}" y1="{y1}" y2="{y2}"></line>')


def PTH(d, stroke="#8a8692", sw=1.2, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path{da} d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"></path>'


def Circ(cx, cy, r, stroke="#c4a0e8", sw=1, fill="none", dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<circle{da} cx="{cx}" cy="{cy}" fill="{fill}" r="{r}" '
            f'stroke="{stroke}" stroke-width="{sw}"></circle>')


def Head(x, y, dx, dy, color="#e8c4a0", s=5.0):
    import math
    L = math.hypot(dx, dy) or 1.0
    ux, uy = dx / L, dy / L
    bx, by = x - ux * 2 * s, y - uy * 2 * s
    nx, ny = -uy, ux
    p1 = (bx + nx * s * 0.62, by + ny * s * 0.62)
    p2 = (bx - nx * s * 0.62, by - ny * s * 0.62)
    pts = f"{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {x:.1f},{y:.1f}"
    return f'<polygon fill="{color}" points="{pts}"></polygon>'


def SVG(w, h, title, subtitle, body):
    parts = [
        f'<svg role="img" style="width:100%;height:auto;display:block;" '
        f'viewbox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">',
        f'<rect fill="#0f0e12" height="{h}" rx="6" width="{w}"></rect>',
        T(w / 2, 32, title, "#c4a0e8", 18 if w >= 800 else 17, 600),
    ]
    if subtitle:
        parts.append(T(w / 2, 54, subtitle, "#8a8692", 11))
    parts.append(body)
    parts.append("</svg>")
    return "\n".join(parts)


def FIG(n, caption, svg):
    return (f'<figure class="dark-sky-figure"><figcaption class="figure-kicker">'
            f'Figure {n} · {caption}</figcaption>{svg}</figure>')


# ------------------------------- Figure 1: chambers map (Nine -> Ten surgery) --
def build_fig1():
    s = (TMP / "fig1_old.svg").read_text()
    s = s.replace("THE NINE CHAMBERS OF THE SOVEREIGN HOUSE",
                  "THE TEN CHAMBERS OF THE SOVEREIGN HOUSE")
    svg_open = s[:s.index("<rect")]
    elements = re.findall(
        r'<(?:rect|circle|text|line)\b[^>]*>.*?</(?:rect|circle|text|line)>', s)
    assert len(elements) > 70, f"unexpected element count {len(elements)}"

    viii_idx = next(i for i, e in enumerate(elements) if 'x="171.0"' in e)
    gates_idx = next(i for i, e in enumerate(elements) if 'x="429.0"' in e)
    bottom_idx = next(i for i, e in enumerate(elements) if "The Living House" in e)

    viii_els = [e for e in elements[viii_idx:gates_idx] if 'x1="411.0"' not in e]
    gates_els = [e for e in elements[gates_idx:bottom_idx] if 'x1="669.0"' not in e]

    # shift the VIII card left to the first column (x -129)
    viii_shift = []
    for e in viii_els:
        for a, b in [('x="171.0"', 'x="42.0"'), ('x="175.0"', 'x="46.0"'),
                     ('cx="193.0"', 'cx="64.0"'), ('x="193.0"', 'x="64.0"'),
                     ('x="303.0"', 'x="174.0"'), ('x="291.0"', 'x="162.0"')]:
            e = e.replace(a, b)
        viii_shift.append(e)

    # clone it as the IX Five Colors card (x +258) with new text
    ix_els = []
    for e in viii_shift:
        for a, b in [('cx="64.0"', 'cx="322.0"'), ('x="64.0"', 'x="322.0"'),
                     ('x="42.0"', 'x="300.0"'), ('x="46.0"', 'x="304.0"'),
                     ('x="174.0"', 'x="432.0"'), ('x="162.0"', 'x="420.0"')]:
            e = e.replace(a, b)
        e = e.replace(">VIII<", ">IX<")
        e = e.replace("THE STONES OF CHANCE", "THE FIVE COLORS OF SOUL")
        e = e.replace("Cleromancy", "Interpersonal Dynamics")
        e = re.sub(r'>d4[^<]*<', '>Tensions · Allies &amp; Dyads · The Stack<', e)
        ix_els.append(e)

    # shift the Gates card right to the third column (x +129), renumber X
    gates_shift = []
    for e in gates_els:
        for a, b in [('x="429.0"', 'x="558.0"'), ('x="433.0"', 'x="562.0"'),
                     ('cx="451.0"', 'cx="580.0"'), ('x="451.0"', 'x="580.0"'),
                     ('x="561.0"', 'x="690.0"'), ('x="549.0"', 'x="678.0"')]:
            e = e.replace(a, b)
        e = e.replace(">IX<", ">X<")
        e = e.replace("GATES OF SKY &amp; SOIL", "GATES OF STARLIGHT &amp; SOIL")
        gates_shift.append(e)

    # connector dashes between the three bottom cards (cloned from row 1)
    dash_tpl = next(e for e in elements if 'x1="282.0"' in e)
    dash_a = dash_tpl.replace('y1="379" y2="379"', 'y1="719" y2="719"')
    dash_b = dash_a.replace('x1="282.0" x2="300.0"', 'x1="540.0" x2="558.0"')

    new_elements = (elements[:viii_idx] + viii_shift + ix_els + gates_shift
                    + [dash_a, dash_b] + elements[bottom_idx:])
    out = svg_open + "\n" + "\n".join(new_elements) + "\n</svg>"

    assert "FIVE COLORS OF SOUL" in out
    assert ">X<" in out and "STARLIGHT" in out
    assert 'x="171.0"' not in out and 'x="429.0"' not in out
    assert 'x1="411.0"' not in out and 'x1="669.0"' not in out
    assert out.count('height="148"') == 9, out.count('height="148"')
    assert "NINE" not in out and "TEN CHAMBERS" in out
    return out


# ------------------------------- Figure 13: beacon receipts (label refresh) ---
def build_fig13():
    s = (TMP / "fig3_old.svg").read_text()
    swaps = [
        ("Tier 2 (Line 2)", "Tier 2 (Covenant)"),
        ("Tier 5 (Method)", "Tier 5 (Workshop)"),
        ("Tier 6 (Radiance)", "Tier 6 (Harvest)"),
        ("Mastery of Shared Sacred Craft", "Mastery of Quiet Craft &amp; Deep Study"),
    ]
    for a, b in swaps:
        assert a in s, f"fig3 missing: {a}"
        s = s.replace(a, b)
    return s


# ------------------------------- Figure 14: T_STOP (carried over as-is) -------
def build_fig14():
    return (TMP / "fig4_old.svg").read_text()
