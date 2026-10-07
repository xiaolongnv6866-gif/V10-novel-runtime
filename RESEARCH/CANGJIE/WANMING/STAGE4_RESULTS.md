# 《晚明》Cangjie Stage 4 — Pressure Test Results

> Final status: **PASS — fallback self-test; independent blind retest recommended**  
> 环境没有独立 sub-agent / 干净上下文，因此不得把本结果描述成独立盲测或比较性非劣证明。

## 4A — 评测设计

- promoted trigger suites: 7 / 7
- router reachability capabilities: 13 / 13
- router reachability cases: 26
- output cases: 40（20 normal + 20 boundary）
- pre-run / post-run 测试修订全部记录在 `.cangjie/evals/EVAL_DESIGN_AUDIT.md`

### 设计修订审计

1. 初稿 normal output 断言过弱，正式执行前加强为 E 段 3–5 个关键字段；
2. upstream scorer 把 `edge_case` 当 non-trigger，正式执行前将“能力应触发并执行边界判断”的边界例改为 `should_trigger`；
3. source-conflict 的“无来源文本”本应触发并停止，因此正式执行前用真正无关请求替换负例；
4. 首轮 output score 37/40，三项失败被判定为**测试缺陷**：有充分信息的负向结论被错误要求 `needs_input|out_of_scope`。按方法规则修测试，不改已有输出，再评分 40/40。

## 4B — Trigger / Router

### Promoted trigger

7 个 promoted 能力，每个 6 条：
- 4 should-trigger
- 1 true negative
- 1 sibling / router confusion test

结果：
- 42 / 42 路由判定符合预期
- 总 FP: 0
- 总 FN: 0
- sibling confusion failures: 0
- 每个 promoted F1: 1.000

> 仅为 main-process route-consistency self-test，不是 blind-host score。

### Router reachability

- 13 / 13 router capability covered
- 26 / 26 reachability cases correct
- 13 / 13 near-neighbor cases correct

## 4C — Actual Outputs

- planned: 40
- completed: 40
- normal: 20 / 20
- boundary / missing-input: 20 / 20
- final audited assertions: **40 / 40 pass**
- first score before test repair: 37 / 40
- outputs edited after first score: **no**
- comparative `without_skill` clean-context run: **unavailable in current host**
- therefore no improvement / non-inferiority claim

### Boundary behavior

Verified that capabilities can:
- surface missing inputs rather than silently guess;
- return a valid “do not restructure / remove redundant POV / do not force aftermath” decision when information is sufficient;
- stop at source boundary instead of inventing rules.

## Cross-capability stress

### NR02 — 高效机器感

PASS.

组合 `scale-restructure + power-contract + delegated-execution` 时仍保留：
- execution deviation
- interest conflict
- supervision cost
- local variation

没有输出“制度设计正确 → 所有人自动服从”。

### NR01 — 资料说明量阈值

PASS as boundary preservation.

`source-conflict-canon` 明确拒绝发明“正文固定放几段史料”的数字规则。该缺口继续留在 `needs-review.md#NR01`。

## Safety / source integrity

- no weapon/combat operational instructions compiled
- no character political view promoted as universal truth without mechanism evidence
- no model-memory source completion for historical conflicts
- no V10 Runtime / Canon modification

## Stage 4 conclusion

知识层、产品化路由层、执行契约层和主要边界在当前环境的 fallback self-test 中全部通过。

**允许进入 Stage 5，但最终交付必须继续保留限制说明：独立 sub-agent 盲测尚未完成。**
