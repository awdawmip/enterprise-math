<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-QRF-R2-INDEPENDENT-FOUNDATION-VERIFICATION",
  "title": "QRF-R2 Independent Foundation Verification — Transverse Scalar Independence",
  "kind": "RESEARCH",
  "owner": "research/qrf-r2-independent-foundation-verification",
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
  "identity_lane": "QRF2",
  "origin_kind": "FREE_AXIOM_CANDIDATE",
  "origin_candidate_id": "QRF-R2",
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

# QRF-R2 Independent Foundation Verification — Transverse Scalar Independence

Status: `READY / DRIVER_APPROVED / DISPATCHABLE`

## 0. Task-local mother question

Does `Delta_a Delta_b Q=0` provide an independently meaningful local primitive for transverse scalar independence, or is it only the current sum-of-squares law rewritten after the axis boundary values are fixed?

The task must try to destroy the candidate before recommending it.

## 1. Frozen task-local inputs and scope

Work on `Q:N_0^2 -> Z` or the weakest codomain actually needed.

The candidate condition is

`Q(a+1,b+1)-Q(a+1,b)-Q(a,b+1)+Q(a,b)=0`.

For the implication to the current sector scalar, the boundary data may be supplied as

`Q(a,0)=a^2` and `Q(0,b)=b^2`.

Those boundary laws are inputs from the axis problem; this task must not re-prove them by assuming the two-variable target formula.

Do not assume Gaussian multiplication, `C4`, Euclidean geometry, Pythagoras, or the target formula away from the axes.

Competing forms such as `a^2+tau ab+b^2` are attack models, not forbidden examples.

## 2. Required mathematical / executable / formal outputs

### A. Exact discrete theorem

Prove or refute, at the weakest domain/codomain scope, that zero mixed second difference plus the two axis boundary functions forces

`Q(a,b)=Q(a,0)+Q(0,b)-Q(0,0)`,

and hence the sum-of-squares specialization when the frozen boundaries are used.

Record whether any symmetry, positivity, homogeneity, continuity, or multiplicative structure is actually unnecessary.

### B. Non-redundancy versus semantic circularity

Separate two questions:

1. Does the condition carry mathematical content relative to weaker assumptions?
2. Does it qualify as a better primitive once the axis laws are fixed?

The three integral quadratic competitors with mixed coefficient `tau=-1,0,1` should be used to test non-redundancy, but their existence alone does not prove primitive superiority.

### C. Operational meaning test

Produce an intrinsic or operational reading of transverse independence that can be checked without first computing or naming the target sum-of-squares formula.

Examples of acceptable evidence include an invariant marginal-shell statement or a local comparison rule whose equivalence to the mixed-difference equation is then proved.

If no such reading exists, say so and classify the equation as a reformulation.

### D. Coordinate and relabeling pressure

Test whether the proposed local independence is stable under the admissible chart relabelings and axis swaps relevant to the native two-channel sector.

Identify exactly which transformations preserve the statement and which would change its meaning.

### E. Boundary-strength audit

Determine whether the candidate is:
- strictly weaker than the target formula as a primitive package;
- theorem-equivalent but operationally more local;
- or only notationally different.

## 3. Success, kill, and return criteria

Return exactly one leading verdict:

- `VERIFY_R2_LOCAL_PRIMITIVE`
- `VERIFY_R2_EQUIVALENT_BUT_FOUNDATION_USEFUL`
- `DOWNGRADE_R2_REFORMULATION_ONLY`
- `REJECT_R2_SCOPE_OR_INVARIANCE_FAILURE`

Verification requires:

1. a theorem-level discrete derivation;
2. explicit weakest hypotheses;
3. a non-target operational meaning for independence;
4. chart/relabeling behavior;
5. a negative boundary showing what the candidate does not determine.

Downgrade if the condition is theorem-equivalent to the target law after frozen boundaries and no independent operational semantics survives.

Reject if an admissible model satisfies the intended operational independence but violates the mixed-difference condition, or vice versa, in a way that breaks the claimed primitive meaning.

The return must not use the Gaussian product or the current holonomy result as a premise for accepting the candidate.
