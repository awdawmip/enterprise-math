# D25 integer-shadow two-jet bridge for signed 216

Date: 2026-11-05. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

Evidence grade: **AUTHOR-DERIVED EXACT ALGEBRA / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED**. This is a portable auxiliary calculation, not the original-class H0/B0 native experiment or a Source CLAIM/checkpoint.

## New connection: terminating integer shadow has two explicit p-adic jets

Fix a prime `p=6n+1>=7`, set `m=(3n,2n,4n)` and `beta=(1/2,1/3,2/3)`. Work in `Z_(p)` and take `0<=k<p`. Define

`v_k=#{j: k>m_j}`,

`q_k=2^(-k)(k!)^(-3) prod_{j=1}^3[ beta_j^(1_{k>m_j}) prod_{0<=r<k,r!=m_j}(r-m_j) ]`,

`h_{a,k}=sum_{j=1}^3 sum_{0<=r<k,r!=m_j} (beta_j/(r-m_j))^a` for `a=1,2`.

Every displayed denominator is a p-unit. Define the exact rational coefficient

`a_k=((1/2)_k(1/3)_k(2/3)_k)/(2^k(k!)^3)`.

**Exact factorization**, not merely a congruence:

`a_k=p^(v_k) q_k prod_{j,r!=m_j}(1+p beta_j/(r-m_j))`.

The valuation regions are `v=0` on `[0,2n]`, `v=1` on `[2n+1,3n]`, `v=2` on `[3n+1,4n]`, `v=3` thereafter. Set

`S=sum_{k=0}^{2n}(6k+1)q_k`,

`A=sum_{k=0}^{2n}(6k+1)q_k h_{1,k} + sum_{k=2n+1}^{3n}(6k+1)q_k`,

`B=sum_{k=0}^{2n}(6k+1)q_k (h_{1,k}^2-h_{2,k})/2 + sum_{k=2n+1}^{3n}(6k+1)q_k h_{1,k} + sum_{k=3n+1}^{4n}(6k+1)q_k`.

For `W_p=sum_{k=0}^{p-1}(6k+1)a_k`, finite-product Taylor expansion gives, for **every** such prime,

`W_p = S + p A + p^2 B (mod p^3)`.     (SHADOW-JET-2)

For `k<=2n`, `q_k=(-1)^k 2^(-k) binom(2n,k)binom(3n,k)binom(4n,k)`; hence **exactly over Q**, not merely modulo p,

`S=4^(-n) C_n` where `C_n=sum_{k=0}^{2n}(6k+1)(-1)^k 2^(2n-k) binom(2n,k)binom(3n,k)binom(4n,k)`.

Thus the earlier terminating integer shadow is the constant Taylor port of a single finite p-adic deformation, while `A` and `B` reconstruct the missing first/second digits. This keeps the low-, medium-, high-valuation source identities separate until the terminal observer.

## An exact two-port residual certificate

Assume `p|S` and `S+pA=p (mod p^2)` (both are known for target primes if the frozen first-digit identity `W_p=p (mod p^2)` is consumed with SHADOW-JET-2). Define

`carry_p=((S+pA-p)/p^2) mod p`, `jet_p=B mod p`.

Then the exact identity

`(W_p-p)/p^2 = carry_p+jet_p (mod p)`     (RESIDUAL-2)

holds. When the separately sourced scalar-interface bridge `Delta_p-R_p=(W_p-p)/p^2 mod p` is used with its original hypotheses, (RESIDUAL-2) supplies an equivalent two-port auxiliary observer. It does not itself discharge the all-prime LIFT identity.

## Independent exact certificate

A Python integer modular checker computes `S,A,B` via factor-by-factor derivative recurrence (no direct original W coefficients) and independently computes `W_p` using the original signed-216 ratio `a_{k+1}/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3)`. It also computes `C_n` from integer binomial coefficients and compares exact residues.

**94/94 primes** `7<=p<=1200, p=1 mod 6` pass the exact formula, integer-shadow equality, and finite `W_p=p mod p^3` check. In each example the two ports cancel:

| p | S mod p^3 | A mod p^2 | B mod p | carry mod p | carry+B mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 442 | 6 | 10 | 3 | 0 |
| 19 | 5491 | 282 | 8 | 11 | 0 |
| 373 | 15521276 | 47909 | 133 | 240 | 0 |

The 94-prime check is regression/falsification evidence, not a proof of `W_p=p mod p^3`. The formula (SHADOW-JET-2) itself is a general exact algebraic result. The all-integer assertion `(6n+1)|C_n` remains a conjecture.

## Continuation / provenance

Mother target: `Delta_p-R_p=0 mod p` for `p=13,19 mod24`; native p373 H0/B0, `[X]U mod 139129`, semilinear direction, eta, kappa and independent review stay with their existing controls. Scientific inputs remain fixed at the task's frozen pin. Do not repeat the parent UR/JT0, the already verified high-tail valuation analysis or earlier finite-prime scans.

Next mathematical unit: express `carry_p` and `B` using a common finite WZ/telescoping or parameter-derivative operator, then prove their all-target cancellation or give one exact counterexample. Separately test the all-n integer-divisibility conjecture by finding a closed certificate rather than increasing its finite search window. Native recovery: reconcile original failed `em-h20-20261105-1620-current-continuation`; current read request `research-hourly20-20261105-1720-native-continuation` must attain terminal status and Source verification before any protected mutation. Do not reuse maintenance conversation or invent a current claim/session.
