# Trigger Self-Test — adaptive-opponents

> environment: fallback_self_test; no independent sub-agent. This is route-consistency evidence, not a blind-host result.

- TP 4 / FP 0 / FN 0 / TN 2
- precision 1.000 / recall 1.000 / F1 1.000
- sibling confusion 0/1
- critical negative failures: 0

| case | expected | selected | verdict |
|---|---|---|---|
| ao-pos-01 | should_trigger | adaptive-opponents | TP |
| ao-pos-02 | should_trigger | adaptive-opponents | TP |
| ao-pos-03 | should_trigger | adaptive-opponents | TP |
| ao-neg-01 | should_not_trigger | wanming-router | TN |
| ao-sib-01 | sibling | limited-info-multipov | OK |
| ao-boundary-01 | should_trigger | adaptive-opponents | TP |
