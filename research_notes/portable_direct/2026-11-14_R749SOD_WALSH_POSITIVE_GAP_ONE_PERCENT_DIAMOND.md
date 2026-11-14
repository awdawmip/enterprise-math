# R749SOD — Exact uniform positive Walsh calibration gap on the L1 diamond of radius 1/100

**Date:** 2026-11-14. **Status:** author-side analytic proof + complete rational polytope certificate; \`NOT_REVIEWED\`.

**Immutable scientific input:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
**Dependencies:** R749SNG (PR #2309, exact base minimax gap), R749SOB–SOC (PR #2365, base fiber and previous positive-gap diamond). These dependencies remain at their original scientific pins. This is an auxiliary 16-state Walsh observer/source model and does **not** identify a native X6/V29/V39 observer or operation.

## Statement

Let \(\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}\) on \(G=\mathbf F_2^4\), and write \(A=\chi_3\), \(B=\chi_{12}\), \(C=\chi_{15}=AB\). Define the nonempty source fiber

\[
\mathcal F_{t,s}=\left\{\mu_{t,s,h,u,v,w,z}(x)
 =\frac{1+tA(x)+sB(x)+hC(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16}
 \ge 0\;\forall x\in G\right\}.
\]

Let \(\rho(t,s)=\inf_{q\in\Delta(G)}\sup_{\mu\in\mathcal F_{t,s}}\mathrm{TV}(q,\mu)\) and \(\rho^{\mathrm{cal}}(t,s)=\inf_{q\in\mathcal F_{t,s}}\sup_{\mu\in\mathcal F_{t,s}}\mathrm{TV}(q,\mu)\). Set

\[
d=\left|t-\frac12\right|+\left|s-\frac12\right|,
\qquad e=|t-s|.
\]

**Theorem.** For every **real** \((t,s)\) with \(d\le1/100\),

\[
\boxed{\rho(t,s)\le\frac25+\frac d{12}},
\qquad
\boxed{\rho^{\mathrm{cal}}(t,s)\ge\frac9{22}-\frac{3e+15d}{22}}.
\]

Consequently,

\[
\boxed{g(t,s)=\rho^{\mathrm{cal}}(t,s)-\rho(t,s)
 \ge\frac1{110}-\frac{3e+15d}{22}-\frac d{12}
 \ge\frac1{110}-\frac{119}{132}d
 \ge\frac1{13200}>0.}
\]

The closed diamond has area \(2/100^2=1/5000\), exactly \(114921/10000=11.4921\) times the area of R749SOC's radius-\(1/339\) diamond. The stronger pointwise bound displays an anisotropic refinement by \(e\). Neither exact off-diagonal minimax values nor the genuine phase boundary are asserted.

## Proof 1 — explicit feasible adversarial witnesses and calibrated lower bound

The source fiber is invariant under translations \(x\mapsto x+3\) and \(x\mapsto x+12\): both fix \(A,B,C\), and they flip the respective pairs \((\chi_1,\chi_2)\) and \((\chi_4,\chi_8)\). Symmetrizing a calibrated prediction center over these four translations preserves \(\mathcal F_{t,s}\) and, by convexity of worst-case total variation, cannot increase its risk. It therefore suffices to lower-bound all calibrated centers of the form

\[
q_{\eta}(x)=[1+tA(x)+sB(x)+\eta C(x)]/16,
\]

with \(\eta\) ranging over the admissible nonnegative laws.

Let \(T_A=\{1,2,4,7,8,11,13,14\}\) and \(T_B=\{0,1,2,3,4,5,6,8,9,10,12\}\). In \(\mathcal F_{t,s}\) construct

\[
\mu_A=\mu_{t,s,\;1-e,\;0,0,0,0},
\qquad
\mu_B=\mu_{t,s,\;d,\;d-\frac12,d-\frac12,d-\frac12,d-\frac12}.
\]

For \(\mu_A\), the four values of its numerator indexed by \(A=\pm1,B=\pm1\) are nonnegative whenever \(t,s\in[0,1]\): the two mixed-sign values are \(2(t-s)_+\) and \(2(s-t)_+\), and the \(A=B=-1\) value is \(2-2\max(t,s)\). In our diamond \(t,s\in[49/100,51/100]\), so \(\mu_A\) is a law.

For \(\mu_B\), let
\(\mu_B^0=\mu_{1/2,1/2,\;0,\,-1/2,-1/2,-1/2,-1/2}\) and
\(r_0=\mu_{1/2,1/2,\;1/2,0,0,0,0}\). The R749SNG source witness \(\mu_B^0\) is nonnegative and \(r_0(x)\ge1/32\) for every atom. Exactly

\[
\mu_B=(1-2d)\mu_B^0+2d\,r_0+
 \frac{(t-\frac12)A+(s-\frac12)B}{16}.
\]

Since \(0\le d\le1/100\), the first term is nonnegative, the second contributes at least \(d/16\) at each atom, and the signed correction has magnitude at most \(d/16\) at each atom. Hence \(\mu_B\) is a compatible law for **every real parameter** in the diamond.

For any laws \(q,\mu\) and any event \(T\), \(\mathrm{TV}(q,\mu)\ge q(T)-\mu(T)\). Direct Walsh character summation on the displayed events gives

\[
L_A=q_\eta(T_A)-\mu_A(T_A)=\frac{1-e-\eta}{2},
\]

\[
L_B=q_\eta(T_B)-\mu_B(T_B)=\frac{6+3\eta-15d}{16}.
\]

Therefore the *nonnegative convex combination* eliminates the center's only free parameter:

\[
\frac{3L_A+8L_B}{11}=\frac{9-3e-15d}{22}.
\]

This lower-bounds the worst-case loss for every symmetrized calibrated center, hence for the calibrated minimax radius.

## Proof 2 — one fixed free center and a complete seven-dimensional exact certificate

Take the global free predictor

\[
q_0(x)=\frac{1+\frac35(A(x)+B(x))+\frac15C(x)}{16}.
\]

Its four distinct numerator values are \(12/5,\ 4/5,\ 4/5,\ 0\), so \(q_0\) is a probability law. We prove the pointwise upper bound

\[
\sup_{\mu\in\mathcal F_{t,s}}\mathrm{TV}(\mu,q_0)
   \le\frac25+\frac d{12}\qquad (d\le1/100).
\]

For signs \((\sigma,\tau)\in\{\pm1\}^2\), the corresponding closed quadrant of the diamond is described by
\(\sigma(t-\frac12)\ge0,\ \tau(s-\frac12)\ge0,\
\sigma(t-\frac12)+\tau(s-\frac12)\le1/100\).
In this quadrant \(d=\sigma(t-\frac12)+\tau(s-\frac12)\) is affine. The joint parameter-and-source region in \(y=(t,s,h,u,v,w,z)\in\mathbb R^7\) is a compact, full-dimensional polytope cut out by 16 atom-nonnegativity inequalities and these 3 region constraints. The function

\[
\Phi(y)=\frac12\sum_{x=0}^{15}|\mu_y(x)-q_0(x)|-\frac{d(y)}{12}
\]

is convex there: a sum of absolute values of affine functions minus an affine function. Its maximum occurs at a vertex. Every vertex has a 7-element independent active constraint set among the 19 defining halfspaces, so enumerating all \(\binom{19}{7}=50,388\) choices **per quadrant** is exhaustive.

The attached \`R749SOD_POSITIVE_GAP_DIAMOND_EXACT_CHECK.py\` uses only Python standard-library integer Bareiss elimination and exact \`fractions.Fraction\` arithmetic. It independently checks feasibility of each candidate vertex against all inequalities, deduplicates rational vertices, and evaluates \(\Phi\) exactly.

| Quadrant signs | Independent 7-facet candidates | Nonsingular | Feasible bases | Distinct vertices | Exact maximum \(\Phi\) |
|---|---:|---:|---:|---:|---:|
| \((+,+)\) | 50,388 | 24,992 | 1,184 | 58 | \(2/5\) |
| \((+,-)\) | 50,388 | 24,992 | 1,332 | 85 | \(2/5\) |
| \((-,+)\) | 50,388 | 24,992 | 1,332 | 85 | \(2/5\) |
| \((-,-)\) | 50,388 | 24,992 | 1,224 | 106 | \(2/5\) |

There are **201,552 complete seven-active-set tests**, with zero upper-bound violations. For an additional independent check, the same script enumerates the unsplit full diamond as a 20-facet seven-dimensional polytope: all \(\binom{20}{7}=77,520\) active sets, 35,456 nonsingular, 1,144 feasible bases, 138 distinct vertices. Its exact maximum unadjusted \(\mathrm{TV}(\mu,q_0)\) is \(481/1200=2/5+(1/100)/12\). The unsplit check independently verifies the uniform bound, while the quadrant checks prove the stronger *pointwise* \(d/12\) estimate.

Finite enumeration is used only on precisely stated rational polytopes with complete vertex coverage. Convexity yields the universal result for all real parameters and all compatible real sources; it is not extrapolation from samples.

## Synthesis, provenance and open obligations

Combining Proofs 1 and 2 gives \(g(t,s)\ge1/110-119d/132\). At \(d=1/100\), the right side is exactly \(1/13200\), positive. The analytic witness proof applies to all real parameters; the exact finite certificate checks the complete upper-bound geometry. At \(d=0\) it recovers the exact R749SNG baseline \(g(1/2,1/2)=1/110\).

Reproduce by running \`python3 R749SOD_POSITIVE_GAP_DIAMOND_EXACT_CHECK.py\` and compare its deterministic JSON stdout against \`R749SOD_POSITIVE_GAP_DIAMOND_RESULTS.json\`. Computation was performed locally on the submitted script, using exact rational arithmetic; external independent review and formal checker acceptance have **not** occurred. This model-internal result must not be promoted to native X6, V29, V39 or P000 semantics without an independently verified observation/operation-preserving map.

**Next scientific problem:** find a stronger lower-bound dual combination and a parameter-adaptive free predictor beyond the fixed \(q_0\), then certify an expanded off-diagonal region and locate a genuine \(g=0\) boundary rather than just the radius of this sufficient certificate. A separate native correspondence problem remains open.