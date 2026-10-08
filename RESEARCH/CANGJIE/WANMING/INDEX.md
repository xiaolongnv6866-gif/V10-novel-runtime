# 《晚明》Cangjie Research Index

> 状态：Cangjie Stage 0–5 已完成仓库交付；V10 Runtime/Canon 未修改。

## 1. 来源与审计

- [SOURCE_AUDIT.md](./SOURCE_AUDIT.md) — EPUB 来源、哈希、正文规模与来源边界
- [BOOK_OVERVIEW.md](./BOOK_OVERVIEW.md) — Stage 0 整书骨架、批判与关键任务
- [coverage-audit.md](./coverage-audit.md) — WM-T01–T15 覆盖与实际交付路径
- [needs-review.md](./needs-review.md) — 尚未解决的来源缺口
- [references.md](./references.md) — reference 层及实际去向

## 2. Stage 1–1.6

- [candidates/](./candidates/) — framework / principle / case / counter-example / glossary 原始候选
- [verified.md](./verified.md) — Stage 1.5 的 20 个 verified canonical 单元
- [STAGE1_5_SUMMARY.md](./STAGE1_5_SUMMARY.md)
- [STAGE1_6_PROMOTION_REVIEW.md](./STAGE1_6_PROMOTION_REVIEW.md)

## 3. Stage 2–3

- [.cangjie/capabilities/verified.yaml](./.cangjie/capabilities/verified.yaml) — Capability Bundle 唯一编译事实源
- [.cangjie/capabilities/cards/](./.cangjie/capabilities/cards/) — 20 张 RIA++ 能力卡
- [GLOSSARY.md](./GLOSSARY.md)
- [STAGE2_SUMMARY.md](./STAGE2_SUMMARY.md)
- [STAGE3_RELATION_GRAPH.md](./STAGE3_RELATION_GRAPH.md)
- [STAGE3_SUMMARY.md](./STAGE3_SUMMARY.md)

## 4. Stage 4

- [STAGE4_PLAN.md](./STAGE4_PLAN.md)
- [STAGE4B_TRIGGER_ROUTER_SUMMARY.md](./STAGE4B_TRIGGER_ROUTER_SUMMARY.md)
- [STAGE4_RESULTS.md](./STAGE4_RESULTS.md)
- [.cangjie/evals/](./.cangjie/evals/) — suites、结果与评测设计审计

Stage 4 最终状态：
- promoted trigger route-consistency：42 / 42
- router reachability：26 / 26
- actual output tasks：40 / 40
- cross-capability stress：2 / 2
- 环境限制：fallback self-test；未获得独立 sub-agent 盲测

## 5. Stage 5

- [STAGE5_OUTPUT_DECISION.md](./STAGE5_OUTPUT_DECISION.md) — 原始 Cangjie auto 决策
- [DIGEST.md](./DIGEST.md) — 人类读者精华长文
- [dist/wanming/SKILL.md](./dist/wanming/SKILL.md) — 正式 single 可发现入口
- [dist/wanming/references/](./dist/wanming/references/) — 20 能力卡、overview、glossary、cheatsheet、capability-index
- [dist/wanming/BUILD_MANIFEST.json](./dist/wanming/BUILD_MANIFEST.json)
- [BUILD_AUDIT/](./BUILD_AUDIT/) — 编译/显式 validator 日志与文件哈希
- [STAGE5_SUMMARY.md](./STAGE5_SUMMARY.md)
- [FINAL_SNAPSHOT.md](./FINAL_SNAPSHOT.md)

## 6. 仍未进入 V10 Runtime

本目录是 `RESEARCH/CANGJIE/WANMING`。  
《晚明》能力即使已经通过 Cangjie 压力测试，也不能自动覆盖 `RUNTIME/CORE.md`。

下一层是 V10 自己的候选晋级评审：比较现有 Runtime、去重、确定候选归宿，再按照 V10_SKILL 的晋级链继续测试。
