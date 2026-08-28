<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-BRANCH-PATTERN-COMPLETION",
  "title": "Ramanujan–Borwein × Enterprise Degree-6 CM(-24) Blind Branch-Pattern Completion",
  "kind": "RESEARCH",
  "owner": "research/rb-enterprise-degree6-cm24-blind-branch-pattern-completion",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Starting only from the independently frozen blind reduction at c73816d, decide the two remaining special-fiber branch-block patterns 4+2+0+0 and 2+2+2+0 for the required degree-6 map, and reconstruct the correspondence exactly or prove both patterns impossible without seeing the originating explicit map.",
  "next_action": "Enumerate the two remaining branch partitions up to source and target symmetry, convert each special fiber into exact square-class/Riemann–Roch constraints on C:t^2=R^3-3R, intersect them with the frozen ODE certificate, and freeze an exact map or exact obstruction before any unblinding.",
  "dependencies": [
    "research_artifacts/RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION/raw_freeze_reduction.json@c73816d3552b4247861e12e476101e94a4a2ce5a",
    "scripts/check_rb_enterprise_degree6_cm24_blind_replication.py@c73816d3552b4247861e12e476101e94a4a2ce5a"
  ],
  "source_refs": [],
  "evidence_status": "PARENT_BLIND_REDUCTION_FROZEN / SIX_BLOCK_PATTERN_EXCLUDED / TWO_PATTERNS_REMAIN / ORIGINATING_EXPLICIT_MAP_WITHHELD / NO_PARENT_TERMINAL_PASS",
  "last_progress_ref": "c73816d3552b4247861e12e476101e94a4a2ce5a",
  "last_progress_at": "2026-08-27T22:31:49+08:00",
  "hard_block": null,
  "tags": [
    "blind-replication",
    "CM-24",
    "degree-6",
    "elliptic-correspondence",
    "branch-divisors",
    "2-descent",
    "Riemann-Roch",
    "exact-ODE",
    "independent-validation"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-BRANCH-PATTERN-COMPLETION",
  "parent_objective_id": "RB_ENTERPRISE_THEOREM_PACKAGE_V2_INDEPENDENT_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RBV2BPC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-REPLICATION",
  "successor_gate": {
    "new_information_gap": "The first blind execution independently reduced the problem and excluded the 6+0+0+0 branch-block pattern, but it did not reconstruct X,Y, derive the period scaling, or refute the degree-6 target. Exactly two branch patterns remain.",
    "why_parent_result_does_not_close_it": "The frozen parent artifact is an exact reduction with verdict BLIND_INCOMPLETE_EXACT_REDUCTION. It supplies parity, ramification, square-class and ODE constraints but no explicit correspondence and no nonexistence proof.",
    "discriminating_outcomes": [
      "One remaining branch pattern yields an exact degree-6 correspondence satisfying the frozen ODE and differential direction.",
      "Both remaining branch patterns are exactly impossible, refuting the frozen degree-6 target.",
      "One pattern is excluded and the other reduces to a strictly smaller finite algebraic certificate that remains unsolved.",
      "A reconstructed map exists but gives a different exact differential or period scaling, reopening the theorem-package normalization bridge."
    ],
    "kill_condition": "Any pre-freeze exposure to the originating explicit X,Y coefficients or their load-bearing symbolic replay terminates the run as BLINDNESS_BROKEN. Any exact contradiction to the frozen parent reduction must be recorded and the affected premise reopened rather than worked around.",
    "alternative_route_or_free_exploration_considered": "Broad new Ramanujan–Borwein exploration, direct formalization of the originating formula, and waiting for the stalled first execution were considered. Completing the two finite branch-pattern cases has strictly higher information value because it is the only remaining independent-validation gap and preserves the blind firewall.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The previous execution has a durable exact freeze but no terminal return and no recent advance. A separate bounded continuation lets a fresh unexposed execution consume the verified reduction without replaying completed work, while keeping the originating answer hidden."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Ramanujan–Borwein × Enterprise Degree-6 CM(-24) Blind Branch-Pattern Completion

Status: `PUBLISHED_REGISTERED / CONTINUATION / BLIND_FORWARD / EXACT_BRANCH_CLASSIFICATION`

## Mother question

Starting only from the independently frozen blind reduction of the degree-6 CM(-24) reconstruction problem, can the two remaining special-fiber branch-block patterns

\[
4+2+0+0
\qquad\text{and}\qquad
2+2+2+0
\]

be classified exactly so that one yields the required algebraic map

\[
f:D\to E_*,\qquad \deg f=6,
\]

or both are proved impossible?

The task is an independent falsification/completion lane. The originating explicit map is not an input.

## Frozen inputs and scope

The only parent research artifact allowed before the raw freeze is

`research_artifacts/RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION/raw_freeze_reduction.json@c73816d3552b4247861e12e476101e94a4a2ce5a`

plus its exact regression checker at the same source revision.

The following mathematical data are therefore frozen:

\[
D:\quad w^4=(R+2)^2R(R^2-3),
\]

\[
t=\frac{w^2}{R+2},\qquad C:\ t^2=R^3-3R,
\]

\[
\phi=\frac{dR}{w}\left(1+\frac{k}{t}\right),
\qquad
k=-i\,3^{1/4}(\sqrt6-2),
\]

and

\[
\lambda_*=35+24\sqrt2-20\sqrt3-14\sqrt6.
\]

The target x-coordinate descends to a degree-6 function

\[
X\in K(C),
\]

and any valid candidate satisfies the frozen ODE certificate

\[
(R+2)t\,\bigl(\delta X\bigr)^2
=
K(t+k)^2X(X-1)(X-\lambda_*),
\qquad
\delta=t\frac d{dR},
\qquad K\ne0.
\]

The parent blind reduction has already excluded the branch-block pattern `6+0+0+0`. Do not redo that classification unless an exact contradiction to the frozen certificate is found.

The remaining special-fiber branch blocks are exactly `4+2+0+0` and `2+2+2+0`, up to the usual source automorphisms and target anharmonic relabeling of \(0,1,\lambda_*,\infty\).

### Required attack order

First enumerate inequivalent assignments of the six branch points of \(D\to C\) to the four special fibers under each remaining block pattern.

For each assignment, encode the parity divisor of every \(X-a\), \(a\in\{0,1,\lambda_*,\infty\}\), as a square class in

\[
K(C)^*/K(C)^{*2}.
\]

Choose minimal Riemann–Roch representatives \(g_a\) for these four square classes and solve the coupled equations

\[
X=\frac{g_0u_0^2}{g_\infty u_\infty^2},
\]

\[
X-1=\frac{g_1u_1^2}{g_\infty u_\infty^2},
\qquad
X-\lambda_*=\frac{g_\lambda u_\lambda^2}{g_\infty u_\infty^2},
\]

inside the smallest sufficient Riemann–Roch spaces on \(C\). Use the ODE certificate as an independent exact filter on every surviving candidate.

A numerical search may be used only to discover coefficients. Every load-bearing identity must be replayed exactly in the algebraic function field before a PASS is frozen.

### Blind firewall

Before the raw freeze, do not inspect the originating explicit \(X,Y\), its coefficients, common base point, target twist constant, exact symbolic replay, originating period-scaling value, account-level journal entries containing those objects, or external material targeted at locating that formula.

The parent blind reduction artifact at `c73816d` is allowed even though it records the already-completed exact reduction. Broader repository/theorem-package comparison begins only after the new raw freeze.

If the executing context has already seen the originating explicit formula or its load-bearing coefficients, it is ineligible for a blind verdict.

## Hard target and required outputs

Hard target:

`RB_ENTERPRISE_DEGREE6_CM24_BLIND_BRANCH_PATTERNS_COMPLETED_OR_REFUTED`.

Required outputs:

1. a complete symmetry-reduced classification of the `4+2+0+0` and `2+2+2+0` branch assignments;
2. exact square-class representatives for all four special fibers in every surviving case;
3. an exact Riemann–Roch solution or exact obstruction for each surviving case;
4. if a map exists, explicit \(X\) and \(Y\), exact degree, common-base-point/divisor analysis if present, target elliptic equation, and exact target \(j\)-invariant;
5. exact verification of the frozen ODE certificate and pullback invariant differential;
6. if a map exists, an independent derivation of \((B_1/\Omega_P)^2\) without importing the originating value;
7. if no map exists, an exact proof excluding both remaining patterns and therefore refuting the frozen degree-6 target;
8. a machine-readable raw-freeze artifact with SHA256 and phase marker `BLIND_BRANCH_PATTERN_FREEZE` before any unblinding;
9. a deterministic exact checker whose load-bearing proof identities do not depend on numerical fitting;
10. post-freeze comparison against the originating theorem-package candidate and a discrepancy report if the reconstructed map/scaling differs;
11. a durable return at `research_returns/RB_ENTERPRISE_DEGREE6_CM24_BLIND_BRANCH_PATTERN_COMPLETION_RETURN_20260828.md`.

## Research value to preserve

The first blind execution has already converted a broad reconstruction problem into two finite branch-divisor cases. Completing those two cases is now the highest-information independent test of the Ramanujan–Borwein × Enterprise theorem-package candidate: a successful reconstruction upgrades the hardest bridge from self-audited to independently reproduced, while an exact obstruction or mismatch pinpoints the precise place where the claimed closure fails.

The task deliberately consumes the verified blind reduction instead of replaying completed work from zero.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `BLIND_BRANCH_PATTERN_RECONSTRUCTION_PASS` — one remaining pattern yields an exact degree-6 map and the differential/period data agree internally;
- `BLIND_BRANCH_PATTERN_EQUIVALENT_PASS` — the reconstructed map is algebraically equivalent to the originating result after Phase-B comparison;
- `BLIND_BRANCH_PATTERN_REFUTED` — both remaining patterns are exactly impossible;
- `BLIND_BRANCH_PATTERN_SCALING_MISMATCH` — an exact map is reconstructed but its differential or period normalization contradicts the theorem-package candidate;
- `BLIND_BRANCH_PATTERN_INCOMPLETE` — the two-pattern problem is reduced to a strictly smaller exact algebraic certificate but not completed;
- `BLINDNESS_BROKEN` — the originating explicit formula or load-bearing coefficients are exposed before the raw freeze.

Do not promote a high-precision fit to a theorem. Do not reopen the already excluded `6+0+0+0` pattern without an exact contradiction. A PASS is evidence for the stated correspondence only; any broader theorem-package status is decided after the blind freeze and comparison.
