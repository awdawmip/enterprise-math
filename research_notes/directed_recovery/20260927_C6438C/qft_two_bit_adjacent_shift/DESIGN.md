# First bounded adjacent-bit shift execution design

Status: PRE_EXECUTION / CODE_ONLY. No scientific import or run occurred while
preparing this design, proof, observer and checker. Python compilation checks
syntax only. A separate result note will record any later actual execution.

## Frozen scientific inputs

- Proof `ADJACENT_SHIFT_REDUCTION.md`: SHA256
  `96757c3624c69bf3ec1e313504f56bb6099d1a79e47032813084b19340c272ad`.
- Observer `adjacent_shift.py`: SHA256
  `bee8a702062dfb16a75139a63b6c52b9451a02834a5b3033f5d52fcaebff9c6e`.
- Checker `check_adjacent_shift.py`: SHA256
  `6a7969e779800652a6143354bcbe732b670cb90128781e2f1243db91d1e6a9fe`.
- Direct one-bit source: `3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521`.
- Existing degree-three floor source:
  `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`.

The observer calls the frozen direct single-bit progression and adds the
proved shifted-boundary correction through two ordinary floor tables. Each
orientation therefore uses at most four tables. This prototype does not use
the recent point/setup shortcuts, does not claim to be the fastest route,
and does not depend on the new degree-five runner. Its purpose is to extend
the exact executable domain to non-top adjacent selected bits with arbitrary
supplied positive R.

## One bounded run

Execute only after independent static review and an actual source-state
startup guard for activity RA-CAAAC604CB513AEA8BBC1DFC. The first successful
or failed execution artifact is exclusive; it must not be overwritten by a
second attempt. Any corrected successor gets new source bindings and a new
evidence location. Directory paths here are restoration locators, not
restrictions on what a future conversation is permitted to do.

Use six tuples (g,ell,k,R), all r in [0,R):

    (3,0,1,5), (4,0,1,5), (4,1,2,6),
    (4,1,2,9), (3,0,1,11), (4,0,1,1).

These yield 37 scalar values, all with k<g-1. Each tuple uses a fresh
production observer, then one new actual typed ordered-pair histogram, then
a fresh serialized-certificate replay. The six histograms comprise 1,152
ordered pairs. The pair comparator function is copied verbatim from the
hash-pinned aligned checker and AST source equality is checked; that older
checker is never imported or executed. The six tuples are not a rerun of
the predecessor's highest-bit grid or the earlier aligned grid.

Production, comparator, positive replay, every paid negative replay and the
single shared native full-adder catalog chronology are counted separately.
There is no ordinary numeric reference, host exponentiation for scientific
answers, trigonometric/ideal-phase propagation or presumed order oracle.
All signed arithmetic and all comparator bit/modulus observations use the
actual typed runner. Public loop indices, comparisons of observed results,
source hashes, JSON and cost accounting remain host bookkeeping.

The grid includes ell=0 and ell=1, R=1, odd and even R, R>L, negative outputs,
empty orientations and the half-modulus double orientation. Full pairwise
agreement checks the underlying finite interval, including windows shorter
than V; this is not a claim that each proof endpoint has a separate explicit
point-query receipt. No highest-bit timing or cost advantage is presumed.

## Rejection and preservation

Twelve invalid-input controls cover strict booleans/types, invalid bit
positions, nonadjacent masks, bad R/residue and nonunit stride; each must
reject before work. After the first valid production query, insert one
nonadjacent input, require unchanged detached snapshots, and complete the
original remaining grid with that same observer. The duplicate snapshots
overlap production and are not separately billed.

Fourteen certificate tamper controls cover base and correction coefficients,
correction offsets/table outputs/terms, the reused displacement sum, dropped
half-modulus orientation, raw normalization, output, a paid valid prefix
followed by an invalid mask, and four early structural/source/type failures.
Nine full honest replays and one paid-prefix replay must be preserved before
their rejection, while the four early controls must have zero work. The
serialized semantic comparator excludes only the declared native cache-call
delta. It does not omit scientific values, signs, sources or cache records.

A rejected invalid input leaves an observer reusable. An exception after a
valid request starts marks the observer terminal and preserves inflight/raw
evidence; export cannot turn it into a complete certificate. This bounded
design does not inject an arithmetic interruption, so that terminal behavior
is source reviewed, not empirically claimed as a tested recovery scenario.
If an unexpected failure occurs, the checker retains every available current
observer/comparator/replay snapshot, completed output, control attempt and
native call before exiting. Import or constructor failure before object
return cannot be reconstructed and must be reported as such.

## Delivery and claim boundary

Read the full saved raw with separate author and shared-context peer readers
before reporting execution success. Bind every signed result to typed
operations, retain all comparator pairs and outer correction references,
and report all paid work. A summary-only review is insufficient. Publish
source/proof/checker/raw chunks and exact restoration metadata, verify full
immutable readbacks, then original-byte Drive backup, native activity and
knowledge journal. P000 and formal admission are unchanged.

At most eight fixed-degree top-level tables gives a symbolic polynomial-bit
algorithm for this adjacent-bit scalar unit. It does not establish practical
scaling from these small fixtures, arbitrary separated masks, full matrix
chronology, unknown-order recovery or complete Shor sampling. The parent
research remains open after this bounded execution.

Global-Knowledge-Sync: main@52978d9 / GLOBAL_KNOWLEDGE_V1
