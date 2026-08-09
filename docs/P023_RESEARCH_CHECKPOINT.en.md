# P023 Research Checkpoint — Composition-Safe Collapse

Status: `CHECKPOINT / ACTIVE RESEARCH`  
Date: 2026-08-09

## Retained core

The research line retains the following generic primitives:

1. a finite fine state space;
2. an explicit coarse quotient / observation partition;
3. the operation(s) and observations the coarse state is required to support in the declared future language;
4. fiber constancy / congruence as the safety criterion;
5. minimal partition refinement when that criterion fails;
6. safe-precision selectors as monotone reductive idempotent maps on the finite lattice of equivalence relations.

No metric error, probability, entropy, continuum limit, or physical interpretation is required for the core theorem.

## Current canonical theorem stack

- T01: fiber constancy iff an observable descends through a quotient;
- T02: `(old coarse label, failed future observable)` is the coarsest one-step repair;
- T03–T07: finite deterministic future refinement stabilizes to the coarsest transition-compatible refinement;
- T08: exact quotient is compatible with every floor-precision quotient;
- T09: same-space multiple collapse descends through floor precision iff the two integer parameters are comparable by divisibility;
- T10–T14: finite closure extends to a finite family of deterministic operations, with operation-word future semantics;
- Stage 2: the safe-precision interior is the largest compatible relation below the supplied precision relation; uniform divisibility scales need not be closed under minimal repair, so localized bounded detail is a legitimate precision object;
- Stage 3 / Supplement 07: repeated fixed safe-selector words stabilize to the joint safe precision for the union of their operation requirements; one-pass selector order may matter while stable safe precision does not.

## Independent bounded checks

Outside repository CI, the mathematical reference definitions were independently reconstructed and exhaustively checked over:

- 4330 deterministic one-operation / binary-observation systems of size at most four for stable compatibility, future-depth semantics, and coarsest compatible refinement;
- 5832 two-generator / binary-observation systems on three states for common compatibility, operation-word semantics, and coarsest common refinement.

No counterexample was found in those bounded domains.

These checks are supporting evidence, not substitutes for proof or repository CI.

## Ownership split after P024

P023 remains the **generic** theory.  It should not absorb every arithmetic specialization of a future-safe quotient.

P024 (`docs/P024_ACTION_LANGUAGE_PRECISION.en.md`) owns the one-dimensional additive/ordered-threshold specialization:

- integer translation action monoids;
- reachable boundary orbits `B-M`;
- one-sided numerical-semigroup holes;
- exact gcd over-refinement defect;
- conductor-localized irregular boundary layers;
- genuine two-sided group completion;
- automatic subgroup completion after finite cyclic periodicization.

The boundary is therefore:

```text
P023: which equivalence relation is future-safe / coarsest?
P024: for integer translations + ordered threshold observations,
      what arithmetic geometry does that relation have?
```

E001 Boolean-contact and E002 actuation results may use P024 as an arithmetic specialization, but they retain ownership of their own engineering/physical semantics.

## Current next theorem target

The generic P023 route should now move beyond the additive threshold case already factored into P024.  High-value targets are:

1. state-dependent operation families whose safe relation cannot be reduced to a state-independent additive monoid;
2. efficient canonical representations of nonuniform/localized safe precision without falling back to arbitrary database-like labels;
3. formal abstraction shared by P019 collapse-word stabilization and P023 selector-word stabilization;
4. interaction between multiple independent safe-precision requirements when their minimal repairs live in different structured state families.
