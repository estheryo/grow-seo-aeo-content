# SEO/AEO Skills

这个仓库收录用于 SEO 与 AI 搜索增长的可复用 Codex Skills，并持续根据新的原创文章、研究和实践报告迭代。

[English](README.md)

## Skills

### `grow-seo-aeo-content`

位于仓库根目录，用于运行一套可衡量的 SEO/AEO 内容增长闭环：

- 盘点和审计网站内容；
- 识别流量恢复、点击率、排名与内容缺口机会；
- 起草基于证据的小范围修改与新文章；
- 避免关键词和搜索意图互相竞争；
- 在人工审批和确定性校验后再发布；
- 在第 28 天和第 56 天衡量页面效果；
- 分别追踪 AI 抓取、引用、引荐流量与业务结果。

### `win-ai-search-citations`

位于 [`skills/win-ai-search-citations`](skills/win-ai-search-citations)，是一个单独的 Skill，用于提高网站在 Google AI、ChatGPT、Claude、Perplexity 等回答引擎中被发现、引用和推荐的机会。

它会：

- 建立真实买家问题和提示词集合；
- 记录不同回答引擎当前引用的网页；
- 对比获胜页面与目标页面的实体覆盖、证据段落和权威信号；
- 将问题映射到唯一的 canonical 页面；
- 创建“问题、直接回答、可验证事实、范围或日期、来源”组成的引用友好内容块；
- 补齐比较、替代方案、价格、用例、行业、实施、案例和文档等购买阶段；
- 分开衡量展现、引用、点击、线索和收入。

### `create-people-first-content`

位于 [`skills/create-people-first-content`](skills/create-people-first-content)，是一个独立的单篇内容质量 Skill，用于创建、审核和改写实用、可靠、以用户为中心的内容。

它会把以下要求转换成明确的发布门禁：

- 目标受众和读者任务；
- 证据、第一手经验与原创信息增量；
- 作者、审核者及内容生产方式；
- 事实核验、标题准确性和内容完整度；
- AI 生成内容的人类复核；
- 自动化摘要、追逐流量、虚假更新等“搜索引擎优先”风险。

## 安装

安装根目录的内容增长 Skill：

```bash
git clone https://github.com/estheryo/grow-seo-aeo-content.git ~/.codex/skills/grow-seo-aeo-content
```

调用方式：

```text
使用 $grow-seo-aeo-content 审计这个网站，排序 SEO/AEO 机会，并提出可衡量的内容计划。
```

如果还要安装独立的 AI 引用 Skill，可将其目录复制或链接到 Codex Skills 目录：

```bash
ln -s "$(pwd)/skills/win-ai-search-citations" ~/.codex/skills/win-ai-search-citations
```

调用方式：

```text
使用 $win-ai-search-citations 分析目标问题中已被 AI 引用的页面，并制定优先级明确的引用增长计划。
```

安装独立的“以用户为中心内容” Skill：

```bash
ln -s "$(pwd)/skills/create-people-first-content" ~/.codex/skills/create-people-first-content
```

调用方式：

```text
使用 $create-people-first-content 审核这篇文章，判断是否达到发布标准，并给出精确的修复清单。
```

## 来源文章

### `grow-seo-aeo-content`

- [How I built an SEO/AEO blog engine — Harsehaj 原始文章](https://harsehaj.substack.com/p/how-i-built-an-seoaeo-blog-engine)
- [如何在 2026 年赢得搜索（Google、AI 与其他渠道）— Jake Ward](https://x.com/jakezward/status/2093320636743512116)

详细的原则、结果、限制与影响范围记录在 [`references/sources.md`](references/sources.md)。

### `win-ai-search-citations`

- [厂商博客如何成为 AI 引用来源 — Alex Groberman](https://x.com/alexgroberman/status/2092607970274378041)
- [本地企业如何获得 Google 与 AI 搜索可见度 — Alex Groberman](https://x.com/alexgroberman/status/2092248243568865453)
- [Claude 如何发现、打开和引用来源 — Alex Groberman](https://x.com/alexgroberman/status/2091910002315518357)
- [通过 Search Console 衡量生成式 AI 可见度 — Alex Groberman](https://x.com/alexgroberman/status/2091554033949626719)
- [ChatGPT 引用研究解读 — Alex Groberman](https://x.com/alexgroberman/status/2091524620591739233)
- [Google Discovery Engine 机制解读 — Alex Groberman](https://x.com/alexgroberman/status/2012536184023462013)
- [对比回答引擎已经引用的获胜页面 — Jared Winger](https://x.com/BuildWithJared/status/2092718076479639713)

每篇来源具体影响了哪些规则，以及对来源中数字和推断的限制，记录在 [`skills/win-ai-search-citations/references/sources.md`](skills/win-ai-search-citations/references/sources.md)。

### `create-people-first-content`

- [什么是 Google HCU？如何创建实用、可靠、以用户为中心的内容 — Loki Yan SEO](https://x.com/loki_yan_seo/status/2094576318788833400)

采用的内容质量门禁、Google 官方资料核验以及未采纳的推测性结论，记录在 [`skills/create-people-first-content/references/sources.md`](skills/create-people-first-content/references/sources.md)。

来源管理默认遵循以下规则：

1. 只保留作者的 canonical 原始链接，并移除跟踪参数；
2. 如果 X 帖子只是转发作者的站外长文，则只保存站外原始文章，不重复保存 X 链接；
3. 区分已观察事实、来源报告、作者推断和 Skill 建议；
4. 记录每次新增来源具体修改了哪些规则；
5. 保留不同来源之间的重要分歧和不确定性。

## 安全边界

Skill 可以读取、评分、验证和起草，但不应直接获得 CMS 生产发布权限。重要内容由人工审批，并在写入前通过服务端程序重新校验当前状态。

## License

Apache License 2.0。
