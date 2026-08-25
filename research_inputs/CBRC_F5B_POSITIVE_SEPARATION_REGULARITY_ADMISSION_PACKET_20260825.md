# CBRC F5B Blind Input — Positive-Separation Regularity Admission Gate

Status: `DRIVER_FROZEN_BLIND_INPUT`
Date: `2026-08-25`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`

This packet isolates the last known regularity gate before any rank-two carrier classification can be considered. It is not a rank-two, phase, norm or wave task.

## 1. Accepted marked-scalar semantics

Work with an enriched additive coefficient carrier `C` containing the old signed generator `e` and a marked scalar

`q : C -> R_nonnegative`

with at least:

- `q(0)=0`;
- `q(e)=1`;
- one fixed scalar law throughout the declared operation domain;
- exact marked two-slot conservation when a local reversible mixing/refinement is authorized:
  `Q(x,y)=q(x)+q(y)` and `Q(M(x,y))=Q(x,y)`.

Do not assume a norm, power law, inner product, quadratic form or probability interpretation.

## 2. Accepted F4 boundary

Accepted Driver review:

`driver_reviews/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_DRIVER_REVIEW_20260823.md@54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`.

For a finitely generated torsion-free-rank-one carrier

`C ~= Z e ⊕ T`

with finite abelian `T`, define the finite-fiber envelope

`f(n)=min_{t in T} q(ne+t)`.

F4 established the free-block obstruction by passing conservation to `f` and deriving a nonzero period for every non-signed-permutation free quotient block. Any condition forcing

`f(n)>0 for every nonzero n`

therefore conflicts with that periodic zero and rules out a non-signed-permutation free quotient block.

F4 also established that the full candidate

`GLOBAL_ZERO_SEPARATION : z!=0 => q(z)>0`

alone does **not** imply torsion-free rank at least two, because a signed-permutation free quotient can still support a torsion-mediated full-carrier mixing.

F4 did not promote `GLOBAL_ZERO_SEPARATION` to Foundation truth.

## 3. Accepted F5AR branch-ontology boundary

Accepted Driver review:

`driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842`.

Working-extension axiom admitted at restricted scope:

`ELEMENTARY_OLD_REFINING_BRANCH_PROJECTION_NONDEGENERACY` (`A0`).

For an authorized elementary two-branch refinement of one embedded old occurrence, both active old-refining outputs must have nonzero old signed projection.

This is a **working-extension axiom**, not `CANONICAL_FOUNDATION`.

A0 closes the signed-permutation torsion loophole at the elementary old-projection level if the free quotient is already known to be signed permutation: a signed-permutation first column has only one nonzero old-coordinate output.

Therefore a rank-one no-go would follow from A0 plus a positive-separation regularity strong enough to invoke the F4 free-block obstruction.

That consequence is not a selector for this stage.

## 4. Positive-separation candidate lattice to classify

F5B must not assume the strongest formulation is preferred. At minimum classify the following and any strict intermediate rules discovered.

### P0 — global coefficient zero separation

`z != 0 => q(z)>0` for every coefficient state `z in C`.

### P1 — free-coordinate-fiber positivity

For every nonzero free coordinate `n` and every finite-torsion label `t in T`,

`q(ne+t)>0`.

No requirement is imposed on pure-kernel states with free coordinate zero.

### P2 — envelope zero separation

For every nonzero integer `n`,

`f(n)=min_{t in T} q(ne+t)>0`.

For finite `T`, determine whether P1 and P2 are equivalent and whether that equivalence depends on finiteness.

### P3 — finite-copy nondegeneracy

For every nonzero integer `n`,

`q(ne)>0`.

This tests only the embedded old signed copy.

### P4 — active-branch scalar positivity

Every nonzero state currently typed as an active retained branch has positive scalar.

This may leave non-active coefficient states with zero scalar.

### P5 — elementary-split-output positivity

Only the two outputs of an authorized elementary balanced split are required to have positive scalar.

## 5. Admission questions

Classify exactly:

1. the implication/strictness lattice among P0–P5 and all useful intermediate rules;
2. which weakest rule is sufficient for the arbitrary rank-one free-block obstruction;
3. which weakest rule, together with admitted A0, closes **all** rank-one balanced-reversible-conserving models at the issued scope;
4. whether that rule is conservative with respect to pure-kernel states, old signed cancellation and canonical Path/N/Boolean BRC;
5. whether positivity on all nonzero coefficient states is unnecessarily strong;
6. whether a rule can be formulated intrinsically without choosing a noncanonical splitting `C ~= Z e ⊕ T`;
7. what extra data are needed if the rule uses a free-coordinate projection or finite-fiber minimum;
8. whether the rule should be admitted to the Coherent-BRC working extension, retained model-relative, deferred or rejected.

## 6. Non-negotiable distinctions

Keep separate:

- `q(z)>0` versus nonzero old projection;
- coefficient-state positivity versus active-branch positivity;
- pure-kernel states versus states with nonzero free coordinate;
- pointwise positivity versus finite-fiber envelope positivity;
- pre-erasure branch scalar versus post-recoalescence aggregate scalar;
- working-extension admission versus native Foundation truth.

Exact signed cancellation must remain possible. If two pre-erasure faithful states recoalesce to coefficient zero, `q(0)=0` is required and is not a violation of pointwise zero separation.

## 7. Conditional rank consequence — not a selector

If and only if F5B admits a regularity strong enough to recover the F4 rank-one free-block obstruction, then together with already admitted A0 the working extension may state

`ADMITTED_POSITIVE_SEPARATION + A0 + BALANCED_REVERSIBLE_CONSERVATION => torsion_free_rank(C) >= 2`.

This remains a theorem of the explicit working extension, not a theorem of native BRC alone.

Do not construct or classify any rank-two carrier in F5B.

## 8. Firewall

Before raw freeze do not read/use:

- downstream coherent-BRC/wave free research;
- R063/R064/R065/FQ mathematics;
- external quantum mechanics, Hilbert spaces, Born rules, path integrals, quantum walks, gauge theory or wave equations;
- preselected complex/quadratic integer carriers;
- finite phase groups;
- norms, inner products, positive quadratic forms, p-norms or square laws;
- Hadamard/Fourier/splitter targets;
- any proposed F6 answer.

The admission decision must be made solely from the accepted F4/F5AR boundaries, exact scalar/refinement semantics, logical minimality, countermodels and conservativity.
