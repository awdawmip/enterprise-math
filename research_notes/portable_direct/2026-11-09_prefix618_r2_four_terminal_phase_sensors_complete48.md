# PREFIX-618-R2 — Four terminal phase sensors are sufficient and minimal for complete native-48 output

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR-SIDE EXACT THEOREM / EXECUTED SYMPY CERTIFICATE / INDEPENDENT DRIVER REVIEW PENDING.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Immediate reusable theorem: PREFIX-617 author-side positive lift, `research_notes/portable_direct/2026-11-09_prefix617_r2_full48_positive_eight_state_intertwiner.md` at `00cdf3bcbea94aaa623e8b3e969f2354a5bfd21e`. Current rules and P000 read separately.

## Question and exact observer scope

Can one reconstruct every original 48-phase **positive branch-sum** at an arbitrary terminal time by observing just a few original phase rows, without reading a full 48-vector, for the native X6 STAR/BRC four-point difference input? Determine the minimum number of simultaneous scalar phase observations.

The native primitive has 48 ordered phase classes, derived from the upstream 96-port/576-tagged-action substrate. This claim is about the fixed 48-phase positive-mass quotient under its native positive-branch sum Q(g), not the tagged 96-port history.

Fix `d=e_4+e_11+e_14+e_32`, nonnegative known initial gates `a,b`, and positive known probe intensity `lambda`. Use original zero-based phase indices. Put `x_0=lambda Q(b)Q(a)d`, `x_t=Q(q_t)...Q(q_1)x_0`, for any finite word with `q_s>=0`. The current task's parameters `a,b,lambda` are **known/calibrated**; unknown-initial-calibration problems remain separate.

## Exact eight-state source formula

From PREFIX-617 the 48x8 nonnegative map `H=[H_C H_B]` has these nonzero entries (all others zero):

| column | phase rows | coefficients |
|---|---|---|
| C0 | 2,3,15 | 1 |
| C1 | 5,28,29 | 1 |
| C2 | 27,38,39 | 1 |
| C3 | 16,17,41 | 1 |
| W0 | 3,14,15 | 1 |
| W1 | 17,40,41 | 2 |
| W2 | 26,27,39 | 4 |
| W3 | 4; 5,29 | 4; 8 |

The exact native intertwiner `Q(g)H=H diag(C,B(g))` is checked in the standalone script. Here `C=2P` with `P e_j=e_(j+1 mod 4)`, and
```text
B(g) = [0 0 0 4(g+3)]
       [1 0 0 0     ]
       [0 1 0 0     ]
       [0 0 1 0     ].
```
The explicitly calibrated initial lift splits into
```text
c_initial = lambda (0,0,4,4)^T
w_initial = lambda (b+3,a+3,1,1/2)^T.
```
Therefore the gate-independent full-48 baseline is
`z_t=H_C C^t c_initial`; the full output is `x_t=z_t+H_B w_t`.

For each residue `r=0,1,2,3`, define an empty product as 1 and
```text
F_r(t)= product over 1 <= s <= t and s mod 4 = r of [4(q_s+3)] .
```
Repeated application of the **original BRC monomial gate update** yields, at every `t>=0`,
```text
w_t[j] = w_initial[(j-t) mod 4] * F_((t-j) mod 4)(t),    j=0,1,2,3.
```
This formula follows by following each initial token through one step of B(g): coordinates advance cyclically and multiply by `4(q_s+3)` exactly on a wrap from coordinate 3 to 0. It is an exact identity for variable gates and rational nonnegative parameters.

## Theorem 618.1 — Four fixed native phase rows reconstruct every output

Take the original native phase readings at the *single terminal instant* `t`:
```text
z14=x_t[14], z40=x_t[40], z26=x_t[26], z4=x_t[4].
```
Rows `(14,40,26,4)` of `H_C` vanish and the corresponding rows of `H_B` form `diag(1,2,4,4)`. Hence
```text
w_t=(z14,z40/2,z26/4,z4/4)^T,
x_t = H_C C^t c_initial + H_B w_t.
```
This reconstructs **all 48** phase sums exactly from at most four original phase samples and known calibration, for *any finite length*, including zero and rational gates.

For `0<=t<4`, only `t` of the four `F_r(t)` have changed from 1, so only the corresponding `t` sensor rows are necessary; the other w-coordinates are known from `w_initial`. For `t>=4`, four sensors suffice.

## Theorem 618.2 — Information-theoretic terminal sensor lower bound

For `t>=4`, exactly **four simultaneous scalar phase readings are necessary** to reconstruct the full terminal native-48 output uniformly over all positive gate words, when observations are any fixed selection of original phase coordinates. The lower bound holds even for nonlinear or discontinuous postprocessing of those readings.

Proof: hold all gates after the first four fixed and take `q_1,...,q_4` in an open positive box. Each of the four distinct residue products `F_r(t)` is a nonzero constant times one independent factor `4(q_s+3)`; the residue-to-output coordinate permutation is bijective. Because `w_initial` is strictly positive, the attainable `w_t` contain an open 4-dimensional box. Each set of `k<4` phase readings restricts to an affine linear map from that box to `R^k`, namely selected rows of `H_B` plus known `z_t`. Such a map has a nonzero null vector. A sufficiently small move along that vector stays in the box and leaves all chosen readings identical. But `H_B` is injective (the four witness rows form a nonsingular diagonal minor), so the two full 48-phase vectors differ. No decoder can separate them. Together with Theorem 618.1, `k_min(t)=min(t,4)` for `t>=0`; the same rank proof for `t<4` restricts to the `t` independent active residue products.

Explicit three-sensor witness at `a=b=lambda=1`, `t=4`: the words `(1,1,1,1)` and `(2,1,1,1)` both yield `(x[14],x[40],x[26])=(64,128,64)`, while `x[4]` equals 32 and 40 respectively. Thus omitting phase 4 loses real future-gate information.

## Corollary 618.3 — Four residue products are the exact endpoint equivalence

For two words of equal length with the *same calibrated* `a,b,lambda>0`, the entire native-48 terminal output is equal **if and only if** their four mod-4 products `F_r(t)` are equal. Reason: the gate-independent baseline cancels, `H_B` has full rank 4, and each of the four initial W coordinates is positive. This strengthens prior operator-level residue invariants by showing necessity from one four-point input and a single endpoint, not a family of input basis probes. For `t<4`, the empty-class products equal 1 and the statement still holds.

A same-class exchange `(0,2,1,5,3,4,7,6)` -> `(3,2,1,5,0,4,7,6)` gives identical complete 48-phase terminal output; exchanging the first two gates generally changes it.

## Complexity and observer fidelity

For known `a,b,lambda`, a streaming algorithm maintains four exact product accumulators and updates one accumulator per gate, using `O(t)` scalar multiplications and `O(1)` active scalar registers. At a chosen endpoint, producing all 48 phase entries requires the baseline `C^t c_initial` and at most 24 nonzero H entries; the sparse output assembly has fixed cost. A single terminal observation of the four phase rows can also reconstruct the 48-vector using only four divisions by `1,2,4,4` and sparse matrix assembly. These are arithmetic-operation bounds; exact bit complexity grows with the word length and input numerator/denominator sizes and is not claimed constant.

Observer safety: the 48-phase quotient is preserved under the **declared** positive branch-sum Q(g) for these probe differences and all gate words by the exact H-intertwiner. The result does not identify individual original 96-port/tagged-path histories; that remains an independent retained provenance question under P000's joint-relation preservation constraint.

## Execution evidence and next question

Checker: `PREFIX618_native_BRC_four_sensor_checker.py`; result JSON: `PREFIX618_native_BRC_four_sensor_results.json`. Native STAR enumeration is rebuilt directly; the standalone exact SymPy script checks `Q(g)H=HM_8(g)`, row matrices, rank, 84 variable-gate test cases covering lengths 0–20, 4,368 exact native phase and sensor-coordinate comparisons, full-rank `t=4` Jacobian determinant `81920`, same-class collisions, and cross-class separation. All assertions passed locally on 2026-11-09. The general claim follows from the symbolic identities and linear-algebra proof, not finite-case extrapolation.

**Next:** (1) construct the actual typed 96-port/tagged-path observer and test whether its future operations descend through the 48-phase positive quotient; produce a two-history separation witness if not; (2) benchmark full input preparation, large-rational bit growth, 48/16/8/7-state and product-streaming endpoint costs; (3) characterize minimum sensor sets with `a,b,lambda` not pre-calibrated.

This is author-side exact mathematics, not a formal Native Result or independent Driver acceptance.
