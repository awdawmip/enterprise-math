# R749SOJ — Exact two-dimensional oblique zero/positive calibration transition

**Date:** 2026-11-14. **Scientific status:** author-side exact theorem and complete rational polytope certificate; **NOT_REVIEWED**. **Mode:** independent portable research, not a canonical Task CLAIM or Result.

**Frozen scientific input:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Verified predecessor statements: R749SOF, [PR #2370](https://github.com/awdawmip/enterprise-math/pull/2370); R749SOH, [PR #2376](https://github.com/awdawmip/enterprise-math/pull/2376); R749SOI, [PR #2380](https://github.com/awdawmip/enterprise-math/pull/2380). All statements in this note concern the **auxiliary 16-state Walsh source-observer model**.

## 1. Exact theorem

For (G=\mathbb F_2^4), set (\chi_m(k)=(-1)^{\operatorname{popcount}(m\mathbin{\&}k)}), (A=\chi_3), (B=\chi_{12}), (C=\chi_{15}=AB). The compatible source fiber at retained moments ((t,s)) is
$$
F_{t,s}=\left\{\mu_{t,s,h,u,v,w,z}(k)=\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}\ge0\ (0\le k<16)\right\}.
$$
Each law automatically has total mass one. Let (\Delta_{16}) denote all 16-point probability laws, and use total variation (TV(p,q)=\tfrac12\sum_k|p(k)-q(k)|). Define
$$
\rho(t,s)=\min_{q\in\Delta_{16}}\max_{\mu\in F_{t,s}}TV(q,\mu),\qquad
\rho^{\mathrm{cal}}(t,s)=\min_{q\in F_{t,s}}\max_{\mu\in F_{t,s}}TV(q,\mu).
$$

**Theorem.** For **all real** ((t,s)) in the closed rectangle
$$
\mathcal R=\left[\frac{13}{20},\frac{17}{25}\right]\times
\left[\frac{12}{25},\frac{13}{25}\right],
$$
the exact minimax radii are
$$
\boxed{\rho(t,s)=\frac{3-t-2s}{4}},\qquad
\boxed{\rho^{\mathrm{cal}}(t,s)=
\max\left\{\frac{3-t-2s}{4},\frac{4-2t-2s}{5}\right\}},
$$
and hence
$$
\boxed{g(t,s)=\rho^{\mathrm{cal}}(t,s)-\rho(t,s)
=\frac{\max\{0,1-3t+2s\}}{20}}.
$$
The **exact local phase boundary** is the straight segment (3t-2s=1) crossing the interior of the rectangle, passing through ((2/3,1/2)). On the (3t-2s>1) side the calibration gap is zero, and on the (3t-2s<1) side it is strictly positive. The rectangle has area (3/2500). The strictly positive side is a quadrilateral of area (1/1500); the zero side is a triangle of area (1/1875).

This identifies a genuine two-dimensional phase boundary rather than a failure boundary for a particular decoder.

## 2. Free minimax lower and upper bounds

Every point of (\mathcal R) satisfies (0\le s\le t\le1) and (t+s\ge1). Reuse the explicitly admissible R749SOH pair
$$
\mu_{\pm}=\mu_{t,s,\,t+s-1,\,\pm(1-s),\,\pm(1-s),\,\pm(1-t),\,\pm(1-t)}.
$$
Its total variation diameter is exactly
$$
TV(\mu_+,\mu_-)=\frac{3-t-2s}{2}.
$$
The triangle inequality gives (\rho(t,s)\ge(3-t-2s)/4) for every free decoder.

An explicit free predictor, admissible for (0\le t\le1), is
$$
\boxed{q_f(k)=\frac{1+A(k)+(2t-1)B(k)+(2t-1)C(k)}{16}}.
$$
Its four ((A,B)=(++),(+-),(-+),(--)) block numerators are respectively (4t,4(1-t),0,0), so it is nonnegative with unit mass. The complete joint-polytope certificate below proves
$$
\sup_{\mu\in F_{t,s}}TV(q_f,\mu)\le\frac{3-t-2s}{4}
$$
throughout the positive-side quadrilateral. On the zero-side triangle the exact free radius follows from R749SOI, with the predictor provided in that theorem; thus the free radius is established on all of (\mathcal R).

## 3. Calibrated prediction: the exact positive-side lower certificate

Translations of (G) by (3) and (12) preserve the Walsh coefficients (\chi_3,\chi_{12},\chi_{15}), while symmetrically canceling (\chi_1,\chi_2,\chi_4,\chi_8). This finite group preserves every fiber (F_{t,s}). Averaging a calibrated decoder over the group leaves its moments ((t,s)) intact and cannot increase worst-case TV by convexity. Thus, in minimizing (\rho^{\mathrm{cal}}), it suffices to take
$$
q_h(k)=\frac{1+tA(k)+sB(k)+hC(k)}{16}.
$$

Use the two compatible source laws, with coefficients shown in the order ((h,u,v,w,z)):
$$
\mu_A:\ (1+s-t,\ s-t,\ s-t,\ 0,\ 0),\qquad
\mu_G:\ (t+s-1,\ s-1,\ s-1,\ t-1,\ t-1).
$$
The sixteen atom probabilities of each are affine in (t,s). At the four vertices of the positive-side quadrilateral each source has nonnegative atoms and unit mass, as verified exactly; therefore both source laws remain admissible throughout the polygon.

For the events
$$
E_A=\{1,2,4,7,8,11,13,14\},\quad
E_G=\{0,1,2,4,5,6,8,9,10,12\}
$$
define the two legitimate TV event lower bounds (L_A=q_h(E_A)-\mu_A(E_A)), (L_G=q_h(E_G)-\mu_G(E_G)). Exact Walsh summation yields
$$
L_A=\frac{1+s-t-h}{2},\qquad
L_G=\frac{7-3t-5s+h}{8}.
$$
Consequently, **for every calibrated center** after symmetrization,
$$
\max_{\mu\in F_{t,s}}TV(q_h,\mu)
\ge\frac{L_A+4L_G}{5}
=\boxed{\frac{4-2t-2s}{5}}.
$$
This lower bound is strictly greater than the free diameter bound exactly when (3t-2s<1). The proof uses the same two source laws throughout the whole positive-side polygon, not a grid of numerical optimization solutions.

## 4. Matching calibrated upper bound and the zero side

On (3t-2s\le1), choose the explicit calibrated center
$$
\boxed{q_c(k)=\frac{1+tA(k)+sB(k)+\frac{9s-t-3}{5}C(k)}{16}}.
$$
Its nonnegativity throughout the positive polygon and the upper bound
$$
\sup_{\mu\in F_{t,s}}TV(q_c,\mu)\le\frac{4-2t-2s}{5}
$$
are certified by the exact joint-polytope vertex test in §5. Combined with §3, this proves the positive-side formula.

On (3t-2s\ge1), every point of (\mathcal R) belongs to the R749SOI triangle (\operatorname{conv}\{(1,0),(3/5,2/5),(1,1)\}). The established R749SOI theorem gives (\rho=\rho^{\mathrm{cal}}=(3-t-2s)/4), with calibrated center
$$
q_0(k)=\frac{1+tA(k)+sB(k)+(t+s-1)C(k)}{16}.
$$
Along the common edge (3t-2s=1), the coefficients agree exactly:
$$
\frac{9s-t-3}{5}=t+s-1.
$$
Thus the piecewise calibrated predictor is continuous across the genuine zero/positive phase boundary.

## 5. Complete exact finite certificate for all real parameters

The strictly positive-side polygon has vertices
$$
(13/20,12/25),\quad (49/75,12/25),\quad
(17/25,13/25),\quad (13/20,13/25),
$$
and is precisely (\mathcal R\cap\{3t-2s\le1\}). In seven variables (X=(t,s,h,u,v,w,z)), its joint source polytope (P) is defined by:
- sixteen inequalities (1+X\cdot(A(k),B(k),C(k),\chi_1(k),\chi_2(k),\chi_4(k),\chi_8(k))\ge0);
- five parameter inequalities (20t\ge13), (-25t\ge-17), (25s\ge12), (-25s\ge-13), and (-3t+2s\ge-1).

Every compatible source in the positive polygon occurs in this compact seven-dimensional polytope. Both proposed predictors and both target radii are affine in (X), so the excess (TV(q(X),\mu(X))-r(X)) is convex. Its maximum is bounded by its maximum over all vertices of (P). Each vertex has seven linearly independent tight facets among the 21 inequalities.

The accompanying standalone standard-library script uses integer Bareiss elimination to exhaust **all** (\binom{21}{7}=116,280) seven-facet combinations. It obtained **47,744 nonsingular systems, 1,176 feasible systems, and 80 distinct feasible rational vertices**. Of these, 16 saturate the free bound and 32 saturate the calibrated bound; **both maximum excesses equal exactly zero** and there are zero upper-bound violations. The script also checks source admissibility, explicit source-pair diameters, event lower-bound identities, and the exact polygon area. All comparisons are exact `fractions.Fraction`, with no floating-point tolerance.

By compactness and convexity, the finite vertex result proves the upper bounds for **every real** ((t,s)) in the positive-side region. The previously certified R749SOI result covers the other region, completing the theorem on the entire rectangle.

**Reproduction:** from `research_notes/portable_direct/`, run `python3 R749SOJ_WALSH_LOCAL_OBLIQUE_CERT.py` and compare stdout to `R749SOJ_WALSH_LOCAL_OBLIQUE_RESULTS.json` (JSON semantic equality). The program has no third-party dependencies.

## 6. Provenance, limits and next research

The frozen source and the definitions of the Walsh observer remain unchanged. This result extends R749SOF's one-dimensional transition at ((2/3,1/2)) to an **exactly located two-dimensional phase boundary segment**, using R749SOH's diameter source pair and R749SOI's zero-side upper theorem. It has not undergone independent mathematical review; the native X6/V29/V39 event-morphism correspondence remains an open separately typed problem.

**Next independent mathematical unit:** enlarge the certified polygon along the oblique line, identify where the free center and the calibrated center change active face, and determine whether the line remains an exact phase boundary beyond this rectangle. Keep separate the stronger question of a native source-/signed-Port-preserving map.

**Research artifacts:** this full note, `R749SOJ_WALSH_LOCAL_OBLIQUE_CERT.py`, and `R749SOJ_WALSH_LOCAL_OBLIQUE_RESULTS.json`. The remote Git object and executed local code are separately verified below at publication, without asserting review or formal task admission.
