<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-NATIVE-MODEL-GROUPOID-UNIVERSALITY",
  "title": "哲学先行 Q10：Native 模型群胚与普遍量词边界",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q10-native-model-groupoid-universality",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Q1 showed that universal and canonical claims are ill-posed until the admissible model class and primitive-preserving equivalences are explicit. Q3 and Q7 showed that morphism semantics and automorphism actions control lift and naturality. Build the smallest model groupoid that makes these quantifiers mathematical.",
  "next_action": "Freeze the primitive signature and allowed isomorphisms for a nontrivial finite Full-Cell model class, place Gen12 and at least two countermodels inside or outside it explicitly, then classify existential, universal, and natural S4-lift statements over that groupoid.",
  "dependencies": [
    "RR-8C52E13D6C3202A25967",
    "RR-49FC19221CA5D69B00E6",
    "RR-1ECF8B93CCAF6463224F",
    "RR-6A8B37CD35D18B55ADD3"
  ],
  "source_refs": [
    "RESEARCH_DOCTRINE.md",
    "driver_reviews/P000_PHILOSOPHY_FIRST_Q1_Q8_DRIVER_REVIEW_20260830.md",
    "RR-8C52E13D6C3202A25967",
    "RR-49FC19221CA5D69B00E6",
    "RR-1ECF8B93CCAF6463224F",
    "RR-6A8B37CD35D18B55ADD3"
  ],
  "evidence_status": "DRIVER_ACCEPTED_PHILOSOPHY_FIRST_Q1_Q8 / SECOND_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["P000", "philosophy-first", "model-groupoid", "universality", "canonicality", "S4", "quantifiers"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-NATIVE-MODEL-GROUPOID-UNIVERSALITY",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PHQ10",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q10：Native 模型群胚与普遍量词边界

Status: `READY / P0 / PHILOSOPHY-FIRST-SECOND-WAVE`

## Mother question

The phrase “every P000 model admits the lift” has no mathematical force until “P000 model” and “same model” are frozen. Q1 killed the existential-to-universal jump; Q3 and Q7 showed that section objects and automorphism-fixed choices depend on actual morphism semantics.

**What is the smallest explicit model groupoid on which existential, universal, and natural lift questions become well-posed and nontrivial?**

The goal is not to invent a maximum category. It is to state just enough primitive structure and allowed equivalence to make the quantifiers honest.

## Frozen inputs and scope

Start from the accepted P000 primitive substrate and current reviewed downstream bridges. Do not define the model class by requiring the desired `S4` conclusion. Do not identify carrier labels with native Cells. Any enriched relation, frame, connection, or adjacency included in an object must be typed as primitive, derived, or optional structure.

Morphisms are initially restricted to primitive-preserving isomorphisms; noninvertible morphisms may be introduced only if a concrete task answer requires them. Gen12 is an existential regression object, not the definition of the class.

## Hard target and required outputs

Hard target: `P000_NATIVE_MODEL_GROUPOID_AND_UNIVERSAL_LIFT_QUANTIFIERS_CLASSIFIED`.

Required outputs:

1. A finite explicit signature for admissible model objects and primitive-preserving isomorphisms.
2. Membership certificates for Gen12 and at least two structurally distinct finite models or exact reasons they lie outside the class.
3. A typed carrier-to-native map or action interface `rho_M` wherever such a map is actually defined; classify kernel, image, and dependence on presentation.
4. Separate exact predicates for `EXISTS_LIFT(M)`, `FOR_ALL_MODELS_EXISTS_LIFT`, and `NATURAL_LIFT_FAMILY`.
5. At least one model-class counterexample that separates existential from universal strength, unless universality is proved under explicit hypotheses.
6. At least one automorphism/naturality counterexample or a proof of a fixed natural family.
7. A minimality audit showing which primitive field or morphism rule is necessary for each universal/canonical conclusion.

## Research value to preserve

Without a model groupoid, later universal theorems can accidentally quantify over presentations, witnesses, or an underspecified universe. This task creates the minimal semantic domain on which the next generation of P000 theorems can even be stated correctly.

## Success, kill, and return criteria

Success: an explicit nontrivial model groupoid supports exact existential/universal/naturality classification with countermodels or theorems whose hypotheses are stated at the correct object level.

Kill/no-go: every proposed class is shown to be either circular because it encodes the target conclusion, too weak because native invariants are presentation-dependent, or too strong because it excludes known admissible countermodels without a primitive reason.

Do not add noninvertible categorical structure or higher objects unless an exact lower-language failure witness requires them.
