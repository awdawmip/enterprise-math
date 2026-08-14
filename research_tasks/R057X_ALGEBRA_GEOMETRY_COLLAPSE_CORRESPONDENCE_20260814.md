<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R057X-ALGEBRA-GEOMETRY-COLLAPSE-CORRESPONDENCE",
  "title": "R057X — Algebra–Geometry Collapse Correspondence",
  "kind": "MATHEMATICAL_RESEARCH",
  "owner": "program/r057-cross-arm-collapse-correspondence",
  "base_state": "R057_A_AND_R057G_FIRST_SERIOUS_CHECKPOINTS_FROZEN / FIREWALL_RELEASE_ELIGIBLE",
  "priority": "P0",
  "leverage": "CROSS_ARM_CORRESPONDENCE / COMMON_COLLAPSE_MOTIFS / TRANSFER_DESIGN",
  "frontier": "Compare the independently frozen R057-A and R057-G collapse grammars at semantic/operator-role level, identify robust shared motifs and transferable corrections, then route explicit post-checkpoint hypotheses back to the two arms.",
  "next_action": "Freeze the correspondence protocol, exact input-checkpoint registry and cross-arm transfer meta-protocol; stop for Driver review before detailed comparison.",
  "dependencies": [
    {
      "target": "research_inputs/R057X_ALGEBRA_GEOMETRY_COLLAPSE_CORRESPONDENCE_PACKET_20260814.md @ 15f87245314260873e611e1df5ea5383b56c5008",
      "action": "CONSUME_AS_FROZEN_PROBLEM_PACKET",
      "satisfied": true
    },
    {
      "target": "R057-A first serious checkpoint SHA256 bc991398000dd1b18ef53967a15b5f2d07c99afee8bdb17cd0a411c73d5cd6bd",
      "action": "READ_ONLY_FROZEN_INPUT",
      "satisfied": true
    },
    {
      "target": "R057-G first serious checkpoint SHA256 e7b215e6ff5b51c647d804161327b117a50dfbb213481734895b66de3afd9459",
      "action": "READ_ONLY_FROZEN_INPUT",
      "satisfied": true
    }
  ],
  "evidence_status": "CROSS_ARM_POST_CHECKPOINT_ANALYSIS / NOT_CANONICAL",
  "hard_block": null,
  "tags": ["R057X","cross-arm","collapse-correspondence","algebra-geometry","transfer"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R057X",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R057X — Algebra–Geometry Collapse Correspondence

Status: `READY / P0 / POST-INDEPENDENT-CHECKPOINT CROSS-ARM / NOT CANONICAL`

## Mother question

R057-A and R057-G have independently frozen their first serious supervised collapse grammars. Determine what structure is genuinely shared across the two representations and what should be transferred into their next grammar-evolution stage.

Use the frozen packet as the complete mathematical specification.

## Stage 0 — freeze comparison semantics first

Before detailed cross-arm comparison create, freeze and return:

- `R057X_CORRESPONDENCE_PROTOCOL_SHA256`
- `R057X_INPUT_CHECKPOINT_REGISTRY_SHA256`
- `R057X_CROSS_ARM_TRANSFER_META_PROTOCOL_SHA256`

The Stage-0 freeze must preserve:

- exact immutable A/G serious-checkpoint hashes;
- A and G use different digitizations/carriers;
- raw scores are not directly comparable across carriers without a matched bridge corpus;
- semantic-role correspondence is allowed now because both first serious checkpoints were frozen before firewall release;
- later A/G changes motivated by X must use provenance `CROSS_ARM_INSPIRED_POST_SERIOUS_CHECKPOINT`;
- target-literal baselines and teacher-center telescoping anchors are not lattice-only correspondence evidence;
- fit/correspondence/theorem statuses remain separate.

Stop after returning the three hashes.

## Stage A — frozen correspondence map

After Driver approval, consume only the already-frozen A/G checkpoints. Do not refit either arm.

At minimum compare:

- RAW ↔ RAW;
- whole endpoint chord ↔ whole endpoint chord;
- contiguous composition ↔ contiguous chord partition;
- class/turn-conditioned sparse exceptions;
- high-capacity lookup behavior;
- compact versus high-capacity error/complexity structure;
- teacher-feature-only geometric rules as unmatched transfer candidates.

Explicitly test the hypotheses in the frozen packet, especially `WHOLE_CHORD_DOMINANCE_CORRESPONDENCE` and `SPARSE_EXCEPTION_CORRESPONDENCE`.

Return a correspondence matrix and common-motif ledger before any matched-corpus fitting.

## Stage B — matched bridge probes

Only if needed, create a new matched bridge corpus/probe design that can evaluate the same local geometric motifs on both carriers.

Do not alter either source checkpoint or pretend old scores are directly comparable.

## Stage C — transfer recommendations

Produce target-specific transfer proposals for R057-A and R057-G. Proposed changes are not automatically applied.

High-priority transfer question:

> Should R057-A Stage C add an algebraic analogue of the G tangent/radial correction before merely expanding K further?

Also ask whether A's sparse K7 exception suggests a compact curvature/turn predicate that G should test instead of adding arbitrary lookup capacity.

Every transfer recommendation must record source checkpoint, target arm, motif, proposed operator/feature, complexity effect and provenance.

## Interpretation

R057X is allowed to compare A and G now because independence has already been preserved through each first serious checkpoint. The purpose of the old firewall was to make convergence informative, not to prohibit later cross-pollination forever.

## Primary return vocabulary

- `CROSS_ARM_WHOLE_CHORD_MOTIF_CONFIRMED`
- `SPARSE_EXCEPTION_STRUCTURE_CORRESPONDENCE_FOUND`
- `GEOMETRIC_CORRECTION_OPERATOR_TRANSFER_CANDIDATE_FOUND`
- `ALGEBRA_GEOMETRY_COLLAPSE_DICTIONARY_FOUND`
- `CROSS_ARM_MOTIF_NOT_ROBUST`
- `CORRESPONDENCE_OPEN`

Return executable checks and finally an artifact manifest when the task closes.
