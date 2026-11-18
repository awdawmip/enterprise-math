# EC49AV — exact deterministic-purchase optimum and sparse optimal-policy reduction

Date: 2026-10-30. Status: AUTHOR_ANALYTIC_PROOF / EXACT_BIGINT_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Frozen model

The exact positive auxiliary 18+18-leaf probability BRC observer of EC49AU, at information parameter η=11/30, action costs (1,1,2,2,0), first-stage expected cost C1=43/48, sensor expected cost C2=13/16, and k=177/172. There are hidden w=0,1,2, action c=A0,A1,B0,B1,STOP, observed u=0,1, and purchased sensor outcome z∈{0,1,2}. The conditional sensor purchase coin depends only on (c,u), not hidden w. For x[w,c]=Pr(c|w), t(w,u)=1/2+(2u−1)(1−w)η, define q_z(c,u)=x[z,c]t(z,u)/3 and T(c,u)=Σ_z q_z. Optimally accepted purchased observations have positive score Δ_z=(43q_z−16T)/172; an unpurchased fiber has no positive score because the P/Q marginal distributions there agree and k>1. Thus H(x,p)=Σ_{c<4,u} p(c,u) Σ_z[Δ_z(c,u)]_+.

## Theorem A: complete deterministic-purchase optimum

For EVERY real first-stage behavioral allocation x satisfying the row simplices, C1=43/48 and exact C2=13/16, and EVERY deterministic observation-only purchase rule p(c,u)∈{0,1}, allowing optimal observation-only acceptance,

**H(x,p) ≤ 14401/123840.**

Equality is achieved by the already published lawful witness W: rows indexed w=0,1,2 are (0,3/16,1/4,0,9/16), (1,0,0,0,0), (0,1,0,0,0), with purchase on all six nonempty paid (c,u) fibers and optimal acceptance. Hence the deterministic-purchase optimum is EXACTLY 14401/123840.

**Proof and finite exact certificate.** Fix one of 2^8 binary purchase masks. For this mask, the first-stage feasible polytope is the intersection of x≥0 with three row-sum equations, the exact action-cost equation Σ a_c x=43/16, and the exact purchase-mass equation Σ p(c,u)t(w,u)x[w,c]/3=13/16. The objective H is a nonnegative weighted sum of positive parts of affine functions of x, so it is convex. A continuous convex function on this compact polytope has a maximizer at an extreme point. The zero mask is infeasible; for each of the other 255 masks the five equality rows have rank five, certified by the existence of a nonsingular five-column basis. Every extreme point has at most five positive coordinates and is represented by one of the C(15,5)=3003 bases.

At η=11/30, t(w,u) is exactly one of {4,15,26}/30; multiplying the purchase row by 90 makes every coefficient an integer. With the first four rows integral and last row scaled, the RHS multiplied by 16 is exactly (16,16,16,43,1170). For each five-support basis S, Cramer's formula gives x_j=det(M_j)/(16 det(M)), all exactly rational. The verifier computes determinants using integer four-by-four cofactors (permutation signs), then tests sign feasibility and scores each feasible basis with gcd-normalized BigInt fractions. No floating-point feasibility screen or numerical tolerance enters the certificate.

The executed 2026-10-30 verifier exhausts 255 purchase masks ×3003 support sets: 445440 nonsingular matrices, 6240 feasible bases, 852 distinct rational first-stage points, and 32 maximizing basic mask/support pairs. Its maximum equals 14401/123840 exactly. An independently implemented Python Fraction calculation on the same defining equations reproduced the same nonsingular count, feasible count and exact maximum. These are author-side exact computational checks; formal checker translation and independent review remain subsequent tasks.

## Theorem B: joint sparse-policy existence for unrestricted purchases

For any η with nonnegative valid t(w,u), finite first- and second-stage costs, and the same finite auxiliary causal model, there exists a global maximizer (x,p) in which (i) at most FIVE of the fifteen x[w,c] entries are positive, and (ii) among the eight observable purchase probabilities p(c,u), at most ONE with positive T(c,u) lies strictly between 0 and 1.

**Proof.** The feasible set in x,p is compact and H continuous. Start at a global maximizer (x*,p*). Fix p*: the purchase-cost constraint is linear in x, and H(x,p*) is convex in x. Replace x* by a maximizing extreme point of the resulting x-polytope; the latter has three row equations, one action-cost equation and one purchase equation, so any vertex has at most five positive entries. Fix that x: optimizing p is a linear program in a box with one equality ΣpT=C2. It has an optimal vertex with at most one strictly fractional coordinate among fibers of T>0; zero-mass coordinates may be set to 0. Replacing p preserves optimality and the sparse x. The replacement uses no hidden-history conditioning or shared random seed.

Together, Theorems A and B reduce any possible strict improvement beyond W at η=11/30 to a policy whose purchase probabilities have EXACTLY ONE fractional positive-mass observable fiber and whose first-stage allocation has at most five positive coordinates. Previous EC49AU certificates further exclude the 168 vertices of the first-stage paid-mass cut polytope as a better witness; no claim about nonvertex allocations follows from that predecessor alone.

## Verification and boundaries

Reproduce with `node VERIFY_EC49AV.js > EC49AV_REPORT.json` (Node.js BigInt, no dependencies); the committed JSON comes from executing the same function in an ECMAScript BigInt runtime. Check the integer Cramer derivation and code, not an external CAS assumption. No formal completeness or independent Driver verdict has been issued. This result addresses the auxiliary strictly positive probability observer only, not signed/phase BRC, native X6, the three-dimensional native slice, or heartbeat update fidelity. P000 and ACTIVE worldview are unchanged.

## Next EC49AW

Use Theorem B to enumerate the eight possible unique fractional purchase fibers, the remaining seven binary purchase bits, and five-support first-stage families. On each support, eliminate x by the five linear constraints and study the resulting exact piecewise rational objective in the one fractional purchase parameter; test endpoints, score-sign transitions, purchasing feasibility and stationary roots with exact isolating intervals. Either exhibit a lawful rational strictly improving witness or derive a global all-real no-improvement certificate. A scalar-price-only certificate cannot close this gap (EC49AU).
