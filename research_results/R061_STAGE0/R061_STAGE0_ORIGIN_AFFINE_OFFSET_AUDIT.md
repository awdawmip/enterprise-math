# R061 Stage 0 — Origin / Affine Offset Audit

## Frozen typing fact

`O_E=0` is a triple cell-boundary intersection. It is not a cell center and
not a cell.

Therefore an origin-based native cell trajectory cannot be written as a free
word in center-to-center transition generators alone.

## Required start operator

A type-correct realization requires an incidence operation of the form

`Sigma_O : O_E -> {one of the three cells incident to O_E}`.

`Sigma_O` is not itself a primitive nearest-center transition. It selects the
first single-cell state. Ambiguity must branch into several single-cell
trajectories; it must not produce a simultaneous multi-cell state.

After selecting `C_start`, a center-transition word `w` can be replayed as

`Sigma_O ; w`.

If `|w|=m`, then conditional on the selected start cell:

- center-to-center transition count contributed by `w` is `m`;
- cell-state count is `m+1`;
- there is additionally one origin-incidence event `Sigma_O`.

## The unresolved affine equation

Let `Addr(C_start)=s_ij` in a sector chart. If the primitive generators act as
unit chart increments, then the absolute endpoint address is schematically

`Addr(C_end)=s_ij + End_formal(w)`

within that chart, with the appropriate chart operation.

But `s_ij` is not supplied by the current foundation, and `s_ij` cannot be
silently set to zero because `(0,0,0)` is the native origin vertex rather than
a center state.

Consequently the identity

`absolute endpoint address = (#X,#Y)`

is not derivable from the present premises.

This is exactly the affine/off-by-one gap the taskbook required to audit.

## N=0

The empty word cannot select a cell at the origin. Therefore zero length
already requires special non-cell or start-incidence semantics.

## 3-4-5 audit

For branch `(3,4)` the formal shuffle theorem proves exactly seven
center-transition **letters**.

It does **not** prove that the native origin-to-endpoint realization has seven
primitive center transitions.

What can be stated exactly is:

`NativePath = Sigma_O ; w`, `|w|=7`

only after a start cell has been chosen and only as a relative transition
description.

Whether the canonical endpoint cell of native address `(3,4,0)` is reached
after 7, 6, or another count of center transitions from an incident start
cell depends on the missing incident-cell/address affine anchor and on the
native canonical path class. The current premises do not determine that
number.

The native length remains `5` by the frozen sector metric; it must not be
replaced by any of those jump counts.

## Verdict

`ORIGIN_AFFINE_OFFSET_RESOLVED = false`.

`SIGMA_O_TYPE_REQUIREMENT = true`.

`NAIVE_3_4_WORD_LENGTH_AS_ORIGIN_TRANSITION_COUNT = not established`.

No guessed `+1/-1` correction is frozen.
