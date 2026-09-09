<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R1160A-GREGORY-MACHIN-RATIONAL-ATOM-GENERATOR",
  "title": "Gregory-Machin bounded rational-atom generator completeness",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Replace raw coprime-pair enumeration of bounded primitive rational turns by an exact Gaussian-prime direction/exponent generator with a proved completeness and duplicate-control boundary.",
  "next_action": "Read the #1160 durable handoff, reconstruct the H=1000 atom universe from exact Gaussian signatures, and formulate a candidate generation theorem whose output can be compared one-for-one with the existing 304191-atom baseline.",
  "dependencies": [],
  "source_refs": [
    "research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md",
    "research_notes/GREGORY_MACHIN_GAUSSIAN_VALUATION_LATTICE_20260903.md",
    "research_notes/GREGORY_MACHIN_RATIONAL_SUPPORT2_H1000_PARETO_20260904.md",
    "research_notes/experiments/gregory_machin_rational_support2_h1000_census_20260904.py"
  ],
  "evidence_status": "SOURCE_BACKED_OPEN_FRONTIER",
  "last_progress_ref": "research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:30:46+08:00",
  "hard_block": null,
  "tags": ["R1160", "gregory-machin", "rational-turn", "gaussian-valuation", "generator", "pareto"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R1160A-GREGORY-MACHIN-RATIONAL-ATOM-GENERATOR",
  "parent_objective_id": "EM-OBJ-1160-GREGORY-MACHIN-DISCRETE-WINDING",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1160A",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:8ac3d9c2fa05d6e96b01415562970e7b856d38e44479aa76fbf99ca875959fb6",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Gregory-Machin bounded rational-atom generator completeness

Status: `READY / SOURCE_BACKED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

Can the complete finite universe of primitive positive rational-turn atoms

\[
[b+ai],\qquad 0<a<b,\qquad \gcd(a,b)=1,
\]

under a declared coordinate-height or bit budget be generated from exact Gaussian-prime orientation/exponent data without scanning every coprime pair `(a,b)` in the ambient box?

## Frozen inputs and scope

The first source is `research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md`; completed predecessor mathematics in that handoff is input, not work to repeat.

Use the exact rational-turn carrier, `C8 + oriented split-prime valuation` signature, and the H=1000 support-two census as frozen source facts at their stated scopes. The baseline box

\[
0<a<b\le1000,\qquad \gcd(a,b)=1
\]

contains exactly 304,191 atoms and 202,662 normalized nonzero free valuation-direction groups.

Candidate generation and completeness evidence must use exact integer/rational arithmetic. Numerical `pi` or inverse-trigonometric fitting may not choose atoms. Analytic ratios or logarithms may be used only after exact atoms exist, for explicitly typed resource ranking.

Existing project valuation/enumeration and typed-incidence-circuit machinery should be reused where it covers the required operation. The task-specific gap is the arithmetic generation and bounded completeness of primitive rational-turn atoms, not a new generic circuit calculus.

## Hard target and required outputs

1. Give an exact generator specification from Gaussian-prime direction/exponent data, including sign/octant, ramified-2 handling, primitive reduction and positive-scale equivalence.
2. Prove a completeness theorem for one declared finite resource universe: every admissible primitive atom in the universe is produced.
3. Prove or implement duplicate control strong enough to state exactly when two generated descriptions represent the same primitive atom.
4. Provide an executable exact checker that reproduces the H=1000 regression baseline, including the 304,191 atom count and 202,662 free-direction group count, without using the old full coprime-pair scan as the production algorithm. A brute-force enumerator may be retained only as the independent finite oracle for this regression.
5. Apply the generator to at least one strictly larger declared resource bound and report generation count, deduplication count, runtime-relevant structural statistics and any new obstruction.
6. If no asymptotic improvement over raw enumeration survives exact completeness and deduplication, return a negative theorem or complexity obstruction rather than preserving a nominal generator.

## Research value to preserve

The current generalized #1160 program is blocked computationally by atom-universe construction, not by endpoint recognition. A complete arithmetic generator would make larger support-two and support-three Pareto searches feasible while preserving the exact native/completion boundary. A negative result would be equally valuable because it would prevent later researchers from repeatedly rebuilding an unhelpful prime-direction generator.

## Success, kill, and return criteria

**Success:** an exact source-backed completeness statement plus a reproducible checker matching the H=1000 baseline and one larger finite experiment, with the generation/deduplication mechanism stated precisely enough for the support-three task to consume.

**Kill:** a proof or decisive exact experiment showing that the proposed Gaussian-prime generation necessarily reconstructs essentially the same ambient pair universe at the declared resource scale, with no usable structural reduction after duplicate control.

**Return:** provide the theorem or obstruction, exact finite scope, checker and regression counts, tool-reuse classification, and the smallest next unresolved boundary. Do not claim global optimality from a bounded generation theorem.
