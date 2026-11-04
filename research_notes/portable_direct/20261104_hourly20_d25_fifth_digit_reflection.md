# D25: original 216–2304 fifth-digit reflected-pair correction

2026-11-04; `TASK_RESEARCH author-side / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical research lane `chatgpt-research-hourly-enterprise-math-20260923`; maintenance lane `chatgpt-hourly-enterprise-math-20260921` remains separate. Reuses the independent onhour lane's fourth-digit reflection at `4aeb30aee8603b611e7834a65cfec82c5931dfbc`; the new theorem gives its first p-adic correction.

## Exact theorem for every prime p >= 5

In Z_(p), retain the **original** rational coefficients

[
a_n=rac{(2n)!(3n)!}{(n!)^5 216^n},qquad
b_n=rac{(4n)!}{(n!)^4 2304^n}.
]

Let m_a=floor((p-1)/3), m_b=floor((p-1)/4), and q_p(c)=(c^{p-1}-1)/p mod p. Define the finite-field harmonic corrections

[
S_a(k)=sum_{j=1}^{k-1}left(-rac3j+rac2{2j+1}+rac3{3j+1}+rac3{3j+2}ight),
]
[
S_b(k)=sum_{j=1}^{k-1}left(-rac3j+rac4{4j+1}+rac4{4j+2}+rac4{4j+3}ight).
]

All denominators are p-units for the ranges below; S_a(1)=S_b(1)=0. The **original** reflected pairs satisfy

[
oxed{k^3 a_krac{a_{p-k}}{p^3}equiv
-rac1{18}left[1+pleft(rac{13}2-q_p(216)+S_a(k)ight)ight]pmod{p^2}},
qquad 1le kle m_a, 	ag{A}
]

[
oxed{k^3 b_krac{b_{p-k}}{p^3}equiv
-rac1{96}left[1+pleft(rac{22}3-q_p(2304)+S_b(k)ight)ight]pmod{p^2}},
qquad 1le kle m_b. 	ag{B}
]

The exact Legendre valuations for n<p are v_p(a_n)=floor(2n/p)+floor(3n/p), v_p(b_n)=floor(4n/p). Thus low factors are p-units and high factors have valuation exactly three on the stated ranges. Equations (A),(B) strictly strengthen the prior mod-p reflection by one full p-adic digit.

### Proof

Write F=(p-1)!. Splitting the factorials into p-free blocks and using H_(p-1)=0 mod p yields, as exact p-local congruences,

[
(2p-2)!/pequiv-F^2(1+2p),quad
(3p-3)!/p^2equiv F^3(1+9p/2),quad
(4p-4)!/p^3equiv-F^4(1+22p/3)pmod{p^2}.
]

For the first truncated p-free block use H_(p-2)=1 mod p and 1/(p-1)=-(1+p) mod p². For the second use H_(p-3)=3/2 mod p and the last block offset 2p; the missing factors (p-1)(p-2) contribute inverse (1+3p/2)/2. For the third use H_(p-4)=11/6 mod p with offset 3p; the missing (p-1)(p-2)(p-3) contribute inverse -(1+11p/6)/6. These expansions include p=5.

With c^{-(p-1)}=1-p q_p(c) mod p², the resulting endpoint evaluations are

[
a_{p-1}/p^3equiv-[1+p(13/2-q_p(216))],qquad
b_{p-1}/p^3equiv-[1+p(22/3-q_p(2304))]pmod{p^2}.
]

Since a_1=1/18 and b_1=1/96, (A),(B) hold at k=1. The exact coefficient recurrences are

[
R_a(j)=a_{j+1}/a_j=(2j+1)(3j+1)(3j+2)/(36(j+1)^3),
quad
R_b(j)=b_{j+1}/b_j=(4j+1)(4j+2)(4j+3)/(576(j+1)^3).
]

For C_a(k)=k³a_ka_(p-k)/p³ and C_b(k)=k³b_kb_(p-k)/p³, exact substitution j=p-k-1 gives

[
rac{C_a(k+1)}{C_a(k)}=
rac{(1-p/k)^3}{(1-2p/(2k+1))(1-3p/(3k+1))(1-3p/(3k+2))},
]
[
rac{C_b(k+1)}{C_b(k)}=
rac{(1-p/k)^3}{(1-4p/(4k+1))(1-4p/(4k+2))(1-4p/(4k+3))}.
]

Modulo p² these are respectively 1+p(S_a(k+1)-S_a(k)) and 1+p(S_b(k+1)-S_b(k)). Multiplying the increments and the k=1 values proves both formulas for every stated prime and index.

## Original weighted high layers through the fifth digit

Preserve both original source identities, ordered pairs (k,p-k), valuation three, and signed weights. Define

[
A_3=sum_{k=1}^{m_a}(6(p-k)+1)a_{p-k},quad
B_3=sum_{k=1}^{m_b}(8(p-k)+1)b_{p-k}.
]

The full high-layer **mod p⁵** observation is now available entirely from low-unit coefficient data:

[
oxed{rac{A_3}{p^3}equiv-rac1{18}
sum_{k=1}^{m_a}rac{1-6k+6p}{k^3a_k}
[1+p(13/2-q_p(216)+S_a(k))]pmod{p^2}},	ag{C}
]

[
oxed{rac{B_3}{p^3}equiv-rac1{96}
sum_{k=1}^{m_b}rac{1-8k+8p}{k^3b_k}
[1+p(22/3-q_p(2304)+S_b(k))]pmod{p^2}}.	ag{D}
]

This retains the fifth-digit signed source A_3-2B_3. It is an optional mechanism discriminator for the frozen original W216-V2304 mod p³ and D24 Delta-R mod p mother problem, **not** an additional prerequisite or a claim of a general p⁵ scalar congruence.

## Executed exact checks

The companion standard-library Python checker was actually run with --limit 5000: **667 primes** (5 <= p <= 5000), **902406** individual original low/high reflected pairs, two full weighted high-tail fifth-digit ports per prime. All assertions passed. Original coefficients were independently rebuilt from integer binomial formulas at p=5,7,11,13,19,23,29,97. The full signed J=W216-2V2304+(-3/p)p was also measured mod p⁵; the 667-prime finite sample had J=0 mod p⁵ only for p=5,7, preserving already-known higher-order falsifier information.

| p | A3/p³ mod p² | B3/p³ mod p² | (A3-2B3)/p³ mod p² | J mod p⁵ |
|---:|---:|---:|---:|---:|
| 11 | 72 | 89 | 15 | 73205 |
| 13 | 70 | 162 | 84 | 257049 |
| 19 | 156 | 206 | 105 | 1824494 |
| 97 | 7901 | 9380 | 7959 | 3098524835 |
| 373 | 109567 | 26602 | 56363 | 3368096883534 |

This is an exact algebraic derivation with finite independent checks, awaiting independent mathematical review. It is **not** a native H0/B0 [X]U or Frobenius experiment.

## Current continuation boundary

Gateway 0.6.11 status read during 2026-11-04 showed UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, 5/5 active jobs; the old #6633 bridge request remains historical FAILED, with no new service Researcher session/CLAIM/OPEN/checkpoint/Result here. The current support owner is issue #1558; native p=373 H0/B0 [X]U modulo 139129 remains issue #1559 PENDING_OWNER. Historical protected staging was not modified.

**Next smallest mother-target unit**: derive a terminating signed Green/WZ or Clausen source-level certificate for original W216-V2304 mod p³ in p≡13,19 mod24, retaining the p≡13 triangular boundary correction; compare exact boundary terms at p=13,19,97,373. Do not repeat the already-published fourth-digit reflection or the prior Clausen/Green proofs.