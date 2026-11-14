# R749SPO — Exact full interval of calibrated Walsh minimax centers on an entire parameter slice

**Scientific status:** AUTHOR_EXACT_NOT_REVIEWED. **Model:** frozen auxiliary 16-atom Walsh fiber, not a native X6/V29/V39 result. **Frozen science:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Antecedents:** R749SPK (PR #2443), R749SPN (PR #2449).

## 1. Model and theorem

For k=0,...,15, write chi_m(k)=(-1)^{popcount(k&m)} and

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3+s\chi_{12}+h\chi_{15}+u\chi_1+v\chi_2+w\chi_4+z\chi_8}{16}.
\]

The source fiber F(t,s) contains the nonnegative laws of this form with the first two moments fixed. Total variation is TV(P,Q)=(1/2) sum_k |P(k)-Q(k)|. The free and calibrated minimax radii are rho=inf_{q in Delta_16} sup_{P in F} TV(P,q) and rho_cal=inf_{q in F} sup_{P in F} TV(P,q).

**Theorem (exact one-parameter center interval).** For every real t in [0,1/6], set s=1/2 and a(t)=1/2-3t. Then

\[
\rho(t,\tfrac12)=\rho^{\rm cal}(t,\tfrac12)=\frac{1-t}{2},
\]

and, for the Walsh-symmetric calibrated center family q_h=p_{t,1/2,h,0,0,0,0}, the complete set of optimal h values is **exactly**

\[
\boxed{\quad -a(t)\le h\le a(t),\qquad a(t)=\tfrac12-3t.\quad}
\]

For every 0<=t<1/6 there are continuously many distinct optimal centers in this family; at t=1/6 the interval collapses to the single h=0. At t=1/10 the exact interval is [-1/5,1/5], strictly extending the previously constructed [0,t] segment. The theorem characterizes the full optimal interval **within this specified one-coefficient center family**; classification of all five-dimensional calibrated minimax centers remains open.

## 2. Four-branch BRC feasibility and lower bound

Let a,b be signs of chi_3,chi_12. Retain full branch provenance by writing 16p_{abcd}=M_ab+cU_a+dV_b, where M_ab=1+at+bs+abh, U_a=u+av, V_b=w+bz. The sixteen nonnegativity inequalities are equivalent to M_ab>=|U_a|+|V_b| for each (a,b). For q_h, U=V=0. On the stated t interval, h=+/-a(t) satisfies all four M_ab>=0; the intermediate h values are feasible by convexity.

As in R749SPN, the two explicit compatible sources

\[
P_\pm=p_{t,1/2,0,-t,-t,\ \pm1/2,\ \pm(1-t)}
\]

are nonnegative. In fact their four BRC inequalities hold with equality. Their total variation is TV(P_+,P_-)=1-t. Thus every free center obeys the metric lower bound rho>=(1-t)/2. In particular the calibrated radius has the same lower bound.

## 3. Exact upper bound for both affine endpoints

It suffices to establish the common risk upper bound for q_+(t)=p_{t,1/2,a(t),0,0,0,0} and q_-(t)=p_{t,1/2,-a(t),0,0,0,0}. For arbitrary source coefficients x=(t,h_src,u,v,w,z), consider the compact six-dimensional rational polytope

\[
K=\{0\le t\le1/6;\quad 1+t\chi_3(k)+\tfrac12\chi_{12}(k)+h_{\rm src}\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)\ge0\ (k=0,\dots,15)\}.
\]

For each sign sigma in {+1,-1}, the excess TV(p_x,q_sigma(t))-(1-t)/2 is convex in x: total variation of a difference of two affine probability vectors is convex, while the benchmark radius is affine. Therefore it suffices to verify its value at every vertex of K. The source fiber boundedness and nonempty full-dimensional interior guarantee this standard vertex reduction.

The accompanying exact-integer Bareiss + rational arithmetic program enumerates all choose(18,6)=18,564 active-facet bases. It finds 9,536 nonsingular bases, 668 feasible solutions counted with repetition, and 78 distinct rational vertices. Both affine endpoint centers have maximum excess exactly 0; 34 vertices saturate each endpoint. The exact computation is finite and exhaustive for the declared K, without float tolerances. Convexity now gives the upper bound for all real t in the segment and all compatible sources. Every q_h between the two endpoints is their convex combination, so TV convexity in q establishes the same bound throughout [-a(t),a(t)].

For integer implementation clarity the program uses scaled variables X=6(t,h_src,u,v,w,z), and 18 integer halfspaces. The condition TV<= (1-t)/2 becomes the exact inequality

\[
\sum_{k=0}^{15}|(X_h-H)\chi_{15}(k)+X_u\chi_1(k)+X_v\chi_2(k)+X_w\chi_4(k)+X_z\chi_8(k)|\le16(6-X_t),
\]

where H=+/- (3-3X_t) is the scaled h coefficient at an affine endpoint.

## 4. Necessity of the two interval endpoints

Consider the single additional source, compatible for the entire interval,

\[
P^*(t)=p_{t,1/2,0,t,t,1-t,1/2}.
\]

Its BRC components are U_+=2t,U_-=0,V_+=3/2-t,V_-=1/2-t. All four BRC nonnegativity inequalities hold with equality. Writing y=|h|, elementary summation over the two internal signs c,d gives exactly

\[
TV(P^*(t),q_h)=\frac1{16}\sum_{A,B=\pm1}
\left[\max\{y,U_A+V_B\}+\max\{y,|U_A-V_B|\}\right].
\]

Here U_A,V_B are nonnegative on the stated interval. At y=a(t)=1/2-3t, the expression equals (1-t)/2. One of the eight maximum terms is max{y,1/2-3t}, and every other term is nondecreasing in y. Thus for y>a(t),

\[
TV(P^*(t),q_h)\ge\frac{1-t}{2}+\frac{y-a(t)}{16}>\frac{1-t}{2}.
\]

Consequently no h outside [-a(t),a(t)] is minimax in this prescribed family, completing the iff assertion.

## 5. Reproduction and next question

Run the exact self-contained standard-library verifier R749SPO_WALSH_CENTER_INTERVAL_EXACT_CERT.py and compare its JSON output with R749SPO_WALSH_CENTER_INTERVAL_RESULTS.json. The authorship check covers the finite joint source-parameter polytope and the algebraic necessity witness; all-real-t extension follows from convexity. Independent mathematical review has not occurred. The structural question remaining is the complete polytope of minimax calibrated centers with nonzero u,v,w,z, including the bifurcation at (t,s)=(1/6,1/2) and neighboring two-dimensional parameter cells. Native X6/V29/V39 provenance-preserving correspondence is a separate open question.
