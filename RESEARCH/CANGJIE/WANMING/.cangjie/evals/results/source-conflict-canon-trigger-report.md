# Trigger Self-Test — source-conflict-canon

> environment: fallback_self_test; no independent sub-agent. This is route-consistency evidence, not a blind-host result.

- TP 4 / FP 0 / FN 0 / TN 2
- precision 1.000 / recall 1.000 / F1 1.000
- sibling confusion 0/1
- critical negative failures: 0

| case | expected | selected | verdict |
|---|---|---|---|
| sc-pos-01 | should_trigger | source-conflict-canon | TP |
| sc-pos-02 | should_trigger | source-conflict-canon | TP |
| sc-pos-03 | should_trigger | source-conflict-canon | TP |
| sc-neg-01 | should_not_trigger | none | TN |
| sc-sib-01 | sibling | wanming-router | OK |
| sc-boundary-01 | should_trigger | source-conflict-canon | TP |
