<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F4-POSITIVE-SEPARATION-RANK-LIFT-CLASSIFICATION",
  "title": "Coherent-BRC F4 — Positive-Separation Rank-Lift Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "GLOBAL_ZERO_SEPARATION_RANK_ONE_EXTENSION_CLASSIFIED",
  "next_action": "Using only the blind F4 packet, classify whether global zero-separation can coexist with balanced reversible scalar-conserving mixing on any finitely generated conservative coefficient carrier of torsion-free rank one, and if not prove the exact rank lower bound without constructing or preselecting a downstream rank-two target.",
  "dependencies": [
    "research_inputs/CBRC_F4_BLIND_POSITIVE_SEPARATION_RANK_LIFT_PACKET_20260823.md@c6bdd396f1777185b8791228492ca50f996307a7"
  ],
  "source_refs": [
    "research_inputs/CBRC_F4_BLIND_POSITIVE_SEPARATION_RANK_LIFT_PACKET_20260823.md@c6bdd396f1777185b8791228492ca50f996307a7"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "tags": ["CBRC","F4","blind-forward","positive-separation","rank-lower-bound","no-go","foundation-facing"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF4"
}
-->

# Coherent-BRC F4 — Positive-Separation Rank-Lift Classification

Task-ID: `RS-CBRC-F4-POSITIVE-SEPARATION-RANK-LIFT-CLASSIFICATION`

Driver: `EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Intended owner branch:

`research/cbrc-f4-positive-separation-rank-lift-classification`

## 0. Driver routing

F3/F3R/F3R2 is closed at the issued weak-scalar scope. The exact survivor set is decidable, but all known accepted rank-one survivor scalars are compatible with nonzero coefficient states carrying zero marked scalar.

F4 does **not** compare against downstream wave structures and does not search for a preferred rank-two carrier.

It tests one new target-independent candidate regularity only:

`GLOBAL_ZERO_SEPARATION: z != 0 => q(z)>0`.

The stage must determine whether this condition is compatible with balanced reversible scalar-conserving mixing on **any** finitely generated conservative coefficient carrier whose torsion-free rank remains one.

## 1. Hard target

`GLOBAL_ZERO_SEPARATION_RANK_ONE_EXTENSION_CLASSIFIED`.

Admissible primary verdicts:

- `F4_RANK_ONE_SURVIVOR_EXISTS`;
- `F4_RANK_ONE_NO_GO_RANK_LIFT_REQUIRED`;
- `F4_RANK_ONE_CLASSIFICATION_UNDERDETERMINED`;
- `F4_TARGET_LEAK_INVALID`.

Failure of existence is a valid and expectedly useful result.

## 2. Phase-A mathematical whitelist

Read/use only:

`research_inputs/CBRC_F4_BLIND_POSITIVE_SEPARATION_RANK_LIFT_PACKET_20260823.md`

at source:

`c6bdd396f1777185b8791228492ca50f996307a7`.

The taskbook is binding specification, not additional mathematical evidence.

Repository/governance files may be used only for execution procedure.

## 3. Continued firewall

Before raw freeze, do not read/use:

- full F0/F1/F2/F3/F3R/F3R2 reports beyond the blind packet;
- R063/R064/R065/FQ mathematics;
- downstream coherent-BRC/wave free research;
- Hodge/Shor mathematics;
- external quantum mechanics, quantum walks, Hilbert spaces, Born rules, path integrals, or wave equations.

Do not preselect or search toward:

- complex numbers or quadratic integer rings;
- rank-two cyclotomic modules;
- finite phase groups;
- square/p-power laws;
- norms, inner products, positive quadratic forms;
- Hadamard/Fourier/splitter matrices;
- continuum equations.

No rank-two construction belongs in F4.

## 4. Candidate regularity status

`GLOBAL_ZERO_SEPARATION` is a **new candidate regularity**, not accepted Foundation truth.

F4 must classify its mathematical consequences and load-bearing role. It may not describe it as physically necessary.

## 5. Q1 — general rank-one conservative carrier normal form

Starting from the blind packet's allowed extension class, work with arbitrary finitely generated conservative additive carriers of torsion-free rank one.

Prove or replay the exact normal form needed for the task:

`C ~= Z e ⊕ T`

with finite abelian `T`, together with the required embedding/retraction of the old signed generator.

Classify the induced form of an arbitrary two-slot additive automorphism on the free quotient and finite torsion fibers sufficiently to support the later no-go/existence proof.

Do not assume `T` cyclic or of order three.

Deliver:

`F4_RANK_ONE_CARRIER_AND_AUTOMORPHISM_NORMAL_FORM_CLASSIFIED`.

## 6. Q2 — finite-torsion envelope theorem

Let

`q:C -> R_nonnegative`

satisfy the inherited marked scalar conditions plus `GLOBAL_ZERO_SEPARATION`.

For the finite torsion fiber define

`f(n)=min_{t in T} q(n,t)`.

Classify exactly what conservation and reversibility force on `f`.

Required:

- prove the output torsion map over every fixed free input is a bijection when the full two-slot map is an automorphism;
- justify taking the minimum over the finite torsion fibers;
- derive a torsion-blind free conservation law;
- derive `f(0)=0`, `f(1)=1`, evenness, and balanced first-column values;
- prove how global zero separation transfers to strict positivity of `f(n)` for every nonzero free integer `n`.

Deliver:

`F4_FINITE_TORSION_MIN_ENVELOPE_CLASSIFIED`.

## 7. Q3 — arbitrary free-block no-go/existence

Let the induced free block be

`A=[[a,b],[c,d]] in GL_2(Z)`.

Without importing the F3R2 proof text, classify the exact scalar consequences of free conservation for arbitrary integer `A`.

At minimum:

1. derive all mixed-difference identities needed;
2. prove whether their constants vanish under nonnegativity/balance;
3. derive the exact annihilator/periodicity statement or an equivalent obstruction;
4. combine it with `GLOBAL_ZERO_SEPARATION`.

If a rank-one survivor exists, give the exact smallest counterexample and show why it escapes the obstruction.

If none exists, prove the no-go for **all** finite `T` and all two-slot additive automorphisms satisfying the inherited balance/conservation requirements.

Deliver:

`F4_RANK_ONE_POSITIVE_SEPARATION_MIXING_CLASSIFIED`.

## 8. Q4 — rank lower bound

If Q3 is a no-go, state the exact consequence for any future conservative finitely generated successful carrier.

The conclusion must distinguish:

- torsion-only enlargement;
- torsion-free rank increase;
- what has actually been proved versus what remains open.

If rank one is impossible, the strongest authorized F4 conclusion is only:

`torsion_free_rank(C) >= 2`.

Do not classify, name, or select any rank-two carrier in this stage.

Deliver:

`F4_MINIMUM_TORSION_FREE_RANK_LOWER_BOUND_CLASSIFIED`.

## 9. Q5 — ablation of the new regularity

Show exactly which part of the no-go disappears when `GLOBAL_ZERO_SEPARATION` is removed.

At minimum replay one exact rank-one balanced conserving survivor allowed by the blind packet's weak-scalar semantics, or prove another smallest witness.

This demonstrates that the new regularity is genuinely load-bearing rather than redundant with old axioms.

Also test separately:

- weakening to positivity only on elementary states;
- weakening to positivity only on the two elementary split outputs;
- `FINITE_COPY_NONDEGENERACY`: `q(n e)>0` for every nonzero integer `n`;
- whether the full global zero-separation condition is stronger than needed for the rank-one no-go.

Deliver:

`F4_POSITIVE_SEPARATION_ABLATION_AND_MINIMALITY_CLASSIFIED`.

## 10. Deterministic checker

Required path:

`scripts/cbrc_f4_validate_positive_separation_rank_lift.py`

Minimum checker coverage:

- exact finite torsion-fiber envelope identities for multiple nonisomorphic finite abelian test groups;
- bounded `GL_2(Z)` regression against the theorem, never used as proof;
- accepted weak-scalar rank-one survivor replay when the new regularity is removed;
- smallest contradictions for zero-separation/nondegeneracy controls;
- all mandatory ablations;
- zero theorem/enumeration mismatches.

No finite enumeration may be used to claim arbitrary finite-group or arbitrary-`GL_2(Z)` completeness.

## 11. Required artifacts

Return all of:

1. `research_reports/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_RETURN_20260823.md`
2. `research_reports/CBRC_F4_SOURCE_AND_TARGET_LEAK_AUDIT_20260823.md`
3. `research_reports/CBRC_F4_ABLATION_AND_COUNTERMODEL_PACKET_20260823.md`
4. `scripts/cbrc_f4_validate_positive_separation_rank_lift.py`
5. `evidence/cbrc_f4_positive_separation_rank_lift_manifest.json`

The return must state exact source SHAs, owner head, artifact SHA-256s, checker digest, primary verdict, and unresolved assumptions.

## 12. Hard acceptance gate

Driver acceptance requires:

`F4_RANK_ONE_CARRIER_AND_AUTOMORPHISM_NORMAL_FORM_CLASSIFIED`

`F4_FINITE_TORSION_MIN_ENVELOPE_CLASSIFIED`

`F4_RANK_ONE_POSITIVE_SEPARATION_MIXING_CLASSIFIED`

`F4_MINIMUM_TORSION_FREE_RANK_LOWER_BOUND_CLASSIFIED`

`F4_POSITIVE_SEPARATION_ABLATION_AND_MINIMALITY_CLASSIFIED`

`TARGET_LEAK_AUDIT_PASS`

plus deterministic checker evidence.

## 13. Freeze / handoff

Freeze the raw F4 packet on the owner branch and report:

- owner head SHA;
- artifact SHA-256 digests;
- checker deterministic digest;
- clean tree status;
- primary verdict.

No rank-two F5, downstream wave comparison, or Foundation promotion is authorized before Driver acceptance.

---

Driver issue note:

`F3 FAMILY CLOSED; TEST POSITIVE-SEPARATION AS A NEW REGULARITY WITHOUT PRESELECTING THE RANK-TWO ANSWER.`
