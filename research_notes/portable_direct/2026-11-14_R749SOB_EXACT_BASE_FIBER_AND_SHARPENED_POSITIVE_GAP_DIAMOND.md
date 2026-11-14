# R749SOB — Exact centered-fiber reference radius and an enlarged positive Walsh calibration-gap diamond

Date: 2026-11-14. Status: AUTHOR_EXACT_COMPUTATION_AND_ANALYTIC_PROOF / NOT_REVIEWED.

Frozen scientific inputs: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Dependencies: R749SNG (PR #2309, 74abff6fff03fb6defec95c6c505c69ea5b0832c), R749SOA (PR #2361, 1227cbd685a477a7796823661f28a0a2e2034d67). Scope: auxiliary 16-state Walsh source/observer model. No native X6/V29/V39 identification is asserted.

## 1. Exact theorem

On G = (F_2)^4, set χ_m(x) = (−1)^popcount(m & x), A=χ_3, B=χ_12, AB=χ_15. The source fiber F_(t,s) comprises all probability laws

\[
\mu(x)=\frac{1+tA(x)+sB(x)+hAB(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16}
\]

for real free h,u,v,w,z making all sixteen atoms nonnegative; all other nonconstant Walsh coefficients are zero. Let ρ be the least worst-case total-variation radius over arbitrary probability centers; ρ_cal uses prediction centers in F_(t,s); g=ρ_cal−ρ.

**R749SOB theorem.** For every real (t,s) with d=|t−1/2|+|s−1/2| ≤ 1/481, the source fiber is nonempty and

\[
\boxed{g(t,s)\ge \frac{916283}{97117786480}>0.}
\]

The new closed L1 diamond has exact area 2/231361; compared to R749SOA's radius 1/827, the certified area is larger by exactly 683929/231361 (approximately 2.956 times). No exact off-center minimax formula is assumed.

## 2. Exact finite base-fiber lemma

At p0=(1/2,1/2), take r0(x)=[1+(A(x)+B(x)+AB(x))/2]/16. Then

\[
\boxed{\max_{\mu\in F_{p0}}\operatorname{TV}(\mu,r_0)=15/32.}
\]

Write y=(2h,2u,2v,2w,2z) and C_x=(χ_15(x),χ_1(x),χ_2(x),χ_4(x),χ_8(x)). The fiber is the intersection of the sixteen integer half-spaces

\[
C_x\cdot y\ge-(2+A(x)+B(x)),\quad x=0,\dots,15.
\]

This polytope is bounded because y_j is twice a ±1 character expectation (hence y_j∈[−2,2]), and full-dimensional because r0 has strictly positive atoms. Thus every vertex admits five linearly independent active inequalities. Exact rational enumeration of all binomial(16,5)=4,368 possible active sets yields 3,008 nonsingular systems, 456 feasible bases (with repeats), and 17 distinct vertices. Every computed vertex is rechecked against all sixteen inequalities.

For each feasible y, the exact objective is

\[
\operatorname{TV}(\mu_y,r_0)
=\frac1{64}\sum_{x=0}^{15}\left|(y_0-1)\chi_{15}(x)+y_1\chi_1(x)+y_2\chi_2(x)+y_3\chi_4(x)+y_4\chi_8(x)\right|.
\]

Of the 17 vertices, four give 5/32, nine give 1/4, and four give 15/32. Convexity of the TV objective gives the global upper bound 15/32. The feasible vertex y=(0,1,1,1,1), corresponding to (h,u,v,w,z)=(0,1/2,1/2,1/2,1/2), attains equality.

The accompanying Python Fraction script exhaustively verifies this five-dimensional polytope, including the precise distribution above. It is a finite exact proof for the base-fiber claim; no sampled floating-point inference is involved.

## 3. Analytic transport, with reference radius retained

For p=(t,s) near p0, reuse the matched-interior reference of R749SOA:

\[
r^*_p(x)=\frac{1+tA(x)+sB(x)+\min(t,s)AB(x)}{16}.
\]

For d=||p−p0||_1, let

\[
C(d)=\frac{d}{1/2-d},\quad H_0(d)=C(d)+d/2.
\]

The original matched-interior construction gives TV Hausdorff distance at most H0(d) between F_p and F_p0: its mixing parameter is ε=d/(1−M), where M=max(t,s,1/2)≤1/2+d, and the signed Walsh correction contributes at most d/2 in TV. Also, because |min(t,s)−1/2|≤d,

\[
\operatorname{TV}(r^*_p,r_0)\le
\frac{|t-1/2|+|s-1/2|+|\min(t,s)-1/2|}{2}\le d.
\]

Every μ∈F_p can first be transported to some μ0∈F_p0 within H0(d). By the exact base lemma,

\[
\operatorname{TV}(\mu,r^*_p)\le
\underbrace{15/32+H_0(d)+d}_{K(d)}
=15/32+C(d)+3d/2.
\]

All μ0∈F_p0 have TV distance to r0 at most 15/32≤K(d). Reapply the same explicit transport in both directions, now using this local reference bound in place of the generic TV(μ,r*)≤1. The transported probability remains nonnegative because each reference atom is at least (1−M)/16, and ε≤1 throughout the stated diamond. Consequently

\[
d_H^{TV}(F_p,F_{p0})\le
H_1(d):=C(d)K(d)+d/2.
\]

For any nonempty compact probability-source sets at TV Hausdorff distance H, their unrestricted minimax radii differ by at most H and their calibrated minimax radii by at most 2H: move a calibrated center and each adversarial source across the Hausdorff correspondence, applying triangle inequality twice. Therefore |g(p)−g(p0)|≤3H.

R749SNG has the exact base value g(p0)=9/22−2/5=1/110, so

\[
g(t,s)\ge\frac1{110}
-3\left[
\frac{d}{1/2-d}
\left(\frac{15}{32}+\frac{d}{1/2-d}+\frac{3d}{2}\right)
+\frac d2
\right].
\]

The subtracted expression increases for d∈[0,1/481]. At the boundary d=1/481, the lower bound equals exactly 916283/97117786480. This proves the theorem **for all real points** in the closed diamond. The accompanying exact script checks the rational endpoint constants.

## 4. Reproducibility, provenance and remaining work

Run Python 3 standard library code R749SOB_SHARP_REFERENCE_TRANSPORT_EXACT_CHECK.py and compare its deterministic JSON stdout with R749SOB_SHARP_REFERENCE_TRANSPORT_RESULTS.json. The checker covers all 4,368 five-constraint choices, computes the 17 exact vertices, and evaluates the inequality at the proposed outer radius. The continuous-region conclusion comes from the displayed analytic inequalities. This is an author-side result, NOT_REVIEWED; it is separate from formal task CLAIM or scientific promotion.

Useful next problem: derive directional (rather than worst-case isotropic) transport constants from the base fiber's exact extremal geometry, or determine the genuine zero/positive calibration-gap boundary with two-parameter minimax dual certificates. The X6/V29/V39 typed observer and future-operation preservation map remains open.