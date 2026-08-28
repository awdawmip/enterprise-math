# A3 Recursive Shell Alignment Tomography — Research Return

Task-ID: `RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY`
Publication-ID: `TP2-78C59019AE494DF41F65`
Researcher-ID: `EM-A3SHELL-19C7D4`
Claim-ID: `chatgpt-a3shell-20260828-1328-19c7d4`

Verdict: `PASS / EXACT_FINITE_SHELL_TOMOGRAPHY_PACKAGE / RADIAL_DEFECT_IS_RELATION_VALUED / COMPOSE_EXISTING_TOOLS / NO_FOUNDATION_PROMOTION`

## Frozen results

For the A3 carrier `Lambda3 = {x in Z^4 : sum x_i = 0}` with radius `max |x_i|`, the exact ball and shell counts are

`|B_n| = (16 n^3 + 24 n^2 + 14 n + 3)/3` and `|S_n| = 16 n^2 + 2`.

The first ball counts are `1,19,85,231` and the first shell counts are `18,66,146`.

The signed permutation action `R_sigma = sgn(sigma) P_sigma` is a faithful 24-element S4 action preserving every shell and having determinant +1 on the three-dimensional carrier.

For the pointer target `a_n=(n,-n,0,0)`, the residual stabilizer is exactly `H={e,(1 2)}`. Every nonempty alignment family is one left coset `H g`. A two-marker rigid target has trivial stabilizer and therefore unique alignment. The one-marker state `(n,n,-n,-n)` is unreachable from the pointer target.

For the task-local depth-d prefix move model, every move fixes `B_(n-d)` pointwise. Thus depth 1 cannot alter the exact `B_(n-1)` interior. Depth 2 is the first coupled prefix semantics capable of changing `S_(n-1)` while preserving `B_(n-2)`.

For aligner cosets `H g_n`, the choice-independent radial defect is the double coset represented by `g_n g_(n+1)^(-1)`. It is invariant under changing alignment representatives and under a common passive frame change. The depth-2 scale square commutes on the residual-H quotient for every state exactly when this relative class is the identity double coset.

For `H={e,(1 2)}`, there are exactly seven double cosets. The stabilizer is not normal, so compressed radial defects are not a group. The smallest explicit witness is `C2*C2={C0,C2}`.

The exact three-radius prototype uses aligner representatives `e,(2 3),e`. The shell markers are `(1,-1,0,0)`, `(-2,0,2,0)`, `(3,-3,0,0)`. Both adjacent compressed defects are `C2`, but the exact endpoint defect is `C0`. This proves that double-coset compression loses intermediate information and therefore needs relation/BRC-valued composition.

For the planar slice `L4={x_4=0}`, the exact ball count is `1+3 n(n+1)` and shell count is `6n`. The residual element `(1 2)` preserves L4 but reverses its two-dimensional orientation. Therefore orientation-sensitive NollM/Eisenstein slice data cannot be erased by the pointer-target stabilizer without losing semantics. Slice index, orientation, and layer/carrier tags must be retained, or the aligned observation remains a stabilizer orbit.

## Replay package

Full proof package: `research_artifacts/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY/A3_SHELL_ALIGNMENT_TOMOGRAPHY_RESULT_20260828.md`

Frozen certificate: `research_artifacts/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY/prototype_certificate.json`

Deterministic checker: `scripts/check_a3_recursive_shell_alignment_tomography.py`

The checker independently verifies all stated finite counts, group laws, stabilizers, shielding, ambiguity, double-coset classes and product witness, the three-radius defect example, and the A2 orientation reversal. When the Enterprise Math package is importable, it also cross-checks the finite action through T7 `finite_symmetry`.

## Tool verdict

`COMPOSE_EXISTING_TOOLS`

The package uses the existing scale enumeration, bounded certificate, collision, precision/refinement, operation-safe quotient, finite symmetry, relation-observable, holonomy, and BRC tool families. The prefix-shell move is task-local. No new shared tool family is justified.

## Semantic boundary

The shell radius, boundary target, active prefix move semantics, word complexity, A2 slice orientation, and any future infinite completion remain operational/readout structures. No physical-world or Foundation claim is made.

## Open residue

`GENERAL_COUPLED_GENERATOR_RADIAL_RELATION_COHERENCE_OPEN`

The next genuine theorem problem is to classify when a more general family of coupled layer moves admits an associative relation/BRC or groupoid lift of the scale defects, and to characterize the first radius where no operation-safe quotient makes the two scale-normalization routes agree. Enlarging the finite radius census alone is not a successor justification.
