# 《晚明》Cangjie Stage 4B — Trigger / Router Self-Test Summary

> environment: **fallback_self_test**  
> 当前环境无独立 sub-agent，因此本结果不是独立盲测，只证明当前描述与路由在主流程自测中保持一致。

## Promoted trigger

7 / 7 promoted entrypoints 完成，每个 6 条：

| target | TP | FP | FN | TN | F1 |
|---|---:|---:|---:|---:|---:|
| adaptive-opponents | 4 | 0 | 0 | 2 | 1.000 |
| micro-life-dashboard | 4 | 0 | 0 | 2 | 1.000 |
| limited-info-multipov | 4 | 0 | 0 | 2 | 1.000 |
| scale-restructure | 4 | 0 | 0 | 2 | 1.000 |
| aftermath-settlement | 4 | 0 | 0 | 2 | 1.000 |
| institution-transfer-pilot | 4 | 0 | 0 | 2 | 1.000 |
| source-conflict-canon | 4 | 0 | 0 | 2 | 1.000 |

- total trigger cases: 42
- critical negative false positives: 0
- sibling confusion failures: 0
- pre-run eval corrections are recorded in `.cangjie/evals/EVAL_DESIGN_AUDIT.md`

## Router reachability

- router capabilities covered: 13 / 13
- total reachability cases: 26
- correct capability reached: 26 / 26
- near-neighbor cases: 13
- near-neighbor failures: 0

## Limitation

Because the same main process designed and ran the tests, these results are lower-confidence than a clean sub-agent blind run. They must not be described as independent-host validation.

## Next

Run Stage 4C actual output self-test:
- 20 normal tasks
- 20 boundary / missing-input tasks
- frozen assertions from `.cangjie/evals/output-cases.json`
