# R749SNA — Complete flat-axis theorem for the disjoint-edge Walsh minimax fiber

Date: 2026-11-13 (Asia/Shanghai). Lineage: R749SMX, R749SMY, R749SMZ. Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, unchanged. Status: author-side proof plus exact finite vertex certificate; independent review pending. Model: auxiliary signed-source observer, not a claimed native V29/V39 event.

## Setting and theorem

Let G=F_2^4, chi_k(x)=(-1)^(k·x), C={1,2,4,8,15}, and B={3,5,6,7,9,10,11,12,13,14}. Let F(t,s) consist of source laws mu with B-Walsh moments m_3=t, m_12=s and the other eight B moments zero, for real t,s in [-1,1]. Total variation is TV(p,q)=sum_x |p(x)-q(x)|/2. Define unrestricted minimax radius rho_B(t,s)=min_{q in Delta(G)}max_{mu in F(t,s)}TV(q,mu), and calibrated radius rho_B^cal(t,s) by restricting q to F(t,s).

**Full-axis theorem:** For every t,s in [-1,1],

\[
\boxed{\rho_B(t,0)=\rho_B^{cal}(t,0)=\tfrac12,\qquad
       \rho_B(0,s)=\rho_B^{cal}(0,s)=\tfrac12.}
\]

On s=0 the calibrated optimal decoder is q_t(x)=(1+t chi_3(x))/16. On t=0 it is q_s(x)=(1+s chi_12(x))/16. The result includes both endpoints and the entire real interval, not only sampled rational points.

## Complete proof

On s=0, Walsh inversion gives the unique representation

\[
\mu(x)=\frac{1+t\chi_3(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)+h\chi_{15}(x)}{16}.
\]

The feasible six-variable vector (t,u,v,w,z,h) belongs to the bounded full-dimensional rational polytope P defined by the sixteen inequalities 16 mu(x)>=0. Boundedness follows because all coordinates are Walsh moments of probability measures. The origin satisfies all sixteen inequalities strictly. Hence every vertex has at least six linearly independent active facets.

The companion exact Fraction checker enumerates every one of the C(16,6)=8008 choices of six active constraints; 3520 have nonsingular coefficient matrices, 1920 produce feasible solutions, and these deduplicate to exactly 18 vertices. The t coordinates of the 18 vertices have multiplicities {-1:2,-1/2:4,0:6,1/2:4,1:2}. For exactly 10 vertices TV(mu,q_t)=1/2 and for the remaining 8 vertices it equals 3/8. This enumeration uses exact rational Gaussian elimination, all sixteen inequalities, and all possible six-facet bases. The 18 vertices form the entire vertex set because P is full-dimensional and bounded.

Moreover,
\[
\operatorname{TV}(\mu,q_t)=\frac1{32}\sum_{x\in G}
|u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)+h\chi_{15}(x)|.
\]
This is a convex function jointly in all six coordinates, so its maximum on P is attained at a vertex. The exact complete vertex certificate establishes TV(mu,q_t)<=1/2 for every real feasible (t,u,v,w,z,h), giving the uniform upper bound for the continuum of axis fibers. The decoder q_t itself is normalized, nonnegative and has precisely the required retained B moments, so it is calibrated.

For each t in [-1,1], define the two source laws
\[
\mu_\pm(x)=\frac{(1+t\chi_3(x))(1\pm\chi_1(x))}{16}.
\]
They are nonnegative, normalized and have retained moments exactly m_3=t and all other B moments zero: multiplication adds only masks 1 and 2=3 xor 1, both omitted in C. Their supports lie on disjoint chi_1 sign classes, so TV(mu_+,mu_-)=1. By the triangle inequality every proposed decoder q has worst-case TV error at least 1/2. Combining the lower bound with the calibrated q_t upper bound proves both first-axis identities.

A permutation of source bits swapping 1 with 4 and 2 with 8 preserves C and B, fixes the mask 15, and exchanges masks 3 and 12. It preserves TV, source-fiber compatibility and calibration. Thus the identical statement and explicit decoder hold on the other axis.

## Verification and novelty

\`R749SNA_AXIS_FLAT_EXACT_CHECK.py\` implements the full 8008-active-set enumeration, exact vertex classification, exact TV histogram, and independently checks a disjoint-support witness for seven rational t values. Actual author-side execution: PASS. \`R749SNA_AXIS_FLAT_RESULTS.json\` contains the complete machine-readable counts. The finite rational certificate proves the all-real-axis bound via polytope convexity; it is not an extrapolation from those seven witnesses.

R749SMZ proved the origin (0,0) by a sum-free argument. This theorem extends that result to both complete axes, showing the calibrated/unrestricted penalty is zero throughout those axes. R749SMY proves a strictly positive penalty 8/225 at the interior point (1/3,1/3), providing a concrete geometric distinction between axis and interior fibers. The deterministic boundary-edge formula in R749SMX remains a separate, compatible result.

## Next scientific problem

Determine the exact piecewise-parametric interior function rho_B(t,s) and its calibrated counterpart, with exact transition curves and dual certificates; specifically test whether any positive-area neighborhood of the axes retains the flat value. The abstract Walsh source result does not yet supply the native licensed V29/V39 Cell/Link/Port correspondence or independent scientific review.