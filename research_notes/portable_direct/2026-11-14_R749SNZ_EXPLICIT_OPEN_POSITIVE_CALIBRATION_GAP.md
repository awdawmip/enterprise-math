# R749SNZ — An explicit two-dimensional open region of strictly positive Walsh calibration penalty

Date: 2026-11-14. Scientific status: **AUTHOR_ANALYTIC_PROOF / NOT_REVIEWED**.
Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Prior exact diagonal theorem: R749SNG, PR #2309, commit `74abff6fff03fb6defec95c6c505c69ea5b0832c`.
This is a result **only** in the auxiliary 16-state Walsh source-observer model; it neither changes P000 nor asserts a native X6/V29/V39 mapping.

## 1. Exact statement

For ((t,s)in[-1,1]^2), let (F_{t,s}) be the nonempty family of probability laws on (G=(\mathbb Z/2)^4) whose Walsh spectrum has prescribed coefficients (m_3=t,m_{12}=s), the eight zero coefficients (m_5,m_6,m_7,m_9,m_{10},m_{11},m_{13},m_{14}=0), and free coefficients (m_{15},m_1,m_2,m_4,m_8). Equivalently,

\[
\mu(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+h\chi_{15}(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16},
\]

with nonnegative atom masses. Let (\rho(t,s)) be the unrestricted minimax total-variation prediction radius of this source fiber; let (\rho^{\mathrm{cal}}(t,s)) be the minimax radius when the center must lie in the fiber.

**Theorem R749SNZ (explicit positive-gap diamond).** For every real pair satisfying

\[
\boxed{|t-\tfrac12|+|s-\tfrac12|\le \frac1{4455}},
\]

the entire fiber is nonempty and

\[
\boxed{\rho^{\mathrm{cal}}(t,s)-\rho(t,s)\ge\frac1{220}>0.}
\]

More precisely, writing (\delta=|t-1/2|+|s-1/2|),

\[
\boxed{\rho^{\mathrm{cal}}(t,s)-\rho(t,s)\ge
\frac1{110}-\frac{81}{4}\,\delta}
\]

for all (\delta\le1/4455). This is an explicitly certified **two-dimensional neighborhood with nonempty interior and a uniform strictly positive gap**, supplementing the diagonal strictly positive gap proved by R749SNG.

## 2. Uniform explicit transport between nearby source fibers

Fix (p=(t,s)) and (p'=(t',s')) with (|t|,|s|,|t'|,|s'|\le3/5), and (\delta=|t'-t|+|s'-s|\le4/25). Define a strictly positive canonical member of (F_p):

\[
r_p(x)=\frac{(1+t\chi_3(x))(1+s\chi_{12}(x))}{16}
=\frac{1+t\chi_3+s\chi_{12}+ts\chi_{15}}{16}.
\]

Both factors are at least (2/5), so (r_p(x)\ge1/100) for all sixteen atoms. For any (\mu\in F_p), set

\[
\varepsilon=\frac{25}{4}\,\delta\le1,\qquad
T_{p\to p'}\mu(x)
=(1-\varepsilon)\mu(x)+\varepsilon r_p(x)
+\frac{(t'-t)\chi_3(x)+(s'-s)\chi_{12}(x)}{16}.
\]

This is normalized, and its preserved Walsh moments are exactly those of (F_{p'}). Each atom is at least

\[
\frac{\varepsilon}{100}-\frac{\delta}{16}=0,
\]

because ((1-\varepsilon)\mu\ge0). Thus (T_{p\to p'}\mu\in F_{p'}) for **every** source law, not just the canonical member.

The total-variation transport cost satisfies

\[
\operatorname{TV}(\mu,T\mu)
\le\varepsilon\operatorname{TV}(\mu,r_p)
+\frac12\sum_{x\in G}\left|
\frac{(t'-t)\chi_3(x)+(s'-s)\chi_{12}(x)}{16}\right|
\le\varepsilon+\frac\delta2
=\frac{27}{4}\delta.
\]

The same construction works in the opposite direction because (p') remains in the same closed box. Therefore the two compact fibers have (total-variation) Hausdorff distance at most (H=(27/4)\delta).

## 3. Stability of unrestricted and calibrated minimax radii

For any nonempty compact source sets (A,B) in the finite probability simplex with TV Hausdorff distance at most (H), and for any prediction (q), the two worst-case source losses differ by at most (H) by the triangle inequality. Taking the minimum over the **common full simplex** gives

\[
|\rho(A)-\rho(B)|\le H.
\]

For calibrated prediction, choose an optimal (q_A\in A) (compactness). Hausdorff proximity supplies some (q_B\in B) with (\operatorname{TV}(q_A,q_B)\le H); and every source (\mu_B\in B) has a matching (\mu_A\in A) within (H). Hence

\[
\max_{\mu_B\in B}\operatorname{TV}(q_B,\mu_B)
\le\rho^{\mathrm{cal}}(A)+2H.
\]

Interchanging (A,B) gives (|\rho^{\mathrm{cal}}(A)-\rho^{\mathrm{cal}}(B)|\le2H), so their calibration penalties differ by at most (3H=(81/4)\delta).

## 4. Exact positive base point and quantitative neighborhood

At (p_0=(1/2,1/2)), R749SNG proves exactly

\[
\rho(p_0)=\frac25,\qquad
\rho^{\mathrm{cal}}(p_0)=\frac9{22},\qquad
\rho^{\mathrm{cal}}(p_0)-\rho(p_0)=\frac1{110}.
\]

Let (\delta=|t-1/2|+|s-1/2|\le1/4455). Both points are in the box (\{|t|,|s|\le3/5\}), and (\delta<4/25). The stability bound implies

\[
\rho^{\mathrm{cal}}(t,s)-\rho(t,s)
\ge\frac1{110}-\frac{81}{4}\delta
\ge\frac1{110}-\frac{81}{4\cdot4455}
=\frac1{220}.
\]

This proves the closed diamond theorem, and hence strict positive calibration cost on its nonempty open interior. Its exact Euclidean parameter area is (2/4455^2). No floating-point or limiting argument enters the proof.

## 5. Evidence, scope and next problem

The analytic proof relies on (i) R749SNG's immutable already-checked **single diagonal point** and (ii) explicit finite-measure transport and minimax triangle inequalities. The attached `R749SNZ_POSITIVE_GAP_NEIGHBORHOOD_EXACT_CHECK.py` validates every rational constant, all 16 canonical support atoms at the relevant box corners, the strict radius conditions and diamond area by Python `Fraction`. This helper is an **arithmetic check of the written analytic proof**, not an exhaustive enumeration of a continuous diamond.

This positive-gap open set is disjoint from the nearby-to-origin zero-gap triangles of R749SNY and supplies an exact two-dimensional contrast. Author proof remains **NOT_REVIEWED**; no formal Result, shared Task CLAIM, mathematical admission or native event correspondence is asserted.

**Next:** sharpen the conservative Lipschitz constants and determine the actual transition curve between the zero-calibration regions and the positive-gap neighborhood, including testing whether it admits a finite piecewise-rational description.
