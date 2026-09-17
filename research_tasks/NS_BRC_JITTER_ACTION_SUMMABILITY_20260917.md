<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-NS-BRC-JITTER-ACTION-SUMMABILITY-20260917",
  "title": "BRC Jitter Action: From Local Flip Instability to Global Summability",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The line has exact local triad flip analogues, a latent-jitter positive Gram, phase-resolved commutator continuation criteria, and shell-difference telescoping mechanisms. The unresolved bridge is whether the full infinite interaction network forces the jitter action or its nonlinear injection to remain integrable on every finite interval.",
  "next_action": "Start from the exact commutator action and latent-jitter balance laws, decompose the full interaction network into birth, transport, and coherent same-output recombination events, and seek a charging scheme that maps every dangerous injection to viscous dissipation, radial mismatch, or a telescoping shell budget without double counting.",
  "dependencies": [],
  "source_refs": [
    "research_notes/ns_brc_program_handoff_20260917.md",
    "research_notes/ns-coupled-polarization-20260910.md",
    "research_notes/ns-orthogonal-response-barrier-20260910.md",
    "research_notes/ns-inexact-newton-error-ledger-20260909.md"
  ],
  "evidence_status": "RESEARCH_PROGRAM_INTEGRATION_V1",
  "last_progress_ref": "research_notes/ns_brc_program_handoff_20260917.md",
  "last_progress_at": "2026-09-17T12:53:00+08:00",
  "hard_block": "GLOBAL_JITTER_ACTION_SUMMABILITY_NOT_CLOSED",
  "tags": ["BRC", "jitter", "Navier-Stokes", "commutator", "Lyapunov", "triad-flip", "summability"],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-NS-BRC-JITTER-ACTION-SUMMABILITY-20260917",
  "parent_objective_id": "EM-NS-BRC-JITTER-REGULARITY-PROGRAM-20260917",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R-NSJA",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# BRC Jitter Action: From Local Flip Instability to Global Summability

Status: `READY / DIRECT USER RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Does the BRC residual/jitter structure force a finite total phase-resolved instability action for every smooth finite-time Navier–Stokes trajectory, thereby ruling out finite-time singularity, or can a coherent infinite interaction network defeat all known budgets?

## 1. Frozen inputs and scope

Use the exact existing objects: the phase-resolved radial commutators, latent-jitter Gram, triad flip exponent, shell-difference factors, and viscous balances. The target is the full PDE interaction network, not isolated triads.

Population labels must retain output frequency, parent frequencies, helicity, phase, radial shell, and path identity until a proved quotient is safe. Positive shell mass alone is not the target observer.

A successful negative result may construct an exact interaction network showing that the current charging rules can recycle jitter without paying a summable budget, but it must respect incompressibility and the interaction algebra actually used in the proof attempt.

## 2. Hard target and required outputs

Hard target: `GLOBAL_JITTER_ACTION_SUMMABLE_OR_EXACT_RECYCLING_NO_GO`.

Deliver all of the following, or an exact negative boundary:

1. A precise global action functional, preferably the established phase-resolved commutator or latent-jitter injection, with its scaling and exact balance law.
2. An exhaustive decomposition of nonlinear contributions into typed BRC events.
3. A charging/telescoping theorem assigning every dangerous event to a nonnegative global budget with controlled multiplicity, or an exact cycle/recycling counterexample.
4. A finite-time integrability theorem sufficient for a known continuation criterion if the positive route succeeds.
5. Explicit treatment of coherent same-output recombination and intermediate-axis-type local exponential growth; these may not be suppressed by early positive aggregation.
6. A final statement separating unconditional full-NS conclusions, geometry/helicity-conditional conclusions, and conjectural residue.

## 3. Research value to preserve

This is the conceptual bridge connecting the user's residual-accumulation/sudden-flip idea to a full PDE theorem. It tests whether BRC jitter is merely descriptive or mathematically coercive. A proof would have direct NS consequences; an exact recycling obstruction would equally reshape the portfolio.

## 4. Success, kill, and return criteria

Success is an unconditional finite-time action bound strong enough to trigger continuation, or an exact interaction-network counterexample showing the present jitter budget cannot close.

Kill any proof that counts the same dissipation repeatedly, assumes independent branches where phases couple, treats local Lyapunov growth as global blow-up, or derives infinite-scale summability only from finitely many shells.

Return the first complete charging theorem, exact recycling no-go, or the smallest missing global invariant.
