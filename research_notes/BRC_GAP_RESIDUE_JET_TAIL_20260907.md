# BRC Completion-Gap Residue Jet — Round 14

Status: `PROVED MODULAR DIFFERENCE TRANSPORT / TABLE CASCADE MOVED BEFORE FULL GAP MATERIALIZATION / FINITE MIXED-TO-POSITIVE CROSSOVER`
Date: `2026-09-07`
Parents: `t0.brc_square_increment_difference_jet`, `t0.brc_square_gap_cascade`
Reuse resolution: `EXTEND_EXISTING_TOOL`

## 1. Recovered frontier

The previous local plan still named

`q(2J+q)`

as the remaining large product in the linear BRC tail. Current main had already
advanced beyond that plan: Round 13 transports the exact square increment by a
third-difference energy jet. After fifteen seed divisions and fifteen seed
products, its steady-state loop contains no fresh division and no product of two
N-growing operands.

The first verified unfinished unit was therefore the next item recorded by Round
13: the three big-integer modulo reductions used by the staged square-gap tables.
This round starts from that durable frontier instead of replaying the completed
energy-jet work.

## 2. Completion gap

For a multiplier state

`mN = J_m^2 + R_m`, `0 <= R_m <= 2J_m`,

the upward completion gap is

`F_m = 0` when `R_m=0`, and otherwise

`F_m = 2J_m+1-R_m = (J_m+1)^2-mN`.

The existing BALANCED table cascade asks whether `F_m` is a quadratic residue
modulo

`4032`, `12155`, and `12673`.

Previously every candidate first materialized the full N-scale integer `F_m` and
then evaluated up to three full big-integer `%` operations.

## 3. Fixed root-residue orbits

For odd N, source multipliers lie in

`{0,1,3,5,7} mod 8`.

Fix one source residue class and write

`m_k = m_0 + 8k`,
`J_k = floor(sqrt(m_k N))`.

Round 13 already computes the exact stride-eight third difference

`w_(k+1) = J_(k+1)-3J_k+3J_(k-1)-J_(k-2)`.

For any fixed modulus M, reduction is a ring homomorphism. Therefore three
seed residues determine an exact modular difference jet:

`j_k = J_k mod M`,
`v_k = nabla J_k mod M`,
`a_k = nabla^2 J_k mod M`.

The next root residue is

`j_(k+1) = j_k+v_k+a_k+w_(k+1) mod M`,

and the difference state updates by

`v_(k+1)=v_k+a_k+w_(k+1) mod M`,
`a_(k+1)=a_k+w_(k+1) mod M`.

No approximation is involved. The full root never needs another reduction
modulo M after the third visit to that source class.

There are five source classes and three seeds per class, hence exactly

`5*3 = 15`

root-residue seed reductions.

## 4. Transporting mN modulo M

Only one global target residue is needed. Seed

`n_M = N mod M`,
`t_m = mN mod M`.

If the sparse stream advances by `h in {1,2}`, then

`t_(m+h) = t_m + h*n_M mod M`.

This costs two one-time full-width reductions (`N mod M` and `m_0 mod M`) and
then only fixed-modulus arithmetic.

## 5. Exact completion-gap residue

At a consumed source state, if `R_m=0`, set

`f_m=0`.

Otherwise use

`f_m = (j_m+1)^2-t_m mod M`.

By the identities above,

`f_m = F_m mod M`

exactly. Thus any registered square-residue bit table can be queried before the
full integer `F_m` is built.

This is a typed observer result. The root residue and target residue are not
substitutes for the exact root/remainder state; they are a lossless modular
observer dedicated to the table gate.

## 6. Transport profiles

The executable surface exposes three exact profiles.

### PRIMARY

Transport only

`M=4032`.

Candidates passing stage one materialize the exact gap and pay the remaining two
native reductions.

### COMPACT (default)

Transport

`M=4032*12155=49,008,960`.

Both first-stage tables are queried from one 26-bit residue. Only their joint
survivors materialize the full gap and pay `%12673`.

The two moduli are coprime. Their exact uniform CRT survival density is

`(192/4032)*(1134/12155)=54/12155`

or approximately

`0.4442616207%`.

Thus the uniform rejection density before full gap materialization is

`99.5557383793%`.

### FULL

Transport

`M=4032*12155*12673=621,090,550,080`.

All three table decisions use only the transported 40-bit residue. After the
fifteen root seeds, the cascade performs no native big-integer modulo operation.
The exact gap is materialized only for complete cascade survivors when an exact
square test is requested.

FULL is mathematically strongest, while COMPACT keeps the modular state smaller
and was chosen as the reference performance profile.

## 7. Zero-false-negative property

Every stage remains a necessary condition only.

If `F_m=b^2`, then for every registered modulus M,

`F_m mod M = b^2 mod M`

is in the corresponding square-residue bit table. Because the transported
residue is exact, no true square can be rejected by PRIMARY, COMPACT, or FULL.

The final exact `isqrt` remains authoritative on survivors.

## 8. Source-reporting convention

The parent energy scanner emits the stride-eight root third difference for the
source state consumed during an advance. The residue wrapper therefore:

1. saves the current source `(m,J,R)`;
2. advances the parent once;
3. uses the emitted exact third difference to update that source orbit;
4. reports the table verdict for the saved source.

This is a one-transition reporting delay. It changes only which endpoint is
included in a finite benchmark, not the set or semantics of a long scan.

## 9. Operation count

For COMPACT:

- two one-time full-width reductions seed `N mod M` and `m_0 mod M`;
- fifteen root reductions seed five modular difference orbits;
- every later source visit uses only word-size modular additions,
  multiplication and table lookups for stages 4032 and 12155;
- only first-two-stage survivors materialize `F_m` and pay `%12673`;
- only BALANCED survivors pay exact gap `isqrt`.

For FULL, the post-seed native modulo count is zero.

The energy/root transport underneath remains exactly Round 13.

## 10. Validation

Repository regression includes:

- exact product-modulus constants for PRIMARY, COMPACT and FULL;
- direct verification of the root-residue third-difference recurrence;
- exactly fifteen root seed reductions and five activated source orbits;
- exhaustive odd `N<500`, 200 transitions each;
- random 64 through 8192-bit scans for all three profiles;
- equality of source root, root remainder and completion-gap residue with direct
  `isqrt`/modulo oracles;
- equality of every cascade verdict with the existing BALANCED implementation;
- preservation of exact-square verdicts;
- a certificate that FULL performs no native post-seed cascade reduction;
- proof-by-execution that a rejected transported prefix can leave the exact gap
  unmaterialized.

## 11. Finite benchmark

The committed benchmark compares two equal-semantics pipelines:

1. Round-13 energy jet plus the native BALANCED cascade on every full gap;
2. the same energy jet plus COMPACT residue transport and native final stage only
   on first-two-stage survivors.

For each bit size, five deterministic populations are used, with four odd values
per population and 2,000 source states per value. Each population ratio is
measured separately; the table reports their median to avoid treating one noisy
interval as a stable crossover.

| N bits | states | first-two survivors | BALANCED survivors | median native/COMPACT |
|---:|---:|---:|---:|---:|
| 1024 | 40,000 | 461 | 92 | 0.790x |
| 2048 | 40,000 | 667 | 119 | 0.964x |
| 4096 | 40,000 | 444 | 62 | 1.049x |
| 8192 | 40,000 | 563 | 83 | 1.076x |
| 16384 | 40,000 | 590 | 116 | 1.089x |

The first-two survivor rate in these structured gap populations is about
1.1%--1.7%, higher than the uniform CRT density but still removes roughly
98.3%--98.9% of full gap materializations and final big-mod reductions.

Interpretation:

- small inputs should retain the native cascade;
- the finite CPython crossover is around several thousand bits and is noisy;
- the 8192 and 16384-bit median populations favor COMPACT by about 7.6% and 8.9%;
- this is an incremental improvement over an already optimized energy-jet
  pipeline, not the total gain relative to direct per-multiplier square roots.

Population-level timings vary materially on the shared execution environment.
No machine-independent AUTO threshold is registered. A conservative runtime
may choose native below 8192 bits and benchmark its own large-integer backend.

## 12. Wider combined bitmap experiment

A 6,126,120-byte bitmap for every accepted residue modulo

`4032*12155`

can replace the two small table lookups with one direct bit access. Isolated
filter lookup becomes much faster, but full-pipeline timings were unstable and
the cache footprint is over three orders of magnitude larger than the existing
3.6 KiB staged payload. It is not promoted.

The retained design uses the existing small tables and transports only their
input residue.

## 13. Decision and boundary

Promote as a T0_BRC extension:

`ENERGY DIFFERENCE JET`
`+ ROOT RESIDUE DIFFERENCE JET`
`+ mN RESIDUE TRANSPORT`
`-> TABLE CASCADE BEFORE FULL GAP MATERIALIZATION`.

This result is an exact execution/observer optimization. It does not:

- shorten the multiplier search horizon;
- change Lehman/Hart-style factor-search complexity;
- prove RSA-scale practicality;
- create a new factorization principle;
- mutate Foundation or Working Truth.

The square-residue tables remain classical modular arithmetic. The BRC-specific
contribution is the exact transport and composition of their observer inputs from
retained root-difference state.

## 14. Next frontier

After FULL residue transport, the steady-state candidate loop has no fresh root,
full division, N-growing product or big-integer table modulo. The remaining
N-scale work is predominantly bounded-coefficient additions inside the quotient,
root and energy jets; exact gap materialization and `isqrt` occur only on complete
table survivors.

The next discriminating question is therefore architectural rather than another
derivative order: fuse the root-residue observer into the existing energy orbit
and batch several source transitions, reducing Python object/dispatch overhead
without weakening the exact provenance state. Any claimed gain must be measured
against the current native cascade and must retain the FULL/COMPACT zero-false-
negative oracle equivalence.
