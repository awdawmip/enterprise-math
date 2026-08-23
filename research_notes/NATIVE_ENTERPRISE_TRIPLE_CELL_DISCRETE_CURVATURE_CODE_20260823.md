# Native Enterprise triple-cell discrete curvature code

Status: `FREE_RESEARCH_EXACT_PRIME_FREE_INCIDENCE_INVARIANT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_TRIPLE_CELL_PRIME_INCIDENCE_HEXACODE_20260823.md`

## 1. Ordered incident-cell labels

Let `(x,y,z)` be the three integer labels, in the fixed geometric vertex order, of one elementary triple-cell incidence event.

Using the exact formulas from the two elementary triangle orientations:

### A_sigma

`x=n`,

`y=n+3r+sigma`,

`z=n+6r+4+2sigma`.

### B_sigma

`x=n`,

`y=n+3r+1+sigma`,

`z=n+6r+4+2sigma`.

No primality condition is imposed in this file.

## 2. Exact second-difference curvature

Define the ordered discrete curvature

`K=x-2y+z`.

Then identically:

`K=4` for every A incidence;

`K=2` for every B incidence.

The value is independent of shell `r`, side position `t`, and cyclic sector slot `sigma`.

Freeze:

`TRIPLE_CELL_ORIENTATION = DISCRETE_LABEL_CURVATURE K in {4,2}`.

This converts the two primitive elementary incidence orientations into two parallel arithmetic curvature classes.

## 3. Cyclic slot from the first difference

Let

`D1=y-x`.

Modulo 3:

- for A: `D1 == sigma (mod 3)`;
- for B: `D1 == 1+sigma (mod 3)`.

Therefore the full six-state incidence type is recovered exactly from the ordered integer labels:

1. compute `K=x-2y+z` to recover A versus B;
2. compute `D1 mod 3` to recover `sigma`.

Explicitly:

- if `K=4`, `sigma == y-x mod 3`;
- if `K=2`, `sigma == y-x-1 mod 3`.

Thus

`ORDERED INCIDENT INTEGER LABELS -> (ORIENTATION, C3 SLOT)`

without any primality readout.

## 4. Prime hexacode as a quotient shadow

If `x,y,z` are all primes greater than 3, each is `+-1 mod 6`.

Reducing the prime-free curvature code modulo 2 and 3 forces the six nonconstant mod-6 words found in the incidence-hexacode note.

Hence the mod-6 prime hexacode is not an isolated pattern. It is the prime-support shadow of the stronger integer invariant:

`K in {4,2}` together with `D1 mod 3`.

## 5. Finite-field curvature planes

For any odd prime `q`, reduction modulo q places an incidence triple on one of two affine planes in `F_q^3`:

`A_q: x-2y+z=4`,

`B_q: x-2y+z=2`.

For `q>2` these planes are distinct.

If all three labels avoid q, the allowed local residue states are the points of the corresponding plane inside `(F_q^*)^3`.

For any odd prime q not dividing the curvature constant, the number of such nonzero states is exactly

`q^2-3q+3`.

Proof: choose nonzero `(x,y)`, giving `(q-1)^2` possibilities; `z=0` occurs for exactly `q-2` of them, so the survivor count is `(q-1)^2-(q-2)`.

For q=5 this gives exactly 13 admissible states per orientation.

## 6. Research significance

The invariant is stronger than a prime-density statement:

- it is defined before deciding whether any of the three labels are prime;
- it is selected by native triple-cell incidence rather than an arithmetic-progression grouping;
- it survives across every shell and side position;
- the six-state prime residue code is derived from it rather than fitted to data.

No novelty claim is made for finite differences or affine planes themselves.

The Enterprise-specific candidate is the exact bridge

`PRIMITIVE TRIPLE-CELL INCIDENCE ORIENTATION`

`<->`

`INTEGER SECOND-DIFFERENCE CURVATURE`.

Current verdict:

`DISCRETE_INCIDENCE_CURVATURE = STRONGEST PRIME-FREE LOCAL INVARIANT IN THE NATIVE PRIME-ALLOCATION LANE SO FAR`.
