# D25 integer-shadow Lucas digit-factorization and all-n congruence families

Date: 2026-11-05. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science input `c47e13e4aba0e006366f989d6334d443f6333ae3`.

Status: **AUTHOR-PROVED GENERAL LUCAS FACTORIZATION / EXACT FINITE BASE-PRIME CERTIFICATES / UNREVIEWED / NOT_ADMITTED**. Separate portable subproblem of the existing integer-shadow approach; no native CM/H0/B0 experiment.

## Theorem: the entire n-dependence factors off the weighted lowest base-q digit

For n>=1 define the integer
`C_n=sum_{k=0}^{2n}(6k+1)(-1)^k 2^(2n-k) binom(2n,k)binom(3n,k)binom(4n,k)`.
Let q>=5 be prime with q | (6n+1), set z=-2^(-1) in F_q, and write base-q digits of 2n,3n,4n as a_i,b_i,c_i. Since gcd(6,q)=1, the lowest digit of n is n0=-6^(-1) mod q. Thus (a0,b0,c0)=(2n0,3n0,4n0) reduced to [0,q-1], independent of the other digits of n.

Define `D_q(a,b,c)=sum_{j=0}^{min(a,b,c)} z^j binom(a,j)binom(b,j)binom(c,j)`,
and `L_q(a,b,c)=sum_{j=0}^{min(a,b,c)} (6j+1) z^j binom(a,j)binom(b,j)binom(c,j)`.
Then the **exact congruence for every n** is

`C_n == 2^(2n) L_q(a0,b0,c0) prod_{i>=1} D_q(a_i,b_i,c_i) (mod q)`. (LUCAS-SHADOW)

Proof: Lucas's theorem factorizes each of the three integer binomial coefficients digitwise. Since z^q=z in F_q, z^k=prod_i z^(k_i). The weight satisfies (6k+1)=(6k0+1) mod q. Summing independently over all digit combinations proves the factorization; out-of-range binomial digits give zero. There is no assumption that n or 6n+1 is prime.

Consequently, for any fixed q satisfying `L_q(a0,b0,c0)=0 mod q`, **every integer n with q|(6n+1)** satisfies `q|C_n`.

## Two unconditional infinite families

For q=5, n0=4 and (a0,b0,c0)=(3,2,1). Therefore
`L_5(3,2,1)=1+7(-1/2)(3)(2)(1)=-20==0 mod5`.
It follows that **for every n>=1 with n==4 (mod5), 5|C_n**.

For q=7, n0=1 and (a0,b0,c0)=(2,3,4). Here
`L_7(2,3,4)=1-84+117/2=-49/2==0 mod7`.
Thus **for every n>=1 with n==1 (mod7), 7|C_n**.

These are exact infinite arithmetic-progression results. They extend the prior n<=500 experimental conjecture beyond a finite window, but do not yet resolve divisibility by the full integer 6n+1 or its prime powers.

## Reusable finite-source certificate

Independent exact integer-binomial arithmetic gives `L_q(a0,b0,c0)=0 mod q` for **all 237 primes 5<=q<=1500**, comprising both residue classes q=1 and 5 mod6. Combining each of these finite q certificates with (LUCAS-SHADOW) yields: for *any* n>=1 and any prime q in this finite set dividing 6n+1, q divides C_n. A second check directly computes C_n and the digit product for 179 (n,q) incidence pairs, 1<=n<125, and confirms equality.

Example lowest-digit certificate records: q=5: (n0,a0,b0,c0,L)=(4,3,2,1,0); q=7: (1,2,3,4,0); q=11: (9,7,5,3,0); q=373: (62,124,186,248,0).

The **remaining question** in the full conjecture `(6n+1)|C_n` is the prime-power valuation q^e (and a general proof of L_q vanishing across all primes q). Lucas's theorem alone is a mod-q factorization; resolving q^e requires an additional carry/refinement operator. Do not replace it by finite scans of n.

## BRC observer and mother task

The digit vector `(a_i,b_i,c_i)` is an exact input representation; `L_q` keeps the weighted lowest-digit readout, while `D_q` retains the higher-digit multiplicative factors. This factorization is a faithful calculation of C_n modq and does not assert native X6/slice transfer. The D25 scalar target remains `Delta_p-R_p=0 mod p` at p=13,19 mod24; the integer shadow is connected to the signed-216 p-adic two-jet reconstruction in sibling note `20261105_hourly20_d25_integer_shadow_two_jet_bridge.md`. Next: derive the q-adic carry correction for q^2|6n+1, or a closed proof of the universal lowest-digit identity, and feed the surviving exact lemma back to the LIFT two-jet certificate.
