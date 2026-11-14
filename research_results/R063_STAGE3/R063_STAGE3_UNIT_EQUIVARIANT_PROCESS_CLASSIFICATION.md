# R063 Stage 3 — Unit-Equivariant Process Classification

Status: `UNIT_EQUIVARIANT_PROCESS = EXACT`
Researcher-ID: `EM-R063S3-F1CF9D`

## Carrier

Represent a native source path by its finite ordered position chain, initially labelled `0` for `X_i` and `1` for `X_j`. Let all process labels live in

`C4 = Z/4Z = {0:+X_i, 1:+X_j, 2:-X_i, 3:-X_j}`.

For finite labelled posets `P,Q`, define the interaction tensor

`P box Q := P x Q`

with ordinary Cartesian product order and label

`lambda_(P box Q)(x,y)=lambda_P(x)+lambda_Q(y) mod 4`.

## Unit action

A unit state `k in C4` acts by globally shifting every label by `k`. Then

`(k.P) box (l.Q) = (k+l).(P box Q)`

exactly, and

`Eval(k.P)=J^k Eval(P)`.

Therefore the quotient of process objects by global label shift has a well-defined multiplication and maps to the Stage 2 unit orbit `URoot`. It retains more information than `URoot` because source positions and partial order remain present.

## Coherence

`(P box Q) box R` and `P box (Q box R)` are canonically isomorphic by

`((x,y),z) <-> (x,(y,z))`.

The isomorphism preserves product order and the label sum `lambda_P+lambda_Q+lambda_R mod 4`. Swapping factors gives the corresponding commutativity isomorphism. The one-point process labelled `0` is the unit.

## Ordered readout boundary

Only after process evaluation/cancellation may an ordered sector convention choose a unit shift that produces a nonnegative ordered component pair. For `(1,2)^2`, the process first exposes raw `(-3,4)`; the Stage 2 `i` convention then applies `-J` (label shift `3`) to obtain `(4,3)`.

The square-axis obstruction is not erased: `(1,1)^2` still has ordered readouts `(0,2)` and `(2,0)` under the two Stage 2 orientations, while the unit-equivariant process has one unit-orbit target.

## Semantic verdict

The carrier is an exact finite multiplicative enrichment, but it is a new process layer constructed from frozen path order plus the derived signed interaction table. It is therefore `N1_DERIVED_OPERATIONAL`, not a global native multiplication law.

`UNIT_EQUIVARIANT_PROCESS = EXACT`.
