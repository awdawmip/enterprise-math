# Enterprise C3 equal-coordinate bouquet：simultaneous-prime 105 gate

Status: `FREE_RESEARCH_EXACT_SIEVE_OBSERVATION / COMPUTATIONAL_SCALE_CHECK / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_BISECTOR_PRIME_BOUQUET_20260823.md`

## 1. Bouquet

`F_-(m)=6m^2-2m+1`

`F_0(m)=6m^2+1`

`F_+(m)=6m^2+2m+1`

and

`P(m)=F_-(m)F_0(m)F_+(m)`.

Expanded:

`P(m)=216m^6+84m^4+14m^2+1`.

## 2. Exact small-prime gate

Modulo 3, the root sets of the three lanes are:

- `F_-`: `{2}`;
- `F_0`: empty;
- `F_+`: `{1}`.

Thus every nonzero residue mod 3 is killed by one lane.

Modulo 5:

- `F_-`: `{1}`;
- `F_0`: `{2,3}`;
- `F_+`: `{4}`.

Thus every nonzero residue mod 5 is killed by one lane.

Modulo 7:

- `F_-`: `{2,3}`;
- `F_0`: `{1,6}`;
- `F_+`: `{4,5}`.

Thus every nonzero residue mod 7 is killed by one lane.

Equivalently the product factors as follows in the corresponding residue rings:

`P(m) mod 3 = -(m-1)(m+1)`;

`P(m) mod 5 = (m-2)(m-1)^2(m+1)^2(m+2)`;

`P(m) mod 7 = -(m-3)(m-2)(m-1)(m+1)(m+2)(m+3)`.

Therefore, once all three polynomial values exceed 7, simultaneous primality implies

`m = 0 mod 3`,

`m = 0 mod 5`,

`m = 0 mod 7`.

Hence

`SIMULTANEOUS_BOUQUET_PRIME => 105 | m`.

This is an exact sieve statement, not a statistical fit.

## 3. Finite experiments

For `m<=5000`, simultaneous-prime events occur at exactly:

- `m=315`:
  - `594721`, `595351`, `595981`;
- `m=3045`:
  - `55626061`, `55632151`, `55638241`;
- `m=4515`:
  - `122302321`, `122311351`, `122320381`.

All are multiples of 105 as required.

Search extended to `m<=1,000,000` by checking only multiples of 105:

- surviving 105-multiples checked: `9523`;
- simultaneous-prime events found: `58`.

The first few `m` values are:

`315, 3045, 4515, 14070, 32025, 45045, 45465, 46095, 95130, 96915, 97020, 97335, 99435, ...`

This finite count does not imply an infinitude theorem.

## 4. Structural interpretation

The equal-coordinate C3 bouquet is not merely three similar prime-rich rays.  The three lanes cooperate as a local wheel sieve:

- mod 3, the two outer lanes eliminate the two nonzero residues;
- mod 5, the three lanes partition all four nonzero residues;
- mod 7, the three lanes partition all six nonzero residues.

Therefore the three-sector coordinate symmetry generates a very compact simultaneous-prime admissibility gate:

`m -> 105k`.

This is currently the strongest exact arithmetic structure extracted from the native tri-sector allocation.

## 5. Boundary

The underlying polynomial-prime / prime-tuple questions are classical number-theory territory.  No novelty claim is made for the general sieve principle or for polynomial prime tuples.

The Enterprise-specific research object is the provenance:

`equal-coordinate loci in the three positive-axis atlas`

`-> symmetric quadratic bouquet`

`-> exact 3*5*7 gate for simultaneous bright states`.

## 6. Next

1. classify the full local root-union profile for all primes q;
2. derive the exact wheel after 3,5,7 and measure additional compression from 11,23,29,...;
3. compare pairwise-prime events and semiprime events;
4. test whether the 105 gate has a native collapse interpretation rather than merely a polynomial-sieve interpretation;
5. only after that consider lifting the C3 bouquet into a native high-dimensional collapse construction.
