# R061 Stage 0 — Forward / Reverse Fiber Audit

## Formal diagram

For every formal shuffle word `w`:

`w -> End_formal(w)=(a,b) -> N=a^2+b^2 -> sqrt(N)`.

Conversely:

`sqrt(N) -> D_N -> disjoint union of Lambda(a,b)`.

At the formal level these are fiber-consistent:

- every word returns to the same coordinate branch from which it was lifted;
- several coordinate decompositions of one `N` remain distinct direction
  branches;
- several noncommutative words above one coordinate pair remain distinct path
  candidates;
- no one-to-one inverse is required.

Examples:

- `N=25` keeps axis branches and the `(3,4)/(4,3)` direction branches;
- `N=65` keeps both inequivalent nondegenerate branches up to swap;
- `N=3` has empty coordinate and formal path fiber.

Thus:

`FORWARD_REVERSE_FIBER_CONSISTENCY_PASS_FORMAL = true`.

## Native obstruction

The native path-to-endpoint map cannot yet be identified with `End_formal`:

1. the origin is not a cell;
2. the first incident cell/address affine anchor is unspecified;
3. third-family/cross-sector nearest-neighbor realizations are omitted by the
   two-positive shuffle;
4. no complete native `Pi_cell` or canonical path class is defined.

Therefore there is no proved commutative diagram

`native path -> absolute center address -> native length`

that inverts the proposed scalar lift on the same native path fiber.

`FORWARD_REVERSE_FIBER_CONSISTENCY_PASS = false`.

The strongest validated inverse is fiber-valued only at the
`scalar <-> coordinate <-> formal word` levels.
