# Native Enterprise triple-prime incidence：minimal prime-valued local self-localization

Status: `FREE_RESEARCH_EXACT_PRIME_VALUED_LOCALIZATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_TRIPLE_CELL_DISCRETE_CURVATURE_CODE_20260823.md`

## 1. Ordered incidence triple

Let `(x,y,z)` be the integer labels of the three Cells meeting at one elementary coordinate vertex, in the fixed local geometric order used by the incidence formulas.

The two primitive incidence orientations satisfy

### A_sigma

`y-x = 3r+sigma`,

`x-2y+z = 4`.

### B_sigma

`y-x = 3r+1+sigma`,

`x-2y+z = 2`.

## 2. Decode orientation without external type information

Compute

`K=x-2y+z`.

Then `K` is exactly `4` or `2`.

Define

`delta=(4-K)/2`.

Thus

- `delta=0` for A;
- `delta=1` for B.

No prime test is required for this decode.

## 3. Decode shell and C3 slot

Set

`u=y-x-delta`.

In both incidence orientations,

`u=3r+sigma`.

Therefore

`sigma = u mod 3`,

`r=(u-sigma)/3`.

So the shell index and cyclic slot are recovered linearly from one local incidence triple, with no global shell search.

## 4. Decode side coordinate

With

`B_r=1+3r(r-1)/2`,

the first label `x` is the center label

`x=B_r+t+sigma*r`.

Hence

`t=x-B_r-sigma*r`.

Thus

`(x,y,z) -> (r,t,sigma)`

is exact on every valid ordered triple-cell incidence event.

The canonical Enterprise address follows from the usual inverse sector chart.

## 5. Prime-valued specialization

If all three labels are primes, the same formulas use only the three prime values themselves.

Therefore a fully-bright triple-cell coordinate vertex is self-localizing:

`THREE INCIDENT PRIME VALUES -> NATIVE SHELL-FIBER COORDINATE`.

The earlier mod-6 hexacode is only the coarse low-modulus shadow:

- ordered residues mod 6 recover local incidence type;
- actual prime differences recover shell scale and exact position.

This is the minimal prime-valued localization object currently identified in the native lane.

## 6. Relation to the five-prime flower

The maximal five-prime flower remains a stronger multi-vertex packet: its sorted values recover shell scale without choosing one elementary triangle and organize into constant-h filaments.

However it is not the first non-Boolean prime-valued readout. That priority belongs to the triple-prime incidence self-localizer in this note.

## 7. Boundary

The formulas are exact consequences of the frozen integer allocation and primitive triple-cell incidence geometry. They do not constitute a new theorem about primes in isolation.

Current classification:

`TRIPLE_PRIME_INCIDENCE_SELF_LOCALIZATION = MINIMAL PRIME-VALUED NATIVE LOCALIZER SO FAR`.
