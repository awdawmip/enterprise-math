# R059D Stage AF — Bulge-Jump / Integer-Curvature Law

Researcher-ID: `EM-R059D-AF-7E31C6`
Task-ID: `RS-R059D-STAGE-AF-BULGE-JUMP-INTEGER-CURVATURE-LAW`
Taskbook source: `43fca741c6dee84172297d85c5b5e8fab652419b`
Frozen source main: `2d4badc86e9348a3c5b2ea2b280b55f7399346d7`
Accepted AE owner head: `f8b56c910150ecd04d7e30ac03ea5bf0083b9429`

## Primary disposition

`NO_LOW_COMPLEXITY_JUMP_GENERATOR_THROUGH_AUDIT_RANGE`

## Raw range and C precision

N and C were replayed for `r=1..512`.
Discovery was frozen to `1..256`; holdout was `257..512`.

C sampling was escalated only as a numerical convergence audit, never to improve a target fit:
- s64→128 changes 17 ledger radii;
- s128→256 changes 2;
- s256→512 changes 2;
- s512→1024 changes 1;
- the complete U/D triangle activation arrays at s1024 and s2048 are identical through all r=1..512.

Therefore the official AF C ledger uses `s=1024`, with independent `s=2048` equality certification.

## New exact integer-curvature theorem

For every frozen N/C sector boundary word, map:
- `1` to height +1,
- `2` to height 0,
- `3` to height -1.

The word is a nonnegative Motzkin excursion. Exactly:

`#1 = #3 = J`, `#2 = r-J`, and `|W_r| = r+J`.

If `h` is the current excursion height, then:

`B = sum h`

where the sum is taken immediately before every a-decreasing symbol `2` or `3` in open-sector columns.

This is a symbolic combinatorial identity: `B` and `J` are two functionals of one boundary-word state. It does not use Euclidean curvature, pi, sqrt, or the source circle equation.

The identity was replayed with zero failures on all 1024 resolver/radius rows.

## Radial jump anatomy

At r=512:
- N: `B=27417`, `J=79`, `DeltaB` reaches 125;
- C: `B=27399`, `J=79`, `DeltaB` reaches 121.

`DeltaJ` is binary in both probes (79 ones and 433 zeros), but `DeltaB` is not binary and grows across the census. The early staircase intuition therefore survives only for the boundary-excess channel J, not for the area/bulge increment.

Exact jump sets:
- `K_B^N`: 438 radii;
- `K_B^C`: 447 radii;
- exact intersection: 393;
- symmetric difference: 99.
- `K_J^N`: 79;
- `K_J^C`: 79;
- exact intersection: 60;
- symmetric difference: 38.

Every J symmetric-difference event is a one-radius phase delay: N jumps at r and C jumps at r+1. There are 19 such pairs. This is a strong finite-census window-skeleton candidate, but not an exact common point skeleton.

Thus:

`NO_RESOLVER_INDEPENDENT_JUMP_SKELETON_FOUND_THROUGH_R512`.

## Scalar state no-go

J is not enough to determine B resolver-independently. The first exact counterexample is:

`r=15, J_N=J_C=2, B_N=23, B_C=21`.

There are 412 same-r/same-J rows with different B through r=512. The smaller exact common state is the full Motzkin boundary word, not J alone.

## Arithmetic candidate that survives holdout

A narrow N-only result survives.

From N discovery J(1..256), exact floor-model feasibility gives:

`15/97 < alpha < 13/84`.

Searching primitive quadratic integer polynomials with coefficient magnitude <=8 yields exactly one positive root in that interval:

`3 alpha^2 + 6 alpha - 1 = 0`.

With this alpha, searching rational beta with denominator <=12 gives uniquely:

`beta=1/3`.

Candidate:

`J_N(r)=floor(alpha r + 1/3)`.

It has 0 mismatches on discovery and 0 mismatches on the untouched holdout 257..512.

It can be run without sqrt or source-Q lookup using the integer recurrence:

`j(0)=0`;

at radius r increment j iff

`3(3j+2)^2 + 6(3j+2)(3r) - (3r)^2 <= 0`.

This candidate is `FORWARD_AUTONOMOUS` for J_N, but remains `PROOF_OPEN` and does not generate B or W_r. It therefore does not satisfy the AF hard target.

For C, an exact affine floor law is already impossible on discovery: the required strict alpha interval collapses to the single boundary `13/84`.

## Other low-complexity negatives

- The AE transient `B=r-2` route fails at N r=11 and C r=12.
- Neither DeltaJ nor sign(Delta2B) has any exact period <=128 on discovery for either resolver.
- No full forward-autonomous B/J generator was frozen before holdout.
- The exact boundary-word state reduction is not itself a generator because W_(r+1) remains unknown.

## Theorem status

PROVED:
- sector Motzkin integer-curvature identity;
- scalar-J insufficiency by explicit counterexample;
- exact C s1024=s2048 occupancy stability through r=512.

FINITE CENSUS:
- J jump disagreements are 19 one-radius N→C delays;
- K_B/K_J overlap statistics.

CANDIDATE:
- N-only algebraic Beatty J generator, exact through discovery and holdout, proof open.

NEGATIVE:
- no resolver-independent exact jump skeleton;
- no low-complexity full B/J forward generator through the audited family/range.

`STOP_FOR_DRIVER_REVIEW`
