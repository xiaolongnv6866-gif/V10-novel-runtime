# 《铁血残明》Cangjie Research — Research Only

本目录保存对用户提供的《铁血残明》EPUB 的正式 Cangjie 蒸馏研究，**不是 V10 Runtime / Canon**。

## 当前进度

- 已完成 V10 v0.2.0 仓库恢复
- 已按原始 Cangjie 2.5 方法执行 Stage 0
- 已完成来源审计与 `BOOK_OVERVIEW.md`
- **Stage 0 已获用户确认；Stage 1 五类候选共154条已保存，但全量语义覆盖硬门仍未通过；Stage 1.5–5 未开始**

## 入口

- [SOURCE_AUDIT.md](./SOURCE_AUDIT.md)
- [BOOK_OVERVIEW.md](./BOOK_OVERVIEW.md)
- [PIPELINE_STATE.md](./PIPELINE_STATE.md)
- [STAGE1_SUMMARY.md](./STAGE1_SUMMARY.md)
- [STAGE1_COVERAGE_AUDIT.md](./STAGE1_COVERAGE_AUDIT.md)
- [candidates/](./candidates/)

## 重要范围限定

这份 EPUB 标注 V3.0，正文只到第534章，第535章只有标题标记，无法据此谈全书结局。

前置年表为贴吧读者编纂，不是作者正文。章号/目录有编辑缺陷，来源定位应带物理章节路径，参见 SOURCE_AUDIT。

出于版权保护，公开仓库不提交 EPUB、全文转写、章文 JSONL 或块索引。正文抽取底稿保留在本地工作区。

## 后续严格流程

Stage 0 已确认 → Stage 1 覆盖补扫 → Stage 1.5 三重验证及轻确认 → Stage 1.6 晋级门 → Stage 2 RIA++ → Stage 3 链接 → Stage 4 压力测试 → Stage 5 编译/交付 → V10 候选晋级流程。

每完成独立可验收子阶段立即更新本目录并回读核验；不直接修改 Runtime/Canon。
