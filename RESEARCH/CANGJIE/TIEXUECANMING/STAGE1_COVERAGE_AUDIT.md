# 《铁血残明》Cangjie Stage 1 — Source-Coverage Audit

> Source bound: user EPUB V3.0 / chapters 1–534 as present; 535 is header-only.  
> Scope: Stage 1 **raw extraction coverage**, **not Stage 1.5 verified capabilities**.

## 1. Extraction status and reproducibility

Source EPUB SHA256: `9100bbcdb9f52bcd5458cbda92e16b646489efbc00df5161ed568ebac83ffbaf`

- Original five extractor instructions re-read before extraction.
- Environment has **no independent Task sub-agent execution tool**. Used documented **serial fallback** with five distinct extractor roles.
- Mechanical pass over **all EPUB chapter-text records** plus focused manual review of selected segments; no claim of complete independent semantic reading by five separate agents.
- Built local text index to identify candidate passages across each book range. The index and full copyrighted novel are **not committed** to the public repository.
- Each raw candidate records `source_chapter`, `source_locator` (physical `Text/chapterNNN.html`), short `source_quote` and mapped `task_ids`.
- Quote strings locally checked for literal presence in the recorded EPUB chapter; maximum stored excerpt length **30 Chinese characters**. Literal quote match validates **location only**, not methodological interpretation.
- Some proposed frameworks/principles are reconstructed **narrative methods** from fictional events, not explicit author teaching; these remain **unverified** until Stage 1.5.

## 2. Raw candidate counts

| Extractor file | Raw records | Verification status |
|---|---:|---|
| `candidates/frameworks.md` | **35** | raw only |
| `candidates/principles.md` | **35** | raw only |
| `candidates/cases.md` | **35** | raw fictional narrative cases |
| `candidates/counter-examples.md` | **23** | narrative counterexamples/inferred writing risks |
| `candidates/glossary.md` | **26** | proposed contextual terms |
| **Total** | **154** | **0 tri-verified** |

Case entries explicitly carry `example_kind: fictional_narrative_scene`; they are **not** real-world firsthand cases. The counterexample file distinguishes inferred narrative-writing failures from an author's explicit admonition.

## 3. Source span and coverage limitations

- Candidate-anchoring chapters/physical locators: **42** distinct chapters.
- First volume range 1–129: **15** chapter labels supporting candidate records.
- Second volume range 130–386: **17** chapter labels.
- Third partial volume range 387–534: **10** chapter labels.
- The full 1–534 range was searched/indexed and sampled by major task/theme, but **42 of 534 uniquely anchored chapters is not a chapter-by-chapter semantic exhaustive scan**. This distinction is a hard limitation, especially for full-scan framework/principle extractors.
- EPUB chapter numbering defects (135 and 197 repeated, 406–407 absent as independent entries, NCX mistakes) require using physical locator rather than chapter number alone.

### Required before claiming Stage 1 fully covered

1. Further **chunk-by-chunk framework full scan** across lightly reviewed chapter ranges, explicitly searching for single-location mechanisms and across-chapter arcs.
2. Further **chunk-by-chunk principle full scan**, including exceptional rules/footnotes beyond the sampled chapters.
3. Case/counterexample/glossary retrieval expansion where new terms and boundary cases show that a chapter window was too narrow.
4. Confirm 18-task coverage by source **sufficiency**, not just topic-tag membership.
5. Cross-check selected quotes in their **narrative surroundings**; a matching short phrase can still support the wrong inference.

Current extractors are valuable but **Stage 1 source-completeness gate remains OPEN**. Do not proceed to Stage 1.5 as if the five full scans are exhaustive.

## 4. Stage 0 independent task → raw candidate audit

Counts are memberships: one candidate may map to multiple tasks. Membership is **not** a coverage-pass decision.

| Stage 0 task | Raw mapped entries | Preliminary state | Attention |
|---|---:|---|---|
| TX-T01 底层行动资格 | 12 | raw candidate present | verify formal/actual authority separation |
| TX-T02 公门职位／私利／程序 | 21 | raw candidate present | clarify historically grounded vs fictional |
| TX-T03 义举话语与自利反差 | 7 | raw candidate present | character motive inferred; check against context |
| TX-T04 多阶层地方危机 | 12 | raw candidate present | compare opposing local positions |
| TX-T05 危机后资源再分配 | 7 | raw candidate present | at least one specific downstream result |
| TX-T06 人情到组织职位 | 21 | raw candidate present | verify role / resource / responsibility chain |
| TX-T07 组织规模与成本 | 22 | raw candidate present | no real-world budget inference |
| TX-T08 家庭／劳力／日常后果 | 12 | raw candidate present | ordinary people need independent motives |
| TX-T09 外部与基层自主视角 | 14 | raw candidate present | verify information access |
| TX-T10 旧交与新职位 | 12 | raw candidate present | dual loyalties, status and speech |
| TX-T11 金融信用与交易成本 | 28 | raw candidate present | fiction, not real financial SOP |
| TX-T12 宣传／声望第三方反应 | 14 | raw candidate present | reception may contradict intent |
| TX-T13 普通人群像／讽刺 | 22 | raw candidate present | preserve dignity, absurdity, dialogue |
| TX-T14 地方功劳到朝廷再定价 | 22 | raw candidate present | verify political context separately |
| TX-T15 多位置有限信息长事件 | 7 | raw candidate present | comparatively light, expand |
| TX-T16 执行偏差和组织自利 | 14 | raw candidate present | verify subordinate genuinely alters outcome |
| TX-T17 历史旁注／编者年表／正文证据等级 | **1** | **INSUFFICIENT / HIGH PRIORITY** | only one indirect principle, not a full source-classification method |
| TX-T18 已有文本／缺失终局 | 4 | raw candidate present | do not infer full-novel resolution |

### Critical attention

**TX-T17 is not satisfied merely because one `task_ids` mapping exists.** It requires explicit cross-check of EPUB front matter (reader-generated timeline), author text, in-story voices, and historical note provenance. A source-classification protocol might belong to V10 research infrastructure rather than a novel-derived execution skill.

**TX-T18 is a source audit fact**, not a novel method; preserve as scope boundary rather than promoting as active authored method.

## 5. Stage 1.5 risks already evident

- **Duplicate mechanisms** across framework, principle, case and negative case records; do not present 154 as unique abilities.
- **Weak short quotes**: some are only a scene entry sentence, not a complete method. V1 must check the full surrounding passage.
- **Generic steps in raw framework pool**: Stage 1 templates often use shared input/action/output language; Stage 1.5 must reconstruct genuine source-specific execution or demote to reference/needs_review.
- **Inferred warnings**: negative events in fiction are not automatically author-provided warnings or universal rules.
- **Copyright**: only short locators and original paraphrases belong in this public repo; no entire chapter extraction.
- **Safety**: do not turn descriptions of wartime actions into applicable weapons/combat instructions.

## 6. Stage conclusion

The **five raw candidate files are saved and individually GitHub back-read** with record counts matching 35+35+35+23+26.

**Stage 1 = extracted initial + supplementary pools; full semantic coverage audit not yet passed.**  
**Stage 1.5 = NOT STARTED.**  
**Runtime and Canon changes = NONE.**
