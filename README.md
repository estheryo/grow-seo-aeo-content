# SEO/AEO Skills

This repository contains reusable Codex skills for measurable SEO and AI-search growth.

[中文说明](README.zh-CN.md)

## Skills

### `grow-seo-aeo-content`

The repository root is a broad content-growth skill. It runs an inventory, prioritization, drafting, approval, publishing, and measurement loop.

### `win-ai-search-citations`

[`skills/win-ai-search-citations`](skills/win-ai-search-citations) is a separate, narrower skill for earning citations and recommendations in Google AI features, ChatGPT, Claude, Perplexity, and similar answer engines. It benchmarks the pages already being cited, maps prompts to canonical pages, creates claim-sized evidence blocks, strengthens independent validation, and measures citations separately from impressions, clicks, leads, and revenue.

It helps an agent:

- inventory and audit website content;
- prioritize recovery, CTR, ranking, and content-gap opportunities;
- draft small evidence-grounded edits and new articles;
- prevent keyword cannibalization;
- keep production publishing behind human approval and deterministic validation;
- measure page outcomes at +28 and +56 days against a site-wide control;
- track AI crawl/discovery, citations, and referrals separately.

## Install

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/estheryo/grow-seo-aeo-content.git ~/.codex/skills/grow-seo-aeo-content
```

Then invoke it with:

```text
Use $grow-seo-aeo-content to audit this website, rank SEO/AEO opportunities, and propose a measurable content plan.
```

To install the separate citation skill, copy or symlink its directory into your Codex skills directory:

```bash
ln -s "$(pwd)/skills/win-ai-search-citations" ~/.codex/skills/win-ai-search-citations
```

Then invoke it with:

```text
Use $win-ai-search-citations to benchmark the pages AI engines cite for our priority prompts and create a prioritized citation plan.
```

## Contents

- `SKILL.md`: operating workflow and safety boundaries
- `scripts/score_opportunities.py`: deterministic opportunity scorer for GSC-like CSV data
- `references/data-contract.md`: scoring input schema
- `references/report-template.md`: audit and measurement report schema
- `references/sources.md`: source provenance and the rules each source influenced
- `agents/openai.yaml`: Codex UI metadata

## Source articles and evolution

This is an evolving collection. The current skills were distilled from these canonical original articles and posts:

### `grow-seo-aeo-content`

- [How I built an SEO/AEO blog engine — original article](https://harsehaj.substack.com/p/how-i-built-an-seoaeo-blog-engine)
- [How to win search in 2026 (Google, AI & everywhere else) — Jake Ward](https://x.com/jakezward/status/2093320636743512116)

See [`references/sources.md`](references/sources.md) for the principles, reported outcomes, limitations, and workflow rules influenced by this article.

### `win-ai-search-citations`

- [Vendor blogs as AI citation sources — Alex Groberman](https://x.com/alexgroberman/status/2092607970274378041)
- [Local business visibility across Google and AI search — Alex Groberman](https://x.com/alexgroberman/status/2092248243568865453)
- [How Claude discovers and cites sources — Alex Groberman](https://x.com/alexgroberman/status/2091910002315518357)
- [Measuring generative-AI visibility in Search Console — Alex Groberman](https://x.com/alexgroberman/status/2091554033949626719)
- [ChatGPT citation study interpretation — Alex Groberman](https://x.com/alexgroberman/status/2091524620591739233)
- [Google Discovery Engine interpretation — Alex Groberman](https://x.com/alexgroberman/status/2012536184023462013)
- [Benchmark pages answer engines already cite — Jared Winger](https://x.com/BuildWithJared/status/2092718076479639713)

See [`skills/win-ai-search-citations/references/sources.md`](skills/win-ai-search-citations/references/sources.md) for the method each source influenced and the caveats applied to reported claims.

Future articles, papers, threads, talks, and implementation reports can be incorporated iteratively. Each revision should:

1. preserve only the author's canonical original link by default;
2. extract testable principles, assumptions, limitations, and reported outcomes;
3. compare the new material with the current workflow, retaining meaningful disagreements;
4. update the smallest appropriate instruction, reference, or script;
5. record exactly what changed in `references/sources.md`;
6. validate the skill and test any modified scripts before publishing.

## Safety model

The agent reads, scores, verifies, and drafts. It should not receive direct CMS publishing authority. A human approves material changes, and tested server-side code revalidates the current state before writing.

## License

Apache License 2.0.
