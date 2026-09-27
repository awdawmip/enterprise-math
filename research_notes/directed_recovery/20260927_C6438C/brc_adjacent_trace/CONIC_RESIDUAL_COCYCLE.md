# The adjacent-trace conic defect has an exact transport law

Status: PURE_SYMBOLIC_RESIDUAL_LAW / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.

This note studies nonzero defects rather than treating them as noise or deleting the state. It extends the HBW adjacent-trace coordinate interface algebraically. It is not a physical residual attribution or an extra experiment.

Over any commutative ring, fix k and put

    F(v,w)=v^2-kvw+w^2+k^2-4,
    D0(v,w)=(v^2-2,vw-k),
    D1(v,w)=(vw-k,w^2-2).

The exact identities are

    F(D0(v,w)) = v^2 F(v,w),
    F(D1(v,w)) = w^2 F(v,w).

To check the first, expand its left side and group the result as

    v^4 + v^2*w^2 - k*v^3*w + (k^2-4)*v^2.

It is exactly v^2 F. Interchanging v,w and reversing the output coordinates proves the second because F is symmetric. These are integer polynomial identities, so no division, floating precision, hidden factor or curve-membership assumption enters the proof.

For any declared bit word, let s_j be the selected pre-update coordinate v_j for bit zero and w_j for bit one. Then

    F_t = F_0 * J_t^2,  J_t=product_(j<t) s_j.

The product is chronological provenance of the selected coordinates, not the count or total mass of alternative histories. A one-register J update would require one extra actual multiplication per bit and its own source/receipt. That register is not implemented or charged in the presently prepared trace program.

## What the defect means, and what it cannot certify

The valid marked HBW trace orbit starts at (2,k), so F_0=0 and the law proves exact conic preservation. For an off-conic candidate it states how the defect changes; a nonzero defect is retained with a deterministic law, not automatically labeled a physical effect or discarded.

Over Z/NZ, a later zero defect does not prove that every earlier state lay on the conic. A selected nonunit s can annihilate information through its square. If s is a unit, F_after=0 implies F_before=0. If gcd(s,N) is proper, the same failed-invertibility branch gives a factor with an actual gcd/division certificate. If s is zero modulo N, the gcd saturates and gives no proper factor. For example D0(0,w)=(-2,-k) is on the conic for every w; membership of that output says nothing about the erased input w. This is a symbolic family, not a run with a chosen modulus.

If F_0 is a certified unit, then gcd(N,F_t)=gcd(N,J_t^2). A stored J would retain the unsquared accumulated critical divisor, but it is a history-product observer, not automatically the primitive return divisor of the terminal point. Repeated hits can increase its prime valuations and different components can cause saturation. It would require a separate first-hit or product-descent contract. No free factorization or complexity advantage follows from this observation.

## Native geometric distinction

The formal Jacobian matrices of the two bit maps are

    dD0 = [[2v,0],[w,v]],  det(dD0)=2v^2,
    dD1 = [[w,v],[0,2w]],  det(dD1)=2w^2.

Thus the defect multiplier is also the Jacobian determinant divided by the known scalar 2 when 2 is a unit. The maps have genuine singular branches. They must not be described as the same integer-unimodular HBW arrow M. M advances a fixed orbit index n to n+1; the bit maps compile a changing exponent prefix to 2n or 2n+1. Both are exact on the declared trace carrier but they are different operation languages.

This supplies a concrete residual law and an observer boundary for the proposed native program. It neither replaces full operation provenance with a conic membership check nor attributes an arithmetic/source failure to nature. The current program relies on proved recurrences and actual typed arithmetic; adding a runtime defect observer would need a separately declared bill and experiment.

Dependency: ADJACENT_TRACE_HBW_GEOMETRY.md, SHA-256 3b8083eb0ecddc1c12406cd64113ce3e2bb88ee676a0e7b8fd3f7c6289511e14. No frozen source or existing review is modified.

Global-Knowledge-Sync: main@8c23cca / GLOBAL_KNOWLEDGE_V1
