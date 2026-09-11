# RSA-270 continuation: primitive-character Galois projector closes the all-level weighted-BRC formula gap

Status: `RESEARCH NOTE / EXACT ALL-LEVEL PROJECTOR THEOREM / N-ONLY EVALUATION OPEN`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T00:13:30+08:00`  
Parents:
- `research_notes/RSA270_CHARACTER_WEIGHTED_BRC_INTERFACE_20260906.md`
- `research_notes/RSA270_EXPLICIT_TERNARY_TRACE_DECODER_20260906.md`
- `research_notes/RSA270_3ADIC_TORSION_PACKET_LADDER_20260906.md`

No RSA-270 factor is obtained.

This note closes one explicit mathematical gap left in the parent interface: beyond level `e=2`, a fixed exact functional from the multiplied BRC profile to the faithful twisted divisor sum `A_e(n)` had not been written down. It now is.

## 1. Setup

Let

`m=3^e`, `e>=2`,

`zeta=zeta_m`,

and let `chi=chi_e` be the faithful primitive Dirichlet character modulo m defined by choosing 2 as primitive root and setting

`chi(2)=xi`, where `xi` is a primitive `phi(m)=2*3^(e-1)`-th root of unity.

Then `chi` is odd:

`chi(-1)=-1`.

For odd `n` with `gcd(n,3)=1`, define

`A_e(n)=sum_(d|n) chi(d)`.

Let `P_(mn)(u)` be the exact divisor-profile coefficient already used throughout the RSA-270 line.

## 2. Gauss/Galois character projector

For every unit `a mod m`, let

`sigma_a(zeta)=zeta^a`

be the corresponding Galois automorphism of `Q(zeta_m)`.

Let

`tau(conj(chi)) = sum_(a mod m) conj(chi(a)) zeta^a`

be the primitive Gauss sum, and define the linear projector

`Pi_chi(Z)
 := [1/tau(conj(chi))] sum_(a mod m)^* conj(chi(a)) sigma_a(Z)`.

The star means units modulo m.

### Monomial projector lemma

For every integer t,

`Pi_chi(zeta^t)=chi(t)`,

where the Dirichlet character is extended by zero on nonunits.

Proof: for unit t, substitute `b=at` in the Gauss sum; for nonunit t, primitivity gives zero. This is the standard Gauss-sum Fourier identity, here used as an exact Galois projector.

## 3. Normalized multiplied profile

Set

`D(zeta)=(zeta^2-1)/(2zeta)`

and

`Z_(e,n)=D(zeta) P_(mn)(zeta)`.

For one profile block with

`t=(d+mn/d)/2`,

we have

`D(zeta) W_(t+1)(zeta)=1/2 (zeta^t-zeta^-t)`.

Every divisor of `mn` is `d=3^j a` with `a|n`, `0<=j<=e`.

If `1<=j<=e-1`, then both `d` and its complementary divisor are divisible by 3, hence

`t=(d+mn/d)/2 ≡ 0 (mod3)`.

Therefore

`Pi_chi(zeta^t)=Pi_chi(zeta^-t)=0`.

**All intermediate 3-adic multiplier packets are annihilated automatically by the primitive character projector.**

Only the two extreme divisor layers `j=0,e` survive.

## 4. All-level projector theorem

At `j=0`, for `a|n`,

`t=(a+m n/a)/2 ≡ a/2 (mod m)`.

At `j=e`,

`t=(m a+n/a)/2 ≡ (n/a)/2 (mod m)`.

Since chi is odd,

`chi(r/2)-chi(-r/2)
 = 2 chi(2)^(-1) chi(r)`.

Summing the two extreme layers and using the divisor involution `a <-> n/a` gives:

**Theorem (primitive-character BRC projector).** For every odd `n` coprime to 3,

`Pi_chi( Z_(e,n) ) = 2 chi(2)^(-1) A_e(n)`.

Equivalently,

`A_e(n)
 = [chi(2)/2] Pi_chi( ((zeta^2-1)/(2zeta)) P_(3^e n)(zeta) )`.

This is exact for every `e>=2`; it is not restricted to semiprimes.

The attached verifier checks the identity on 32 `(e,n)` cases through `e=5`, including primes and composites, and separately verifies the Gauss projector on all monomials through `e=4`.

## 5. Semiprime consequence

For `N=pq`,

`A_e(N)=(1+chi(p))(1+chi(q))
       =1+chi(N)+chi(p)+chi(q)`.

N gives the product

`chi(p)chi(q)=chi(N)`.

The projector gives the sum

`chi(p)+chi(q)=A_e(N)-1-chi(N)`.

Because `chi_e` is faithful, sum + product determine the unordered factor character values and therefore the unordered residues `{p,q} mod 3^e`.

Thus the multiplied BRC profile contains the faithful factor-residue coefficient at **every 3-adic level through one fixed explicit Galois/Fourier projector**.

This strengthens the parent `CHARACTER_WEIGHTED_BRC_INTERFACE` statement, where exact equality with a fixed general-level BRC functional was still open.

## 6. Important correction to the computational interpretation

The theorem is a mathematical interface, not yet an efficient algorithm.

Naively,

`Pi_chi`

contains `phi(3^e)=2*3^(e-1)` Galois conjugates, and the Gauss/cyclotomic representation dimension grows with the level. Therefore:

`EXPLICIT ALL-LEVEL PROJECTOR != COMPACT N-ONLY EVALUATOR`.

The existing 2-4 integer ternary-trace decoder remains computationally sharper when previous factor residues are known: it performs sparse candidate discrimination rather than constructing the full faithful Fourier coefficient.

The new theorem nevertheless removes two algebraic nuisances:

1. no ad-hoc subtraction of intermediate multiplier packets is needed for the dense faithful projector — primitivity kills them automatically;
2. the target coefficient is now exactly identified with the pre-existing `A_e(n)` at every level, not merely known to be factor-residue equivalent.

## 7. Radix-3 factorization of the dense projector

The dense Galois sum itself has a compact **operator factorization**, even though applying it to an explicitly expanded cyclotomic vector may still cause exponential state growth.

Use the decomposition

`(Z/3^e Z)^* = {+-1} x <4>`,

where 4 has order

`L=3^(e-1)`.

Let

`eta=chi(4)`

(a primitive L-th root), and write `Y=sigma_4` as the Galois shift operator. The 3-primary projector numerator is

`sum_(k=0)^(L-1) conj(eta)^k Y^k`.

By the unique base-3 expansion of k,

`sum_(k=0)^(L-1) conj(eta)^k Y^k
 = product_(j=0)^(e-2)
   [ 1 + (conj(eta) Y)^(3^j) + (conj(eta) Y)^(2*3^j) ]`.

The odd part contributes the two-term factor

`1-sigma_-1`.

Hence the full faithful projector numerator factors into

- one 2-term odd projector;
- `e-1` three-term radix-3 projectors.

The verifier checks this factorization through `e=6`.

This is the structural match to the existing ternary BRC decoder: the dense faithful Fourier projector is a radix-3 cascade, while the decoder reads only the few local traces needed to select the next lift.

## 8. Product-side meaning and next target

The parent note already identified

`sum_(n>=1) A_e(n) q^n
 = sum_(d>=1) chi_e(d) q^d/(1-q^d)`

as the twisted Lambert / weight-1 Eisenstein coefficient series.

The present theorem now gives a direct coefficient-level bridge:

`multiplied BRC profile at 3^e-torsion`
` -> primitive Gauss/Galois projector`
` -> faithful twisted divisor sum A_e(n)`.

The remaining problem is therefore not algebraic identification. It is **state complexity / N-only evaluation**.

Highest-value next question:

> Can the radix-3 projector factors be pushed through the BRC product/generating-function representation while keeping only a bounded or polylogarithmic state per level, rather than expanding a `3^e`-dimensional cyclotomic coefficient vector?

A positive answer would turn the now-explicit all-level interface into a factor-residue algorithm. A negative answer should identify exactly where the state dimension necessarily expands and would provide a strong no-go theorem for the current 3-adic character route.
