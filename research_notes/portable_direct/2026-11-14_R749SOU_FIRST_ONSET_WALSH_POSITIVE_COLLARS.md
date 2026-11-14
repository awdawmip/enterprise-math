# R749SOU — Two exact positive-gap onset collars from the first Walsh threshold

**Date:** 2026-11-14. **Status:** AUTHOR_ANALYTIC_NOT_REVIEWED.
**Frozen science:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
**Dependencies:** R749SOS–SOT ([PR #2399](https://github.com/awdawmip/enterprise-math/pull/2399), scientific SHA `5f2830988e31eae99d9ef11882e626b56b022552`), R749SOG transport lemma ([PR #2376](https://github.com/awdawmip/enterprise-math/pull/2376)). Scope: auxiliary 16-state Walsh source observer.

## Model and exact theorem

For k in F_2^4, let chi_m(k)=(-1)^popcount(m & k), A=chi_3, B=chi_12, C=chi_15=A*B. The complete compatible probability fiber is

\[
F_{t,s}=\left\{p(k)=\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}\ge0\quad(k=0,\ldots,15)\right\}.
\]

Define the free minimax total-variation Chebyshev radius rho by centers in the entire 16-atom simplex, and the calibrated radius rho_cal by centers restricted to F_(t,s). Put g=rho_cal-rho, t_*=5/22, G(t)=(22t-5)/48.

Define two triangular wedges in the (t,s) parameter square:

\[
\begin{aligned}
W_t &= \{(t,s): 5/22<t\le 1/4,\quad |s-1/2|\le G(t)/8\},\\
W_s &= \{(t,s): 5/22<s\le 1/4,\quad |t-1/2|\le G(s)/8\}.
\end{aligned}
\]

**Theorem (all real parameters).** On W_t,

\[
\boxed{g(t,s)\ge\frac{371}{6128}\frac{22t-5}{48}>0,}
\]

and on W_s the same estimate holds with s in place of t. On the lower half s<=1/2 of W_t, the stronger g(t,s)>=G(t)/16 holds. Each triangular wedge has exact area 1/33792; the wedges do not overlap, so their union has area 1/16896. The exact bounding slopes of W_t are

\[
s=\frac12\pm\frac{11}{192}\left(t-\frac5{22}\right),\qquad 5/22\le t\le1/4.
\]

The largest vertical half-width is 1/768. At the apex (5/22,1/2), g=0 by the pinned line theorem.

## Complete analytic proof

**1. Exact line theorem.** R749SOT proves for every real 5/22<=t<=1/4:

\[
\rho(t,1/2)=\frac{7-2t}{16},\qquad
\rho_{\mathrm{cal}}(t,1/2)=\frac{1+t}{3},\qquad
g(t,1/2)=G(t).
\]

This depends on the pinned exact source-pair diameter, calibrated event-dual certificate, explicit affine upper centers and exhaustive exact joint-polytopal vertex certificates, not on floating samples. On this interval, 0<=G<=1/96.

**2. Positive reference and explicit source-fiber transfer.** Define

\[
r_{t,s}(k)=\frac{1+tA(k)+sB(k)+\min(t,s)C(k)}{16}.
\]

Inspecting the four (A,B) sign groups proves r belongs to F_(t,s), with min_k r_(t,s)(k)=(1-max(t,s))/16. Given any p in F_(t,s0), choose target s1, let d=|s1-s0| and alpha=d/(1-max(t,s0))<=1. Set

\[
\Phi(p)(k)=(1-\alpha)p(k)+\alpha r_{t,s_0}(k)
 +\frac{(s_1-s_0)B(k)}{16}.
\]

The alpha*r term places >=d/16 probability in every atom, cancelling the worst negative signed correction. Walsh orthogonality proves that Phi(p) is a normalized, nonnegative law with the required A=t and B=s1 moments and all other constrained zero coefficients. Hence Phi(p) is in F_(t,s1). The total-variation bound is

\[
\operatorname{TV}(p,\Phi(p))
\le\alpha\operatorname{TV}(p,r)+d/2
\le \frac{d}{1-\max(t,s_0)}+\frac d2.
\]

Apply the same construction in reverse. When both direction parameters satisfy the stated alpha<=1 condition, the Hausdorff distance between the complete compatible fibers is at most

\[
H(F_{t,s_0},F_{t,s_1})\le\frac{d}{1-\max(t,s_0,s_1)}+\frac d2.
\]

**3. Radius stability.** For compact nonempty TV source sets of Hausdorff distance H, their free minimax radii differ by <=H (keep the old center and approximate the source), and their fiber-calibrated radii differ by <=2H (approximate both source and old calibrated center). Both directions give

\[
g(t,s_1)\ge g(t,s_0)-3H.
\]

In W_t, s0=1/2, d=|s-1/2|<=G/8<=1/768, t<=1/4<1/2-d. Thus both transports apply and

\[
H\le \frac{d}{1/2-d}+\frac d2.
\]

For G(t)>0, the exact inequalities are

\[
\begin{aligned}
g(t,s)&\ge G-3\left(\frac{d}{1/2-d}+\frac d2\right)\\
&\ge G\left(1-\frac{3}{4-G}-\frac3{16}\right)\\
&\ge G\left(1-\frac{288}{383}-\frac3{16}\right)
=\frac{371}{6128}G>0,
\end{aligned}
\]

where the last estimate uses G<=1/96. For s<=1/2, both denominators are >=1/2, so H<=5d/2 and g>=G-15d/2>=G/16.

**4. Exact swap symmetry and areas.** Exchange k's two lower bits with its two upper bits. This atom permutation swaps chi_3 and chi_12, fixes chi_15, and interchanges (chi_1,chi_2) with (chi_4,chi_8). It establishes a bijection F_(t,s) <-> F_(s,t), preserving total variation and both domains of admissible prediction centers. Therefore for all real 0<=t,s<=1,

\[
\rho(t,s)=\rho(s,t),\quad
\rho_{\mathrm{cal}}(t,s)=\rho_{\mathrm{cal}}(s,t),\quad
g(t,s)=g(s,t).
\]

This transfers the proof to W_s. The width at t is G(t)/4, t1-t*=1/44, G(t1)=1/96. Hence

\[
\operatorname{area}(W_t)=\int_{5/22}^{1/4}G(t)/4\,dt=1/33792.
\]

In W_t, t<=1/4 and s>=1/2-1/768>1/4; in W_s the coordinates reverse. The wedges are disjoint and their total area is 1/16896.

## Reproduction and remaining problem

Run `python research_notes/portable_direct/R749SOU_WALSH_ONSET_COLLARS_EXACT_CHECK.py` and compare stdout to `R749SOU_WALSH_ONSET_COLLARS_RESULTS.json`. Standard-library Fraction tests all exact constants, the atom relabeling and 40 explicit two-way nonnegative probability transfers. Universal validity comes from the analytic proof and R749SOS–SOT exact line theorem; the program's finite transport examples are supplemental regression checks.

**Next:** derive matching dual events and piecewise minimax centers in the two-dimensional neighborhood of (5/22,1/2), to locate the actual zero/positive boundary and determine whether it has a corner. Native X6/V29/V39 typed transfer and independent mathematics review remain open.
