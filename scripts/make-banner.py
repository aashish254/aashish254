#!/usr/bin/env python3
"""Render assets/contributions.svg from scripts/banner-data.json.

The data file is a snapshot of the GitHub contributions calendar; regenerate
it with:

    gh api graphql -f query='{viewer{contributionsCollection(
      from:"2025-09-29T00:00:00Z",to:"2026-09-29T23:59:59Z"){
      contributionCalendar{totalContributions weeks{contributionDays{
      contributionCount date}}}}}}' > /tmp/contrib.json

then rebuild `weeks` and `pulled_at` in scripts/banner-data.json.
"""
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
data = json.loads((here / "banner-data.json").read_text())

W, H = 1280, 260
PAD_L, PAD_R, PAD_T, PAD_B = 28, 28, 64, 46
plot_w = W - PAD_L - PAD_R
plot_h = H - PAD_T - PAD_B

weeks = data["weeks"]
n = len(weeks)
peak = max(weeks)
step = plot_w / (n - 1)

# Linear scale: the shape of the record is the point, so no log smoothing.
points = [(PAD_L + i * step, PAD_T + plot_h - (v / peak) * plot_h) for i, v in enumerate(weeks)]
baseline = PAD_T + plot_h
line = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f},{y:.1f}" for i, (x, y) in enumerate(points))
area = f"{line} L{points[-1][0]:.1f},{baseline:.1f} L{points[0][0]:.1f},{baseline:.1f} Z"

ticks = []
for label, idx in data["ticks"].items():
    x = PAD_L + idx * step
    ticks.append(
        f'<text x="{x:.1f}" y="{H - 16}" text-anchor="middle" '
        f'font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" '
        f'letter-spacing="0.4" fill="#8A867F">{label}</text>'
        f'<line x1="{x:.1f}" y1="{PAD_T - 8}" x2="{x:.1f}" y2="{baseline}" stroke="#221F1C" stroke-width="1"/>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{data['aria_label']}">
  <title>{data['aria_label']}</title>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="#0B0C0E" stroke="#221F1C"/>
  <line x1="{PAD_L}" y1="{baseline}" x2="{W - PAD_R}" y2="{baseline}" stroke="#2E2A26" stroke-width="1"/>
  {''.join(ticks)}
  <path d="{area}" fill="#FF5C35" fill-opacity="0.10"/>
  <path d="{line}" fill="none" stroke="#FF5C35" stroke-width="1.75" stroke-linejoin="round"/>
  <circle cx="{points[-1][0]:.1f}" cy="{points[-1][1]:.1f}" r="3.5" fill="#FF5C35"/>
  <text x="{PAD_L}" y="34" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="26" fill="#EDEAE4">{data['total']}</text>
  <text x="{PAD_L + 92}" y="34" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" letter-spacing="1.2" fill="#8A867F">CONTRIBUTIONS · {n} WEEKS · PEAK WEEK {peak}</text>
  <text x="{W - PAD_R}" y="34" text-anchor="end" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="11" letter-spacing="0.4" fill="#8A867F">GitHub API · {data['pulled_at']}</text>
</svg>
'''

out = here.parent / "assets" / "contributions.svg"
out.parent.mkdir(exist_ok=True)
out.write_text(svg)
print(f"{out} <- {n} weeks, total {data['total']}, peak week {peak}")
