# R762GW — Spectral return asymptotics for the signed STAR BRC candidate

Date: 2026-11-20 (Asia/Shanghai). Author-side TASK research for RS-X6-TRIADIC-CLOSURE-DYNAMICS / immutable publication TP2-8B7E13C5904A2D6F1142. Frozen taskbook: enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8; frozen P000: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Starting sources: R762GU (#2845; commit 1bf0bbf396e41bea55d979a63d4b034e2b87e845) and separately appearing R762GV (commit be582a235f390f7fe10467b4730b42a8b137f19d). Review: NOT_REVIEWED.

## Scope: native six-axis readout, auxiliary signed inventory

The four auxiliary STAR labels v=0,1,2,3 form the vertices of K4 and the six **native X6 axis labels** are 01,02,03,12,13,23. The incidence vector H_v in signed Z^6 has three ones at axes incident to v. A candidate signed letter T(v,s), s=+1 or -1, has six-axis *composite* readout s H_v, retaining its actual ordered three-component realization and branch provenance. For a word of length m, the internal inventory is z in Z^4 and the chart-relative native Cell readout is Y=Bz in Z^6 (B has columns H_v). The internal four-index encoding does not assert four native spatial dimensions. R762GU proved B injective over integer inventories.

Exactly eight candidate letters are available at each step, with one unit of **positive BRC source mass** per distinct ordered word. This free language is a constructed model, not an independently authorized native TRIADIC_CLOSURE_E Cell/Link/Port/time or rotation dynamics. Path length m is a source-order count and not an independent heartbeat-time coordinate. No signed-force amplitude cancellation is inferred from positive source counts.

## Theorem GW1 — Exact one-sum central return formula

Write Z_m for the number of ordered length-m words having *complete six-axis net Cell readout* Y=0, and P_m=Z_m/8^m. Then Z_(2n+1)=0 and for all integers n>=0,

\[
\boxed{Z_{2n}=\binom{2n}{n}\sum_{j=0}^{n}
 \binom{n}{j}^{2}\binom{2j}{j}\binom{2(n-j)}{n-j}.}
\]

In particular this reduces the four-index factorial sum of R762GU to an exact **single integer sum with n+1 terms**.

**Proof.** B is injective, hence Y=0 iff z=0. At each vertex the positive and negative letter counts must agree, say r_v, with sum r_v=n. Positive BRC ordered-word mass is
\[
Z_{2n}=(2n)!\sum_{r_0+r_1+r_2+r_3=n}\prod_{v=0}^3(r_v!)^{-2}.
\]
Let F(t)=sum_(r>=0) t^r/(r!)^2. Vandermonde's identity gives
\[
[t^j]F(t)^2=\frac{1}{(j!)^2}\sum_{a=0}^j\binom ja^2
=\frac{\binom{2j}j}{(j!)^2}.
\]
Convolve two such coefficients and multiply by (2n)!, observing that
(2n)!/[j!^2(n-j)!^2]=binom(2n,n)binom(n,j)^2. This proves the displayed formula, without removing any ordered-path multiplicity.

## Theorem GW2 — Two-peak BRC return asymptotic with first correction

For the *freely composable, equally weighted* signed STAR language, as n tends to infinity,

\[
\boxed{P_{2n}=\frac{2}{\pi^2n^2}
 \left(1-\frac{1}{2n}+O(n^{-2})\right),\qquad P_{2n+1}=0.}
\]

**Proof.** Inventory increments are the auxiliary nearest-neighbor moves +/-e_v in Z^4, each with probability 1/8. Their characteristic function is
\(\phi(\theta)=\frac14\sum_{v=0}^3\cos\theta_v\).
By the integer-injective map B and Fourier coefficient extraction on this *internal-index torus*,
\[
P_m=(2\pi)^{-4}\int_{[-\pi,\pi]^4}\phi(\theta)^m\,d\theta.
\]
There are precisely two points on the four-torus where |phi|=1: theta=0 and theta=(pi,pi,pi,pi). For even powers the two peak neighborhoods contribute equally. Elsewhere a compact strict bound |phi|<=rho<1 gives an exponentially small remainder.

Near zero put S_k=sum_v theta_v^k. Taylor expansion gives
\[
\log\phi=-S_2/8+S_4/96-S_2^2/128+O(\|\theta\|^6).
\]
Rescale theta=u/sqrt(n). For 2n steps, the local integrand is
\[
e^{-\|u\|^2/4}\left[
 1+\frac1n\left(\frac{\sum_v u_v^4}{48}
 -\frac{(\sum_vu_v^2)^2}{64}\right)
 +O(n^{-2}Q(u))\right]
\]
in the Gaussian-integrated sense for a fixed polynomial Q. One explicit justification is to restrict first to ||u||<=n^(1/12), use the sixth-order Taylor remainder and a Gaussian majorant there, bound the rest of a fixed small theta-neighborhood by exp(-c||u||^2), and bound the remaining compact torus by rho^(2n). Thus the integrated remainder is O(n^-2) *relative to the leading n^-2 factor*, justifying termwise integration.

Under the normalized Gaussian proportional to exp(-||u||^2/4), four independent coordinates have variance 2; therefore E(sum_v u_v^4)=48 and E((sum_v u_v^2)^2)=96. The relative order-1/n correction is 48/48-96/64=-1/2. The leading Gaussian integral is (4pi)^2=16pi^2. Two equal peaks and the (2pi)^-4 Fourier normalization give 2*16pi^2/(2pi)^4=2/pi^2. Each original source word is equiprobable, so these are exact positive BRC word-return probabilities. Odd-length return is forbidden by parity of sum_v z_v.

## Corollary GW3 — Refined ordered-source residual asymptotic

R762GV previously established that the zero-readout fiber is the **unique largest** positive BRC fiber at each positive even length and that its cardinality gives the exact minimum worst-case fixed-width repair for *complete ordered-word recovery* from (m,Y):
\[
b_{2n}=\lceil\log_2 Z_{2n}\rceil.
\]
Combining this existing rank/unrank theorem with GW2 sharpens its coarse O(log n) estimate to
\[
\boxed{\log_2 Z_{2n}
=6n-2\log_2 n+\log_2(2/\pi^2)
 -\frac{1}{2n\ln2}+O(n^{-2}).}
\]
The ceiling is applied to the exact finite integer value, not to a truncated asymptotic expansion. For recovery of the *whole source history*, the endpoint-only observer loses almost three bits per event, with a precisely quantified 2log_2 n saving. If future operations read only additive net Cell displacement, this provenance repair is unnecessary. This corollary does not assert an irreducible amount of native physical state or a seventh spatial dimension.

## Verification, distinctions and next unit

The reproducible R762GW_CHECK.py standard-library verifier implements the exact one-sum integer formula, independently reconstructs endpoint masses by an 8-branch integer BRC DP through m=8, checks totals and the known R762GU central counts through m=12, and prints float *diagnostics* for n=12,24,48,64,128. R762GW_EVIDENCE.json records those observations. The asymptotic and correction are established by the analytic proof above, not by numerical extrapolation. Author-side checker PASS. Independent mathematical review NOT_REVIEWED. A GitHub branch file is durable source evidence, not a native Source PROGRESS, Result, or theorem promotion.

Next research problem: construct or verify the actual typed TRIADIC_CLOSURE_E Cell/Link/Port and separate heartbeat-time gate, then test whether it preserves free eight-branch convolution. If it does not, classify the exact gate's return spectrum (periodicity, effective rank and possible absorption), without transferring the auxiliary Z^4 exponent to native dynamics without proof.
