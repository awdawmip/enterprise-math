# Portable BRC certificate: p^15 half-point jet via H10 boundary carrier

Status: PORTABLE / STAGED ONLY / NOT SOURCE-PUBLISHED / NOT RESULT / NOT LIFT.
Scope: current Enterprise Math D24 unit-reciprocity task, target primes p ≡ 13,19 (mod 24).
This note does not alter the frozen task scope or theorem status.

## 1. Carrier and provenance

For an odd target prime p, define

U_p = C(2p-1,p-1)^2 C(3p-1,p-1)
    = Π_{k=1}^{p-1} (1+p/k)^2 (1+2p/k),

and harmonic carriers

H_r = Σ_{k=1}^{p-1} k^{-r} ∈ Z_p.

The two copies of the n=2 port and the single n=3 port are retained until the logarithmic observer is applied. No positive-mass quotient is used.

Let

F_p(λ)=Σ_{k=0}^{p-1} ((1/2)_k(1/3)_k(2/3)_k/(k!)^3) λ^k

and

J_p = 9F_p'''(1/2)+27F_p''(1/2)-44F_p'(1/2)-8F_p(1/2).

The previously established exact top-boundary identity is consumed as input:

J_p = -8 p^3 U_p (1+p q_p(6))^{-3},

where q_p(6)=(6^{p-1}-1)/p.

## 2. p-adic logarithm through degree 11

Because k is a p-adic unit and p/k ∈ p Z_p,

log U_p
 = Σ_{r≥1} (-1)^{r+1}(2+2^r)/r · p^r H_r.

For every r≥1, reflection k↦p-k gives the exact p-adic identity

H_r = (-1)^r Σ_{j≥0} binom(r+j-1,j) p^j H_{r+j}.

Hence for odd r,

2H_r = - Σ_{j≥1} binom(r+j-1,j) p^j H_{r+j}.

Starting with r=1,3,5,7,9,11 and recursively substituting this identity, while discarding only terms already carrying p^12, eliminates all odd harmonic carriers below degree 12. The remaining coefficients are exact:

log U_p ≡
 -5 p^2 H_2
 -(17/2) p^4 H_4
 -(65/3) p^6 H_6
 -(257/4) p^8 H_8
 -205 p^10 H_10
 (mod p^12).

This step needs no numerical fit and no Bernoulli compression. The new independent carrier at this precision is H_10.

## 3. Exponentiation without information loss

Each even H_{2m} is p-integral; for the target primes p≥13 the displayed rational denominators are p-adic units. Since the logarithm begins at p^2 H_2, keeping all products that can survive modulo p^12 yields

U_p ≡ 1
 -5 p^2 H_2
 -(17/2) p^4 H_4
 -(65/3) p^6 H_6
 -(257/4) p^8 H_8
 -205 p^10 H_10
 +(25/2) p^4 H_2^2
 +(85/2) p^6 H_2 H_4
 +(325/3) p^8 H_2 H_6
 +(289/8) p^8 H_4^2
 -(125/6) p^6 H_2^3
 -(425/4) p^8 H_2^2 H_4
 (mod p^12).

Terms such as p^10 H_2 H_8 and p^10 H_4 H_6 have p-adic valuation at least 12 for the target range and therefore do not survive this observer. The formula preserves the first H_10 boundary port and the new mixed interactions H_2H_6, H_4^2, H_2^2H_4.

## 4. p^15 half-point jet certificate

Combining the preceding congruence with the exact top-boundary identity gives the compact BRC-preserving certificate

J_p ≡ -8 p^3 (1+p q_p(6))^{-3} · U_p^(12)  (mod p^15),

where U_p^(12) is exactly the displayed polynomial representative modulo p^12.

Equivalently, no expansion of the Fermat-quotient normalization is required: the normalization remains a separate observer factor, while the harmonic boundary carriers retain their provenance.

This strictly strengthens the earlier p^13/H8 certificate. It is portable evidence only; it does not establish LIFT/JT2 and does not change the accepted-parent or UR/JT0 formal status.

## 5. Independent finite falsification

The companion checker independently computes:

1. U_p directly from the three original multiplicative ports modulo p^12;
2. U_p^(12) from H_2,H_4,H_6,H_8,H_10;
3. F_p,F_p',F_p'',F_p''' directly from the finite hypergeometric recurrence modulo p^15;
4. the factored p^15 jet certificate.

For all 166 primes p<5000 with p≡13 or 19 (mod 24), both U12 and J15 have zero failures. This finite regression is not used as the proof.

## 6. BRC resolution

BRC resolution: COMPOSE_APPLIED.
Carrier: labeled n=2,n=2,n=3 multiplicative ports -> p-adic logarithmic harmonic carrier.
Observer horizon: modulo p^12 for U_p and modulo p^15 for J_p.
Information retained: port multiplicity, harmonic order, p-power valuation, normalization factor, mixed interactions.
Information intentionally not compressed: H_10 into Bernoulli scalars; normalization into the boundary carrier.
Smallest next portable unit if formal UR execution remains blocked: extend the reflection/log calculation two further p-powers and determine the first H_12 / quartic-interaction terms required for U_p mod p^14.
