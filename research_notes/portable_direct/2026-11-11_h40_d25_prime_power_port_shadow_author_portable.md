# D25/LIFT — exact prime-power Lucas shadow of both Clausen ports

**Date:** 2026-11-11. **Role/provenance:** H40 author portable mathematics; no native Source Task CLAIM, checkpoint, Result, or independent review. **Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; original frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. Extends the independently published Lucas/Euler mod-q port transfer at d7fda5c785e8e0ef6a9218c41cef39e56f0863f1.

## Universal theorem (exact in F_q, not modulo q^r)

Fix any prime q>=5 and integer r>=1. Define N=q^r and epsilon_r=0 if N=1 mod 6, epsilon_r=1 if N=5 mod 6, m_r=(N-1-4epsilon_r)/6. Set

    F_{u,v}(X)=sum_{0<=k<=min(u,v)} binom(u,k)*binom(v,k)*X^k
    A_r=F_{m_r,2m_r+epsilon_r}(1/2),
    B_r=(1-6epsilon_r)*A_r+6*F'_{m_r,2m_r+epsilon_r}(1/2).

The denominators are q-adic units. Write (A_1,B_1) for the same pair at r=1. Define

    c_q(r) = 1,                                  if q=1 mod 6,
    c_q(r) = 2^{-((q+1)/2)*floor(r/2)} in F_q,    if q=5 mod 6.

Then for all q,r, as an identity of **two labeled ports** in F_q^2,

    (A_r,B_r) = c_q(r)*A_1^(r-1)*(A_1,B_1).       (1)

For r=1 take A_1^0=1, even when A_1=0.

## Proof

Lucas binomial digit factorization gives F_{m_r,2m_r+epsilon_r}(X) = F_{a_r,b_r}(X) F_{M,R}(X^q) in F_q[X], where (a_r,b_r) are the least q-adic digits and (M,R) the remaining higher digits. Differentiating kills the derivative of the second factor in F_q[X]. At X=1/2 its Frobenius value equals F_{M,R}(1/2).

If q=6t+1, epsilon_r=0 for every r, and m_r=t*(1+q+...+q^(r-1)), so (a_r,b_r)=(t,2t), (M,R)=(m_{r-1},2m_{r-1}). Thus A_r=A_1*A_{r-1} and B_r=B_1*A_{r-1} in F_q, giving (1) by induction.

If q=6t+5, epsilon_r is 1 for r odd and 0 for r even. Put a=t,b=2t+1,d=q-1-a-b=(q+1)/2. Direct digit subtraction shows that (a_r,b_r)=(a,b) for odd r and (q-1-a,q-1-b) for even r, with (M,R)=(m_{r-1},2m_{r-1}+epsilon_{r-1}). Use the exact complementary-polynomial identity

    F_{q-1-a,q-1-b}(X) = (1-X)^d F_{a,b}(X) mod q.

Its derivative at X=1/2 gives the corresponding labeled weighted B-port: the lower digit pair is (A_1,B_1) for odd r and 2^(-d)*(A_1,B_1) for even r. In fact 1-6epsilon_r-12d = 1-6epsilon_1 modulo q in the even case. Hence A_r=s_r*A_1*A_{r-1}, B_r=s_r*B_1*A_{r-1} with s_r=2^(-d) on even r and 1 on odd r. Iterating multiplies exactly floor(r/2) complementary factors and proves (1).

## Information preserved and consequences

If A_1=0 mod q, both higher ports A_r,B_r are 0 mod q for every r>=2. If B_1=0 and A_1 is nonzero, B_r=0 and A_r is nonzero mod q for all r>=1. Thus the high-digit multiplier A_1^(r-1) is a necessary residual coordinate for distinguishing a unique base zero from a simultaneous mod-q collapse. This is a BRC labeled-port observer composition with explicit complement scalar; it does not identify the higher q-adic valuations.

For fixed q and known base pair, computing (1) requires O(log r) field multiplications via modular exponentiation; constructing/printing the exact input N=q^r costs Theta(r log q) input/output bits. The full mod-q^r pair is not computed by (1).

## Exact certificate and next operation

An independent raw-binomial calculation checks all primes 5<=q<=997 and exponents r>=1 for which m_r<=600: 188 exact pair comparisons; 22 cases with r>=2; 9 cases with r>=2 and A_1=0, where both higher ports vanish. No discrepancies. Examples:
(q,r,N,base pair,high pair) =
(5,5,3125,(1,0),(4,0));
(7,4,2401,(2,0),(2,0));
(11,3,1331,(8,0),(8,0));
(13,3,2197,(0,6),(0,0));
(17,2,289,(0,1),(0,0));
(29,2,841,(25,0),(21,0)).
The separate standalone program d25_prime_power_port_shadow_verify_20261111.py reproduces the finite check. This certificate is auxiliary and author-checked; mathematical universality comes from the above digit induction.

Next: derive a **mod-q^2 correction** of the two-port Lucas/Euler transition carrying q-adic digit/carry information, and compare q=13,N=169 split valuations with q=7 prime-power examples. The mother D25/LIFT Task requires the *original-class* H0/B0, semilinear Frobenius eta and Delta_p-R_p; preserve prior native Source units and UR V2 provenance.