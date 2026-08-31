# Native Enterprise triple-cell prime incidence hexacode

Status: `FREE_RESEARCH_EXACT_INCIDENCE_CODE / FINITE_CENSUS / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent direction: native triple-cell incidence fold after the CRT/local-sieve null comparison.

## 1. Why this fold is different

The earlier C3 fold grouped three sector slots carrying the same side coordinate. That produced an arithmetic progression and was therefore strongly exposed to classical prime-tuple sieve structure.

The present fold is selected instead by a primitive fact of the current Enterprise plane:

- cell centers form the gap-free triangular carrier with nearest-center spacing 1;
- every elementary unit center triangle has exactly one common triple boundary-intersection point;
- coordinate vertices are incidence events among three circle cells, not simultaneous native cell states.

This construction uses the triangular carrier only to determine **which three cells are incident to one coordinate vertex**. It does not use carrier Euclidean length as the native Enterprise metric.

## 2. Two elementary incidence orientations

Work first in sector S12 and write a cell-center address as `(a,b,0)` with `a,b>=1` for the interior census. Let

`r=a+b`, `t=b`.

The two elementary center triangles incident to the diagonal neighbor `(a+1,b+1,0)` are:

- orientation A: `(a,b,0)`, `(a+1,b,0)`, `(a+1,b+1,0)`;
- orientation B: `(a,b,0)`, `(a,b+1,0)`, `(a+1,b+1,0)`.

Cyclic relabeling gives the corresponding two orientations in each of the three native sectors. Thus the local incidence type is

`(orientation, sigma) in {A,B} x C3`,

with exactly six types.

## 3. Integer labels of an incidence triple

Under the frozen tri-sector integer allocation, let

`n=N(r,t,sigma)=B_r+t+sigma*r`,

`B_r=3r(r-1)/2+1`.

Then direct substitution into the shell-coordinate map gives:

### A_sigma

`I_A(r,t,sigma) =`

`( n, n+3r+sigma, n+6r+4+2sigma )`.

### B_sigma

`I_B(r,t,sigma) =`

`( n, n+3r+1+sigma, n+6r+4+2sigma )`.

These formulas are exact consequences of the address allocation and the elementary incidence relation.

## 4. Exact mod-6 incidence code

Assume all three labels in an incidence triple are primes greater than 3. Each residue is therefore in `{1,5} mod 6`.

Parity and mod-3 constraints force one and only one residue word for each of the six incidence types:

| incidence type | ordered prime residues mod 6 |
|---|---|
| A0 | `(1,1,5)` |
| A1 | `(1,5,1)` |
| A2 | `(5,1,1)` |
| B0 | `(1,5,5)` |
| B1 | `(5,1,5)` |
| B2 | `(5,5,1)` |

Thus the six local incidence types are in bijection with the six nonconstant binary words in `{1,5}^3`.

The two constant words

`(1,1,1)` and `(5,5,5)`

cannot occur for a nonexceptional fully-prime triple-cell incidence event.

Freeze:

`TRIPLE_CELL_FULL_PRIME_INCIDENCE -> SIX_NONCONSTANT_MOD6_WORDS`.

## 5. Bidirectional decoder

Map residues to signs by

`1 -> +1`, `5 -> -1`.

For a fully-prime incidence triple, let `(eps_0,eps_1,eps_2)` be the sign word.

Then:

`eps_0*eps_1*eps_2 = -1` iff the incidence orientation is A;

`eps_0*eps_1*eps_2 = +1` iff the incidence orientation is B.

Moreover:

- in orientation A, the unique `-1` occurs at position `2-sigma mod 3`;
- in orientation B, the unique `+1` occurs at position `sigma`.

Hence the ordered mod-6 residue word recovers the complete local incidence label `(orientation,sigma)`.

Conversely, `(orientation,sigma)` determines the residue word exactly.

Therefore:

`ORDERED PRIME RESIDUES MOD 6 <-> LOCAL TRIPLE-CELL INCIDENCE TYPE`.

This is an exact readout, not a statistical classifier.

## 6. C3 x C2 symmetry

Cyclic sector rotation permutes the three A codewords by moving the unique `5`, and permutes the three B codewords by moving the unique `1`.

Changing elementary triangle orientation `A <-> B` complements all three bits:

`1 <-> 5`.

Thus the six codewords form one natural `C3 x C2` incidence package.

The geometry and the arithmetic code carry the same six-state action.

## 7. Exact finite census

Interior census:

- shells `2 <= r <= 3000`;
- side positions `1 <= t < r`;
- all three sector slots;
- both elementary orientations;
- primality decided only after the incidence triple is fixed.

Fully-prime counts:

- `A0 = 2859`;
- `A1 = 2870`;
- `A2 = 2910`;
- `B0 = 2987`;
- `B1 = 2933`;
- `B2 = 2845`.

Mean count: `2900.666666...`.

Population coefficient of variation across the six incidence types:

`CV ~= 0.01686646`.

Every fully-prime triple with all labels greater than 3 obeyed its predicted mod-6 codeword; violations: `0`.

Representative first interior events include:

- `B2`: `(17,29,43)` -> `(5,5,1) mod 6`;
- `A2`: `(29,43,61)` -> `(5,1,1)`;
- `A1`: `(37,53,73)` -> `(1,5,1)`;
- `B0`: `(67,89,113)` -> `(1,5,5)`.

The near-balance of the six finite counts is only a diagnostic. The exact result is the six-word incidence code and its bidirectional decoder.

## 8. Why this survives the previous negative result

The earlier AP/CRT statistics were quantitatively explained by classical Hardy-Littlewood local sieve data. Here the grouping itself is not selected by a common arithmetic-progression offset set; it is selected by the primitive triple-cell incidence of the native carrier.

The mod-6 constraints are still elementary classical congruence arithmetic, so no novelty claim is made for the congruence facts in isolation.

The research-specific candidate is the exact correspondence

`NATIVE THREE-CELL COORDINATE-VERTEX TYPE`

`<->`

`NONCONSTANT THREE-BIT PRIME RESIDUE WORD`.

## 9. Current verdict and next discriminating test

`TRIPLE_CELL_PRIME_INCIDENCE_HEXACODE = STRONG_NATIVE_LOCAL_PATTERN_CANDIDATE`.

Next:

1. lift the six exact mod-6 words to mod 30 and classify the remaining local-state orbits;
2. test whether the mod-5 refinement carries more information about incidence than a matched local congruence null predicts;
3. classify presentation/orientation invariance of the code without using a Euclidean metric;
4. only then consider using incidence vertices as the primitive units of a higher-dimensional collapse tower.
