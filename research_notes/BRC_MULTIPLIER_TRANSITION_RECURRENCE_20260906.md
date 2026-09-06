# BRC Consecutive-Multiplier Root Transition — Round 5

Status: `PROVED DERIVED RECURRENCE / STATIC FAST PATH + DYNAMIC FALLBACK / FINITE PERFORMANCE BENCHMARK / NO ASYMPTOTIC FACTORIZATION CLAIM`
Date: `2026-09-06`
Parent: `t0.brc_multiplier_basin`
Composition: `t0.brc_square_gap_prefilter`

## Question

For fixed positive N, can the retained BRC root state

`mN = J_m^2 + R_m`, `0<=R_m<=2J_m`

be advanced from multiplier m to m+1 without materializing
`floor(sqrt((m+1)N))` again?

**Yes.** One dyadic predictor plus at most two exact BRC basin crossings is
enough.

## The transition theorem

Set

`beta_m=sqrt((m+1)/m)`, `gamma_m=beta_m-1`.

Choose B with `J_m<2^(B-1)`. Let

`C_m=floor(2^B gamma_m)`,
`d0=floor(C_m J_m / 2^B)`.

Because `J_m/2^B<1/2`,

`d0 <= gamma_m J_m < d0+3/2`.

Write `sqrt(mN)=J_m+delta`, `0<=delta<1`. Since
`beta_m<=sqrt(2)`,

`sqrt((m+1)N)`
`=J_m+gamma_m J_m+beta_m delta`
lies in

`[J_m+d0, J_m+d0+3)`.

Therefore

`J_(m+1)-(J_m+d0) in {0,1,2}`.

This gives the proved **two-correction bound**.

## Root-free remainder update

Put `a0=J_m+d0`. From `mN=J_m^2+R_m`,

`G0=(m+1)N-a0^2`
`=R_m+N-d0(2J_m+d0)`.

Starting at `(a,G)=(a0,G0)`, while `G>=2a+1` perform

`G <- G-(2a+1)`,
`a <- a+1`.

At most two iterations occur. On exit,

`a=J_(m+1)`, `G=R_(m+1)`.

After the initial m=1 root, no new N-dependent integer root is required.

## Predictor table

One checked-in high-precision table covers the common static fast path

`bit_length(N)<=4096`, `m<=100`.

It stores 99 constants at `B_max=2053` with raw payload

`25443 bytes` (~24.8 KiB),

SHA-256

`b434d3be1f2c6a8f6a32276e7fa4660fd554969d5f32021e3e5c0504633c1003`.

For smaller N, runtime obtains the exact lower-precision constant simply by
right shift. This avoids multiplying a 4096-bit-N scan by unnecessarily wide
constants.

For `N>4096` bits the same theorem remains valid; the reference implementation
builds the 99 constants once by exact integer arithmetic and caches them. That
fallback is functional but not included in the static-path performance claims.

## Why this is genuinely BRC-relevant

The recurrence uses the retained pair `(J_m,R_m)` directly. If R_m had been
discarded by a root-only collapse, `G0` cannot be reconstructed. Thus the
previous observer-loss warning becomes constructive:

`ROOT_ONLY -> NOT MULTIPLIER-TRANSITION COMPLETE`

while

`(ROOT,REMAINDER,m) -> EXACT NEXT STATE`.

The local correction is literally subtraction of the next square-basin widths
`2J+1`.

## Validation

Derivation checks covered random 16..8192-bit values. Repository regression
adds:

- exact static-table regeneration and SHA-256 check;
- exact dyadic precision downshift;
- dynamic fallback check above 4096 bits;
- exhaustive N=1..499, m=1..100;
- random 128..8192-bit equivalence to direct roots;
- proof-bound assertion `correction_steps<=2`;
- exact ceiling-gap reconstruction.

Observed mean correction count in the static timing population was about
0.59..0.62 per transition; maximum was 2.

## Performance with the 504-byte gap filter

Full m=1..100 pipeline:

1. direct: fresh multiplier root + fresh gap root every m;
2. residue: fresh multiplier root + mod-4032 prefilter;
3. transition+residue: one initial multiplier root + 99 BRC transitions +
   mod-4032 prefilter.

Current-environment medians:

| N bits | residue speedup | transition+residue speedup |
|---:|---:|---:|
| 128 | 1.10x | 1.17x |
| 256 | 1.27x | 1.65x |
| 512 | 1.34x | 1.98x |
| 1024 | 1.41x | 2.12x |
| 2048 | 1.42x | 2.11x |
| 4096 | 1.45x | 1.91x |

A separate small-integer probe showed the recurrence loses below roughly the
100-bit scale in this Python environment. This is therefore a large-integer
scan optimization.

These are finite implementation timings, not an asymptotic factorization
result.

## Strategic consequence

The repeated multiplier root is no longer the dominant unavoidable primitive
for m=1..100. The pipeline can now be

`one root at m=1`
`-> exact root/remainder transport`
`-> ceiling gap from R_m`
`-> 504-byte residue lookup`
`-> exact gap root only for survivors`.

The next attack should target multiplier ordering / early-hit probability or
batch many N values, not spend more effort optimizing repeated sqrt(mN).

## Boundaries

- Exact finite integer theorem; no floating state.
- Static performance claim only through 4096-bit N and m<=100.
- Dynamic cached predictor fallback above 4096 bits is functional but is not
  claimed faster for a one-off N.
- Difference-of-squares factoring remains classical multiplier-Fermat/Lehman
  prior art.
- No asymptotic factorization speedup and no Foundation promotion.
