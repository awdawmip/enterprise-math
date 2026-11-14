# R155B — Exact local criterion for preserving a Sturmian phase-fiber signature under an adjacent swap

Date: 2026-11-15 (Asia/Shanghai). Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Status: author-side exact theorem with exhaustive finite checker, independent review `NOT_REVIEWED`. Scope: R146 external scalar tied-phase observer only. Predecessor R155 at project branch commit `2c3e2f9d484ff20203a547160508c6295a088e68`.

## Problem and definitions

Let `w=w_0...w_{m-1}` be an admissible finite Sturmian word. Set `s_j=sum_{i<j}w_i`. Its slope-support endpoints are `alpha=a/b < beta=c/d`, both reduced, and cuts are `U=min_j[b(s_j+1)-aj]`, `V=max_j[ds_j-cj]`, as in R146.

Fix `t` with `1<=t<m` and `w_{t-1}w_t=01`. Let `w'` be obtained by replacing those two consecutive bits with `10`. Then `s'_t=s_t+1`, while every other prefix sum is unchanged. We seek an exact criterion for the **entire quadruple** `(alpha,beta,U,V)` of `w'` to equal that of `w`.

## R155B theorem: six exact tests

The quadruples agree **if and only if** all six conditions hold:

**A — left slope feasibility.** For every `0<=i<t`,

`(s_t-s_i)*b <= a*(t-i)`.

**B — right slope feasibility.** For every `t<j<=m`,

`(s_j-s_t)*d >= c*(j-t)`.

**C — lower endpoint retained.** At least one of:

- `alpha=0`; or
- some pair `0<=i<j<=m`, `i!=t`, `j!=t`, has `(s_j-s_i-1)*b=a*(j-i)`; or
- some `i<t` has `(s_t-s_i)*b=a*(t-i)`.

**D — upper endpoint retained.** At least one of:

- `beta=1`; or
- some pair `0<=i<j<=m`, `i!=t`, `j!=t`, has `(s_j-s_i+1)*d=c*(j-i)`; or
- some `j>t` has `(s_j-s_t)*d=c*(j-t)`.

**E — lower cut retained.** Some `j!=t` in `0..m` satisfies `b(s_j+1)-aj=U`.

**F — upper cut retained.** `d*s_t-c*t+d <= V`.

All six tests are exact rational/integer comparisons. Given the prefix sums and the original signature, they take at most `O(m^2)` arithmetic comparisons; only one prefix coordinate changes under the swap.

## Proof (both directions)

For a pair of indices `(i,j)`, the changed count is

`s'_j-s'_i=(s_j-s_i)+[j=t]-[i=t]`.

The lower support bound is `(s_j-s_i-1)/(j-i)`. Its only possible **increase** occurs at pairs with `j=t`, by exactly `1/(j-i)`; testing that these new lower bounds do not exceed `alpha` is condition A. Every other lower bound stays fixed or decreases. Therefore `alpha'<=alpha` is equivalent to A. Equality `alpha'=alpha` occurs automatically at the clipped boundary `alpha=0`, or because an unchanged pair witnesses `alpha`, or because one of the increased bounds with `j=t` newly witnesses it. These are precisely C. A lower bound with `i=t` decreases and cannot newly witness a value it previously did not exceed.

Likewise, the upper support bound is `(s_j-s_i+1)/(j-i)`. Its only possible **decrease** occurs at pairs with `i=t`; requiring each such new bound to be at least `beta` is B. Other upper bounds stay fixed or increase. Equality `beta'=beta` occurs at clipped boundary `beta=1`, at an unchanged witness, or at a decreased bound with `i=t`, exactly D. Thus A–D are necessary and sufficient for the new slope support to equal `(alpha,beta)`. Since the old interval is nonempty, they also ensure the swapped word is admissible.

With these endpoints fixed, the lower-cut values `b(s_j+1)-aj` change only at `j=t`, where they increase by `b>0`. Their minimum stays equal to `U` exactly when some other index attains `U` (E). The upper-cut values `ds_j-cj` change only at `j=t`, where the value increases by `d>0`. Their maximum stays equal to `V` exactly when the changed value remains <=`V` (F); this inequality also guarantees an unchanged index already attained the old maximum. Therefore E–F are necessary and sufficient for cut preservation. Combining the two parts proves the equivalence. QED.

## Scope, consequences and exact validation

If all six conditions hold, R146 immediately gives `C_{w'}(K)=C_w(K)` for every `K>=2`, because the entire defining signature is identical. This is a proven **sufficient and necessary test for adjacent swaps**, not a claim that every possible global word alias must be adjacent.

`R155B_check.py` exhaustively enumerates all binary words of lengths `2..14`, computes exact reduced endpoints/cuts with integer cross-products, and tests each eligible `01 -> 10` swap against both the six-test prediction and a fresh full-signature recomputation. Results: **4,105 swaps tested; 113 preserved; zero mismatches**. For this finite range, every collision class of equal quadruples is a singleton or adjacent-swap doubleton; that last observation is explicitly finite. Output: `R155B_verification.json`, marker `R155B_ADJACENT_SWAP_CRITERION_PASS`.

The rule transforms the R155 multi-one construction into a general, exact local alias detector. Next question: prove or disprove that arbitrary finite Sturmian signature fibers have size at most two, and, if so, whether every collision arises from a qualifying adjacent swap. An independent direction remains the global permanence threshold `T(m)`, for which word-local signature-preservation is not itself a global saturation proof.
