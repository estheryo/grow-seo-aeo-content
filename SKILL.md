---
name: grow-seo-aeo-content
description: "Audit and grow a website's SEO and answer-engine visibility through a measurable content loop: inventory pages, combine search/analytics/CMS data, rank recovery/CTR/ranking/content-gap opportunities, propose surgical edits, draft evidence-grounded articles, add human approval gates, and measure 28/56-day outcomes. Use for SEO audits, AEO/GEO/LLM citation analysis, content decay, low-CTR pages, keyword gaps, editorial planning, content refreshes, AI-assisted blog generation, building a recurring content-growth engine, or incorporating newly supplied SEO/AEO source articles into this evolving skill."
---

# Grow SEO/AEO Content

Build a closed loop from evidence to measured outcomes. Treat AI as a reader, analyst, and drafter; do not let it publish or mutate production content directly.

## Evolve from source material

When the user supplies a new article, paper, thread, talk, or implementation report for this skill:

1. Read the complete source and retain its canonical URL.
2. Record only the author's canonical original URL by default. Use an alternative URL only when the original is unavailable, and label it as a fallback.
3. Extract testable principles, implementation patterns, assumptions, limitations, and reported outcomes.
4. Compare them with the current workflow; preserve useful disagreements instead of forcing consensus.
5. Update the smallest appropriate part of `SKILL.md`, a reference, or a script. Do not paste article summaries into the core instructions when a concise rule is sufficient.
6. Add or update the source entry in `references/sources.md`, including what changed in the skill.
7. Validate the skill and test changed scripts before publishing the revision.

Read `references/sources.md` when tracing why a rule exists, evaluating conflicting advice, or incorporating new source material. Never represent a source's reported result as a universal benchmark.

## Choose the operating mode

- **Public audit**: Use crawlable pages, sitemaps, robots directives, search-result evidence, page metadata, structured data, and visible citations. Label traffic and opportunity estimates as unavailable unless supplied.
- **Connected audit**: Combine CMS inventory, Google Search Console (GSC), product analytics, rank/keyword data, backlink data, and prior-run snapshots.
- **Recurring engine**: Add scheduled audits, draft generation, approval cards, deterministic write handlers, measurement enrollment, and weekly reporting.

Never imply access to private analytics that was not provided. Separate observed facts, inferences, and recommendations.

## Execute the workflow

### 1. Define scope and baseline

Record the domain, locales, page types, audience, conversion goals, product documentation sources, comparison window, and available data. Prefer 28-day windows with a preceding 28-day comparison.

Map the **Total Addressable Search Market**: every commercially relevant search or question the organization could realistically win or influence. Cover three connected surfaces:

- **Google**: category, high-intent, comparison, alternative, problem, use-case, and AI Overview queries.
- **AI search**: recommendations, comparisons, category and problem prompts, competitor questions, and likely follow-ups across relevant answer engines.
- **Influence sources**: reviews, Reddit, YouTube, LinkedIn, publications, directories, comparison sites, and communities that repeatedly shape those results or buyer decisions.

Prioritize commercial relevance over list size. Establish a coverage baseline: the proportion of the mapped market where the brand has a useful owned page, meaningful search visibility, accurate AI presence, or credible third-party inclusion. Keep the component measures visible; do not hide them behind a single composite score.

Inventory canonical URLs from the CMS or sitemap. For each URL capture page type, publish/update dates, title, description, canonical, robots state, headings, word count, links, images, structured data, and content owner when available.

### 2. Run cheap checks across every page

Check missing/duplicate titles and descriptions, broken links and media, unintended noindex/canonical states, sitemap inconsistencies, stale product positioning, orphan pages, thin or overlapping content, weak internal linking, and missing answer-friendly structure.

Load the live page before alleging a factual contradiction. Quote or link the authoritative product documentation that establishes the contradiction.

### 3. Rank opportunity, not age

With GSC data, calculate three opportunity families over the latest 28 days:

- **Recover**: material clicks lost versus the previous window. Require both an absolute and proportional decline.
- **CTR**: impressions multiplied by the positive gap between expected CTR for the page's position and actual CTR. Treat this as a ranking signal, not a precise forecast, because GSC averages positions across queries.
- **Rank**: estimated clicks gained if a page-two query moved to page one. Prefer queries with meaningful impressions and positions roughly 5–20.

Use the largest supported opportunity as the primary intervention. Suppress low-impression noise. A verified click loss outranks modeled headroom. Use `scripts/score_opportunities.py` for reproducible CSV scoring; read `references/data-contract.md` before preparing its input.

Without GSC, rank by observable severity and confidence, but do not invent click headroom.

### 4. Select the intervention

- Choose a title/description test for high impressions, page-one visibility, and weak CTR.
- Choose a surgical content update for decay, factual drift, broken references, or lost clicks.
- Choose content expansion for positions 5–20 where intent is only partially satisfied.
- Choose a new article only for demonstrated demand that no existing canonical page owns.
- Route an overlapping proposed topic to the existing owner page; never create cannibalizing content.
- Drop or defer pages where demand is absent and no strategic or conversion value exists.

### 5. Draft with bounded authority

Prefer small, reviewable changes: one metadata replacement, one exact phrase/link swap, or one clearly scoped section. Ground product claims and code samples in current first-party documentation; attach a source URL to every code snippet.

Gate new drafts on:

1. Strategy: real audience, intent, content cluster, and business relevance.
2. Structure: direct answer/TL;DR, descriptive headings, scannable explanation, and next step.
3. Provenance: supported claims and traceable code examples.
4. Cannibalization: no existing page already owns the target intent.

Allow at most two repair attempts after a failed gate, then stop and report the failure.

### 6. Protect production writes

Give the agent no CMS write or publish tool. Persist suggestions with before-state hashes. Present Approve/Edit/Skip to a human in the team's existing workflow. On approval, let a tested server-side handler re-fetch and revalidate the current content, authorization, invariants, and draft conflicts before writing.

Only consider unattended fixes for deterministic, reversible cases such as filling an empty metadata field from an approved value or replacing a dead link with a verified canonical successor. Keep an audit log and rollback value.

### 7. Influence the sources you do not own

Separate the market into what the organization owns—website, commercial pages, content, documentation, and technical foundations—and what it can only influence—reviews, communities, publications, directories, videos, and independent comparisons.

For each priority commercial query or prompt, record which third-party sources repeatedly appear, which brands they include, and whether the target brand is accurately represented. Prioritize opportunities on two dimensions: frequency across commercially valuable results and likely influence on buyer consideration.

Earn inclusion through useful original data, quotable expert commentary, strong review profiles, transparent comparison evidence, legitimate publisher relationships, and genuine community participation. Do not recommend fake accounts, undisclosed paid endorsements, review manipulation, or low-quality listicle placement.

### 8. Measure causally

At publication, save the page's prior 28-day metrics and site-wide metrics over the same dates. Re-read at +28 and +56 days. Compare page change with the site-wide change so a general algorithmic or seasonal lift is not misattributed.

For new pages, record a zero-baseline growth curve: indexing, impressions, ranking queries, clicks, conversions, AI citations, and AI referrals at +28/+56 days.

Track AEO as separate layers:

- Crawl/discovery: can answer engines access and understand the page?
- Citation: is the domain/page cited for a stable prompt set?
- Referral: do users click through from answer engines?

Do not treat AI referral traffic as proof of citation, or citation as proof of conversion.

Treat prompts as a portfolio rather than a handful of spot checks. For each stable prompt set, track presence, position, recommendation strength, description accuracy, sentiment, citations, and competitors. Use weak results diagnostically: inspect the owned-page, evidence, review, and third-party-source gaps that may explain the difference.

### 9. Deliver an actionable report

Produce:

1. Executive summary and data limitations.
2. Evidence table with URL, observed issue, source, confidence, and severity.
3. Ranked queue with primary lever, rationale, recommended change, owner, and success metric.
4. Content-gap plan with target intent, evidence of demand, canonical owner, sources, and cannibalization result.
5. Search-market map with owned coverage, external influence sources, competitor presence, and commercial priority.
6. Measurement plan with baseline and +28/+56 checkpoints.
7. Automation design only when requested, including approval and rollback boundaries.

Use `references/report-template.md` for the report schema. Keep observed facts distinct from modeled estimates.

## Cost and quality controls

Run metadata, link, indexability, traffic-delta, and terminology checks broadly. Ration expensive document-to-page factual verification to the highest-opportunity pages plus a rotating sample. Never flag drift from model memory.

Favor first-party sources. For technical topics, cite official documentation or source code. Preserve locale boundaries and avoid recommending English content that duplicates a localized canonical strategy.
