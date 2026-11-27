# Stage236–239: four all-real exact optimal segments (external N14 IID)

2026-10-28. Author-side portable research, `AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED`. No native Result/CLAIM or Driver acceptance.

## Frozen authority and scope

GLOBAL_KNOWLEDGE_V1 `main@4faffbe68584637f37d630e345543a8f7300f394`; Enterprise Math source control `main@f01fb212f8d640ebced88b2dc836b52f4d933596`; P000 protected original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; parent Stage235 proof is at Draft PR #1571 immutable commit `28bbde8127bacdc6d28473855ff6903e49a7c480`.

The external model has observations X_i i.i.d. under `P=(3,1,20)/24` or `Q=(2,2,20)/24`. A randomized sequential policy chooses a stopping time T≤14 and one of labels P/Q based on its entire ordered observation history and private coins. Set `eP=Pr_P(decide Q)`, `eQ=Pr_Q(decide P)`, `tP=E_P T`, `tQ=E_Q T`; define

`V14(alpha)=inf{max(tP,tQ): eP≤alpha and eQ≤alpha}`.

Previous stage's exact endpoint is `alpha235=237666670990705/648489579282432`, `V235=647346693246113/81061197410304`.

## Exact theorem, every real delta (including irrational)

For each stage j, `V14(alpha_(j-1)+delta)=V_(j-1)+slope_j*delta` for **every real** `0≤delta≤Delta_j`. No appeal to interpolation on finitely many test points is made.

| stage | slope | Delta_j | alpha_j | V_j |
|---|---|---|---|---|
| 236 | -2943068/23045 | 138014907635825/400081542840649728 | 15323241207681715/41771181786955776 | 41467533247735739/5221397723369472 |
| 237 | -730392/5855 | 3221491614256775/2339186180069523456 | 1077247581785/2925595459584 | 2841501441371/365699432448 |
| 238 | -4367352/35755 | 558671875/417942208512 | 180193047485/487599243264 | 1390895775373/182849716224 |
| 239 | -26129112/217655 | 680171875/557256278016 | 1446305583005/3900793946112 | 10912825831109/1462797729792 |

## Proof 1: lower bound against arbitrary ordered-history strategies

For count state `s=(n,a,b)`, where a and b are counts of the first two symbols, the likelihood ratio on *every individual ordered history* ending at that state equals `r(s)=Q(h)/P(h)=2^(a+b)/3^a`. For exact rational penalties `lambdaP,lambdaQ>0` define the backwards Bellman recursion:

`B(s)=min{lambdaQ*r(s) [stop and decide P], lambdaP [stop and decide Q], 1+sum_{i=0}^2 P_i B(next_i(s)) [continue if n<14]}`.

At n=14 the continue option is omitted. For any policy depending arbitrarily on its full ordered history and private coins, conditional expectation of its remaining loss is at least `B(s)` by backwards induction: all three admissible actions dominate the minimum. At root, `tP+lambdaP*eP+lambdaQ*eQ ≥ H=B(0,0,0)`. Hence for both error constraints `≤alpha`, `V14(alpha)≥H-(lambdaP+lambdaQ)alpha`. This lower bound does **not** assume Markov policies.

## Proof 2: exact safe observer reduction and finite tight face

All histories reaching the same count state have identical `r(s)`, also after conditioning on continued survival, because the Q probability of each such complete history is its P probability times the same r(s). Private policy coins are hypothesis-independent. Therefore the conditional action distribution among *surviving* paths, given count state, agrees under P and Q. Define the count-state randomized kernel to equal that distribution. Finite forward induction on n establishes identical P/Q state-action occupancies, so it preserves **exactly the four declared observables** `(eP,eQ,tP,tQ)`, including future outputs under these model transitions. It does not preserve full history or claim any native-X6 quotient theorem. An independent verification algorithm instead follows every unmerged ordered path with exact positive integer P/Q masses before aggregation (BRC provenance discipline).

In the finite acyclic count MDP, the Bellman-tight randomized occupancy polytope is the convex hull of deterministic Bellman-tight stationary count policies. For a stage with k binary Bellman ties, assigning one of the two actions at each tie gives *all* `2^k` deterministic tight extreme candidates. Outside ties the minimizing action is unique because each recorded alternative gap is strictly positive. Full ordered-history strategies achieving equality in the lower bound are observationally represented in this polytope by the preceding occupancy argument. No assumption is made that ancestor-related tie randomizations have vanishing mixed terms.

Intersect this finite convex hull of four-observer vectors with the one affine equation `eP=eQ`. The extreme points of that intersection are either already balanced deterministic corners or intersections of a convex-hull edge with the equality hyperplane. Checking **every pair of corners with opposite signs of `d=eP-eQ`** is a finite superset of genuine hull edges and therefore includes all possible extreme intersection points, even when the set contains redundant combinations. For corners v,w of opposite d signs, the exact mixture weight on v is `u=-d_w/(d_v-d_w)`. For d_v d_w<0, 0<u<1, and the new four-observer vector is `u*v+(1-u)*w`. Thus minimum/maximum feasible equal error on this tight face occur among the enumerated finite balanced vertices. Their endpoint policies are root mixtures of count-deterministic tight policies. Every intermediate **real** error has a root-mixed balanced tight policy; irrational mixing probabilities are legitimate in the declared policy class.

The exact finite enumeration checks each deterministic corner has `tP>tQ`. Hence all their convex mixtures and the entire tight face have `tP>tQ`. For every balanced tight strategy, Bellman equality implies `tP=H-(lambdaP+lambdaQ)alpha`; therefore `max(tP,tQ)=tP` and the universal Bellman lower bound is attained. This proves each all-real theorem over its entire maximal equal-error tight-face interval.

## Rational supporting certificates and exhaustive coverage

| stage | lambdaP | lambdaQ | H | binary ties | strict gaps | minimum strict gap | corners | balanced vertices | ordered integer DFS visits |
|---|---|---|---|---|---|---|---|---|---|
| 236 | 131416/2095 | 1497492/23045 | 299837417672867/5472430792704 | 2 | 1238 | 50/13827 | 4 | 3 | 10804 |
| 237 | 357144/5855 | 373248/5855 | 205336817693957/3823518173184 | 7 | 1233 | 125/42156 | 128 | 4071 | 293468 |
| 238 | 2127864/35755 | 2239488/35755 | 1231585368994117/23349255727104 | 8 | 1232 | 625/257436 | 256 | 14703 | 447586 |
| 239 | 12692184/217655 | 13436928/217655 | 7386935856241577/142136267802624 | 9 | 1231 | 3125/1567116 | 512 | 46767 | 644072 |

Each Bellman run enumerates all 680 legal count states, and exactly all 2^k tight deterministic policies. For each policy, an independent unmerged ordered-history integer P/Q branch-mass DFS matches the four exact `fractions.Fraction` suffix-DP observables. Total verified DFS visits across stages **1,395,930**.

## Explicit endpoint strategies and positive time margins

Bitstrings follow each stage's lexicographic Bellman tie-state order, as regenerated by the reference script. The two weights in each row sum exactly to 1. Every margin is strictly positive, proving strict P-time dominance also on endpoints.

| stage | endpoint | policy bitstrings | respective weights | exact tP−tQ |
|---|---|---|---|---|
| 236 | left | 10, 11 | 6332318351/8727890625, 2395572274/8727890625 | 99253794949631/162122394820608 |
| 236 | right | 00, 10 | 1197786137/12493109375, 11295323238/12493109375 | 6340751358322253/10442795446738944 |
| 237 | left | 0010000, 1010000 | 1197786137/12493109375, 11295323238/12493109375 | 6340751358322253/10442795446738944 |
| 237 | right | 0000000, 0001111 | 1904212899/16690625000, 14786412101/16690625000 | 430416404657/731398864896 |
| 238 | left | 10100000, 10101111 | 1904212899/16690625000, 14786412101/16690625000 | 430416404657/731398864896 |
| 238 | right | 00000000, 01011111 | 3050411137/20220375000, 17169963863/20220375000 | 208992366391/365699432448 |
| 239 | left | 101000000, 101111111 | 3050411137/20220375000, 17169963863/20220375000 | 208992366391/365699432448 |
| 239 | right | 000000000, 010111111 | 8922452221/232396850000, 223474397779/232396850000 | 1629030615503/2925595459584 |

Every left endpoint is equal in both exact alpha and exact value to the immediately preceding theorem's right endpoint. Slopes obey the exact ordering

`122232/955 > 2943068/23045 > 730392/5855 > 4367352/35755 > 26129112/217655`.

Thus each new line improves strictly immediately right of the former right endpoint. For any one fixed stage there is no equal-error tight policy beyond the computed maximal face error; equality to that stage's supporting line beyond its endpoint would force such a tight policy by the universal Bellman bound and compact policy polytope, contradiction. This proves fixed-support strict-right separation, not a global assertion about possible later supports.

## Reproduction and scientific boundaries

Execute `python3 PORTABLE_REPRO_STAGE236_239.py`: this creates full deterministic four-observer, ordered-DFS, tie, exact-gap and rational endpoint certificate `PORTABLE_EXACT_CERT_STAGE236_239.json`. Execute `python3 INDEPENDENT_CERT_AUDIT_236_239.py` to re-derive the Bellman comparisons and enumerate all balanced pairs independently (without importing generator code). Program and independent audit were actually executed on author-side, with observed `STAGE236_239_PORTABLE_EXACT_PASS 1395930` and `STAGE236_239_INDEPENDENT_AUDIT_PASS 1395930`. See exact execution logs. SciPy approximate LP was used only to locate candidate neighborhoods; all asserted theorem fractions were recovered and checked by exact rational recurrence and independent integer branch enumeration.

The positive integer branch masses and provenance-preserving serial composition use BRC-compatible arithmetic as a declared mathematical interface (`REUSE_APPLIED`); native heartbeat typed BRC runtime was not executed in this auxiliary IID model. The observer quotient is certified only for the four outputs and finite n≤14 transitions. The P000 native-X6 world remains six spatial axes, separately typed time; no X6 embedding, three-dimensional layer readout, native relation/future operation preservation, physics claim or infinite-horizon theorem follows.

Evidence remains **author-side executable and exact mathematical reasoning only**: not an independent Driver review, formal Lean kernel check, native CLAIM, Source Result or mathematical project acceptance. Native owner query returned `CONTROL_QUOTA` and `research_authority_granted=false`; hence authoritative active owner has not been determined. The next step, Stage240, currently has an exact **dual-only** candidate; see `NEXT_TASK_PACKET_240.md`.
