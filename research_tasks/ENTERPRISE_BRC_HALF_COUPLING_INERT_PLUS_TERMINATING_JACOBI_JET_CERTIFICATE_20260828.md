<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE",
  "title": "Enterprise BRC Inert-Plus Terminating Jacobi-Jet Certificate",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-inert-plus-terminating-jacobi-jet-certificate",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Prove, refute, or strictly reduce the single terminating Jacobi-jet certificate JT2 for inert-plus primes p=6m+1 with m congruent to 2 or 3 modulo 4, preserving the already-frozen finite-tail and parameter-jet reductions.",
  "next_action": "Start from the exact terminating Phi/Psi parameter jet at z=1/2. Attack JT0 first only as a staged first digit, then the full mod-p^2 JT2 certificate. Test a terminating creative-microscoping/WZ route and a structurally distinct Frobenius/Jacobi-sum route unless one closes or refutes the target.",
  "dependencies": [
    "driver_reviews/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_FINITE_JACOBI_HARMONIC_IDENTITIES_DRIVER_REVIEW_20260828.md@main",
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-FINITE-JACOBI-HARMONIC-IDENTITIES/RR-2498834D6D9E2A3D6787.json@main",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_FINITE_JACOBI_HARMONIC_IDENTITIES_RETURN_20260827.md@main"
  ],
  "source_refs": [
    "research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_FINITE_JACOBI_HARMONIC_IDENTITIES/jacobi_jet_certificate_20260827.json@main",
    "Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665, Conjecture A14(ii)"
  ],
  "evidence_status": "DRIVER_ACCEPTED_STRICT_REDUCTION / SINGLE_TERMINATING_JT2_CERTIFICATE_OPEN / FULL_PLUS_TARGET_UNPROVED",
  "last_progress_ref": "RR-2498834D6D9E2A3D6787",
  "last_progress_at": "2026-08-28T04:25:00+00:00",
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "p-adic",
    "inert-plus",
    "Jacobi-polynomial",
    "parameter-jet",
    "creative-microscoping",
    "WZ",
    "Frobenius"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP6JT",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-FINITE-JACOBI-HARMONIC-IDENTITIES",
  "successor_gate": {
    "new_information_gap": "The reviewed result collapses the two finite identities R0/R1 and five harmonic-block quantities to one terminating mod-p^2 Jacobi-jet certificate JT2, but supplies neither an all-prime certificate nor a counterexample.",
    "why_parent_result_does_not_close_it": "Exact parameter-jet identities, Jacobi formulas, prior-art identification, and finite regression do not evaluate the required second p-adic digit uniformly for all inert-plus primes.",
    "discriminating_outcomes": [
      "Prove JT2 uniformly for both inert-plus residue classes, closing the plus branch of the weighted supercongruence conditional only on already accepted predecessors.",
      "Prove JT0 but isolate a strictly smaller exact second-digit certificate for JT1.",
      "Produce an exact counterexample to JT0 or JT2 and independently recompute it, refuting the corresponding plus target.",
      "Prove a route-specific no-go and freeze the smallest remaining Frobenius, Jacobi-sum, or terminating WZ identity."
    ],
    "kill_condition": "Any exact counterexample independently recomputed kills the relevant identity. A larger prime scan, an assumed Frobenius sign, use of Sun A14(ii) as a theorem, or reopening finite-tail bookkeeping is non-closing.",
    "alternative_route_or_free_exploration_considered": "Closing the plus route at the existing-conjecture boundary, assigning a fresh owner to the broad supercongruence, and returning to unrestricted hypergeometric exploration were considered. The one-certificate JT2 interface is strictly smaller and more discriminating.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The reviewed task is terminal at exact-reduction scope. JT2 has a new proof interface with no separate harmonic arrays or tail blocks, so a bounded continuation preserves the reduction rather than repeating the parent."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Inert-Plus Terminating Jacobi-Jet Certificate

Status: `PUBLISHED_REGISTERED / CONTINUATION / SINGLE EXACT CERTIFICATE`

## Mother question

For every prime

\[
p=6m+1,\qquad p\equiv13,19\pmod{24},
\]

prove, refute, or strictly reduce the single terminating Jacobi-jet certificate

\[
\left(a+\frac{p\Phi_{xx}}{72}\right)
\left(\Psi-\frac{p\Psi_x}{6}\right)
\equiv1+pR_p\pmod{p^2},
\tag{JT2}
\]

where all quantities are evaluated at \((x,z)=(m,1/2)\),

\[
\Phi_m(x,z)=
\sum_{k=0}^{6m}\frac{(-x)_k(-2x)_k}{(k!)^2}z^k,
\qquad
\Psi_m=(1+12z\partial_z)\Phi_m,
\]

and

\[
a=\frac{\Phi}{p}-\frac{\Phi_x}{6}.
\]

The first digit

\[
a\Psi\equiv1\pmod p
\tag{JT0}
\]

may be used as a staged subtarget, but the full task is JT2.

## Frozen inputs and scope

Freeze the accepted finite Clausen-tail reduction, reflected scalar \(R_p\), parent parameter deformation, and the exact identities that convert \(F_0,F_1,F_2,J_0,J_1\) into the value and first two \(x\)-derivatives of the single terminating \(\Phi/\Psi\) object.

Do not reopen the earlier valuation blocks or separate harmonic arrays unless an exact contradiction to the accepted reduction is produced. Treat Zhi-Wei Sun's A14(ii) only as an existing conjectural statement of the inherited target, never as a theorem dependency.

Both classes \(p\equiv13\) and \(19\pmod{24}\) are required. Finite computation is limited to falsification, recurrence validation, and certificate regression.

## Hard target and required outputs

Hard target:

`INERT_PLUS_TERMINATING_JACOBI_JET_JT2_PROVED_REFUTED_OR_STRICTLY_REDUCED`.

Required outputs:

1. a uniform proof, exact counterexample, or strictly smaller exact certificate for `(JT2)`;
2. a separate exact disposition of `(JT0)` and of the second \(p\)-adic digit;
3. a terminating derivation that controls the cutoff-sensitive \(\Phi_{xx}\) contribution;
4. explicit treatment of both \(m\equiv2\) and \(3\pmod4\);
5. at least two structurally distinct proof mechanisms seriously tested unless one closes or refutes the target;
6. exact dependency separation for WZ/creative-microscoping, Jacobi-sum, Frobenius, or \(p\)-adic inputs;
7. a deterministic checker used only as regression support;
8. a durable task return and exact smallest residue if the full certificate remains open.

## Research value to preserve

The prior route has compressed a length-\(p\), derivative-weighted supercongruence into one finite second-order Jacobi parameter jet. A proof of JT2 closes the inert-plus branch; a counterexample refutes it exactly; and a further strict reduction can expose the genuine finite-field or terminating identity without carrying obsolete tail bookkeeping.

Preserve the exact prior-art boundary: the inherited target is known as a conjecture, so progress must come from a new proof or a valid refutation rather than from relabeling the conjecture as an input theorem.

## Success, kill, and return criteria

Success is an all-prime proof of JT2 with the plus sign derived. A valid partial result may prove JT0 and isolate one strictly smaller second-digit identity whose equivalence is proved exactly.

One independently recomputed exact counterexample terminates the corresponding claim negatively. A route-specific no-go is valuable only when it rules out a precisely stated mechanism and leaves a smaller live target.

Kill any route whose main output is a larger finite prime scan, an assumed character sign, an infinite-series identity without finite truncation control, or a return to the already-eliminated harmonic-block and Clausen-tail formulation. Stop at the strongest exact statement and do not promote the result into BRC physics or Foundation semantics.
