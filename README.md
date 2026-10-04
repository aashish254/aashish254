# Aashish Mahato

Systems Architect · AI Integration Engineer · Kathmandu, Nepal

I build local-first tools for people who work with AI agents, and I send the
fixes back upstream instead of keeping them in my own fork. Most of my
open-source work goes into [Laya](https://github.com/NandhaKishorM/laya), an AI
decision engine that answers with a single forward pass rather than generating
token by token, so speed and correctness are the product; I have worked on its
batching, its TypeScript SDK, its CLI, its MCP server and its benchmarks.

My own tools — [burn](https://github.com/aashish254/burn),
[limen](https://github.com/aashish254/limen) and
[agentvault](https://github.com/aashish254/agentvault) — run on your machine with
no account and no telemetry; agentvault only talks to a channel you configure
yourself, for approvals.

## Contributions

**[Laya](https://github.com/NandhaKishorM/laya)** — its biggest contributor
outside the owner, [per its own graph](https://github.com/NandhaKishorM/laya/graphs/contributors).
What I built there:

- **Batching across every backend.** [The ONNX runtime got the batch API the
  torch agent already had](https://github.com/NandhaKishorM/laya/pull/489),
  [the TypeScript SDK got it too](https://github.com/NandhaKishorM/laya/pull/329),
  [structured decisions got a throughput form](https://github.com/NandhaKishorM/laya/pull/520),
  and [the CLI scores a file of requests in one pass](https://github.com/NandhaKishorM/laya/pull/511).
- **Long documents.** [Route first, then scan the whole state in
  windows](https://github.com/NandhaKishorM/laya/pull/497) — and
  [the same API on the ONNX agent](https://github.com/NandhaKishorM/laya/pull/494).
- **The TypeScript SDK brought to parity with the Python core:**
  [the hooks lifecycle](https://github.com/NandhaKishorM/laya/pull/308),
  [structured decisions](https://github.com/NandhaKishorM/laya/pull/339),
  [truncation reported from the real token
  budget](https://github.com/NandhaKishorM/laya/pull/336),
  [per-language temperature overrides](https://github.com/NandhaKishorM/laya/pull/398).
- **Ways to reach it.** [The CLI](https://github.com/NandhaKishorM/laya/pull/155),
  [batch tools over MCP for agents](https://github.com/NandhaKishorM/laya/pull/513),
  [a schema-driven LangChain decision
  node](https://github.com/NandhaKishorM/laya/pull/524).
- **Benchmarks that report what they measured.** [Which commit a score came
  from](https://github.com/NandhaKishorM/laya/pull/588), [whether the GPU ran it
  or the CPU quietly did](https://github.com/NandhaKishorM/laya/pull/574), [what
  a request waited for](https://github.com/NandhaKishorM/laya/pull/592).
- **Trust in the checkpoints.** [Each one verified against its own SHA-256
  map](https://github.com/NandhaKishorM/laya/pull/572), and [a truncated download
  repaired rather than trusted](https://github.com/NandhaKishorM/laya/pull/801).

**Documentation.** [Curriculum fixes into
freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp/pulls?q=is%3Apr+is%3Amerged+author%3Aaashish254)
where a hint or an assertion taught the wrong thing — [one of them here](https://github.com/freeCodeCamp/freeCodeCamp/pull/70447).
[Dead links and broken tables in
public-apis](https://github.com/public-apis/public-apis/pulls?q=is%3Apr+is%3Amerged+author%3Aaashish254).
[Typos and a compatibility fact in MDN](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3Aaashish254+user%3Amdn),
including [Safari's support for `sizes="auto"`](https://github.com/mdn/browser-compat-data/pull/30629).

**Bugs in tools I use.** [A savings counter that printed `$0.00` instead of
pricing itself](https://github.com/headroomlabs-ai/headroom/pull/3821) · [a
layout solver that lost a node to float
rounding](https://github.com/tt-a1i/archify/pull/591) · [a flake8-bugbear check
that flagged names it shouldn't
have](https://github.com/PyCQA/flake8-bugbear/pull/581) · [a crash on an
unlisted model id](https://github.com/andrewyng/openworker/pull/677) · [an empty
write that would truncate a
file](https://github.com/odysseus-dev/odysseus/pull/6415) · [local CLIs shadowed
by broken PATH shims](https://github.com/stablyai/orca/pull/23275) · [a missing
test for nested fixture
discovery](https://github.com/StellarCanary/ProtocolCanary-Fixtures/pull/90).

Every link above is a merged pull request. [The full set is one search
away](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3Aaashish254).

## Elsewhere

[LinkedIn](https://www.linkedin.com/in/aashish-mahato-572611257) ·
[LeetCode](https://leetcode.com/u/aashish124) ·
[All my pull requests](https://github.com/pulls?q=is%3Apr+author%3Aaashish254)
