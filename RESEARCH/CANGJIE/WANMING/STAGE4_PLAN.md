# 《晚明》Cangjie Stage 4 — Pressure Test Plan

> 方法来源：Cangjie v2.5.0 `methodology/06-stage4-pressure-test.md`。  
> 本阶段不修改 V10 Runtime / Canon。

## 环境与可信度

当前环境**没有独立 sub-agent 原语**。因此本轮 Stage 4 只能按原方法允许的 fallback 路径，由主流程自测。

- 不能宣称“独立盲测”。
- 触发/路由与输出结果必须标记为 `fallback_self_test`。
- 可信度低于独立 sub-agent 盲测。
- 后续如获得干净 sub-agent，可直接复用本阶段 suites 做更高可信度复测。

## 子阶段

### 4A — 评测设计

1. 为 7 个 promoted 能力建立完整 trigger suite：
   - should_trigger: 3
   - should_not_trigger: 2（其中至少 1 条同书兄弟能力/来源 router 诱饵）
   - edge_case: 1
2. 为 13 个 router 能力建立 router reachability 用例：
   - 给出用户意图 prompt
   - 期望来源 router 命中唯一 capability card
   - 至少包含 1 条近邻混淆用例
3. 为 20 个 active 能力各建立：
   - 1 个正常 output case
   - 1 个边界/缺输入 output case
4. 固定 `split_seed=42`，`train_ratio=0.6`。

### 4B — 触发 / 路由压力测试

- promoted：测试是否准确触发，诱饵容错为 0。
- router：测试 `wanming-router` 能否到达正确卡，不得只证明“router 被触发”。
- promoted 与 router 必须有互斥近邻负例。
- 若 A2 描述导致混淆，回 Stage 2 修 A2/B，再把失败用例加入回归集。

### 4C — 实际输出压力测试

20 个 active 能力全部实际执行代表任务：
- 正常完成 20 个
- 边界/缺输入 20 个
- 计划总数 40 个

检查：
- 必需输入是否被尊重
- 缺失输入是否被标记而不是静默猜测
- 输出契约字段是否齐全
- 分支/停止条件是否生效
- 是否超出《晚明》来源能力边界
- 是否把人物观点误写成作者真理
- 是否出现危险的现实武器/作战操作内容（若出现则失败）

### 跨能力压力条件

1. **NR02 高效机器感**  
   对 `scale-restructure + power-contract + delegated-execution` 组合施压：
   - 输出必须保留执行偏差、利益分歧、监督成本或地方差异中的至少一项；
   - 不允许“制度设计正确 → 所有人自动准确服从”。

2. **NR01 资料说明量阈值**  
   对 `source-conflict-canon` 设负例：
   - 用户若问“正文应该放几段史料说明才不过载”，该能力必须明确**来源不足**，不得发明固定阈值。

## 通过标准

### promoted trigger
- should_not_trigger / sibling 诱饵：**0 容错**
- 其余用例：全部记录原始结果；不能用平均分掩盖关键负例失败

### router reachability
- 正常意图必须到达正确 capability
- 近邻意图必须到达相邻正确 capability，而非当前目标

### outputs
- 40 / 40 计划任务必须有实际结果；缺失计入分母
- 机械/结构断言先于语义判断
- 任一关键边界失败 → 回炉对应卡，再复测
- 没有独立 agent，因此即使全部通过，最终状态只能写：
  `PASS — fallback self-test; independent blind retest recommended`

## 交付

- `.cangjie/evals/promoted/*.json`
- `.cangjie/evals/router-reachability.json`
- `.cangjie/evals/output-cases.json`
- `.cangjie/evals/results/*.md|json`
- `STAGE4_RESULTS.md`
