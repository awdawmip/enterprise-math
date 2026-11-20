# X6 Unit186 — exact affine inversion of finite-horizon signed native depth fibers

**Date:** 2026-11-20. **Parent:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task/publication:** `RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2`. **Author logical lane:** `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane excluded. **Status:** AUTHOR_PROVED / EXECUTED_EXACT_INTEGER_CHECK / GITHUB_VERIFIED / UNREVIEWED / NOT_ADMITTED. This note does not assert Native PROGRESS, review, Result or P000 modification.

## Source and novelty boundary

Frozen signed-X6 science `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`), in particular the twelve signed primitive directions and native endpoint BRC. Historical genuine A3 production source `awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:src/enterprise_math/weighted_relation_field.py` (blob `e50bf991e4dc4280063556a7aad1028f9f9404ed`) and its actual test consumer `tests/test_weighted_relation_field.py` (blob `51748dfe340c385907c4f2218fa1ae5ae2260522`).

Already completed Unit182 observer-fiber BRC sum, Unit183 trace lift, Unit184 sharp size and bits, and Unit185 one-bit rank updates are **consumed without rediscovery**. New in Unit186: an explicit finite affine formula for both extreme feasible common depths, with an implementation using no search over depths, an exact bit-cost bound, and a typed source-consumer reconstruction certificate. The X6 adapter is new mathematical research code; it is not misrepresented as a preexisting production integration or native benchmark.

## Theorem — direct endpoint inversion using seven affine constraints

Let `M≥0` be the exact number of signed six-axis primitive events from chosen anchor 0. Let `a=(a_1,…,a_6)∈Z_{≥0}^6`, `min_i a_i=0`, be the terminal relative observer `q(z)=z−min(z)1`. Write the six entries in nondecreasing order `s_1≤…≤s_6`, and define

\[
S=\sum_{i=1}^{6}s_i,\quad
B_t=2\sum_{i=7-t}^{6}s_i-S\quad(0\le t\le6),
\]

where the empty sum for `t=0` is 0. Thus `B_0=-S`, `B_3=∑(top 3)−∑(bottom 3)`, and `B_6=S`.

Define the integer lower and upper endpoints

\[
\boxed{L_M(a)=\max_{t=0,1,2}\left\lceil\frac{B_t-M}{6-2t}\right\rceil,\qquad
U_M(a)=\min_{t=4,5,6}\left\lfloor\frac{M-B_t}{2t-6}\right\rfloor.}
\]

The exact set `H_M(a)` of common depths of reachable native endpoints is empty if **any** of the following holds: `M ≢ S (mod 2)`; `B_3>M`; or `L_M(a)>U_M(a)`. Otherwise,

\[
\boxed{H_M(a)=[L_M(a),U_M(a)]\cap\mathbb Z.}
\]

In particular the mathematical interval endpoints can be computed using one six-entry sort, a fixed number of additions/comparisons, and only six divisions by the positive constants 2, 4 and 6; no depth enumeration or binary search is required. For a valid reachable signed-native terminal state, all observed coordinate integers have O(log(M+2)) bits, so the exact input-to-bounds computation uses **O(log(M+2)) bit operations** with conventional linear-time division by fixed small constants, including sorting six names. This is a fixed-six-dimension statement, not an O(1) bit-cost assertion or a general variable-dimension theorem.

**Proof.** Unit184's exact fiber characterization, derived from the frozen signed primitive graph, is `H_M(a)={h∈Z: Σ_i |a_i+h|≤M}` when the parity `M≡Σ_i a_i (mod2)` holds. For any six real numbers `x_i=a_i+h`, the identity `Σ_i|x_i|=max_{σ_i∈{-1,1}}Σ_iσ_i x_i` is exact. If exactly `t` signs are positive, the maximizing choice places the `t` positive signs on the `t` largest `a_i`, so the corresponding affine value is `(2t−6)h+B_t`. Consequently,

\[
\sum_i|a_i+h|=\max_{0\le t\le6}\big((2t-6)h+B_t\big).
\]

The seven simultaneous inequalities `(2t−6)h+B_t≤M` are equivalent to the three displayed lower bounds for `t<3`, the central feasibility constraint `B_3≤M`, and the three upper bounds for `t>3`. Taking integer ceilings and floors proves both directions, including negative depths and boundary cases. Parity follows from `Σ_i|a_i+h|≡Σ_i a_i+6h≡S (mod2)`; a mismatch cannot be repaired by changing depth. □

## Genuine-source relation-field consumer bridge

For the *genuine* frozen A3 producer with six **unit capacities**, `Z_ij=z_i−z_j`. Its row maximum gives `a_i=max_j Z_ij`, since the row compares `z_i` to the minimum native coordinate. For an allowed endpoint rank `j∈[0,U_M(a)−L_M(a)]`, reconstruct `h=L_M(a)+j`, `C=Σ_i a_i+6h`. The genuine frozen consumer `recover_totals_from_weighted_field((1,…,1),Z,C)` has the source formula

\[
z_i=(C+\sum_j Z_{ij})/6=a_i+h.
\]

Integrality, total preservation and field closure hold for genuine generated inputs. The **new Unit186 checker independently executes this source-equivalent recovery formula** on every enumerated valid endpoint; it does not claim to have imported the frozen production module into this checker. It reconstructs full terminal signed coordinates, not complete ordered path history, native R063 output, or arbitrary weighted-state semantics.

The exact sorted `B_t` carrier also supplies Unit185's streaming epsilon margins by two consecutive direct bound computations. This is a practical closed-form evaluation of its already proved rank update, not a new one-bit theorem.

## Execution and scope of finite evidence

The committed Python checker enumerates **all 184,690 reachable six-axis endpoints** over the exact horizons `M=0,…,10`, groups them into **97,306 terminal relative fibers**, independently checks every interval by direct integer depth search, and verifies **184,690 source-formula field reconstructions**. Additionally, **3,000 fixed-seed large-integer cases** up to horizon `10^15` compare the affine formula to an independent median-based binary-search reference. Every horizon also rechecks Unit184's preexisting sharp cardinality `floor(M/3)+1` as a regression, not a new discovery. All checks returned zero mismatches. Each of six noncentral affine candidates is observed as active in the exact bounded corpus. The same checker was actually executed in Python normal, `-O`, and `-OO` with byte-identical JSON output SHA-256 `2d9879817f8fc18dc322fd34637fcc458a2a12ffb6d40d58938ed5f59a60d61d`; errors use mandatory exceptions, not removable assertions.

- Checker: `research_checks/X6_UNIT186_EXACT_FIBER_ENDPOINT_ALGORITHM_CHECK_20261120.py` at `610f076e4111d409a4b58993b256fb5529073322`, Git blob `5adefe754862e11215ac58b980f8e9dbadc43038`, SHA-256 `e3ddb832a6d5f1b8980ec888c6548ab2a540c5eb671d6dbd178039cee760f279`.
- Certificate: `research_checks/X6_UNIT186_EXACT_FIBER_ENDPOINT_ALGORITHM_RESULTS_20261120.json` at `a2aeade1f14f6f78d1fd339d92f33aff3ad36174`, Git blob `d8bce3f9c3b6f59d53492eae1b183d510431e9b0`, SHA-256 `2d9879817f8fc18dc322fd34637fcc458a2a12ffb6d40d58938ed5f59a60d61d`.

This computation is a **new finite-horizon inversion experiment**, not a rerun or substitute for the old successful native R063 six-file benchmark (17/17 original conditions; 512/512 regressions).

## Remaining mother-task obligations and precise next unit

The true historical LP011 native-axis `argmax` and LP019 unlawful positive N-BRC subtraction still have **UNRESOLVED_PROVENANCE**, lacking a verified offending `commit:path:line` plus typed downstream consumer; do not convert correct row maxima or positive A3 differences into fictitious errors. 28-LP cross-surface integration, Units149–152 legacy Native associations, author Units175 onward Native semantic checkpoints, and independent Driver review remain open. Native Source checkpoint last independently authenticated in this lane is through Unit174; latest local author Activity through Unit185 was verified before Unit186. This note makes no claim of current winning CLAIM, platform identity attestation, Native PROGRESS or mathematical admission.

Next discriminating scientific work: use the new affine inversion on a *real frozen source operation that consumes an absolute state or grand total*, and test its factorization through `(M,Z,j)` versus `(M,Z)` with explicit minimal residual. Alternatively return to unresolved LP011/LP019 only with exact historical source evidence. Keep the current signed-X6 input pin and observer/operation types.
