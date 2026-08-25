# CBRC F5B — Positive-Separation Regularity Axiom Admission Return

Status: `FINAL_FROZEN`
Researcher-ID: `EM-CBRCF5B-B8E421`
Task-ID: `RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION`
Owner branch: `research/cbrc-f5b-positive-separation-regularity-axiom-admission`
Taskbook source: `11c5c651df54cf0117f936d5dbf421e37b9b7a34`

## 1. Source freeze

Only the taskbook-whitelisted mathematical sources were used:

1. `research_inputs/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_PACKET_20260825.md@1cdfb6b1f8fb0806507c9a4ce72278461246034b`;
2. `driver_reviews/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_DRIVER_REVIEW_20260823.md@54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`;
3. `driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842`.

No downstream mathematical source was read.

## 2. Canonical formulation

At the accepted finitely generated torsion-free-rank-one scope, use the canonical retraction

`pi : C -> Z e`

with finite kernel `T=ker(pi)`. Define

`f(n)=min { q(z) : pi(z)=n e }`.

The admitted local rule is

`FREE_PROJECTION_ZERO_SEPARATION`:

`pi(z) != 0 => q(z)>0`.

This is P1 intrinsically, without choosing a splitting.

## 3. P0–P5 lattice

For finite `T`:

`P0 => P1 <=> P2 => P3`.

The strict converses fail as follows:

- `P1 !=> P0`: on `C=Z e + Z/2`, let all nonzero free-coordinate states have positive scalar while the nonzero pure-kernel state has scalar zero.
- `P3 !=> P1`: on `C=Z e + Z/2`, keep the embedded old copy positive but give a nontrivial torsion-labelled point in a nonzero free fiber scalar zero.

The equivalence `P1 <=> P2` uses finiteness: pointwise positivity on a finite fiber is equivalent to positivity of its minimum. Without finite attainment, P1 need not imply a positive infimum.

P4/P5 are typing-dependent rather than pure carrier predicates. At the already admitted A0 elementary old-refining scope:

- `P1 => P5`;
- `P4 => P5`;
- `P0 => P4 => P5`.

Unrestricted P1 and P4 are incomparable because P1 deliberately leaves pure-kernel active states unconstrained, while P4 need not constrain inactive nonzero free-fiber states. P3 is likewise insufficient to control P4/P5 in the presence of nontrivial fibers.

Freeze:

`F5B_POSITIVE_SEPARATION_REGULARITY_LATTICE_CLASSIFIED`.

## 4. Weaker proof-side intermediates

Two strictly weaker global envelope conditions were discovered:

`P6_ZERO_SUBGROUP_EXCLUSION`:
for every `p != 0`, some positive multiple `k p` satisfies `f(kp)>0`.

`P7_ENVELOPE_APERIODICITY`:
`f` has no nonzero period.

They satisfy

`P2 => P6 => P7`

strictly.

Both are enough to contradict the accepted F4 conclusion that every non-signed-permutation free block forces a nonzero period. They are not admitted as working-extension axioms because they are global arithmetic shape conditions on the already-formed envelope rather than local scalar-separation semantics. P7 can even allow an entire nonzero subgroup of free fibers to be scalar-zero.

Thus:

- weakest proof-side contradiction condition can be weaker than P2;
- weakest serious local positive-separation rule among the issued candidates is the finite-scope P1/P2 equivalence class;
- the intrinsic local representative is P1.

## 5. Minimal F4 obstruction regularity

The exact F4 contradiction step is:

- non-signed-permutation free block gives a nonzero period `p` of `f`;
- `f(0)=0`;
- therefore `f(p)=0`;
- P2 gives `f(p)>0`.

So P2 is exactly sufficient for the accepted finite-torsion F4 mechanism, and P1 is equivalent to it at the issued scope.

P0 is unnecessarily strong because pure-kernel positivity is not used. P3, P4 and P5 are insufficient because none controls every nonzero free fiber.

Freeze:

`F5B_MINIMAL_FREE_BLOCK_OBSTRUCTION_REGULARITY_CLASSIFIED`.

## 6. Exact insufficiency witness below P1/P2

Take `C=Z e` and the period-6 scalar

`h=[0,1,1/4,3/4,1/4,1]`.

Set `q(n e)=h(n mod 6)` and

`A=[[-4,-3],[-3,-2]]`.

Then `det(A)=-1`, `A` is not a signed permutation, and exact enumeration of all 36 residue pairs gives

`q(x)+q(y)=q(-4x-3y)+q(-3x-2y)`.

For the elementary input `(e,0)`, both old projections `-4,-3` are nonzero, so A0 holds; the two output scalars are `1/4` and `3/4`, so P5 holds. But `q(6e)=0`.

Hence:

`A0 + P5` is insufficient, and elementary P4 is likewise insufficient when only those outputs are typed active.

## 7. Rank-one closure with admitted A0

Assume P1 plus the already admitted A0.

1. P1 gives P2 because the torsion fiber is finite.
2. F4 then forces every rank-one free quotient block to be a signed permutation.
3. A signed-permutation first column has exactly one nonzero old coordinate and one zero old coordinate.
4. A0 requires both elementary old-refining output projections to be nonzero.
5. Contradiction.

Therefore:

`A0 + FREE_PROJECTION_ZERO_SEPARATION + BALANCED_REVERSIBLE_CONSERVATION => torsion_free_rank(C) >= 2`.

Status:

`WORKING_EXTENSION_THEOREM`.

No rank-two carrier is constructed or classified.

Freeze:

`F5B_WORKING_EXTENSION_RANK_ONE_CLOSURE_CLASSIFIED`.

## 8. Conservativity / ontology cost

P1 is preferred over P0 and over an envelope-minimum axiom because:

- pure-kernel states `pi(z)=0` may still have scalar zero;
- exact signed cancellation remains legal, including recoalescence to coefficient zero with `q(0)=0`;
- canonical Path/N/Boolean objects are unchanged;
- the rule uses only the canonical retraction `pi`, not a chosen splitting;
- finite torsion is needed only for the current P1-to-P2 minimum proof, not to state P1;
- future enrichments incur only the local obligation that a state with nonzero old projection cannot have scalar zero.

Freeze:

`F5B_POSITIVE_SEPARATION_CONSERVATIVITY_AND_ONTOLOGY_COST_CLASSIFIED`.

## 9. Checker evidence

Exact pushed checker:

`scripts/cbrc_f5b_validate_positive_separation_regularity_admission.py`

Git blob:

`719a7f1820e4b6c9d495e2cdb83e77af4c6c64f1`

Byte-identity verification: `PASS`.

Execution:

- result: `PASS`;
- check count: `101`;
- mismatch count: `0`;
- checker SHA-256: `8a472298db0b9270213f2deaf4180cadbe4fb8bb4c1d5fcecb6f2deaa7157895`;
- deterministic digest: `668c57c8da749b33eac111420644ee27739cacd267b83b9903edfb7e0ab53f7e`.

The bounded checker is regression evidence only; the arbitrary finite-torsion implication and rank-one closure are theorem proofs above.

## 10. Final admission verdict

Primary verdict:

`F5B_ADMIT_RESTRICTED_FREE_FIBER_POSITIVITY_ONLY`.

Admitted working-extension axiom:

`FREE_PROJECTION_ZERO_SEPARATION : pi(z) != 0 => q(z)>0`.

Epistemic status:

`WORKING_EXTENSION_AXIOM`.

Explicit non-status:

`FREE_PROJECTION_ZERO_SEPARATION != CANONICAL_FOUNDATION`.

Hard target:

`POSITIVE_SEPARATION_REGULARITY_AXIOM_ADMISSION_STATUS_CLASSIFIED`.

Leak audit:

`TARGET_LEAK_AUDIT_PASS`.

Stop condition:

`F6_NOT_OPENED = true`.
