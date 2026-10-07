# Trigger Self-Test — limited-info-multipov

> environment: fallback_self_test; no independent sub-agent. This is route-consistency evidence, not a blind-host result.

- TP 4 / FP 0 / FN 0 / TN 2
- precision 1.000 / recall 1.000 / F1 1.000
- sibling confusion 0/1
- critical negative failures: 0

| case | expected | selected | verdict |
|---|---|---|---|
| mp-pos-01 | should_trigger | limited-info-multipov | TP |
| mp-pos-02 | should_trigger | limited-info-multipov | TP |
| mp-pos-03 | should_trigger | limited-info-multipov | TP |
| mp-neg-01 | should_not_trigger | aftermath-settlement | TN |
| mp-sib-01 | sibling | adaptive-opponents | OK |
| mp-boundary-01 | should_trigger | limited-info-multipov | TP |
