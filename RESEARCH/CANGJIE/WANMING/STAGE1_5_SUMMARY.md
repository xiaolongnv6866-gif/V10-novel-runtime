# 《晚明》Cangjie Stage 1 / 1.5 Summary

## 执行状态

- Stage 0：用户已确认进入下一阶段。
- Stage 1：完成。
- Stage 1.5：完成，等待用户轻确认。
- Stage 1.6 以后：尚未开始。
- V10 Runtime：未修改。

## Stage 1 原始候选池

| extractor | 数量 | 产物 |
|---|---:|---|
| framework | 18 | `candidates/frameworks.md` |
| principle | 17 | `candidates/principles.md` |
| case | 13 | `candidates/cases.md` |
| counter-example | 10 | `candidates/counter-examples.md` |
| glossary | 15 | `candidates/glossary.md` |
| **合计** | **73** |  |

当前环境没有独立 sub-agent，按 Cangjie 原 SKILL 的降级路径串行执行五个 extractor；每个候选保留独立职责边界，提交前回原 EPUB 抽取章节核对短引文。

## Stage 1.5 三重验证

### verified：20 个 canonical 能力单元

1. `wm-v01` 行动资格逐级兑现
2. `wm-v02` 反馈—筛选—规则修改的组织学习闭环
3. `wm-v03` 规模触发的组织重构
4. `wm-v04` 信息分流与决策优先级
5. `wm-v05` 职责—资源—问责的权力契约
6. `wm-v06` 方向上收、专业执行下放
7. `wm-v07` 中央瓶颈后的地方分权与试点
8. `wm-v08` 适应性对手与世界反馈
9. `wm-v09` 成功同时生成收益与新约束
10. `wm-v10` 微观生活仪表盘与社会成本穿透
11. `wm-v11` 宏观任务线与日常生活线交替
12. `wm-v12` 多位置有限信息拼接重大事件
13. `wm-v13` 高潮后的后果持续结算
14. `wm-v14` 制度移植的试点—缺口—争论—修订循环
15. `wm-v15` 重复场景只展开差值
16. `wm-v16` 终局的公共记忆再编码
17. `wm-v17` 长期关系的多轴状态演化
18. `wm-v18` 冲突史料的作者侧裁决与 Canon 固化
19. `wm-v19` 资源升值后的基层权力再拆分
20. `wm-v20` 用权力与资源结构碰撞生成冲突

每项均在 `verified.md` 中记录：原始候选映射、来源位置、V1 理由、V2 新输入 walkthrough、V3 具体任务增益。

### reference

- `c01–c13`：保留为 A1 / 来源案例。
- `ce01–ce10`：保留为 Boundary / 失败模式素材。
- `g01–g15`：保留到后续 `GLOSSARY.md`。
- `p16`：来源充分，但独立任务过窄，作为岗位/关系能力的参考边界，不单列 active 能力。
- Stage 0 的“高效机器感”与“资料说明过载”批判保留为压力测试边界，不冒充作者方法。

### needs_review

1. **NR01：史料如何进入正文而不形成说明过载**  
   已验证“史料冲突 → 作者裁决 → Canon 固化”；但原书没有给出可执行的说明量阈值，不能用模型常识补成规则。
2. **NR02：成熟组织的高效机器感何时伤害人物性**  
   这是对文本的批判性判断，不是作者明确方法；仅作为 Stage 4 压力条件。

### rejected

- 本轮无“无原文依据 / 错误归因”的彻底淘汰项。
- 重复内容通过 canonical merge 去重，没有因为“不值得独立成 Skill”而错误丢弃。

## Coverage 硬门

Stage 0 的 15 个关键任务均有可追踪去向；其中：

- WM-T01 / 02 / 03 / 05–13 / 15：有 verified 能力覆盖。
- WM-T04：保留为多能力组合 + glossary/reference；没有把小说中的具体军工、军制、财务数字包装成现实操作方法。
- WM-T14：**部分完成**。史料冲突裁决已 verified；“资料说明量控制”仍为 needs_review，因此不能宣称该任务完整蒸馏。

## 下一门槛

按 Cangjie v2.5 流程，当前必须先得到用户对 Stage 1.5 四类分流的轻确认；确认后才能进入 Stage 1.6 独立 Skill 晋级门。
