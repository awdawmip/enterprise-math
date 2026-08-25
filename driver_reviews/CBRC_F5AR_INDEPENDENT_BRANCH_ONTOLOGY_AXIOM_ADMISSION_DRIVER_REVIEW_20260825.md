# CBRC F5AR — Independent Branch Ontology Axiom Admission Driver Review

Status: `ACCEPTED_WITH_WORKING_EXTENSION_SCOPE_NARROWING`
Date: `2026-08-25`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`
Task-ID: `RS-CBRC-F5AR-INDEPENDENT-BRANCH-ONTOLOGY-AXIOM-ADMISSION-REPLICATION`
Taskbook source: `7fc3522b2e5b9273025c8d399206460e44b13f6b`
Accepted owner branch: `research/cbrc-f5ar-independent-branch-ontology-axiom-admission`
Accepted owner head: `d41deb8c9fabb014e00bbc6133d366192f31a8a1`
Researcher-ID: `EM-CBRCF5AR-7E8B04`

## 0. Driver verdict

`F5AR_ACCEPTED_WITH_SCOPE_NARROWING`.

Accepted primary mathematical verdict:

`F5AR_ADMIT_RESTRICTED_ELEMENTARY_RULE_ONLY`.

Hard target:

`BRANCH_TO_OLD_SUPPORT_FAITHFULNESS_AXIOM_ADMISSION_STATUS_INDEPENDENTLY_CLASSIFIED = ACCEPTED`.

Scope narrowing is mandatory:

- the admitted rule is a **new Coherent-BRC working-extension axiom**;
- it is not derived from existing BRC semantics;
- it is not promoted to `CANONICAL_FOUNDATION` by this review;
- it does not authorize F6 or a rank-two carrier search by itself.

## 1. Publication-liveness and source firewall

The pre-math gate is accepted.

The owner branch contains `evidence/cbrc_f5ar_execution_stamp.json` with:

- `phase = STARTED_BEFORE_MATH`;
- `admission_verdict = null`;
- `math_source_read_before_stamp = false`;
- exact taskbook source and four whitelist refs.

The audit records the reconciled pre-math stamp commit `680ff7d2eb164b3be33522c52561afaa30c48ce4` and remote verification before mathematics.

`TARGET_LEAK_AUDIT_PASS` is accepted. The research did not preload downstream coherent-wave, R063/R064/R065/FQ, external quantum/wave material, rank-two/complex/quadratic carriers, phase groups, norms, inner products, square laws or splitter targets.

## 2. Accepted candidate lattice

Write `p(b)` for the old signed integer coordinate of an active enriched branch.

Accepted candidate relations:

- `A1 => A0`;
- `A3 => A4 => A0`;
- `A2` is incomparable with `A0,A1,A3,A4`;
- every other distinct implication among `A0..A4` fails with explicit countermodels.

The useful intermediate projection-only rule is

`A1pi : RefOld(b,w) => p(b) != 0`.

An infinite strict finite-depth ladder also exists:

`... => D_3 => D_2 => D_1=A0`,

while

`A4 = forall d>=1, D_d`.

Therefore no finite-depth checker can by itself establish arbitrary-depth leafwise faithfulness.

## 3. Accepted minimal loophole-closing theorem

The exact F4 elementary loophole is the active old-refining split pattern

`(nonzero old projection, zero old projection)`

up to marker relabeling.

Among marker-symmetric predicates depending only on the two elementary old projections, the weakest exact loophole-closing predicate is

`A0 : p1 != 0 and p2 != 0`.

Every strictly weaker predicate admits some zero-coordinate pair and therefore leaves the kernel-branch loophole open.

Accepted consequences:

- A2 does not close the loophole;
- total old-coordinate conservation does not close it;
- enriched nonzeroness alone does not close it;
- concrete-witness support without nonzero signed projection does not close it;
- A3 closes it but is unnecessarily strong because it forbids harmless off-active-branch kernel states.

## 4. Canonical BRC consistency and signed cancellation

A0 is accepted as consistent with the canonical Path-formal/N/Boolean BRC layers because it constrains only the extra active enriched-branch layer.

It does not alter:

- concrete path words or prefix trajectories;
- path counts;
- typed terminals;
- N augmentation;
- Boolean support;
- the minimal `(1,1)` two-witness commuting diamond.

Exact signed cancellation remains legal.

Two individually faithful pre-erasure branches may have old projections `+a` and `-a`; after same-terminal recoalescence and marker erasure their aggregate may be zero. Compatibility requires the recoalesced aggregate not to remain automatically typed as an active retained branch.

Freeze:

`PRE_ERASURE_BRANCH_FAITHFULNESS != POST_RECOALESCENCE_AGGREGATE_NONZERO`.

## 5. Composition boundary

A0 is intentionally elementary and does not imply arbitrary-depth A4.

The exact arbitrary-depth closure property is equivalent to the hereditary local schema:

> every authorized child of every reachable active parent with nonzero old projection also has nonzero old projection.

To propagate a typed old-link rule through arbitrary depth requires additional genealogy/functorial structure, such as a persistent root map `rho : B_active -> W` preserved by refinement.

That structure is not admitted by this review.

Therefore:

`A0_ADMITTED != A4_ADMITTED`.

## 6. Conservativity and ontology cost

A0 is conservative over the canonical Path/N/Boolean BRC base theory in the model-extension sense: every canonical witness structure can be extended with an enrichment/branch layer satisfying A0 without changing any base object, path count, augmentation, Boolean support or terminal.

It is deliberately non-conservative over the class of all previously allowed enriched models, because it excludes the F5R kernel-only active-branch countermodel. That is the intended new-axiom effect.

A0 has lower ontology cost than A1/A4 and much lower algebraic cost than A3:

- no explicit support set required;
- no arbitrary-depth genealogy required;
- off-branch kernel states remain legal;
- translation and marker relabeling covariance are retained.

## 7. Admitted rule — exact scope

Admit into the Coherent-BRC working extension only:

`ELEMENTARY_OLD_REFINING_BRANCH_PROJECTION_NONDEGENERACY`:

> An authorized elementary two-branch refinement of one embedded old concrete occurrence may declare both outputs active retained old-refining branches only if each output has nonzero old signed projection.

Not admitted:

- global support-reflecting retraction A3;
- descendant-family nonzero aggregate A2;
- mandatory witness-support metadata A1;
- arbitrary-depth leafwise A4;
- hereditary branch genealogy H;
- any post-recoalescence nonzero requirement.

Epistemic freeze:

`ELEMENTARY_OLD_REFINING_BRANCH_PROJECTION_NONDEGENERACY = WORKING_EXTENSION_AXIOM`.

`ELEMENTARY_OLD_REFINING_BRANCH_PROJECTION_NONDEGENERACY != CANONICAL_FOUNDATION`.

## 8. Rank consequence remains conditional on a second unadmitted regularity

F5AR correctly states the conditional theorem

`GLOBAL_ZERO_SEPARATION + ADMITTED_BRANCH_FAITHFULNESS => torsion_free_rank(C) >= 2`.

However `GLOBAL_ZERO_SEPARATION` was introduced in F4 as a candidate regularity and was not promoted by the F4 Driver review; F4 explicitly authorized no Foundation promotion.

Therefore no unconditional rank-two lower bound is accepted here.

Freeze:

`RANK_TWO_LOWER_BOUND = STILL_CONDITIONAL_ON_POSITIVE_SEPARATION_ADMISSION`.

This is the next load-bearing gate.

## 9. Checker evidence

Accepted pushed-checker evidence:

- checker blob `8c2008bf39a9ab0517e5f4c074f17fc0a59bf629`;
- SHA-256 `315539c4cf0509c99d5d12a6ca38c65a3d528c0544328226653d695c4def9368`;
- result `PASS`;
- check count `65`;
- mismatch count `0`;
- finite tree depth `4`;
- finite tree models `6561`;
- deterministic digest `eab541a2e3144852acd883f5b6152d61a39e560b5913fba2371d39273c4831b0`.

The arbitrary-depth closure theorem is accepted from the proof, not from the depth-4 enumeration.

## 10. Successor routing

Do not open F6.

The only authorized successor is a positive-separation regularity admission/minimality audit. It must classify whether the full

`GLOBAL_ZERO_SEPARATION : z != 0 => q(z) > 0`

is needed, or whether a strictly weaker free-fiber/envelope positivity rule is sufficient and more conservative.

Only after that regularity is explicitly admitted at working-extension scope may Driver consider opening a rank-two carrier classification.

Freeze:

`F5AR_ACCEPTED_WITH_SCOPE_NARROWING = true`.

`A0_WORKING_EXTENSION_AXIOM_ADMITTED = true`.

`F6_NOT_AUTHORIZED = true`.
