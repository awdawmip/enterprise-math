# BRC Energy Scaled Cross Coordinate — Round 14

Status: `VERIFIED PRIOR ANSWER / TWO CORRECTIONS / EXACT OBSERVER-EQUIVALENT COORDINATE / FINITE CONSTANT-FACTOR BENCHMARK`
Date: `2026-09-07`
Parent: `t0.brc_square_increment_difference_jet`
Reuse resolution: `EXTEND_EXISTING_TOOL`

## 1. Question

Verify the preceding informal product-jet answer before continuing.  In
particular:

1. check the algebraic rewrite of `q(2J+q)` from the quotient/remainder carrier;
2. check whether `q^2` and the quotient remainder really form a useful smaller
   recurrence;
3. continue from the current main-backed square-increment difference jet rather
   than replaying already-completed work.

The audit found two concrete corrections to the informal answer and then a
smaller exact execution coordinate for the current energy jet.

## 2. Correction 1: the general product identity was right; the h=2 specialization was not

The exact Euclidean carrier is

`2hJ = q(4m+h) + rho`.

Therefore

`q(2J+q)`
`= ((4m+2h)q^2 + q rho)/h`.

For `h=1`,

`q(2J+q) = (4m+2)q^2 + q rho`.

For `h=2`, the correct specialization is

`q(2J+q) = (2m+2)q^2 + q rho/2`.

The earlier chat answer wrote `(2m+1)q^2 + q rho/2`; it lost the final `q^2`
term when specializing.  The repository implementation never used that faulty
specialization: the main-backed energy jet computes/transports the exact
square increment directly.

## 3. Correction 2: q^2 transports exactly, but Delta q is not a constant small quantity

If `q'=q+d`, then of course

`q'^2 = q^2 + 2qd + d^2`.

So retaining `q^2` is algebraically sufficient to avoid a fresh square.  The
informal answer went too far when it treated `d=Delta q` as if it were a
uniformly bounded small integer.  On the `m~N^(1/5)` tail, the first quotient
difference still grows with N.  What the proved quotient jet controls is the
stride-8 second difference and the third-difference repair:

`-2 <= nabla^2 q <= 98`,

`-4 <= nabla^3 q_new <= 4`.

Thus the naive `q^2` update still contains a product of two N-growing operands
through `q*Delta q`.  The current square-increment difference jet is stronger:
it retains enough higher difference state to remove all such post-seed general
products.

## 4. Correction 3: Delta rho is not uniformly small

The informal answer proposed testing whether the Euclidean remainder difference
`Delta rho` might be bounded by a small N-independent constant.  That hypothesis
is false and is not used by the main-backed quotient jet.

The exact remainder has

`0 <= rho < 4m+h`.

Across one stride-8 orbit its change can scale with the multiplier.  Finite
stress probes already produce remainder differences far beyond any small fixed
constant, with bit length growing as the input scale grows.  The correct design
is the one already merged in `t0.brc_quotient_jet_tail`: retain `rho` exactly and
transport the provisional Euclidean residual, then normalize by at most four
additions/subtractions of the new denominator.

So the rejected route is

`SMALL Delta rho -> FINITE-STATE REMAINDER NOISE`.

The retained exact quotient remainder remains a necessary repair/provenance
coordinate.

## 5. Durable frontier found during the audit

The repository had already advanced beyond the speculative product-jet plan.
Current main contains `t0.brc_square_increment_difference_jet`, which transports

`E=q(2J+q)`

on each of the five stride-8 source residue orbits.

Write at the current orbit point

`s = nabla q`,
`a = nabla^2 q`,
`t = nabla J`,
`u = nabla^2 J`,
`e = nabla^3 q_new`,
`w = nabla^3 J_new`.

The proved bounds are

`e in [-4,4]`,
`a_new in [-2,98]`,
`w in [-3,387]`.

The current implementation retains

`M = s*u`

and uses the exact third-difference identity

`nabla^3 E_new`
`= e*(2*(J+q+s+a+t+u+w)+e)`
`  + 2*w*(q+s+a)`
`  + 6*(M+a*(s+t))`.

After the fixed seed budget, every newly evaluated product has a bounded
integer factor; there is no multiplication of two N-growing operands.

## 6. Observer-equivalent cross coordinate

The energy observer never consumes M alone.  It consumes

`K = M + a*(s+t)`.

Since `(a,s,t)` are already retained,

`M = K - a*(s+t)`.

Thus replacing M by K is a bijective coordinate change on the already-retained
jet state.  No observer or provenance information is lost.

The energy third difference collapses to

`nabla^3 E_new`
`= e*(2*(J_new+q_new)-e)`
`  + 2*w*(q_new-e)`
`  + 6*K`.

The cross coordinate itself closes:

`K_new`
`= K + s*w + e*(s+t) + a_new*(2*u_new+a_new)`.

Again every newly evaluated product has a bounded coefficient.

## 7. Scaled cross coordinate

A direct K implementation is exact but its finite timing gain was not stable at
all large bit sizes.  The actual observer uses `6*K`, so retain instead

`C = 6*K`.

This remains information-equivalent:

`K=C/6`,
`M=C/6-a*(s+t)`,

and C is exactly divisible by 6 by construction.

Now

`nabla^3 E_new`
`= e*(2*(J_new+q_new)-e)`
`  + 2*w*(q_new-e)`
`  + C`,

so the steady-state energy observer no longer performs the big-integer
multiplication `6*K`.

The exact C recurrence is

`C_new`
`= C`
`  + 6*s*w`
`  + 6*e*(s+t)`
`  + 6*a_new*(2*u_new+a_new)`.

The only multipliers introduced here are bounded:

- `6e in [-24,24]`;
- `6w in [-18,2322]`;
- `6a_new in [-12,588]`.

Therefore the scaled coordinate preserves the existing
`POST-SEED GENERAL-MULTIPLICATION-FREE` theorem.

## 8. Independent exact validation

Before repository toolization, an independent integer prototype ran the current
M-coordinate and the C-coordinate side by side.

Validation compared on every step:

`(m,J,R,q,rho,E)`

plus square-residue-cascade outcomes.  Random cohorts through 2048 bits ran
1,200 transitions per sample with no mismatch.  The checked-in regression goes
further by comparing the new scanner directly against the current
`EnergyDifferenceJetTailScanner` on exhaustive small odd N and random
64..8192-bit streams.

Separate algebraic tests verify:

1. `M <-> C` invertibility;
2. the compact energy third-difference identity against the existing exact
   identity;
3. the C recurrence against direct reconstruction from the next finite
   differences.

The seed budget remains exactly 15 quotient divisions and 15 direct square-
increment products.

## 9. Finite performance

A unified local reference benchmark used the same deterministic odd-N sequence,
3,000 retained transitions per sample and the same BALANCED square-gap cascade.
Median timings over seven repetitions were:

| N bits | samples | current M / scaled C |
|---:|---:|---:|
| 1024 | 8 | 1.082x |
| 2048 | 8 | 1.075x |
| 4096 | 8 | 1.138x |
| 8192 | 6 | 1.034x |
| 16384 | 4 | 1.026x |

This is a modest constant-factor execution improvement, not an asymptotic
complexity theorem.  The gain is largest in the middle large-integer range and
shrinks at very large sizes as other bounded-coefficient updates dominate.

## 10. Square-gap residue transport audit

The parent note proposed transporting the three BALANCED cascade residues
instead of recomputing big-integer `%` operations.  Exact residue-state
recurrences were prototyped and matched direct completion-gap residues.  A
2-adic front gate using `gap & 4095` is also an exact zero-false-negative
necessary square test and makes the filter function itself substantially
cheaper.

However, after the current energy jet is active, full-pipeline profiling shows
that square-gap filtering is no longer the dominant cost.  The extra residue
state produced only small/noisy end-to-end changes in CPython.  Therefore these
variants are not promoted in this round.

Decision:

`EXACT RESIDUE TRANSPORT / 2-ADIC FRONT -> HELD BACK BY FULL-PIPELINE COST`.

Do not infer mathematical failure; this is an implementation-cost decision.

## 11. Decision and boundary

Promote the scaled C coordinate only as a compatible execution variant of the
existing T0_BRC square-increment jet:

`M=s*u`
`<-> C=6*(s*u+a*(s+t))`.

No Foundation mutation, Working Truth mutation, new factorization principle,
search-horizon reduction or RSA-practicality claim is made.

The next discriminating attack should profile the remaining bounded-coefficient
updates as a group.  Another derivative order is unlikely to help unless it
reduces the number of N-sized temporary integers rather than merely replacing
one exact formula by another.
