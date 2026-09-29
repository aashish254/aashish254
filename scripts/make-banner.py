#!/usr/bin/env python3
"""Render assets/contributions.svg from scripts/banner-data.json.

The data file is a snapshot of the GitHub contributions calendar, one entry per
week with Sunday-first `counts` and `levels` (null = outside the window).
Regenerate it with:

    gh api graphql -f query='{viewer{contributionsCollection(
      from:"2025-09-29T00:00:00Z",to:"2026-09-29T23:59:59Z"){
      contributionCalendar{totalContributions weeks{contributionDays{
      contributionCount contributionLevel date}}}}}}' > /tmp/contrib.json

then rebuild `weeks`, `total` and `pulled_at` in scripts/banner-data.json. The
levels come from GitHub's own quartiles, so the shading matches what the site
draws for the same account.
"""
import datetime
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
data = json.loads((here / "banner-data.json").read_text())

W, H = 1280, 260
PAD_L, PAD_R, PAD_T = 28, 28, 62
CELL, GAP = 18, 4
PITCH = CELL + GAP
MONO = "ui-monospace, SFMono-Regular, Menlo, monospace"

# GitHub's dark-mode contribution scale.
FILLS = {None: "none", 0: "#161B22", 1: "#0E4429", 2: "#006D32", 3: "#26A641", 4: "#39D353"}
BONE, MUTED, HAIRLINE = "#EDEAE4", "#8A867F", "#221F1C"

weeks = data["weeks"]
n = len(weeks)
grid_w = n * PITCH - GAP
grid_h = 7 * PITCH - GAP
top = PAD_T + 14

cells = []
for i, wk in enumerate(weeks):
    for r, lvl in enumerate(wk["levels"]):
        if not lvl:
            continue
        x = PAD_L + i * PITCH
        y = top + r * PITCH
        cells.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{FILLS[lvl]}"/>')

# Every cell is drawn; the lit ones are painted on top of the tiled empties.
empty_tile = (f'<pattern id="e" x="{PAD_L}" y="{top}" width="{PITCH}" height="{PITCH}" '
              f'patternUnits="userSpaceOnUse">'
              f'<rect width="{CELL}" height="{CELL}" rx="3" fill="{FILLS[0]}" '
              f'stroke="#22272E" stroke-width="0.5"/></pattern>')
empty_grid = (f'<rect x="{PAD_L}" y="{top}" width="{grid_w}" height="{grid_h}" fill="url(#e)"/>')

# Label a month at the first week whose window starts on or after its 1st.
labels = []
seen = set()
for i, wk in enumerate(weeks):
    d = datetime.date.fromisoformat(wk["start"])
    key = (d.year, d.month)
    if key in seen or d.day > 7:
        continue
    seen.add(key)
    name = d.strftime("%b")
    if name not in ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"):
        continue
    x = PAD_L + i * PITCH
    labels.append(
        f'<text x="{x}" y="{PAD_T - 4}" font-family="{MONO}" font-size="11" '
        f'letter-spacing="0.4" fill="{MUTED}">{name}</text>'
    )

legend_y = top + grid_h + 26
EMPTY_STROKE = ' stroke="#22272E" stroke-width="0.5"'
legend = []
for j, lvl in enumerate([0, 1, 2, 3, 4]):
    x = W - PAD_R - (5 - j) * PITCH - 44
    stroke = EMPTY_STROKE if not lvl else ""
    legend.append(f'<rect x="{x}" y="{legend_y - 12}" width="{CELL}" height="{CELL}" rx="3" '
                  f'fill="{FILLS[lvl]}"{stroke}/>')
legend.append(f'<text x="{W - PAD_R - 5 * PITCH - 52}" y="{legend_y}" text-anchor="end" '
              f'font-family="{MONO}" font-size="11" letter-spacing="0.4" fill="{MUTED}">Less</text>')
legend.append(f'<text x="{W - PAD_R}" y="{legend_y}" text-anchor="end" '
              f'font-family="{MONO}" font-size="11" letter-spacing="0.4" fill="{MUTED}">More</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{data['aria_label']}">
  <title>{data['aria_label']}</title>
  <defs>{empty_tile}</defs>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="#0B0C0E" stroke="{HAIRLINE}"/>
  {''.join(labels)}
  {empty_grid}
  {''.join(cells)}
  {''.join(legend)}
  <text x="{PAD_L}" y="34" font-family="{MONO}" font-size="26" fill="{BONE}">{data['total']}</text>
  <text x="{PAD_L + 92}" y="34" font-family="{MONO}" font-size="11" letter-spacing="1.2" fill="{MUTED}">CONTRIBUTIONS · {n} WEEKS · {sum(1 for w in weeks for c in w['counts'] if c)} ACTIVE DAYS</text>
  <text x="{W - PAD_R}" y="34" text-anchor="end" font-family="{MONO}" font-size="11" letter-spacing="0.4" fill="{MUTED}">GitHub API · {data['pulled_at']}</text>
</svg>
'''

out = here.parent / "assets" / "contributions.svg"
out.parent.mkdir(exist_ok=True)
out.write_text(svg)
lit = sum(1 for w in weeks for c in w["counts"] if c)
print(f"{out} <- {n} weeks, total {data['total']}, {lit} lit cells")
