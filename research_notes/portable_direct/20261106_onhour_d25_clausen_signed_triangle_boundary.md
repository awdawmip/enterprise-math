# D25 TASK_RESEARCH — exact Clausen triangular boundary for the original 216 carrier

Date: 2026-11-06. Status: **AUTHOR-PROVED (one finite-modulus theorem) / EXACT FINITE CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0**.
Canonical Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; **unchanged frozen scientific Source pin** `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane only: `chatgpt-research-onhour-enterprise-math-20260923`. No maintenance-lane action.
Parent target remains `Delta_p - R_p = 0 (mod p)` for p=13,19 (mod 24), with the separately frozen scalar bridge to `W_p = p (mod p^3)`. The published Guo–Zudilin 2304 result was consumed earlier, not reproved. Native original-class fixed H0/B0 experiment (#1559) remains NOT_RUN / PENDING_OWNER.

## 1. Classical Clausen identity applied to the exact original 216 coefficients

Let
[
a_n=\frac{(2n)!(3n)!}{216^n(n!)^5},quad
W_p=\sum_{n=0}^{p-1}(6n+1)a_n,quad
d_n=\frac{(1/6)_n(1/3)_n}{2^n(n!)^2}
=\frac{\prod_{t=0}^{n-1}(6t+1)(3t+1)}{36^n(n!)^2}.
]
Clausen's classical formal-series formula (NIST DLMF §16.12.2; take a=1/6,b=1/3) gives exactly
[
\left[{}_2F_1(1/6,1/3;1;z)\right]^2
={}_3F_2(1/2,1/3,2/3;1,1;z).
]
The original 216 coefficient equals `(1/2)_n(1/3)_n(2/3)_n/[2^n(n!)^3]`. Comparing coefficients and evaluating at z=1/2 yields the **exact rational** identity
[
\boxed{a_n=\sum_{i+j=n}d_i d_j,qquad
W_p=\sum_{i+j<p}(1+6i+6j)d_i d_j.}\tag{1}
]
This is a triangular sum, NOT the full product of two truncated sums. Source for the classical identity: https://dlmf.nist.gov/16.12.E2 .

## 2. Exact valuation filtration and nonzero triangular overflow

Fix any prime `p=6m+1>3`. For `0<=n<p`, all factors of `36^n(n!)^2` are units in `Z_(p)`. The sole p-divisible factors of the two numerator progressions in that index range occur at t=m (6t+1=p) and t=2m (3t+1=p). Hence
[
v_p(d_n)=
\begin{cases}
0&0\le n\le m,\\
1&m<n\le2m,\\
2&2m<n<p.
\end{cases}\tag{2}
]
Set `S_p=sum_{n=0}^{p-1}d_n`, `T_p=sum_{n=0}^{p-1} n d_n`. The full square weighted sum equals exactly `S_p^2+12S_p T_p`. Its omitted half-plane `i+j>=p` has, modulo p³, ONLY the two ordered branches with one low index `1<=i<=m` and the other high index `j=p-r,1<=r<=i`. Low/low, low/middle, and middle/middle never overflow; middle/high and high/high have valuation >=3. Thus
[
W_p\equiv S_p^2+12S_pT_p-
2p^2\sum_{i=1}^m\sum_{r=1}^i
(1+6(i-r))\,d_i\,\frac{d_{p-r}}{p^2}
\pmod{p^3}.\tag{3}
]
The factor `2` here counts the two **labelled ordered branches**. All signs, p-adic carries and truncation geometry are retained.

## 3. Explicit complementary high-index coefficient (no hidden native assumption)

For `1<=r<=m`, define the finite mod-p unit
[
e_r=
\frac{36^{r-1}[(r-1)!]^2}
{\prod_{s=1}^r(1-6s)(1-3s)}
\in\mathbb F_p.\tag{4}
]
No denominator factor is zero modulo p in the stated range. Wilson's theorem and the complete residue products of `(6t+1)` and `(3t+1)` for t=0,...,p-1 show
[
\boxed{d_{p-r}/p^2\equiv e_r\pmod p.}\tag{5}
]
Explicitly, after removing the respective single p factor and omitting the last r terms,
[
(1/6)_{p-r}/p\equiv
-\frac{6^{r-1}}{\prod_{s=1}^r(1-6s)},quad
(1/3)_{p-r}/p\equiv
-\frac{3^{r-1}}{\prod_{s=1}^r(1-3s)}
\pmod p.
]
Further, `(p-r)!≡(-1)^r/(r-1)! (mod p)` and `2^{-(p-r)}≡2^{r-1} (mod p)`, proving (5). Define
[
J_p=\sum_{i=1}^m\sum_{r=1}^i(1+6(i-r))d_i e_r\pmod p.
]
Substituting (5) into (3) proves the directly usable **new finite boundary certificate**:
[
\boxed{W_p\equiv S_p(S_p+12T_p)-2p^2 J_p\pmod{p^3}}
\qquad\text{for ALL primes }p\equiv1\pmod6.\tag{6}
]

Consequently, on the original target classes p=13,19 (mod24), the OPEN universal 216 statement `W_p≡p (modp^3)` is **equivalent** to the explicitly labelled quadratic/boundary congruence
[
\boxed{S_p(S_p+12T_p)\equiv p+2p^2J_p\pmod{p^3}}.\tag{7}
]
No unproved factor divisibility is needed for this equivalence. If `p|S_p` is independently established, (7) can then be divided by p to reduce its modulus to p²; such uniform first-factor vanishing is NOT proved here.

## 4. Integer verification and discriminating counterexample to dropping branches

A Python stdlib-only checker reconstructs both original coefficients and the Gauss coefficients modulo p³, computes `S,T,J,W` independently, checks (5) for all r<=m and (6) for **all 80 primes 7<=p<=997 with p≡1 (mod6)** (including **45 frozen target primes**). It also checks (1) exactly as rational coefficients n=0,...,8 and independent modular convolution for p=7,13,19. **All asserted checks passed; 0 assertion failures**.

| p | S mod p | S+12T mod p | 2J mod p | full-square S(S+12T) mod p³ | corrected W mod p³ |
|---:|---:|---:|---:|---:|---:|
| 7 | 2 | 0 | 3 | 154 | 7 |
| 13 | 0 | 6 | 0 | 13 | 13 |
| 19 | 0 | 12 | 12 | 4351 | 19 |
| 37 | 0 | 29 | 11 | 15096 | 37 |
| 43 | 0 | 25 | 15 | 27778 | 43 |
| 67 | 0 | 11 | 21 | 94336 | 67 |
| 373 | 0 | 171 | 196 | 27269657 | 373 |

**Adversarial p=19**: the naive full-square replacement yields 4351 mod 19³=6859, whereas the original 216 sum gives 19. Their difference is `4332=12*19²`; the correction `2J=12 (mod19)` accounts for it exactly. At p=373 the correction is `196*373²` modulo 373³. It cannot be silently discarded. Across the frozen 45 test primes, the correction is nonzero for **44**, and zero for p=13.

Finite observation only (NOT a theorem): among those 45 target primes, `S_p=0 (mod p)`; for the other 35 primes p≡1 (mod6) up to 997, `S_p+12T_p=0 (mod p)`. This split suggests a residue-character/CM explanation and is an admissible next discriminating lemma, **not** a proof of either uniform factor law or of the mother supercongruence.

## 5. BRC / observer scope and next exact proof unit

`COMPOSE_APPLIED`: the original 216 index population and its signed weights are preserved under the *exact* Clausen convolution (1). Labelled low/high pair incidence, complement index r, valuations 0/1/2, full-square projection and signed overflow correction are explicit. Equation (6) permits compression only for the declared output W modulo p³ and this single sum/product operation. It does not identify the native H0/B0 module, crystalline Frobenius, eta, kappa, six-dimensional world dynamics, nor any mod-p⁴ result. The triangle-vs-square difference is a concrete information-loss witness.

NEXT: prove/disprove the observed `p|S_p` for p≡13,19 (mod24) using a source-authorized finite-field/Jacobi or modular interpretation, **then** construct the two-digit congruence `(S_p/p)(S_p+12T_p)≡1+2pJ_p (modp²)`; test existing p=19,373 nonzero overflow first. This is an alternative direct 216 proof route, not a replacement for already completed bottom-jet and shell work. Original native benchmark #1559 remains PENDING_OWNER / NOT_EXECUTED. Formal Source CLAIM, Result and independent review have NOT been performed by this note.

**Sources:** classic Clausen formula NIST DLMF §16.12.2 (external theorem); frozen original 216 source; prior Guo–Zudilin elimination note at `d8006c283f417c5c087da8fbaf0411f0316a73b3`; own author-side exact finite checker. Evidence status: AUTHOR_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED.
