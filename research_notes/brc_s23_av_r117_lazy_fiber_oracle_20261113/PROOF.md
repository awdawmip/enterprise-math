# R117 — Exact lazy feasibility oracle without new-time cut expansion

Date: 2026-11-13. Enterprise Math Research1 author-side finite ranked Boolean auxiliary observer. Continues the R116 branch frontier at `46c4d9d0a508333a3ce434d2664624badb1d05f7`, retaining frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. P000 and the original full six-phase S23 scientific inputs remain unchanged.

## Model and problem

On a compact rational interval `I=[0,1]`, let an old finite collection of potential times `T` have known exact cells: rational singleton points and rational open intervals `(a,b)` on each of which every old Boolean eligibility bit is constant. Retain all old complete identity rankings, histories, signatures and their persistent rank-tree roots. An unseen time `N∈Z` has the *single-phase auxiliary* eligibility predicate

`M_N(theta) = 1[{N theta+1/4} ∈ [0,1/2))`,

where `{z}=z-floor(z)` for arbitrary signed rational `z`. For each attained old signature `s` determine whether its potentially disconnected parameter fiber `D_s` meets both values of `M_N`, and produce exact rational witnesses without enumerating any of the new `Θ(|N|)` phase cuts.

## R117.1 — Integer-intersection oracle on one open cell

For a rational open old cell `J=(a,b)`, `a<b`, and `N≠0`, define

`l=min(Na+1/4,Nb+1/4)`, `h=max(Na+1/4,Nb+1/4)`.

The phase `q=N theta+1/4` ranges *exactly* over `(l,h)` even when `N<0`.

The eligible phase bands are `[k,k+1/2)`, `k∈Z`, and the ineligible bands are `[k+1/2,k+1)`.

**Theorem.** `J∩M_N^{-1}(1)≠∅` exactly when there is an integer `k` with
`l-1/2<k<h`.
Likewise, `J∩M_N^{-1}(0)≠∅` exactly when there is an integer `k` with
`l-1<k<h-1/2`.

**Proof.** Two nondegenerate intervals `(l,h)` and `[k+δ,k+δ+1/2)` intersect if and only if `k+δ<h` and `k+δ+1/2>l`, where `δ=0` for eligibility 1 or `δ=1/2` for eligibility 0. Rearranging yields the two strict integer inequalities. QED.

In both cases, set `L=l-(δ+1/2)`, `H=h-δ` and `k_0=floor(L)+1`. A feasible band exists if and only if `k_0<H`. If feasible, let

`q_- = max(l,k_0+δ)`, `q_+ = min(h,k_0+δ+1/2)`.
Then `q_-<q_+`, and `theta=((q_-+q_+)/2-1/4)/N` is a rational witness strictly inside `(a,b)` with desired eligibility.

For an old singleton cell `{a}`, eligibility is evaluated directly at `a`. For `N=0`, the predicate is constant true and any rational point in the old cell is a witness for bit 1.

All comparisons, floors and midpoint calculations are exact over integers and rationals. There is no loop over `N`, no approximation and no phase-cut generation for the new time.

## R117.2 — Fiber refinement with disconnected preimages and inherited roots

Iterate all old exact cells `J_i`, reading their old signature `s_i` at a rational representative. For each bit `b∈{0,1}`, call R117.1 (or singleton evaluation) to determine whether `J_i∩M_N^{-1}(b)` is nonempty and save one actual rational witness.

**Theorem.** The union of recorded `(s_i,b)` is precisely the attained new signature set `S_(T∪{N})`, even when one old signature occurs on several disconnected old cells. The new signature count equals R116's exact `d+r`; each resulting state may initially share its parent `s`'s immutable historical rank-root and all current Top-k capacities. A later one-sided insertion of a complete new-time identity modifies only states with `b=1`.

**Proof.** Old cells cover `I` and preserve every old bit, so any new signature is realized within some old cell; the oracle finds its bit there. Conversely, every returned witness belongs to its old cell with precisely the recorded old and new bits. This establishes exact new signature coverage. Root inheritance and selective insertion then follow from R116.2 with no information loss in the declared Boolean observer. QED.

If `q` old cells are already constructed, there are at most `2q` oracle calls and at most `2q` candidate witnesses, independently of `|N|`. Each call uses a fixed number of rational integer operations; the actual bit complexity depends on endpoint size `B` and `log_2(|N|+2)` rather than `|N|` iterations. Computing/storing old cells, their signatures, and ranked histories remains separately costed. For larger phase families, a corresponding exact band or semilinear feasibility law must be supplied; this theorem establishes the particular stated single-phase predicate.

## Exact validation

Python 3 `Fraction` checker: `check_r117.py`. Deterministic seed `1172026`. It compares the returned attained new signature set to full exact cut atomization for 150 randomized cases, including positive/negative old and new times and disconnected old signature fibers. It independently verifies every returned rational witness against old and new eligibility.

Executed local output (complete JSON in `verification_r117.json`):
- 150 random cases;
- 7,772 old-cell/bit oracle calls versus 9,050 new-time raw atoms used for finite brute comparison;
- 1,674 checked rational signature witnesses;
- four huge signed frequencies `±(10^30+39)`, `±(10^80+7)`, with each case using 39 old cells, **78** oracle calls and returning 8 attained signatures, with witness bit lengths at most 105 and 270 respectively;
- status `R117_PASS`.

The huge-frequency cases never enumerate the new cuts or use floating point; their results are exact mathematical instances under the declared auxiliary model. The 150-case comparison is finite implementation verification, not proof of the all-integer statement, which follows from the interval argument above.

## Remaining question R118

Extend the exact oracle from one threshold phase to the original S23 six-affine-phase qualification predicate. Determine whether feasible intersections of simultaneous Boolean phase conditions can be decided with a compact arithmetic certificate, including offset coupling, boundary semantics, disconnected fibers and potentially large time parameters; compare certificate construction, integer bit complexity, persistent historical memory and witness recovery against full cut enumeration. Keep full identity/provenance. No native X6 Cell/Link/Port authorization is asserted by this auxiliary result.
