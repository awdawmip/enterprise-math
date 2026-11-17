# R261 — exact 13-adic depth profile of 63 labelled scalar observers

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_MODULAR_COMPUTATION / NOT_REVIEWED**.
Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent verified science: R260 and R260A at `enterprise-math@6bbb4062b54094d2fdea30df1d31891659d9fdb1`.

## Question and exact domain

For the *auxiliary positive rational* seven-source model of R258, set
`s=866/2197`, `J=3327364117`, `T=3975468120`, `K=36933000`, and
`q_(m,k)=JT^k h_(m,k)/K` for original labelled masks `m=0,...,62`,
`k>=3`. The prior exact integer recurrence has order
`d_m=1+popcount(m)`; `sum_m d_m=249`.

For a fixed power `13^a`, ask the *minimal number of original source labels* whose complete time series generate every one of the 63 labelled series by **time-independent coefficients in Z/13^a Z**, valid simultaneously at **every k>=3**. This is a typed linear observer compression, retaining provenance of the selected masks.

## Theorem 1 — 249 taps decide infinite-future reconstruction

Let `R=Z/13^a Z`, `E` be the forward-shift operator, and let
`C_m(E)` be the monic integer characteristic annihilator of mask m.
The monic product `G(E)=prod_(m=0)^62 C_m(E)` has degree 249 and annihilates
all mask sequences over every R. Thus, for any fixed coefficients `c_b in R`,
the identity `q_(m,k)=sum_(b in S)c_b q_(b,k)` for **all k>=3**
holds if and only if it holds at the **249 consecutive events**
`k=3,...,251`. The reverse implication is the monic recurrence induction
for the difference sequence; the other implication is immediate.

Consequently the problem is exactly the minimal original-row generating-set
problem for the 63-by-249 matrix `A_a=(q_(m,3+j) mod 13^a)` over R.

## Theorem 2 — certified minimal generating set over a prime-power ring

For any prime p and exponent a>=1, there is a recursive exact
elimination which returns a subset of *original* rows, reconstruction
coefficients for every input row, and a list of nonnegative layer counts.
Its selected-row cardinality is minimal, and is the minimal number of
cyclic generators of the row module. This holds for arbitrary rectangular
matrices over R=Z/p^a Z, including torsion modules.

Proof. Reduce the rows modulo p and pick original rows with independent
reductions spanning their F_p row image; let their number be r_0.
Choose r_0 pivot columns giving an invertible minor modulo p, hence
an invertible minor modulo p^a. For each original row solve its pivot
coefficients modulo p^a, subtract its combination of the selected rows,
and obtain a residual with all pivot coordinates zero and all entries
divisible by p. These operations split the row module into a free direct
summand R^{r_0} and a residual submodule supported in p times the complementary
coordinates. Dividing the residuals by p identifies their module with a
row-generated module over Z/p^(a-1) Z. Iterate. The minimal number of
generators is r_0 plus that of the residual module (local-ring Nakayama,
or the corresponding elementary-divisor normal form). The recursive
reconstruction coefficients are lifted and substituted back to the
original selected rows; their modular equality can be checked entrywise.
The layers are exactly the counts of invariant factors of valuation
0,1,...,a-1 in the finite-ring Smith decomposition. QED.

## R261 exact 13-adic numerical theorem

All values below were obtained with exact `Fraction` initial states and
modular integer recurrence. The theorem above turns the finite data into
**all-future** statements for this fixed input. The bottom row displays
the minimal 15-original-label basis modulo 13^10, not a heuristic selection.

| a | modulus 13^a | new Smith-layer count | minimum labels |
|---|---:|---:|---:|
| 1 | 13 | 1 | 1 |
| 2 | 169 | 1 | 2 |
| 3 | 2,197 | 1 | 3 |
| 4 | 28,561 | 2 | 5 |
| 5 | 371,293 | 2 | 7 |
| 6 | 4,826,809 | 2 | 9 |
| 7 | 62,748,517 | 1 | 10 |
| 8 | 815,730,721 | 1 | 11 |
| 9 | 10,604,499,373 | 2 | 13 |
| 10 | 137,858,491,849 | 2 | **15** |

The first ten exact 13-adic elementary-divisor strata (not an assertion
about later strata) are `[1,1,1,2,2,2,1,1,2,2]`. Equivalently, the
computed prefix of Smith valuations for the integral 63-by-249 tap matrix
is `[0,1,2,3,3,4,4,5,5,6,7,8,8,9,9]`.

Original-mask minimal generators:

- modulo 13: `[9]`
- modulo 169: `[9,10]` (sharpens R260A's lower bound)
- modulo 2,197: `[9,10,12]`
- modulo 28,561: `[9,10,12,13,14]`
- modulo 137,858,491,849: `[9,10,12,13,14,15,24,25,26,27,29,30,44,45,46]`.

This gives a concrete provenance-preserving p-adic repair: one label
suffices at first precision, and each further residual layer requires
the stated extra original mask taps.

## Reproducibility, validation and limitations

Run `python R261_10_layer_observer.py` from this directory. It imports
`R260_labelled_modular_quotient.py` from the pinned parent branch (and
thus the exact R258 model), runs all ten exponents, generates
`R261_full_verification.json` with all 63 reconstruction coefficient
vectors for each exponent, and writes `R261_verification_digest.json`.
No floating point is used.

For each modulus: all 63-by-249 tap entries are reconstructed exactly;
then the next 249 taps are checked separately using each mask's own
characteristic recurrence. A total of 63*498*10 labelled tap values is
covered, including additional 249-tap checks per case. The finite
249-window plus monic-annihilator argument establishes every later event.

The complete local reproduction produced a 92,291-byte full JSON with
SHA-256 `87eac27cd9ded605493ecd4d383ef3459dad2f507a9fbbe874cd4d8b4f24e669`.
The committed digest records the precise ten layer profiles and mask
sets; the full JSON is reproducible from committed code and upstream
source. No independent referee or native BRC EffectHistogram integration
was performed.

The result concerns only the declared 63-mask auxiliary positive-rational
observer and constant-coefficient modular reconstruction. No claim
about signed-BRC dynamics, complete native X6 or three-dimensional
slice dynamics follows from it.

## Next scientific questions

Determine additional 13-adic layers and their growth pattern, or derive
a symbolic p-adic invariant-factor description rather than a fixed-depth
table. Investigate whether a smaller **zero-only test observer** exists
than the constant-linear reconstruction basis. Compare the p-adic
compression costs with a genuine typed BRC source-preserving interface
and assess the analogous 23-adic precision lift.
