# figs_new_b.py — Figures 6-12: branching tree, Christmas tree, Hermes,
# relational dyad, five-color mesh, Open Portals, seven-step ladder
from helpers import T, R, Ln, PTH, Circ, Head, SVG


# ------------------------------- Figure 6: the branching decision tree --------
def build_fig_branch():
    b = []
    b.append(T(436, 76, "PATH A", "#c4a0e8", 10, 600, "start"))
    for x, n, l1, l2 in [(436, "4", "STEP A", "first action"),
                         (548, "5", "COST A", "hidden cost"),
                         (660, "6", "RELATIONS", "home impact")]:
        b.append(R(x, 88, 96, 52))
        b.append(T(x + 48, 109, f"{n} · {l1}", "#c4a0e8", 9, 600))
        b.append(T(x + 48, 123, l2, "#8a8692", 7))
    b.append(T(766, 114, "→ 7 · 8 · 9", "#8a8692", 9, 400, "start"))
    b.append(Ln(532, 114, 544, 114, "#8a8692", 1.5))
    b.append(Head(552, 114, 1, 0, "#8a8692", 4))
    b.append(Ln(644, 114, 656, 114, "#8a8692", 1.5))
    b.append(Head(664, 114, 1, 0, "#8a8692", 4))
    for x, t1, t2 in [(48, "1 · TENSION", "the core crossroads"),
                      (168, "2 · DRIVER", "the emotional engine"),
                      (288, "3 · QUESTION", "what must be answered")]:
        b.append(R(x, 198, 104, 56, "#e8c4a0", 2))
        b.append(T(x + 52, 221, t1, "#e8c4a0", 9.5, 600))
        b.append(T(x + 52, 236, t2, "#8a8692", 7))
    b.append(Ln(152, 226, 164, 226, "#e8c4a0", 1.5))
    b.append(Head(172, 226, 1, 0, "#e8c4a0", 4))
    b.append(Ln(272, 226, 284, 226, "#e8c4a0", 1.5))
    b.append(Head(292, 226, 1, 0, "#e8c4a0", 4))
    b.append(PTH("M 392 226 L 414 226 L 414 114 L 428 114", "#c4a0e8", 1.5))
    b.append(Head(436, 114, 1, 0, "#c4a0e8", 4))
    b.append(PTH("M 392 226 L 414 226 L 414 338 L 428 338", "#c4a0e8", 1.5))
    b.append(Head(436, 338, 1, 0, "#c4a0e8", 4))
    for x, n, l1, l2 in [(436, "10", "STEP B", "first action"),
                         (548, "11", "COST B", "hidden cost"),
                         (660, "12", "RELATIONS", "home impact")]:
        b.append(R(x, 312, 96, 52))
        b.append(T(x + 48, 333, f"{n} · {l1}", "#c4a0e8", 9, 600))
        b.append(T(x + 48, 347, l2, "#8a8692", 7))
    b.append(T(766, 338, "→ 13 · 14 · 15", "#8a8692", 9, 400, "start"))
    b.append(Ln(532, 338, 544, 338, "#8a8692", 1.5))
    b.append(Head(552, 338, 1, 0, "#8a8692", 4))
    b.append(Ln(644, 338, 656, 338, "#8a8692", 1.5))
    b.append(Head(664, 338, 1, 0, "#8a8692", 4))
    b.append(T(436, 392, "PATH B", "#c4a0e8", 10, 600, "start"))
    b.append(T(420, 444, "mirror positions across the fork — 4↔10 first action · "
                         "5↔11 cost · 6↔12 relations · 7↔13 fuel · 8↔14 hurdle · "
                         "9↔15 harvest", "#8a8692", 8.5))
    return SVG(840, 470, "SPREAD F · THE 15-CARD BRANCHING DECISION TREE",
               "One Trunk · Two Branches · Compare Each Position Across the Fork",
               "\n".join(b))


# ------------------------------- Figure 7: the 22-card Christmas tree ----------
def build_fig_xmas():
    b = []
    b.append(PTH("M 320 72 L 96 470 L 544 470 Z", "#2a2830", 1, dash="5 5"))
    b.append(PTH("M 255 523 C 70 470, 70 140, 300 100", "#8a8692", 1.2, dash="4 4"))
    b.append(Head(310, 100, 1, 0, "#8a8692", 4.5))
    b.append('<text fill="#8a8692" font-family="Georgia, serif" font-size="8" '
             'font-weight="600" text-anchor="middle" transform="rotate(-90 58 330)" '
             'x="58" y="330">ASCENDING RETURN STROKE</text>')
    b.append(R(265, 80, 110, 46, "#e8c4a0", 2))
    b.append(T(320, 108, "1 · CROWN", "#e8c4a0", 10.5, 600))
    for x in (215, 325):
        b.append(R(x, 150, 100, 46))
        b.append(T(x + 50, 178, "02" if x == 215 else "03", "#c4a0e8", 11, 600))
    for i, x in enumerate([160, 270, 380]):
        b.append(R(x, 220, 100, 46))
        b.append(T(x + 50, 248, f"0{i + 4}", "#c4a0e8", 11, 600))
    for i, x in enumerate([125, 225, 325, 425]):
        b.append(R(x, 290, 90, 46))
        b.append(T(x + 45, 318, f"{i + 7:02d}", "#c4a0e8", 11, 600))
    for i, x in enumerate([104, 192, 280, 368, 456]):
        b.append(R(x, 360, 80, 46))
        b.append(T(x + 40, 388, f"{i + 11:02d}", "#c4a0e8", 11, 600))
    for i, x in enumerate([90, 168, 246, 324, 402, 480]):
        b.append(R(x, 430, 70, 46))
        b.append(T(x + 35, 458, f"{i + 16:02d}", "#c4a0e8", 11, 600))
    b.append(R(265, 500, 110, 46, "#e8c4a0", 2))
    b.append(T(320, 528, "22 · ROOT", "#e8c4a0", 10.5, 600))
    tiers = [(96, "TIER 1 · THE CROWN", "the high release — 1 card", "#e8c4a0"),
             (166, "TIER 2 · THE COVENANT", "radical consent &amp; TOGETHER — 2", "#c4a0e8"),
             (236, "TIER 3 · THE PASSAGE", "through night into body — 3", "#c4a0e8"),
             (306, "TIER 4 · THE DYNAMO", "the power circuit — 4", "#c4a0e8"),
             (376, "TIER 5 · THE WORKSHOP", "mastery &amp; craft — 5", "#c4a0e8"),
             (446, "TIER 6 · THE HARVEST", "solar joy — 6", "#c4a0e8"),
             (516, "TIER 7 · THE ROOT", "soil grounding · T_STOP — 1", "#e8c4a0")]
    for y, t1, t2, col in tiers:
        b.append(T(610, y, t1, col, 9, 600, "start"))
        b.append(T(610, y + 14, t2, "#8a8692", 8, 400, "start"))
    b.append(T(420, 580, "roll a d6 beside each tier for its live kinetic voltage "
                         "(1 stillness → 6 breakthrough)", "#8a8692", 9))
    b.append(T(420, 604, "the ascending return verifies that the root fulfills the crown",
               "#8a8692", 8.5, italic=True))
    return SVG(840, 630, "THE 22-CARD CHRISTMAS TREE ENGINE",
               "The Master Lifecycle · 22 Major Arcana · Seven Descending Tiers "
               "+ the Ascending Return", "\n".join(b))


# ------------------------------- Figure 8: the Hermes 36 grand tableau --------
def build_fig_hermes():
    b = []
    anchors = {4: "THE HOUSE", 21: "MOUNTAIN", 28: "GENTLEMAN", 31: "THE SUN"}
    for i in range(1, 37):
        row, col = divmod(i - 1, 9)
        x = 36 + col * 86
        y = 76 + row * 78
        cx = x + 40
        if i in anchors:
            b.append(R(x, y, 80, 72, "#e8c4a0", 1.5))
            b.append(T(cx, y + 34, f"{i:02d}", "#e8c4a0", 12, 600))
            b.append(T(cx, y + 52, anchors[i], "#e8c4a0", 6.5, 600))
        else:
            b.append(R(x, y, 80, 72, "#c4a0e8", 1))
            b.append(T(cx, y + 42, f"{i:02d}", "#c4a0e8", 12, 600))
    b.append(T(76 + 40, 310 + 16, "✦", "#e8c4a0", 9, 600))
    b.append(T(420, 404, "✦ significator (28 Gentleman) · warm cells mark anchors: "
                         "4 The House · 21 The Mountain · 31 The Sun", "#8a8692", 8.5))
    return SVG(840, 424, "THE HERMES 36 GRAND TABLEAU",
               "A Simultaneous Spatial Field · 4 × 9 Matrix — Read by Proximity, "
               "Rows, Columns &amp; Diagonals", "\n".join(b))


# ------------------------------- Figure 9: the relational dyad ---------------
def build_fig_dyad():
    b = []
    b.append(T(150, 88, "PARTNER A POLE", "#e8c4a0", 10.5, 600))
    b.append(T(420, 88, "THE SHARED CRUCIBLE", "#c4a0e8", 10.5, 600))
    b.append(T(690, 88, "PARTNER B POLE", "#e8c4a0", 10.5, 600))
    b.append(Ln(150, 168, 150, 208, "#2a2830", 1, "4 3"))
    b.append(Ln(690, 168, 690, 208, "#2a2830", 1, "4 3"))
    b.append(Ln(420, 168, 420, 208, "#2a2830", 1, "4 3"))
    b.append(Ln(420, 272, 420, 312, "#2a2830", 1, "4 3"))
    b.append(Ln(235, 136, 335, 136, "#8a8692", 1, "2 4"))
    b.append(Ln(505, 136, 605, 136, "#8a8692", 1, "2 4"))
    b.append(Ln(235, 240, 335, 240, "#8a8692", 1, "2 4"))
    b.append(Ln(505, 240, 605, 240, "#8a8692", 1, "2 4"))
    cards = [(65, 104, "1 · CORE DRIVE", "the feeling · the need", "#e8c4a0"),
             (65, 208, "2 · ATTENTION CAP", "the energy available", "#e8c4a0"),
             (605, 104, "6 · CORE DRIVE", "the feeling · the need", "#e8c4a0"),
             (605, 208, "7 · ATTENTION CAP", "the energy available", "#e8c4a0"),
             (335, 104, "3 · THE HEARTH", "the foundation now", "#c4a0e8"),
             (335, 208, "4 · ACTIVE STACK", "the live topic between you", "#c4a0e8"),
             (335, 312, "5 · SHARED FLAME", "the mutual gift", "#e8c4a0")]
    for x, y, t1, t2, col in cards:
        b.append(R(x, y, 170, 64, col, 2 if col == "#e8c4a0" else 1.5))
        b.append(T(x + 85, y + 27, t1, col, 10, 600))
        b.append(T(x + 85, y + 44, t2, "#8a8692", 7.5))
    b.append(T(420, 420, "if an attention card is a heavy Spade, the partner is tapped "
                         "out — let them rest by the Hearth", "#8a8692", 9, italic=True))
    return SVG(840, 440, "THE 7-CARD RELATIONAL DYAD SPREAD",
               "Five Colors of Soul · The Health, Communication &amp; Mutual Care "
               "Between Two", "\n".join(b))


# ------------------------------- Figure 10: the five-color mesh --------------
def build_fig_mesh():
    b = []
    b.append(Circ(360, 330, 238, "#2a2830", 1.5, dash="6 4"))
    b.append(PTH("M 360 120 L 236 490 L 560 255 L 160 255 L 484 490 Z",
                 "#8a8692", 1.2, dash="5 5"))
    b.append(R(295, 298, 130, 64, "#e8c4a0", 2.5))
    b.append(T(360, 325, "0 · SHARED HEARTH", "#e8c4a0", 10.5, 600))
    b.append(T(360, 342, "the whole sanctuary", "#8a8692", 7.5))
    nodes = [(298, 92, "1 · WHITE", "the hearth &amp; care", "#e8e4ec"),
             (98, 227, "2 · BLUE", "mind &amp; truth", "#8aa8d8"),
             (498, 227, "5 · GREEN", "somatic bond", "#8ac8a4"),
             (174, 462, "3 · BLACK", "autonomy · space", "#77727e"),
             (422, 462, "4 · RED", "the living flame", "#d88a80")]
    for x, y, t1, t2, col in nodes:
        b.append(R(x, y, 124, 56, col, 1.8))
        b.append(T(x + 62, y + 22, t1, col, 9.5, 600))
        b.append(T(x + 62, y + 38, t2, "#8a8692", 7))
    b.append(T(360, 600, "watch which node starves and which overheats — when all five "
                         "harmonize around 0, the hearth burns warm", "#8a8692", 8.5))
    return SVG(720, 630, "THE 5-COLOR FAMILY &amp; CHOSEN COMMUNITY MESH",
               "One Shared Hearth · Five Relational Drives in Pentagram Harmony",
               "\n".join(b))


# ------------------------------- Figure 11: Open Portals modes --------------
def build_fig_portals():
    b = []
    b.append(T(60, 92, "MODE I · BIPOLAR SEAM PROBE", "#e8c4a0", 10.5, 600, "start"))
    b.append(R(80, 106, 160, 72, "#c4a0e8", 1.5))
    b.append(T(160, 132, "LIGHT CARD", "#c4a0e8", 10, 600))
    b.append(T(160, 148, "celestial intention", "#8a8692", 7.5))
    b.append(T(160, 163, "W &gt; 0", "#c4a0e8", 8, 600))
    b.append(R(600, 106, 160, 72, "#e8c4a0", 1.5))
    b.append(T(680, 132, "DARK CARD", "#e8c4a0", 10, 600))
    b.append(T(680, 148, "somatic fuel", "#8a8692", 7.5))
    b.append(T(680, 163, "W &lt; 0", "#e8c4a0", 8, 600))
    b.append(Ln(244, 142, 344, 142, "#8a8692", 1.5))
    b.append(Head(352, 142, 1, 0, "#8a8692", 4))
    b.append(Ln(596, 142, 430, 142, "#8a8692", 1.5))
    b.append(Head(422, 142, -1, 0, "#8a8692", 4))
    b.append('<rect fill="none" height="48" rx="6" stroke="#e8c4a0" '
             'stroke-dasharray="5 4" stroke-width="1.5" width="136" x="352" y="118"></rect>')
    b.append(T(420, 138, "THE PORTAL", "#e8c4a0", 9.5, 600))
    b.append(T(420, 152, "W = 0 · 3-inch seam", "#8a8692", 7))
    b.append(T(60, 216, "MODE II · PORTAL ACTIVATION &amp; FREQUENCY TUNING",
               "#e8c4a0", 10.5, 600, "start"))
    b.append(R(345, 230, 150, 44, "#c4a0e8", 1.5))
    b.append(T(420, 249, "MENTAL KEY", "#c4a0e8", 9, 600))
    b.append(T(420, 263, "the thought required", "#8a8692", 7))
    b.append(Ln(420, 274, 420, 280, "#8a8692", 1.5))
    b.append(Head(420, 286, 0, 1, "#8a8692", 4))
    b.append(R(80, 296, 150, 50, "#c4a0e8", 1.5))
    b.append(T(155, 317, "EMOTIONAL KEY", "#c4a0e8", 9, 600))
    b.append(T(155, 331, "the feeling required", "#8a8692", 7))
    b.append(Ln(236, 321, 339, 321, "#8a8692", 1.5))
    b.append(Head(345, 321, 1, 0, "#8a8692", 4))
    b.append(R(610, 296, 150, 50, "#c4a0e8", 1.5))
    b.append(T(685, 317, "PHYSICAL KEY", "#c4a0e8", 9, 600))
    b.append(T(685, 331, "the body required", "#8a8692", 7))
    b.append(Ln(604, 321, 401, 321, "#8a8692", 1.5))
    b.append(Head(395, 321, -1, 0, "#8a8692", 4))
    b.append(R(345, 286, 150, 76, "#e8c4a0", 2))
    b.append(T(420, 314, "PORTAL CARD", "#e8c4a0", 10.5, 600))
    b.append(T(420, 331, "d20 ≥ 10 = wide open", "#8a8692", 8))
    b.append(T(420, 347, "the standing wave", "#8a8692", 7))
    b.append(T(420, 428, "Mode III: recursive ingress on an ambiguous card · Mode IV: "
                         "altar remediation between Wand and Cup, sealed by the Pentacle",
               "#8a8692", 8.5))
    b.append(T(420, 448, "Mode V: the Truth-Weight — the Dagger laid flat upon a tangled "
                         "card, edge never to the cards", "#8a8692", 8.5))
    return SVG(840, 476, "OPEN PORTALS · OPERATIONAL MODES",
               "Transverse Threshold Ingress · Light Side (W &gt; 0) · Dark Side "
               "(W &lt; 0) · The Seam (W = 0)", "\n".join(b))


# ------------------------------- Figure 12: the seven-step ladder ------------
def build_fig_steps():
    b = []
    steps = [
        ("Inscribe the question &amp; center at the Point of Stillness (L)",
         "three slow breaths · a clean sheet of paper · the stated intention"),
        ("Touch the altar tools &amp; inscribe the working figure",
         "Wand (will) · Cup (calm) · Pentacle (the cool weight of earth) · Dagger (the traced figure)"),
        ("Cast the core stones of chance",
         "d4 domain · d6 phase · d8 vector — the unbribable lots"),
        ("Set the horizon &amp; clear the resolution gate",
         "d12 life sector · d20 threshold — a roll of 10 or more opens the gate"),
        ("Lay the 22-card Christmas tree &amp; roll live tier tickers",
         "seven descending tiers · a d6 of kinetic voltage beside each"),
        ("Strike the whispering book for the scripture seal",
         "one verse · its living room · the bench translation"),
        ("Synthesize into hands-on craft &amp; seal at T_STOP",
         "the words cease · the tools are grounded · we live with our hands"),
    ]
    for i, (t1, t2) in enumerate(steps):
        y = 84 + i * 64
        col = "#e8c4a0" if i % 2 == 0 else "#c4a0e8"
        b.append(R(90, y, 660, 52, col, 1.3))
        b.append(Circ(124, y + 26, 15, col, 1.2))
        b.append(T(124, y + 30, str(i + 1), col, 11, 600))
        b.append(T(152, y + 23, t1, "#e4e0e8", 11.5, 600, "start"))
        b.append(T(152, y + 40, t2, "#8a8692", 8.5, 400, "start"))
        if i < 6:
            b.append(Ln(420, y + 52, 420, y + 58, "#8a8692", 1.5))
            b.append(Head(420, y + 62, 0, 1, "#8a8692", 3.5))
    b.append(T(420, 560, "follow in order whenever you need deep clarity "
                         "and unshakeable guidance", "#8a8692", 9))
    return SVG(840, 580, "THE SEVEN-STEP MASTER BEACON PROCEDURE",
               "The Complete Operational Ritual for a Comprehensive Master Inquiry",
               "\n".join(b))
