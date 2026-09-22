<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923",
  "title": "p17 Order-2 Affine Patterns: Portable Exact Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "All sixteen relaxed p17 order1 affine classes were excluded and separately consumed by Root: 154 proof nodes and170 pruning edges. These are scientific checks, not formal Driver Acceptance of the existing global T6 Result. The coupled order2 patterns remain unclassified.",
  "next_action": "Start with the smallest unclassified pattern q2-1: one positive vertical atom (q,r)=(2,1), denominator595, exponent594, q0 budgets1737 and2331. Use the common portable basis and six congruences; prove exclusion or retain an exact kernel. Submit one or a small batch of new certificates with completed_pattern_ids and next_pattern before extending.",
  "dependencies": [],
  "source_refs": [
    "research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/PROOF.md",
    "research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/portable_input.json",
    "research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/remaining_certificates.json",
    "research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/order2_problem.json",
    "research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/ROOT_REVIEW.json",
    "research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/ROOT_ORDER1_REVIEW.json"
  ],
  "evidence_status": "NEW_DIRECT_USER_SUPPORT_CERTIFICATES_NOT_PARENT_ACCEPTANCE",
  "last_progress_ref": "research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/remaining_certificates.json",
  "last_progress_at": "2026-09-23T04:27:22+08:00",
  "hard_block": null,
  "tags": [
    "T6",
    "BRC",
    "p17",
    "portable-exact-certificate",
    "two-branch-completeness"
  ],
  "claim_lease_minutes": 120,
  "identity_lane": "T6P17",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
  "successor_gate": {
    "new_information_gap": "Order2 contains same-side two-atom and opposite-side coupled patterns absent from the sixteen order1 classes.",
    "why_parent_result_does_not_close_it": "The parent frozen Result reaches p17 q0 only. New direct support reaches order1, while neither result classifies the coupled order2 affine classes.",
    "discriminating_outcomes": "Either complete exact emptiness certificates for the order2 family, or a verified local kernel with exact two-side budgets and explicit remaining H0/lower-prime completion.",
    "kill_condition": "Stop any branch that drops a feasible second integer, asserts emptiness after a resource stop, rounds a proof integer, or claims global T6/parent Acceptance from a local certificate.",
    "alternative_route_or_free_exploration_considered": "Consider modular dual inequalities and symbolic family arguments before case-by-case enumeration. Repeating order1 or generating unrelated FREE hypotheses would not address this exact new mixed-sign gap.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The bounded portable support interface can be independently executed and reviewed without reopening the frozen parent Result or inheriting its acceptance. It preserves the actual parent lineage while removing a host-specific execution dependency from this finite mathematical subproblem."
  },
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923",
  "parent_objective_id": "EM-T6-SHAPE-MOMENT-EXACT-THRESHOLD",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "policy_review": {
    "temporary_overrides": [],
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS"
  }
}
-->

# p17 order2: complete portable affine classification

## Mother question

For each of the272 explicitly supplied primitive vertical patterns of total
order2, is its p17 reciprocal-moment affine class empty under separate side
exponent-mass budgets2331? Alternatively, does a genuine local modular kernel
survive and require completion into all BRC observers H0,...,H6?

## Frozen inputs and scope

Use a=e+1, signed integer multiplicities and q0 weights w_j=17j-1,j=1,...,16.
The exact mixed moduli are17^k,k=1,...,6. An atom(q,r) has denominator
17*(17q+r), exponent-mass17*(17q+r)-1, and signed reciprocal contribution
(17q+r)^(-k). The portable problem supplies all coefficients, right sides,
side budgets and272 pattern descriptors as decimal strings. The common basis,
Gram factors and complete arithmetic requirements are in portable_input.json.
For any pattern Vplus,Vminus, set the kth right side to
-sum_(q,r in Vplus)(17q+r)^(-k)+sum_(q,r in Vminus)(17q+r)^(-k)
mod17^k; subtract each side's exact fixed atom costs from2331. This compact
rule completely specifies the inputs without opening all272 records. For
q2-1 the right side is -35^(-k), and the two q0 budgets are1737 and2331.
Begin from the compact rule below; reading the entire272-case JSON is not a startup prerequisite.

Up to overall sign the cases are16 single q2 atoms,136 same-side unordered
pairs of q1 atoms (including repeated atoms), and120 opposite-side distinct
q1 pairs. Identical opposite atoms cancel to lower order and are not primitive.
All parities and composite denominators remain. The packet deliberately includes
relaxed classes whose cofactor contains a prime above17. If the solver uses
maximal-prime admissibility to remove one, prove and label that domain exclusion;
do not claim that its larger relaxed affine class is empty.

P000 is unconditional. These coefficient arrays are auxiliary mathematics,
not extra spatial dimensions or new physical laws. No old Result Acceptance,
Working Truth, Foundation status or blind independence is inherited.

## Hard target and required outputs

Classify the entire finite family, or exhibit a verified counterexample to
its universal emptiness claim. Supply exact inputs, signed q0 vector for any
survivor, both side totals, all six mixed congruences and the unresolved full
H0/lower-prime completion. A local kernel alone is not a complete T6 collision.
For exclusion, provide an exhaustive proof tree or a stronger exact family
lemma, with no lost branches and a clear resource-exhaustion outcome.

Apply D_i>R² to retain up to two adjacent integers at every descending node;
do not reuse the stronger one-candidate rule without D_i>4R². Derive/check all
certificate inequalities from exact integers and rationals. Existing BRC
division/remainder traces and the portable BigInt verifier are reusable; a
mathematically equivalent independently checked implementation is allowed.
Persist complete portable data and a concise self-contained proof. Start at
q2-1 and return one or a small batch of newly classified patterns, with exact
completed_pattern_ids and next_pattern. The full family is the hard target;
a partial certificate must not claim family completion. Pure mathematical proof or any exact implementation is permitted.

## Research value to preserve

This continues the genuine move from a host-dependent lattice calculation to
a small, exact, independently checkable BRC proof object. It addresses new
same-side and opposite-side correlation patterns, preserving signed mass and
valuation information. It neither invents a global tool family nor repeats the
already excluded order1 units merely because their original host is absent.

## Success, kill, and return criteria

Success: complete exact classification of the272 relaxed cases, a proved
uniform exclusion of the maximal-p17-admissible subfamily with explicit domain
accounting, or a verified local kernel that refutes the proposed universal
local emptiness statement and defines a concrete completion problem.

Kill unsupported quotients, prime-only replacement, floating near-equality,
missing feasible children, fake empty results from resource limits and local
claims promoted to the global T6 threshold. A resource stop must retain the
exact completed cases and next unresolved case. The original global T6 task
and its review boundary remain intact. Publication of this task does not
approve any predecessor's mathematics; ordinary independent review applies.
