<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-REFLECTED-DERIVATIVE-PRODUCT-BRIDGE",
  "title": "Enterprise BRC Half-Coupling Inert Plus Reflected Derivative Product Bridge",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-inert-plus-reflected-derivative-product-bridge",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "For inert primes p congruent to 13 or 19 modulo 24, prove or exactly obstruct the reduced product congruence G_p H_p congruent p+p^2 R_p modulo p^3 after the finite Clausen tail has been exactly collapsed to the reflected p^2 correction R_p.",
  "next_action": "Exploit the explicit reflected R_p rather than reopening finite-tail bookkeeping. Derive the p-adic expansion of G_p and H_p to the precision needed for G_p H_p-p, with the + Frobenius sign produced from exact arithmetic and not assumed. Test at least two distinct proof routes before returning unclosed.",
  "dependencies": ["research_result_reviews/RR-C7AAFCCFA9417B3F2C0A/DR-9291E2191AE9A09D116E.json@main","research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md@main"],
  "source_refs": ["research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE/route_audit_20260827.json@main","Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665, Conjecture A14(ii)"],
  "evidence_status": "PARENT_CLASS_SPLIT_ACCEPTED / PLUS_CLASSES_HAVE_EXACT_REFLECTED_P2_TAIL_REDUCTION / TARGET_UNPROVED",
  "last_progress_ref": "DR-9291E2191AE9A09D116E",
  "last_progress_at": "2026-08-27T09:04:00+00:00",
  "hard_block": null,
  "tags": ["p-adic","inert-primes","13-mod24","19-mod24","Clausen","reflected-tail","derivative-product","supercongruence"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-REFLECTED-DERIVATIVE-PRODUCT-BRIDGE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP4P",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-FINITE-CLAUSEN-DERIVATIVE-BRIDGE",
  "successor_gate": {
    "new_information_gap": "The parent proves that for p congruent to 13,19 mod24 the entire degree-at-least-p Clausen correction is p^2 times an explicit reflected R_p, so the remaining unknown is the product congruence for G_p H_p rather than tail cancellation.",
    "why_parent_result_does_not_close_it": "The reflected tail is explicit, but the required p-adic expansion of G_p H_p through p^2 beyond the leading +p term has not been proved.",
    "discriminating_outcomes": ["Complete proof of G_p H_p ≡ p+p^2R_p mod p^3 for both plus inert classes.","Proof for only one of 13 or 19 mod24 with an exact complementary blocker.","Exact counterexample to the reduced congruence.","A strictly smaller p-adic Gamma, Dwork, or terminating-hypergeometric identity whose proof is the sole remaining gap."],
    "kill_condition": "Any exact counterexample kills the plus-class target after independent recomputation. A route that merely extends finite primes or inserts the + sign by assumption is non-closing.",
    "alternative_route_or_free_exploration_considered": "Preferred independent lanes are p-adic Gamma/Dwork expansion of G_p,H_p and a terminating parameter deformation or higher-dimensional WZ identity. The finite tail route is already closed and must not be repeated.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent has terminally split the inert classes into distinct mechanisms. This child has a one-formula product target with no unit-tail cancellation problem, so a separate proof contract is mathematically justified."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4","review_state":"PASS","temporary_overrides":[]}
}
-->

# Enterprise BRC Half-Coupling Inert Plus Reflected Derivative Product Bridge

Status: `PUBLISHED_REGISTERED / DRIVER SUCCESSOR / CONTINUATION / EXACT_PROOF`

## Mother question

For every prime `p ≡ 13,19 (mod 24)`, prove or exactly refute the already reduced congruence

\[
G_pH_p\equiv p+p^2R_p\pmod{p^3},
\]

where `G_p`, `H_p`, and the explicit reflected correction `R_p` are frozen by the parent finite-Clausen return. Combined with `T_p≡p^2R_p`, this is exactly the plus-sign inert half of the original supercongruence.

## Frozen inputs and scope

The parent identity `S_p=G_pH_p-T_p`, the `p=6m+1` valuation blocks, the fact that only `0×2` and `2×0` tail pairs survive modulo `p^3`, and the explicit reflection formula for `B_{p-r}/p^2 mod p` are frozen inputs. Do not re-prove them unless an exact contradiction is found.

This task begins after the finite tail has been eliminated as an independent unknown. Work on the p-adic product `G_pH_p` and its first correction. The target sign is `+1` for these residue classes but must emerge from the proof; it cannot be inserted into an imported transformation.

At least two structurally distinct proof mechanisms should be seriously tested unless one already closes or refutes the target. Finite regression is falsification support only.

## Hard target and required outputs

Hard target: `INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_PROVED_REFUTED_OR_EXACTLY_REDUCED`.

Required outputs: an exact treatment of both residue classes 13 and 19 mod24; complete p-adic precision through mod `p^3`; explicit use or elimination of `R_p`; a dependency map for every imported Gamma/Dwork/hypergeometric theorem; a deterministic checker only for regression; and a durable return `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md`.

## Research value to preserve

The parent task has already transformed a difficult two-dimensional finite tail into one explicit reflected correction. The remaining plus-class problem is therefore a sharply isolated derivative-product supercongruence. Closing it would prove half of the inert residue classes without any additional finite-tail conjecture; failing it should isolate a much smaller p-adic transformation identity rather than reopen the broad all-prime problem.

## Success, kill, and return criteria

Freeze one of `INERT_PLUS_BRIDGE_PROVED`, `INERT_PLUS_TARGET_REFUTED`, `ONE_PLUS_CLASS_PROVED`, `PLUS_ROUTE_EXACT_NO_GO`, or `PROOF_NOT_CLOSED_WITH_SMALLER_IDENTITY`.

No finite prime range proves the theorem. No mod-`p^2` unweighted identity closes a derivative-weighted mod-`p^3` target. Do not reopen the minus classes or the parent tail decomposition. Stop at the strongest exact statement and return for Driver review.
