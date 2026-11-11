# R5 — exact global endpoint order stratification: three gates, four plateaus

Date: 2026-11-12 (Asia/Shanghai). Status: author-side finite exact-rational theorem in the **external** frozen P/Q–BRC Blackwell auxiliary observer. No native X6 interpretation or canonical mathematical admission is asserted.

## Frozen source and question

Original 28-mass, 15 *labeled* six-arc-atom fixture: `research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py` at immutable Enterprise Math commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Earlier full-range 1144 fixed-threshold result: `research_notes/brc_r5_third_signed_envelopes_20261112/GLOBAL_FIXED_SPECTRUM.md` at `0bb04a83ddcaededda0e5970e9b5ea865dc5e194`. Original frozen scientific pins: Global `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`.

Retain the unchanged vectors `X,D`, all 15 exact atom increments `M_a`, and the observation-invisible perturbation `H` with source-3 target (1,2,6) entries (-23,28,-5) and reversed source-1 entries. Set

- `x=155682221/25142124560000000 = X_(1,3) = X_(0,3)`;
- `X(r)=X+x*r*H`, where `r=eta/x` is an **exact rational or real** parameter;
- `epsilon_*=9/115400000`, the same maximal fixed 15-move ray endpoint;
- `I=[L,U]` where `L=-427508577031693280/628800490619` and `U=1/23`. This is the previously proved maximal interval in which both `X(r)` and `X(r)+epsilon_*D` are nonnegative.

The new question is: **How many of the 15! labeled complete operation orders have all 16 intermediate states nonnegative at epsilon_* as r varies through I?**

## Exact result

Define three exact parameter gates, in strictly increasing order,

```
rho_15 = -16881105436483/2066058754891
rho_12 = -13486918620883/2066058754891
rho_3  =  -3304358174083/2066058754891
rho_q  = (1 - q*epsilon_*/x)/23, q in {15,12,3}.
```

The number of legally feasible labeled complete permutations is **exactly**:

| Complete parameter interval | Feasible labeled prefix masks, including empty mask | Complete legal 15-move permutations |
|---|---:|---:|
| `[L, rho_15]` | 16,462 | **88,224,369,664** |
| `(rho_15, rho_12]` | 12,870 | **22,377,295,168** |
| `(rho_12, rho_3]` | 9,523 | **8,884,916,032** |
| `(rho_3, U]` | 7,109 | **3,514,190,816** |

The corresponding numbers of prefix masks lost immediately **after** each gate are 3,592, 3,347 and 2,414. The decreases in legal full orders are respectively **65,847,074,496**, **13,492,379,136** and **5,370,725,216**. Equality at any gate belongs to the plateau on its left because the model allows zero intermediate mass. In particular, the original `r=0` model has 3,514,190,816 endpoint-legal permutations, while `r=-10` has 88,224,369,664 — an exact ratio `2757011552/109818463` (approximately 25.105). Both retain the same observed Blackwell vector, identical atom dictionary and endpoint increment.

The 1,144 fixed first-zero capacity values of the previous theorem remain present throughout I. The present result concerns *complete legal operation orders at the fixed endpoint*, a different, stricter path statistic.

## Complete finite proof

For each subset/mask `S subset {0,...,14}`, define the exact integral vector `P_S = 36*sum_{a in S} M_a`, and

`F_S(r) = X + x*r*H + (epsilon_*/36)*P_S`.

There are precisely `2^15=32768` labeled masks. A complete permutation is legally executable at epsilon_* exactly when every one of its 16 visited prefix masks has `F_S(r)[k]>=0` for **all 28 coordinates**. Every atom preserves the observer. Since `X(r)>=0`, each fixed prefix trajectory is affine in epsilon; endpoint feasibility also certifies every intermediate scaling along that prefix ray.

For each S and each k, the nonnegativity constraint is affine in r. Intersect all 28 half-lines with I, giving the exact feasible r interval `J_S=[ell_S,u_S]` or the empty set. Compute these intervals with rational arithmetic, without sampling: the empty count is **16,306**, leaving **16,462** masks feasible at some r. For all nonempty `J_S`, `ell_S=L`. The only values attained by `u_S<U` are exactly the three values `rho_15,rho_12,rho_3`, with multiplicities **3592,3347,2414**, respectively. Every such upper gate is attained at the **same coordinate** `k=(target 1,source 3)`; the relevant `P_S[k]` equals `-36q` for `q=15,12,3`. In this coordinate,

`F_S(r)[k]=x*(1-23r)-q*epsilon_*`;

hence its zero is precisely `rho_q=(1-q*epsilon_*/x)/23`. Other coordinates are checked as part of the 28-coordinate finite proof and produce no additional internal gate.

Because these are *all* nonempty-mask interval endpoints, feasibility of every mask is constant on each of the four intervals above, with the indicated right-closed convention. Let `f_r(S)` be the Boolean mask feasibility. The exact recurrence

`dp_r(empty)=1`, `dp_r(S)=f_r(S)*sum_{a in S} dp_r(S without {a})`

counts each labeled legal ordering exactly once by its last atom. Evaluating it with integer arithmetic yields the four table entries. An independent forward recurrence that adds one allowed atom from each legal prefix produces identical counts, including at all three gates and both endpoints L/U. This proves the complete real-parameter piecewise-constant classification.

## Reproduction and evidence

- `VERIFY_GLOBAL_ENDPOINT_ORDERS.py` imports the original immutable project fixture at its inherited project-relative path, reconstructs every integral mask delta, solves 28 exact affine feasibility inequalities per mask, and applies two distinct Boolean-lattice integer-DP recurrences.
- `EXACT_OUTPUT.txt` records locally executed equivalent-fixture Python Fraction output. The local fixture was transcribed from the immutable original GitHub source; the published script's original-import path requires clean-checkout execution for independent remote-byte reproduction.
- All arithmetic in the certificate is rational/integer; the finite universe is the 32,768 labeled masks and all their 28 coordinates. No statistical sampling is used in the proof.

## Interpretation and next question

An observation-invisible redistribution can strongly change legal order multiplicity while keeping the observation, complete endpoint, labeled operations and the 1,144 fixed first-zero capacity values unchanged. The full admissible perturbation domain has **exactly three endpoint-order gates**. This gives a compact exact control statistic for this frozen external model.

Next: classify the *moving first-zero threshold spectrum* globally over I and compare its chambers with these three endpoint-order gates. Examine whether a general sufficient criterion for one-coordinate gate domination can be extracted from the per-mask affine half-line construction, and whether a smaller combinatorial certificate can replace full-mask enumeration in similar BRC fibers.

Source Result/Review and formal mathematical admission remain pending; no existing task claim or other owner's activity is altered.
