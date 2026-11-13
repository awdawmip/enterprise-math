# R749SNS — Continuous piecewise-calibrated Walsh minimax polygon

Date: 2026-11-14. Classification: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED. Scientific domain: the frozen 16-state **auxiliary Walsh source observer** from awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. No native X6/V29/V39 correspondence, P000 modification, independent review or shared task CLAIM is asserted.

## 1. Model and statement

On the group \(G=\mathbb F_2^4\), let \(\chi_m(x)=(-1)^{\mathrm{popcount}(m\mathbin{\&}x)}\). The retained Walsh-moment masks are \(B_0=\{3,5,6,7,9,10,11,12,13,14\}\), with \(m_3=t,\ m_{12}=s\) and the other eight retained moments zero. Every compatible source law is

\[
\mu_{t,s,h,u,v,w,z}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+h\chi_{15}(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16},
\]

with all 16 atom masses nonnegative. Let \(\mathcal F(t,s)\) be this probability fiber and \(\mathrm{TV}(\mu,q)=\tfrac12\sum_x|\mu(x)-q(x)|\). Define the unrestricted and source-calibrated minimax radii respectively as

\[
\rho(t,s)=\min_{q\in\Delta(G)}\max_{\mu\in\mathcal F(t,s)}\mathrm{TV}(\mu,q),\quad
\rho^{\mathrm{cal}}(t,s)=\min_{q\in\mathcal F(t,s)}\max_{\mu\in\mathcal F(t,s)}\mathrm{TV}(\mu,q).
\]

We reuse the exact old R749SNO/R749SNR domain \(Q=\operatorname{conv}\{B,E,H,G_0\}\), with
\(B=(7/10,3/20),\ E=(1/2,3/10),\ H=(3/5,2/5),\ G_0=(1,0)\), area \(19/400\). On \(Q\), the previously established author-side result is \(\rho=\rho^{\mathrm{cal}}=(3+t-s)/8\).

Set three new parameter points \(A=(7/10,1/10),\ C=(3/5,7/40),\ D=(3/5,1/5)\), and define

\[
P_1=\operatorname{conv}\{A,B,C\},\qquad
P_2=\operatorname{conv}\{B,C,D\},\qquad
P_3=\operatorname{conv}\{B,D,E\}.
\]

**Theorem R749SNS.** For every real parameter pair in the nonconvex polygon

\[
\boxed{\mathcal P=Q\cup P_1\cup P_2\cup P_3,\qquad
\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{3+t-s}{8}.}
\]

An optimal calibrated center can be chosen continuously with
\[
q_{t,s}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+\eta(t,s)\chi_{15}(x)}{16},
\]
and the following piecewise-affine \(\chi_{15}\) coefficient:

\[
\eta(t,s)=
\begin{cases}
3/20-3s/2,&(t,s)\in P_1,\\
(t+s-1)/2,&(t,s)\in P_2,\\
(3t+5s-3)/2,&(t,s)\in P_3\cup N,\\
0,&(t,s)\in T.
\end{cases}
\]

Here the old \(Q=N\cup T\), where \(N=\operatorname{conv}\{B,E,G_0\}\) is the R749SNR affine chamber and \(T=\operatorname{conv}\{E,H,G_0\}\) is the R749SNO zero-residual center chamber. Each pair of adjacent affine formulas agrees identically along the common edge: \(BC,BD,BE,EG_0\). At \(B,C,D,E\), the respective shared values are \(-3/40,-9/80,-1/10,0\).

The simple polygon has cyclic boundary
\[
A\to B\to G_0\to H\to E\to D\to C\to A.
\]
The triangle interiors are pairwise disjoint and are disjoint from the old Q interior. Its exact area, by the shoelace formula, is

\[
\boxed{|\mathcal P|=\frac{43}{800}
=\frac{19}{400}+\frac1{400}+\frac1{800}+\frac1{400}.}
\]

The new material certifies \(1/160\) additional area, an increase of \(5/38\) (about 13.16%) relative to the old \(Q\).

## 2. Unrestricted lower bound on all new chambers

Translations of \(G\) by the xor masks 3 and 12 preserve each Walsh fiber. Averaging any predictor over the resulting four-element translation group cannot increase its worst-case TV risk. Each averaged law belongs to the span \(\{1,\chi_3,\chi_{12},\chi_{15}\}\).

For the fixed event \(S=\{3,5,7,9,11,13,14,15\}\), the character sums of \(\chi_3,\chi_{12},\chi_{15}\) all vanish; thus every such averaged predictor has \(q(S)=1/2\). Construct the affine compatible source
\[
W_{t,s}=\mu_{t,s,0,s-1,-t,-s,-s}.
\]
All 16 atom masses of W are nonnegative at all vertices of each \(P_i\) as checked by exact Fractions; therefore W is feasible at every real point of each triangle by affinity. The direct event sum is
\[
W_{t,s}(S)-1/2=(3+t-s)/8.
\]
The variational event inequality then gives the same lower bound for unrestricted, and consequently calibrated, minimax risk on \(P_1\cup P_2\cup P_3\).

## 3. Exact joint-fiber upper certificates

The decoder q has the required ten source moments automatically. Its atom masses are nonnegative at each parameter-triangle vertex and therefore throughout the triangle. Thus it is a valid calibrated predictor.

For each chamber, form the **joint** 7-dimensional source-parameter polytope in \((t,s,h,u,v,w,z)\); it has 16 atom nonnegativity inequalities and three triangle inequalities. With \(y=40(t,s,h,u,v,w,z)\), the source inequalities have rows \((\chi_3(x),\chi_{12}(x),\chi_{15}(x),\chi_1(x),\chi_2(x),\chi_4(x),\chi_8(x))\cdot y\ge-40\). The additional parameter inequalities are:

| Chamber | Exact triangular parameter constraints |
|---|---|
| P1 | \(t\le7/10,\quad3t+4s\ge5/2,\quad t+4s\le13/10\) |
| P2 | \(t\ge3/5,\quad t+4s\ge13/10,\quad t+2s\le1\) |
| P3 | \(3t+4s\le27/10,\quad t+s\ge4/5,\quad t+2s\ge1\) |

Every such polytope is compact and full-dimensional. Every vertex must be the intersection of seven independent active constraints. The accompanying standard-library checker exhaustively enumerates all \(\binom{19}{7}=50,388\) active bases per region, solves exactly with integer Bareiss elimination, checks all 19 inequalities with rational arithmetic, and deduplicates vertices. At every feasible vertex it checks the inequality
\[
\Delta(t,s,h,u,v,w,z)
=\mathrm{TV}(\mu_{t,s,h,u,v,w,z},q_{t,s})-(3+t-s)/8\le0.
\]

| Complete exact vertex check | P1 | P2 | P3 |
|---|---:|---:|---:|
| All bases | 50,388 | 50,388 | 50,388 |
| Non-singular bases | 27,648 | 27,600 | 28,912 |
| Feasible bases | 756 | 904 | 928 |
| Distinct rational vertices | 124 | 114 | 116 |
| Equality vertices | 40 | 28 | 36 |
| Violating vertices | **0** | **0** | **0** |
| Maximum exact excess | 0 | 0 | 0 |

Within each chamber, q is affine in (t,s), and \(\Delta\) is a convex function on the entire joint polytope (TV of an affine difference minus an affine target). Hence its maximum occurs at an extreme point. The exhaustive exact certificates prove the upper bound for **all real** parameter points, not just sampled parameters or triangle corners. Combined with the lower witness and the previously verified R749SNO/R749SNR theorem on Q, this establishes the displayed equality on \(\mathcal P\).

## 4. An exact warning about naïve affine gluing

A single affine coefficient that interpolates three valid vertex decoders need not work over the triangle they span. For \(\operatorname{conv}\{B,E,C\}\), the naïve interpolating coefficient is
\[
\eta_{\mathrm{naive}}(t,s)=3t/4+3s/2-33/40.
\]
At \((t,s)=(17/30,13/60)\), choose the feasible source coefficients
\[
(h,u,v,w,z)=(-13/60,-47/60,-47/60,0,0).
\]
Both source and interpolated decoder are nonnegative probability laws, but exact arithmetic gives
\[
\mathrm{TV}(\mu,q_{\mathrm{naive}})=41/96
=67/160+1/120
>\underbrace{(3+t-s)/8}_{67/160}.
\]
This proves a limitation of **that specific predictor**, not a positive minimax calibration gap. It also justifies verifying joint source-parameter polytopes rather than inferring an interior result from independent endpoint fibers.

## 5. Reproduction, scope and continuation

Run the companion Python standard-library program R749SNS_CONTINUOUS_WALSH_POLYGON_EXACT_CHECK.py, and compare its complete deterministic stdout to R749SNS_CONTINUOUS_WALSH_POLYGON_RESULTS.json. Integer Bareiss and Fraction calculations establish exact (not floating-point) vertex checks and the stated counterexample; the script asserts shared-edge continuity, lower-witness positivity, polygon areas and all three region checks. The new region is not asserted to be the **maximal** zero-gap domain.

Previously saved inputs are preserved: R749SNO in PR #2339 supplies the old T triangle, and R749SNR in PR #2344 supplies the old N triangle, both on the same frozen auxiliary source pin. No prior scientific files, Activity records, identities, Result/Review records or Task CLAIMS need rewriting.

**Next discriminating problem:** build the adjacent chambers across AC, CD and DE, seek an exact positive \(\rho^{\rm cal}-\rho\) witness if one exists, and separately test whether any signed-Port/provenance-preserving mapping to the native X6/V29/V39 observer can be proved. The present theorem is author-side exact mathematics, pending independent review.
