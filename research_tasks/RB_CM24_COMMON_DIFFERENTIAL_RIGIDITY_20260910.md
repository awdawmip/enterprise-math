<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RB-CM24-COMMON-DIFFERENTIAL-RIGIDITY",
  "title": "RB degree-6 common differential constraints via elliptic factors and CM norms",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "An accepted degree-6 map f0 with exact unsquared pullback phi and the complete residual branch index are available. No common elliptic-factor or CM-norm rigidity theorem for all maps with proportional pullback has been accepted.",
  "next_action": "Verify the fixed-target common-elliptic-factor argument and its integral CM norm gate, without assuming primitive f0; prove an exact universal constraint, exhibit a counterexample, or freeze the first precise obstruction with its retained scalar and descent data.",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/0f4fc206e6c3a950cdd7c7587a455bfc829d8a33/research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909/exact_map_proof.md",
    "https://github.com/awdawmip/enterprise-math/blob/0f4fc206e6c3a950cdd7c7587a455bfc829d8a33/research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909/source_freeze.json",
    "https://github.com/awdawmip/enterprise-math/blob/0f4fc206e6c3a950cdd7c7587a455bfc829d8a33/research_result_records/RS-RB-CM24-SOURCE-EXPOSED-EXACT-MAP-CERTIFICATE/RR-F79FA3D36EF85CC4C6CE.json",
    "https://github.com/awdawmip/enterprise-math/blob/0f4fc206e6c3a950cdd7c7587a455bfc829d8a33/research_result_reviews/RR-F79FA3D36EF85CC4C6CE/DR-7D70258F6D39E9B6B00D.json",
    "https://github.com/awdawmip/enterprise-math/blob/0a3de47e91ed0c8c5fd3d5ef3a36ef0e630bb7ec/driver_reviews/RB_SIX_BLOCK_COMPLETE_HALF_SECTION_REVIEW_20260910_5816EB.md",
    "https://github.com/awdawmip/enterprise-math/blob/0a3de47e91ed0c8c5fd3d5ef3a36ef0e630bb7ec/research_result_reviews/RR-ADD4970017D408BAE050/DR-5AE91265A50B7D0B5F9F.json",
    "https://github.com/awdawmip/enterprise-math/blob/0a3de47e91ed0c8c5fd3d5ef3a36ef0e630bb7ec/research_driver_followups/DR-5AE91265A50B7D0B5F9F/DFU-B44F4018DACEEFD71E08.json",
    "https://github.com/awdawmip/enterprise-math/blob/0a3de47e91ed0c8c5fd3d5ef3a36ef0e630bb7ec/research_artifacts/RB_SIX_BLOCK_DRIVER_REVIEW_20260910_5816EB/portfolio_direction.md",
    "https://github.com/awdawmip/enterprise-math/blob/0a3de47e91ed0c8c5fd3d5ef3a36ef0e630bb7ec/research_artifacts/RB_SIX_BLOCK_DRIVER_REVIEW_20260910_5816EB/portfolio_tool_coverage.json",
    "https://github.com/awdawmip/enterprise-math/blob/0a3de47e91ed0c8c5fd3d5ef3a36ef0e630bb7ec/research_artifacts/RB_SIX_BLOCK_DRIVER_REVIEW_20260910_5816EB/portfolio_tool_coverage.run.json",
    "https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/squareclass_rr_reduction.md",
    "https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/empty_fiber_obstruction.md"
  ],
  "evidence_status": "SOURCE_EXPOSED / DRIVER_ORIGIN_UNREVIEWED_CANDIDATE / NO_RIGIDITY_PREMISE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "degree-6",
    "common-differential",
    "Jacobian",
    "CM-norm",
    "twist-descent",
    "source-exposed"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RB-CM24-COMMON-DIFFERENTIAL-RIGIDITY",
  "parent_objective_id": "RB_ENTERPRISE_THEOREM_PACKAGE_V2_INDEPENDENT_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RBV2CR",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-RB-CM24-SOURCE-EXPOSED-EXACT-MAP-CERTIFICATE",
  "successor_gate": {
    "new_information_gap": "The accepted map is one witness and the 1980 residual objects are labelled parameter systems. Neither decides whether all admissible maps sharing the differential line are constrained by the same elliptic factor and integral CM norm, with relative scalar, twists and descent retained.",
    "why_parent_result_does_not_close_it": "The exact-map Task proves one map and exact pullback; the six-block Task excludes one occupancy type. Neither proves uniqueness, a common-factor theorem, or arithmetic descent for the remaining parameter systems.",
    "discriminating_outcomes": [
      "A proved universal constraint, possibly the proposed translation/sign orbit statement, with its exact coefficient-field, differential-scalar and equivariance domain.",
      "An exact admissible counterexample to the proposed rigidity, identifying the invariant that distinguishes it from the accepted map.",
      "A proved limitation of the common-factor/CM-norm route or a smaller explicitly unresolved lemma; freeze that boundary without converting incompleteness into a theorem."
    ],
    "kill_condition": "Reject any step that sets the relative scalar to one, assumes primitive f0 or saturated lattices, identifies a twist from j alone, or drops descent/translation data. An exact contradiction to a frozen accepted premise reopens that premise; an unresolved decisive lemma yields INCOMPLETE rather than brute-force expansion or a claimed rigidity PASS.",
    "alternative_route_or_free_exploration_considered": "Reuse of the four current RB Tasks, direct per-system RR/ODE elimination, period/homology work, closure, parking and a new free exploration were considered. Existing Task source firewalls or completed local targets do not contain this source-exposed universal question. Test the structural route first; if it has a proved limitation, return the exact obstruction for the Driver to choose one targeted elimination or arithmetic route.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is a distinct bounded source-exposed common-constraint question with its own falsifiable target. Rewriting the older blind Tasks would alter frozen sources and hard targets; reopening a completed single-map/six-block Task would conflate a witness or local obstruction with a universal statement. No automatic successor follows from the prior PASS."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# RB degree-6 common differential constraints via elliptic factors and CM norms

Status: `SOURCE_EXPOSED / BOUNDED STRUCTURAL QUESTION / RIGIDITY UNPROVED`.

## Mother question

Can the accepted degree-6 map and the common pullback differential line supply a rigorous constraint on every admissible degree-6 map, through a common elliptic factor and an integral CM norm calculation? Decide the proposed rigidity statement below, or identify its exact mathematical obstruction. A common-factor argument, CM identification, norm identity and descent conclusion are proof obligations, not task premises.

## Frozen inputs and scope

Work in characteristic zero with the fixed algebraic embedding alpha > 0, alpha^4 = 3, beta > 0, beta^2 = 2, i^2 = -1 and Im(i) > 0. Put s = alpha^2 and L = Q(alpha,beta,i). The accepted certificate establishes [L:Q] = 16. Use smooth projective normalizations of

    C: t^2 = R^3 - 3R,      D: w^2 = (R+2)t,
    k = -i alpha(s beta - 2),
    lambda = 35 + 24 beta - 20s - 14s beta,
    phi = (dR/w)(1 + k/t).

The accepted input f0 has X0 = N/D0 in L(C), the exact unsquared coordinate Y0 = w delta(X0)/(t+k), delta = t d/dR, and target

    E0: Y^2 = C0 X(X-1)(X-lambda),
    C0 = -i alpha(9+3 beta+2s+4s beta)/4,
    omega0 = dX/Y,
    f0^*omega0 = phi,      deg(f0) = 6,
    j(E0) = 2417472 + 1707264 beta.

Read N, D0 and their exact source conventions from the immutable source_freeze.json and accepted exact_map_proof.md in the source references. The proof file's historical INCOMPLETE header predates RR-F79FA3D36EF85CC4C6CE and DR-7D70258F6D39E9B6B00D; that later accepted scope supplies this single-map input. Keep its base-point cancellation, twist and unsquared differential sign. This does not assert its period normalization or Jacobian lattice primitivity.

First formulate and test the geometric statement over an algebraic closure with the chosen characteristic-zero embedding: for every morphism f: D -> E0 of degree six with f^*omega0 = c phi, c nonzero, is f = epsilon f0 + T with epsilon in {+1,-1} and a constant T in E0? Do not set c = 1. If a different universal constraint is actually proved, state it exactly and distinguish it from this conjecture.

Only after establishing the geometric result, specialize to the original cover form. Its deck involution sigma fixes R,t and sends w to -w. For maps satisfying f composed with sigma = [-1] composed with f, determine which translations survive. Prove any reduction to E0[2] and to the fixed-target Klein-four transformations; do not quotient by all S4 relabelings or use an unsupported source-sign symmetry. General translated maps and centered equivariant maps are different domains and must be reported separately.

For a target twist Ed: y^2 = d X(X-1)(X-lambda) over a declared field K containing the necessary input constants, retain the exact transport isomorphism to E0, its field of definition and its multiplier on invariant differentials. Report the relation between d, the original pullback scalar and c, plus the exact Galois/descent condition. Geometric existence, K-rational maps, K-defined endomorphisms and equality of j are not interchangeable. No primitive-map, connected full kernel, saturated image lattice, homology index, or period integer may be assumed. If a lattice index is needed, prove or explicitly retain it as unresolved data.

The accepted six-block obstruction and complete corrected branch index are inputs. The remaining 540 + 1440 = 1980 objects are labelled parameter systems under the stated fixed-target normalization; they are not 1980 maps, nonempty families or irreducible components. Consume that frontier without repeating the old enumeration or the six-block certificate. Do not attempt to solve all systems as a fallback inside this Task. This Task excludes analytic period evaluation, derivation of the original B1/OmegaP value, full homology normalization, mother-objective closure, blind reconstruction claims and Foundation promotion.

All source references in the frontmatter are immutable admitted inputs. Empty dependencies means no unmet execution dependency; it does not erase these inputs. The same publication commit also contains the Driver's decision_and_reuse.md, input_manifest.json and driver_candidate_unreviewed.md under research_artifacts/RB_COMMON_DIFFERENTIAL_TASK_20260910_5816EB. Read the candidate with its authorship and unreviewed status intact.

## Hard target and required outputs

Hard target: `RB_DEGREE6_COMMON_DIFFERENTIAL_CONSTRAINT_DECIDED_OR_EXACT_BOUNDARY_FROZEN`.

1. A precise theorem, exact counterexample, proved route limitation, or explicitly incomplete reduced boundary, with quantifiers, fields, differential scalars, translations/equivariance and proof dependencies stated separately.
2. A self-contained check of the common elliptic-factor argument for homomorphisms J(D) -> E0, including connected kernels, dual images and polarizations as needed. Handle nonprimitive maps and all finite isogeny factors. Cite the exact primary theorem used and verify every hypothesis.
3. A proved identification of the required geometric endomorphism algebra/order or a precise unresolved CM gate. The task label and the numerical/formal j value alone are not a proof. Distinguish geometric endomorphisms from those defined over L or K. Derive the required integral norm equation before enumerating it, and retain relative c through the derivation.
4. A transparent exact certificate for any finite algebraic/norm calculations, with source pins, actual run receipts and meaningful tamper or counterexample tests. Reuse existing exact rings and applicable BRC/finite-relation components; no new general mechanism is authorized merely by lexical novelty. A machine calculation cannot replace the geometric argument.
5. An application statement for the full residual parameter index: specify exactly which solutions would obey the new constraint and which arithmetic/degeneracy conditions remain. If an orbit is proved, give its exact maps or transformations and their scalars/twists. Do not equate a parameter-system index with actual solution count.
6. A source-exposure and authorship statement. The Driver supplied the optional candidate; a researcher who checks it is a source-exposed non-author checker of that candidate, not a blind generator. Mark any newly authored repair separately. The Driver cannot provide the sole decisive acceptance of a claim the Driver authored; further independent decisive review must be routed when required.
7. A durable return at research_returns/RB_CM24_COMMON_DIFFERENTIAL_RIGIDITY_RETURN_20260910.md, result/proof artifacts under research_artifacts/RB_CM24_COMMON_DIFFERENTIAL_RIGIDITY_20260910/, and an immutable complete handoff manifest with exact file hashes, commands, actual outputs, failures, unresolved residue and next action. Preserve material needed after the session ends before FINAL. Current activity/CLAIM/ER/Result/Driver control protocols remain mandatory; a forward assignment itself grants no execution.

## Research value to preserve

A structural constraint could decide many candidate systems at once while preserving the relative differential and arithmetic data needed later. A counterexample or exact failed lemma would be equally useful: it identifies why common-factor/CM reasoning cannot replace a targeted RR or descent calculation. The prior map proves existence and the prior obstruction excludes one pattern; neither establishes this universal constraint. The new task was selected after checking all four existing RB publications and consuming the actual tool coverage, not because the previous Task returned PASS.

## Success, kill, and return criteria

Freeze one primary result:

- `COMMON_CONSTRAINT_PROVED`: all load-bearing steps of an exact universal constraint are proved and its geometric, equivariant and arithmetic application boundary is explicit. Claim the proposed full orbit only if it is proved. An unresolved arithmetic residue must remain named; it cannot be described as original-field closure.
- `RIGIDITY_CONJECTURE_REFUTED`: an exact admissible degree-six map or exact counterexample to a stated indispensable implication is given, with a verified distinction from the proposed orbit. Failure of one proof strategy alone does not refute rigidity.
- `COMMON_FACTOR_ROUTE_LIMITATION_PROVED`: a precise obstruction to the proposed route is proved; report the smaller extra datum or alternate route required, without claiming a universal no-go for every structural method.
- `COMMON_CONSTRAINT_INCOMPLETE`: the first unresolved decisive lemma and all proved partial facts are frozen. This is an allowed bounded return, not a satisfied rigidity hard target.

Kill unsupported compression immediately: an unjustified c=1, a field/twist identification from j alone, an unproved lattice/primitivity assumption, or a missing nonprimitive case invalidates that argument. Repair it in scope if possible; otherwise freeze the exact failure. A contradiction with an accepted frozen premise must be isolated and sent for premise review. Do not hide it by changing the inputs. Do not replace a failed structural step by a fresh 1980-system sweep or unrequested period/homology work. A Task terminal return triggers a genuine Driver portfolio choice; the RB mother remains open.
