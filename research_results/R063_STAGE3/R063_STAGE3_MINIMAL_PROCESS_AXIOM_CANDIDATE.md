# R063 Stage 3 — Minimal Process Law Candidate

Status: `ISOLATED / N1_DERIVED_OPERATIONAL / NOT_N0_PROMOTED`
Researcher-ID: `EM-R063S3-F1CF9D`

## Candidate law: C4 signed interaction tensor

Minimal closed multiplicative carrier found in Stage 3:

1. each source path retains its finite ordered position chain;
2. positions carry `C4={+X_i,+X_j,-X_i,-X_j}` labels;
3. multiplication forms the Cartesian product of position posets;
4. each interaction label is the mod-four sum of its two input labels.

The positive-positive restriction reproduces the uniquely derived four-entry Stage 3 interaction table. The full `C4` closure is required for repeated multiplication and unit equivariance.

Cancellation and ordered orientation are **not** part of the associative primitive. They are downstream reduction/readout operations. This separation is what preserves process associativity.

## Ingredient classification

| ingredient | verdict | reason |
|---|---|---|
| four-entry pairwise interaction table | `DERIVABLE` | uniquely forced by Stage 2 bilinear law |
| pairwise interaction rectangle/product poset | `SUFFICIENT_WITH_OTHERS` | carries every pair occurrence and both source orders |
| signed output channel | `NECESSARY` | `X_j tensor X_j=-X_i` cannot live in positive-letter paths |
| full `C4` unit label state | `NECESSARY` | three-label binary alphabet is not closed under repeat/unit transport |
| count cancellation | `DERIVABLE` | quotient by opposite signed counts; exact normal form |
| positional cancellation selector | `REDUNDANT` | all-normal-form relation is canonical; any selector adds arbitrary choice |
| source position/order inheritance | `NECESSARY` | removing it erases the W2 source-sensitive relation |
| Gaussian factorization provenance | `REDUNDANT` for this lift | Stage 3 begins after a component path/root has already been fixed |
| ordered orientation state | `SUFFICIENT_WITH_OTHERS` only for ordered readout | not needed for unit-equivariant process multiplication |

## Semantic status

This is a process law **derived to realize a frozen higher-layer multiplication**, not a proof that the Enterprise N0 substrate already contains this operation. Under `native_semantics_admissibility.json`, its current strongest admissible type is

`N1_DERIVED_OPERATIONAL`.

A future native promotion would require a separate construction/invariance certificate from the declared N0 substrate and is not authorized by Stage 3.

`MINIMAL_SIGNED_INTERACTION_PROCESS_LAW = C4_LABELLED_CARTESIAN_POSITION_TENSOR`.
