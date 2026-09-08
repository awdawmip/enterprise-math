<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-1195-SELECTOR-INTERVAL-HEIGHT-CERT",
  "title": "1195: Exact Finite Selector Interval and Height Certificate",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "CP16 proves that truncated odd-selector matrices converge at scale O(rho^(N+1) N^(-1/2)) and that a certified projective enclosure narrower than the height-separation scale can uniquely identify a bounded-height integer/rational formula ray. The remaining gap is an actual auditable interval certificate for a nontrivial rank-5 1/pi^2 formula; the existing four-item demonstration is high-precision numerical evidence only.",
  "next_action": "Select the rank-5 benchmark used in CP16 or another simpler catalog row, derive rigorous enclosures for every shifted-moment matrix entry and its omitted tail at a small finite depth, propagate those intervals through the two-by-three selector kernel to a projective ray enclosure, and compare it with an explicit height-separation bound to certify the unique primitive integer coefficient ray.",
  "dependencies": [],
  "source_refs": [
    "research_notes/1195_research_handoff_index_20260909.md",
    "issue:1195#issuecomment-5540925126",
    "issue:1195#issuecomment-5533695230",
    "issue:1195#issuecomment-5533660662",
    "issue:1195#issuecomment-5533544516",
    "issue:1195#issuecomment-5540836463"
  ],
  "evidence_status": "RESEARCH_HANDOFF_INTEGRATION_V1",
  "last_progress_ref": "research_notes/1195_research_handoff_index_20260909.md",
  "last_progress_at": "2026-09-09T00:50:00+08:00",
  "hard_block": "EXACT_SELECTOR_INTERVAL_AND_HEIGHT_UNIQUENESS_CERTIFICATE",
  "tags": [
    "1195",
    "pi-power",
    "selector",
    "interval-arithmetic",
    "height",
    "finite-certificate",
    "rank5",
    "inverse-problem"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-1195-SELECTOR-INTERVAL-HEIGHT-CERT",
  "parent_objective_id": "EM-PI-POWER-SPECTRAL-SELECTOR",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1195C",
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

# 1195: Exact Finite Selector Interval and Height Certificate

Status: `READY / DIRECT USER RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Can a small finite number of pi-free shifted hypergeometric layers rigorously and uniquely identify the integer/rational polynomial coefficient ray of a nontrivial Ramanujan `1/pi^2` formula under an explicit height bound, with every matrix entry, tail, conditioning factor, and projective separation enclosed by exact rational or validated interval arithmetic?

## 1. Frozen inputs and scope

Read `research_notes/1195_research_handoff_index_20260909.md` first. Consume CP1, CP5, CP8, CP15, and CP16; do not replay the asymptotic theorem or return another decimal-only recognition experiment.

The admissible starting theorem is that the canonical complement-symmetric rank-5 terms have a base-controlled critical tail after a bounded transient and that the selector is the one-dimensional kernel of a `2 x 3` odd-moment matrix. CP16 already supplies the asymptotic identification law

`N_id(H)=2 log H/kappa + O(log log H)`

up to explicit conditioning constants. This task is to close the finite, auditable certificate layer for at least one actual formula.

The target `1/pi^2` evaluation is not needed to certify the selector and must not be used to choose the coefficient ray. Known coefficients may be used only as a post-certificate validation target after the finite enclosure has already isolated a unique bounded-height ray.

## 2. Hard target and required outputs

Hard target: `FINITE_PI_FREE_SELECTOR_UNIQUENESS_CERTIFICATE`.

Deliver all of the following, or an exact negative/minimal-depth boundary replacing an impossible item:

1. Choose one explicit convergent rank-5 formula from the Cohen–Guillera catalog and state its hypergeometric kernel, base `rho`, declared coefficient-height bound `H`, and finite depth `N` before performing coefficient recovery.
2. Give rigorous enclosures for every required shifted-moment entry of the `2 x 3` selector matrix through depth `N`. Exact rationals, rational upper/lower bounds for constants, or validated ball intervals are acceptable; unqualified decimal arithmetic is not.
3. Prove a tail bound for each matrix entry from finite hypergeometric data. Reuse the CP1 critical-tail law where valid and include the shifted logarithmic/digamma factors needed by the odd moments rather than bounding only the unshifted series.
4. Propagate the entry intervals through a kernel computation using minors, cross products, or an interval linear-algebra argument. Produce an explicit projective enclosure for `[A:B:C]` and expose its conditioning/gap factor.
5. Prove an explicit separation lemma for distinct primitive integer/rational projective rays within the declared height model. State the chosen affine chart and denominator/coordinate height convention; do not hide chart-degeneracy assumptions.
6. Certify that the projective enclosure intersects exactly one admissible height-`H` ray, and only after that compare it with the known Ramanujan polynomial as post-hoc validation.
7. Report the minimal certified depth reached by the method. If the intended four-item depth is insufficient, return the exact obstruction and the smallest depth that closes, or a rigorous lower bound on the additional information required.
8. Provide a compact reproducibility artifact or exact calculation table sufficient for another researcher to independently verify every enclosure without knowing the target value of `pi`.

An exact no-go at shallow depth is a successful result if it identifies whether the failure is caused by tail size, selector conditioning, projective chart choice, or arithmetic height separation.

## 3. Research value to preserve

The route has moved from computing `pi` accurately to identifying the formula itself from finite spectral information. CP16 shows asymptotically that analytic convergence rate and arithmetic identification precision are coupled by a height-information budget. A finite interval certificate would turn this from an asymptotic reconstruction principle into an auditable inverse theorem: finite data determines the unique low-height Ramanujan coefficient ray before the external completion is invoked.

Preserve the distinction among numerical precision, selector conditioning precision, and bounded-height identification precision. A formula may converge rapidly yet be ill-conditioned as an inverse selector, and the certificate must make that distinction visible rather than absorb it into an unspecified constant.

## 4. Success, kill, and return criteria

Success is a complete pi-free finite certificate isolating one nontrivial rank-5 coefficient ray under a declared height bound, including exact tail, conditioning, and projective separation bounds. A certified minimal-depth result or an exact shallow-depth no-go is equally acceptable.

Kill any route that uses PSLQ or rational reconstruction as proof without an enclosing uniqueness inequality, plugs the known coefficient ray into the construction before the finite enclosure is formed, uses only the unshifted tail while ignoring logarithmic shifted moments, or reports machine precision without a sound interval/rational error model.

Do not generalize to all 13 formulas before one benchmark is completely certified. Return the first end-to-end interval certificate, exact depth obstruction, or rigorously reduced remaining inequality.