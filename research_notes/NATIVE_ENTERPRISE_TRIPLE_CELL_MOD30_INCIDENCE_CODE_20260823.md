# Native Enterprise triple-cell mod-30 incidence code

Status: `FREE_RESEARCH_EXACT_LOCAL_CODE / FINITE_DISTRIBUTION_CENSUS / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parents:

- `NATIVE_ENTERPRISE_TRIPLE_CELL_PRIME_INCIDENCE_HEXACODE_20260823.md`;
- `NATIVE_ENTERPRISE_TRIPLE_CELL_DISCRETE_CURVATURE_CODE_20260823.md`.

## 1. CRT split of prime residues mod 30

A prime greater than 5 lies in

`U(30)={1,7,11,13,17,19,23,29}`.

Via CRT, its mod-30 state consists of:

- the fixed mod-6 sign bit `+-1`;
- one nonzero mod-5 residue.

For a fully-prime triple-cell incidence event, the mod-6 part already determines one of the six incidence hexacode words.

The new mod-5 part is constrained by the exact curvature plane

`x-2y+z=kappa`,

with

- `kappa=4` for orientation A;
- `kappa=2` for orientation B.

The three cyclic sector slots share the same mod-5 curvature plane inside each orientation; their distinction remains in the mod-6 word.

## 2. Exactly 13 mod-5 states per incidence type

For q=5, a fixed nonzero curvature plane contains exactly

`5^2-3*5+3=13`

points in `(F_5^*)^3`.

Therefore each of the six incidence types admits exactly 13 prime-compatible mod-30 residue triples.

Since the six mod-6 words are disjoint, the complete mod-30 incidence code has exactly

`6*13=78`

states.

By comparison, arbitrary ordered triples of primes greater than 5 have

`phi(30)^3=8^3=512`

possible mod-30 unit words.

Thus primitive triple-cell incidence restricts the prime residue word to a 78-state subset before any statistical prime-density question is asked.

## 3. Exact code description

A mod-30 word `(x,y,z)` belongs to incidence type `(O,sigma)` exactly when:

1. all three coordinates are units mod 30;
2. its reduction mod 6 is the unique hexacode word for `(O,sigma)`;
3. `x-2y+z == 4 mod 5` for A, or `==2 mod 5` for B.

These conditions generate all 78 states exactly.

## 4. Finite occupancy at r<=3000

In the frozen interior triple-prime census through shell 3000, every one of the 13 allowed mod-30 states occurs for every incidence type.

Within-type counts across the 13 states have population CV:

- A0: `0.06060`;
- A1: `0.05079`;
- A2: `0.04457`;
- B0: `0.07453`;
- B1: `0.05513`;
- B2: `0.07088`.

So at this scale the full-prime events broadly fill the exact local code rather than concentrating on a single mod-30 state.

This near-balance is only a finite diagnostic; the 78-state restriction is exact.

## 5. Orientation homothety

Modulo any odd prime q, the two curvature planes

`L=4` and `L=2`, where `L(x,y,z)=x-2y+z`,

are scalar-homothetic: multiplying an A-plane state by `2^{-1}` sends it to the B plane.

Thus after quotienting global nonzero scalar presentation, the two orientations have the same projective incidence-state space; the orientation information resides in the absolute curvature normalization before this quotient.

This cleanly distinguishes:

- **integer/native orientation readout**: curvature 4 versus 2;
- **projectivized local state shape**: one common punctured curvature-plane geometry.

## 6. General q-channel

For every odd prime q not dividing the curvature constant, one orientation has exactly

`q^2-3q+3`

q-admissible nonzero residue states.

This suggests a richer incidence-channel tower than the earlier one-dimensional shell-residue CRT tower: each new q-channel carries a punctured two-parameter curvature-plane state rather than only one unit residue.

This is a research direction, not yet a promoted high-dimensional definition.

## 7. Verdict

`MOD30_INCIDENCE_CODE = 78 EXACT STATES`.

`NO_SINGLE PRIME-RICH RESIDUE STATE IS SELECTED AT THIS LEVEL`.

The next discriminating construction is to normalize curvature and test a CRT product of these incidence-state planes across primes, with downward collapse defined by forgetting one local incidence channel.
