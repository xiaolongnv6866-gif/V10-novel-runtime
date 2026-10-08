# V10 Index v0.1

这是当前最小索引。随着正式正文与蒸馏结果进入仓库，本文件将扩展为可检索入口。

## 启动必读

1. `../V10_SKILL.md`
2. `../RUNTIME/CORE.md`
3. `../CANON/MASTER_SETTING.md`
4. `../CURRENT/PROJECT_STATE.md`

## 当前关键主题定位

### 主角与穿越
- `CANON/MASTER_SETTING.md` §3, §8, §10
- `RUNTIME/CORE.md` §F

### 崇祯与初见
- `CANON/MASTER_SETTING.md` §4
- `RUNTIME/CORE.md` §B, §H

### 南阳 / 唐王府
- `CANON/MASTER_SETTING.md` §5, §7
- `CURRENT/PROJECT_STATE.md` 当前前期方向

### 1641 / 1644 / 1649–1652 时间线
- `CANON/MASTER_SETTING.md` §2, §9

### 人物与关系
- `RUNTIME/CORE.md` §B

### 情节与长期因果
- `RUNTIME/CORE.md` §A, §C

### 叙事与文笔
- `RUNTIME/CORE.md` §D

### 爽点与商业可读性
- `RUNTIME/CORE.md` §E

### 财政 / 军队 / 权力
- `RUNTIME/CORE.md` §G

### 历史改变与国际世界
- `RUNTIME/CORE.md` §H

## 未来索引要求

正式正文进入后，至少需要支持按以下维度回查 Canon：

- 章节 / 场景
- 人物
- 地点
- 日期
- 势力
- 事件
- 人物知道/不知道的信息
- 钱粮与军事资源
- 伏笔 / 未解决状态
- 技术与生产
- 读者已知而人物未知的信息

索引只负责定位，不得取代原文事实。


### 《晚明》Cangjie / V10 候选晋级
- `RESEARCH/CANGJIE/WANMING/INDEX.md` — 《晚明》Cangjie Stage 0–5 全部蒸馏产物入口
- `RESEARCH/CANGJIE/WANMING/FINAL_SNAPSHOT.md` — Cangjie 定版快照
- `RESEARCH/V10_CANDIDATES/WANMING.md` — 20→15 候选去重与 Cluster A–D 测试状态
- `RESEARCH/V10_CANDIDATES/WANMING_CANDIDATE_OVERLAY.md` — 盲测专用候选 Overlay，非 Runtime
- `TESTS/WANMING_CANDIDATE_BLIND_PROTOCOL.md` — 双臂盲测协议
- `TESTS/WANMING_CANDIDATE_BLIND_TESTS.md` — 候选盲测20题
- `TESTS/WANMING_CANDIDATE_BLIND_SCORING.md` — 评测者专用评分表，不得交给被测会话
- `TESTS/WANMING_CANDIDATE_BLIND_RUNBOOK.md` — 两个干净 Temporary Chat 的运行说明
- `TESTS/results/2026-10-08-wanming-candidate-ab-blind-evaluation.md` — 双臂盲测正式评分、15项最终处置与晋级记录
- `TESTS/bundles/V10-wanming-baseline-blind-v0.1.zip` — Baseline 盲测包
- `TESTS/bundles/V10-wanming-candidate-blind-v0.1.zip` — Candidate 盲测包

当前状态：**双臂盲测已通过；3项完成最小晋级，12项留在 reference/tool 层；Canon 未修改。Runtime 已升级为 v0.2，V10_SKILL 已升级为 v0.2.0。**

### 《铁血残明》Cangjie 蒸馏
- `RESEARCH/CANGJIE/TIEXUECANMING/README.md` — 研究入口
- `RESEARCH/CANGJIE/TIEXUECANMING/SOURCE_AUDIT.md` — EPUB 1–534 章节范围、版本与缺口
- `RESEARCH/CANGJIE/TIEXUECANMING/BOOK_OVERVIEW.md` — Stage 0 整书理解（六层结构与 18 个关键任务）
- `RESEARCH/CANGJIE/TIEXUECANMING/PIPELINE_STATE.md` — 恢复断点
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_SUMMARY.md` — 五提取器154条原始候选
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_COVERAGE_AUDIT.md` — 初版来源覆盖审计（154条）
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_COVERAGE_UPDATE_2026-10-08.md` — 197条时的历史原始候选来源审计
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_SEMANTIC_BATCH_03.md` — 第33—80章连续区间6章全文/42章定向审读，新13条候选
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_SEMANTIC_BATCH_02.md` — 最新第1—32章审读与15项新增候选
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_REVIEW_BACKLOG.md` — 下一轮逐块审读范围与严格完成条件
- `RESEARCH/CANGJIE/TIEXUECANMING/QA/validate_stage1_candidates.py` — 可重复执行的字段校验器
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_SCHEMA_REPAIR_AUDIT.json` — 237条字段校验与12条旧错位记录修复
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_SEMANTIC_BATCH_01.md` — 31章定向语义补读记录与222条时的旧原始候选
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_T17_PROVENANCE_REVIEW.md` — 84项注释/年表来源分层复核
- `RESEARCH/CANGJIE/TIEXUECANMING/STAGE1_CHAPTER_SCAN_MATRIX.tsv` — 532物理章题机械扫描矩阵
- `RESEARCH/CANGJIE/TIEXUECANMING/candidates/` — frameworks/principles/cases/counter-examples/glossary 五份源绑定提取文件

当前：**Stage 0 用户已确认；Stage 1 已保存250条原始候选，严格字段校验通过，仍须补足全量语义覆盖；Stage 1.5–5 未开始。**

### 双书蒸馏验收标准校正（2026-10-08）
- `RESEARCH/CANGJIE/CROSS_BOOK_STAGE1_PARITY_AUDIT_2026-10-08.md` — 《晚明》与《铁血残明》Stage 1 源覆盖口径不一致的正式审计与返工要求。
- **《晚明》Stage 5 编译交付已完成，但 Stage 1 全量语义覆盖的可审计证明不足，待追溯复核。** 《铁血残明》Stage 1 仍未过全量语义覆盖门。严禁以原始候选数量或测试通过率代替完整来源覆盖。
