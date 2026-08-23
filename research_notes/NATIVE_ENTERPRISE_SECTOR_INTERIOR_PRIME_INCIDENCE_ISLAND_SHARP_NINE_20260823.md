# Native Enterprise sector-interior prime-incidence islands：sharp nine-Cell cap

Status: `FREE_RESEARCH_EXACT_EXISTENCE_PLUS_OBSTRUCTION / SECTOR_INTERIOR / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_TRIPLE_CELL_PRIME_INCIDENCE_HEXACODE_20260823.md`

## 1. Scope

This result concerns the **frozen sector-interior triple-cell incidence graph** already used by the hexacode census:

- `1 <= t < r`;
- `sigma in {0,1,2}`;
- two elementary triangle orientations A/B inside each native sector;
- a hyperedge is retained only when all three incident Cell labels are primes.

No claim is made here about additional cross-sector seam incidences that have not yet been separately frozen/audited.

## 2. Mod-6 decomposition by sector slot

For an elementary incidence triangle to contain three primes greater than 3, all three labels must be units modulo 6.

Exact substitution into the incidence formulas gives the following necessary-and-sufficient mod-6 conditions.

### Slot sigma=0

`A0` is mod-6 eligible iff

- `r` even;
- `t == 3*(r/2) mod 6`.

`B0` is eligible iff

- `r` odd;
- `t == 3*((r-1)/2) mod 6`.

Every eligible `A0(r,t)` is paired only with `B0(r+1,t)` through their shared two Cells. No third eligible triangle can continue the component. Hence every sigma=0 component has at most four Cells.

### Slot sigma=2

`A2` is eligible iff

- `r` even;
- `t == 4-r/2 mod 6`.

`B2` is eligible iff

- `r` odd;
- `t == (5-r)/2 mod 6`.

Every eligible `B2(r,t)` is paired only with `A2(r+1,t+1)`. Hence every sigma=2 component has at most four Cells.

### Slot sigma=1

`A1` is eligible iff

- `r` odd;
- `t == (r-3)/2 mod 6`.

`B1` is eligible iff

- `r` even;
- `t == r/2+4 mod 6`.

Both conditions are equivalent to

`h=t-ceil(r/2) == 4 mod 6`.

Thus sigma=1 is the only slot supporting arbitrarily long mod-6 eligible chains.

## 3. Sigma=1 zigzag filament

Fix an integer `h==4 mod6` and define the Cell on shell r by

`t_r=h+ceil(r/2)`,

`C_r=N(r,t_r,1)`.

For odd r the eligible triangle is `A1(r,t_r)`; for even r it is `B1(r,t_r)`. In both cases its three Cells are exactly

`C_r, C_{r+1}, C_{r+2}`.

Hence the entire mod-6 eligible sigma=1 graph is a union of rolling three-Cell windows along constant-h zigzag filaments.

## 4. Mod-5 periodic cut

Write `r=2m` or `2m+1`. Direct substitution gives

- even `r=2m`:
  `C_r = 6m^2+h+1`;
- odd `r=2m+1`:
  `C_r = 6m(m+1)+h+3`.

Modulo 5 the sequence is periodic with period 10 in r. For each `h mod5`, one period is:

| h mod5 | `C_0,...,C_9 mod5` | longest cyclic nonzero run |
|---|---|---:|
| 0 | `1,3,2,0,0,4,0,0,2,3` | 5 |
| 1 | `2,4,3,1,1,0,1,1,3,4` | 9 |
| 2 | `3,0,4,2,2,1,2,2,4,0` | 7 |
| 3 | `4,1,0,3,3,2,3,3,0,1` | 5 |
| 4 | `0,2,1,4,4,3,4,4,1,2` | 9 |

A run of L consecutive mod-30 unit Cells on a sigma=1 filament gives one connected eligibility component of L Cells whenever `L>=3`, because the active hyperedges are the rolling triples.

Therefore every mod-30 eligible sigma=1 component has at most 9 Cells.

Since every prime greater than 5 is a unit modulo 30, every nonexceptional prime-incidence component in the frozen sector-interior graph has at most 9 Cells.

Together with the sigma=0/2 four-Cell bound:

`SECTOR_INTERIOR PRIME-INCIDENCE COMPONENT SIZE <= 9`.

## 5. Sharpness: an explicit nine-prime island

The previously frozen sharp maximal-prime filament with

`h=-2474`

contains the nine prime Cell labels

`171283421,`

`171315481,`

`171347543,`

`171379609,`

`171411677,`

`171443749,`

`171475823,`

`171507901,`

`171539981`.

Their native shell-fiber coordinates are

- `(10686,2869,1)`;
- `(10687,2870,1)`;
- `(10688,2870,1)`;
- `(10689,2871,1)`;
- `(10690,2871,1)`;
- `(10691,2872,1)`;
- `(10692,2872,1)`;
- `(10693,2873,1)`;
- `(10694,2873,1)`.

The seven consecutive incidence hyperedges are

`B1@10686, A1@10687, B1@10688, A1@10689, B1@10690, A1@10691, B1@10692`,

each joining three consecutive primes in the list.

The immediately adjacent same-filament Cells are

- `C_10685 = 171251365`, divisible by 5;
- `C_10695 = 171572065`, divisible by 5.

Thus the mod-30 eligibility component is closed at both ends, and because the nine displayed Cells are all prime, they form an actual prime-incidence connected component of size 9.

The nine primalities were independently checked in the sharp-filament packet by direct trial division through square roots.

Hence the bound is sharp:

`MAX SECTOR-INTERIOR PRIME-INCIDENCE ISLAND SIZE = 9`.

## 6. Interpretation

The 2D native prime skeleton does not percolate through the frozen sector-interior incidence graph. Mod 6 first collapses the geometry into short diamonds in slots 0/2 and one-dimensional sigma=1 zigzag channels; mod 5 then cuts every long channel after at most nine eligible Cells.

This is stronger than a finite-density observation: the finite island cap is a local congruence consequence of the native incidence allocation.

## 7. Boundary / next gate

This note deliberately does not claim a full-plane theorem across sector seams. The next gate is to determine whether the current native foundation fixes seam triple-cell incidences strongly enough to audit their effect on connectivity. If seam incidence is not uniquely determined by current canonical chart gluing, the sharp-nine theorem remains correctly scoped to the frozen sector-interior graph.
