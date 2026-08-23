<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F3R-BALANCED-MIXING-SURVIVOR-FAMILY-COMPLETION",
  "title": "Coherent-BRC F3R — Balanced Mixing Survivor-Family Completion",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "BALANCED_MIXING_SURVIVOR_FAMILY_COMPLETELY_CLASSIFIED",
  "next_action": "Complete the F3 current-carrier balanced-mixing survivor and scalar-family classification without selecting a downstream-looking representative; prove finite/parameterized/infinite family structure or exact underdetermination.",
  "dependencies": [
    "research/cbrc-f3-balanced-reversible-mixing-conservation-forward-classification@ce10996ca7995279770cb7c51b21cc7812f358d4",
    "driver_reviews/CBRC_F3_BALANCED_REVERSIBLE_MIXING_CONSERVATION_DRIVER_REVIEW_20260823.md@bdcee332462d52dbd3642bb3f05b2cafecaebe31"
  ],
  "source_refs": [
    "research_inputs/CBRC_F3_BLIND_BALANCED_MIXING_PACKET_20260823.md@19ed5cfdba021cf67be0f059d8e26be1fb5af3b2",
    "research/cbrc-f3-balanced-reversible-mixing-conservation-forward-classification@ce10996ca7995279770cb7c51b21cc7812f358d4"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": ["CBRC","F3R","rework","balanced-mixing","survivor-family","scalar-conservation","classification"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF3R"
}
-->

# Coherent-BRC F3R — Balanced Mixing Survivor-Family Completion

Task-ID: `RS-CBRC-F3R-BALANCED-MIXING-SURVIVOR-FAMILY-COMPLETION`

Driver: `EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Owner branch:

`research/cbrc-f3r-balanced-mixing-survivor-family-completion`

## 0. Driver routing

F3 raw work at

`research/cbrc-f3-balanced-reversible-mixing-conservation-forward-classification@ce10996ca7995279770cb7c51b21cc7812f358d4`

is accepted as an **existence checkpoint** but not as complete closure.

Driver review:

`driver_reviews/CBRC_F3_BALANCED_REVERSIBLE_MIXING_CONSERVATION_DRIVER_REVIEW_20260823.md@bdcee332462d52dbd3642bb3f05b2cafecaebe31`.

The accepted checkpoint proves that the current carrier admits at least one genuine balanced reversible additive mixing with a nonunique conserved marked-scalar family. It does **not** classify all admissible mixing classes or all scalar families required by the issued F3 taskbook.

F3R is a completion/rework stage, not a new downstream direction.

## 1. Hard target

`BALANCED_MIXING_SURVIVOR_FAMILY_COMPLETELY_CLASSIFIED`.

The stage must close the exact gaps G1–G4 in the Driver review.

Admissible final outcomes include:

1. `F3R_ONE_PHYSICAL_MIXING_FAMILY` — every admissible survivor is equivalent to one classified family;
2. `F3R_FINITE_INEQUIVALENT_FAMILIES`;
3. `F3R_PARAMETERIZED_OR_INFINITE_FAMILY_CLASSIFIED` — exact invariants/parameters classify all survivors;
4. `F3R_CURRENT_AXIOMS_STRICTLY_UNDERDETERMINE_MIXING` — a proof that no stronger honest selector exists under the frozen axioms;
5. `F3R_NO_COMPLETE_CLASSIFICATION_WITHOUT_NEW_AXIOM` — only if accompanied by an exact obstruction showing why the present data cannot distinguish declared inequivalent models;
6. `F3R_TARGET_LEAK_INVALID`.

Do not optimize for uniqueness.

## 2. Mathematical source whitelist

Before F3R raw freeze, read/use only:

1. `research_tasks/COHERENT_BRC_F3_BALANCED_REVERSIBLE_MIXING_CONSERVATION_FORWARD_CLASSIFICATION_20260823.md@bbdc0ad66c5bde1c712f2fbd80308929cd6159e6`;
2. `research_inputs/CBRC_F3_BLIND_BALANCED_MIXING_PACKET_20260823.md@19ed5cfdba021cf67be0f059d8e26be1fb5af3b2`;
3. the frozen F3 owner packet at `ce10996ca7995279770cb7c51b21cc7812f358d4`:
   - `research_reports/CBRC_F3_BALANCED_REVERSIBLE_MIXING_CONSERVATION_RETURN_20260823.md`;
   - `research_reports/CBRC_F3_SOURCE_AND_TARGET_LEAK_AUDIT_20260823.md`;
   - `research_reports/CBRC_F3_ABLATION_AND_COUNTERMODEL_PACKET_20260823.md`;
   - `scripts/cbrc_f3_validate_balanced_mixing_forward.py`;
   - `evidence/cbrc_f3_balanced_mixing_manifest.json`;
4. the Driver review at `bdcee332462d52dbd3642bb3f05b2cafecaebe31`.

Repository/governance files may be used only for execution procedure.

Do not open any downstream coherent/wave comparison result before raw freeze.

## 3. Continued firewall / forbidden selectors

Until raw freeze, do not read/use:

- R063/R064/R065/FQ mathematics;
- downstream coherent-BRC/wave free research;
- external quantum mechanics, quantum walks, Hilbert spaces, Born rules, path integrals, gauge theory, wave equations;
- F1 torsion-free counterfactual as a target route.

Do not preselect or rank candidates by resemblance to:

- a complex/quadratic integer carrier;
- a finite phase group;
- a square/norm/inner product;
- a known splitter/Hadamard/Fourier matrix;
- a continuum wave law.

Do not reject a survivor merely because its scalar is periodic, nonhomogeneous, or vanishes on some nonzero state unless an issued axiom forbids that behavior.

## 4. Frozen accepted checkpoint

Treat only the following as accepted F3 facts:

1. current carrier:
   `C1 = Z e ⊕ <tau | 3tau=0>`;
2. accepted unary transports `R,J,S` from the blind packet;
3. every two-slot additive automorphism has block form `(A,B,D)` with
   `A in GL_2(Z)`, `B in M_2(F3)`, `D in GL_2(F3)`;
4. literal free-block commutation with marker swap gives only signed monomial matrices and cannot realize strict positive balanced splitting;
5. one exact survivor exists with
   `A0=[[2,3],[3,4]]`, `B0=0`, `D0=I`;
6. for that exact survivor a nonunique exact scalar family `q_delta` exists and balance gives two output scalar values `1/2,1/2`;
7. the accepted relative non-sign discriminator survives for that survivor;
8. target-leak audit passed.

Do **not** inherit the raw report's claims that the whole survivor family or scalar family is classified; those are precisely what F3R must decide.

## 5. Physical equivalence to classify first

Before filtering survivors, define the exact physical/presentation equivalence relation on two-slot mixing operators generated only by operations already authorized by the frozen input.

At minimum test/classify the actions of:

- marker swap `P`;
- per-slot accepted unary transports generated by `R,J,S`;
- common/global accepted transport;
- inversion `M -> M^{-1}` **only when** an operational reversal statement proves that the inverse belongs to the same unoriented local operation class;
- compositions of the above.

You must distinguish:

- equality of representatives;
- conjugacy;
- left/right gauge transport;
- inverse-orientation equivalence;
- genuinely inequivalent operations.

Deliver:

`F3R_MIXING_PHYSICAL_EQUIVALENCE_CLASSIFIED`.

## 6. Q1 — complete free-block survivor classification

Let

`A=[[a,b],[c,d]] in GL_2(Z)`.

Classify exactly which `A` can occur in at least one mixing operator `(A,B,D)` for which there exists at least one nonnegative scalar `q` satisfying F3 M1, M2, M4, M5, M6, M9.

Required:

1. derive necessary and sufficient conditions, not merely a search box;
2. classify the possible first columns `(a,c)` compatible with a strictly positive balanced elementary split;
3. classify all second columns `(b,d)` up to the physical equivalence from Section 5;
4. prove whether the survivor set is finite, finitely parameterized, or genuinely infinite;
5. if infinite, give exact invariants/normal forms that decide equivalence;
6. prove whether the canonical `A0=[[2,3],[3,4]]` is universal, minimal within an operation-complexity order, one member of an infinite family, or otherwise positioned.

Do not define operation complexity only after seeing the answer. If a secondary minimal-mixing notion is useful, declare its order before using it and keep it separate from carrier minimality.

Deliver:

`F3R_FREE_BLOCK_SURVIVOR_FAMILY_CLASSIFIED`.

## 7. Q2 — complete torsion/cross lift classification

For every free-block physical class from Q1, classify all

`B in M_2(F3)`, `D in GL_2(F3)`

that admit at least one scalar law satisfying the same F3 conditions.

Required:

- exact formulas or finite orbit classification of admissible `(B,D)`;
- marker/reversal transport of lifts;
- whether torsion-sensitive and torsion-blind scalar laws admit different lift families;
- whether any lift changes the free-block equivalence class physically;
- complete finite enumeration is allowed only after the theorem reduces the problem to a finite set.

Deliver:

`F3R_TORSION_CROSS_LIFT_FAMILY_CLASSIFIED`.

## 8. Q3 — complete conserved marked-scalar classification

For every physical mixing class surviving Q1/Q2, classify all

`q:C1 -> R_nonnegative`

satisfying F3 M1, M2, M5, M6, M9.

Required:

1. give a theorem-level solution space or prove that no finite parametrization exists;
2. identify the invariants/orbits on which `q` can depend;
3. determine which scalar values are forced by balance and which remain free;
4. state whether any survivor forces homogeneity, strict positivity, a positive form, polarization, or finite-copy scaling;
5. produce exact inequivalent countermodels wherever uniqueness fails;
6. do not use a downstream target as a regularity selector.

Deliver:

`F3R_ALL_SURVIVOR_SCALAR_LAWS_CLASSIFIED`.

## 9. Q4 — strengthened but nonbinding regularity controls

The original F3 did not assume global strict positivity or homogeneity. Do not silently add them now.

As **counterfactual controls only**, test one at a time:

1. `GLOBAL_ZERO_SEPARATION`: `z != 0 => q(z)>0`;
2. `INTEGER_COPY_MONOTONICITY`: if a natural order on a derived free coordinate is available, larger positive copies do not decrease scalar;
3. `FINITE_COPY_NONDEGENERACY`: no nonzero old signed multiple `n e` may have zero scalar;
4. `TAGGED_REFINEMENT_NONAMPLIFICATION`: a marked refinement may not increase total scalar above the pre-refinement elementary value unless another accepted operation supplies the difference.

For each, classify exactly which F3R survivor families die/survive. These are not Foundation premises and must not be used to choose the main answer.

Deliver:

`F3R_REGULARITY_COUNTERFACTUALS_CLASSIFIED`.

## 10. Q5 — recoalescence and composition across the whole family

For every surviving physical family, verify/classify:

- exact inverse recovery;
- composition through depth >=4;
- direct-sum pair extension to >=3 markers;
- branch serialization/reversal consistency;
- preservation of `e+Je=0`;
- preservation of the accepted relative non-sign discriminator;
- existence or failure of the two-path post-mixing unmarked discriminator analogous to the canonical F3 witness.

If a survivor fails the discriminator but satisfies mixing/conservation, classify that as a distinct subfamily rather than discarding it without an issued condition.

Deliver:

`F3R_FAMILY_COMPOSITION_AND_RECOALESCENCE_CLASSIFIED`.

## 11. Q6 — final underdetermination/minimality verdict

Using only the completed family classification, answer:

1. Does balanced reversible mixing plus marked scalar conservation select a unique physical mixing family?
2. Does it select a unique scalar law up to normalization?
3. If not, what exact finite/parameter/infinite freedom remains?
4. Is there any mathematically justified next selector already implicit in the frozen native/refinement semantics, or would every further selector be a genuinely new axiom?

Do not open a downstream comparison in this task.

Deliver:

`BALANCED_MIXING_SURVIVOR_FAMILY_COMPLETELY_CLASSIFIED`.

## 12. Deterministic checker

Required path:

`scripts/cbrc_f3r_validate_balanced_mixing_survivor_family.py`

Minimum coverage:

- exact replay of the accepted canonical F3 survivor;
- bounded `GL_2(Z)` scans used only as regression tests against theorem-predicted normal forms;
- complete finite enumeration of every torsion/cross block class after theorem reduction;
- physical-equivalence canonicalization checks;
- exact scalar conservation for representative(s) of every theorem-level survivor family on the finite quotient implied by the proof, where applicable;
- counterexamples for every excluded class at the smallest exact witness;
- composition/recoalescence through depth >=4;
- every regularity counterfactual;
- zero theorem/enumeration mismatches.

Do not claim completeness from a finite box search over `GL_2(Z)`.

## 13. Required artifacts

Return all of:

1. `research_reports/CBRC_F3R_BALANCED_MIXING_SURVIVOR_FAMILY_RETURN_20260823.md`
2. `research_reports/CBRC_F3R_SOURCE_AND_TARGET_LEAK_AUDIT_20260823.md`
3. `research_reports/CBRC_F3R_REGULARITY_AND_ABLATION_PACKET_20260823.md`
4. `scripts/cbrc_f3r_validate_balanced_mixing_survivor_family.py`
5. `evidence/cbrc_f3r_balanced_mixing_survivor_family_manifest.json`

Report exact source SHAs, owner head, artifact SHA-256s, checker digest, and primary verdict.

## 14. Hard acceptance gate

Driver acceptance requires:

`F3R_MIXING_PHYSICAL_EQUIVALENCE_CLASSIFIED`

`F3R_FREE_BLOCK_SURVIVOR_FAMILY_CLASSIFIED`

`F3R_TORSION_CROSS_LIFT_FAMILY_CLASSIFIED`

`F3R_ALL_SURVIVOR_SCALAR_LAWS_CLASSIFIED`

`F3R_REGULARITY_COUNTERFACTUALS_CLASSIFIED`

`F3R_FAMILY_COMPOSITION_AND_RECOALESCENCE_CLASSIFIED`

`BALANCED_MIXING_SURVIVOR_FAMILY_COMPLETELY_CLASSIFIED`

`TARGET_LEAK_AUDIT_PASS`

plus deterministic checker evidence.

## 15. Freeze / handoff

Freeze on the owner branch and report:

- owner head SHA;
- artifact SHA-256 digests;
- checker deterministic digest;
- clean tree status;
- primary verdict.

No F4 or downstream comparison is authorized before Driver acceptance.

---

Driver issue note:

`F3 EXISTENCE ACCEPTED; COMPLETE THE MIXING/SCALAR SURVIVOR FAMILY BEFORE DOWNSTREAM MATCHING.`
