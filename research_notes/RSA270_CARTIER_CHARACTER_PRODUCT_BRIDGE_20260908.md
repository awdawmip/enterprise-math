# RSA-270 continuation: repeated ternary Cartier section + character projector = twisted Eisenstein/Lambert series

Status: `RESEARCH NOTE / EXACT GENERATING-SERIES BRIDGE / N-ONLY COEFFICIENT COST OPEN`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-08T00:26:51+08:00`  
Parent: `research_notes/RSA270_PRIMITIVE_CHARACTER_GALOIS_PROJECTOR_20260908.md`

No RSA-270 factor is obtained.

## 1. The exact BRC product series

Let

`F(Q,u)=sum_(M>=0) P_(2M+1)(u) Q^M`

be the bivariate BRC/divisor-profile generating series, equivalently the Ramanujan/Kac-Cheung product already used in the RSA-270 line.

For a q-series

`f(Q)=sum_(M>=0) a_M Q^M`,

define the ternary Cartier section operators

`C_r f(Q)=sum_(M>=0) a_(3M+r) Q^M`,  `r in {0,1,2}`.

## 2. The target 3^e multiplier is the all-ones ternary Cartier path

Let `m=3^e` and

`c_e=(m-1)/2`.

Because

`c_e = 1+3+3^2+...+3^(e-1)`,

its base-3 expansion is exactly `111...1` (e digits).

Repeated middle-section extraction therefore gives

`C_1^e F(Q,u)
 = sum_(R>=0) P_(3^e(2R+1))(u) Q^R`.

Proof: after e applications the surviving original coefficient index is

`M=3^e R + (3^e-1)/2`,

hence

`2M+1=3^e(2R+1)`.

This converts the multiplied-profile tower into one fixed radix-3 coefficient path, with no ambiguity in the selected residue class.

## 3. Combine with the primitive-character projector

Let `zeta=zeta_(3^e)`, let `chi_e` be the faithful primitive odd character modulo `3^e`, and define

`D_e=(zeta^2-1)/(2zeta)`.

The parent projector theorem was proved coefficientwise for every odd n (the proof actually does not require `3∤n`; divisors carrying a 3-power have character value zero). Therefore

`[chi_e(2)/2] Pi_(chi_e)( D_e P_(3^e n)(zeta) )
 = A_e(n)`

for every odd positive integer n, where

`A_e(n)=sum_(d|n) chi_e(d)`.

Applying this coefficientwise to the Cartier identity gives the exact series theorem:

**Theorem (Cartier-character product bridge).**

`[chi_e(2)/2] Pi_(chi_e)( D_e C_1^e F(Q,zeta) )
 = sum_(R>=0) A_e(2R+1) Q^R`.

Thus a single repeated ternary section of the original BRC product, followed by the now-explicit faithful Galois projector, is **exactly the odd-index twisted divisor-sum series**.

## 4. Relation to the standard Lambert / weight-1 Eisenstein series

Define

`L_e(q)=sum_(n>=1) A_e(n) q^n
      =sum_(d>=1) chi_e(d) q^d/(1-q^d)`.

Let

`H_e(Q)=sum_(R>=0) A_e(2R+1) Q^R`.

Then the odd part of the Lambert series is

`L_e^odd(q)=q H_e(q^2)`.

Since `A_e` is multiplicative and 2 is coprime to the conductor,

`L_e(q)=sum_(v>=0) A_e(2^v) L_e^odd(q^(2^v))`,

with

`A_e(2^v)=1+chi_e(2)+...+chi_e(2)^v`.

Therefore the Cartier-character BRC series determines the complete standard twisted Lambert / weight-1 Eisenstein coefficient series by an explicit 2-adic reconstruction.

This is the direct generating-series version of the coefficient-level character interface:

`RAMANUJAN/BRC PRODUCT F`
` -> e copies of C_1`
` -> 3^e-torsion normalization`
` -> faithful Gauss/Galois projector`
` -> weight-1 twisted Eisenstein/Lambert coefficients A_e`.

## 5. Why this is stronger than the earlier interface

Earlier notes had established separately:

- the multiplied torsion packet is factor-residue complete;
- a constant-width ternary trace decoder exists given the previous residue state;
- `A_e(n)` is factor-residue complete;
- level e=2 admits an explicit equality between a BRC trace and `A_2`.

The two new notes now close the missing algebraic chain at **every level**:

1. `P_(3^e n)(zeta_(3^e)) -> A_e(n)` by one explicit primitive-character projector;
2. the whole family `n=1,3,5,...` is obtained directly from the original product by the repeated middle Cartier path `C_1^e`.

So the open problem is no longer “which arithmetic coefficient is the BRC packet computing?” It is solely **how expensive the repeated section/projector is when performed from the product side at a huge target index**.

## 6. Computational frontier: a double radix-3 problem

Two independent structures are now radix-3 cascades:

1. the coefficient selector is `C_1^e` — the all-ones ternary digit path;
2. the faithful Galois projector numerator factors into one odd 2-term operator and `e-1` three-term character projectors.

This creates a concrete possibility that did not exist in #1330's fixed-modulus analysis:

> push the coefficient Cartier cascade and the character Galois cascade through the infinite product **together**, looking for a bounded-state or polylog-state recursion.

If the product admits such a stable finite-dimensional state, `A_e(N)` could become N-only computable one 3-adic digit at a time and the branch-oracle reduction would factor RSA-270 under H2.

If the required state dimension provably grows like `3^e` (or otherwise super-polynomially in e), the same formulation gives a sharp no-go theorem.

## 7. Next exact unit

Do not enumerate cyclotomic coefficients or more multipliers.

Define the state space generated from the product `F(Q,u)` under the paired operators

`(C_1, character-relative-3-projector)`

for one level, then two levels, and compute its minimal exact dimension for small e. The discriminating question is whether the dimension stabilizes, grows polynomially in e, or triples at each level.

This is now the highest-value experiment because it directly tests the only remaining gap between an exact factor-residue coefficient and an N-only algorithm.
