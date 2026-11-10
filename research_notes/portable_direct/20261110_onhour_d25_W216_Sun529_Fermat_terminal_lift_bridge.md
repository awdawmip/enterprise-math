# D25/W216 — Fermat-quotient terminal jet and signed Sun-5.29 bridge

Date: 2026-11-10 Asia/Hong_Kong. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923. **AUTHOR_SIDE / EXACT ALGEBRAIC PROOF / REPRODUCIBLE FINITE REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.

## External source: old conjecture, not a theorem

Zhi-Hong Sun, *Supercongruences involving Apéry-like numbers and binomial coefficients*, AIMS Mathematics 7(2) (2022), 2729–2781, published 2021-11-18; DOI 10.3934/math.2022153, page 2758, Conjectures 5.28–5.29. Official PDF https://www.aimspress.com/aimspress-data/math/2022/2/PDF/math-07-02-153.pdf . Conjecture 5.29 proposes for inert p≡13,19 (mod24), where (p/3)=+1, the exact original-coefficient relation F2 = 13 F1/2 − 5p/2 (mod p²). Here this is a **named defect** only, never a proved input. The companion Conjecture 5.28 on F0/p² is not assumed.

## Definitions and integrality

For any prime p>3, work in p-local rationals. Let

~~~text
A_k = binom(2k,k)^2 * binom(3k,k) / 216^k,
W_p = sum(k=0..p-1) (6k+1) A_k,
F_r = sum(k=0..p-1) A_k / (k+1)^r,  r=0,1,2,
E_p = F_2 - (13/2)*F_1 + (5/2)*p,
q_p(216) = (216^(p-1)-1)/p mod p.
~~~

The term k=p-1 is **retained**. Its A_(p-1) has exact p-adic valuation 3, compensating inverse moments with p and p² denominators; all displayed F_r are p-integral. Signed 6k+1 weight and original coefficient identity are preserved.

## Theorem A: all-prime terminal first jet

For **every prime p>3**,

~~~text
A_(p-1)/p³ ≡ −1 + p (q_p(216)−13/2)   (mod p²).       (A)
~~~

**Proof.** Exact integer-factorial reblocking yields the following rational identity (each product factor has p-unit denominator):

~~~text
A_(p-1)/p³ = 2/[(p−1)²(p−2) 216^(p−1)]
           · PROD(i=1..p−2)(1+p/i)
           · PROD(i=1..p−1)(1+p/i)
           · PROD(i=1..p−3)(1+2p/i).                (A1)
~~~

H_(p−1)=0 mod p by pairing inverses in the finite field; hence H_(p−2)=1, H_(p−3)=3/2 mod p. The product therefore is 1+4p (mod p²). The front rational factor 2/[(p−1)²(p−2)] is −1−5p/2 (mod p²); the factor 216^(−(p−1)) is 1−p q_p(216) (mod p²). Their product is precisely −1+p(q_p(216)−13/2), proving (A), including valuation 3. No prior conjecture, CM or Frobenius identification enters this proof. □

## Theorem B: all-prime original signed p³ bridge

For **every prime p>3**,

~~~text
W_p−p ≡ −2 F0 − (2/3) E_p + (2/3)p² q_p(216)  (mod p³).  (B)
~~~

**Proof.** Consume the previously source-published exact rational inverse-moment telescope, for n≥1:

~~~text
W_n = SUM(k=0..n−2) d_k A_k + (7−6n)A_(n−1),
d_k = −(k−1)(6k+5)/[3(k+1)²]
    = −2 + 13/[3(k+1)] − 2/[3(k+1)²].
~~~

Restoring the exceptional k=p−1 term in all three F_r gives the **exact rational equality**

~~~text
W_p = −2F0+(13/3)F1−(2/3)F2+B_p,
B_p = [9−6p−13/(3p)+2/(3p²)] A_(p−1).              (B1)
~~~

Insert (A) into B_p: its signed terminal carry is

~~~text
B_p ≡ −2p/3+(2/3)p² q_p(216)                 (mod p³). (B2)
~~~

By definition, (13/3)F1−(2/3)F2=−(2/3)E_p+(5/3)p. Subtract p from (B1) and use (B2). This proves (B) unconditionally for all p>3. □

## LIFT consequence in the exact inert target classes

Suppose p≡13,19 (mod24) and the separately sourced first-digit and F0-divisibility inputs hold:

~~~text
(H) W_p ≡ p (mod p²),  F0 ≡ 0 (mod p²).
~~~

Equation (B) then **proves** E_p≡0 (mod p²), which is the inert target-class clause of Sun's Conjecture 5.29 *conditional on H*. Define α_p=F0/p², ε_p=E_p/p² and λ_p=(W_p−p)/p² in F_p. The theorem gives

~~~text
λ_p = −2α_p − (2/3)ε_p + (2/3)q_p(216) (mod p),      (C)
λ_p=0  iff  ε_p = q_p(216)−3α_p (mod p).             (D)
~~~

The target exact source relation Δ_p−R_p = λ_p (mod p) transfers the observer only with its original G_p,h, signed cutoff and provenance preserved. Equation (D) identifies a **new testable third-digit condition** between a published inverse-moment conjecture and the frozen LIFT question. It does not prove the universal vanishing of λ_p and does not turn Sun's conjecture into an assumed theorem. Previously author-proved finite Clausen/CM double root yields F0=0 (mod p), *not automatically* modulo p²; H remains an explicitly typed hypothesis. This precise distinction is retained.

## Actually executed checks and BRC observer audit

Companion original-coefficient script d25_w216_sun529_fermat_terminal_bridge_20261110.py uses the standard library's exact integers, modular inverses and rational Fraction. Author execution verified:

- 12 exact rational all-n identities, n=1,…,12;
- unconditional (B) at ten non-target primes 5,7,11,17,23,29,31,41,47,53;
- all 13 target primes 13,19,37,43,61,67,109,139,157,163,181,229,373 for (A),(B),(C),(D) as finite observations, plus independent three-product endpoint reconstruction (A1).

Selected p-adic data, entries mod p:

| p / p mod24 | α=F0/p² | ε=E/p² | q_p(216) | λ=(W−p)/p² | q−3α |
|---|---:|---:|---:|---:|---:|
| 13 / 13 | 11 | 0 | 7 | 0 | 0 |
| 19 / 19 | 8 | 1 | 6 | 0 | 1 |
| 37 / 13 | 34 | 29 | 20 | 0 | 29 |
| 43 / 19 | 24 | 9 | 38 | 0 | 9 |
| 373 / 13 | 71 | 183 | 23 | 0 | 183 |

Theorem proofs are symbolic, finite data is regression only. BRC COMPOSE_APPLIED: retain original k-labels and signed weights, p-valuations, exceptional end index and Fermat quotient; projection to moments is justified by exact telescope for THIS observer, not for native crystalline H0/B0.

## Durable continuation, source status, next action

Parent target: all p≡13,19 (mod24) Δ_p−R_p=0 (mod p), or original-class counterexample/strict equivalent certificate, still OPEN. Do not repeat frozen D24 UR, accepted predecessor proof, Source native checkpoints, previously source-published p-block transfer, three-band q2, cubic Newton p5 counterexamples and original rational inverse-moment identity. This unit adds exact universal terminal first jet (A), unconditional B and conditional refined conjectural link D.

Next mathematical action: construct a direct finite hypergeometric/Clausen/WZ proof or exact same-object falsification of ε_p = q_p(216)−3α_p, preserving the k=p−1 denominators and both prime classes. Independently establish or falsify uniform F0≡0 (mod p²) from frozen original CM input without equating scalar surrogate with native Frobenius. Keep native Issue #1559 as actual support path (OPEN, PENDING_OWNER). Original fixed H0/B0 p373 [X]U mod139129, rank, Frobenius semilinear direction/η, signed odd κ, Δ−R and independent replica remain NOT_RUN. Previous genuine own Researcher session MCP-5378d3819d8947bda9049c9428493e2d was registered, but recovery_status this run returned SESSION_CAPABILITY_REQUIRED; no authenticated own winning CLAIM/open run or native Source checkpoint. No Maintenance lane identity or schedule changes.

**AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED** until actual independent scientific review and native Source authorization.
