<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-QRF-R3-INDEPENDENT-FOUNDATION-VERIFICATION",
  "title": "QRF-R3 Independent Foundation Verification — Oriented Origin Triangle and Positive Atlas",
  "kind": "RESEARCH",
  "owner": "research/qrf-r3-independent-foundation-verification",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Independent falsification-oriented verification of one audited quadratic-refoundation replacement candidate.",
  "next_action": "Reconstruct the candidate from frozen premises, attack the weakest hypothesis set, and return a proof, counterexample, or exact downgrade.",
  "dependencies": [
    "QRF Phase-B validation packet",
    "Enterprise Math source snapshot main@d16877c3b62a7d3b7568780c732f610c260c13c1",
    "current foundational-logic and native-semantics contracts"
  ],
  "source_refs": [
    "awdawmip/chatgpt-global-knowledge@1f037142d90ed3f326cabffc5d5d8d2c6274d4a1:journal/enterprise-math/2026-08-22/20260822T152200+0800-quadratic-refoundation-phase-b-validation.md",
    "awdawmip/enterprise-math@d16877c3b62a7d3b7568780c732f610c260c13c1:research_axiom_candidate_state_machine.json",
    "awdawmip/enterprise-math@d16877c3b62a7d3b7568780c732f610c260c13c1:FOUNDATIONAL_LOGIC.md",
    "awdawmip/enterprise-math@d16877c3b62a7d3b7568780c732f610c260c13c1:native_semantics_admissibility.json"
  ],
  "evidence_status": "INDEPENDENT_VERIFICATION_TASK_READY",
  "last_progress_ref": "awdawmip/chatgpt-global-knowledge@1f037142d90ed3f326cabffc5d5d8d2c6274d4a1:journal/enterprise-math/2026-08-22/20260822T152200+0800-quadratic-refoundation-phase-b-validation.md",
  "last_progress_at": "2026-08-22T15:22:00+08:00",
  "hard_block": null,
  "tags": [
    "qrf",
    "foundation-facing",
    "falsification",
    "independent-verification",
    "replacement-candidate"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "QRF3",
  "origin_kind": "FREE_AXIOM_CANDIDATE",
  "origin_candidate_id": "QRF-R3",
  "origin_candidate_state": "AUDITED_REPLACEMENT_CANDIDATE",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9cb0f9abbec5b946fb67557c2ef8e7d371df3e5aa059d409da1192a55cf0eac2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# QRF-R3 Independent Foundation Verification — Oriented Origin Triangle and Positive Atlas

Status: `READY / DRIVER_APPROVED / DISPATCHABLE`

## 0. Task-local mother question

Is one `C2` orientation datum together with the unlabeled origin triangle exactly necessary and sufficient to generate the three positive direction families and the min-zero address atlas, without importing extra labels, Euclidean orientation, or the forbidden native diagonal quotient?

The task is to attack necessity, sufficiency, and layer typing independently.

## 1. Frozen task-local inputs and scope

Start from an unlabeled elementary origin triangle in the triangular carrier and its translation structure.

The candidate may use one binary cyclic-orientation choice.

Axis names are gauge labels only.

The carrier translation group may have three directed generators with carrier-only relation

`e1+e2+e3=0`.

The native address target is the set of nonnegative triples with minimum zero.

Do not assume native equivalence under common diagonal shifts. Any diagonal relation used in the proof must remain explicitly typed as a carrier decoding fact.

Do not assume metric angles, embedded Euclidean coordinates, or a pre-existing positive orientation.

## 2. Required mathematical / executable / formal outputs

### A. Exact no-section theorem

Prove or refute that the two cyclic orientations of the unlabeled triangle form a `C2` torsor under the full triangle automorphism group, with reflections exchanging the two sheets.

Conclude precisely what bare incidence cannot canonically select.

### B. Sufficiency of one orientation datum

Starting only from the oriented triangle and translation classes of its directed boundary edges, construct the three positive direction families.

Show equivariance under cyclic relabeling and describe reflection as orientation reversal rather than a hidden fourth choice.

### C. Minimality attack

Try to remove the orientation bit.

Search for any already-available datum in the frozen substrate that canonically selects one sheet. If such a datum exists, the bit is redundant and the candidate must be narrowed.

Conversely, check whether one bit is actually insufficient because an additional axis label, base edge, metric orientation, embedding, or ordering is needed.

### D. Min-zero decoder theorem

Prove the existence and uniqueness of the min-zero representative for each carrier displacement using the kernel of the carrier map.

Then audit the proof line by line for semantic leakage: the diagonal kernel may justify normalization of a carrier representative, but must not become native ontic equivalence.

### E. Representation-versus-ontology audit

State exactly what is generated:
- positive direction families;
- gauge-labeled coordinates;
- carrier-to-native normal-form decoding.

State exactly what is not generated:
- a native diagonal quotient;
- a metric angle convention;
- a unique global axis labeling beyond gauge;
- any path-fiber collapse.

## 3. Success, kill, and return criteria

Return exactly one leading verdict:

- `VERIFY_R3_MINIMAL_C2_REFOUNDATION`
- `VERIFY_R3_ONLY_WITH_EXTRA_TYPED_DATUM`
- `DOWNGRADE_R3_BIT_REDUNDANT`
- `REJECT_R3_LAYER_LEAK_OR_NONCANONICALITY`

Strict verification requires:

1. an exact automorphism/torsor obstruction for bare incidence;
2. sufficiency of one orientation datum;
3. proof that no smaller frozen datum selects a sheet;
4. an exact min-zero uniqueness theorem;
5. no use of the carrier diagonal relation as native equivalence;
6. explicit relabeling/reflection behavior.

Kill or downgrade if:
- a canonical orientation is already determined without the bit;
- one bit does not suffice without additional hidden structure;
- the atlas construction depends on metric embedding rather than incidence and translation;
- the normal-form proof reinstates the forbidden native quotient.

Return the smallest corrected primitive package if the original candidate is too strong or too weak.
