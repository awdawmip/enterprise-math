# R030 Research Context Compiler — Meta-tool Injection Backtest

Researcher-ID: `EM-R030-CX8F42`  
Task: `RS-R030-RESEARCH-CONTEXT-COMPILER-METATOOL-INJECTION-BACKTEST`  
Taskbook source: `db9958cc006cacc32d5b30cd1a9a35594543a8d1`  
Status: `RESEARCH / NOT CANONICAL`

## 1. Decision

Return class:

`CONTEXT_COMPILER_NARROWLY_USEFUL / EXACT_TOOL_CHANNEL_POSITIVE / MINIMUM_CRITICAL_COVER_DOMINATES / COLD_START_REDISCOVERY_REDUCED / META_TOOL_INJECTION_CANDIDATE / NOT_CANONICAL`

Driver recommendation: `ADOPT_NARROW`.

A deterministic task-relative Context Pack is worth becoming a formal researcher startup companion artifact, **after** the reasoning registry is reconciled to R029. It must not replace TASKBOOK or COMMON SURFACE, and it must not default to an all-matches tool dump.

## 2. Layer separation

The implementation preserves four distinct layers:

- `TASKBOOK`: task-specific problem contract and authority.
- `COMMON SURFACE`: accepted reusable knowledge router.
- `REASONING REGISTRY`: typed reusable reasoning operators and diagnostic lenses.
- `CONTEXT PACK`: deterministic task-relative compiled working context.

The pack is derived from the task signature, registry and relevant pinned sources. It is not hand-maintained and therefore is not a second taskbook.

## 3. Task Semantic Signature

The compiler derives or accepts an inspectable signature containing object types, carrier types, semantics, current observable, future language, future horizon, claim mode, minimality scope, composition requirement, resource-comparison flag, equal-semantic-contract requirement, evidence targets, dependencies, exclusions, semantic facts, risk flags and explicit unknown fields.

Unknown carrier/future/evidence information remains `UNKNOWN`; the compiler does not silently invent it.

## 4. EXACT vs DIAGNOSTIC

`EXACT_REQUIRED` is selected only from structured signature facts/risk capabilities, declared dependencies and accepted evidence obligations. Keyword matches cannot place a tool in this channel.

`DIAGNOSTIC_SUGGESTED` may use auxiliary textual triggers, but it is not theorem evidence. Interpretive ontology/philosophy lenses are confined to this channel.

This separation survived adversarial fixtures where naive substring matching falsely read the tail of `Boolean` as `Lean`, and where `no Boolean result-support` was initially misread as a positive carrier declaration. The repaired parser uses token boundaries and negation-aware extraction.

## 5. Deterministic selection

Three strategies are implemented:

`ALL_MATCHES`, `TOP_K`, and `MINIMUM_CRITICAL_COVER` (`MCC`).

MCC solves an exact weighted set-cover problem over structured required capabilities. Objective order is deterministic: minimum estimated injected tokens, then minimum tool count, then lexicographic tool IDs. Broadly related tools cannot substitute for a typed capability they do not actually cover.

The compiler also records selected reasons, omitted tools/reasons, known non-implications, source pointers, context budget, unknown fields, relevant common-surface digest and a tamper-detectable context digest.

## 6. Historical replay design

Historical replay uses R017, R020, R022, R023, R023I, R024, R025 and R028.

Gold construction is deliberately asymmetric to avoid hindsight leakage:

- startup semantic fixtures are independently curated from the original taskbooks;
- later returns/current accepted boundaries are used only to label post-hoc critical distinctions and score coverage;
- late factual answers are **not** injected into the signature or selected-tool input.

There are 23 post-hoc critical distinctions. Nineteen were already explicit in the original startup taskbooks, so they are calibration/precision cases rather than rediscovery wins. Four were genuinely late relative to startup context.

The four late distinctions are:

1. R023I: a successful build claim must actually cover the new load-bearing module.
2. R023I: source provenance is not compiler/root-coverage evidence.
3. R025/R027: a numerical `r >= 2^p` threshold does not remove p-power-aligned islands; regime classification must cross threshold with alignment structure.
4. R025/R027: `k=0` is a degenerate/exact regime and invalidates blanket binary-doubling strengthening without a positive-support scope.

For R025 the pack does **not** inject those answers. It injects `REGIME_EXHAUSTION`, whose kill-test axes require threshold equality, alignment subregimes and zero/degenerate states, plus evidence/horizon guards. Therefore the recovery credit belongs to the research action, not to an answer leak.

## 7. Frozen backtest metrics

Under the common pre-catalog representation used for the strategy sweep:

- critical distinctions: `23`
- startup-explicit: `19/23 = 82.6%`
- genuinely late: `4`
- MCC critical recall: `23/23 = 100%`
- MCC recovered late: `4/4 = 100%`
- MCC strict gold-hit-density lower bound: `23/43 = 53.5%`
- MCC selected tools across eight tasks: `43`
- MCC estimated tool injection: `3,706 tokens`
- MCC mean generated human startup pack: `~1,098 tokens/task`
- MCC structural overload: `0`
- MCC diagnostic wrong-route risk: `0`

The 53.5% value is deliberately named a **strict gold-hit-density lower bound**, not universal relevance precision. The gold enumerates critical distinctions, not every legitimate task obligation; e.g. prior-art rooting and bounded-minimality guards can be valid without owning a gold row.

A later representation-only compaction moved common registry contract fields and long source strings into registry-level defaults/source catalog. It did not change selected tools, recall, late recovery, overload or wrong-route risk; the four committed sample human packs average about `950` estimated tokens/task. The adoption decision is nevertheless reported against the conservative frozen pre-compaction cost above.

## 8. Context-budget Pareto

Frozen strategy sweep:

| strategy | recall | tools | tool tokens | mean human pack | structural overload | wrong-route risk |
|---|---:|---:|---:|---:|---:|---:|
| MCC | 1.000 | 43 | 3,706 | ~1,098 | 0 | 0 |
| TOP_K=1 | 1.000 | 65 | 5,629 | ~1,257 | 25 | 16 |
| TOP_K=2 | 1.000 | 70 | 6,034 | ~1,302 | 30 | 26 |
| TOP_K=3 | 1.000 | 73 | 6,268 | ~1,327 | 33 | 32 |
| TOP_K=5/8 | 1.000 | 77 | 6,664 | ~1,352 | 37 | 41 |
| ALL_MATCHES | 1.000 | 77 | 6,664 | ~1,353 | 37 | 41 |

MCC is the unique nondominated point under the frozen objective. ALL_MATCHES buys no additional critical recall or late recovery, but injects 34 additional tools and about 2,958 additional estimated tool tokens.

Therefore:

`MORE_CONTEXT_ALWAYS_IMPROVES_RESEARCH = KILLED`

`ALL_RELEVANT_TOOLS_SHOULD_ALWAYS_BE_INJECTED = KILLED`

`A_HIGH_RECALL_PACK_IS_GOOD_EVEN_IF_NOISY = KILLED`

## 9. Required distinctions reproduced

The registry/compiler explicitly represents the taskbook’s targeted distinctions:

- static correctness != dynamically reusable state;
- one-step exact != composition-safe;
- Boolean support != count != provenance;
- branch selector/token != full semantic state;
- declared future != realized future/suffix;
- bounded/declaration-class minimality != global minimality;
- resource Pareto claims require equal semantic contracts;
- current coarse equality != suffix-safe recoalescence;
- finite exhaustive evidence != universal proof;
- source provenance != module coverage evidence;
- exact certificate validity != heuristic search quality;
- causal != predictive != retrospective relevance.

## 10. Keyword attack

Six adversarial keyword fixtures all pass after parser repair. A naive keyword baseline selected 17 extra tools across those fixtures. This kills `KEYWORD_SELECTION_IS_ENOUGH`.

Critical channel selection is capability-driven; text triggers may only augment diagnostic suggestions.

## 11. Mutation sensitivity

Ten mutations all changed the pack in the required direction:

- remove carrier declaration;
- Boolean support -> N-count/provenance;
- one-step -> arbitrary finite words;
- declared future -> realized trace;
- bounded -> global minimality;
- build PASS while actual module coverage becomes unconfirmed;
- equal semantic contract -> cross-contract resource comparison;
- add low-evidence interpretive lens;
- finite evidence -> universal claim;
- remove suffix horizon.

The interpretive-lens mutation affects only `DIAGNOSTIC_SUGGESTED`, not `EXACT_REQUIRED`.

## 12. Freshness and audit

The context digest depends on the task semantic digest, reasoning-registry digest, **relevant common-surface slice**, and selected pinned source identities.

An unrelated common-surface mutation leaves the pack digest stable. A relevant A4 BRC validation mutation changes it. Thus:

`GLOBAL_REPOSITORY_MOVEMENT_MUST_INVALIDATE_EVERY_CONTEXT = KILLED`.

Tamper audit detects digest changes, and omitted candidates/uncovered capabilities are emitted as `meta_tool_delta` feedback rather than auto-promoting tools.

## 13. Meta-tool delta for R029

Four compiler failures produced concrete registry feedback:

1. evidence-grade triggers need token-boundary parsing, not substring containment;
2. carrier declarations need polarity/negation fixtures;
3. broad relatedness cannot satisfy a specific typed obligation such as actual module coverage or declared/realized split;
4. generic counterexample generation and exhaustive regime partitioning are composable but not interchangeable.

The compiler is forbidden from auto-promoting a tool, changing R029 trust class, or keeping a tool killed by R029 merely to preserve metrics.

## 14. Validation

Focused validation completed:

- Python `py_compile`: PASS;
- focused `unittest`: `15/15 PASS`;
- CLI `compile`: PASS;
- CLI `inspect`: PASS;
- CLI `audit`: PASS;
- CLI `backtest`: PASS;
- keyword adversarial suite: PASS;
- mutation suite: `10/10 PASS`.

The full repository suite was not run because the local execution container could not resolve GitHub for a clone; repository reads/writes used the GitHub connector. This is not represented as repo-wide validation. CI is not required for this research task.

## 15. R029 state

R029 was checked during execution and again at the final freshness gate. No R029 owner return/PR/registry was found, while Enterprise Math `main` remained at the R030 source commit.

Therefore this task ships an explicit `SEED_REGISTRY_NOT_R029_FINAL` registry. Before promotion, if R029 has returned, R030 must remap semantic equivalents to R029 IDs/trust classes, remove any R029-killed tools, and rerun the backtest. Metrics must not be preserved by retaining a killed seed tool.

## 16. Final answer to the taskbook

Yes: task-relative compiled context is worth becoming a formal startup companion artifact, but only narrowly:

`TASKBOOK authority + COMMON SURFACE routing + R029 reasoning registry + MCC-compiled Context Pack`.

Do not adopt hand-maintained packs, global all-context dumps, keyword-only selection, or interpretive lenses as facts.

This R030 artifact is `NOT_CANONICAL`; it makes no common-surface rewrite and requests Driver review/promotion separately.
