# R749SNN — Exact full boundary-ray zero-calibration theorem for Walsh minimax

Date: 2026-11-14. Source: auxiliary 16-state Walsh model frozen at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Direct continuation of R749SNM and R749SNL. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED; no native X6/signed-Port/V29/V39 correspondence or P000 update.

## Exact theorem

Let G=F_2^4 and chi_m(x)=(-1)^popcount(m&x). Retain Walsh moment indices B={3,5,6,7,9,10,11,12,13,14}; set m_3=t, m_12=s and the other eight retained moments to zero. Let F(t,s) be the compatible probability fiber and TV(mu,q)=sum_x |mu(x)-q(x)|/2. Define unrestricted and moment-calibrated minimax radii:

    rho(t,s)=min_{q probability}max_{mu in F(t,s)}TV(mu,q)
    rho_cal(t,s)=min_{q in F(t,s)}max_{mu in F(t,s)}TV(mu,q).

**Theorem.** For all real numbers 3/5<=t<=1 with s=1-t,

    rho(t,1-t)=rho_cal(t,1-t)=(1+t)/4.

This extends the preceding R749SNM polygon's segment on t+s=1 from t<=4/5 all the way to t=1; it is an exact whole-real-interval result, not a finite-grid fit.

## Lower certificate

Write A=chi_3, D=chi_12, AD=chi_15, U=chi_1, AU=chi_2, V=chi_4, DV=chi_8. Every source is

    mu_(t,s,h,u,v,w,z)(x)
    =[1+t A(x)+s D(x)+h AD(x)+u U(x)+v AU(x)+w V(x)+z DV(x)]/16.

Translation by the xor masks 3 and 12 preserves the fiber and averages all characters except 1,A,D,AD to zero. By convexity of the worst-case total variation, every unrestricted center can be replaced by an invariant center without increasing the worst-case error.

Choose the affine source W(t,s)=(h,u,v,w,z)=(0,s-1,-t,-s,-s). For each endpoint t=3/5 and t=1, with s=1-t, W has 16 nonnegative atom masses and total 1; source feasibility follows throughout the line segment by affinity. On E={3,5,7,9,11,13,14,15}, all A,D,AD Walsh sums vanish. Every invariant center assigns mass exactly 1/2 to E. Direct substitution gives W(E)-1/2=(1+t)/4. Hence rho(t,1-t)>=(1+t)/4, and the same lower bound holds for the calibrated radius.

## Calibrated upper witness and exhaustive exact certificate

The center q_t(x)=[1+t A(x)+(1-t)D(x)]/16 is nonnegative, normalized and has all required Walsh moments for 0<=t<=1.

Let the six free variables be (t,h,u,v,w,z). Scale them by L=5: y=5(t,h,u,v,w,z). The joint source/parameter polytope is defined by sixteen inequalities, one per x, with integer row

    (A(x)-D(x), AD(x), U(x), AU(x), V(x), DV(x))

and right-hand side -5*(1+D(x)), together with t>=3/5 and t<=1, represented by rows (1,0,0,0,0,0) >=3 and (-1,0,0,0,0,0)>=-5.

This compact convex polytope is bounded, nonempty and full-dimensional in its affine 6-coordinate representation. Each vertex is found among intersections of six independent inequalities. The attached exact Python code enumerates all C(18,6)=18,564 six-facet combinations with integer Bareiss elimination and Fraction reconstruction; it checks all constraints, deduplicates rational vertices, and verifies at each vertex

    TV(mu_(t,1-t,h,u,v,w,z),q_t) <= (1+t)/4.

Output: 10,848 nonsingular bases; 2,704 feasible bases; 24 distinct exact rational vertices; 10 vertices attaining equality; zero upper-bound violations.

The function TV(mu,q_t)-(1+t)/4 is convex in the six joint variables. Thus a maximum on this polytope is attained at a vertex. The finite exhaustive exact check therefore proves the inequality for **all** real t in [3/5,1], not just sampled endpoints. The explicit lower certificate proves equality and calibration optimality.

## Verification, limitations, next research question

Run: python research_notes/portable_direct/R749SNN_WALSH_BOUNDARY_LINE_EXACT_CHECK.py

Its result is recorded in R749SNN_WALSH_BOUNDARY_LINE_RESULTS.json; all arithmetic is standard-library integer and Fraction. Independent mathematical review remains pending. The line theorem is about the auxiliary Walsh observer only, not a licensed X6 future observer.

Next: characterize the complete two-parameter chamber around the upper boundary t+s=1 and the exact phase boundary in its interior, noting that this additional line segment lies outside the R749SNM four-sided polygon.