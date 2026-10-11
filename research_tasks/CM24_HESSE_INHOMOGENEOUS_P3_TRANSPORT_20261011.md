<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT",
  "title": "CM24 explicit inhomogeneous Hesse correction and exact-half second-digit transport",
  "kind": "RESEARCH",
  "owner": "research/enterprise-cm24-hesse-inhomogeneous-p3-transport",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Unit16 proves the finite Gauss-to-Hesse comparison modulo p^2 but the uniform polynomial and exact-half comparison fail modulo p^3; no independently defined correction presently transports the second divided digit.",
  "next_action": "Freeze the explicit factorial/harmonic seed and nonhomogeneous Hesse recurrence; prove or refute their coefficientwise p^3 correction and exact-half second divided-digit transport; obtain a decisive nonauthor check of final bytes.",
  "dependencies": [
    "RR-82F6383FB6634F72B457",
    "DR-2EA60F5817976E662FA6"
  ],
  "source_refs": [
    "research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT/MCP-437d44dcd4e241aaaf32867dfe6d6368/b1e66412a436e4c99749/CM24_QUADRATIC_MOD_P2_TASK_LIFT_PROOF.md@ca7fb8a95d680cb874f6bc4444f3d5d8e87d2e24",
    "research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT/MCP-437d44dcd4e241aaaf32867dfe6d6368/b1e66412a436e4c99749/_checkpoint.json@ca7fb8a95d680cb874f6bc4444f3d5d8e87d2e24",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md"
  ],
  "evidence_status": "FROZEN_UNIT16_PRECISION_BOUNDARY_PLUS_EXPLICIT_READONLY_CANDIDATE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "CM24",
    "FINITE_ARITHMETIC",
    "SECOND_DIGIT",
    "INHOMOGENEOUS_HESSE"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "CM24P3",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE",
  "successor_gate": {
    "new_information_gap": "The known finite quadratic comparison transports g_p/p only modulo p; its p^3 failure leaves the second divided-digit coordinate transfer unexplained by an independent structural carrier.",
    "why_parent_result_does_not_close_it": "The accepted Jacobi reduction names UR/LIFT, while unit16 supplies only a p^2 finite coordinate map and a strict p^3 counterexample; neither supplies this correction.",
    "discriminating_outcomes": [
      "An independently defined factorial/harmonic seed and inhomogeneous Hesse recurrence prove the all-prime coefficientwise p^3 correction and exact-half second-digit transport.",
      "The frozen candidate fails at an explicit coefficient, endpoint, denominator, or marked exact-half value, giving a bounded counterexample and an exact remaining gap."
    ],
    "kill_condition": "Reject any exact failure, circular or fitted seed, nonunit denominator, or mere renaming of the old discrepancy without structural identification. Do not extend to period normalization, UR/LIFT acceptance, unbounded literature search, or another carrier in the same unit.",
    "alternative_route_or_free_exploration_considered": "Close unit16 at its already proved precision; wait for independent raw period calibration; or publish this arithmetic supplement separately. Free discovery is not needed for this explicit missing precision interface.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The old Task is an external-duplication audit. An exact arithmetic Task preserves that mother question and gives the new independent carrier a bounded proof and review scope."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:95971566f9870cd5097ef7bf012fd52db8e2f74f367da75e97e7c55416633990",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# CM24 finite Hesse correction and exact-half second-digit transport

Prepared for canonical Task publication; mathematics awaits independent execution and review.

Task-ID: `RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT`.
Kind: RESEARCH. Priority: P1. Leverage: HIGH.
Parent line: CM24 / accepted terminating Jacobi strict reduction.
Hard target: `CM24_FINITE_QUADRATIC_P3_CARRIER_PROVED`.
Identity lane: `CM24P3`.

## 0. Mother question

Can an independently defined finite harmonic or inhomogeneous Hesse carrier
repair the finite quadratic hypergeometric map modulo p³, and thereby
transport g_p/p modulo p² to the exact marked lifts x_±=(2±sqrt(2))/4?

## 1. Frozen inputs and scope

For p=6m+1, p≥7, freeze
f_p(w)=sum[n=0..p-1](1/6)_n(1/3)_n w^n/(n!)²,
L_p(x)=sum[n=0..p-1](1/3)_n(2/3)_n x^n/(n!)²,
q(x)=4x(1-x), and g_p=f_p(1/2).

Consume unit16's exact coefficientwise f_p(q)=L_p modulo p², the precise
counterexample at 13, and the inherited CM0 divisibility only for the target
classes p mod24 in {13,19}. These are frozen inputs, not replay units.
Accepted JT2 reduction RR-82F6383FB6634F72B457 and its review
DR-2EA60F5817976E662FA6 remain at their existing strength.

Unit16 evidence commit: ca7fb8a95d680cb874f6bc4444f3d5d8e87d2e24.
Source prefix:
research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT/MCP-437d44dcd4e241aaaf32867dfe6d6368/b1e66412a436e4c99749/.
Proof CM24_QUADRATIC_MOD_P2_TASK_LIFT_PROOF.md:
SHA256 dbe74c73a06875332cf12e7d550eedbcacf9f9a46367c447e875347490ce5632.
Checkpoint _checkpoint.json:
SHA256 5a3022f81aa708b678bc23975028c82a31302936419cd1bd2fd9ff17c5eae245.
The prior standalone audit's external-duplication hard target stays OPEN.

This Task is a bounded finite arithmetic structural comparison. It does not
repeat source inventory, select a period gauge, prove UR, decide the parent
LIFT certificate, or assert a novelty theorem. No new provider query is
required; preserve shared KQB turn b8d7d14d-77c2-4a4b-8719-e1230a7029a0
at its exhausted 3/3 standard budget.

Retain the full finite coefficient population, both exact algebraic lifts,
conjugation, branch tags, signed values, derivatives, Jacobians, and inherited
full-level h/omega^r marks. The arithmetic readout is explicitly external;
The parent native-world X6 and separately typed time remain unchanged. No
scalar identity promotes a full-X6 propagation or native spatial embedding.

## 2. Hard target and required outputs

Freeze an independent candidate J_p before target evaluation. One available
candidate is a polynomial of degree≤p-2 with one explicit factorial/harmonic
seed and the recurrence

    (j+1)²J_(j+1)-(j+1/3)(j+2/3)J_j=-2/9.

Prove or refute the uniform coefficientwise statement

    f_p(q(x))=L_p(x)+p²x^p J_p(x) modulo p³.

The initial seed must be evaluated from finite unit factorial/harmonic
products or Fermat quotient data. It may not read the evaluated discrepancy,
g_p's second digit, the UR/LIFT target, or fitted per-prime constants.
Handle every factor-entry, truncation endpoint, and denominator explicitly.
If CM0 annihilates the homogeneous Hasse ambiguity at the exact half, prove or refute whether the fixed zero-seed recurrence computes the value correction; distinguish this from the derivative, which retains its boundary dependence.

Use the formula to state the exact-half second divided-digit transport and,
when valid, the corresponding differentiated observer with branch tags.

Deliver a proof or precise counterexample, candidate-definition freeze,
task-local exact checker and finite results, method-reuse resolution,
independently checked author-input pins, and a durable next-step/handoff.
A distinct nonauthor reviewer must decisively check the final bytes before
mathematical acceptance. Mathematical acceptance and Source publication
remain separate states. Root determines checkpoint versus frozen Result
delivery through the current canonical route; no raw local draft is a Result.

## 3. Research value to preserve

The old finite map transports only g_p/p mod p and demonstrably loses its
second digit. The proposed universal inhomogeneous Hesse forcing identifies
the source of that lost information and yields an independently consumable
corrected coordinate carrier, without merely renaming a known discrepancy.
This repairs a precision interface needed by later LIFT work; it does not
supply the missing independent modular-period normalization.

The information gap is the absence of an independently evaluable p³
quadratic truncation carrier. Alternatives considered: close the already
completed unit16; await a raw period calibration; or keep the pure arithmetic
work hidden inside an external literature audit. A separate bounded Task
preserves that audit's mother question and exposes the new arithmetic scope.

## 4. Success, kill, and return criteria

Success requires an all-prime argument in the declared p=6m+1 domain,
an independent candidate definition, explicit precision/denominator bounds,
and a directly consumable exact-half formula. Finite computation supports
the proof and can falsify the candidate; finite passes alone are not a theorem.

Initial bounded regression: p=7,13,19,31,37,43; full coefficientwise p³
comparison, factor-entry and last-degree residual, exact two-branch values
and corrected second digits at 13/19, derivative transport, plus the
omitted-correction negative at 13. Do not repeat the old 77-prime scan.

Kill this candidate for a single exact failure, a nonunit denominator,
circular seed/target-fit, or only a copied high-degree discrepancy with no
new structural identification. Preserve failed formulas and counterexamples.
Do not silently switch the carrier, enlarge scope into an unbounded search,
choose period signs/roots from the desired answer, or claim UR/LIFT/global
mathematical completion. Return the exact unresolved component and next
independent route if the bounded candidate fails.
