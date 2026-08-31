# Native Enterprise triple-cell discrete curvature code

Status: `FREE_RESEARCH_EXACT_PRESENTATION_EQUIVARIANT_INCIDENCE_CODE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_TRIPLE_CELL_PRIME_INCIDENCE_HEXACODE_20260823.md`

## 1. Ordered incident-cell labels in the forward unit-step presentation

Let `(x,y,z)` be the three integer labels, in the fixed geometric vertex order, of one elementary triple-cell incidence event.

Under the forward monotone side traversal selected in the frozen unit-step allocation:

### A_sigma

`x=n`,

`y=n+3r+sigma`,

`z=n+6r+4+2sigma`.

### B_sigma

`x=n`,

`y=n+3r+1+sigma`,

`z=n+6r+4+2sigma`.

No primality condition is imposed in this file.

## 2. Exact second-difference curvature in one presentation

Define

`K=x-2y+z`.

In the forward presentation:

`K=4` for every A incidence;

`K=2` for every B incidence.

The value is independent of shell `r`, side position `t`, and cyclic sector slot `sigma`.

## 3. Orientation-reversal audit

The current tri-sector allocation is conditionally unique only up to global orientation reversal of the unit-step side traversal.

Under the reverse traversal

`t -> r-1-t`

applied consistently in all three sector blocks, direct recomputation gives:

`K=2` for A,

`K=4` for B.

Therefore the statement

`A=4, B=2`

is **not** an absolute presentation-independent invariant.

The presentation-stable content is:

`{K_A,K_B}={2,4}`.

Define the centered sign

`chi=K-3 in {+1,-1}`.

Then either geometric orientation flip `A<->B` or side-traversal reversal flips `chi`. Thus `chi` is a relative chirality / C2-torsor coordinate between geometric triangle orientation and allocation orientation.

Freeze corrected claim:

`DISCRETE_CURVATURE CHIRALITY = PRESENTATION-EQUIVARIANT, NOT ABSOLUTE`.

## 4. Cyclic slot from the first difference

In the forward presentation let

`D1=y-x`.

Modulo 3:

- for A: `D1 == sigma (mod 3)`;
- for B: `D1 == 1+sigma (mod 3)`.

Thus within the chosen forward presentation the six-state incidence type is recovered exactly from `(K,D1 mod 3)`.

Under global orientation reversal the decoding table is transported accordingly; the abstract six-state package survives, while the named A/B curvature representatives swap.

## 5. Prime hexacode as a quotient shadow

If `x,y,z` are all primes greater than 3, each is `+-1 mod 6`.

Reducing the presentation-equivariant curvature code modulo 2 and 3 forces the six nonconstant mod-6 words found in the incidence-hexacode note.

The exact six-state code therefore survives as an equivariant package even though the absolute assignment of curvature 2 versus 4 to A/B depends on traversal orientation.

## 6. Finite-field normalized curvature plane

For any odd prime `q>=5`, K is invertible. Normalize by

`(X,Y,Z)=K^{-1}(x,y,z) mod q`.

Then both geometric orientations, in either global side-traversal presentation, land on the same affine plane

`X-2Y+Z=1`.

If all three labels avoid q, the local state lies in

`H_q={(X,Y,Z) in (F_q^*)^3 : X-2Y+Z=1}`.

Its exact size is

`q^2-3q+3`.

Thus normalization by the observed curvature precisely quotients the presentation-dependent chirality and leaves one common incidence-state space.

This is why the later 2D-19D incidence CRT tower survives the forward/reverse presentation ablation as an abstract state tower.

## 7. Research significance and boundary

The strongest honest prime-free statement is not an absolute numeric curvature attached to a named triangle orientation. It is the equivariant structure:

`TWO PRIMITIVE INCIDENCE ORIENTATIONS`

`<->`

`TWO CURVATURE REPRESENTATIVES {2,4}`

with reversal swapping them, plus the normalized common plane `H_q`.

No novelty claim is made for finite differences, affine planes, or chirality torsors themselves.

Current verdict:

`DISCRETE_INCIDENCE_CURVATURE = STRONG PRESENTATION-EQUIVARIANT LOCAL STRUCTURE`.

`ABSOLUTE A=4/B=2 CLAIM = REJECTED`.
