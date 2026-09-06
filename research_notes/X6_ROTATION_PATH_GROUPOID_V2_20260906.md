# X6 rotation-path groupoid: operation-safe lift above triadic frame rotations

Status: `FREE_RESEARCH / EXACT DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Task: `RS-X6-NATIVE-ROTATION-DYNAMICS`
Depends on: `X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`

## 1. Why the frame group is not yet dynamics

V1 proves the exact triadic frame group

`R_triad = (C2)^6 semidirect A6`

and shows that every triadic macrostep on the signed unit shell has two shortest native Cell realizations.

A frame element records only the endpoint transformation. P000 path semantics, BRC provenance and the existing C6/C12 branch split show that the actual microtrajectory is additional information.

Therefore native rotation dynamics needs a typed carrier above the frame action.

## 2. Native path groupoid

Let `Path(X6)` be the groupoid whose objects are native spatial Cells and whose morphisms are finite primitive signed-axis Cell paths. Immediate reversal supplies path inverse; concatenation supplies composition.

Every signed frame element `g in R_triad` acts on Cells and on primitive path words by signed-axis relabeling.

## 3. Rotation-path groupoid

Define a rotation-path arrow from `x` by

`(g,gamma)`

where

- `g in R_triad`;
- `gamma` is a concrete native path from `x` to `g x`.

For

`(g,gamma): x -> g x`

and

`(h,eta): g x -> h g x`,

define

`(h,eta) o (g,gamma) := (h g, gamma ; eta)`.

Identity is `(1,empty_path)`. Inverse is

`(g,gamma)^-1=(g^-1,reverse(gamma))`.

All source/target types match exactly, so this is a groupoid.

Call it

`ROT_PATH_X6`.

It has two natural forgetful maps:

`ROT_PATH_X6 -> X6 action-groupoid of R_triad`

and

`ROT_PATH_X6 -> Path(X6)`.

Neither forgetful map is declared observer-safe for arbitrary future operations.

## 4. Length grading makes every BRC fiber finite

Because PF paths allow arbitrary loops, the ungraded fiber over one frame arrow contains infinitely many paths.

For `M in N_0`, define

`Rot_M(x,g)={gamma: x -> g x | PATH_COUNT(gamma)=M}`.

Each `Rot_M(x,g)` is finite on signed X6.

Composition respects the exact grading:

`Rot_M(x,g) x Rot_N(gx,h) -> Rot_{M+N}(x,hg)`.

Hence the finite graded family is operation-safe and supports the existing tower

`Path-formal BRC -> N-BRC -> Boolean BRC`

at each fixed grade.

This is the preferred finite computational carrier for native rotation research.

## 5. Shortest rotation fibers are not a sub-groupoid

Define

`M_min(x,g)=||g x-x||_1`.

The shortest fiber is `Rot_{M_min}(x,g)`.

V1 already gives the obstruction. For a unit phase `a` and a nontrivial triadic generator `Q`,

`M_min(a,Q)=2`,

`M_min(Qa,Q^-1)=2`,

but

`M_min(a,1)=0`.

Concatenating one shortest forward lift with one shortest inverse lift gives a length-4 loop. It cannot belong to the shortest identity fiber.

Therefore shortest-path projection is not closed under rotation composition.

## 6. A full triadic frame cycle has nontrivial path holonomy

Let `Q=Q_S` and choose one signed unit phase `a_0`. The frame orbit is

`a_r=Q^r a_0`, `r mod 6`.

For each macro edge

`a_r -> a_{r+1}`

there are exactly two shortest native branches, INNER and OUTER.

Thus a six-macrostep frame loop `Q^6=1` has exactly

`2^6=64`

distinct concatenated shortest microtrace lifts of total length `12`.

They all begin and end at the same native Cell `a_0`, while their intermediate Cell histories differ.

Hence

`FRAME_HOLONOMY = IDENTITY`

does not imply

`PATH_HISTORY = EMPTY`.

This is the simplest exact separation between rotation frame closure and native path holonomy.

The all-OUTER bit word is precisely the intrinsic 12-Cell outer cycle from V1. On the four established FCC STAR slices it is the existing typed C12 outer microcycle. The other 63 branch words are equally valid signed-X6 shortest concatenations unless a separate law excludes them.

## 7. Exact branch-word observer

For one six-step triadic frame cycle define

`beta=(beta_0,...,beta_5) in {I,O}^6`.

The map from `beta` to the 12-microstep Cell sequence is injective because changing `beta_r` changes the unique intermediate Cell at microtime `2r+1` while all macro endpoints remain fixed.

Thus the six branch bits are genuine path provenance, not redundant coding.

N-BRC at the macro-terminal Cell therefore records multiplicity `64` for this restricted concatenated-shortest population, while Boolean support records `1`.

## 8. Universal law-selection interface

A deterministic native rotation law on this restricted macro interface is a section choosing one path in each allowed `Rot_M(x,g)` fiber.

A stochastic/weighted law is a positive or signed/phase decoration on those path witnesses, with the appropriate BRC carrier chosen by observer needs.

The rotation-path groupoid itself does not choose INNER, OUTER, minimal length or any probability. It is the universal provenance-preserving carrier in which such laws can be stated and compared.

## 9. Current consequence

The upper rotation problem is now split cleanly:

1. **frame algebra** — V1 triadic group `(C2)^6 semidirect A6`;
2. **universal path lift** — `ROT_PATH_X6` and its finite length grading;
3. **law selection** — still open: which rotation path fibers or branch weights nature admits;
4. **time coupling** — still open: how one macro rotation event is ordered/calibrated in the native time dimension.

This decomposition is operation-safe and is now the recommended interface for the sibling triadic, time and internal-state tasks.
