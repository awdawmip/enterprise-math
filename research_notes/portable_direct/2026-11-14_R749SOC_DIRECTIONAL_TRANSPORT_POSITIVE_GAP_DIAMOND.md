# R749SOC — Direction-sensitive matched-interior transport; 5.95× positive Walsh calibration-gap diamond

Date: 2026-11-14. Status: AUTHOR_ANALYTIC_PROOF_AND_EXACT_CERTIFICATE / NOT_REVIEWED.

Frozen source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Dependencies: R749SNG (exact base minimax gap); R749SOA (matched-interior two-way transport); R749SOB (exact 17-vertex base-fiber reference radius). Scope: auxiliary 16-state Walsh source/observer model, with no native X6/V29/V39 identification asserted.

## 1. Exact theorem

For every real (t,s) satisfying d=|t−1/2|+|s−1/2|≤1/339, the source fiber F_(t,s) is nonempty and

\[
\boxed{\rho^{\mathrm{cal}}(t,s)-\rho(t,s)\ge\frac{43323}{5646650680}>0.}
\]

The certified positive-gap diamond has area 2/114921, which is exactly 683929/114921 (approximately **5.9513 times**) the R749SOA certified area, and 231361/114921 times the R749SOB certified area.

## 2. Exact directional base-fiber lemma

At p0=(1/2,1/2), take the R749SOB reference r0=[1+(χ_3+χ_12+χ_15)/2]/16. For every μ0 in the exact five-dimensional source fiber F_p0, for every 2≤c≤678/337 and every (a,b) with |a|+|b|≤1,

\[
\boxed{\operatorname{TV}\left(c(r_0-\mu_0)+\frac{a\chi_3+b\chi_{12}}{16}\right)
\le\frac{15c}{32}+\frac1{16}.}
\]

Here TV on a signed zero-total vector denotes one-half of its L1 norm.

**Proof of the base lemma.** The left side is jointly convex in the variable source μ0, in the scalar c, and in the directional pair (a,b). The maximum over μ0 is at one of R749SOB's exact 17 polytope vertices; over the L1 direction ball it is attained at one of (±1,0),(0,±1); for each such choice, the bound can be checked at c=2 and c=678/337 and extended to intermediate c by convexity, since the right side is affine in c.

All 17×4×2=136 finite exact conditions are evaluated by the companion Fraction program. At c=2, maximum directional values for the two masks χ_3 and χ_12 are 1 for the negative sign and 7/8 for the positive sign, against bound 1. At c=678/337, the corresponding maxima are 2711/2696 and 1187/1348 against bound 2711/2696. Hence the displayed bound holds for all c, directions and source laws in the asserted domains. Negative-axis cases attain the bound.

## 3. Analytic two-way transport

For p=(t,s), set δ=(t−1/2,s−1/2), d=|δ_t|+|δ_s|>0, M=max(t,s,1/2), ε=d/(1−M), c=ε/d=1/(1−M). For d≤1/339,

\[
2\le c\le c_{\max}(d):=\frac1{1/2-d}\le678/337,\qquad 0\le\epsilon\le1.
\]

R749SOA's matched-interior reference is

\[
r^*_p=\frac{1+t\chi_3+s\chi_{12}+\min(t,s)\chi_{15}}{16}.
\]

For μ0∈F_p0, the same valid matched-interior transport is

\[
T_{p0\to p}\mu_0=(1-\epsilon)\mu_0+\epsilon r_0+
\frac{\delta_t\chi_3+\delta_s\chi_{12}}{16}.
\]

The nonnegative reference lower atom bound from R749SOA proves Tμ0∈F_p. Its TV displacement is d times the signed expression in the directional lemma with (a,b)=δ/d, hence at most

\[
d\left(\frac{15c_{\max}(d)}{32}+\frac1{16}\right).
\]

For the reverse transport, start from any μ∈F_p. The original R749SOA Hausdorff estimate provides some μ0∈F_p0 satisfying

\[
\operatorname{TV}(\mu,\mu_0)\le H_0(d):=d\,c_{\max}(d)+d/2.
\]

The reverse valid transport is

\[
T_{p\to p0}\mu=(1-\epsilon)\mu+\epsilon r^*_p-
\frac{\delta_t\chi_3+\delta_s\chi_{12}}{16}.
\]

The signed displacement ε(r*_p−μ)−(δ_tχ_3+δ_sχ_12)/16 differs from the directional base-fiber displacement ε(r0−μ0)−(δ_tχ_3+δ_sχ_12)/16 in TV norm by at most

\[
\epsilon\bigl[\operatorname{TV}(r^*_p,r_0)+\operatorname{TV}(\mu,\mu_0)\bigr]
\le d\,c_{\max}(d)\,[d+H_0(d)],
\]

using R749SOB's reference bound TV(r*_p,r0)≤d. Thus the two source fibers have symmetric Hausdorff TV distance at most

\[
H_2(d)=d\left(\frac{15c_{\max}(d)}{32}+\frac1{16}\right)
+d\,c_{\max}(d)\left[d+H_0(d)\right].
\]

The unrestricted TV minimax radius is 1-Lipschitz in Hausdorff TV and the calibrated radius is 2-Lipschitz; therefore |g(p)−g(p0)|≤3H2(d). From R749SNG, g(p0)=1/110. Every term in H2(d) is increasing on the stated interval, and the exact endpoint constants are

\[
H_0(1/339)=1693/228486,\quad H_2(1/339)=932543/307999128,
\]

\[
1/110-3H_2(1/339)=\boxed{43323/5646650680}>0.
\]

This establishes the theorem for the complete real-parameter diamond. The finite exact certificate is used only for the directional base lemma and endpoint arithmetic; the all-real-parameter extension follows analytically.

## 4. Reproduction and frontier

Run Python 3 standard-library script R749SOC_DIRECTIONAL_TRANSPORT_EXACT_CHECK.py alongside the prerequisite R749SOB_SHARP_REFERENCE_TRANSPORT_EXACT_CHECK.py. Compare deterministic JSON stdout with R749SOC_DIRECTIONAL_TRANSPORT_RESULTS.json. The program exhausts 17 exact source vertices, two scalar endpoints and four signed unit directions and checks all derived rational constants. Result is author-side / NOT_REVIEWED, with no shared CLAIM or native-world Result implied.

Next mathematical question: replace the reverse transport's generic ε(d+H0) deviation by the exact joint directional fiber optimum and seek the true two-dimensional zero/positive-gap transition boundary. Native X6/V29/V39 observer/future-operation preservation and independent review remain open.