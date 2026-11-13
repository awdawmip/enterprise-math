# R130.2 — Persistent exact random-access to S23 event signatures

Date: 2026-11-13 (Asia/Shanghai). Same auxiliary S23 scope and frozen scientific input as R130.1; R129 predecessor `ddef5881c7e9996fbc08c6f48cd0c387606d035d`.

## Theorem

Given R130.1's lossless sparse event log for `m>=1` bits and `q` ordered rational cut positions, there is a persistent binary indexed state structure satisfying:

- preprocessing additional to the sparse log: `O(m+U log(m+1))` binary-node construction operations, where `U=Σ_c(|D_cut(c)|+|D_right(c)|) <= 2 J_total`;
- storage: `O(m+q+U log(m+1))` nodes/references;
- exact query `S_i(theta)` for rational `theta∈(l,h)`: `O(log(q+1)+log(m+1))` comparisons/tree steps;
- exact entire word reconstruction: `O(m)` output bits plus a balanced-tree traversal.

Each event has two version roots, `root_cut(c)` and `root_right(c)`, both obtained by applying their respective sparse replacements **to the same pre-cut left root**. A cut is not used as the base for the following open cell. Equal parameter comparisons select the singleton root; strict intermediate comparisons select the preceding right-open root; parameters before the first cut select the initial root.

This supplies a random-access exact bit oracle with event-time provenance and half-open-boundary fidelity. It does not assume that a compact log compresses all distinct fully materialized words into smaller-than-output space.

## Proof

Build a balanced binary tree over the m initial bit values. A point replacement creates a new immutable root by copying at most `ceil(log2 m)+1` nodes along that index's path and sharing every untouched subtree. For each cut, apply `D_cut` and `D_right` separately to the same left-open root, then make the right root the current one. By R130.1 both versions represent exactly the corresponding singleton/open signatures. Inductively every stored version is correct. The ordered cut array supports binary search for the version applicable to a query theta; descent along the tree recovers bit i. Summing point-update costs and maintaining two roots per cut proves the bounds.

## Reproducibility

`check_r130_indexed.py` imports the exact `check_r130.py` sparse oracle and implements immutable tuple-tree path copying. It tests every bit of 377110 query positions/coordinates across 104 instances (100 seeded random, four adversarial), including all singleton roots and all open-cell midpoints; the report includes 33066 persistent bit replacements, equal to the actual nontrivial deltas. In the m=64 Farey case, 1227 cut positions, 7688 replacements, and 158720 bit queries were checked against independent complete-word evaluation. Result: `R130_PERSISTENT_INDEX_PASS`.

Finite verification validates the implementation on the declared samples; the theorem's general bounds follow from immutable point-update induction.

## Next

Add exact coefficient-sensitive bit-cost and runtime benchmarks, compare persistent indexing with R127 modular ILP / R126 three-integer feasibility when the slopes have hundreds of digits, and explore gcd-quotiented phase indexing. Preserving named cuts and exact endpoint words remains part of the representation contract.
