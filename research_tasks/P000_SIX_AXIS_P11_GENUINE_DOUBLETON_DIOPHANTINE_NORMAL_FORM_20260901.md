<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-P11-GENUINE-DOUBLETON-DIOPHANTINE-NORMAL-FORM",
  "title": "P000 six-axis genuine P11 doubleton Diophantine normal form",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-p11-genuine-doubleton-diophantine-normal-form",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The pairability-filtered P11 revision closes the exact 0/1-bit selector law: genuine ambiguity occurs only when a C1 or C2 combinatorial collision has both candidate packets integer-pairable. What remains unclassified is the arithmetic shape of all such genuine doubletons beyond the two minimal B=6 witnesses and their homogeneous scaling families.",
  "next_action": "Translate the exact C1/C2 plus six-edge pairability conditions into a primitive integer normal form, quotient the known common root-scaling action, and prove a complete parametrization or an exact obstruction to finite rational parametrization, with simultaneous-C1+C2 and bounded-height regressions treated separately.",
  "dependencies": [
    "RR-16ADB5F4DE72A332B509"
  ],
  "source_refs": [
    "research_returns/P000_SIX_AXIS_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR_PAIRABILITY_REVISION_V2_RETURN_20260901.md",
    "research_artifacts/P000_SIX_AXIS_P11_COLLISION_LOCUS_CONDITIONAL_SELECTOR_PAIRABILITY_REVISION_V2/certificate_20260901.json"
  ],
  "evidence_status": "PARENT_RESULT_DRIVER_ACCEPTED_REQUIRED / GENUINE_DOUBLETON_DIOPHANTINE_GAP / DERIVED_ARITHMETIC_ONLY",
  "hard_block": null,
  "tags": [
    "P000",
    "six-axis",
    "P11",
    "doubleton",
    "pairability",
    "Diophantine",
    "normal-form",
    "parametrization"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-P11-GENUINE-DOUBLETON-DIOPHANTINE-NORMAL-FORM",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-ARITHMETIC-TROPICAL-INTEGRATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000P11D1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-P11-COLLISION-LOCUS-CONDITIONAL-SELECTOR",
  "successor_gate": {
    "new_information_gap": "The accepted pairability-filtered theorem gives an exact membership test for genuine C1/C2 doubletons but not a structural classification of all integer solutions. Only two minimal B=6 witnesses and their common root-scaling families are currently frozen.",
    "why_parent_result_does_not_close_it": "Testing six discriminant-square/parity predicates is decision-complete for a given H,T, but it does not explain the solution set, primitive seeds, simultaneous-collision families, or whether every genuine doubleton arises from finitely many rational parameter families after scaling.",
    "discriminating_outcomes": [
      "all primitive C1 and C2 genuine doubletons admit finitely many explicit rational/integer parameter families",
      "a finite set of normal forms exists but one or more families require Pell-type or higher arithmetic parameters rather than rational parametrization",
      "the frozen system contains an exact obstruction to finite parametrization and the obstruction can be isolated as a higher-genus or otherwise provably non-rational component"
    ],
    "kill_condition": "Do not add higher mixed moments, infer native orientation or Pfaffian-slot choice, reduce P000 dimension, claim factorization, or enter Full-Cell dynamics. If finite parametrization fails, return the exact arithmetic obstruction rather than enlarging the grammar.",
    "alternative_route_or_free_exploration_considered": "Closing now would leave the newly isolated genuine doubleton locus as a black-box six-square test. Further information-coding work is already closed by the 0/1-bit theorem, while native geometry routes are separately owned. A Diophantine normal-form analysis is the smallest new mathematical question created by the accepted result.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent hard target is selector correctness and is complete. This task changes the object from deciding the cardinality of a fixed fibre to classifying the global integer solution variety of genuine doubletons, with independent success and kill outcomes."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 six-axis genuine P11 doubleton Diophantine normal form

## Mother question

The accepted pairability-filtered P11 theorem identifies genuine two-state ambiguity exactly: on distinct sorted marginals `H=(h0,h1,h2)` and `T=(t0,t1,t2)`, either `C1: AC=BD` with both `132/213` packets pairable, or `C2: AD=BC` with both `231/312` packets pairable. What is the arithmetic structure of **all** integer solutions to these genuine-doubleton systems after removing the already-known common scaling symmetry?

Can the solution set be described by finitely many explicit primitive normal forms and parameter families, or is there an exact arithmetic obstruction to such a finite rational parametrization?

## Frozen inputs and scope

Freeze the accepted Generation-2 P11 result at derived six-coordinate arithmetic strength. Use sorted distinct integer marginals, positive gaps

`A=h1-h0`, `B=h2-h1`, `C=t1-t0`, `D=t2-t1`,

the exact pairability predicate

`Pair(h,t) <=> h^2-4t=d^2>=0` with `d congruent h (mod 2)`,

and the genuine-doubleton criteria:

- `C1: AC=BD` plus pairability of all six `(h,t)` edges appearing in `132` and `213`;
- `C2: AD=BC` plus pairability of all six `(h,t)` edges appearing in `231` and `312`.

For each pairable edge, the unordered integer root pair is uniquely recovered from `(h,t)`. Common scaling of every recovered local root by `m>=1` sends `H -> mH` and `T -> m^2 T` and preserves the genuine-doubleton class. This scaling is known input and must be factored out rather than rediscovered as the whole classification.

No higher mixed moment may be introduced. All objects remain a derived arithmetic facade; the task does not select an oriented Pfaffian slot or a native geometric structure.

## Hard target and required outputs

Hard target:

`P000_P11_GENUINE_DOUBLETON_DIOPHANTINE_NORMAL_FORM_EXACTLY_CLASSIFIED_OR_FINITE_PARAMETRIZATION_OBSTRUCTED`.

Required outputs:

1. rewrite the C1 and C2 genuine-doubleton conditions as explicit integer equations in recovered local-root variables, and prove equivalence with the frozen `(H,T)` formulation;
2. define an exact primitive normalization modulo common root scaling and prove existence/uniqueness of the primitive representative up to the declared finite symmetries;
3. classify the C1 and C2 primitive solution sets separately, including sign patterns, zero-root boundaries, parity constraints, and the effect of swapping the two local roots on any edge;
4. determine whether each primitive solution set is covered by finitely many rational/integer parameter families; if yes, give formulas and prove completeness, and if not, isolate a precise arithmetic component obstructing finite rational parametrization;
5. treat simultaneous `C1+C2` as a separate sublocus and classify whether it is a specialization of the separate families or carries genuinely different primitive arithmetic;
6. recover the frozen minimal `B=6` C1 and C2 witnesses and their scaling families from the classification rather than inserting them as exceptional data;
7. search for primitive solutions in one predeclared bounded root-height range and compare the observed orbit counts/families with the symbolic classification; bounded enumeration is regression evidence, not proof;
8. provide explicit counterexamples to tempting but false simplifications, including "every genuine doubleton is a scale of a B=6 seed" unless that statement is actually proved;
9. classify the relevant classical Diophantine machinery used in the proof—such as conic parametrization, Pell-type equations, or curve genus—as prior mathematics, and separate it from the task-specific specialization;
10. supply an exact task-local checker/certificate and a NEW immutable Result with complete Git blob SHA-1 plus SHA-256 bindings for every frozen output.

## Research value to preserve

The prior sequence has reduced a broad six-coordinate alignment problem to an exact arithmetic rarity: after `H,T,P11` are known, all remaining ambiguity is a genuine pairability-filtered doubleton and costs exactly one bit. A Diophantine normal form would explain where those exceptional bits come from instead of treating them as black-box collisions. It may expose finite primitive families, Pell-like towers, or a sharp obstruction; all three outcomes materially change how this arithmetic residue should be understood.

## Success, kill, and return criteria

Terminal success is one of:

- `FINITE_PRIMITIVE_C1_C2_PARAMETER_FAMILIES_COMPLETE`;
- `DIOPHANTINE_NORMAL_FORMS_COMPLETE_WITH_NONRATIONAL_PARAMETER_COMPONENTS`;
- `FINITE_PARAMETRIZATION_OBSTRUCTED_WITH_EXACT_ARITHMETIC_COMPONENT`.

A successful Return must prove completeness at the declared normal-form strength, not only exhibit additional examples. If a finite parametrization fails, freeze the exact obstruction and stop there. Do not enlarge the mixed-invariant grammar or infer native orientation, dimension reduction, factorization, or Full-Cell dynamics. Return a NEW immutable Result for Driver review and make no downstream task decision from the researcher lane.
