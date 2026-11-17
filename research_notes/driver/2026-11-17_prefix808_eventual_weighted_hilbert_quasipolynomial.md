# PREFIX-808 — Exact eventual weighted Hilbert quasi-polynomial for high-carry cokernels

Date: 2026-11-17. **Author-side algebraic corollary (not independent Native review)**, derived by EM-DVR-DEBB5E from the pinned Reeve/Kummer carry structure; original TU/Reeve observer source EM-DIRECT-4660FF.

## Inputs and scope

Fix any field K, h≥2 and positive e|d|h. Put n=d/e, H=h/d and S=K[U_0,U_1,U_2,U_3], A=U_0U_3, B=U_1U_2, I=(A,B). Let M_k be the ek-character module of D_h=S[z_0,z_1]/(z_0^h-A,z_1^h-B), with 0≤k<n, and J_d the degree-d invariant monomial ideal. For c≥1 define E_{k,c}=M_k/J_d^cM_k.

Use the **explicit integral positive grading** deg(U_i)=h and deg(z_0)=deg(z_1)=2. Let

    r_q=ek+qd, N_q=#{(a,b): 0≤a,b<h, a+b=r_q},
    m_q=max(0,ceil((c-q)/H)).

Only finitely many q≥0 have N_q>0 and m_q≥1.

Pinned input [exact shifted graded S-resolution and weighted Hilbert series](https://github.com/awdawmip/enterprise-math/blob/53f2970a830167d5d1bfd89419f7edda23c388a4/research_notes/driver/2026-11-17_prefix808_weighted_hilbert_resolution_source_degree_audit.md). Its load-bearing normal-form hypothesis is pinned at [exact S-module filtration](https://github.com/awdawmip/enterprise-math/blob/92b39528063e442db55c5fd48b82b1dfe2e39105/research_notes/driver/2026-11-17_prefix808_higher_carry_exact_s_module_filtration.md).

## Theorem

For every integer m≥1 and every j≥2m, the coefficient of x^j in the ordinary-standard-graded Hilbert series of S/I^m is exactly

    H_m(j)=2m(m+1)(3j-4m+4)/3.                         (1)

Consequently, for every sufficiently large weighted degree D, the degree-D Hilbert function of E_{k,c} is **exactly**

    dim_K(E_{k,c})_D =
      Σ_{q: D≡2r_q (mod h)}
         N_q * 2m_q(m_q+1)/3 *
             [3(D-2r_q)/h - 4m_q+4],                  (2)

where the summation is over q with N_q>0, m_q≥1 and D≥2r_q+2hm_q. Thus the weighted Hilbert function is eventually a quasi-polynomial of degree at most one and period dividing h, with exact linear expressions on each occupied residue class and zero on unoccupied residue classes.

This is a *uniform theorem for all positive divisor chains* and all characteristics. It uses the compatible grading stated above, not an inferred canonical grading.

## Proof

The shifted graded resolution in the pinned input yields for each S/I^m (where deg U_i=1 for the moment)

    Hilb(S/I^m;x)=
      [1-(m+1)x^(2m)+m x^(2m+2)]/(1-x)^4.

For j≥2m, the coefficient is

    C(j+3,3) -(m+1)C(j-2m+3,3) +m C(j-2m+1,3).

The last binomial is correctly zero when its upper index equals 1 or 2, so the displayed identity applies also at j=2m and 2m+1. Expand the three cubic polynomials: the cubic and quadratic coefficients cancel and the result simplifies to 2m(m+1)(3j-4m+4)/3, proving (1).

With deg U_i=h and a normal-form generator z_0^a z_1^b of weighted degree 2r_q, the contribution at D is the coefficient of x^j where j=(D-2r_q)/h, provided that j is a nonnegative integer. The exact graded S-decomposition of the pinned theorem is a finite direct sum of such shifts with multiplicities N_q. Substitute (1) when D≥2r_q+2hm_q and sum over all admissible q. This proves (2) and its eventual periodic-linear statement. QED.

## Worked example and exact regression

For h=d=4, e=1, k=0, c=3, the only nonzero (N_q,m_q,r_q) are (1,3,0) and (3,2,4). Both reach the linear regime at D=24. Therefore for every D≥24,

    dim_K(E_{0,3})_D =
       15D-184  if D≡0 (mod 4);
       0        otherwise.

In particular degrees D=24,28,32 yield 176,236,296, agreeing with the independent weighted normal-form enumeration in the pinned antecedent.

A separate exact integer regression tested (1) for all m=1,...,12 and every j=2m,...,2m+100: **1,212 checked pairs, zero disagreements**. This verifies expansion and threshold indices; the universal statement follows from the polynomial identity above.

## Research status

This closes the local question of the eventual weighted Hilbert function of each already-defined E_{k,c}. The original TU/Reeve source model and later cyclic-cover/carry contributors remain separately credited. No new native Result, independent admission, Task completion, mother-goal closure or native-X6 transfer is asserted. The distinct N-coupled coverage and JT2 mother questions retain their actual open status.
