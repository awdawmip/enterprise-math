<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F3-BALANCED-REVERSIBLE-MIXING-CONSERVATION-FORWARD-CLASSIFICATION",
  "title": "Coherent-BRC F3 — Balanced Reversible Mixing and Scalar Conservation Forward Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "BALANCED_REVERSIBLE_MIXING_SCALAR_CONSERVATION_MINIMAL_EXTENSION_CLASSIFIED",
  "next_action": "Using only the blind F3 packet, classify whether the accepted observable non-sign carrier can support a genuinely branch-mixing reversible balanced refinement with a conserved nonnegative marked scalar, and if not classify the least carrier/readout extension that can, without preselecting a target algebra or power law.",
  "dependencies": [
    "research_inputs/CBRC_F3_BLIND_BALANCED_MIXING_PACKET_20260823.md@19ed5cfdba021cf67be0f059d8e26be1fb5af3b2",
    "driver_reviews/CBRC_F2_OBSERVABLE_NONSIGN_RECOALESCENCE_DRIVER_REVIEW_20260823.md@1668a534e042c852069299a56851b5795e25e860"
  ],
  "source_refs": [
    "research_inputs/CBRC_F3_BLIND_BALANCED_MIXING_PACKET_20260823.md@19ed5cfdba021cf67be0f059d8e26be1fb5af3b2"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "CBRC",
    "F3",
    "blind-forward",
    "balanced-mixing",
    "reversible-refinement",
    "scalar-conservation",
    "foundation-facing"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF3"
}
-->

# Coherent-BRC F3 — Balanced Reversible Mixing and Scalar Conservation Forward Classification

Task-ID: `RS-CBRC-F3-BALANCED-REVERSIBLE-MIXING-CONSERVATION-FORWARD-CLASSIFICATION`

Driver: `EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Owner branch:

`research/cbrc-f3-balanced-reversible-mixing-conservation-forward-classification`

## 0. Driver routing

F0 established the minimal conservative signed cancellation layer.

F1 established a least hidden finite non-sign transport layer under its accepted extension order.

F2 established that the hidden layer is **compatible with relative recoalescence observability**, but also proved that the scalar readout family is extremely nonunique. Even a coarse support-type readout can satisfy the F2 conditions.

Therefore F3 must not continue by guessing a better readout table.

The next load-bearing question is whether a stronger local operational structure can select both carrier and scalar behavior:

> Can one elementary marked alternative be reversibly and nontrivially refined/mixed into two marked alternatives, both carrying nonzero scalar content, with exact scalar conservation and choice independence; and can the inverse local law recoalesce them without loss before the declared final unmarked aggregation?

If the accepted F1/F2 carrier cannot support this, classify the least conservative enlargement that can.

## 1. Hard target

`BALANCED_REVERSIBLE_MIXING_SCALAR_CONSERVATION_MINIMAL_EXTENSION_CLASSIFIED`.

Admissible primary outcomes include:

- current accepted carrier supports a unique minimal balanced mixing/readout class;
- current carrier supports a family;
- current carrier has an exact no-go but a least larger carrier exists;
- several inequivalent least larger carriers survive;
- the operational requirements are inconsistent;
- the requirements remain underdetermined and no honest minimum can be selected.

Failure of uniqueness is not task failure.

## 2. Phase-A mathematical whitelist

Read/use only:

`research_inputs/CBRC_F3_BLIND_BALANCED_MIXING_PACKET_20260823.md`

at source:

`19ed5cfdba021cf67be0f059d8e26be1fb5af3b2`.

The taskbook itself is binding specification, not an additional mathematical source.

Repository/governance files may be read only for execution/build procedure.

Before raw freeze, do not open any upstream full report or downstream comparison source.

## 3. Phase-A blindness / forbidden preload

Until the F3 raw packet is frozen, do not read or use:

- full F0/F1/F2 reports beyond the blind packet;
- F1 torsion-free counterfactuals;
- R063/R064/R065/FQ mathematics;
- downstream coherent-BRC/wave free research;
- Hodge/Shor mathematics;
- external quantum mechanics or quantum walks;
- complex-amplitude, Hilbert-space, Born, path-integral, or wave-equation formalisms.

Forbidden as premises or target selectors are any prechosen:

- quadratic integer ring or field;
- complex numbers;
- finite cyclic phase group;
- root of unity;
- square, p-power, norm, inner product, or quadratic form;
- balanced 2x2 matrix;
- trigonometric law;
- physical beam-splitter or continuum model.

Ordinary algebra, finitely generated abelian groups, additive automorphisms, ordered nonnegative scalar functions, finite combinatorics, universal constructions, and exact finite classification are allowed.

## 4. F3 local state semantics

Let `C` be a conservative coefficient carrier extending the accepted blind-input carrier if enlargement is required.

A **marked two-slot state** is `(x,y) in C ⊕ C`, representing two distinguishable Path-formal alternatives before marker erasure.

This is bookkeeping for retained alternatives, not a simultaneous multi-cell native state.

Let the marker swap be

`P(x,y)=(y,x)`.

Let

`q:C -> R_nonnegative`

be a local marked scalar assigned to one marked coefficient state. Do not assume any formula for `q`.

The marked total is

`Q(x,y)=q(x)+q(y)`.

This additivity is only for **still-distinguishable marked slots**.

The unmarked same-terminal recoalescence readout remains a separate object and is not to be identified with `Q` without proof.

## 5. Operational requirements to classify

### M1. `ZERO_AND_ELEMENTARY_NORMALIZATION`

`q(0)=0`, `q(e)=1`.

Test whether strict positivity `z!=0 => q(z)>0` is forced or must be an additional condition. For the specific balanced split outputs in M5, both scalar values must be strictly positive.

### M2. `ACCEPTED_ABSOLUTE_TRANSPORT_INVARIANCE`

On the accepted blind-input operations wherever defined,

`q(R^k z)=q(z)`,

`q(Jz)=q(z)`,

`q(Sz)=q(z)`.

If the carrier is enlarged, classify the weakest extension of these actions needed for consistency; do not add more symmetry than required.

### M3. `REVERSIBLE_LOCAL_MIXING`

There exists an additive bijection

`M:C⊕C -> C⊕C`

representing one local pre-collapse refinement/mixing step.

`M` is not allowed to be only independent per-slot transport, a global sign, marker swap, or a composition of those trivial actions.

If additivity itself is too strong or inconsistent, prove that and formulate the weakest replacement preserving finite composition and reversibility.

### M4. `MARKER_RELABELING_CHOICE_INDEPENDENCE`

The physical mixing class must be independent of naming the two marker slots.

Do **not** assume `MP=PM` in advance. Classify all target-independent possibilities consistent with choice independence, including commuting, conjugate, inverse, or other derived transport relations, and state which are actually forced.

### M5. `BALANCED_NONTRIVIAL_REFINEMENT`

For an elementary one-slot input `(e,0)`, write

`M(e,0)=(a,b)`.

Require:

- `a != 0`, `b != 0`;
- `q(a)>0`, `q(b)>0`;
- branch naming must not prefer one output physically;
- therefore derive the correct meaning of `balanced` from M4 and scalar invariance rather than imposing `a=b` or a particular numerical coefficient.

At minimum determine whether balance forces

`q(a)=q(b)`

or a weaker orbit-equivalence statement.

### M6. `EXACT_MARKED_SCALAR_CONSERVATION`

For every state in the declared generated domain,

`Q(M(x,y))=Q(x,y)`.

The same must hold for `M^{-1}`.

Do not assume a norm theorem; this is the operational conservation condition from which any scalar geometry must be derived.

### M7. `COMPOSITION_AND_REFINEMENT_CONSISTENCY`

Repeated local mixing must be well-defined through depth at least four.

Temporary refinement into more marker slots followed by a declared inverse/local recoalescence may not change results solely because of parenthesization, serialization, or marker names.

Classify exactly what higher-slot extension is required or whether a two-slot law is sufficient locally.

### M8. `SIGN_DARK_AND_RELATIVE_NONSIGN_COMPATIBILITY`

The accepted signed cancellation capability must survive.

The accepted relative non-sign discriminator from the blind packet must not be invalidated merely by enlarging the carrier.

This condition does **not** require any particular unmarked scalar value.

### M9. `NO_HIDDEN_SCALAR_RESCALING`

A reversible local change of coefficient presentation may not secretly multiply all marked scalar values by a step-dependent arbitrary factor. Conservation must use one fixed `q` on the declared domain.

## 6. F3-Q1 — current-carrier mixing no-go/existence

First test the accepted blind-input carrier exactly as given.

Classify every additive automorphism of `C1⊕C1` relevant to M3–M8 up to the declared relabeling equivalence.

Required:

- prove whether a balanced nontrivial `M` can exist on `C1`;
- do not infer impossibility merely because a familiar linear matrix is unavailable;
- classify torsion-assisted mixing separately from free-part mixing;
- exhibit an exact survivor or exact obstruction.

Deliver:

`CURRENT_OBSERVABLE_CARRIER_BALANCED_MIXING_CAPABILITY_CLASSIFIED`.

## 7. F3-Q2 — scalar conservation family on current carrier

Independently of Q1, classify all `q` on the current carrier that can satisfy M1, M2, M5, M6 for every Q1 survivor.

If no nontrivial mixing survives Q1, state whether scalar conservation is vacuous or whether it provides an independent obstruction.

If multiple `q` survive, give at least two inequivalent exact countermodels.

Deliver:

`CURRENT_CARRIER_MARKED_SCALAR_CONSERVATION_CLASSIFIED`.

## 8. F3-Q3 — least carrier enlargement if required

If current `C1` fails M3–M6, define an explicit conservative-extension order for the joint pair `(C,M,q)`.

It must consider at least:

1. preservation/retraction of the accepted old carrier;
2. torsion-free rank increase;
3. new additive generators and relations;
4. torsion added or removed;
5. size/structure of the orbit generated by an elementary coefficient under derived local transports;
6. complexity of the local mixing law;
7. whether scalar values require an additional ordered/divisible coefficient domain;
8. whether internal coefficient multiplication is required or merely optional.

Classify all least extensions at the first successful complexity level.

Do not impose torsion-free unless derived as necessary.

Deliver:

`MINIMAL_BALANCED_MIXING_CARRIER_EXTENSION_CLASSIFIED`.

## 9. F3-Q4 — does conservation select the scalar law?

For every least surviving `(C,M)` family, classify all nonnegative scalar laws `q` satisfying M1–M9.

Questions to answer without target-law language:

- Is `q` unique up to normalization?
- Is a homogeneous degree forced?
- Is a bilinear/polarization object forced?
- Does a positive form emerge from conservation, or do nonlinear/orbit-valued laws remain possible?
- Does the old F2 torsion-sensitive readout survive conservation?

If any power, quadratic form, or polarization emerges, prove it from the operational conditions and provide ablations showing which condition selects it.

Deliver:

`BALANCED_MIXING_SCALAR_LAW_CLASSIFIED`.

## 10. F3-Q5 — recoalescence discriminator after mixing

Use the minimal same-terminal two-path fiber.

Construct the smallest exact experiment using only derived F3 operations that compares at least two relative transport presentations with the same tagged total and the same single-branch scalar data.

Classify whether unmarked aggregate classes can differ while the marked scalar is conserved.

Do not fit a sinusoid or continuum fringe.

Deliver:

`BALANCED_MIXING_RELATIVE_RECOALESCENCE_DISCRIMINATOR`.

## 11. F3-Q6 — multiplication / coefficient algebra boundary

Ask only after the additive/mixing/scalar classification is frozen mathematically:

- does composition of `M`, accepted transports, and coefficient addition force an internal multiplication?
- does any endomorphism generator satisfy a derived polynomial relation?
- are several inequivalent algebra structures compatible with the same observable data?

Do not identify any resulting algebra by a familiar name before the raw packet freeze.

Deliver:

`BALANCED_MIXING_COEFFICIENT_ALGEBRA_BOUNDARY_CLASSIFIED`.

## 12. Mandatory ablations

Remove one at a time and rerun the smallest discriminating classification:

1. reversibility M3;
2. branch relabeling choice independence M4;
3. balanced two-nonzero-output condition M5;
4. marked scalar conservation M6;
5. composition/refinement consistency M7;
6. sign-dark compatibility M8;
7. fixed scalar/no-rescaling M9;
8. strict positivity on split outputs;
9. minimal-extension requirement.

Also test the counterfactual in which `q` is allowed to be an arbitrary orbit label with no conservation requirement; this must demonstrate exactly what M6 adds.

## 13. Deterministic checker

Required path:

`scripts/cbrc_f3_validate_balanced_mixing_forward.py`

Minimum coverage:

- exact current-carrier presentation and accepted `R,J,S` relations;
- mathematically complete enumeration of every finite/local candidate class used in a minimality claim;
- branch-swap equivalence checks;
- balanced split of `(e,0)`;
- scalar conservation on a declared finite generating window;
- inverse mixing checks;
- composition through depth `>=4`;
- smallest two-path recoalescence discriminator;
- every mandatory ablation/countermodel;
- zero theorem/enumeration mismatches.

Enumeration is regression evidence only; infinite-domain and uniqueness claims require proof.

## 14. Target-leak kill conditions

Immediate `F3_TARGET_LEAK_INVALID` if the researcher:

- reads full upstream counterfactual/downstream wave material before freeze;
- starts from a known amplitude/beam-splitter algebra;
- assumes a square/p-norm/inner product;
- preselects a complex/quadratic integer carrier;
- chooses a finite phase group or polynomial because it matches a downstream model;
- identifies `balanced` with a prechosen numeric matrix;
- uses external quantum/wave theory as a premise;
- silently assumes torsion must be removed because it looks unphysical.

## 15. Explicit non-goals

F3 must not:

- derive or name a physical probability law;
- fit double-slit data;
- derive a continuum wave/Schrodinger/Dirac equation;
- compare to R063/R064/R065 or downstream free-research results before freeze;
- optimize quantum algorithms;
- promote any F3 object to Foundation truth.

## 16. Required artifacts

Return all of:

1. `research_reports/CBRC_F3_BALANCED_REVERSIBLE_MIXING_CONSERVATION_RETURN_20260823.md`
2. `research_reports/CBRC_F3_SOURCE_AND_TARGET_LEAK_AUDIT_20260823.md`
3. `research_reports/CBRC_F3_ABLATION_AND_COUNTERMODEL_PACKET_20260823.md`
4. `scripts/cbrc_f3_validate_balanced_mixing_forward.py`
5. `evidence/cbrc_f3_balanced_mixing_manifest.json`

The main report must include exact source SHAs, theorem/countermodel statements, minimality order, survivor family, scalar-law classification, ablation map, checker digest, unresolved assumptions, and primary verdict.

## 17. Verdict taxonomy

Choose exactly one primary verdict:

- `F3_CURRENT_CARRIER_UNIQUE_BALANCED_MIXING`
- `F3_CURRENT_CARRIER_BALANCED_MIXING_FAMILY`
- `F3_CURRENT_CARRIER_MIXING_NO_GO_MINIMAL_EXTENSION_FOUND`
- `F3_FINITE_MINIMAL_MIXING_EXTENSION_FAMILY`
- `F3_MIXING_EXISTS_SCALAR_LAW_UNDERDETERMINED`
- `F3_BALANCED_MIXING_NO_GO_UNDER_CONSTRAINTS`
- `F3_EXISTENCE_WITHOUT_MINIMALITY`
- `F3_TARGET_LEAK_INVALID`

Secondary tags must separately report current-carrier viability, carrier extension, mixing law, scalar law, recoalescence discriminator, multiplication boundary, and ablations.

## 18. Hard acceptance gate

Driver acceptance requires all of:

`CURRENT_OBSERVABLE_CARRIER_BALANCED_MIXING_CAPABILITY_CLASSIFIED`

`CURRENT_CARRIER_MARKED_SCALAR_CONSERVATION_CLASSIFIED`

`MINIMAL_BALANCED_MIXING_CARRIER_EXTENSION_CLASSIFIED` if enlargement is needed

`BALANCED_MIXING_SCALAR_LAW_CLASSIFIED`

`BALANCED_MIXING_RELATIVE_RECOALESCENCE_DISCRIMINATOR`

`BALANCED_MIXING_COEFFICIENT_ALGEBRA_BOUNDARY_CLASSIFIED`

`TARGET_LEAK_AUDIT_PASS`

plus all required ablations and deterministic checker evidence.

## 19. Freeze / handoff

Freeze the raw F3 packet on the owner branch and report:

- owner head SHA;
- artifact SHA-256 digests;
- checker deterministic digest;
- clean working-tree status;
- primary verdict.

Only after Driver acceptance may any downstream comparison stage be opened.

---

Driver issue note:

`RELATIVE_OBSERVABILITY_ACCEPTED; QUANTITATIVE LAW NOT ACCEPTED; CLASSIFY BALANCED REVERSIBLE MIXING FORWARD.`
