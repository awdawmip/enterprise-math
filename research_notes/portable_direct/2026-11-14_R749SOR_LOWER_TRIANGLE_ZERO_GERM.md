# R749SOR — Exact lower-triangle zero-gap germ at s = 1/2

**2026-11-14; AUTHOR_EXACT_NOT_REVIEWED.** Follow-up to R749SOQ (Draft PR #2394), in the identical frozen auxiliary Walsh source model at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Earlier upper-triangle work R749SOP (PR #2392) does not cover this segment. No native X6/V29/V39 correspondence or new formal Task claim is asserted.

## Exact theorem

Let \(A=\chi_3\), \(B=\chi_{12}\), \(C=\chi_{15}=AB\) on \(\mathbb F_2^4\), and let the legal source family be

\[
\mu_{t,s,h,u,v,w,z}(k)=
\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

As in R749SOQ, \(\rho\) and \(\rho^{cal}\) denote, respectively, the free and source-moment-calibrated minimax TV Chebyshev radii of this fiber. For **every real parameter** \(0\le t\le1/6\) with \(s=1/2\),

\[
\boxed{\rho(t,1/2)=\rho^{cal}(t,1/2)=\frac{1-t}{2}.}
\]

Thus the positive-gap phenomenon at \((1/2,1/2)\) is separated from the \(t=0\) parameter axis by an entire exact zero-cost interval, not just an isolated zero-gap endpoint.

## Explicit matching lower bound

R749SOQ's two disjoint-support sources at \(t=0,s=1/2\) are

\[
p_\pm(k)=\frac{(1\pm\chi_8(k))(1\pm\frac12\chi_4(k))}{16}.
\]

Both belong to \(F_{0,1/2}\) and \(\mathrm{TV}(p_+,p_-)=1\). Let

\[
\nu(k)=\frac{(1+A(k))(1+\frac12 B(k))}{16}
=\mu_{1,1/2,1/2,0,0,0,0}(k).
\]

For every real \(t\in[0,1]\), the two laws \(\mu_\pm(t)=(1-t)p_\pm+t\nu\) belong to \(F_{t,1/2}\), and their difference is \((1-t)(p_+-p_-)\). Consequently

\[
\mathrm{TV}(\mu_+(t),\mu_-(t))=1-t,\qquad
\rho(t,1/2)\ge(1-t)/2.
\]

The lower bound requires no finite search.

## Explicit optimal calibrated decoder and complete upper certificate

Choose

\[
\boxed{q_t(k)=
\frac{1+tA(k)+\frac12 B(k)+(3t-\frac12)C(k)}{16}.}
\]

It lies in the fiber (all unretained coefficients vanish) and is nonnegative for the stated interval: its four \((A,B)\) numerators are \(1+4t,\ 1-2t,\ 2-4t,\ 2t\), all nonnegative for \(0\le t\le1/6\).

Consider the joint six-dimensional source polytope with variables \((t,h,u,v,w,z)\), \(0\le t\le1/6\), and the 16 atom nonnegativity constraints at \(s=1/2\). It is bounded and full-dimensional (take interior \(t\), other coefficients zero). The function

\[
(t,h,u,v,w,z)\ \longmapsto\
\mathrm{TV}(\mu_{t,1/2,h,u,v,w,z},q_t)-(1-t)/2
\]

is convex: TV of two affine maps is convex, and subtracting an affine expression preserves convexity. Every maximum occurs at a polytope vertex. Each joint-polytope vertex is represented by six linearly independent active facets. The supplied executable checker uses integer Bareiss elimination and exact Fraction comparisons to exhaust all \(\binom{18}{6}=18,564\) six-facet subsets. It verifies:

| Certificate | Exact count/value |
|---|---:|
| Active six-facet subsets | 18,564 |
| Nonsingular bases | 9,536 |
| Feasible bases | 668 |
| Distinct feasible rational vertices | 78 |
| Vertices at t=0 and t=1/6 | 28 and 50 |
| Interior-t vertices | 0 |
| Bound-tight vertices | 34 |
| Maximum excess above (1-t)/2 | **0** |
| Upper-bound violations | **0** |

It also checks unit mass, nonnegative atoms, and explicit source pair TV \(=1-t\) at \(t=0,1/20,1/12,1/6\). The exact vertex certificate plus convexity proves \(\mathrm{TV}(\mu,q_t)\le(1-t)/2\) for **every real** \(t\) in the interval and **every** compatible source \(\mu\). Together with the matched lower bound, this proves the theorem.

## Scope and continuation

R749SOQ covered both axes; this theorem proves a nontrivial lower-triangle segment with a closed-form optimal calibrated center and matching source diameter. At least until \(t=1/6\), the common-floor mass remains zero (R749SOQ) while the minimax radius decreases linearly and the calibration gap stays exactly zero. The finite exact certificate is a proof over the whole real interval via convexity, not a parameter sampling inference.

The next unresolved point is the **first nonzero calibration gap** along \(s=1/2\) as \(t\) increases beyond \(1/6\). The separate native typed source/branch/signed-port representation remains open. Reproduce with standard Python 3: R749SOR_LOWER_GERM_EXACT_CHECK.py; compare stdout with R749SOR_LOWER_GERM_RESULTS.json. Author-side proof only, NOT_REVIEWED.