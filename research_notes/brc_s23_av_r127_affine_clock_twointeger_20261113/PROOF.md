# R127-AFFINE — Exact two-integer reduction via short affine phase-clock relations

Date: 2026-11-13 (Asia/Shanghai). Author-side auxiliary S23 mathematics. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor: [R126 rotation three-integer result](https://github.com/awdawmip/enterprise-math/blob/8eb8e6f0488a9fbad070f234d36404af015a8a14/research_notes/brc_s23_av_r126_rotation_threeinteger_20261113/PROOF.md).

## Statement and proof

For rational `x,l,h` with `l<h`, integers `N,j,a,c,d`, and `m>=1`, put `A=N-j-a`, `E=c-a`, and `Z_i(theta)=x+(A+i*d)*theta`. The R126 exact circle-rotation theorem gives the directed half-open S23 Boolean observation
`M_i(theta)=1[{Z_i(theta)}<{E*theta}]`
on `theta in (l,h)`, with `{y}=y-floor(y)`. This formulation includes signed coefficients, zero-length arcs, wraparound and equality fibers.

**R127.1 (affine-clock rank reduction).** Assume integers `u,v` satisfy `E=u*A+v*d`. For prescribed bits `b=(b_0,...,b_{m-1})`, feasibility is equivalent to a union of at most
`(|u|+|v|+1)*|P_m|`
rational mixed-linear systems with only **two integer unknowns** `n,k` and one continuous parameter `theta`, where
`P_m={(floor(alpha+i*beta))_(0<=i<m):0<=alpha,beta<1}`
is R121's finite mechanical-word set.

To construct the systems, choose `w in P_m` and integer `s` from the inclusive range `floor(L0)..floor(U0)`, where
`L0=min(0,u)+min(0,v)-u*x`,
`U0=max(0,u)+max(0,v)-u*x`.
Because `U0-L0=|u|+|v|` is integral, this range contains exactly `|u|+|v|+1` integers. Impose these rational affine inequalities:

1. `l<theta<h`;
2. `0<=Z_0(theta)-n<1` and `0<=d*theta-k<1`;
3. define `r=u*n+v*k+s`, require `0<=E*theta-r<1`;
4. define `z_i=Z_i(theta)-n-i*k-w_i`, require `0<=z_i<1` for each `i`;
5. if `b_i=1`, require `z_i<E*theta-r`; otherwise require `z_i>=E*theta-r`.

**Proof of soundness.** The inequalities force `n=floor(Z_0)`, `k=floor(d*theta)`, `r=floor(E*theta)`, and `n+i*k+w_i=floor(Z_i)`. Hence `z_i={Z_i}` and `E*theta-r={E*theta}`; item 5 is precisely the required bit. There are no spurious solutions.

**Proof of completeness.** Given a genuine `theta`, take its actual floors `n,k`, let `alpha={Z_0}`, `beta={d*theta}` and choose `w_i=floor(alpha+i*beta)`. The affine relation yields
`E*theta=u*n+v*k+u*alpha+v*beta-u*x`.
Taking `s=floor(u*alpha+v*beta-u*x)` gives the exact true `r=u*n+v*k+s`; the min/max bounds place `s` in the asserted range. Every required inequality then holds. QED.

The continuous `theta` may be eliminated by exact Fourier–Motzkin lower/upper-bound pairing, retaining strictness of every half-open boundary. A feasible integer pair then yields an exact rational witness from the remaining rational interval (interior midpoint or an allowed weak singleton). Thus the proof reduces each fixed signature to two-dimensional integer linear feasibility with `O(m)` input affine inequalities per candidate; the final elimination may produce `O(m^2)` inequalities. For `|u|+|v|=O(1)`, the inherited `|P_m|=Theta(m^3)` bound gives `O(m^3)` two-integer ILP systems for one specified `m`-bit word. For large minimal relation coefficients, branch cost must be included, and the R126 three-integer method remains a comparison route.

**R127.2 (exact relation criterion and shortest branch search).** Let `g=gcd(A,d)>0`. An integer relation `E=u*A+v*d` exists iff `g|E`, by Bézout. If `A=d=0`, such a relation exists exactly when `E=0`. From one solution `(u0,v0)`, all solutions are
`u=u0+(d/g)*t, v=v0-(A/g)*t`, `t in Z`.
The exact branch count is minimized by minimizing the convex piecewise-linear function
`F(t)=|u0+(d/g)*t|+|v0-(A/g)*t|`.
On every real segment between successive zeros of its two affine terms, `F` is linear; an integer minimum is attained at an integer immediately adjacent to a zero, or anywhere along a flat minimum segment. Floor/ceil of the two zeros (with zero-slope cases ignored) and `t=0` suffice to find a global integer minimum. Extended Euclid plus this constant-sized candidate set therefore computes a minimum-branch relation with polynomially many bit operations. This criterion applies to this **integer-affine elimination**, not to all conceivable two-integer encodings.

## Concrete new family

`A=1,d=2,E=3` has `u=v=1`; E is not an integer multiple of d, extending the special family `E=s*d` handled in R126.3. For huge signed values, `A=±(10^120+7)`, `d=±(10^120+9)`, and `E=A-d=∓2` admit `u=1,v=-1`, with **three s branches**, regardless of phase-clock magnitude.

## Verification / scope

The independent executable `check_r127.py` uses standard-library `fractions.Fraction`. Its exact reference cuts all crossings of `Z_i`, `E*theta` and `Z_i-E*theta` through integers, evaluates **every interior cell and singleton cut**, and compares all bit patterns to exhaustive small-domain two-integer mixed-linear feasibility with exact strict/weak intervals. It also tests signed Bézout minima and huge signed forward certificates.

Deterministic seed `12720261113` returned `R127_AFFINE_TWO_INTEGER_PASS`: **63 complete cases**, **652 bit-pattern comparisons**, **8,767 exact critical representatives**, **486,114 candidate systems**, **471 recovered positive witnesses**, **493 short-relation checks**, and **2 explicit huge-signed forward witnesses**. Of the complete cases, 23 had E not divisible by d. This finite enumeration checks the implementation; the universal result follows from the algebraic proof. It is not yet a production efficient two-dimensional ILP solver.

The coefficients `a,c,j,N,d`, signed timing and observer provenance remain in the record. This exact Boolean auxiliary reduction does not authorize native X6 Cell/Link/Port events or constitute mathematical review.

**Next:** implement an actual exact 2D ILP backend with certified strict-facet witnesses and compare the optimally-short affine branch family with R126's 3D ILP route on common inputs; investigate coefficient families with large optimal `|u|+|v|`.
