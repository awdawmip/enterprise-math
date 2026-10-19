# RSA-270 continuation: exact cubic recursion for the faithful-character tower

Status: `RESEARCH NOTE / EXACT THEOREMS / BRANCH SELECTION OPEN N-ONLY`  
Researcher-ID: `EM-DIRECT-66DE45`  
Research mode: `TASK_RESEARCH`  
At: `2026-09-06T20:31:34+08:00`  
Parent: `research_notes/RSA270_CHARACTER_WEIGHTED_BRC_INTERFACE_20260906.md`

No RSA-270 factor is obtained.

## 1. Compatible faithful characters

For `e>=1`, let

`phi_e = 2*3^(e-1)`

and define the faithful primitive character modulo `3^e` by

`chi_e(2)=zeta_(phi_e)`.

Because 2 is a primitive root modulo every `3^e`, this is faithful. The characters are compatible:

`chi_(e-1)(a) = chi_e(a)^3`

for every `a` coprime to 3.

For a squarefree semiprime `N=pq`, define

`P_e := chi_e(N) = chi_e(p) chi_e(q)`,
`T_e := chi_e(p) + chi_e(q)`,
`A_e := sum_(d|N) chi_e(d) = 1 + P_e + T_e`.

`P_e` is N-only computable from `N mod 3^e`. The factor-split information is exactly `T_e`.

## 2. Exact cubic recursion

Let

`x=chi_e(p)`, `y=chi_e(q)`.

Then

`x^3+y^3 = chi_(e-1)(p)+chi_(e-1)(q)=T_(e-1)`,

and `xy=P_e`.

Therefore

`T_e^3 = x^3+y^3+3xy(x+y)
       = T_(e-1)+3 P_e T_e`.

Hence:

**Theorem (character cubic recursion).**

`T_e^3 - 3 P_e T_e - T_(e-1) = 0`.

Everything in the cubic except the root choice is known from N and the previous level.

## 3. The three roots are exactly the three factor-lift branches

Let `omega` be a primitive cube root of unity. Fix one compatible lift pair `(x,y)` with product `P_e`. The three product-preserving lifts of the previous character pair are

`(omega^k x, omega^(-k) y)`, `k=0,1,2`.

Their sums are

`T_e^(k)=omega^k x + omega^(-k)y`.

Each satisfies the same cubic because cubes erase omega and the product remains `P_e`. Conversely the cubic has degree 3, so these are exactly its roots counted with multiplicity.

Thus the 3-adic Hensel digit is literally the choice of one root of the known cubic.

At the first H2 level:

`P_1=1`, `T_1=-2`.

For e=2 with RSA-270 `P_2=1`,

`T_2^3-3T_2+2=0 = (T_2-1)^2(T_2+2)`.

The two unordered branches are:

- `T_2=1` -> `A_2=3` -> level-9 BRC trace 36;
- `T_2=-2` -> `A_2=0` -> level-9 BRC trace 0.

The double root reflects inversion/unordered identification of the two nontrivial cubic phases at the singular first lift.

## 4. Exact coefficient norm recursion

The character-value field grows by a cubic cyclotomic extension at each step. The relative conjugates send a lift root `x` to `x, omega x, omega^2 x`.

Therefore

`Norm_(e/e-1)(1+x)
 = (1+x)(1+omega x)(1+omega^2 x)
 = 1+x^3`.

Apply this independently to `x=chi_e(p)` and `y=chi_e(q)`:

**Theorem (Eisenstein-coefficient norm tower).**

`Norm_(e/e-1)(A_e) = A_(e-1)`.

Unlike the earlier norm identity for the full bivariate q-series, this is a norm recursion for the **target coefficient itself** and has no coefficient convolution.

It still does not choose the upper-level conjugate/root: norm deliberately erases precisely the missing trit.

## 5. Discriminant and cyclic-cubic structure

The cubic

`X^3 - 3P_e X - T_(e-1)`

has discriminant

`Delta_e = 27(4P_e^3 - T_(e-1)^2)
         = -27( T_(e-1)^2 - 4P_(e-1) )`.

But

`T_(e-1)^2 - 4P_(e-1)
 = (chi_(e-1)(p)-chi_(e-1)(q))^2`.

Hence the discriminant is `-27` times a square in the lower character field. From levels whose lower field contains the cubic roots of unity, this is the expected cyclic-cubic/Kummer pattern.

The algebraic structure therefore matches the BRC ternary decoder exactly:

`LOWER CHARACTER STATE -> KNOWN CUBIC -> THREE GALOIS ROOTS -> ONE FACTOR-LIFT TRIT`.

## 6. Computational interpretation

This removes another layer of unnecessary search. If `T_(e-1)` is known, the next state is not an arbitrary residue among `3^e` possibilities; it is one of three explicitly constructible algebraic candidates.

The explicit ternary twisted-trace decoder from the companion note gives a constant-width way to identify which candidate is correct **if** the required BRC residue-flow integers can be evaluated from N.

Thus the remaining question is now maximally concentrated:

> Given N, the known cubic coefficients `(P_e,T_(e-1))`, and its three roots, can an Enterprise/BRC N-only observable select the correct root without recreating the hidden divisor/factor split?

The norm, ordinary character `chi_e(N)`, and any other factor-symmetric operation on the already-collapsed N cannot do so; all three branches share those data by construction.
