# Native Enterprise tri-sector integer allocation：typed-Cell lift and affine-shell correction

Status: `FREE_RESEARCH_FOUNDATION_ALIGNMENT_CORRECTION / EXACT_REINTERPRETATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 1. Why a typed lift is required

The canonical native line definition distinguishes coordinate vertices from circle cells and freezes three sector-local affine Cell charts

`C_12(a,b)`, `C_23(b,c)`, `C_31(a,c)`

with nonnegative local coordinates. In particular, the three cells `C_ij(0,0)` are the distinct anchor cells incident to the native origin.

Axis line identities glue globally, while chart-local Cell trajectories on the two sides of a shared axis remain distinct realizations.

Therefore the most faithful prime-allocation carrier is the **typed Cell chart**, not a naive deduplication of all axis-adjacent cells into one global min-zero vertex address.

## 2. Typed Cell shells

Use sector slot

- `sigma=0` for `C_12(a,b)`;
- `sigma=1` for `C_23(b,c)`;
- `sigma=2` for `C_31(a,c)`.

Define the local Cell-trace shell sum `s` and side coordinate `t` by

- sigma 0: `s=a+b`, `t=b`;
- sigma 1: `s=b+c`, `t=c`;
- sigma 2: `s=a+c`, `t=a`.

For every `s>=0`, each sector contributes exactly `s+1` typed cells. Hence the complete typed Cell shell contains

`3(s+1)`

cells.

At `s=0` these are exactly the three distinct origin-anchor cells.

## 3. Gap-free typed Cell allocation

Allocate positive integers shell by shell, with the three sector blocks kept C3-equivariant and unit-step ordered inside each block.

The first integer on typed shell s is

`B^C_s = 1 + sum_{j=0}^{s-1} 3(j+1)`

so

`B^C_s = 1 + 3s(s+1)/2`.

The typed Cell label is therefore

`N_C(s,t,sigma)=1+3s(s+1)/2+t+sigma*(s+1)`

for

`0<=t<=s`, `sigma in {0,1,2}`.

This enumerates every positive integer exactly once across all typed Cell charts.

## 4. Exact equivalence with the existing experimental formula

All previous native prime-allocation experiments used

`N(r,t,sigma)=1+3r(r-1)/2+t+sigma*r`

with `r>=1`, `0<=t<r`.

Set

`r=s+1`.

Then identically

`N(r,t,sigma)=N_C(s,t,sigma)`.

Therefore **no prime data or arithmetic formula changes**. The correction is semantic/typed:

`LEGACY EXPERIMENTAL r = TYPED CELL TRACE SHELL s + 1`.

The old r-th layer of `3r` labels is exactly the canonical typed Cell shell `s=r-1` of `3(s+1)` distinct Cell states.

## 5. Elementary incidence formulas survive exactly

Inside one typed sector, an orientation-A elementary center triangle is

`(a,b)`, `(a+1,b)`, `(a+1,b+1)`;

orientation B is

`(a,b)`, `(a,b+1)`, `(a+1,b+1)`.

Under `r=s+1`, these translate exactly into the already-frozen experimental shell triples

- A: `(r,t)`, `(r+1,t)`, `(r+2,t+1)`;
- B: `(r,t)`, `(r+1,t+1)`, `(r+2,t+1)`.

Hence the incidence-label formulas, discrete curvature, hexacode, loop code, five-prime flowers, filaments, and sharp-nine island calculations remain numerically unchanged.

## 6. Interpretation correction

The research lane should henceforth distinguish:

- `VADDR`: native coordinate/triple-intersection vertex address;
- `CADDR`: typed sector-local affine Cell address;
- `s`: typed Cell component-trace shell sum;
- `r=s+1`: the enumeration-layer size used by the existing prime tables.

Do not identify the Cell center with the coordinate vertex carrying the same local integer pair.

Freeze for this research lane:

`PRIME ALLOCATION CARRIER = TYPED CIRCLE-CELL STATES`.

`EXISTING INTEGER DATA = PRESERVED UNDER r=s+1`.

## 7. Boundary

This is a correction of the research interpretation, not a modification of canonical Enterprise foundation. The canonical source continues to control typed vertex/Cell semantics.
