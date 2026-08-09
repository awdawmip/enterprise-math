# A3 Relation Quotient — Research Ownership and Continuation Protocol

Status: `ACTIVE RESEARCH OWNER NOTE`  
Branch: `research/core/relation-quotient`  
Architecture owner: `A3 — Partition relation-state algebra`

## 1. Ownership

This branch owns the reusable mathematics of capacity-weighted partition relation states.

Core object:

\[
Z_{ij}=m_jc_i-m_ic_j,
\qquad
Z=cm^T-mc^T.
\]

Its scope includes:

- partition quotient `Z' = A Z A^T`;
- partition kernel `K_A={eta:A eta=0}`;
- relation rank, relation quantum, and refinement memory;
- weighted collision observations `E^(s)`;
- exact relation precision induced by a declared future operation/observation language.

## 2. Historical P019 mixed branch

The historical branch `research/p019-minimum-precision-lattice-geometry` and its `P019_*` documents remain discovery provenance. They are not deleted, force-moved, or rewritten into a new history.

From this note onward:

- A3 does not add new `P019_MINIMUM_PRECISION_LATTICE_GEOMETRY_SUPPLEMENT_*` files;
- new reusable relation-state mathematics uses `A3_*` document names;
- historical `P019_*` assets are edited only to correct factual errors, not as the active naming line;
- canonical P019 meaning is controlled by source `main` / `PROBLEM_STATUS`; the historical relation filenames are `NAME_COLLISION_ONLY` with canonical P019.

## 3. Boundaries with other research nodes

### A2 / P023

General future-compatible quotient, operation-family closure, behavioral/future equivalence, and general minimal repair belong to A2/P023.

A3 keeps only:

- specializations to weighted relation state;
- integer partition/capacity formulas;
- A3-specific exact solvers, counterexamples, and precision consequences.

If an A3 result survives after removing weighted-relation assumptions, relay it upward to A2/P023 rather than maintaining a duplicate mother theorem here.

### A4

A4 admissible-support/correspondence is a different mathematical object. A3 and A4 interact only through proved bridges; terminology is not a merger criterion.

### A5 / P022

Lattices, primitive adjacency, balls/shells, geometry-specific filling/interpolation, and physical-space candidates belong to P022/A5.

A3 may consume geometry-derived partitions/observations, but does not continue FCC/HCP/A_p physical-geometry ontology on this branch.

## 4. Shared research mechanism

Cross-route synchronization uses GitHub Issue #82, `Research Relay: cross-branch theorem and finding bus`, not repeated whole-branch merges.

Before a new general theorem line:

1. check this branch head and source `main`;
2. read the latest relevant Relay entries for A3/A2/A4/A5;
3. classify the relation first as `SAME_MOTHER / STRICT_GENERALIZATION / SPECIALIZATION / GENERATOR / COMPOSABLE_INDEPENDENT / CONFLICT / NAME_COLLISION_ONLY`;
4. move assets only through dependency, corollary, or semantic replay when actual code/theorem movement is required.

Generalizations, bridges, important counterexamples, and new precision/witness obligations must be relayed.

## 5. Integration discipline

Long-lived divergence is allowed. Do not repeatedly merge `main` merely to make the branch look synchronized.

Canonical integration remains:

`owner branch audit -> Relay/lineage -> latest-main clean integration branch -> semantic replay of the minimal slice`.

Historical research files do not define canonical theorem status.

## 6. Current frontier

Already available:

- exact partition descent for integer linear/affine dynamics;
- observation-aware minimum exact partitions for linear observations;
- task-derived relation-rank / relation-quantum precision profiles.

The next A3-specific frontier is:

> **For predicate-controlled / piecewise integer dynamics, characterize exact quotients that may erase hidden branch identity when all branches have the same coarse output.**

The first target is a binary linear-threshold affine map on the full integer lattice, separating:

- cases where the guard must descend explicitly;
- cases where the guard may be erased because the coarse branch effects coincide;
- negative boundaries showing that exactness need not behave monotonically under intermediate partition refinement.
