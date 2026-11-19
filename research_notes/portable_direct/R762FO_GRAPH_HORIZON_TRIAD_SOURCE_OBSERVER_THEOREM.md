# R762FO — Finite-horizon source-observer fibers under graph-restricted triad swaps

Date: 2026-11-19 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_ENUMERATION_PASS / NOT_REVIEWED.
Mother task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, frozen taskbook `awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md`.
Frozen P000/X6 input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Direct antecedents: R762FM (PR #2778, `356e3ee52a83270f39db13397cf941db4456ced1`) and R762FN (PR #2782, `d32cbdef5039b522d81a67587d5b47237455416e`).
This result is a self-contained extension of R762FN's source matching and does not require accepting its PR as a reviewed theorem.

## Population and explicitly conditional update

Fix one X6 native Cell, three distinct selected native axes and k separately sourced positive tokens on each axis:
A_1,...,A_k, B_1,...,B_k, C_1,...,C_k. Each candidate event contains precisely one token of each type. A grouping history is encoded by two permutations `(sigma,tau) in S_k x S_k`:
`(A_i,B_{sigma(i)},C_{tau(i)})` for every i. The coarse positive-BRC observer retains the original named tokens, directions and multiplicities but forgets which tokens form one event. Its complete grouping fiber has `(k!)^2` histories.

Choose an arbitrary simple undirected graph G on the A-slot labels `{1,...,k}`, and a fixed visible slot a. For each edge `{i,j}` of G define an *abstract logical partner-swap* U_ij: exchange the entire ordered B/C partner pairs attached to A_i and A_j. This is a bijection of histories; it preserves all primitive tokens, their positive weights, their signed native-axis types and the number of candidate triads. The swaps are proposed operations on a source-incidence data type. No native `TRIADIC_CLOSURE_E` Cell/Link/Port event or rotation license is inferred from their definition.

The future readout Q_a returns the pair of *named source IDs* `(B_{sigma(a)},C_{tau(a)})`. The finite-horizon observer F_(G,a,h) is the **family of responses** `Q_a(U_w(history))` for every *known* graph-edge swap word w of length at most h, with each experiment beginning from the same initial history. The operation word is available to the observer. This models future query capability, not merely a single unknown trajectory.

Let `D_h={i:dist_G(a,i)<=h}` and `r_h=|D_h|`; disconnected-vertex distances are infinity.

## Theorem 1 — Exact finite-horizon information and sharp representation size

For every k>=1, every graph G, root a and integer h>=0, the F_(G,a,h)-equivalence classes of grouping histories are exactly the fibers of the restriction map

`(sigma,tau) -> ((sigma(i),tau(i)))_(i in D_h).`

Consequently the number of distinct future-observation signatures is

`N_h = (k!/(k-r_h)!)^2,`

and every such signature has precisely

`F_h = ((k-r_h)!)^2`

compatible complete grouping histories. The minimum additional *fixed-length* source-relation memory required to answer all declared horizon-h experiments without access to the hidden grouping is

`b_h = ceil(log_2 N_h)` bits.

**Proof.** Track which original A-row occupies the visible slot a while graph-edge transpositions act on its row positions. In one swap that row either stays or moves across one G-edge. After at most h swaps it can come from no vertex outside D_h. Conversely, for any i in D_h take a shortest path from a to i, and perform partner-pair swaps along that path in reverse order, thereby bringing the original row i to slot a in exactly dist_G(a,i) moves. Thus the full experiment family observes precisely the ordered partner pairs of all rows in D_h. Two states therefore have identical F responses iff their sigma and tau restrictions to D_h agree. Each restriction independently is an injection from r_h named A slots into k B/C partner IDs; there are (k)_(r_h)=k!/(k-r_h)! injections. Independently extending each injection to a permutation on the remaining k-r_h labels has (k-r_h)! possibilities. Multiplication proves N_h and F_h. Information-counting gives the bit lower bound, and rank/unrank of two partial injections attains it. QED.

This is an exact observer- and horizon-specific quotient: the hidden fiber is preserved as an explicit pair of residual permutations on the unqueried slots, rather than treated as numerical noise. A code sufficient for horizon h is not automatically sufficient after extension to h+1.

## Theorem 2 — Earliest possible full recovery horizon

For k>=2, F_(G,a,h) uniquely determines the *entire* original grouping if and only if `r_h>=k-1`. If the vertex distances from a, including infinity for disconnected vertices, are sorted `d_1<=...<=d_k`, the least such horizon is

`h_* = d_(k-1)`,

understood as infinite if this distance is infinite. For k=1, h_*=0.

**Proof.** Theorem 1 gives `F_h=1` exactly when `(k-r_h)! = 1`, i.e. k-r_h is 0 or 1. Equivalently r_h>=k-1, which first occurs when the second-largest vertex distance has entered the ball. The final unmatched B and C partners determine the one omitted row. QED.

Thus a **single fixed visible source-port** can force the full R762FN memory `ceil(log_2 (k!)^2)` after sufficient permitted reversible updates. For a disconnected graph with at least two vertices outside the visible component, the horizon-independent residual fiber remains nontrivial. The graph specifies exactly which otherwise-invisible relations can be recovered through permitted future transport.

## Exact examples and a delayed distinguishing witness

For the path graph `A1--A2--A3--A4`, visible root A1:

| horizon h | accessible A rows | r_h | signatures N_h | fiber F_h | sharp bits |
| --- | --- | ---: | ---: | ---: | ---: |
| 0 | {1} | 1 | 16 | 36 | 4 |
| 1 | {1,2} | 2 | 144 | 4 | 8 |
| 2 | {1,2,3} | 3 | 576 | 1 | 10 |
| >=3 | {1,2,3,4} | 4 | 576 | 1 | 10 |

Take `sigma=(1,2,3,4)`, `sigma'=(1,2,4,3)`, and `tau=(1,2,3,4)` in both histories. Their Q_A1 values after any zero- or one-swap experiment agree. The two-step word `U_(2,3)` followed by `U_(1,2)` moves the originally third row to visible A1 and distinguishes B3 from B4. This is an explicit positive-BRC provenance defect whose first visibility occurs at horizon two.

For the disconnected two-edge graph `{1,2},{3,4}`, root A1, even h unbounded sees only two A rows; `N_h=144`, `F_h=4`. The other component's two B and two C assignments remain free. This also demonstrates why a single-Cell coarse total or present-time answer does not certify future-safe relation compression.

## Verification and interpretation

`R762FO_VERIFY.mjs` exhaustively enumerates all `(k!)^2` histories for every k=1,...,4, all 75 simple graphs across these k, every root and h=0,...,k-1. It independently enumerates reachable slot-origin permutations through each graph's edge swaps and checks that the accessible set equals the closed graph ball, then checks every signature count and equal fiber size. Exactly 1,105 graph/root/horizon cases and 592,449 history-case comparisons PASS. The explicit k=4 witness is also checked in the independent Python scratch calculation; machine results are `R762FO_EVIDENCE.json`. The displayed proof is valid for every finite k and h; the exhaustive computation covers only k<=4. Independent mathematical review: NOT_REVIEWED.

The operational primitives are logical reversible incidence swaps over source-labelled candidate triads. They have not been proved to be admitted as native X6 rotation or native `TRIADIC_CLOSURE_E` updates. The established P000 six-dimensional Cell torsor, S6 axis-permutation skeleton and PERP_E relation remain unchanged. No Euclidean vector-sum-zero condition is imported. Positive BRC counts preserve multiplicities, but signed/phase or physically dynamical claims would require separate exact carriers and licenses.

## Next research unit

Extract exact native Cell/Link/Port admissibility and any genuine triad-exchange rule from the frozen/task-applicable sources. Determine the induced graph of licensed local exchanges (or show a bounded obstruction), then apply the proven formula to its graph-distance balls. Test time-ordered causal updates where a reversed experiment is unavailable: the present theorem explicitly assumes repeatable known swap words from one initial state. Compare the exact recovery cost with source-state storage, and retain residual permutations for inaccessible components.
