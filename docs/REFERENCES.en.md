# Source Index and Neighboring Prior Work

## 1. Canonical reference system

The old free-form bibliography has been replaced by a provenance system.

- `sources.json` is the canonical machine-readable bibliography and records how each source is used.
- `lineage.json` records which Enterprise Math component each source affects and whether the relationship is adoption, combination, reinterpretation, contrast, or inspiration.
- `docs/PRIOR_ART_AND_NOVELTY.en.md` is the human-readable explanation of the intellectual lineage and provisional novelty boundary.
- `docs/CITATION_POLICY.en.md` defines how new references must be added and maintained.

Stable source citations use `[SRC-*]` identifiers.

## 2. Main prior-art families

The current registry covers:

- integer square root and order-defined floor division;
- Galois adjoints and closure/interior operators;
- fixed-point, scaled-integer, block-floating, and exact-real arithmetic;
- exact finite representations of algebraic numbers;
- finite-information critiques of physical real-number ontology;
- discrete spacetime and causal sets;
- logical irreversibility and reversible computation;
- Mori-Zwanzig projection and coarse-graining;
- preimage entropy and folding entropy;
- forward dynamical semigroups in open quantum systems.

The full verified bibliography is in `sources.json`; this file deliberately does not duplicate every URL.

## 3. Citation rule

A source is cited because it supports a specific lineage statement, not because it is vaguely related.

The main prior-art map must state:

1. what the earlier work actually established;
2. what Enterprise Math directly reuses;
3. what Enterprise Math changes or rejects;
4. what must not be attributed to Enterprise Math as an invention;
5. whether the remaining project claim is mathematics, synthesis, or physical hypothesis.

## 4. Update rule

New material prior art must update the source registry and lineage graph in the same research change.

If a new source narrows a novelty claim, narrowing the claim is mandatory.

Finding earlier work is counted as progress because it makes the project more precise and prevents false originality claims.
