# grow-seo-aeo-content

A reusable Codex skill for running a measurable SEO/AEO content growth loop.

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

## Contents

- `SKILL.md`: operating workflow and safety boundaries
- `scripts/score_opportunities.py`: deterministic opportunity scorer for GSC-like CSV data
- `references/data-contract.md`: scoring input schema
- `references/report-template.md`: audit and measurement report schema
- `references/sources.md`: source provenance and the rules each source influenced
- `agents/openai.yaml`: Codex UI metadata

## Source articles and evolution

This is an evolving skill. Its initial workflow was distilled from Harsehaj's first-person implementation report about BlogEO at Browserbase:

- [How I built an SEO/AEO blog engine — original article](https://harsehaj.substack.com/p/how-i-built-an-seoaeo-blog-engine)

See [`references/sources.md`](references/sources.md) for the principles incorporated, reported outcomes, limitations, and the parts of the skill this article influenced.

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
