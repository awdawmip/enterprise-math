# Native Enterprise filament access basins: exact dimension-2 through dimension-19 table

Status: `FREE_RESEARCH_EXACT_HIGH_DIMENSIONAL_BASIN_TABLE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_ENTERPRISE_FILAMENT_FINITE_QUOTIENT_MULTIPROBE_GCD_ACCESS_20260824.md`;
- `NATIVE_ENTERPRISE_GLOBAL_PRIME_INCIDENCE_TIGHT_PATH_ISLAND_SPECTRUM_3_TO_9_20260823.md`.

## 1. Basin observable

For island size

`k in {3,4,5,6,7,8,9}`

and primorial collapse dimension d, let

`A_d(k,s)`

be the number of size-s coordinate subsets whose projection on the native quotient code `C_k(P_d)` is injective.

Let

`A_d(k)=sum_(s=2)^k A_d(k,s)`

be the total number of information subsets with at least two probes.

## 2. Closed formula for three or more probes

Write

`E=ceil(k/2)`,

`O=floor(k/2)`.

For the realized window lengths k<=9, every probe subset of size at least3 that meets both parity classes has step gcd equal to1 or3.

Both are coprime to every

`P_d/6=5*7*...*p_d`.

Therefore for every `d=2,...,19` and every `s>=3`,

`A_d(k,s)=C(k,s)-C(E,s)-C(O,s)`.

So all high-dimensional changes occur entirely in the two-probe layer.

## 3. Exact two-probe stages

The number of parity-bridging pairs is

`E*O`.

### Dimension 2: P_2=6

Every odd separation is protected:

`A_2(k,2)=E*O`.

### Dimension 3: add channel5

Exactly the pairs at separation5 collapse.  There are

`max(k-5,0)`

such pairs, so

`A_3(k,2)=E*O-max(k-5,0)`.

### Dimension 4: add channel7

The separation7 pairs also collapse:

`A_4(k,2)=E*O-max(k-5,0)-max(k-7,0)`.

### Dimensions 5 through19

Every later channel prime exceeds the largest possible separation8 in a nine-Cell island.  Hence

`A_d(k,2)=A_4(k,2)`

for all `4<=d<=19`.

Thus the complete access basin stabilizes exactly at dimension4.

## 4. Total information-set basin table

The dimension-2 total is the number of subsets meeting both parity classes:

`A_2(k)=2^k-2^E-2^O+1`.

Dimension3 subtracts the bad separation5 pairs, and dimension4 onward also subtracts separation7 pairs.

| island size k | A_2(k) | A_3(k) | A_4(k)=...=A_19(k) |
|---:|---:|---:|---:|
| 3 | 3 | 3 | 3 |
| 4 | 9 | 9 | 9 |
| 5 | 21 | 21 | 21 |
| 6 | 49 | 48 | 48 |
| 7 | 105 | 103 | 103 |
| 8 | 225 | 222 | 221 |
| 9 | 465 | 461 | 459 |

## 5. Two-probe basin table

| island size k | dimension2 | dimension3 | dimensions4--19 |
|---:|---:|---:|---:|
| 3 | 2 | 2 | 2 |
| 4 | 4 | 4 | 4 |
| 5 | 6 | 6 | 6 |
| 6 | 9 | 8 | 8 |
| 7 | 12 | 10 | 10 |
| 8 | 16 | 13 | 12 |
| 9 | 20 | 16 | 14 |

For the sharp nine-Cell code, the protected pair separations evolve as

`{1,3,5,7}`

`-> {1,3,7}`

`-> {1,3}`

and then remain fixed through dimension19.

## 6. Size-resolved stable counts

For every dimension2 through19, the counts for s>=3 are:

### k=9

- size3: 70;
- size4: 120;
- size5: 125;
- size6: 84;
- size7: 36;
- size8: 9;
- size9: 1.

Only the size2 count changes `20 ->16 ->14`.

The same stability holds for every smaller island size according to the binomial formula above.

## 7. Native high-dimensional interpretation

The collapse-channel tower does not progressively destroy all observability.

It acts in three sharp stages:

1. `d=2`: parity bridge established; all odd baselines work;
2. `d=3`: the unique connectivity-break channel5 also kills 5-periodic two-probe geometry;
3. `d=4`: channel7 kills 7-periodic two-probe geometry;
4. `d=5,...,19`: no further change is visible inside a maximal nine-Cell window.

So both topology and information access stabilize at very low collapse dimension:

`CONNECTIVITY STABILIZES AT d=3`,

`NINE-CELL TWO-PROBE ACCESS STABILIZES AT d=4`.

## 8. Boundary

The table is exact for the frozen native filament quotient codes and the sharp global island bound9.  It is not a statistical fit and does not assert a coordinate-independent property of arbitrary prime sets.
