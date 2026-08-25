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
- `agents/openai.yaml`: Codex UI metadata

## Safety model

The agent reads, scores, verifies, and drafts. It should not receive direct CMS publishing authority. A human approves material changes, and tested server-side code revalidates the current state before writing.

## License

Apache License 2.0.
