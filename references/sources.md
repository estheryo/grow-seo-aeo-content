# Source registry

This registry records the material used to evolve the skill. It preserves provenance without copying full copyrighted articles into the repository.

## Registered sources

### SRC-001 — How I built an SEO/AEO blog engine

- Author: Harsehaj
- Published: 2026-08-22 on Substack; shared as an X article/thread on 2026-08-24
- Canonical long-form version: https://harsehaj.substack.com/p/how-i-built-an-seoaeo-blog-engine
- X version: https://x.com/harsehaj/status/2091690736211112005
- Relationship: The X and Substack URLs are two presentations of the same underlying article, not independent corroborating sources.
- Context: A first-person implementation report about BlogEO, built during a Browserbase growth-engineering internship.
- Principles incorporated:
  - Rank audit work by recoverable clicks, CTR headroom, and ranking headroom rather than content age alone.
  - Separate broad cheap checks from rationed, expensive document-level factual verification.
  - Generate new content from demonstrated search demand and block keyword cannibalization.
  - Give the agent no production write tool; use human approval and a deterministic server-side handler.
  - Store page and site-wide baselines and re-read outcomes at +28 and +56 days.
  - Track AI discovery/crawl, citation, and referral as separate AEO layers.
  - Put approval and reporting inside the team's existing workflow rather than another dashboard.
- Reported outcomes: The author reported 18 generated posts, 50+ edits, 5.8× search-impression growth, 9.8× page-one-query growth, and average blog position improving from 10.9 to 6.6. Treat these as project-specific observations, not expected results.
- Limitations reported: Opportunity estimates are soft; crawl measurement was deferred; expensive fact checking was rationed; AI citation data relied on manual CSV export.
- Skill areas influenced: opportunity scoring, generation gates, publishing safety, measurement, AEO layers, cost controls, and weekly operating cadence.

## Adding a source

Assign the next `SRC-NNN` identifier and record:

- title, author, publication date, and canonical URL;
- mirrors or reposts and their relationship to the canonical source;
- source type and implementation context;
- principles incorporated, rejected, or held as alternatives;
- reported outcomes and explicit limitations;
- exact skill files or rules changed.

Prefer links and concise synthesis. Do not archive full article text unless its license explicitly permits redistribution and doing so materially helps the skill.
