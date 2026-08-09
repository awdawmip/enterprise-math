# P022 — Two-Sided Event-Driven Repair of Coordination History

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE REPAIR / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: coordination-history drift reconstruction; excursion orientation repair  
Cross-route relevance: P018/P023 state-dependent repair, witness identity and symmetry breaking

## 1. What coordination history still forgets

Whole-shell coordination history recovers at every radius the unordered absolute drift pair

\[
P_q=\{|\delta_q^+|,|\delta_q^-|\}.
\]

To reconstruct the two **labelled signed** microscopic stacking windows, two different hidden freedoms remain:

1. orientation of each nonzero excursion of either absolute channel;
2. which labelled side takes which branch when two equal absolute channels split.

These freedoms are event-driven.

## 2. Zero-departure events

Whenever one absolute channel is at zero and the next step leaves zero, a new signed excursion begins.  Its sign can be chosen independently.

Let

\[
E(P)
=
\sum_{q=1}^{N}
\#\{\text{zero entries of }P_{q-1}\},
\]

with

\[
P_0=\{0,0\}.
\]

This equals the total number of one-sided excursions across both labelled channels, independent of how side labels are reconstructed.

## 3. Diagonal-split events

Suppose

\[
P_{q-1}=\{d,d\}.
\]

If

\[
P_q=\{d-1,d+1\},
\]

then the unordered observation no longer says which labelled side moved inward and which moved outward.

One binary side-label decision is required.

Define

\[
\boxed{
B(P)
=
\#\{q:P_{q-1}=\{d,d\},\ P_q\text{ unequal}\}.
}
\]

Once the channels are unequal, their labels are forced by nearest-neighbor continuity until they meet again.  Therefore no additional side-label bit is needed between diagonal meetings.

## 4. P022-TR01 — ordered absolute histories form a `2^B` fiber

At every diagonal split choose one bit specifying which labelled side takes the larger successor.

Between split events the labelled continuation is forced.  Distinct choices produce distinct ordered absolute-history pairs.

Hence

\[
\boxed{
\#\{\text{ordered absolute realizations of }P\}=2^{B(P)}.
}
\]

## 5. P022-TR02 — exact microscopic fiber size

For each fixed labelled absolute realization, the one-sided excursion theorem gives one orientation bit per excursion.  The total excursion count is the unordered-history invariant `E(P)`.

Therefore

\[
\boxed{
|O^{-1}(P)|
=2^{E(P)+B(P)}.
}

Equivalently, the exact repair-bit dimension is

\[
\boxed{r(P)=E(P)+B(P).}
\]

The required repair is:

- one **orientation bit** for each zero-departure excursion;
- one **side-label bit** for each diagonal split.

No per-layer bitstream is required.

## 6. P022-TR03 — sharp repair range

For every nonempty horizon `N`,

\[
\boxed{2\le r(P)\le N+1.}
\]

### Lower bound

At the first step both zero channels leave zero, so `E>=2`.

The bound is attained when the two channels remain equal and never return to zero before the horizon, producing no later excursion or split event.

### Upper bound

A one-step repair cost can be `2` only when the previous state is

\[
\{0,0\}.
\]

Every later occurrence of `{0,0}` must have been entered from `{1,1}` by a step with repair cost `0`.  So every later excess `+1` above a one-bit-per-step baseline is paired with a preceding deficit `−1`.  Only the initial departure has no compensating predecessor.

Hence total cost is at most `N+1`.

The alternating history

\[
\{1,1\},\{0,2\},\{1,1\},\{0,2\},\ldots
\]

attains the upper bound.

## 7. Aggregate split load

The diagonal-split contribution can also be counted exactly across all `4^N` ordered microscopic windows.

At prefix time `t>=1`, a split requires the two signed walks to have equal nonzero absolute magnitude.  The number of ordered length-`t` prefix pairs with that property is

\[
2\binom{2t}{t}
-
2\mathbf 1_{2\mid t}\binom{t}{t/2}^2.
\]

Exactly two of the four next-step pairs split the absolute magnitudes.  The remaining suffix is arbitrary.  Therefore the total diagonal-split bit load is

\[
\boxed{
D_N
=
\sum_{t=1}^{N-1}
\left[
\binom{2t}{t}
-
\mathbf 1_{2\mid t}\binom{t}{t/2}^2
\right]
4^{N-t}.
}
\]

Combining this with twice the one-sided excursion repair load gives the exact aggregate two-sided repair load.

## 8. Precision consequence

The hidden information of a coordination history is generated at two geometric boundaries:

- the **zero boundary**, where orientation is born again;
- the **diagonal symmetry boundary**, where side identity becomes ambiguous again.

Thus precision repair is tied to symmetry-breaking events, not uniformly to elapsed horizon.

This is a concrete finite model for the broader principle:

\[
\boxed{
\text{hidden state should be retained where future semantics branch, not everywhere.}
}
\]

## 9. Executable assets

- `src/enterprise_math/p022_barlow_two_sided_repair.py`;
- `tests/test_p022_barlow_two_sided_repair.py`;
- `src/enterprise_math/p022_barlow_repair_polynomial.py` for the induced fiber-dimension distribution.

Direct finite tests group all ordered microscopic word pairs through short horizons, verify `2^(E+B)` exactly, and reconstruct all microscopic pairs from the declared event bits.
