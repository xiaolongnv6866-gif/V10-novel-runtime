# 2026-10-08 — 《晚明》候选能力双臂盲测 A/B 评估

## 测试输入

Raw answer attachment SHA256:
- Baseline answer: `ccfb7908174ef18f64aa84f8c7528779c95ef0dcd4836e12075d23adececaa19`
- Candidate answer: `6df73fa7416fcd077b4669a916527345a8ec773dc442e5d230d92688eda06272`

- Arm A: Baseline 临时会话答卷
- Arm B: Candidate 临时会话答卷
- 评分协议：`TESTS/WANMING_CANDIDATE_BLIND_PROTOCOL.md`
- 隐藏评分表：`TESTS/WANMING_CANDIDATE_BLIND_SCORING.md`

两份答卷均声明未使用旧聊天、Memory 或外部资料；Baseline 明确未获得 Overlay，Candidate 明确按低于 Canon/Runtime 的测试候选层使用 Overlay。

## Gate 1 — 标准 V10 40题 non-regression

Evaluator result:

- Arm A Baseline: **40 / 40**
- Arm B Candidate: **40 / 40**
- fatal Canon errors: 0
- Candidate regression: **NONE**

结论：Gate 1 PASS。

## Gate 2 — 候选专项 20题

评分：0 / 1 / 2。

| Q | Baseline | Candidate | 说明 |
|---:|---:|---:|---|
| 1 | 2 | 2 | 两组都区分钱与公开调遣权，并要求有限授权桥梁 |
| 2 | 2 | 2 | 两组都拒绝无症状预设多层官僚 |
| 3 | 1 | 2 | Baseline 有基层事实和复测，但缺“异议/淘汰建议”显式闭环；Candidate 明确证据筛选、矛盾意见、采纳/不采纳及下一轮验证 |
| 4 | 2 | 2 | 两组都能识别真授权与配角复读主角答案的区别 |
| 5 | 1 | 2 | Baseline 会分层与核实，但未完整锁定“紧急/重要 + decide/delegate/record/verify + 重要不紧急不被挤出”；Candidate 完整 |
| 6 | 2 | 2 | 两组都保持外部角色的信息边界与合理误判 |
| 7 | 2 | 2 | 两组都能从资源升值检查旧权力合同，而非直接道德化 |
| 8 | 2 | 2 | 两组都能从具体损失生成差异化阻力 |
| 9 | 2 | 2 | 一户只代表一条因果路径，不代表全社会 |
| 10 | 2 | 2 | 两组都避免把所有生活戏工具化 |
| 11 | 2 | 2 | 两组都删除/合并冗余 POV，并保留信息渠道 |
| 12 | 2 | 2 | 两组都能多维检查余波并选择进入场景的后果 |
| 13 | 2 | 2 | 两组都严格区分作者知识与陈启明知识；Candidate 更结构化但 Baseline 已完整执行 |
| 14 | 2 | 2 | 两组都拒绝“第一次试点失败=制度错误” |
| 15 | 1 | 2 | Baseline 已会比较史料并保留未知，但未完整写出“采用后写入 Canon + 受影响文本扫描”的正式协议；Candidate 完整 |
| 16 | 2 | 2 | 无原始来源就不凭记忆裁决 |
| 17 | 2 | 2 | 无持续状态变化就不强写余波 |
| 18 | 2 | 2 | 无具体损失就不强套结构利益冲突 |
| 19 | 2 | 2 | 两组都保留幽默、关系、生活连续性的非工具化价值 |
| 20 | 2 | 2 | 两组短场景均合格；Candidate 不弱于 Baseline |

Totals:

- Arm A Baseline: **37 / 40**
- Arm B Candidate: **40 / 40**
- delta: **+3**
- mandatory Q2/Q6/Q13/Q15/Q19/Q20: Candidate 全部 > 0
- Gate 2 threshold 38/40: **PASS**

## Gate 3 — A/B incremental value

Overall:
- Candidate >= Baseline: **PASS**
- Candidate standard V10 regression: **NONE**
- anti-overuse probes Q2/Q10/Q17/Q18/Q19/Q20: **no regression**
- prose Q20: **equal-or-better / PASS**

真正产生可测增益的只有三处：

1. **C01 组织学习闭环** — Q3 从 1 → 2
2. **C03 信息分流与决策优先级** — Q5 从 1 → 2
3. **P01 冲突史料裁决→Canon** — Q15 从 1 → 2

其余 12 项虽然来源层有价值、开放测试也通过，但 Baseline Runtime 已经能在盲测中给出满质量答案；继续把它们全部写入 Runtime 会增加规则密度而没有可证明增益。

## Gate 4 — 15项最终处置

| candidate | final disposition | reason |
|---|---|---|
| V10-WM-C01 组织学习闭环 | **PROMOTE_MERGE** | Baseline Q3 不完整；Candidate 明确增加异议/筛选/采纳与复测闭环 |
| V10-WM-C02 规模触发组织重构 | REFERENCE_ONLY | Q2 两组均2；现有 Runtime 已可靠阻止无症状官僚化 |
| V10-WM-C03 信息分流与决策优先级 | **PROMOTE_MERGE** | Baseline Q5 不完整；Candidate 增加稳定的信息入口与决策层边界 |
| V10-WM-C04 专业执行下放 | REFERENCE_ONLY | Q4 两组均2；现有 A2/B4/F4 已足够 |
| V10-WM-C05 微观生活仪表盘 | REFERENCE_ONLY | Q9/Q20 两组均满分；留作正文技法与来源证据 |
| V10-WM-C06 高潮后多维结算 | REFERENCE_ONLY | Q12/Q17 两组均满分；现有 A4/A5/C1 足以恢复 |
| V10-WM-C07 制度移植试点循环 | REFERENCE_ONLY | Q13/Q14 两组均满分；F1/F3/F4 已能稳定产生同等判断 |
| V10-WM-C08 资源升值后的权力再拆分 | REFERENCE_ONLY | Q7 两组均满分；无需新增默认规则 |
| V10-WM-S01 行动资格检查器 | REFERENCE_ONLY | Q1 两组均满分；G1/G2/G4 已足够 |
| V10-WM-S02 权力契约五要素 | REFERENCE_ONLY | Q1/Q4 两组均满分；作为作者侧检查工具保留即可 |
| V10-WM-S03 适应性世界闭环 | REFERENCE_ONLY | Q6 两组均满分；A1/H1/H2 已可靠恢复 |
| V10-WM-S04 生活线反向影响主线 | REFERENCE_ONLY | Q10/Q19 两组均满分，且现有 Runtime 已避免过度工具化 |
| V10-WM-S05 多位置有限信息矩阵 | REFERENCE_ONLY | Q11 两组均满分；保留为规划工具 |
| V10-WM-S06 权力资源结构冲突 | REFERENCE_ONLY | Q8/Q18 两组均满分；C3/G1 已能独立推出 |
| V10-WM-P01 冲突史料裁决→Canon | **PROMOTE_PROTOCOL** | Q15 从 1→2；V10_SKILL 当前确实缺完整的冲突史料→Canon 工作协议 |

## 最终结论

《晚明》15项候选没有全部晋级。

盲测后只晋级 **3项**：
- 2项以紧凑方式合并进现有 Runtime；
- 1项进入 V10_SKILL / Canon research protocol；
- 其余12项留在 RESEARCH/reference/tool 层。

这正符合 V10 的目标：吸收来源能力，但不让 Runtime 因规则堆叠越来越复杂。

## Runtime merge specification

### Merge 1 — A5 组织失败经验
在 A5 后追加：
当失败属于组织任务时，经验不能只留在主角脑中；应保留基层事实与异议，经筛选后把采纳项写入岗位/流程/规则，并在下一次相似任务中验证，不要求所有人当场一致。

### Merge 2 — H1 组织信息入口
在 H1 后追加：
成熟组织的信息不得把主角当总收件箱；区分紧急/重要、可委派/需裁决/待核实。未核实消息保持未核实，中间层可整理和建议，但不能偷替上层完成价值取舍。

## V10_SKILL protocol specification

增加“冲突史料裁决”协议：
- 分开记录各来源明确声称；
- 区分直接记载/后世转述/推断/缺失；
- 只比较有依据的证据，不发明权重；
- 结论只能采用A/采用B/保持未知；
- 若采用，写入 Canon 并记录弃用版本与受影响文本；
- 新证据出现时走正式修订；
- 无来源文本不得凭模型记忆裁决。
