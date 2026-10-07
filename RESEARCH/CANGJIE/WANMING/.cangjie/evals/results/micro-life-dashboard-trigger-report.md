# Trigger Self-Test — micro-life-dashboard

> environment: fallback_self_test; no independent sub-agent. This is route-consistency evidence, not a blind-host result.

- TP 4 / FP 0 / FN 0 / TN 2
- precision 1.000 / recall 1.000 / F1 1.000
- sibling confusion 0/1
- critical negative failures: 0

| case | expected | selected | verdict |
|---|---|---|---|
| ml-pos-01 | should_trigger | micro-life-dashboard | TP |
| ml-pos-02 | should_trigger | micro-life-dashboard | TP |
| ml-pos-03 | should_trigger | micro-life-dashboard | TP |
| ml-neg-01 | should_not_trigger | wanming-router | TN |
| ml-sib-01 | sibling | wanming-router | OK |
| ml-boundary-01 | should_trigger | micro-life-dashboard | TP |
