<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST",
  "title": "因子盲 QR/CRT 前缀 rank/select：精确算法与完全计费边界比较",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Accepted fixed-period negative boundary and conditional paid explicit-table lower bounds are frozen. Implicit CRT/MITM prefix enumeration, rank/select correctness and full cost remain prospective; no S1/S2/S3 gain or all-N-derived impossibility is granted.",
  "next_action": "Freeze a public-N-only QR wheel model, modulus choice, exact survivor predicate, prefix query and complete cost ledger; compare the proposed CRT/MITM mechanism to primary known wheel/CRT/Fermat algorithms before selecting the one exact algorithm to prove.",
  "dependencies": [],
  "source_refs": [
    "research_tasks/FACTOR_BLIND_SQUARE_MULTIPLICATIVE_SHELL_BRIDGE_20260829.md@406f74e0e2fa833389245ebb26fc24e6e777679b",
    "research_result_records/RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE/RR-C5769D6B237D02BFF025.json@406f74e0e2fa833389245ebb26fc24e6e777679b",
    "driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/439ae263bb3a33f6a462/ROOT_FACTORBLIND_PERIODIC_SCOPE_AND_PAID_TABLE_GENUINE_DRIVER_REVIEW.md@9695951e57c4ffd7b4e100955ce758053efc7c0f",
    "research_notes/FACTORBLIND_GROWING_QR_WHEEL_EXPLICIT_COST_20261013_FBF223/ROOT_GROWING_QR_WHEEL_EXPLICIT_TABLE_NEARLINEAR_BOUND.md@77bac03c5c9a3ec587664095ddc54ab3f4efffb8",
    "research_result_reviews/RR-C5769D6B237D02BFF025/DR-B819FB64CA4E7836CA35.json@a84a011d6e2644a32cd871c1032697fb571acef7"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "EXTERNAL_PRIOR_ART_DUPLICATION",
    "DRIVER_AUTO_FOLLOWUP",
    "QR",
    "CRT",
    "MITM",
    "PREFIX_RANK_SELECT",
    "PAID_COST",
    "PROSPECTIVE_MATH",
    "PRIOR_ART_COMPARISON"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST",
  "parent_objective_id": "OBJ-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EXTERNAL_PRIOR_ART_DUPLICATION",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE",
  "successor_gate": {
    "new_information_gap": "Implicit CRT/MITM prefix indexing may avoid the full-period table charged by existing bounds; exact correctness and paid comparator cost are not established.",
    "why_parent_result_does_not_close_it": "Fixed M excludes only o(T); frozen empirical failure covers named predictors. Explicit-table lower bounds do not cover implicit CRT/MITM construction, indexing or amortization.",
    "discriminating_outcomes": [
      "Exact algorithm and complete paid matched-cost theorem",
      "Exact obstruction or cost-dominance boundary for a declared representation",
      "Identified prior-art/controlled-Task duplicate with no duplicate execution"
    ],
    "kill_condition": "The proposed representation is an already known/controlled exact method, its necessary work is silently uncharged, or its claimed gain disappears against the equally optimized matched comparator.",
    "alternative_route_or_free_exploration_considered": "Reuse the accepted negative return and Source paid-table papers; retain separate residual-priority/Hart work; avoid unbounded searches over all N-derived features.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The original negative stage and files remain frozen; this prospective exact indexing/cost problem is distinct and leaves the original hard-target and parent mathematical scope open."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 因子盲 QR/CRT 前缀 rank/select：精确算法与完全计费边界比较

Status: `READY / DRIVER REVIEW FOLLOW-UP / PENDING IMMUTABLE PUBLICATION`

## 0. Mother question

Can an implicit CRT/MITM survivor representation support exact prefix rank/select at a justified fully paid cost relative to a matched factor-blind QR-wheel/Fermat comparator? This is a scoped continuation inside the still-open factor-blind shell parent Objective.

## 1. Frozen inputs and scope

Consume exact Source RR-C5769D6B237D02BFF025 (sha256:1149fb488e66bdff40cd52b79b1566400c4691b8254ec884aa113a4a4d7c934f), its old ACCEPTED/NONE DR-B819FB64CA4E7836CA35 (sha256:4c7b3f49728aaeb1c5798f0cb6d34a4e58b435beac68735cbe065b5fc439f133), the Source9695951 scope/paid-table report, and Source77bac03 growing-QR explicit-table paper. These are proved/scoped input boundaries, not proof that this prospective algorithm works. For public odd N, define a0=ceil(sqrt(N)); for a declared public modulus M and supported residue set R_N, define prefix survivors S_N(U)={0<=t<=U : (a0+t)^2-N meets the declared local QR conditions modulo M}. Preserve exact N-dependent residues and coupled CRT relationships, with gcd(N,M)>1 handled as a separately charged factor-revealing branch. Use only public N and predeclared public parameters; hidden factors/true T are verifier-only. Do not assume prime-power coverage from the existing squarefree-odd theorem. Native ontology remains X6 with this integer-offset observer explicitly scoped; retain joint relations required by later reconstruction.

## 2. Hard target and required outputs

1. Define exact rank_N(U)=|S_N(U)| and select_N(k) (domain, indexing and absent-answer behavior), modulus/prime selection and all admissible inputs. Provide one concrete deterministic implicit CRT/MITM algorithm or an exact obstruction to the proposed representation; prove soundness, completeness, no duplicate survivors and exact rank/select or clearly delimit the supported query. 2. Derive a complete paid bit/arithmetic/space cost ledger: input size, public prime/modulus construction, local root extraction, gcd checks, CRT basis, preprocessing, storage, sorting/merging, prefix queries and candidate certification; charge per-instance work, and separate any justified amortized regime. Do not treat T, hidden factors, a presieved survivor list, a free table or batch certification as a free input. 3. Perform an actual primary-source prior-art/duplication comparison against known QR-wheel/CRT/MITM/Fermat constructions using the same cost model and prefix/output conventions. State exactly what is duplicate and what information or cost gap remains. 4. Prove either a scoped paid-cost advantage/boundary against the matched comparator, a lower/obstruction bound, or an explicit unresolved boundary. A fully explicit full-period table lower bound alone does not bound implicit CRT. Any small exact verification is supplementary and must be newly authorized after claim/open; no old 600-case benchmark, fixed-M proof checker or prior census replay.

## 3. Research value to preserve

Stage handoff statement: the old Task may become native DONE/COMPLETE because its accepted narrow negative Result and substantive follow-up publication are complete. Its immutable NO_S1_NO_S2_NO_S3 disposition is not rewritten; mathematical_targets_satisfied remains false as a scientific statement, and parent OBJ-FACTOR-BLIND-SQUARE-MULTIPLICATIVE-SHELL-BRIDGE remains OPEN. This prose is not a backend closure_analysis field. This prospective Task records a scoped algorithm/cost question with S1/S2/S3 still ungranted and the all-N-derived mathematical target still open. Working Truth, Foundation, L4 and tool-integration status remain unchanged; the parent Objective remains OPEN. Preserve all frozen paper/checker bytes and original contributor identities. Existing residual-priority/Hart tasks are separate; stop if this exact prospective scope is already controlled elsewhere rather than duplicate dispatch.

## 4. Success, kill, and return criteria

PASS only for the exact proven algorithm/obstruction and paid matched-comparison scope actually delivered; positive factorization benefit additionally needs its own complete justified claim and is not automatic. NEGATIVE_BOUNDARY/PARTIAL is valid when a specific representation or cost advantage fails: preserve counterexample/obstruction, scope, unresolved residue and no-repeat instructions without claiming all algorithms fail. Kill exact duplicate work after primary-source/control evidence identifies the existing solution or Task. A merely faster uncharged query after a free full-period table is not success. A finite experiment alone is not a uniform algorithm/cost theorem. Return a self-contained proof, pseudocode, cost ledger, primary-source comparison and immutable artifact pointers for genuine later review. Do not claim, run, freeze or review under the identity of the previous author. Prospective Task publication itself grants no execution; a real authorized researcher must own its claim/open before new computation.
