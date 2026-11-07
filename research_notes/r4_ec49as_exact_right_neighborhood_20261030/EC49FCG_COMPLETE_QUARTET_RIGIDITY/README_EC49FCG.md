# EC49FCG — complete four-slot local rigidity (2026-11-06)

**Author-side finite proof and exact computation. Independent Driver admission is pending.**
Researcher: `EM-DIRECT-8D4E4E`; activity `RA-14527A8F32903D475238FC9D`. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original source: [frozen exact model](../EC49FCF_EARLY1_LATE3_150/frozen_model.py), inherited from `VERIFY_EC49FBY.py` at `5b10f1c296cb8826d4b69f6fd83dba89d765df1c`.

## Theorem and exact domain

Let `W` be the fixed 24-path, 158-nonempty-prefix witness in the frozen nine-state DFA over `acdefg`. The two H2/H3 roots remain fixed. The H4–H9 slots have ten early and ten late observation-signature addresses. Candidate paths must preserve the original slot length, complete positive BRC key `L=(4,2,1)` or `M=(7,3,2)`, and the observed signature. Prefix identity retains ordered **signed native X6 primitive steps**. For **every** four-element subset of these twenty slots, the minimum number of distinct prefixes across the unchanged and replaced paths is exactly **158**.

The earlier author-side units EC49FBZ–EC49FCF covered 4,165 distinct four-slot subsets. This EC49FCG computation covers the remaining disjoint 680. Thus all `C(20,4)=4,845` four-slot subsets are covered by the cited finite certificates. The present run alone proves the remaining 680.

| Additional family (one early slot in each) | Sets | Raw candidate products | Actual final union checks | Minimum |
|---|---:|---:|---:|---:|
| H8+H8+H9 | 120 | 24,068,524,032,000 | 601,150 | 158 |
| H7+H8+H8 | 240 | 18,051,393,024,000 | 887,100 | 158 |
| H7+H8+H9 | 320 | 16,387,080,192,000 | 2,042,352 | 158 |
| **Total** | **680** | **58,506,997,248,000** | **3,530,602** | **158** |

## Exact argument

Fix four slots `S`. Let `F` be the signed prefix union of the other twenty original paths. For a legal word at slot `s`, let `R_s=P(word)\F`, where `P(word)` retains every nonempty primitive prefix. The cost is `|F|+|R_1 ∪ R_2 ∪ R_3 ∪ R_4|`. Put `d=158-|F|`.

A strict improvement requires the total residual union cardinality `<d`. All candidates with residual size `>=d` can be discarded; the same holds for any partial union of size `>=d`. Identical residual sets may be deduplicated **for this fixed cost/observer**, without identifying their source paths in other contexts. Reindexing the active set of signed prefixes by a bijection preserves all union cardinalities.

For two especially large H7+H8+H8 cases (family indices 208,209, zero-based), let `X=R_1∪R_2`, `k=|X|`. Any strictly improving completion must satisfy `|R_3\X|<=d-1-k` and `|R_4\X|<=d-1-k`. The verifier checks these necessary conditions for **every** remaining candidate in each slot before exact four-way union evaluation; exclusions are exhaustive and sound. All other 678 sets use direct three-level prefix-monotonicity pruning and exhaustive fourth unions. Every set produces no cost below 158; retaining its original witness attains 158.

## Evidence / replay

The [executed verifier](VERIFY_EC49FCG.py) imports the published frozen model, enumerates all 680 sets in three disjoint families, and writes exact per-group JSON records. Run the five commands in its docstring; the 240- and 320-case families are split to keep Python execution bounded. All five ranges were executed in the research environment; their output JSONs were combined and checked for 680 distinct sets, exact minima and raw search counts. The 680-row certificate has SHA-256 `045b84678ed043c5007c6850a12157fa6875826466529a0a14469205f6004267`; compressed SHA-256 `64da0e6b9befad04def3f04571e22d26cd53bab4ca8f749076eb480baf854df5`. Summary data is in [EC49FCG_SUMMARY.json](EC49FCG_SUMMARY.json). Re-running the commands regenerates the full row-level certificate.

The theorem concerns the fixed keys, signatures, roots and exactly four replacement slots. Five-slot coordinated changes, alternative cache-key schedules and the 93-prefix mother target are the next research units. An independent Driver should inspect the frozen generator, the necessary-extension pruning and a sample signed-prefix trace before mathematical admission.
