# Aashish Mahato

**Systems Architect · AI Integration Engineer**

B.Tech CSE (VIT Vellore) · Kathmandu, Nepal · Nova
[LinkedIn](https://www.linkedin.com/in/aashish-mahato-572611257) ·
[LeetCode](https://leetcode.com/u/aashish124) ·
[burn live docs](https://aashish254.github.io/burn/) ·
[limen live docs](https://aashish254.github.io/limen/)

![509 GitHub contributions over the 53 weeks ending 29 Sep 2026, as a contribution heatmap. Nearly all of them fall in the last four columns.](assets/contributions.svg)

I build local-first AI tools, and I put the fixes back into the projects I
actually use instead of keeping them in my own fork.

## The short version

- **83 pull requests merged into other people's projects in September 2026.**
- **64 of them into [Laya](https://github.com/NandhaKishorM/laya)**, a
  28,000-star AI decision engine. I'm its biggest contributor outside the
  owner: 117 contributions to its graph, against 37 for the next name.
- **Around 20,000 lines added**, nearly all of it in that one project.
- **64 more pull requests open** across 32 repositories, waiting on review.

Every number here was pulled from the public GitHub API on **29 Sep 2026**. The
queries are at the [bottom](#receipts) — re-run them, and if a figure has
drifted, the query is still the truth.

## Where the work went

**Laya — 64 merged.** Laya answers with a single forward pass instead of
generating token by token, so speed and correctness _are_ the product. I made
it batch across every backend instead of handling one request at a time, gave
its TypeScript SDK the same features as the Python core, built the ways people
actually reach it (command line, MCP server for agents, LangChain), and made
its benchmarks report what they really measured — which commit a score came
from, and whether the model ran on the GPU or quietly fell back to the CPU.
A few examples: [batching](https://github.com/NandhaKishorM/laya/pull/489),
[the CLI](https://github.com/NandhaKishorM/laya/pull/155),
[honest health checks](https://github.com/NandhaKishorM/laya/pull/574).

**Documentation — 15 merged.** 6 into [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/pulls?q=is%3Apr+is%3Amerged+author%3Aaashish254)
curriculum, 5 into [public-apis](https://github.com/public-apis/public-apis/pulls?q=is%3Apr+is%3Amerged+author%3Aaashish254)
(dead links removed, broken tables repaired), 4 into
[MDN](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3Aaashish254+user%3Amdn).

**Smaller fixes — 4 merged.** A savings counter that printed `$0.00` instead of
pricing itself in [headroom](https://github.com/headroomlabs-ai/headroom/pull/3821),
a float-rounding bug in [archify's layout
solver](https://github.com/tt-a1i/archify/pull/591), a false positive in
[flake8-bugbear](https://github.com/PyCQA/flake8-bugbear/pull/581), and a
missing test for nested fixture discovery in
[ProtocolCanary](https://github.com/StellarCanary/ProtocolCanary-Fixtures/pull/90).

## Waiting on review

64 open pull requests. Where they are:
[Laya 8](https://github.com/NandhaKishorM/laya/pulls?q=is%3Apr+is%3Aopen+author%3Aaashish254)
·
[pear-desktop 5](https://github.com/pear-devs/pear-desktop/pulls?q=is%3Apr+is%3Aopen+author%3Aaashish254)
·
[paperclip 5](https://github.com/paperclipai/paperclip/pulls?q=is%3Apr+is%3Aopen+author%3Aaashish254)
·
[odysseus 5](https://github.com/odysseus-dev/odysseus/pulls?q=is%3Apr+is%3Aopen+author%3Aaashish254)
·
[mempalace 4](https://github.com/MemPalace/mempalace/pulls?q=is%3Apr+is%3Aopen+author%3Aaashish254)
·
[the remaining 37 across 27 repos](https://github.com/pulls?q=is%3Apr+is%3Aopen+author%3Aaashish254)

## My own projects

17 repositories, 75 stars between them. The six that matter:

- **[Aniflow](https://github.com/aashish254/Aniflow)** ★9 — turns webtoons into
  narrated videos: object detection, multi-voice narration, automated editing.
- **[burn](https://github.com/aashish254/burn)** ★8 — tells you what your coding
  agents actually cost. Reads the logs Claude Code, Codex, OpenCode and Gemini
  CLI already leave on disk. No account, no network.
  [Live docs](https://aashish254.github.io/burn/)
- **[limen](https://github.com/aashish254/limen)** ★7 — shows how much of your
  prompt is boilerplate your agent re-sends every call, and cuts it.
  [Live docs](https://aashish254.github.io/limen/)
- **[stratmate](https://github.com/aashish254/stratmate)** ★7 — planning and
  timing math for mobile game alliances.
- **[agentvault](https://github.com/aashish254/agentvault)** ★6 — a permission
  firewall for AI agents. On its own benchmark: 103 of 103 attacks blocked, 8
  of 8 normal operations allowed.
- **[ulp](https://github.com/aashish254/ulp)** ★6 — an open file format for
  agent usage and cost, mergeable between machines with no server.

## Also counted

23 pull requests were closed without ever being merged, and that belongs in the
record too. Ten of them were duplicates I opened against the same files in
`tldr-pages` — the maintainers closed the whole set. The rest split across MDN
(2), freeCodeCamp (2), Laya (2), JabRef (2) and five other repos.

---

<details>
<summary>Receipts — the queries behind every number above (29 Sep 2026)</summary>

```bash
# merged PRs (84 total, 83 excluding one to my own stratmate)
gh api "search/issues?q=is:pr+author:aashish254+is:merged&per_page=100"

# open PRs (64)
gh api "search/issues?q=is:pr+author:aashish254+is:open&per_page=100"

# closed without merging (23)
gh api "search/issues?q=is:pr+author:aashish254+is:closed+is:unmerged&per_page=100"

# lines landed: additions/deletions/changed_files for each merged PR
gh api repos/<owner>/<repo>/pulls/<number> --jq '{additions,deletions,changed_files}'

# contributions calendar (509 over 53 weeks)
gh api graphql -f query='{viewer{contributionsCollection(
  from:"2025-09-29T00:00:00Z",to:"2026-09-29T23:59:59Z"){
  contributionCalendar{totalContributions weeks{contributionDays{contributionCount date}}}}}}'

# my repositories and their stars
gh api users/aashish254/repos --paginate --jq '.[] | select(.fork==false)'
```

The chart above is built from that calendar by
[`scripts/make-banner.py`](scripts/make-banner.py), reading the committed
snapshot [`scripts/banner-data.json`](scripts/banner-data.json). Star counts are
the API's at pull time and will have moved since.

</details>

---

_Engineering notes: [system architecture & API orchestration
patterns](docs/architecture-patterns.md) ·
[developer onboarding & contribution practice](docs/developer-onboarding.md)_
