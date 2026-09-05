# X6 universal Cell completion prototype

Status: `RESEARCH CANDIDATE / EXACT INTEGER ENDPOINT ALGEBRA / NOT P000 PROMOTION`

This experiment implements the universal minimal Cell-endpoint completion forced by the four established K4 three-axis slice relations.

## Core model

Axis order:

`AB, AC, AD, BC, BD, CD`.

Endpoint normal form:

`G6^cell ~= Z^2 x Z/2`.

The `(u,v,sheet)` tuple in `x6_cell.py` is **only a computational normal form for endpoint state**. It is not a claim that Enterprise space has two spatial dimensions. P000 spatial dimension remains six because the native space has six native spatial axes.

## Main API

- `CellState(u,v,sheet)` — exact endpoint normal form;
- `axis_generator(axis)` — one of six native positive-axis endpoint generators;
- `step(state,axis,direction)` — adjacency event; `direction=-1` is path reversal, not a native negative axis;
- `endpoint_from_exponents(z)` — endpoint of a signed six-axis net trace;
- `return_certificate(z)` — exact integer Cell-return test;
- `slice_address(state,v)` — existing-style nonnegative min-zero address in one selected three-axis slice;
- `slice_sheet_bit(state,v)` — the one full-state bit omitted by ordinary slice endpoint observation;
- `from_slice_chart(v,address,bit)` — full-state reconstruction;
- `change_slice_chart(...)` — exact integer chart transition;
- `rotate_state(state,perm)` — intrinsic S4 positive-axis permutation symmetry.

## Exact return criterion

For `z=(AB,AC,AD,BC,BD,CD)`, define

- `M1=AB+CD`;
- `M2=AC+BD`;
- `M3=AD+BC`.

Then the path returns to the starting Cell iff

`M1=M2=M3`

and one/every K4 triangular-face sum is even, e.g.

`AB+AC+BC == 0 mod 2`.

## Type boundary

Do not replace Path-formal or Weighted-BRC state by `CellState` when future observers need path identity, multiplicity, branch weight, line/component trace, history, or signed chart holonomy. The endpoint quotient is legal only for the terminal-Cell observer.

## Verification

- `scripts/check_x6_native_universal_completion_v2.py` independently reconstructs the endpoint normal form, S4 action, Smith determinantal divisors, return criterion and BRC type regressions without importing this module.
- `check_x6_cell.py` exercises the reusable module, including 5,000 exact one-slice-address-plus-bit roundtrips and exhaustive return testing on `[-2,2]^6`.
