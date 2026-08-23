<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F3R2-SURVIVOR-MEMBERSHIP-PREDICATE-COMPLETION",
  "title": "Coherent-BRC F3R2 — Survivor Membership Predicate Completion",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "BALANCED_MIXING_SURVIVOR_MEMBERSHIP_PREDICATE_CLASSIFIED",
  "next_action": "Close only the remaining F3R membership gap: derive an exact necessary-and-sufficient survivor predicate for arbitrary current-carrier mixing operators, including arbitrary free blocks and torsion/cross lifts, or prove an exact irreducibility obstruction stronger than tautological cone nonemptiness.",
  "dependencies": [
    "research/cbrc-f3r-balanced-mixing-survivor-family-completion@02dd3cc0be4843cbfa4b4bb3b83ec886b6429648",
    "driver_reviews/CBRC_F3R_BALANCED_MIXING_SURVIVOR_FAMILY_DRIVER_REVIEW_20260823.md@93c48c015c4b1522eaf8566586ed76bab31fa324"
  ],
  "source_refs": [
    "research/cbrc-f3r-balanced-mixing-survivor-family-completion@02dd3cc0be4843cbfa4b4bb3b83ec886b6429648",
    "driver_reviews/CBRC_F3R_BALANCED_MIXING_SURVIVOR_FAMILY_DRIVER_REVIEW_20260823.md@93c48c015c4b1522eaf8566586ed76bab31fa324"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": ["CBRC","F3R2","rework","membership","balanced-mixing","classification"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF3R2"
}
-->

# Coherent-BRC F3R2 — Survivor Membership Predicate Completion

Task-ID: `RS-CBRC-F3R2-SURVIVOR-MEMBERSHIP-PREDICATE-COMPLETION`

Driver: `EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Intended owner branch:

`research/cbrc-f3r2-survivor-membership-predicate-completion`

## 0. Driver routing

F3 established existence of balanced reversible mixing on the current carrier.

F3R established, and Driver accepts, the strict-underdetermination theorem:

- infinitely many pairwise physically inequivalent survivor models exist;
- infinitely many inequivalent conserved scalar laws exist;
- no frozen F3 axiom selects the canonical F3 matrix, the `(2,3)` support-split stratum, one prime pair, one period, or one scalar law.

F3R also established exact first-column feasibility and exact support-splitting congruence survivor strata.

The remaining gap is narrower:

> Given an **arbitrary** current-carrier two-slot additive automorphism `M=(A,B,D)`, decide exactly whether there exists at least one nonnegative marked scalar `q` satisfying the frozen F3 invariance, balance, and conservation requirements.

F3R2 is membership-only completion. Do not reopen carrier selection, wave matching, or regularity selection.

## 1. Hard target

`BALANCED_MIXING_SURVIVOR_MEMBERSHIP_PREDICATE_CLASSIFIED`.

A valid completion must provide one of:

1. `STRUCTURAL_IFF_PREDICATE` — a theorem-level necessary-and-sufficient condition on `(A,B,D)`;
2. `COMPLETE_PARAMETER_OR_NORMAL_FORM` — all physical survivor classes parameterized exactly;
3. `FINITE_REDUCTION_IFF` — membership reduced theoremically to a finite exact feasibility object computable from explicit invariants of `(A,B,D)`;
4. `IRREDUCIBILITY_OBSTRUCTION` — an exact proof that no stronger structural reduction is possible in the declared formal language, accompanied by a canonical decision object strictly more informative than the tautology “a scalar exists iff a scalar exists”.

The following is **not** sufficient:

`M survives iff Q(M) is nonempty`

when `Q(M)` is merely defined as “the set of all admissible scalar laws”.

## 2. Mathematical source whitelist

Before raw F3R2 freeze, read/use only:

1. F3R owner packet at `02dd3cc0be4843cbfa4b4bb3b83ec886b6429648`:
   - `research_reports/CBRC_F3R_BALANCED_MIXING_SURVIVOR_FAMILY_RETURN_20260823.md`;
   - `research_reports/CBRC_F3R_SOURCE_AND_TARGET_LEAK_AUDIT_20260823.md`;
   - `research_reports/CBRC_F3R_REGULARITY_AND_ABLATION_PACKET_20260823.md`;
   - `scripts/cbrc_f3r_validate_balanced_mixing_survivor_family.py`;
   - `evidence/cbrc_f3r_balanced_mixing_survivor_family_manifest.json`;
2. Driver review at `93c48c015c4b1522eaf8566586ed76bab31fa324`;
3. the frozen F3 taskbook/blind packet only when required to recover the exact M1–M9 semantics already referenced by F3R.

No downstream coherent/wave comparison source may be opened.

## 3. Firewall / forbidden selectors

Continue to forbid as mathematical selectors:

- R063/R064/R065/FQ mathematical results;
- downstream coherent-BRC/wave results;
- external quantum/wave theory;
- complex/quadratic integer carriers;
- square/norm/inner-product/Born laws;
- Hadamard/Fourier/known splitter matching;
- rejecting periodic or non-strictly-positive scalars merely because they look unphysical.

F3R2 is a mathematical membership classification, not a physical-model selection stage.

## 4. Frozen accepted facts

Treat as accepted:

1. current carrier `C1 = Z e ⊕ <tau | 3tau=0>`;
2. accepted unary operations `R,J,S`;
3. every two-slot additive automorphism has block form
   `(A,B,D)` with `A in GL_2(Z)`, `B in M_2(F3)`, `D in GL_2(F3)`;
4. exact physical equivalence generated by accepted left/right unary gauge, marker swap, and authorized inverse orientation;
5. strict positive balanced elementary splitting requires first free column `(a,c)` with
   `gcd(a,c)=1`, `|a|>=2`, `|c|>=2`;
6. explicit exact support-splitting survivor strata `S_{p,r}` exist for arbitrary distinct primes;
7. the total survivor set is infinite and physically nonunique;
8. for a fixed operator `M`, scalar conservation can be written as linear relations on the unary-orbit value space;
9. F3/F3R target-leak audits passed.

Do not claim that all survivors belong to `S_{p,r}` unless F3R2 proves it.

## 5. Membership object

For a full operator `M`, define the unary-orbit value variables only as required by the accepted invariances.

Translate every frozen F3 marked conservation condition into exact linear equalities/inequalities on those variables.

The task is to eliminate the scalar variables as far as mathematically possible and characterize the projection onto the operator data `(A,B,D)`.

Methods may include ordinary integer/finite-field algebra, convex cones, Farkas-type alternatives, invariant relation modules, semigroup/orbit decompositions, finite quotient theorems, or exact recurrence classification. Do not import a downstream target algebra.

## 6. Q1 — arbitrary free-block membership

For arbitrary

`A=[[a,b],[c,d]] in GL_2(Z)`

with an admissible first column, determine whether there exists **some** choice of `(B,D)` and **some** admissible nonnegative scalar law making `A` survive.

Required:

- decide whether every unimodular second-column completion of an admissible first column survives;
- if not, give exact necessary-and-sufficient restrictions on `(b,d)` or exact survivor subfamilies whose union is all survivors;
- explicitly decide whether free survivors exist outside every support-splitting prime-pair stratum `S_{p,r}`;
- classify up to the frozen physical equivalence.

Deliver:

`F3R2_FREE_BLOCK_MEMBERSHIP_CLASSIFIED`.

## 7. Q2 — arbitrary torsion/cross lift membership

For each free survivor `A`, classify exactly which

`B in M_2(F3)`, `D in GL_2(F3)`

admit at least one scalar law.

The accepted `3888` torsion-blind and `36` positive-delta six-periodic counts are examples/strata, not a priori the full answer.

Required:

- exact iff criterion or complete finite orbit table after theorem reduction;
- marker/reversal transport of the lift classes;
- explicit statement whether some lifts survive only with torsion-sensitive scalar laws;
- explicit statement whether every lift of every free survivor has at least one torsion-blind law.

Deliver:

`F3R2_FULL_LIFT_MEMBERSHIP_CLASSIFIED`.

## 8. Q3 — eliminate scalar variables / exact feasibility criterion

Starting from the fixed-operator conservation relation space, derive the strongest exact feasibility theorem available.

At minimum separate:

- homogeneous conservation equalities;
- normalization `q(e)=1`;
- balanced split constraints `q(a)=q(c)=1/2` on the elementary outputs;
- nonnegativity;
- unary-invariance identifications.

If a dual obstruction theorem exists, state it explicitly: membership fails iff some finite/structured positive certificate contradicts normalization/balance.

If the infinite orbit space reduces to a finite quotient exactly for a class of operators, characterize precisely when and how.

Deliver:

`F3R2_SCALAR_FEASIBILITY_IFF_CLASSIFIED`.

## 9. Q4 — relationship to support-splitting strata

Determine the exact status of the F3R prime-pair models:

- universal normal form;
- proper subclass of all survivors;
- generating family under a closure operation;
- extremal rays of a larger positive cone;
- or another exact role.

Do not assume one outcome.

Deliver:

`F3R2_SUPPORT_SPLIT_STRATA_POSITION_CLASSIFIED`.

## 10. Q5 — physical equivalence / decision normal form

Give a canonical membership normal form or a canonical decision procedure invariant under the accepted physical equivalence.

If the membership predicate is algorithmic, state termination and exactness. If it depends on an infinite relation module, give a theorem showing why the declared representation is canonical and how equivalent operators yield equivalent decision objects.

Deliver:

`F3R2_PHYSICAL_MEMBERSHIP_NORMAL_FORM_CLASSIFIED`.

## 11. Q6 — closure decision

Conclude exactly one:

- `F3R2_ALL_SURVIVORS_EXPLICITLY_CLASSIFIED`;
- `F3R2_ALL_SURVIVORS_DECIDABLE_BY_FINITE_EXACT_PREDICATE`;
- `F3R2_ALL_SURVIVORS_CLASSIFIED_BY_CANONICAL_INFINITE_FEASIBILITY_OBJECT`;
- `F3R2_MEMBERSHIP_IRREDUCIBLE_WITH_EXACT_OBSTRUCTION`;
- `F3R2_TARGET_LEAK_INVALID`.

Only the first four may close:

`BALANCED_MIXING_SURVIVOR_MEMBERSHIP_PREDICATE_CLASSIFIED`.

## 12. Deterministic checker

Required path:

`scripts/cbrc_f3r2_validate_survivor_membership.py`

Minimum coverage:

- replay accepted F3/F3R explicit survivors;
- include free matrices with admissible first column that are **outside** the known `S_{p,r}` examples and classify them correctly;
- compare theorem membership against bounded `GL_2(Z)` scans used only as regression;
- exhaust all `B,D` after any theoremic finite reduction;
- produce smallest exact non-survivor certificates;
- physical-equivalence invariance tests;
- zero theorem/enumeration mismatches.

Do not infer completeness from a finite `GL_2(Z)` box.

## 13. Required artifacts

Return:

1. `research_reports/CBRC_F3R2_SURVIVOR_MEMBERSHIP_RETURN_20260823.md`
2. `research_reports/CBRC_F3R2_MEMBERSHIP_OBSTRUCTION_AND_COUNTERMODEL_PACKET_20260823.md`
3. `research_reports/CBRC_F3R2_SOURCE_AND_TARGET_LEAK_AUDIT_20260823.md`
4. `scripts/cbrc_f3r2_validate_survivor_membership.py`
5. `evidence/cbrc_f3r2_survivor_membership_manifest.json`

Report owner head, artifact SHA-256s, checker digest, clean-tree status, and primary verdict.

## 14. Acceptance gate

Driver acceptance requires:

`F3R2_FREE_BLOCK_MEMBERSHIP_CLASSIFIED`

`F3R2_FULL_LIFT_MEMBERSHIP_CLASSIFIED`

`F3R2_SCALAR_FEASIBILITY_IFF_CLASSIFIED`

`F3R2_SUPPORT_SPLIT_STRATA_POSITION_CLASSIFIED`

`F3R2_PHYSICAL_MEMBERSHIP_NORMAL_FORM_CLASSIFIED`

`BALANCED_MIXING_SURVIVOR_MEMBERSHIP_PREDICATE_CLASSIFIED`

`TARGET_LEAK_AUDIT_PASS`

plus deterministic evidence.

No F4/downstream comparison is authorized before this gate closes.

---

Driver issue note:

`STRICT UNDERDETERMINATION ACCEPTED; CLOSE ONLY THE ARBITRARY-OPERATOR SURVIVOR MEMBERSHIP PREDICATE.`
