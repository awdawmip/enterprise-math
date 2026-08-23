# Native Enterprise long filament: universal fourth-order recurrence and characteristic-mode decomposition

Status: `FREE_RESEARCH_EXACT_PRIME_FREE_VALUE_DYNAMICS / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_MAXIMAL_PRIME_FILAMENT_SHARP_LENGTH_FIVE_20260823.md`;
- `NATIVE_ENTERPRISE_SHARP_NINE_ENDPOINT_HOLOGRAPHY_AND_DUAL_TANGENT_SIEVE_20260823.md`.

## 1. Prime-free filament sequence

On the long sigma-1 typed filament with fixed transverse coordinate h, the integer label at shell r is

`C_r(h)=h+3*r^2/2+1+(1-(-1)^r)/4`.

This identity is defined before primality is tested.

Hence every consecutive long-filament value sequence is the sum of

1. a quadratic polynomial in r;
2. one alternating parity term.

## 2. Homogeneous universal recurrence

The quadratic part is annihilated by `(E-1)^3`; the alternating part is annihilated by `(E+1)`.

Therefore the full sequence is annihilated by

`(E-1)^3(E+1)=E^4-2E^3+2E-1`.

Equivalently, for every four-step window,

`C_{r+4}-2*C_{r+3}+2*C_{r+1}-C_r=0`.

Thus any prime-incidence filament realization satisfies the same homogeneous recurrence on its prime values:

`p_{i+4}-2*p_{i+3}+2*p_{i+1}-p_i=0`.

No prime hypothesis is needed for the recurrence itself; primality selects finite windows of this universal native integer dynamics.

## 3. Curvature oscillator

Define the local second difference

`K_i=p_i-2*p_{i+1}+p_{i+2}`.

For a filament starting with chirality chi,

`K_i=3-chi*(-1)^i`.

Hence

`K_i in {2,4}`,

`K_i+K_{i+1}=6`.

After centering

`kappa_i=K_i-3`,

we have the exact two-state law

`kappa_{i+1}=-kappa_i`,

so `kappa_i in {+1,-1}`.

The unique non-polynomial mode is therefore one alternating C2 chirality bit.

## 4. Characteristic decomposition

The characteristic polynomial is

`(lambda-1)^3(lambda+1)`.

Thus the value dynamics decomposes algebraically into

- a three-dimensional generalized lambda=1 sector, generating constant/linear/quadratic drift;
- a one-dimensional lambda=-1 sector, generating parity chirality.

For the frozen allocation the quadratic coefficient is fixed to `3/2`, so an individual geometric filament still has only the native placement parameters rather than four free recurrence coefficients.

## 5. Relation to curvature flattening

For a sharp-nine window centered at j=0, removing

`(3/2)j^2 + (chi/2)*1_{j odd}`

leaves an affine line.

The fourth-order recurrence is the translation-invariant version of the same statement: it detects the entire quadratic-plus-alternating family without choosing a center.

## 6. Orientation reversal

Reversing the order of a filament changes `i -> -i` and flips the presentation chirality, but the recurrence equation is invariant because its coefficient polynomial is reciprocal up to an overall sign.

Therefore the zero-recurrence relation itself is orientation-stable even though the sign of the centered curvature mode is presentation-equivariant.

## 7. Research interpretation

The long native filament carries a very small exact value dynamics:

`QUADRATIC SHELL DRIFT + ONE C2 CHIRALITY MODE`.

Sharp prime islands are finite prime-valued realizations of this pre-existing geometry-generated sequence, not arbitrary prime strings fitted after the fact.

No claim is made that the recurrence theory itself is new; the research-specific object is its derivation from the native typed-Cell incidence allocation and its role in the exact prime-island endpoint code.
