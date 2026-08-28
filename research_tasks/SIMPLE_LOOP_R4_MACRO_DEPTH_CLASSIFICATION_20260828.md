<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SIMPLE-LOOP-R4-MACRO-DEPTH-CLASSIFICATION",
  "title": "Simple-loop blocking-graph rank-4 and strict depth-9 macro family classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "No exact invariant classification yet determines whether a rank-4 simple-loop blocking motif forces an 11-run locked skeleton or supports a strict simple-to-simple macro depth 9 family; both targets remain to be proved or refuted from the geometry.",
  "next_action": "Freeze an invariant blocking digraph and blocker-rank from repeated-vertex obstruction equations, then derive the complete rank-4 candidate motif list before any bounded verification.",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SIMPLE-LOOP-R4-MACRO-DEPTH-CLASSIFICATION",
  "parent_objective_id": "OBJ-SIMPLE-LOOP-MACRO-DEPTH-INDEPENDENT-CLASSIFICATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "identity_lane": "SLR4",
  "claim_lease_minutes": 240,
  "evidence_status": "USER_DIRECTED_INDEPENDENT_CLASSIFICATION_R4_DEPTH9_UNPROVED_H6_REGRESSION_AVAILABLE",
  "last_progress_ref": "INDEPENDENT_TASK_PUBLICATION_20260828",
  "last_progress_at": "2026-08-28T14:28:11+08:00",
  "tags": [
    "Enterprise Math",
    "simple loops",
    "blocking graph",
    "macro depth",
    "positive-axis holonomy",
    "discrete Stokes"
  ],
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Research Task — Simple-loop blocking-graph rank-4 and strict depth-9 macro family classification

## Repository placement

- Suggested owner branch after a valid claim: `research/simple-loop-r4-macro-depth-classification`.
- Required return: `research_returns/SIMPLE_LOOP_R4_MACRO_DEPTH_CLASSIFICATION_RETURN_20260828.md`.
- Optional bounded exact atlas, only after structural narrowing: `artifacts/simple_loop_r4_macro_depth/`.
- The task is independent publication. It may reuse canonical definitions and frozen theorem packets below, but no prior task result is its lineage authority.

## Source files

Read and preserve the typing boundaries in:

- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`
- `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`
- `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md`

The research may also read the three journal packets listed under canonical supporting results. Any further source must be declared in the return and must not silently change the native point/displacement distinction.

## Canonical definitions to reuse

Use the positive-axis basis `e1,e2,e3` and the oriented incidence

`omega((a,b,c),(d,e,f)) = ae + bf + cd - af - bd - ce`.

For a concrete closed positive-axis word `w=g_1...g_N`, use

`A2(w)=sum_{r<s} omega(e_{g_r},e_{g_s})`

and the cyclic turn statistic

`Theta(w)=sum_r omega(e_{g_r},e_{g_{r+1}})`, with cyclic indexing.

For a positive simple closed loop of holonomy `H`, preserve the already established Stokes/Euler relation

`F=A2=2I+3H-2`

and positive orientation `Theta=+3`.

A local area-raising rhombus move is the commuting-diamond replacement that raises `A2` by `2` before imposing simple-loop admissibility. The alternate diamond vertex is the lattice vertex that the local replacement would insert. A move is simple-admissible only when the resulting embedded loop remains simple.

Equivalence of closed words is taken modulo cyclic rotation and the global `C3` relabeling `1->2->3->1`, unless a statement explicitly needs based representatives.

The notions `blocking digraph`, `blocker-rank`, `simple-to-simple packet`, and `macro depth` are NOT inherited definitions. They must be frozen exactly in this task before any classification claim.

## Canonical supporting results to reuse directly

These are regression and adversarial anchors only. They do not prove any rank-4, 11-run, or depth-9 claim.

1. All-holonomy simple positive-loop Stokes spectrum — commit `20f955c45e63cd07f5c8bf832cdf61bd08025a82`, journal `journal/enterprise-math/2026-08-26/20260826T195200+0800-q-catalan-axis-chord-all-h-stokes-spectrum.md`. It proves
   `F=3H-2+2r`, `0 <= r <= (H-1)(H-2)/2`.
2. First simple-loop local rhombus lock — commit `534f658496229d548704d7e191a9975d46161ca1`, journal `journal/enterprise-math/2026-08-26/20260826T213100+0800-first-simple-loop-rhombus-lock-h6.md`. Its canonical regression representative is
   `1^5 2^5 3^2 1 3^2 2 3^2`, with `H=6`, `F=22`, `I=3`, `Theta=+3`; the H=6 locked census reduces to one cyclic/C3 class.
3. Minimal H=6 macro unlock — commit `690088b873f4f3e39a83aec3b6458a4e792c3123`, journal `journal/enterprise-math/2026-08-26/20260826T214200+0800-h6-lock-minimal-four-letter-macro-unlock.md`. The exact regression packet is `1332 -> 2331`, with no simple-to-simple packet of support length 2 or 3 for that locked loop, `Delta F=+6`, `Delta I=+3`, and `Delta Theta=0`. One shortest adjacent-transposition realization has five swaps:
   `1332 -> 3132 -> 3312 -> 3321 -> 3231 -> 2331`,
   with incidence increments `+2,+2,-2,+2,+2`; every intermediate embedded loop is non-simple.

The distinction `ALGEBRAIC_PRIMITIVITY != PRIMITIVITY_RELATIVE_TO_SIMPLE_GEOMETRIC_SUBSPACE` is a regression guard. Do not manufacture a new fundamental BRC generator merely because a macro is primitive inside the simple-loop subspace.

## Mother question

Can global simple-loop locking be classified by an invariant finite blocking object rather than by holonomy-specific census, and at the first genuinely rank-4 obstruction does that object force an 11-run turn skeleton and a strict simple-to-simple macro depth of 9?

The two numerical claims are hypotheses, not premises. The research must independently prove or refute each one. A clean counterexample, impossibility theorem, or corrected sharp value is a successful scientific outcome if exact.

## Frozen inputs and scope

Work only with positive-axis closed words whose embedded boundary is simple in the native triangular/overlapping-circle-cell plane. Preserve holonomy, cyclic/C3 quotienting, oriented incidence, Stokes/Euler quantities, and the distinction between algebraic word moves and moves admissible inside the simple geometric subspace.

For every area-raising reflex corner, derive the alternate rhombus vertex directly from the local word and lattice coordinates. If that alternate vertex is already occupied by a nonlocal boundary occurrence, record the obstruction as a dependency from the reflex corner to the blocking boundary occurrence. Repeated-vertex equalities must be written as exact lattice-coordinate equations before graph compression.

The first phase is symbolic/structural. Finite enumeration is permitted only after the blocking equations reduce the candidate family to a bounded, explicitly justified search space. A raw scan at the next holonomy is not evidence for a universal theorem.

## Hard target and required outputs

1. Freeze a label-invariant blocking digraph `B(gamma)` for a positive simple loop and an invariant blocker-rank `R(gamma)` or prove that no such rank satisfying the stated invariance/obstruction role exists.
2. Derive the exact repeated-vertex blocking equations that characterize an edge of `B(gamma)`, including all orientation and locality conditions needed to exclude false blockers.
3. Classify the minimal locked motifs at blocker-rank `R=4` modulo cyclic/C3 equivalence, or prove that rank 4 is empty/nonminimal under the correct definition.
4. Prove or refute: every minimal rank-4 locked motif forces an 11-run turn skeleton. If false, return the smallest exact counterexample and the corrected structural invariant.
5. Define simple-to-simple packet support and macro depth `d(gamma)` intrinsically. Prove or refute the existence of a strict family with `d(gamma)=9`, and state whether 9 is local, family-specific, or universal.
6. For every sharp unlock family used in the proof, give an exact packet replacement, its support length, `Delta A2`, `Delta F`, `Delta I`, `Delta Theta`, a shortest adjacent-transposition realization in unrestricted path space, and a proof that every shorter candidate fails or leaves the simple-loop subspace.
7. Attempt an all-holonomy structural upper bound for macro depth from the blocking equations. If no such bound is true in the frozen model, supply an exact unbounded family or a decisive obstruction explaining why the proposed route cannot yield one.
8. Produce a bounded exact machine-checkable atlas only after Items 1–3 have structurally narrowed the search; the atlas must include canonical representatives and sufficient certificates to replay every classification claim.

Hard target state:

`SIMPLE_LOOP_R4_BLOCKING_MOTIF_AND_MACRO_DEPTH_CLASSIFIED_OR_EXACTLY_REFUTED`

## Research value to preserve

This task tests whether the first H=6 phenomenon is the beginning of a finite obstruction calculus or an isolated occupancy accident. A successful blocking-graph theorem would convert nonlocal simplicity failure into a composable finite object, separate geometric from algebraic primitivity, and give a principled route to higher-holonomy macro-depth results without blind census. A sharp refutation is equally valuable because it prevents a misleading rank/depth hierarchy from being promoted from one low-holonomy example.

## Success, kill, and return criteria

SUCCESS requires exact definitions plus one of the following: a complete rank-4 motif classification with proved 11-run/depth behavior, or an exact refutation that replaces the conjectural numbers with the correct invariant statement. Every theorem depending on bounded computation must include enough data or code-level specification for independent replay.

KILL the rank-4 route if blocker-rank cannot be made invariant without arbitrary labels, if rank-4 motifs are empty/nonprimitive under the correct object, or if repeated-vertex equations collapse to holonomy-specific accidental occupancy with no stable motif semantics. KILL the 11-run or depth-9 subclaim immediately upon a verified counterexample; do not repair it by changing definitions after seeing the counterexample.

RETURN a single rigorous report at `research_returns/SIMPLE_LOOP_R4_MACRO_DEPTH_CLASSIFICATION_RETURN_20260828.md` containing: frozen definitions, proof/counterexample packet, exact representatives, bounded-search certificate if used, regression replay against the H=6 anchor, theorem-status table, and the recommended next mathematical route. Task completion is task-terminal only and does not silently assert completion of the broader simple-loop program.

## Required proof discipline

- Derive blocker equations before enumerating candidates.
- Keep based-word, cyclic, and cyclic/C3 counts separate.
- Distinguish packet support length from adjacent-transposition distance.
- Distinguish algebraic realizability from simple-loop admissibility at every intermediate state.
- Treat `11` and `9` as falsifiable targets; never encode either into the definition of rank or depth.
- If a computational specialization is used only as a collision filter, replay all surviving identities exactly before theorem status is assigned.

## Regression checks

At minimum, the final definitions must replay the H=6 locked representative and explain its two blocked area-raising reflex moves. They must also reproduce the known simple-to-simple unlock `1332 -> 2331`, the `+6` incidence/face gain, the `+3` interior-cell gain, and the fact that the five-swap unrestricted factorization exits the simple-loop subspace at every intermediate state.

## Forbidden shortcuts

Do not use a blind H=7 or larger census as proof of the structural theorem. Do not define blocker-rank by the desired answer. Do not use static equal-lens overlap area as a hidden weight. Do not identify the primitive simple-loop macro with a new primitive Path-formal/BRC generator. Do not silently quotient native point addresses by the diagonal displacement relation. Do not promote exploratory numerical evidence to theorem status without an exact certificate.
