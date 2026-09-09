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
  "task_id": "RS-EMW59A-1159-HIGH-ORDER-PRECISION-RG",
  "title": "Issue 1159 arbitrary-order precision hierarchy and scaled spectral RG",
  "frontier": "The original quartic Richardson certificate has been extended in free research to an arbitrary-order dyadic annihilation hierarchy, explicit rational weights, a candidate uniform weight-condition bound below two, two-direction monotone refinement, radical-only upper/lower brackets, single-scale formal-phase certificates, a scaled spectral RG equation, and universal modified-equation correction operators. The all-orders sign and error constants need one coherent exact proof and tool extraction.",
  "next_action": "Starting from the exact finite spectral-decimation recurrence and the internal phase expansion for T_q, prove the general annihilation-filter identities and sign/monotonicity structure, then derive explicit target-free two-sided error certificates and reconcile them with the scaled RG and central-factorial modified-equation expansions.",
  "dependencies": [],
  "source_refs": [
    "research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md",
    "research-branch:free/1159-internal-phase-euler-w59a@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c",
    "research-commit:fd07b3c9a4311e4aa401c790eb774e131d4ef054",
    "research-commit:b140675ff04e728a9a1b8d84b297156c98fdbd14",
    "lean-branch:free/1159-spectral-precision-lean-w59a@269b1cafac209e42d6770b0aae4a4d8d0a981f8a"
  ],
  "evidence_status": "FREE_RESEARCH_1159_DURABLE_HANDOFF_20260909",
  "last_progress_ref": "research_notes/EM_FREE_W59A_ISSUE1159_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:58:00+08:00",
  "hard_block": "ALL_ORDER_SPECTRAL_PRECISION_CERTIFICATE",
  "tags": ["EM-FREE-W59A", "issue-1159", "precision", "Richardson", "dyadic", "spectral-RG", "modified-equation"],
  "registry_key": "RS-EMW59A-1159-HIGH-ORDER-PRECISION-RG",
  "identity_lane": "RW59RG",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# Issue 1159 arbitrary-order precision hierarchy and scaled spectral RG

Status: `READY / FREE-RESEARCH INTEGRATION`

## Mother question

Is the quartic completion bracket only the first member of an exact all-orders refinement geometry, and can the dyadic annihilation filters, radical-only bounds, scaled spectral renormalization, and central-factorial correction operators be proved as one stable precision theory?

## Frozen inputs and scope

Read the #1159 state-machine handoff first. Consume the exact finite decimation law, inverse dyadic first-mode branch, compact determinant convergence, and the already proved quartic algebraic kernel.

The later branch proposes formulas at several strengths: exact finite filter identities, analytic sign/monotonicity claims, asymptotic modified-equation expansions, and numerical stability observations. These must be separated. Do not treat an asymptotic series as a certified interval without a remainder argument.

Use only target-free internal quantities for the actual completion certificates. Classical values may be used to test decimals after a certificate is established.

## Hard target and required outputs

Hard target: `ALL_ORDER_SPECTRAL_PRECISION_CERTIFICATE`.

Deliver the strongest exact package supported by proof:

1. Define the level-`m` dyadic annihilation operator `A_m=prod_{r=1}^m (4^r E-I)/(4^r-1)` and prove exactly which inverse-power error modes it kills.
2. Prove the closed rational weight formula and audit the candidate stability identity/bound for `sum |w_(m,j)|`, including the claimed uniform bound below two if true.
3. Establish the monotone precision lattice in resolution and annihilation order, with exact hypotheses for strictness.
4. Generalize the lower-bound construction and derive radical-only upper bounds. Determine explicit target-free interval widths at several orders, not merely formal asymptotics.
5. Re-derive the single-scale arbitrary-order formal-phase certificates from the pinned source and determine which can be turned into rigorous one-sided bounds.
6. Prove the scaled finite RG identity and derive the first correction operators of the modified equation from it. Reconcile these operators with the central-factorial coefficient expansion by an independent coefficient calculation.
7. Determine a general recurrence for the universal correction operators or error eigenmodes and state the analytic conditions under which the formal expansion has a controlled remainder.
8. Extend the existing finite precision tool as a T5 precision/refinement subtool with exact rational filter weights and certified interval metadata; do not create a duplicate top-level tool family.

## Research value to preserve

A successful all-orders theory would turn the isolated fourth-order approximation into a reusable refinement geometry: resolution and extrapolation order become two monotone axes, while the finite spectral RG explains why the error modes have exactly the powers the filters annihilate.

The candidate uniform weight bound is particularly valuable because it would show that very high formal order need not be numerically ill-conditioned in this dyadic geometry.

## Success, kill, and return criteria

Success is an exact all-orders filter theorem plus at least one nontrivial family of proved target-free two-sided certificates, with the scaled-RG/modified-equation correspondence rigorously established to stated order.

Kill any argument that infers a one-sided bound solely from cancellation of an asymptotic expansion. Kill any stability claim that is based only on a handful of numerical filter weights.

If the hierarchy changes sign or loses monotonicity at some order, return the first failing level, a counterexample or exact obstruction, and the maximal surviving theorem.