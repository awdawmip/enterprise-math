# FQ-20260809-005 propagation audit — current-main closure candidate

Task: `RS-GOV-FOUNDATION-BACKFLOW`  
Publication: `TP2-2C438651496A928ADCB7`  
Researcher: `EM-GOV-76FA5C`  
Claim: `CL-P0-BACKFLOW-20260920-9fc58a6b278d`  
Work branch: `research/p0-backflow-9fc58a6b278d`  
Audited Enterprise Math main: `3ae6979a97b13062da2c0636362f4ae1a4d94f24`  
Prior branch frontier: `991322c64ac3113632e7704bfead7e4eb695aedc`  
Status: `PROPAGATION_DRIFT_VERIFIED / MINIMAL_CANDIDATE_SIMULATED / CANONICAL_WRITE_NOT_AUTHORIZED_BY_THIS CLAIM`

## Result

FQ-20260809-005 is **not an open research question** at the audited main snapshot.

The mathematical/API choice has already completed all semantic stages required before propagation:

- research RETURN: Issue #164 comment `5242436041`, frozen PR #431 head `ca351e5446b3a84835ade9509f1ab97c276841d9`;
- Steward verification: Issue #164 comment `5242447403`, status `ANSWERED / STEWARD_ACCEPTED / INTEGRATION_READY`;
- source L4 canonicalization: PR #436, merge `3a40fe680e7aad4bc458540483c3c753e15f2cc4`;
- propagation contract: Issue #164 comment `5242825481`;
- later Driver sweep: Issue #164 comment `5389854714`, classifying the remaining state as direct Foundation maintenance rather than a research successor.

Current source main independently confirms the canonical API is already live:

- `src/enterprise_math/geometry.py` blob `a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152`: `graph_distance` validates closed/symmetric/loop-free adjacency and `directed_graph_distance` preserves literal outgoing shortest-walk semantics;
- `src/enterprise_math/__init__.py` blob `66ceedcbfcba6a1447fd1297385700b1de63930a`: both helpers are exported;
- `docs/P012_INTRINSIC_DISCRETE_GEOMETRY.en.md` blob `eb087c335ec3c97b8a2ee3a56c628e0edcd5faf7`: theorem scope remains connected undirected simple graphs, with disconnected spaces handled componentwise or by an extended distance.

The previous task-local exhaustive finite check (67,234 distance queries) therefore remains relevant regression evidence and was not rerun.

## Verified propagation drift on current main

At `3ae6979a97b13062da2c0636362f4ae1a4d94f24`, the following stale state remains:

1. `foundation_steward.json` blob `cedd5b098b95f778dd89a370c35a72706452c834`
   - `problem_set.active_questions` still contains `FQ-20260809-005`;
   - no canonical `graph_distance_api` convention records the accepted boundary.

2. `research_common_surface.json` blob `8923091dbd04af2bb885bfcce723ba4724267421`
   - `foundation_steward.active_foundation_questions` still contains FQ-005;
   - `active_interface_alerts` still contains FQ-005;
   - `tool_scope_alerts.FQ-20260809-005` still states that API layering is unresolved;
   - `canonical_specializations` has no `A5_graph_distance_api` entry.

3. `foundation_backflow.json` blob `e86e59a714e65f7dd91b023033c6d154f9052067`
   - `answered_question_scheduler_links` still carries FQ-005 with next action `STEWARD_VERIFICATION_OR_CANONICALIZATION`;
   - `canonicalized_examples` lacks FQ-005.

4. `docs/RESEARCH_COMMON_SURFACE.en.md` blob `d63f114d4997f2e580da93bdf418f36ec0bacd01`
   - still contains the active FQ-005 interface alert and lists FQ-005 among active Foundation questions.

5. `docs/RESEARCH_COMMON_SURFACE.zh-CN.md` blob `7ef1651c5eb30c88ebc27f451be380812511a2ef`
   - contains the same stale active alert and active-question listing.

This is a source-of-truth propagation mismatch: implementation, review and L4 source are canonical, while shared Foundation routing still describes the pre-answer state.

## Minimal propagation candidate

I simulated the narrow candidate in memory against the exact current JSON bytes. It requires no new mathematics and no P012/source-code/test change.

### foundation_steward.json

- remove FQ-005 from `problem_set.active_questions`;
- add `canonical_foundation_conventions.graph_distance_api` recording:
  - stable `graph_distance` = P012 theorem-facing shortest-step API on closed/symmetric/loop-free adjacency;
  - `directed_graph_distance` = literal outgoing-adjacency shortest-walk helper, without ordinary-metric symmetry;
  - equal value on P012-valid input;
  - componentwise finite metric with explicit cross-component rejection;
  - endpoint-before-zero and adjacency-key-closure repairs;
  - prior-art boundary;
  - research/steward/canonical provenance above.

### research_common_surface.json

- remove FQ-005 from `active_foundation_questions` and `active_interface_alerts`;
- remove `tool_scope_alerts.FQ-20260809-005`;
- add `canonical_specializations.A5_graph_distance_api` with status `CANONICAL_MAIN + EXECUTABLE_CHECKED` and exact provenance.

### foundation_backflow.json

- remove the stale FQ-005 answered scheduler link. The research task is terminal and no longer needs a Foundation action;
- add exactly one `canonicalized_examples` entry:
  - canonical PR 436 / merge `3a40fe680e7aad4bc458540483c3c753e15f2cc4`;
  - final gates `quality`, `bilingual-sync`, `reference-integrity`;
  - class `THEOREM_TOOL_API_REPAIR`;
  - RETURN / Steward / source-canonicalization / PR provenance.

### Human Common Surface

In both English and Chinese files:

- replace the active-interface warning with a canonical A5 graph-distance API paragraph;
- remove FQ-005 from the active-question list;
- retain FQ-007 as active;
- state FQ-005 as resolved/source-canonical with the accepted layered API.

Do **not** rewrite P012 theorem documentation: its present hypotheses and disconnected-space section already agree with the accepted resolution.

## Candidate consistency checks performed

The simulated candidate was checked before this report was written:

- Steward active-question set and Common Surface active-question set remain equal after removing FQ-005.
- FQ-005 is absent from active interface alerts and `tool_scope_alerts`.
- Every remaining tool-scope alert remains a member of the active Foundation-question set.
- The stale FQ-005 answered scheduler link is removed.
- Exactly one FQ-005 canonicalized example is introduced.
- Current package exports, implementation validators and P012 theorem/domain text were independently re-read at `3ae6979a97b13062da2c0636362f4ae1a4d94f24`.

The repository-wide `tools/check_research_common_surface.py`, full test suite, bilingual checker and reference-integrity checker were **not** executed in this connector-only checkpoint; no such pass is claimed. A canonical maintenance writer must run the strongest available local validation before publication.

## Authority / method boundary

This TASK_RESEARCH claim is restricted to:

`research_returns/RS-GOV-FOUNDATION-BACKFLOW/EM-GOV-76FA5C/`

Therefore this report does **not** mutate Foundation/Common Surface canonical files and does not self-grant Steward/Driver acceptance or L4 authority. It gives the authorized maintenance role a current-main, source-pinned, minimal patch target.

P000 was loaded and unchanged. BRC is `NOT_APPLICABLE` to this propagation-consistency unit because no mathematical branch carrier, observer quotient or new general-purpose mechanism is being introduced. Tool-reuse gate is likewise `NOT_APPLICABLE`: this checkpoint introduces no reusable tool family.

## Smallest next unfinished unit

1. Hand this exact current-main propagation candidate to the authorized Foundation/Driver maintenance path for a five-surface patch and local checker execution.
2. Verify canonical readback after that patch; only then call FQ-005 backflow fully closed.
3. After FQ-005 propagation is durable, intake FQ-20260810-007's exact integration state. Do not reopen its already-completed research task merely because PR #444 integration debt may remain.
