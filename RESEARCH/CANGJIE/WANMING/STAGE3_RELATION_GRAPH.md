# 《晚明》Cangjie Stage 3 — Capability Relation Graph

> 原则：只记录真实的 depends-on / contrasts-with / composes-with，不为“网络看起来完整”强行加边。  
> 当前 active capabilities: 20；关系边: 24。

| # | A | 关系 | B | 说明 |
|---:|---|---|---|---|
| 1 | `actionability-ladder` | composes-with | `success-constraints` | 每一级行动资格兑现后，成功会自然生成下一层责任与约束。 |
| 2 | `actionability-ladder` | composes-with | `scale-restructure` | 个人行动力扩大成组织力量后，规模变化会触发结构重构。 |
| 3 | `learning-loop` | composes-with | `institution-transfer-pilot` | 制度试点暴露问题后，需要反馈—筛选—规则修改闭环吸收经验。 |
| 4 | `scale-restructure` | composes-with | `power-contract` | 重构决定需要哪些岗位；权力契约把岗位落到职责、资源和问责。 |
| 5 | `scale-restructure` | composes-with | `delegated-execution` | 结构重构只有配合真实授权，才能摆脱主角亲力亲为。 |
| 6 | `scale-restructure` | composes-with | `decentralized-pilot` | 地域型瓶颈是规模重构的一种特例，常需要地方分权试点。 |
| 7 | `scale-restructure` | composes-with | `structural-conflict` | 新结构重新分配权力资源，会自然生成内部与外部阻力。 |
| 8 | `information-triage` | composes-with | `delegated-execution` | 信息先分流到正确决策层，再由专业岗位执行，形成完整处理链。 |
| 9 | `power-contract` | composes-with | `resource-power-rebalance` | 只有先知道原始权力合同，才能判断资源升值后哪些权限需要拆分。 |
| 10 | `power-contract` | composes-with | `delegated-execution` | 授权执行必须建立在明确职责、资源、边界与问责之上。 |
| 11 | `decentralized-pilot` | composes-with | `institution-transfer-pilot` | 地方分权本身可作为一种有限制度试点，二者共享试点与回收逻辑。 |
| 12 | `adaptive-opponents` | composes-with | `limited-info-multipov` | 有限视角规定对手知道什么，适应性对手据此更新判断。 |
| 13 | `adaptive-opponents` | composes-with | `success-constraints` | 主角成功会改变外部角色估价，成为成功后二阶约束的一部分。 |
| 14 | `success-constraints` | composes-with | `aftermath-settlement` | 成功的新约束应进入事件后果矩阵，而不是只做抽象提醒。 |
| 15 | `success-constraints` | composes-with | `resource-power-rebalance` | 组织成功让资源升值时，新的寻租与拆权问题就是典型二阶约束。 |
| 16 | `success-constraints` | composes-with | `structural-conflict` | 成功扩大权力资源后，会触发既有群体利益结构的反应。 |
| 17 | `micro-life-dashboard` | composes-with | `macro-micro-rhythm` | 生活仪表盘提供具体内容，宏观—微观节奏决定它何时进入长篇。 |
| 18 | `micro-life-dashboard` | composes-with | `aftermath-settlement` | 事件余波可通过家庭、教育、劳动等生活指标落地。 |
| 19 | `macro-micro-rhythm` | composes-with | `repeat-by-delta` | 生活线反复出现时，应通过差值而不是重新完整解释来维持时间感。 |
| 20 | `limited-info-multipov` | composes-with | `aftermath-settlement` | 大事件结束后，可沿不同受影响位置继续结算后果。 |
| 21 | `public-memory-recoding` | composes-with | `relationship-multiaxis` | 终局公共叙述可以与老关系当事人的私人记忆形成反差。 |
| 22 | `relationship-multiaxis` | composes-with | `structural-conflict` | 结构性利益变化会只改变关系的部分轴，而不必把关系整体清零。 |
| 23 | `resource-power-rebalance` | composes-with | `structural-conflict` | 拆权本身会让既得利益受损，从而产生新的结构性冲突。 |
| 24 | `source-conflict-canon` | contrasts-with | `public-memory-recoding` | 前者追求作者侧事实一致，后者刻意呈现后世传播对事实的变形。 |

## 审计

- 关系数：24
- 超过 25 条警戒线：否
- source-conflict-canon 与 public-memory-recoding 为明确对比关系，其余为组合关系。
- 未发现必须建立的强制单向 depends-on；实际执行前置条件已保留在各卡 E/B 中。
