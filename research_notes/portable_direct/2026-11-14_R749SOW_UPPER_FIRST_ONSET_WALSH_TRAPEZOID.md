# R749SOW — Exact upper-side Walsh first-onset trapezoid

Date: 2026-11-14. Status: AUTHOR_EXACT_NOT_REVIEWED.

Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Immediate predecessors: R749SOS–SOT, PR #2399 @5f2830988e31eae99d9ef11882e626b56b022552, and R749SOU–SOV, PR #2404 @986aa94c2ca6323207796b031deff0d7f1283e36.
This is the frozen **auxiliary 16-atom Walsh source observer**. Typed native X6/V29/V39 source-provenance correspondence remains unresolved.

## Exact theorem

Let K=F_2^4 and χ_m(k)=(-1)^popcount(k&m). Put A=χ_3, B=χ_12 and C=χ_15=AB. Define

p_(t,s,h,u,v,w,z)(k) =
[1+t A(k)+s B(k)+h C(k)+u χ_1(k)+v χ_2(k)+w χ_4(k)+z χ_8(k)]/16.

The compatible source fiber F_(t,s) consists of all choices of (h,u,v,w,z) making each of the 16 atoms nonnegative. Let ρ(t,s) be the minimax TV radius over arbitrary probability centers and ρ_cal(t,s) the minimax TV radius over centers in F_(t,s), and g=ρ_cal−ρ.

Consider the new **closed trapezoid**

\[
\mathcal T=\left\{(t,s):\quad \frac12\le s\le\frac{103}{200},\qquad
\frac{1+3s}{11}\le t\le\frac{614-820s}{825}\right\}.
\]

Its vertices are (5/22,1/2), (68/275,1/2), (509/2200,103/200), (639/2750,103/200), and its area equals **63/400000**.

**Theorem. For every real (t,s)∈𝒯, including all boundary points,**

\[
\boxed{\rho(t,s)=\frac{3-t+s}{8},\quad
\rho_{\mathrm{cal}}(t,s)=\frac{1+t}{3},\quad
g(t,s)=\frac{11t-3s-1}{24}.}
\]

Thus \(11t-3s=1\) is an **exact zero-gap segment** from (5/22,1/2) to (509/2200,103/200). Throughout the rest of 𝒯, where t>(1+3s)/11, the calibration gap is strictly positive. This extends the preceding s≤1/2 exact region to the *upper* side of the first-onset point.

## Exact free lower certificate

Write p(t,s,h,u,v,w,z) for the law above. The following two compatible sources are affine in (t,s):

\[
P_+=p(t,s,0,-t,-t,1-t,s),\qquad
P_-=p(t,s,0,t,t,t-1,-s).
\]

At the four vertices of 𝒯, all 16 atoms of each law are nonnegative and normalized. The signs of each atomwise difference P_+−P_- are weakly consistent across all four corners. Since the two laws depend affinely on the parameters, these conditions persist on all of 𝒯 and the fixed-sign TV sum gives exactly

\[
\operatorname{TV}(P_+,P_-)=\frac{3-t+s}{4}.
\]

Every probability center has maximum TV risk at least half this diameter; hence \(\rho\ge(3-t+s)/8\).

## Calibrated lower certificate

Translations \(k\mapsto k\oplus a\) for \(a\in\{0,3,12,15\}\) preserve A,B,C and map compatible sources to compatible sources. Averaging any calibrated center over this group preserves feasibility and does not increase its worst-case TV risk. Its only nonconstant surviving Walsh coefficients are A,B,C, so it has the form \(q_h=p(t,s,h,0,0,0,0)\).

Take the compatible source witnesses

\[
U=p(t,s,-t,0,0,-s-t,t-1),\qquad
V=p(t,s,1+t-s,0,0,t-s,t-s).
\]

Their exact atomwise nonnegativity at the four corners proves feasibility throughout 𝒯. Using the fixed signed TV-event vectors in canonical k=0,…,15 order,

\[
\sigma_U=(-1,-1,-1,-1,+1,-1,-1,+1,+1,-1,-1,+1,+1,+1,+1,+1),
\]
\[
\sigma_V=(+1,-1,-1,+1,-1,+1,+1,-1,-1,+1,+1,-1,+1,-1,-1,+1),
\]

the identity \(\operatorname{TV}(p,q)\ge\frac12\sum_k\sigma_k(p_k-q_k)\) yields, **for all real h**,

\[
\operatorname{TV}(U,q_h)\ge\frac{h+s+t+1}{4},\qquad
\operatorname{TV}(V,q_h)\ge\frac{1+t-s-h}{2}.
\]

The exact checker verifies these algebraic equalities at the four parameter corners and multiple independent h values; affine dependence proves them globally. Their maximum is minimized at \(h=(1+t)/3-s\) and has value \((1+t)/3\). Therefore \(\rho_{\mathrm{cal}}\ge(1+t)/3\).

## Explicit upper centers

Choose the feasible calibrated center

\[
q_{\mathrm{cal}}(t,s)=p\big(t,s,(1+t)/3-s,0,0,0,0\big).
\]

For the free center, reuse the full 16-component, exact-rational arrays Q00, DT, DS from R749SOV's companion executable (also included in the R749SOW executable):

\[
q_{\mathrm{free}}(t,s;k)=Q00[k]+(44t-10)DT[k]+100(s-49/100)DS[k].
\]

Here the second affine coefficient extends beyond the R749SOV range, so its validity is established by a **new** proof rather than presumed by extrapolation.

## Exhaustive 7D exact-rational upper certificate

In variables y=(t,s,h,u,v,w,z) form the joint polytope with 16 source-atom inequalities and four domain inequalities

\[
2s\ge1,\quad 200s\le103,\quad
11t-3s\ge1,\quad 825t+820s\le614.
\]

This polytope is bounded and full dimensional: take strict interior (t,s), and h=u=v=w=z=0. Every vertex is an intersection of at least seven linearly independent active facets. The companion standard-library Python executable enumerates **all \(\binom{20}{7}=77,520\)** seven-facet subsets, solves them by exact integer Bareiss elimination and Fraction back-substitution, and filters every candidate against all 20 inequalities. The observed, locally re-executed exact certificate is:

| Metric | Result |
|---|---:|
| Seven-facet combinations | 77,520 |
| Nonsingular bases | 37,184 |
| Feasible bases (including duplicates) | 784 |
| Distinct rational vertices | 200 |
| Distinct vertices over each of the four parameter corners | 50 |
| Max TV(p,q_free)−(3−t+s)/8 | 0 |
| Max TV(p,q_cal)−(1+t)/3 | 0 |
| Free / calibrated tight vertices | 77 / 72 |

Every checked vertex additionally satisfies nonnegative, normalized source and both center laws. The two upper-bound excesses are **convex** functions of the seven joint variables: both the source and each center are affine in (t,s,h,u,v,w,z), TV is convex, and the prescribed radius is affine. Every point in the bounded polytope is a convex combination of vertices, so both inequalities extend to **all real parameters and compatible sources**. Combined with the two matching lower certificates this proves the theorem.

The area is the average of horizontal widths 1/50 and 1/1000 multiplied by the vertical height 3/200:
\[
\operatorname{area}(\mathcal T) =
\frac12\left(\frac1{50}+\frac1{1000}\right)\frac3{200}
=\frac{63}{400000}.
\]

## Reproduction, evidence and next scientific question

- Python: \`python research_notes/portable_direct/R749SOW_EXTENSION_EXACT_CHECK.py\`
- Numerical certificate summary: \`research_notes/portable_direct/R749SOW_EXTENSION_RESULTS.json\`. Compare source/result scope, exact counts, maximum excesses and witness signs; the summary is a compact record, not necessarily a byte-for-byte copy of the program's stdout.
- Arithmetic: Python 3 standard library only, integers, Fraction, exact Bareiss; no floating-point acceptance tests.
- Proof coverage: all real (t,s)∈𝒯 and all compatible source distributions. Exact finite vertex completeness plus convexity and analytic lower witnesses establish universal quantification.
- Review: AUTHOR_EXACT_NOT_REVIEWED.

**Next:** Extend the exact zero segment \(11t-3s=1\) past \(s=103/200\), where the present free center eventually develops a positive upper-bound excess, by finding the next optimal affine center or a genuine phase-break witness. Solve the neighboring \(t<(1+3s)/11\) chamber to classify the zero-gap region on the other side. Preserve the original frozen scientific model and eventually identify any typed, future-operation-preserving correspondence to native X6/V29/V39.
