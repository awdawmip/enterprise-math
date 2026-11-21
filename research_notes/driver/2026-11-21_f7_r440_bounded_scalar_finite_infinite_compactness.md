# CBRC F7 Driver r440 — bounded-scalar finite-to-infinite minimax compactness

Date: 2026-11-21 (+08:00). New mathematical reduction by existing Driver EM-DVR-DEBB5E; retain original F7 author EM-CBRCF7-83A1D4 and frozen RR-AA38973D56330E59D315 without changing the original no-go scope.

## Statement

Keep the original F7 matrix A, J parity, q(0,0)=0, q(t,0)=1 for nonzero integer t, q(2,1)=q(-1,-1)=1/2, nonzero positivity q>=1/2 and defect D_q defined in r436/r438.

Let Q_1 be the **uniformly bounded subclass** of all such q for which q(x,y)<=1 at every integer pair (including the already fixed old axis). Define

    E_B^{<=1}=min_{q in Q_1} max_{z in [-B,B]^4 intersect Z^4}|D_q(z)|
    E_infty^{<=1}=inf_{q in Q_1} sup_{z in Z^4}|D_q(z)|.

**Theorem (finite constraints determine the infinite bounded-class optimum):**

    E_infty^{<=1} = sup_{B>=1} E_B^{<=1} = lim_{B -> infinity} E_B^{<=1}.

Moreover the infinite-domain infimum is **attained** by some q in Q_1. Each finite E_B^{<=1} is attained by a rational-valued assignment on the finitely many coordinates sampled by that cube.

**Exact feasibility equivalence:** for every epsilon>=0, there exists q in Q_1 satisfying |D_q(z)|<=epsilon for every z in Z^4 **if and only if** every finite cube [-B,B]^4 admits some (potentially different) q_B in Q_1 with |D_{q_B}(z)|<=epsilon on that cube. No compatibility hypothesis on the chosen q_B tables is required: the compactness argument supplies a compatible limiting q.

## Proof

Remove the fixed origin/axis/marked coordinates. The remaining independent J-even scalar values form a countable coordinate set I. Their admissible values each lie in the compact interval [1/2,1], so Q_1 is a nonempty closed subspace of the countable product [1/2,1]^I, which is compact (equivalently sequentially compact by diagonal extraction). Nonemptiness follows from the r435 globally defined J-even marked scalar with range [1/2,1] off the origin.

For fixed z, D_q(z) depends on at most four scalar coordinates, so it is continuous on Q_1. Consequently M_B(q)=max_{|z|_infty<=B}|D_q(z)| is continuous, and reaches its minimum E_B^{<=1}. These minima are nondecreasing in B, and uniformly <=4/7 by r435. Put L=sup_B E_B^{<=1}. The sets C_B={q in Q_1: M_B(q)<=L} are closed, nonempty, nested and contained in compact Q_1. Their intersection contains q_infty, and this one q_infty has sup_{z in Z^4}|D_{q_infty}(z)|<=L. Conversely every q has sup_z|D_q(z)|>=M_B(q)>=E_B^{<=1} for every B. Thus E_infty^{<=1}=L and q_infty attains the infimum. Replacing L by a specified epsilon proves the feasibility equivalence.

For fixed B, only finitely many scalar coordinates are used; the scalar variables range over a rational box, and the epigraph formulation of the finite absolute-defect objective is a rational polyhedron with an attained finite minimum. Hence rational optimal finite tables exist. This fact does **not** require a uniform denominator across B.

## Consequences and evidence status

1. Exact finite certificates/dual obstructions at growing B compute a monotone sequence converging to **the bounded-class global optimum**. An obstruction E_B^{<=1}>1/2 at one finite B proves the bounded global optimum >1/2. An exact feasible certificate at every B for epsilon=1/2 proves existence of a globally half-defect bounded scalar, even without a constructive formula for it.
2. r439's checked B10 candidate has range [1/2,1], so E_10^{<=1}<=50000001/100000000. Together with the fixed marked witness, 1/2<=E_10^{<=1}<=0.50000001. The same holds for B<=10; r436 established E_B=1/2 for B<=8 in the unrestricted class, using an also bounded table.
3. For the unrestricted original class Q (only a positive lower bound and **no fixed upper cap**), this compactness proof is not automatically applicable: the product of unbounded coordinate ranges is not compact. The issue is whether an optimum-preserving uniform cap or another compactness mechanism is available. Its general global bounds remain 1/2<=E_infty<=4/7.

This theorem is a new self-contained mathematical reduction and a certificate interpretation, not a Native Review, native Result admission, new official Task or objective closure. Formal first Review still faces the original #2874 global-audit-budget failure and the separate frozen manifest SHA256 discrepancy. The scientific frontier is to certify larger B exactly, search a bounded finite dual obstruction, or construct a global scalar.

