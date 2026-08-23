# Native Enterprise sharp nine-Cell islands：mod-5 tangency and the two chiral residue packets

Status: `FREE_RESEARCH_EXACT_EXTREMAL_CODE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_GLOBAL_TYPED_CELL_PRIME_INCIDENCE_ISLAND_SHARP_NINE_20260823.md`

## 1. Long-filament formulas modulo 5

On the only long mod-6 eligible sigma-1 filament,

`h=t-ceil(r/2)==4 mod6`.

Writing `r=2m` or `2m+1`, the Cell labels reduce modulo 5 to

`C_{2m}=m^2+h+1`,

`C_{2m+1}=m(m+1)+h+3`.

A sharp nine-Cell mod-30 eligibility island requires a period-10 sequence with exactly one zero modulo 5, leaving the other nine consecutive positions nonzero.

## 2. Even-branch tangency

For the even branch,

`m^2+h+1=0 mod5`.

Exactly one m-root occurs only when the quadratic has the double root `m=0`, namely

`h=-1=4 mod5`.

For this h the odd branch has no root modulo 5.

Therefore the unique zero occurs at

`r=0 mod10`,

and the sharp nine-run starts at

`r=1 mod10`.

Combining with `h=4 mod6` gives

`h=4 mod30`.

## 3. Odd-branch tangency

For the odd branch,

`m(m+1)+h+3=0 mod5`.

Its discriminant is zero exactly for

`h=1 mod5`.

Then there is one double root `m=2 mod5`, hence one zero at

`r=5 mod10`.

The even branch has no root for this h.

So the sharp nine-run starts at

`r=6 mod10`.

Combining with `h=4 mod6` gives

`h=16 mod30`.

## 4. Exactly two sharp local channels

Thus a nine-Cell mod-30 eligibility island can occur only in the two channels

- `(r_start mod10,h mod30)=(1,4)`;
- `(r_start mod10,h mod30)=(6,16)`.

These are precisely the two local channels previously found from the length-five maximal-flower capacity calculation.

The extremal component is therefore selected by a double-root/tangency condition, not by an arbitrary high local density.

## 5. Two forced mod-30 residue words

Substituting the two channels into the nine consecutive Cell labels gives the exact residue packets:

### Odd-start / h=4 mod30

`(7,11,19,29,13,29,19,11,7) mod30`.

### Even-start / h=16 mod30

`(11,1,23,19,17,19,23,1,11) mod30`.

Both are palindromic.

Their reductions modulo 6 are the two alternating chiral words

`(1,5,1,5,1,5,1,5,1)`

and

`(5,1,5,1,5,1,5,1,5)`.

Therefore the sharp nine-Cell local code has exactly two chiral residue packets.

## 6. Realization

The two explicit sharp prime filaments already frozen in the branch realize both packets:

- odd-start packet: `r_start=107811`, `h=7624`, `h mod30=4`;
- even-start packet: `r_start=10686`, `h=-2474`, `h mod30=16`.

All 18 displayed Cell values across the two packets are prime as independently checked in the corresponding sharp-filament records.

## 7. Interpretation

The maximum island size 9 is achieved exactly when the mod-5 divisibility locus is touched with multiplicity two in one parity branch and completely missed by the other branch.

Thus the two extremal prime-incidence chiralities are the arithmetic shadows of the two possible mod-5 tangencies.
