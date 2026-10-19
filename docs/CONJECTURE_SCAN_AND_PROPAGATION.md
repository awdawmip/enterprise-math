# Conjecture Scan and Dependency Propagation

Status: `ACTIVE_CANDIDATE_CONTROL`
Effective: `2026-09-07`
Parent policy: `docs/CONJECTURE_ASSET_GOVERNANCE.md`
Machine policy: `conjecture_scanner_policy.json`

## 1. Why this exists

Conjecture governance is useful only if unproved claims are actually discovered and if their epistemic state propagates through later research. This document turns the standing historical/closeout duty into an operational scan-and-revalidation loop.

The scanner is deliberately conservative: it should increase registry completeness without increasing epistemic certainty.

## 2. Intake pipeline

For every research closeout and every historical scan generation:

1. Collect candidate markers from unresolved sections, smallest-successor/frontier fields, empirical regularities, proposed laws, candidate tools, no-claim boundaries and prior-art boundaries.
2. Split proved substrate from the unproved residue.
3. Ask whether the residue asserts a direction. A directionless question is not a conjecture.
4. Freeze the narrowest useful falsifiable statement or reusable tool contract.
5. Record its exact scope, evidence envelope, dependencies, falsifier and promotion target.
6. Classify the hit as `A_REGISTER`, `B_FREEZE_THEN_REGISTER`, `C_REVIEW_ONLY`, or `D_EXCLUDE`.
7. Record excluded high-signal hits too, so later scans do not repeatedly mistake them for conjectures.

## 3. High-signal false positives

The following often contain words such as predictor, experiment, frontier or theorem, but must not be registered merely because they look research-like:

- an exact theorem plus a benchmarked implementation;
- a proved/certified predictor whose runtime crossover is empirical;
- a failed compression/routing idea with no surviving restricted law;
- a finite observation with no precise asserted extension;
- an open question with no asserted direction;
- a tool whose mathematics is established and only implementation/reviewer acceptance is missing.

The September 7 BRC multiplier chain supplies canonical examples: exact pairwise transport, exact 2-adic reductions, certified table-free/deep-tail predictors and the staged square-gap CRT cascade are ordinary proved/certified research assets, not conjectural tools. Their performance measurements remain empirical without infecting mathematical correctness.

## 4. Active-task priority

A conjecture that already drives an active formal task receives scan priority even if it originated outside Enterprise Math. The registry entry should normally freeze the internal reduced form actually used by the project rather than duplicating every broader external formulation.

Example: the Enterprise BRC inert-plus half-coupling route reduces the relevant plus-class specialization of Zhi-Wei Sun A14(ii) to a single terminating Jacobi-jet mod-p^2 certificate. The reduced certificate is the project-facing conjecture asset; the broader published conjecture remains a provenance/prior-art reference.

## 5. Dependency taint

For any asset or research result `X`, define `T(X)` as the transitive set of unresolved conjectural dependencies used for proof, advertised soundness, or claimed scope.

- If `T(X)` is nonempty, `X` is not unconditionally proved merely because every algebraic step downstream is rigorous.
- A conjecture used only for experiment selection should be tagged `EXPERIMENT_SELECTION_ONLY`; this does not taint an independently certified output.
- A heuristic optional dependency is distinct from an essential proof dependency.

New machine-readable records should expose direct conjectural dependencies, transitive taint sources, dependency essentiality and whether downstream review is required.

## 6. State-transition propagation

### Empirical validation

`CONJECTURE -> EMPIRICALLY_VALIDATED` changes evidence and priority, not truth status. No taint clears.

### Proof

When an asset becomes `PROVED`, clear only the contribution of that asset and only over the exact proved scope. Traverse reverse dependencies and re-evaluate them. Never auto-promote a dependent that still has its own proof gap or another unresolved conjectural dependency.

### Restriction

When an asset becomes `RESTRICTED`, intersect every downstream use with the surviving scope. Any use touching removed scope is `REVIEW_REQUIRED`.

### Refutation

When an asset becomes `REFUTED`, essential dependents using the refuted scope become `REVIEW_REQUIRED` and must be re-derived, restricted, parked, superseded or refuted. Historical experimental outputs may remain, but the refuted claim may not continue as supporting evidence.

### Supersession

A replacement clears the old dependency only if it logically covers the exact scope previously used. Name similarity or stronger empirical performance is insufficient.

### Cycles

An unresolved strongly connected component cannot bootstrap itself to proof. A conjectural dependency cycle needs an external proof/falsifier or a scope restriction that breaks the cycle.

## 7. Bounded certification

Finite-domain conjectures deserve aggressive proof closure. If the frozen claim is finite and the entire domain is exhaustively checked with an exact/replayable certificate, that exact bounded claim can move directly to `PROVED`. No infinite extrapolation is imported.

## 8. Scan-generation closeout

Every scan generation should record:

- sources inspected;
- newly registered assets;
- review-only candidates;
- deliberate non-conjecture classifications;
- state changes to existing assets;
- newly discovered downstream dependencies;
- the revised prove/kill queue;
- an explicit statement that the historical scan is generational rather than claimed exhaustive unless a complete corpus traversal was actually certified.
