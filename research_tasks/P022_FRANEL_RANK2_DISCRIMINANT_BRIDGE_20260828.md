<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-FRANEL-RANK2-DISCRIMINANT-BRIDGE",
  "title": "P022 Franel Rank-Two Discriminant Bridge",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "BLOCKED",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Prove or refute that on the admissible q=18m-1 primitive-twin boundary, q | F_(6m) forces the nonsquare rank-two cusp-transfer discriminant sector, equivalently (-2/q)=-1, by coupling the Franel second-order cusp transfer to the accepted Hahn/conductor-18 boundary functional.",
  "next_action": "Construct an exact 2x2 connection, Cartier, Hasse-Witt, or Casoratian minor linking the boundary coefficient F_(6m) or its Hahn diagonal to the Franel cusp first-jet state; compute its determinant and quadratic character, then prove the boundary-zero implication or freeze the smallest exact failure mechanism.",
  "dependencies": [
    "RS-P022-OBSERVATION-HISTORY / TP2-2346F5D3E731ED56DB0A terminal handoff or explicit release",
    "research_result_records/RS-P022-FRANEL-FIRST-REENTRY-KERNEL-NONVANISHING/RR-EF198E9B037C152CD050.json",
    "research/p022-observation-history-d5d438@65915c88313800e68b9340cfe1c295b10192c8fd"
  ],
  "source_refs": [
    "docs/P022_BARLOW_FRANEL_BOUNDARY_RANK2_PULLBACK.en.md@65915c88313800e68b9340cfe1c295b10192c8fd",
    "docs/P022_BARLOW_FRANEL_BOUNDARY_DUAL_HASSE_ADJOINT.en.md@65915c88313800e68b9340cfe1c295b10192c8fd",
    "docs/P022_BARLOW_FRANEL_BOUNDARY_CONDUCTOR18_THREE_SECTION.en.md@65915c88313800e68b9340cfe1c295b10192c8fd"
  ],
  "evidence_status": "RESEARCHER_RESIDUE_CAPTURE / PARENT_EXECUTION_ACTIVE / RANK2_CUSP_TRANSFER_DISCRIMINANT_BRIDGE_PROVED_WIP / ALL_M_BOUNDARY_NONVANISHING_OPEN",
  "last_progress_ref": "research/p022-observation-history-d5d438@65915c88313800e68b9340cfe1c295b10192c8fd",
  "last_progress_at": "2026-08-28T03:00:16+00:00",
  "hard_block": "PARENT_EXECUTION_ACTIVE_RS-P022-OBSERVATION-HISTORY_TP2-2346F5D3E731ED56DB0A",
  "tags": [
    "P022",
    "Franel",
    "rank-two",
    "cusp-transfer",
    "discriminant",
    "Legendre-symbol",
    "Cartier",
    "Casoratian",
    "Hahn",
    "conductor-18"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-FRANEL-RANK2-DISCRIMINANT-BRIDGE",
  "parent_objective_id": "P022_OBSERVATION_HISTORY_IDENTIFIABILITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022R2D",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P022-OBSERVATION-HISTORY",
  "successor_gate": {
    "new_information_gap": "The active parent execution has isolated a natural rank-two Franel cusp-transfer determinant with quadratic character (-2/q), but it has not proved that vanishing of the one-third boundary coefficient forces the nonsquare determinant sector.",
    "why_parent_result_does_not_close_it": "The accepted Hahn reduction and the parent conductor-18/dual-Hasse work identify equivalent scalar boundary obstructions; the dual-Hasse scalar first jets are formally adjoint and therefore not independent. The remaining load-bearing step is a genuinely matrix-level connection between the boundary functional and the rank-two transfer discriminant.",
    "discriminating_outcomes": [
      "A proof that q | F_(6m) implies (-2/q)=-1 for every admissible twin-boundary m closes the q=3r-1 first-reentry boundary.",
      "An admissible exact counterexample with q | F_(6m) but (-2/q)=+1 refutes the discriminant bridge and identifies the smallest failure mechanism.",
      "An exact equivalence with a smaller 2x2 Cartier, Casoratian, Hasse-Witt, or Hahn connection minor relocates the sole blocker to a named matrix invariant."
    ],
    "kill_condition": "Kill any route that only enlarges finite scans, reuses the already-redundant scalar dual-Hasse first-jet relation as an independent condition, assumes generic Frobenius nonvanishing, or infers the boundary-zero implication merely from the identity det(A0)=-9/8.",
    "alternative_route_or_free_exploration_considered": "Continuing only inside the broad observation-history task, opening another scalar hypergeometric route, and unrestricted free exploration were considered. The rank-two bridge is captured separately because it is now a distinct matrix-level theorem with a sharp quadratic-character endpoint; execution remains blocked while the parent line is active.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent task has already compressed several scalar and p-adic routes and is still active. A typed blocked continuation preserves the newly isolated rank-two theorem without creating duplicate execution, while giving the later runtime one precise proof obligation once the parent releases it."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P022 Franel Rank-Two Discriminant Bridge

Status: `PUBLISHED_REGISTERED / CONTINUATION / BLOCKED_MATRIX_FRONTIER`

## Mother question

At the first dangerous primitive-twin Franel boundary, write

\[
r=6m,\qquad q=18m-1,
\]

with \(q\), \(12m-1\), and \(12m+1\) prime. The accepted arithmetic reduction identifies the remaining boundary obstruction with

\[
q\mid F_{6m},
\]

equivalently with vanishing of the accepted Hahn diagonal and of the sign-free conductor-18 boundary kernel.

The rank-two Franel pullback exposes a natural cusp-transfer matrix

\[
A_0=
\begin{pmatrix}
-1&0\\
1&9/8
\end{pmatrix},
\qquad
\det A_0=-\frac98,
\]

so that

\[
\left(\frac{\det A_0}{q}\right)
=
\left(\frac{-2}{q}\right).
\]

Prove or refute the load-bearing implication

\[
\boxed{
q\mid F_{6m}
\Longrightarrow
\left(\frac{-2}{q}\right)=-1
}
\]

under the full admissible twin-boundary hypotheses.

## Frozen inputs and scope

The accepted Hahn exact reduction may be consumed at its reviewed strength:

\[
q\mid F_{6m}
\iff
Q_{3m}(3m;-9m,3m-1,9m)\equiv0\pmod q.
\]

The current parent execution also supplies exact task-local identities for the sign-free conductor-18 kernel, the dual-Hasse formal-adjoint relation, the rank-two Franel pullback, and the cusp-transfer matrices. Those parent-execution identities are source material for this task, but any statement not yet terminally frozen must be rechecked at the exact source revision before it is used as a premise.

The task is blocked while the parent observation-history execution remains active. When released, begin from the smallest matrix-level bridge rather than replaying the scalar reductions.

Preferred routes include:

- a \(2\times2\) connection or Cartier matrix for the second-order Franel equation;
- a Hasse-Witt or Frobenius off-diagonal minor;
- a Casoratian coupling the Hahn second-order difference operator to the Franel rank-two state;
- an exact finite-field hypergeometric or Jacobi-sum realization whose determinant character is computable.

Finite computation may falsify candidate identities and locate counterexamples. It is not proof of the all-parameter implication.

## Hard target and required outputs

Hard target:

`P022_RANK2_DISCRIMINANT_BRIDGE_PROVED_OR_REFUTED_OR_MINIMAL_EXACT_MATRIX_OBSTRUCTION_FROZEN`

Required outputs:

1. an exact rank-two object connecting \(F_{6m}\), the Hahn diagonal, or the conductor-18 boundary functional to the Franel second-order state;
2. an exact determinant, Casoratian, Cartier, or equivalent invariant with its quadratic character computed;
3. a proof that boundary vanishing forces \((-2/q)=-1\), or an admissible exact counterexample;
4. if universal closure is not reached, an exact equivalence to a strictly smaller named matrix invariant together with the precise unresolved nonvanishing statement;
5. an explicit reconnection to the \(q=3r-1\) first-reentry visibility question;
6. symbolic or exact-integer checks separated clearly from proof-level arguments;
7. a frozen return classifying the bridge as proved, refuted, or reduced to the minimal exact matrix obstruction.

## Research value to preserve

This task is the first point in the P022 boundary analysis where the mod-eight midpoint discriminator and the one-third Franel boundary obstruction meet on a natural rank-two surface.

A positive result would replace the remaining all-\(m\) Franel nonvanishing problem by one quadratic-character exclusion and close the first dangerous re-entry boundary. A negative result is equally valuable because it would prove that the cusp determinant alone is insufficient and identify the exact additional matrix datum required.

The task also creates a direct interface between the continuous rank-two Franel equation, the discrete Hahn operator, and the conductor-18 finite-field organization, rather than adding another scalar period identity.

## Success, kill, and return criteria

Return `RANK2_DISCRIMINANT_BRIDGE_PROVED` only with a proof valid for every admissible \(m\).

Return `RANK2_DISCRIMINANT_BRIDGE_REFUTED` only with an exact admissible counterexample and a verified explanation of where the proposed implication fails.

Return `MINIMAL_EXACT_MATRIX_OBSTRUCTION_FROZEN` only when the boundary-zero condition has been proved equivalent to a strictly smaller named \(2\times2\) determinant, Casoratian, Cartier, Hasse-Witt, or Hahn-connection invariant whose remaining nonvanishing is genuinely independent.

Kill a proposed closure if it relies only on a finite prime cutoff, treats the already-proved scalar formal-adjoint relation as a second independent equation, assumes positive-weight Hahn zero theory in the non-positive specialization, assumes generic Frobenius transversality, or infers the desired implication from the Legendre symbol of \(\det A_0\) without an exact connection to the boundary coefficient.
