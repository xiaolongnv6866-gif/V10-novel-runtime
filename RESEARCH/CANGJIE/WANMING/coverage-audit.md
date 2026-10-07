# 《晚明》Coverage Audit — Stage 1.5

| task_id | 原书关键任务 | 候选/能力去向 | 判定 | 审计说明 |
|---|---|---|---|---|
| WM-T01 | 低身份→行动力 | wm-v01 | verified | 完整覆盖：资源/身份/人员逐级兑现 |
| WM-T02 | 个人能力→组织能力 | wm-v02, wm-v04, wm-v06 | verified | 反馈闭环、信息分流、专业执行 |
| WM-T03 | 规模升级/授权/监督 | wm-v03, wm-v05, wm-v07, wm-v19 | verified | 含规模瓶颈、职责契约、地方试点、寻租修正 |
| WM-T04 | 财政—产业—人口—军队闭环 | wm-v05 + g08/g10/g11/g12/g13 | partial/reference | 原书有大量系统联动证据，但本轮未将具体军工/财务数值规则包装成通用能力；通过权力契约与术语网络保留 |
| WM-T05 | 独立世界/适应性对手 | wm-v08, wm-v20 | verified | 对手更新判断 + 权力结构冲突 |
| WM-T06 | 成功制造新约束 | wm-v09, wm-v19, wm-v20 | verified | 收益、暴露、寻租、既有结构反应 |
| WM-T07 | 普通生活仪表盘 | wm-v10 | verified | 正向改善与伤亡成本双向证据 |
| WM-T08 | 宏观/家庭/幽默节奏 | wm-v11 | verified | 跨卷结构验证；幽默本身未独立 skill 化 |
| WM-T09 | 多视角大事件 | wm-v12 | verified | 有限信息多位置拼接 |
| WM-T10 | 事件后果持续结算 | wm-v13, wm-v10 | verified | 人员/资源/政治/家庭余波 |
| WM-T11 | 制度移植试点与妥协 | wm-v07, wm-v14 | verified | 地方治理试点 + 司法失败学习 |
| WM-T12 | 重复场景写差值 | wm-v15 | verified | 跨卷重复簇支持 |
| WM-T13 | 长期关系状态演化 | wm-v17 + p16 reference | verified | 信任/职位/利益/价值分歧多轴 |
| WM-T14 | 史料进入正文 | wm-v18 + NR01 | partial/needs_review | 史料冲突裁决已验证；说明量控制缺来源规则 |
| WM-T15 | 终局公共记忆回看 | wm-v16 | verified | 终章茶馆与英雄章节形成完整机制 |

## 硬门结论

- critical/high 任务均有候选与明确去向。
- WM-T04 保留为“系统联动参考 + 多能力组合”，未把小说内具体数值/军制包装成现实方法。
- WM-T14 只有“史料冲突裁决”达到 verified；“资料说明量控制”明确留在 needs_review，**因此本轮不得宣称《晚明》的资料入文能力已经完整蒸馏**。


## Stage 3 实际交付路径

| 内容类别 | 实际交付位置 | 状态 |
|---|---|---|
| 20 个 verified 能力 | `.cangjie/capabilities/verified.yaml` + `cards/*.md` | 已交付 |
| c01–c13 案例 | 对应能力卡 A1 / 来源证据 | 已交付 |
| ce01–ce10 反例 | 对应能力卡 B / 失败处理 | 已交付 |
| g01–g15 术语 | `GLOSSARY.md` + `.cangjie/capabilities/book/glossary.md` | 已交付 |
| p16 岗位契合边界 | `BOOK_OVERVIEW.md#Stage-3-保留参考映射` | 已交付为 reference，不升 active |
| 高效机器感批判 | `BOOK_OVERVIEW.md#Critical` + Stage 4 压力条件 | 保留 |
| WM-T14 资料说明量阈值 | `needs-review.md#NR01` + Overview | **未解决，不伪装交付** |
| 整书 overview | 根目录 `BOOK_OVERVIEW.md` + Bundle `book/overview.md` | 已同步 |
| 能力关系图 | `STAGE3_RELATION_GRAPH.md` + Bundle `also_read` | 已交付 |

### WM-T14 状态保持

`source-conflict-canon` 已解决“冲突史料如何裁决并固定小说 Canon”；  
**“资料该在正文放多少才不过载”仍然没有来源完整的可执行规则，因此 coverage 继续保持 partial/needs_review。**
