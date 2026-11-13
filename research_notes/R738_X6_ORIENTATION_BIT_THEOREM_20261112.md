# R738 — Orientation-line one-bit recovery of signed X6 BRC path history

Date: 2026-11-12 Asia/Shanghai. Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; authoritative P000: `p000_reality_foundation.json` and `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`. Reuses author-side R735 signed circulation (PR #2132) and R737 cubic closing-depth repair (PR #2135). P000, original evidence and existing task publications are unchanged.

## Question and typed carrier

For a chosen unordered triple `A={a,b,c}` of distinct native X6 axes, consider six-step *coordinate-path* BRC branches made of each signed primitive axis step `+a,-a,+b,-b,+c,-c` exactly once. Each branch retains its full word, sign and identity, with positive integer branch count; no signed physical force amplitudes or Euclidean equilibrium are inferred. Let `NB(A)` require that no adjacent steps are inverse on the same axis. Its size is 240. The ambient X6 still contains six native axes; this three-axis display is a three-dimensional research slice, not a two-dimensional native plane.

For a signed path w, set `Q_i` to the sign of its first i-step. Define R735's integer signed circulation `J_ij=Σ_t x_i(t−1) Δx_j(t)` for i<j. Previously, (Q,J) split the 240 NB branches into 144 singleton and 48 double fibers. R737 proved a three-component closing-depth K gives injectivity. Find a minimal *native-label-covariant* repair with the true one-bit storage lower bound.

Define the first-appearance order `f(w)=(f_1,f_2,f_3)`, a permutation of A. Rather than assigning an absolute sign without a chart, store the orientation `ε(w)=f_1∧f_2∧f_3 ∈ Or(A)`, the two-element orientation torsor of the unordered active triple. Relative to a chosen oriented frame (a,b,c), ε is the parity ±1 of the permutation between that frame and the first-appearance order.

## Theorem — exact minimal orientation residual

For every selected native X6 axis triple A, the observation
`D(w)=(Q(w),J(w),ε(w))`
is injective on NB(A). (Q,J) alone has exactly 48 two-element fibers, hence any fixed-length exact recovery extension requires at least one bit. The orientation-torsor residual is a single bit and achieves that bound.

D is natural under the S6 relabeling of native axes if ε is transported as an orientation: `ε(gw)=g_*ε(w)` in `Or(gA)`. If integer signs are stored using the ascending-label frame in each chart, then
`ε_chart(gw)=sgn(π_{g,A}) ε_chart(w)`,
where `π_{g,A}` is the permutation that orders `g(a),g(b),g(c)` into the destination ascending frame. It is a **twisted (orientation-line) bit**, not a scalar bit with trivial group action.

### Combinatorial proof with only five basic patterns

For any fixed Q, forgetting signs turns the six-step word into a double-occurrence word on three symbols (each used twice), with no equal adjacent symbols. There are exactly 30 such patterns. S3 acts freely on these patterns by relabeling symbols, so there are five orbits. Choosing the representatives whose first appearances are 0,1,2 yields the complete five-element list below. Fix Q=(+,+,+) and write the crossing vector `A=(A_01,A_02,A_12)` where `A_ij=J_ij/(Q_i Q_j)`. For any Q, multiplying by the nonzero Q_i Q_j is an invertible change of observer.

| Representative word | A | Distinct A-values in its six relabelings | Multiplicity per A-value |
| --- | --- | ---: | ---: |
| 010212 | (1,0,1) | 6 | 1 |
| 012012 | (1,1,1) | 6 | 1 |
| 012021 | (1,1,0) | 3 | 2 |
| 012102 | (0,1,1) | 3 | 2 |
| 012120 | (0,0,1) | 6 | 1 |

Each row's A-value orbit is disjoint from all other rows. These 24 occupied A-values exhaust the 30 patterns with 18 singletons and six double fibers for each Q. For the two double-fiber rows, the two relabelings with equal A differ by a transposition of active axes; their first-appearance orientation therefore changes sign. Thus (A,ε) separates every double pair. Reinstating Q gives 8×30=240 uniquely decodable branches, 8×24=192 (Q,J) classes, and 8×6=48 double fibers. The six-to-one abstract branch selection was never applied: all 240 provenance-labeled branches remain distinct.

For the crossing identity used above, project a branch to axes i,j: `A_ij=+1` exactly for the unsigned pattern ijij, `A_ij=−1` exactly for jiji, and 0 for iijj, ijji, jiij, or jjii. This follows by directly summing the two j-increments weighted by the current integer i-coordinate. It supplies an independent check of the coordinate J formula.

### Why an ordinary invariant scalar is insufficient

Take `w=(+0,+1,+2,−0,−2,−1)` and `w'=(+0,+2,+1,−0,−1,−2)`. They share Q=(+,+,+) and J=(1,1,0). The axis transposition (1 2) maps w to w', preserving the entire observed (Q,J) value; any additional scalar with *trivial* relabeling action must take the same value on both. Their first-appearance orientations are opposite, so the twisted one-bit residual succeeds. Exact enumeration shows 24 of the 48 double fibers have an observation-preserving relabeling that swaps the pair (the displayed example already proves the obstruction).

## BRC law, algorithm and verification

Typed BRC carrier: the finite **positive-counted, ordered, provenance-retaining signed X6 coordinate-path family**; each of its 240 branches has count 1. Observer: (Q,J,orientation). Composition of branch families is disjoint tagged union with additive nonnegative counts; it is not cancellation of signed/complex force amplitudes. Allowed later operation for the losslessness claim: any deterministic operation of the reconstructed six-token path in this exact finite carrier. Preserve chart/orientation transport when composing observers across label changes.

Online encoding requires only a set of axes already encountered, first directions Q, three integer J accumulators and the parity of first-appearance order. Exact recovery uses a finite (Q,J,ε) lookup; this is a finite-state compression theorem, not a general asymptotic speedup or a force dynamics theorem.

The accompanying Python standard-library checker enumerates all 90 unsigned double-occurrence strings and all 30 nonbacktracking ones, all eight Q assignments, all 240 signed NB branches and their fibers. It tests 72,000 transported cases across 20 native X6 axis triples, 720 S6 relabelings and five orbit representatives. An additional independent full checker compared coordinate integration with pair-projection crossings and counted 24 observation-preserving swappable double fibers. All integer checks passed: `R738_X6_ORIENTATION_BIT_EXACT_PASS`. Evidence is `R738_X6_ORIENTATION_BIT_RESULTS.json`.

## Exact scope, current control and next unit

This is an author-checked finite combinatorial theorem for the R735 coordinate carrier, not a physical identification of coordinate J with V39 loop flow j. Source task hard target remains the construction of legal signed X6 Cell/Link/Port force-incidence and `TRIADIC_CLOSURE_E` updates (including V29, V39 and triadic rotation covariance). Next test: for one Source-pinned legal triad event, determine whether the first-appearance orientation is observed, transported or erased by V29/V39, and find the smallest event-level state needed to predict the next legal update.

At 2026-11-12 08:25 Asia/Shanghai, the native control read gave publication `TP2-8B7E13C5904A2D6F1142`, `NEEDS_DISPATCH`, `taskbook/unassigned`, `claim_id=null`. A new native session issuance returned `SESSION_ISSUANCE_QUOTA`; no new Researcher-ID or winning CLAIM was obtained. This document is author-side mathematical evidence only; it grants no Result, Driver review, or P000 promotion.
