# D25 AF4 — exact Pfaff short-root and signed p²-band decomposition

2026-11-09. TASK_RESEARCH author-side mathematical derivation; **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE H0/B0**.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Original Source-native frontier remains `b58330b74576153cdadde5d80a3d92df3a819a0e`. This note continues the 20261109 Gauss affine first-jet certificate and retains its P/L/T source bands.

## 1. A shorter exact root problem (proved)

Let p be any prime with `p≡13 (mod 24)`, and put

`m=(p+3)/8`, `a=(5p-1)/8=5m-2`, `b=(7p-3)/8=7m-3=p-m`.

Then `p=8m-3`, `1<m<a<b<p`. Write

`P(z)=sum_{k=0}^a binom(a,k)binom(b,k) z^k` in `F_p[z]`, and

`R(z)=sum_{k=0}^{m-1} (-1)^k binom(a,k)binom(m-1,k) z^k (1-z)^(m-1-k)`.

**Theorem (all such p, polynomial identity in F_p[z]).**

`boxed{P(z)=(1-z)^(4m-1) R(z) = (1-z)^((p+1)/2) R(z)}`.

Proof: the terminating Pfaff identity is an exact rational polynomial identity:

`P(z)=(1-z)^a sum_{k=0}^a [(-a)_k (b+1)_k/(k!)²] (z/(z-1))^k`.

Since `b+1=p+1-m`, every `(b+1)_k` for `k≥m` contains exactly one factor p, and for `k<m` it equals `(1-m)_k (mod p)`. Hence the surviving terms are

`(1-z)^a sum_{k=0}^{m-1} binom(a,k)binom(m-1,k) (z/(z-1))^k`.

Clearing denominators yields the displayed polynomial factorization, as `a-m+1=4m-1`. The division was only a proof step in the rational function field; the final assertion is an equality of polynomials over F_p.

At `z=1/9`, `1-z=8/9` is a p-unit, so the unsolved original condition `P(1/9)=0 (mod p)` is **equivalent** to the much shorter

`boxed{Q0=sum_{k=0}^{m-1} (-1)^k binom(a,k)binom(m-1,k)8^(-k) = 0 (mod p)}`.

Here the sum length is `m=(p+3)/8` instead of `a+1=(5p+7)/8`; e.g., at p=373 it uses 47 rather than 234 summands. This reduction is a true equality of the declared scalar observer mod p. It does not discard the higher-precision boundary.

## 2. The missing p-adic digit is an explicit signed edge band (proved)

All terms below are in `Z_(p)`; `Q0` is computed modulo `p²`, `Q1,Qedge` modulo p. Define `q_k=(-1)^k binom(a,k)binom(m-1,k)8^(-k)` for `0≤k<m`, and `H_j=sum_{r=1}^j1/r`, `H_0=0`. Set

`Q0 = sum_{k=0}^{m-1} q_k (mod p²)`

`Q1 = -sum_{k=0}^{m-1} q_k (H_(m-1)-H_(m-1-k)) (mod p)`

`Qedge = (-1)^(m-1)(m-1)! sum_{k=m}^a binom(a,k)(k-m)!/(k!8^k) (mod p)`.

**Theorem (all such p, modulo p²).**

`boxed{P(1/9) ≡ (8/9)^a [Q0+p(Q1+Qedge)] (mod p²)}`.

Proof: in the exact terminating Pfaff identity, expand `(p+1-m)_k` at p. For k<m, factor `(1-m)_k` and expand the product `prod_{j=0}^{k-1}(1+p/(1-m+j))` to first order; its logarithmic jet is `-(H_(m-1)-H_(m-1-k))`. For m≤k≤a, the factor at j=m-1 is precisely p; the other factors reduce modulo p to `(-1)^(m-1)(m-1)!(k-m)!`. Insert `z/(z-1)=-1/8`; signs of `(-a)_k` and `(-1/8)^k` cancel in the edge band. Since `a+m-1<p`, no second multiple of p occurs. This proves the identity directly from integer/rational products.

When `Q0≡0 (mod p)`, it follows that

`boxed{ P(1/9)/p ≡ (8/9)^a [Q0/p+Q1+Qedge] (mod p) }`.

Combining the pre-existing affine Gauss first-jet `M_p=P+p(L+T) (mod p²)` gives the **equivalent** residual certificate

`(8/9)^a [Q0/p+Q1+Qedge] + L+T ≡ 0 (mod p)`.

`L` is the low-band parameter jet and `T` is its middle-index single-zero band from the predecessor proof; they retain separate provenance. The Pfaff high-index `Qedge` is another typed, signed band; it must not be merged with `T` absent an exact observer-safe relation.

## 3. Executed exact checks and reproducibility

All calculations use integer modular arithmetic; no floating point. The companion standalone Python script independently evaluates original `P` and its derivative and the Pfaff polynomial/band expressions for **all 157 primes p≤10000, p≡13 (mod24)**. For each p: the factorization and derivative agree modulo p; the Pfaff three-band expression agrees with original P modulo p²; `Q0=0 (mod p)` is observed; and `R'(1/9)≠0 (mod p)` is observed. The last two are **finite observations**, not uniform theorems.

| p | m | Q0/p | Q1 | Qedge | (8/9)^a mod p | P/p | R'(1/9) mod p |
|--:|--:|--:|--:|--:|--:|--:|--:|
|13|2|0|1|10|9|8|4|
|37|5|8|25|14|20|15|11|
|61|8|47|30|56|27|53|27|
|109|14|60|98|3|15|17|14|
|373|47|296|112|183|180|75|369|

For p=373, `180*(296+112+183)=75 (mod 373)`. The predecessor independent affine data `L=66,T=232` then give `75+66+232=0 (mod373)`. This reproduces the *same* original Gauss first-jet observation without relabeling it as an H0/B0 native computation.

## 4. BRC and observer scope; next exact action

Applied typed BRC/signed-band bookkeeping to the population `k=0..a`, distinguishing the low unit `Q0`, its first jet `Q1`, and the single-zero `Qedge`; the previous affine bands `L,T` and all carry/divisibility information remain separate. Allowed readouts are P mod p², P/p when divisible, and the corresponding Gauss affine M/p. These are *external scalar calculations* under the existing X6 project worldview; no new spatial axis/native Frob map is inferred.

Next: prove the shortened terminating polynomial root `Q0≡0 mod p` for all p≡13 mod24 (or identify an exact counterexample), then attempt the full signed five-band cancellation. A promising route is a Jacobi/finite-field character-sum representation of the degree-(m-1) polynomial, or a finite WZ relation retaining the p² edge. Avoid recalculating the predecessor's 157-prime M scan.

Independent highest-priority native obligation remains issue #1559: actual p=373 same-original-class fixed H0/B0 divided-power `[X]U mod139129`, module rank, semilinear direction/eta, signed kappa, Delta-R and independent replication. No native CLAIM, run, benchmark, Result, independent review, or canonical admission is asserted by this author-side record.
