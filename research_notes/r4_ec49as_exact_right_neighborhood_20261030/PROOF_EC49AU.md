# EC49AU — exact causal BRC optimum to η=75/206 and sharp scalar-price obstruction

Date: 2026-10-30. Classification: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Frozen model and provenance

Continue EC49AS/AT at immutable research commit `787829f75bf3836a776480edf6291aa19759750b`, retaining the auxiliary positive 18+18-leaf P/Q observer. The hidden variable is `w∈{0,1,2}`, the first action `c∈{A0,A1,B0,B1,STOP}` costs `(1,1,2,2,0)`, and `u∈{0,1}` is observed before any conditionally independent sensor coin. The observation factor is `t(w,u)=1/2+(2u−1)(1−w)η`; conditional paid leaf masses are `P=x[w,c]t(w,u)(1+1[z=w])/12` and `Q=x[w,c]t(w,u)/9`. The first-stage cost is `C1=43/48`, exact sensor purchase mass `C2=13/16`, and `H=P(accept)−(177/172)Q(accept)`. Only `(c,u)` may condition the sensor coin; terminal acceptance cannot recover `w`.

## Theorem 1 — continuous all-real extension

For every real `9/25 ≤ η ≤ 75/206` and every legal real causal behavioral strategy,

`H ≤ h(η) := 77/688+(674η−175)/16512`.

Equality is attained by the pre-existing lawful witness

`W[0]=(0,3/16,1/4,0,9/16)`, `W[1]=(1,0,0,0,0)`, `W[2]=(0,1,0,0,0)`.

It buys on all paid `(c,u)` fibers (total mass `13/16`) and accepts only `(c,z)∈{(A0,1),(A1,2),(B0,0)}` or `(c,u,z)=(A1,1,0)`. The acceptance function uses observable data only; all behavioral randomness is independent. At the new endpoint `η=75/206`, `(α,β,H)=(8483/19776,1127/3708,98797/850368)`.

**Proof.** Let `q_z(c,u)=x[z,c]t(z,u)/3`, `T=Σ_z q_z`, and `V=Σ_z[43q_z−16T]_+/172`. Unpurchased and STOP fibers have no positive support. Every legal strategy satisfies, for any scalar `λ≥0`,

`H ≤ G_{λ,η}(x) := λ(13/16)+Σ_{c<4,u}[V(c,u)−λT(c,u)]_+`.

The first-stage feasible cut polytope `Π` has three stochastic row equations, the exact first-stage cost `43/16` before division by three, and the paid-mass inequality `Σ_{w,c<4}x[w,c]≥39/16`. The existing exact rank/support enumeration in `VERIFY.py` covers all `168` vertices: `24` high-mass original vertices and `144` purchase-boundary vertices. Since `G` is convex in `x`, its maximum is attained at a vertex. For fixed `x` and `λ`, `G` is convex in `η`, so its maximal vertex envelope is convex in `η`.

Use one fixed rational price `λ=11/172`. The reproduced exact Fraction endpoint certificates are:

| η | max G on 24 high vertices | max G on 144 boundary vertices | h(η) |
|---|---|---|---|
| `9/25` | `47723/412800` | `47891/412800` | `47891/412800` |
| `75/206` | `98797/850368` | `98797/850368` | `98797/850368` |

The maximum dual equals `h` at both endpoints. Convexity bounds the upper envelope by the chord `h` throughout the **entire real interval**, not just a rational grid. The explicitly lawful W has objective `h(η)` throughout. Therefore `Hmax=h` on the stated interval. Combining this with the earlier author-side EC49AQ/AR and EC49AT certificates extends the already proved piecewise optimal-value formula to all `0≤η≤75/206`, with its first kink at `175/674`.

## Theorem 2 — sharp failure of the whole one-price dual family, not of the witness

Let `U_λ(η)=max_{x∈Π}G_{λ,η}(x)`. For **every** real `75/206<η≤11/30` and **every** `λ≥0`,

`U_λ(η)>h(η)`.

Thus `75/206` is the exact upper endpoint at which a scalar purchase-price dual can match this witness over the tested right neighborhood. This is a **certificate-method barrier**: it does *not* prove that the true feasible causal optimum exceeds `h`.

**Proof.** Consider the lawful first-stage distribution `X[0]=(0,11/16,0,0,5/16)`, `X[1]=(1,0,0,0,0)`, `X[2]=(0,1,0,0,0)`. Its total paid mass is `43/48`, too large to buy everywhere at the required cost. Exact checking of all leaf-score signs at both ends of `[75/206,11/30]` shows that on this interval its hypothetical full-purchase envelope is affine:

`F_η(X)=9/128+9η/64`, with paid mass `43/48`.

Set `L=11/172`. If `0≤λ≤L`, the pointwise inequality `[V−λT]_+≥V−λT` yields

`U_λ(η)≥G_{λ,η}(X)≥F_η(X)−λ/12≥F_η(X)−L/12 = h(η)+(103/1032)(η−75/206)>h(η)`.

If `λ>L`, use the lawful witness W, which has total paid mass exactly `C2` and full-purchase support `F_η(W)=h(η)` throughout this interval. Its fiber `(c,u)=(A1,1)` has positive `T` and exactly `V/T=L` throughout. Therefore

`G_{λ,η}(W)−h(η)=Σ_{c,u}[λT(c,u)−V(c,u)]_+≥(λ−L)T(A1,1)>0`.

These cases cover every nonnegative scalar price. In particular, the previous fixed `λ=3/50` failure at `η=11/30` is not repaired by *any* scalar λ.

## Theorem 3 — exact best one-price upper bound at η=11/30

At the prescribed rational test point,

`h(11/30)=14401/123840 ≤ Hmax(11/30) ≤ inf_{λ≥0} U_λ(11/30) = 209867/1802560`.

The one-price dual gap relative to the witness is exactly `71/506970`.

**Proof of minimax.** For every `λ≥0`, the same high-mass X gives an affine minorant

`G_{λ,11/30}(X)≥39/320−λ/12`.

For W, omit its `(A1,1)` purchased fiber while lower-bounding the others linearly. This yields the second minorant

`G_{λ,11/30}(W)≥227/2064+(71/720)λ`.

The two lines have opposite slopes and intersect at `λ*=1473/22532`, with common value `209867/1802560`. Hence `U_λ(11/30)` is at least this value for *all* prices. At exactly `λ*`, the exhaustive 168-vertex Fraction calculation confirms that no vertex has larger dual, proving equality of this infimum.

## Additional exact local obstruction

If the first-stage `x` is restricted to one of the `168` vertices, exact optimal conditional buying is fractional knapsack over the eight `(c,u)` fibers, ordered by `V/T`. At `η=11/30`, all 24 high-mass vertices have best feasible objective at most `162689/1444800`, strictly below `h`; the maximum over all 144 purchase-boundary vertices is `h` exactly. Thus any feasible counterexample exceeding W must use a **nonvertex first-stage distribution**. This finite-family result does not rule out an interior causal counterexample.

## Execution, limits, and next problem

Run `python3 VERIFY_EC49AU.py` alongside predecessor `VERIFY.py`; expected stdout is `EC49AU_REPORT.json`. The test uses only Python `Fraction`, exact support enumeration, exact fiber scores, and endpoint sign checks. The continuous interval theorem is due to the stated convexity argument, not numerical interpolation. No Lean formalization or independent review has occurred. This theorem concerns only the *auxiliary strictly positive probability BRC observer*; it neither proves a map to signed/phase BRC nor preserves native X6/heartbeat updates. P000 and ACTIVE worldview are unchanged.

**EC49AV:** At `η=11/30`, either produce a lawful rational interior first-stage `x` with conditionally independent purchase coins and `H>14401/123840`, or prove a stronger causal inequality excluding every interior `x`; the scalar λ route is now provably insufficient. Preserve source leaf definitions and the exact cost/hidden-history constraints, and pursue separately a typed correspondence to the signed BRC and six-dimensional native model.
