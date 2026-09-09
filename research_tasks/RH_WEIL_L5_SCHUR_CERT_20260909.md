<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RH-WEIL-L5-SCHUR-CERT",
  "title": "RH Weil compact-window positivity: rigorous Schur certificate to log(5)/2",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The finite Schur/Feshbach algebra has been audited and toolized: inverse-free residual-square bounds, conditional response-jet superconvergence with explicit remainder budgets, and an exact Schur-Bernstein whole-interval checker are verified. A boundary-regularity counterexample rules out assuming operator-norm Taylor smoothness from a fixed prime comb or smooth finite entries. The genuine Weil positivity extension from L=0.8 to L=(log 5)/2 is still unproved; the missing inputs are the exact Weil form/normalization, common carrier, genuine finite enclosure, complement coercivity, retained-port residual including boundary/far-tail effects, and complete error budgets for both parity sectors.",
  "next_action": "Start from the project handoff and global audited index, fix the exact Weil lower form and parity normalization used at L=0.8, and build one rigorous common-form-space retained/tail decomposition on L in [0.8,(log 5)/2]. Derive certified parameter and tail enclosures, then feed the resulting finite polynomial/rational lower core into the exact Schur-Bernstein interval checker. If the required regularity or coercivity fails, return the first theorem-quality obstruction instead of increasing formal jet order.",
  "dependencies": [],
  "source_refs": [
    "research_notes/RH_WEIL_SCHUR_L5_HANDOFF_20260909.md",
    "global-knowledge:knowledge/projects/enterprise-math/rh-weil-schur-handoff-index-20260909.md@b7478684f70ef8d0999426689dfcee1299ec7d05",
    "global-knowledge:knowledge/projects/enterprise-math/rh-schur-response-audit-frontier-20260907.md",
    "global-knowledge:knowledge/projects/enterprise-math/nt-tool-schur-bernstein-interval-certificate-20260907.md",
    "global-knowledge:knowledge/projects/enterprise-math/nt-tool-response-regularity-boundary-ledger-20260907.md",
    "external:teddyli18000/web-ingest@75f5e6febe792ac7d4a06affb275582bb5c3582a:temp-work/riemann-weil-research/README.md"
  ],
  "evidence_status": "AUDITED_RH_WEIL_SCHUR_HANDOFF_20260909",
  "last_progress_ref": "research_notes/RH_WEIL_SCHUR_L5_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T07:40:00+08:00",
  "hard_block": "GENUINE_WEIL_COMMON_FORM_DOMAIN_COERCIVITY_AND_INTERVAL_RESIDUAL_CERTIFICATE",
  "tags": [
    "RH",
    "Weil",
    "compact-window",
    "Schur",
    "Feshbach",
    "Bernstein",
    "response-residual",
    "BRC"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RH-WEIL-L5-SCHUR-CERT",
  "parent_objective_id": "EM-RH-WEIL-COMPACT-WINDOW-POSITIVITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "DIRECT",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
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

# RH Weil compact-window positivity: rigorous Schur certificate to log(5)/2

Status: `READY / AUDITED FRONTIER / PUBLISHED_REGISTERED`

## 0. Mother question

Can the actual compact-window Weil quadratic form be certified strictly positive for every
\(L\in[0.8,(\log 5)/2]\) in both parity sectors, using the already audited Schur/Feshbach
residual and whole-interval certificate machinery; or does the genuine infinite-dimensional
response exhibit a precise regularity, coercivity, or boundary obstruction that kills this route?

## 1. Frozen inputs and scope

Begin with `research_notes/RH_WEIL_SCHUR_L5_HANDOFF_20260909.md` and the global canonical
handoff index named in `source_refs`. Consume the audited results rather than reconstructing
them from conversation history.

Frozen results and boundaries:

- the finite Hermitian residual-square identity and inverse-free Schur lower certificate are valid;
- response-jet coefficient cancellation is valid only together with a real common carrier,
  uniform coercivity, and an explicit remainder bound;
- cubic response order is not known to be sufficient for the actual Weil family;
- the exact Schur-Bernstein checker proves a whole finite polynomial parameter interval when
  its coefficient certificates pass; endpoint or grid positivity is not a substitute;
- the existing four-core/eight-tail interval success is a synthetic regression, not Weil evidence;
- zero-extension translation can have only square-root boundary regularity, so a fixed arithmetic
  comb and smooth finite entries do not imply operator-norm Taylor smoothness;
- a form-domain residual estimate may be used only after proving its common domain, coercivity,
  port boundedness, and residual norm hypotheses;
- a Schur-core margin is not automatically a numerical lower bound for the full block operator.

Under the strict `log n < 2L` convention used in the referenced compact-window formulation,
the active prime-power set remains `{2,3,4}` through the right endpoint. If the selected exact
Weil formulation uses a different endpoint convention or normalization, record the conversion
before using this plateau fact.

The target is this finite support interval only. Do not present success here as RH, universal
Weil positivity, or positivity for later prime-power thresholds.

## 2. Hard target and required outputs

Hard target: `WEIL_L08_TO_LOG5_OVER2_STRICT_POSITIVITY_CERTIFIED_OR_RESPONSE_ROUTE_KILLED`.

Deliver the following, or replace an impossible item by an exact obstruction that explains
which hypothesis fails:

1. State the exact Weil quadratic form or rigorously justified lower form being certified,
   including Fourier/Mellin convention, support parameter, arithmetic endpoint convention,
   and even/odd parity decomposition.
2. Identify a common form domain for the whole interval and prove that the retained/tail split
   and all declared response ports are well-defined there.
3. Reconstruct or obtain the genuine finite retained block and its coupling to the complement,
   with rigorous rounding/quadrature/analytic enclosures rather than floating-point midpoints.
4. Prove a uniform complement coercivity floor on the interval, or give an exact counterexample
   showing that no such floor is available for the chosen split.
5. Bound the true retained-port residual, explicitly including parameter remainder,
   boundary-layer and far-tail contributions. Do not infer an integer Taylor order merely from
   finite matrix entries.
6. Convert the resulting finite lower core to an exact rational/interval polynomial enclosure
   whenever justified and run the Schur-Bernstein whole-interval certificate. If a direct
   Bernstein coefficient test is inconclusive, subdivision or a stronger exact polynomial
   positivity certificate is allowed, with its own proof boundary stated.
7. Close both parity sectors. If a quantitative lower bound for the full block operator is
   stated, certify the shifted full block rather than identifying it with the Schur-core margin.
8. Preserve executable/checkable artifacts and a compact handoff showing every source,
   constant, interval and failed shortcut needed for independent replay.

A valid negative completion may prove that the response-jet architecture cannot control the
actual Weil family on this interval because of a concrete domain, regularity, coercivity or
port-observability failure. The obstruction must be theorem-quality and identify the next
smallest viable carrier.

## 3. Research value to preserve

The Schur line has already converted a vague high-dimensional spectral computation into a
small future-relevant port problem with an exact residual penalty and a whole-interval finite
certificate. The remaining uncertainty is now sharply typed: whether the genuine Weil
infinite-dimensional tail admits the common carrier, coercivity and residual control needed to
make that compression mathematically legitimate.

A positive result would be a rigorously certified extension beyond the published \(L=0.8\)
base window and a reusable pattern for later threshold-by-threshold continuation. A negative
result would be equally valuable if it isolates the precise boundary or response datum that a
safe BRC quotient must retain.

## 4. Success, kill, and return criteria

Success is a rigorous certificate of strict positivity for every
\(L\in[0.8,(\log 5)/2]\) in both parity sectors under one explicit normalization, with
machine-checkable finite artifacts and independently justified infinite-tail/error bounds.

A strictly smaller but nonzero certified extension beyond `0.8` is an acceptable intermediate
return only if it also supplies a reusable continuation certificate and leaves a precisely
bounded residual interval.

Kill routes that rely only on floating-point eigenvalues, finite samples, endpoint checks,
formal response jets without actual remainder bounds, the synthetic regression as Weil
evidence, or unproved smoothness of the zero-extended infinite tail. Do not restart the already
audited finite Schur algebra unless an exact contradiction is found.

Return the first full-interval proof, rigorous nontrivial subinterval advance, or exact
regularity/coercivity/port obstruction that strictly reduces the remaining mathematical
frontier.
