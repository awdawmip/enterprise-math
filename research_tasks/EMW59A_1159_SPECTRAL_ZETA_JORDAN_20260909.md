<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "EM-FREE-W59A-ISSUE1159-WALLIS-SINE-ROTATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EMW59A-1159-SPECTRAL-ZETA-JORDAN",
  "title": "Issue 1159 spectral moments, Jordan totients, and even-zeta route",
  "frontier": "Exact finite determinant coefficients imply polynomial reciprocal spectral moments Z_s(M). The free-research branch derives low-order formulas, primitive-denominator Mobius/Jordan-totient formulas, a Riccati recurrence for leading even-zeta coefficients, and a primitive spectral Dirichlet-series/RH readout. The general all-s formula and the semantic strength of the RH readout remain to be independently audited.",
  "next_action": "Derive the general Newton/Riccati recurrence for Z_s(M) directly from the exact normalized spectral polynomial, prove polynomiality in M^2 and primitive Jordan-totient inversion, then justify the dominated finite-spectrum limit giving the even-zeta formula and separately audit what the primitive Dirichlet-series RH readout actually asserts.",
  "dependencies": [],
  "source_refs": [
    "research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md",
    "research-branch:free/1159-internal-phase-euler-w59a@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c",
    "research-commit:ad6fbb0a1ac98d63ff99354569ca04c0f601ee50",
    "research-commit:6bbb4454f9f2ba3cb23409846ebf414ed1dc4028"
  ],
  "evidence_status": "FREE_RESEARCH_1159_DURABLE_HANDOFF_20260909",
  "last_progress_ref": "research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:57:00+08:00",
  "hard_block": "GENERAL_SPECTRAL_MOMENT_AND_DIRICHLET_SERIES_AUDIT",
  "tags": ["EM-FREE-W59A", "issue-1159", "spectral-moments", "Jordan-totient", "zeta", "Bernoulli", "Dirichlet-series"],
  "registry_key": "RS-EMW59A-1159-SPECTRAL-ZETA-JORDAN",
  "identity_lane": "RW59ZETA",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# Issue 1159 spectral moments, Jordan totients, and even-zeta route

Status: `READY / FREE-RESEARCH INTEGRATION`

## Mother question

Can the reciprocal moments of the finite Dirichlet rotation spectrum be determined for all orders from the exact finite characteristic polynomial, and do their primitive-denominator components give a rigorous Jordan-totient and even-zeta theory with a precisely scoped Dirichlet-series readout?

## Frozen inputs and scope

Read the #1159 state-machine handoff first. Consume the exact finite determinant coefficient formula and finite spectral realization. The low-order formulas on the research branch are evidence to reproduce, not axioms.

The internal phase `tau` may be used only once its required fixed-mode limit and lower bound have been proved or explicitly imported from an audited source. Classical formulas for `zeta(2s)` and Bernoulli numbers are comparison targets, not proof premises for the finite-spectrum derivation.

The phrase `RH readout` in the research branch is deliberately not a truth claim. The task must determine whether it is an exact reformulation, a transform identity, a heuristic analogy, or something weaker. No statement may be presented as proving the Riemann Hypothesis unless an actual proof is supplied and independently verified.

## Hard target and required outputs

Hard target: `GENERAL_SPECTRAL_MOMENT_AND_DIRICHLET_SERIES_AUDIT`.

Deliver all of the following when valid:

1. Define `Z_s(M)=sum_{k=1}^{M-1} u_(k,M)^(-s)` and prove for every fixed positive integer `s` that it is a polynomial in `M^2` of degree `s`.
2. Derive a general Newton, Riccati, generating-function, or equivalent recurrence from the finite normalized characteristic polynomial; recover the known `s=1,2,3` formulas as checks.
3. Determine the leading coefficient `beta_s` intrinsically and prove its Bernoulli-number formula, or return the exact recurrence if a closed form requires a later compatibility theorem.
4. Perform primitive-denominator Mobius inversion and prove that every primitive moment is a fixed rational linear combination of Jordan totients `J_2(d),...,J_(2s)(d)`.
5. Prove the finite-spectrum dominated-tail limit that yields `zeta(2s)=beta_s tau^(2s)` from fixed-mode convergence and a summable uniform radius bound, without using the Euler product as a hidden shortcut.
6. Audit the primitive spectral Dirichlet series: define it precisely, establish its domain of convergence and Euler/arithmetic decompositions actually justified by the finite theory, and classify the branch's `RH readout` at the exact logical strength it deserves.
7. Produce explicit machine-checkable symbolic formulas for several orders beyond `s=3` to test the general recurrence and primitive inversion.

## Research value to preserve

This direction converts exact finite spectral coefficients into an arithmetic moment hierarchy. It could connect the same finite rotation carrier simultaneously to Bernoulli numbers, Jordan totients, even zeta values, and primitive denominator arithmetic without starting from a continuous Fourier spectrum.

A careful audit of the Dirichlet-series extension is especially valuable because it separates a real spectral encoding from any accidental overstatement about deep analytic conjectures.

## Success, kill, and return criteria

Success is an all-orders finite moment theorem with primitive Jordan-totient inversion, a rigorous even-zeta limit, and a logically exact classification of the primitive Dirichlet-series readout.

Kill any derivation of `beta_s` that simply substitutes the known classical `zeta(2s)` formula and then claims the finite theory discovered it. Likewise, kill any RH claim that is only a change of notation or a spectral repackaging.

If polynomiality or the primitive Jordan form breaks at some order, return the first failing order and the corrected algebraic pattern.