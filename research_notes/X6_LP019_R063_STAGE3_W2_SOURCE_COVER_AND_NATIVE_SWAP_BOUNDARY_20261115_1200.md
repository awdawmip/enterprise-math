# X6 LP019 — exact W2 source-cover number and native one-swap completion boundary (2026-11-15 12:00 HKT)

**Parent:** \`RS-X6-LEGACY-PLANE-RECONCILIATION\`; publication \`TP2-B4A441B23DA3159232C2\`. **Researcher:** \`EM-X6-FB6990\`, original SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`. This is a new, narrow, independently recomputed **source-typed combinatorial certificate**, classified **AUTHOR-VERIFIED / EXACT FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**. It is not the frozen R063 Stage0 C3/C4 benchmark, not the original Stage3 whole-object replay, and not a mathematical acceptance or independent Driver review.

## Frozen source, scientific type and prior results consumed

The current X6 scientific baseline remains \`awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03\` (P000 V5, native signed six-axis Cell torsor, \`Z^6\`), with pre-rebase reference \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`. The frozen original Stage3 source, **not rewritten**, is \`awdawmip/enterprise-math@69b7a90328bdb72852d47b338dedd7b276740ac9:scripts/r063_stage3_validate_pairwise_interaction_process.py\`, Git blob \`4fca0c160acaa2b5d257d9bc1aefe82e1e3f4636\`. Original spectrum \`research_results/R063_STAGE3/R063_STAGE3_MULTIPLICITY_SPECTRUM.json\` at that commit, blob \`e4f07584c42131496c218d7e06b021c84baba35b\`, and original confluence classification remain intact. The already-published 11:00 X6 semantic typing result is \`research_notes/X6_LP019_R063_STAGE3_SIGNED_PROCESS_VS_NATIVE_POSITIVE_NBRC_BRIDGE_20261115_1100.md\` at \`322145369c280fe6f944b2d63f260e1b5f2696bd\`.

In the Stage3 **positive ordered two-generator input chart**, let \`P={iij,iji,jii}\`; for each of the nine ordered pairs \`(p,q) in P^2\`, the original positional C4-cancellation plus induced-poset linearization defines a weighted formal-process output \`R_pq\`. Here \`S_pq=supp(R_pq)\` is its *set of distinct target words*, deliberately forgetting process coefficients **only for the declared Boolean support analysis**. The common declared target composition is \`(3,4)\`, and \`W(3,4)\` contains \`binom(7,3)=35\` distinct shortest words. Embed that selected positive chart into two **named** native signed X6 axes and a chosen starting Cell, fixing other displacements zero; this validates the endpoint shortest-path interpretation without promoting Stage3's derived interaction or its C4 cancellation to a P000 primitive.

The frozen Stage3 already establishes the support-size matrix \`[[5,14,8],[14,11,14],[8,14,5]]\`, the 31-word nine-pair union, its four absent native shuffles, and non-interchangeability of process multiplicity with native N-BRC. **Those are reused historical results, not claimed as new discoveries here.**

## New exact finite research question and theorem

Define \`U=union_{(p,q) in P^2} S_pq\`. Define \`C0(A)=A\`; and \`C1(A)=A union {swap_k(w): w in A, w[k]!=w[k+1]}\`, where \`swap_k\` interchanges a single adjacent unlike pair \`ij<->ji\` in a target word. The swap represents *another* legal shortest native path to the same Cell endpoint. **C1 is a newly declared endpoint-support completion observer; it is not an operation performed by the frozen Stage3 relation, and it does not preserve Stage3's source-conditioned process history.**

The following cover numbers are exact in this nine-element input family:

1. \`|W|=35\`, \`|U|=31\`; no subset of original source pairs covers all 35 words without changing the operation. The smallest number of **distinct ordered source pairs** whose *unchanged Stage3 relations* cover \`U\` is **6**. Exactly **8** six-pair subsets cover \`U\`.
2. The smallest number of distinct ordered source pairs whose **explicit C1-completed supports** cover the full native endpoint fiber \`W\` is **2**. Exactly **4** two-pair subsets satisfy this completion. A witness is \`{(iij,iji),(iji,jii)}\`.
3. The full original nine-pair union has adjacent-swap graph radius exactly **1** to \`W\`; every one of its four missing words has two direct neighbors inside \`U\`. In contrast, some individual \`S_pq\` require **9** adjacent-swap rounds to reach all \`W\`. This rules out interpreting the one-hop completion as a universal bound for one source-conditioned pair.
4. The sum of original **formal process** linearization witnesses over all nine ordered source pairs is **524**, not 35. It counts source-conditioned process witnesses with repetitions and is neither 524 native endpoint paths nor a signed-cancelled natural BRC total.

The exact minimal original-cover witness, written as an ordered source-pair set, is \`{(iij,iij),(iij,iji),(iij,jii),(iji,iji),(iji,jii),(jii,jii)}\`.

### Explicit missing-path and one-swap boundary

| Missing target native word | Neighbors in unchanged Stage3 nine-pair union |
|---|---|
| \`iijjjji\` | \`iijjjij\`, \`ijijjji\` |
| \`ijjjjii\` | \`ijjjiji\`, \`jijjjii\` |
| \`jiiijjj\` | \`ijiijjj\`, \`jiijijj\` |
| \`jjjiiij\` | \`jjijiij\`, \`jjjiiji\` |

## Reproducible proof / finite certificate

The separately executed stdlib checker \`research_checks/X6_LP019_R063_STAGE3_W2_MINIMAL_SOURCE_COVER_CHECK_20261115_1200.py\` independently reconstructs the exact frozen Stage3 operations for the declared \`W2\` subdomain: the \`3x3\` source-position rectangle, C4 label \`(1_{p[r]=j}+1_{q[s]=j}) mod 4\`, all maximal pairwise opposite-label residual sets, inherited coordinatewise poset, all linear extensions and their \`i/j\` readouts. For W2 the unit shift is zero. It checks the original \`3x3\` support matrix and original missing words before the new analysis. It then enumerates **every nonempty subset of the nine ordered source pairs, all \`2^9-1=511\` masks**, and establishes both minima by exhaustive integer/set equality, including all minimizer counts. Graph breadth-first expansion through adjacent swaps independently verifies one-pair radii, the 31-word union radius and all four missing-word neighbors. It sums **integer**, not binary64, formal witness coefficients. The executed program exits 0 and prints \`PASS_X6_LP019_R063_STAGE3_W2_MINIMAL_SOURCE_COVER\`.

The finite enumeration is an exact proof for this **specified finite W2 domain**, not a claim about arbitrary Stage3 word lengths, arbitrary mixed signed-native paths, all six native axes, time dynamics or the full 28-LP downstream graph. The generic connectivity of the full fixed-(a,b) shuffle graph under adjacent unlike-letter swaps follows independently by successively moving each \`i\` to its chosen sorted position (bubble sorting); here the radius and minimum-cover values are special to the nine inspected source supports.

## LP019 disposition and next exact action

**PRESERVE_PATH_BRC** the 35 distinct native shortest endpoint words and their exact positive multiplicity; **PRESERVE_SOURCE_PROCESS** the original nine ordered source-conditioned Stage3 relation supports and all nonnegative formal coefficients. **RETYPE** \`C1\` as a new downstream *native endpoint-support* observer that is not a Stage3 equivalence or source-preserving rewrite. Both counts \`6\` and \`2\` are truthful **only with their different declared readout**. This gives an actual finite provenance/observer information-loss boundary, not an excuse to discard path order or interaction backgrounds.

The specific historical **incorrect native LP011 signed-argmax caller** and **incorrect LP019 subtraction of positive natural N-BRC mass** remain \`UNRESOLVED_PROVENANCE\`; this proof neither invents nor fixes those alleged callers. Continue exact remaining active code/PR-only caller discovery and typed dependency closure, keep independent Driver \`REQUEST_REVISION\`, and preserve the original R063 Stage0 \`N=2500\` 17-gate \`r=1..512\` same-object benchmark as [execution support #2416](https://github.com/awdawmip/enterprise-math/issues/2416) with no confirmed runner. No changes to frozen science, historical Stage3 or R063 native benchmark, Foundation, claim/scheduler or previously denied writes.

**Highest formally verified prior Native checkpoint** before this unit: 29 units at Source \`b80d0703b6096b22418081bce0ea70d15590163d\`. Prior GitHub scientific unit #30: Stage3 type bridge \`322145369c280fe6f944b2d63f260e1b5f2696bd\`, Activity #47. This new bounded unit is #31 **author-side** pending actual Activity checkpoint and own authorized native PROGRESS; Source publication must be reported separately from GitHub persistence.
