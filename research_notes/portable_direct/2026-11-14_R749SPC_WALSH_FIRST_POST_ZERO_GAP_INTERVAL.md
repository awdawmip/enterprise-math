# R749SPC — Exact onset of a positive Walsh calibration gap on s=3/5

Date: 2026-11-14. Status: AUTHOR_EXACT_NOT_REVIEWED.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessors: R749SPA–SPB at PR #2417, immutable commit 6e2be5b2a2bb3c37e0aa4c28b9f1b893a446477f.
This is a complete auxiliary 16-atom Walsh observer calculation; no native X6/V29/V39 dynamics transfer is asserted. Independent mathematical review pending.

## 1. Exact theorem

Let K=F_2^4, chi_m(k)=(-1)^popcount(k&m) and

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

For fixed (t,s), let F_{t,s} be **all** nonnegative normalized members of this seven-coefficient family. Let TV(p,q)=sum_k |p(k)-q(k)|/2. Write rho(t,s) for the minimax TV radius with an arbitrary 16-atom probability center, rho_cal(t,s) for the same radius with center constrained to F_{t,s}, and g=rho_cal-rho.

**Theorem.** For every real t in [2/5,1/2], with s=3/5,

\[
\boxed{\rho(t,3/5)=3/5-t/2,\qquad
\rho^{\rm cal}(t,3/5)=14/25-2t/5,\qquad
g(t,3/5)=(t-2/5)/10.}
\]

In particular g=0 at t=2/5 and g>0 for **every** 2/5<t<=1/2. R749SPA–SPB already established g=0 throughout 0<=t<=2/5. Together these results fix the first strictly positive calibration gap on the full interval 0<=t<=1/2.

Explicit optimal free and calibrated centers are, respectively,

\[
q_f(t)=p_{2t-4/5,\,1,\,2t-4/5,\,0,0,0,0},\qquad
q_c(t)=p_{t,\,3/5,\,\frac95(t-2/5),\,0,0,0,0}.
\]

Both are probability laws for the whole interval, and q_c belongs to the compatible source fiber. At t=1/2 the exact free radius is 7/20, the calibrated radius 9/25 and g=1/100. At t=2/5 both radii are 2/5.

## 2. Free lower certificate: two compatible source laws

Define the two source families

\[
P_+(t)=p_{t,3/5,t-2/5,2/5,2/5,1-t,1-t},
\qquad P_-(t)=p_{t,3/5,t-2/5,-2/5,-2/5,t-1,t-1}.
\]

Every source atom is affine in t. Exact nonnegativity and normalization at t=2/5 and t=1/2 therefore establish source feasibility at every real intermediate t. The 16 atomwise difference signs are endpoint-consistent (zero permitted); exact total variation is

\[
\operatorname{TV}(P_+(t),P_-(t))=6/5-t.
\]

The TV triangle inequality forces any probability center to have worst-case source radius at least (6/5-t)/2=3/5-t/2.

## 3. Calibrated lower certificate: two event witnesses

Let G={d in F_2^4 : chi_3(d)=chi_12(d)=1}. Translation of atom indices by any d in G preserves TV and the complete source fiber: coefficients t,s,h stay fixed, and u,v,w,z only change signs. Symmetrizing any calibrated center over the four translations keeps it in the source fiber, removes the four latter Walsh characters, and cannot increase its worst-case source risk by convexity and source-fiber invariance. Thus the calibrated minimax value may be obtained among centers q_h=p(t,3/5,h,0,0,0,0).

Let S_1(t)=P_-(t) and let

\[
S_2(t)=p_{t,3/5,t+2/5,0,0,t-3/5,t-3/5}.
\]

Both are compatible sources for all real t in the claimed interval, as follows from endpoint atom nonnegativity. On the fixed index events

\[
E_1=\{7,11,12,13,14,15\},\qquad
E_2=\{0,3,5,6,9,10,12,15\},
\]

exact Walsh expansion gives, for all real h and all real t,

\[
S_1(t)(E_1)-q_h(E_1)=13/20-5t/8+h/8,
\]
\[
S_2(t)(E_2)-q_h(E_2)=1/5+t/2-h/2.
\]

For any event E, TV(P,Q)>=P(E)-Q(E). Thus the calibrated risk is at least the maximum of these two affine functions of h. One increases while the other decreases. Their intersection, at h_*(t)=9(t-2/5)/5, is the global minimizer of that maximum and has value 14/25-2t/5. This proves the calibrated lower bound for any member of F_{t,3/5}. The attached exact checker tests the event identities at the four corners (t,h) in {2/5,1/2} x {-1,1}, establishing the entire affine identity; it also checks all required source endpoint probabilities.

## 4. Matching upper bounds: exhaustive exact joint-polytope certificate

Let J be the six-dimensional joint polytope in variables x=(t,h,u,v,w,z) defined by all 16 source-atom nonnegativity inequalities for fixed s=3/5 and 2/5<=t<=1/2. It is compact because source Walsh coefficients of a probability law lie in [-1,1]. It is full-dimensional: at t=9/20,h=1/10,u=v=w=z=0 all inequalities, including t bounds, are strict.

The script R749SPC_WALSH_RIGHT_ONSET_CERT.py translates these constraints into 18 **integer** inequalities, checks all C(18,6)=18,564 active-facet combinations using exact integer Bareiss elimination and Fraction back-substitution, excludes singular or infeasible combinations, and deduplicates vertices. It then checks exact normalization/nonnegativity and the two upper inequalities

\[
TV(p_x,q_f(t))<=3/5-t/2,\qquad
TV(p_x,q_c(t))<=14/25-2t/5
\]

at every one of the 40 exact vertices.

| Exact joint-polytope metric | Verified value |
|---|---:|
| Active basis combinations | 18,564 |
| Nonsingular | 9,536 |
| Feasible bases including repetitions | 780 |
| Distinct exact vertices | 40 |
| Vertex t values | 20 at 2/5 and 20 at 1/2 |
| Free/calibrated tight vertices | 16 / 16 |
| Maximum risk excess, free/calibrated | 0 / 0 |
| Checker | PASS |

Every atomwise difference p_x-q_f(t) or p_x-q_c(t) is affine in x, and both target radii are affine in t. Hence each risk-minus-radius is a convex function on J. Because every point of compact J is a convex combination of its vertices, the zero-max-excess certificate proves both upper inequalities for all real x in J, not only sampled t. These upper bounds exactly match the lower certificates, completing the theorem.

The center q_f is a valid unrestricted probability center, but has chi_12 coefficient 1 rather than the source's 3/5; this exhibits the mechanism generating the positive gap. The source carrier is never quotient-collapsed in the vertex check. Averaging in Section 3 applies only to prediction-center optimization with its explicitly specified TV observer and group invariance.

## 5. Files, review scope and next frontier

Research files in the same directory: this manuscript, R749SPC_WALSH_RIGHT_ONSET_CERT.py, R749SPC_WALSH_RIGHT_ONSET_RESULTS.json. Run the pure-standard-library Python 3 checker and compare its exact JSON stdout with the saved results. Frozen input and all hypotheses remain unchanged. This is an author-side reproducible exact theorem, awaiting independent review.

Next mathematical unit: determine the next optimal-radius phase just above t=1/2 on the s=3/5 slice; preliminary numerical LP indicates a new free-center transition. Obtain exact matching source/event lower witnesses and exhaustive parameter-polytope upper certificates before extending the real theorem. Separately, investigate the observer/provenance-preserving transport needed for genuine native X6/V29/V39 BRC event operations.
