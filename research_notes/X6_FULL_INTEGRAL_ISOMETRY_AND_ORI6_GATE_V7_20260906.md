# X6 rotation V7: full integral component-isometry frame group and the Ori6 gate

Status: `FREE_RESEARCH / EXACT ALGEBRAIC CLOSURE / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`;
- `research_notes/X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`;
- current `Ori_6=S6/A6` chart/rotation results.
Checker: `experiments/x6_integral_isometry_v7_20260906/check_integral_isometry_ori6.py`.

## 1. Question

The current X6 Foundation fixes the signed integer component carrier and the native component norm

`q(z)=z_1^2+...+z_6^2`.

The physical/path-level native rotation law is still open. But a narrower static question can now be closed exactly:

> what are all integer-linear frame automorphisms preserving the frozen X6 component norm?

The answer is the full signed-permutation group. This closes the **static integral frame-isometry envelope**, not the physical rotation dynamics.

## 2. Norm-one lattice shell

Let

`A in GL(6,Z)`

satisfy

`q(Az)=q(z)`

for every `z in Z^6`.

For each standard basis vector `e_i`,

`q(Ae_i)=q(e_i)=1`.

An integer vector has squared norm one iff exactly one component is `+1` or `-1` and every other component is zero. Hence

`Ae_i in {+/-e_1,...,+/-e_6}`.

Because `A` is invertible, the six images `Ae_i` are six distinct signed coordinate units and use every unsigned coordinate axis exactly once.

Therefore every column of `A` has one nonzero entry `+/-1`, with one such entry in each row. Thus `A` is a signed permutation matrix.

Conversely every signed permutation preserves `q`.

Hence

`O_X6(Z) := {A in GL(6,Z): q(Az)=q(z) for all z}`

satisfies

`O_X6(Z) ~= (C2)^6 semidirect S6`.

Its order is

`2^6 * 6! = 46080`.

This proof uses only the frozen integer component carrier and sum-of-squares readout. It does not import classical 90-degree orthogonality as a native premise.

## 3. Meaning for the affine Cell torsor

`X6_NATIVE_SPATIAL` is an affine torsor for `Z^6`, not a vector space with a distinguished ontic origin.

After choosing a pivot/Cell anchor `c`, an element of `O_X6(Z)` acts on relative displacement coordinates around `c` by a signed permutation. Changing the pivot conjugates the same frame law by translation.

Thus the result classifies **anchor-relative integral linear frame isometries**. It does not assert that each one is one primitive Cell-transition event or that every physical rotation process is instantaneous.

A macro frame isometry may require a nontrivial Path/BRC realization and time/event context.

## 4. Triadic subgroup is exactly the even-positive-permutation half

The current canonical triadic generators produce

`R_triad=(C2)^6 semidirect A6`,

of order 23040.

Under the natural projection

`pi:O_X6(Z)->S6`

that forgets sign flips,

`R_triad=pi^{-1}(A6)`.

Therefore

`[O_X6(Z):R_triad]=2`.

So the triadic/channel/chart dynamics found so far fills **exactly one index-two half** of the complete integral linear isometry frame group.

## 5. Ori6 is positive-axis permutation parity

Define the current relational orientation charge

`Ori_6 := S6/A6 ~= C2`.

For a signed frame `g`, `Ori_6(g)` depends only on the parity of its underlying unsigned-axis permutation.

This is the quotient that current triadic positive-frame dynamics, unsigned channel circulation and orientation-preserving all-20 chart transport preserve.

The kernel is exactly `R_triad`.

Thus `Ori_6` gives the exact static gate between the current generated frame dynamics and the other half of the integral isometry envelope.

## 6. Ori6 is not ordinary matrix determinant

A signed permutation matrix has ordinary determinant

`det(g)=sgn(permutation) * product_i epsilon_i`.

The sign-flip kernel `(C2)^6` contains both determinant signs while having trivial `Ori_6` charge. Hence matrix determinant and `Ori_6` are distinct invariants.

All four combinations occur:

- `Ori_6=0`, `det=+1`;
- `Ori_6=0`, `det=-1`;
- `Ori_6=1`, `det=+1`;
- `Ori_6=1`, `det=-1`.

Therefore classical determinant-based “orientation preserving/reversing” terminology must not be substituted for the current project-specific `Ori_6` sector unless an additional bridge theorem is supplied.

## 7. One odd positive-axis generator closes the static frame envelope

Take any signed frame isometry whose unsigned permutation is odd, for example the pure positive-axis transposition

`P_12:E_1<->E_2`

with the other four axes fixed.

Since `A6` together with any odd permutation generates all of `S6`, and `R_triad` already contains the full sign kernel `(C2)^6`,

`<R_triad, P_12> = O_X6(Z)`.

Thus no large missing algebraic family remains at the integer-linear frame level. The entire static gap is one `Ori_6`-changing coset.

This is a group-generation statement only. It does not prove that `P_12` or any other odd-positive-permutation frame change is an admissible physical native event.

## 8. Physical rotation gate is now sharply isolated

The rotation problem separates into three layers.

### Static frame envelope — closed here

`O_X6(Z)=(C2)^6 semidirect S6`, order 46080.

### Current triadic frame dynamics — closed algebraically

`R_triad=(C2)^6 semidirect A6`, order 23040.

### Physical/event realization — still open

For every proposed frame transformation one must specify/derive:

- admissible source/target decorated state;
- concrete Cell-path/BRC realization or a proved law section;
- event kind/context;
- dependency/time behavior;
- retained internal/channel variables.

The branch-selector no-go already proves that even one fixed frame arrow can require different path sections under different event semantics.

Hence static membership in `O_X6(Z)` is necessary for an integer-linear norm-preserving frame transformation, but it is not sufficient for physical admissibility.

## 9. Exact next question: can Ori6 change dynamically?

All currently constructed native upper generators that couple

- triadic positive-axis rotation,
- minimal unsigned channel circulation,
- orientation-preserving chart transport

project to `A6`. Therefore they preserve `Ori_6`.

The exact unresolved gate is now:

> does any native event law produce an odd positive-axis permutation while remaining compatible with P000, concrete Cell/path semantics, internal state and event-time typing?

Two possibilities are mathematically clean:

1. **no admissible odd event exists under the eventual physical law** — `Ori_6` becomes a dynamical superselection charge;
2. **at least one admissible odd event exists** — together with current triadic dynamics it connects the full integral isometry envelope.

Current mathematics does not choose between them. Do not promote either branch without an event-level law/certificate.

## 10. Verification

The exact checker independently enumerates:

- all `2^6*6!=46080` signed permutations;
- all 23040 elements generated by the 20 canonical triadic generators;
- the 64-element pure sign kernel;
- equality of the triadic group with the even-positive-permutation half of the signed permutation group;
- closure to all 46080 elements after adding one odd positive-axis transposition;
- all four combinations of `Ori_6` parity and ordinary determinant sign;
- exactly 12 norm-one lattice vectors `+/-e_i`.

The first theorem itself is symbolic and does not rely on exhaustive enumeration: preserving the norm-one integral shell forces every integer-linear isometry to be a signed permutation.

No Foundation promotion, physical-law claim or external novelty claim is made.
