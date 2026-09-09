<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-EMW59A-JT2-INDEPENDENT-CERTIFICATE-AUDIT",
  "title": "JT2 independent certificate, precision and scope audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "UR and QTF3 are published proof obligations; compatible uniform certificates and exact original JT2 source have not yet been independently verified.",
  "next_action": "After both immutable proof returns exist, recover their exact sources and perform the claim-by-claim compatibility audit, recording missing original inputs explicitly.",
  "dependencies": [
    {
      "task_id": "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",
      "required_artifact": "immutable proof return"
    },
    {
      "task_id": "RS-EMW59A-JT2-QTF3-FIXED-POINT",
      "required_artifact": "immutable proof return"
    }
  ],
  "source_refs": [
    "research_notes/EMW59A_JT2_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md",
    "https://github.com/awdawmip/enterprise-math/blob/587e6ee4a138c34de9d87bc90e06f17d7fe1b910/research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md",
    "https://github.com/awdawmip/chatgpt-global-knowledge/blob/f48cd4d076f61a5b804a7617158359e198b2fd5d/journal/progressive-number-theory/2026-09-09/20260909T105443%2B0800-ur-legendre-barycentric-lift.md"
  ],
  "evidence_status": "PREDECESSOR_REPORTED_FRONTIER_WITH_EXPLICIT_PROOF_SOURCE_GAPS",
  "last_progress_ref": "research_notes/EMW59A_JT2_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T04:11:39.921477+00:00",
  "hard_block": {
    "missing_object": "Immutable UR and QTF3 proof returns with reproducible artifacts",
    "owner": "GV-EMW59A-JT2-PERSISTENT-LINE-DRIVER",
    "necessity": "Independent certificate verification needs the actual returned proofs, not only their task specifications.",
    "unblock_condition": "The explicitly activated line Driver binds both exact returned Result/artifact revisions and an independent verifier, then authorizes this bounded audit."
  },
  "tags": [
    "JT2",
    "Ramanujan-Legendre",
    "handoff-20260909",
    "RW59AUDIT"
  ],
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-EMW59A-JT2-INDEPENDENT-CERTIFICATE-AUDIT",
  "parent_objective_id": "EM-FREE-W59A-JT2-RAMANUJAN-LEGENDRE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RW59AUDIT",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",
  "successor_gate": {
    "new_information_gap": "Proof compatibility and exact JT2 reduction evidence are not implied by either isolated lemma.",
    "why_parent_result_does_not_close_it": "The existing tasks target two different precisions and do not supply an independent combined audit.",
    "discriminating_outcomes": [
      "uniform compatible proof",
      "normalization or scope mismatch",
      "exact counterexample",
      "missing original theorem source"
    ],
    "kill_condition": "Any unsupported division, unmatched prime scope, or missing original target blocks positive combined certification.",
    "alternative_route_or_free_exploration_considered": "Author-only checking, a direct independent proof, and closing a falsified route were considered; independent verification preserves a distinct evidential function.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "A bounded independent audit avoids self-certification and makes the later synthesis reproducible without this chat."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# JT2 independent certificate and scope audit

## 0. Mother question

Do the returned UR-Legendre and QTF3 certificates hold uniformly on the same explicitly declared prime and coefficient-ring scope, and do their exact inputs support the predecessor's claimed reduction to the original JT2 theorem?

## 1. Frozen inputs and scope

Read `research_notes/EMW59A_JT2_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md` first, then the immutable predecessor handoff. Mathematical predecessors are `RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT` and `RS-EMW59A-JT2-QTF3-FIXED-POINT`. This is verification of that exact route, not a new theorem direction. The current user explicitly requests complete publication before this conversation closes.

Use the returned uniform proofs, not numerical pass counts. Keep CM0 and simple-root transversality as predecessor-reported completed work to recover and consume, not projects to repeat. Exact proof artifacts for them and the full original JT2 statement are not identified in the recovered handoff; register a source gap until exact source bytes and theorem locations are supplied. Do not infer a theorem statement from the name JT2. Treat the displayed UR-to-JT2 implication as conditional until its source is recovered.

The first explicit algebraic scope to check is `p>3`, `p=3n+1`, `t^2=1/2`, and `t^p=-t` in the residue field. Distinguished lifts, coefficient rings, every allowed prime class, exclusions, and valuations must be stated. Frobenius exchange in the residue field is not automatically an equality of ordinary p-th powers modulo `p^2` or `p^3`.

## 2. Hard target and required outputs

Return an independently checkable matrix of claims, exact source pins, assumptions, precision, and verdicts covering:

1. `3 B(x) = P_(2n)(x)+2P_n(x) mod p^2`, with `B(x)=P_(p-1)(-1/3,x)`, including the coefficientwise parameter-reflection/Taylor proof.
2. `(P_(2n)(t)+2P_n(t)) P_n'(t) = -p t mod p^2` and the equivalent divided-value identity. Justify every division by p.
3. The specialized Sun recurrence, differentiated recurrence, reflection-defect balance, and any extra normalization used to close UR. Determine whether the equations actually determine the needed scalar rather than merely constrain it.
4. `sum_(k=0)^(p-1) (1/3)_k(2/3)_k/((k!)^2 2^k) = sum_(k=0)^(p-1) (1/6)_k(1/3)_k/(k!)^2 mod p^3`, with the exact truncation and denominator valuations.
5. The residual differential equation, reflection assertion, and the degree/solution-space restrictions needed to infer a one-dimensional homogeneous Hasse component. A differential equation alone does not specify its solution space or normalization.
6. The exact original JT2 statement, all definitions of `G_p`, `Q_m`, `L_p`, `F_p`, `lambda_p`, `delta_p`, and the source-backed reduction map, or an explicit list of unrecovered inputs.
7. A self-contained proof audit, exact-arithmetic reproducibility certificate and negative/boundary checks. Record the two proof authors and require an independent verifier for the final mathematical verdict.

## 3. Research value to preserve

Two individually correct congruences need not compose when their prime scopes, lifts, derivative normalization, or required precision differ. This audit detects those mismatches before an integrated JT2 proof is asserted. A counterexample, a remaining scalar, or an exact missing-source certificate is a valuable result.

## 4. Success, kill, and return criteria

Success is an evidence-complete compatibility verdict covering both proof returns and the original target. Return `VERIFIED_COMPATIBLE`, `REVISION_REQUIRED`, `EXACT_COUNTEREXAMPLE`, or `SOURCE_GAP`, with exact source files and proof locations for each conclusion. These are audit verdicts, not automatic theorem acceptance.

Kill a proof step using numerical agreement as universality, a mod-p identity as a higher-precision identity, reflection symmetry without its defect, or an unsupported identification of the JT2 target. Do not redefine JT2 to the two displayed lemmas. A source gap is not a disproof of CM0 or transversality. Leave final integration blocked until its full evidence conditions hold.
