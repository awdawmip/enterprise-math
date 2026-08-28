<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-POSITIVE-SUPPORT-SECOND-ORDER-NULL",
  "title": "Prime-Factor Semiprime Shell Positive-Support Second-Order Null",
  "kind": "RESEARCH",
  "owner": "research/prime-factor-semiprime-shell-positive-support-second-order-null",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Repair the second-order semiprime-shell null without reusing holdouts by enforcing exact positive conditional support before residual standardization, then decide whether any cross-scale occupancy residual survives both corrected density/covariance null families.",
  "next_action": "Freeze exact positive-support eligibility from the wheel-block null geometry before inspecting corrected residual z-scores; run 4096 discovery replicates under both corrected nulls, freeze one eligible candidate if it clears both family-wise gates, and only then evaluate untouched X=3e8 and 1e9.",
  "dependencies": [
    "research_tasks/PRIME_FACTOR_SEMIPRIME_SHELL_SECOND_ORDER_DENSITY_NULL_20260828.md@main"
  ],
  "source_refs": [],
  "evidence_status": "DIRECT_USER_CONTINUATION / PRIOR_NULL_MISSPECIFICATION_UNREVIEWED / HOLDOUTS_3E8_AND_1E9_STILL_UNTOUCHED / NO_WORKING_TRUTH_GRANT",
  "last_progress_ref": "RR-19573ADC79F8528B536E",
  "last_progress_at": "2026-08-28T05:30:00+00:00",
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "semiprimes",
    "positive-support-null",
    "wheel-210",
    "conditional-randomization",
    "gap-surrogate",
    "blind-holdout",
    "falsification"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-POSITIVE-SUPPORT-SECOND-ORDER-NULL",
  "parent_objective_id": "PROGRESSIVE_PLANE_PRIME_SEMIPRIME_COORDINATE_DISCOVERY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFSS2R",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL",
  "successor_gate": {
    "new_information_gap": "The first second-order generation is terminally non-identifiable because its Null A creates singleton (microcell,residue) strata and exact sigma=0 on the first three discovery scales. It leaves untouched whether a positive-support conditional null still explains the factor-shell phase.",
    "why_parent_result_does_not_close_it": "The prior generation diagnoses its own null design; it does not evaluate a valid second-order residual statistic and did not access the fresh 3e8 or 1e9 holdouts.",
    "discriminating_outcomes": [
      "Both corrected positive-support nulls explain every eligible discovery feature or the frozen candidate fails either untouched holdout, yielding SECOND_ORDER_DENSITY_ARTIFACT.",
      "One exactly support-eligible feature clears both 99% family-wise discovery gates and both null-specific 99% one-sided gates on both untouched holdouts, yielding SECOND_ORDER_RESIDUAL_CANDIDATE.",
      "The exact support intersection is empty or empirical variance collapses despite exact support, yielding POSITIVE_SUPPORT_NULL_FAILURE without holdout access.",
      "A corrected survivor localizes to a predeclared fixed wheel/gap stratum, yielding LOCAL_ARITHMETIC_STRATUM_SURVIVOR rather than a global shell law."
    ],
    "kill_condition": "No epsilon regularizer, post-hoc support threshold, changed bin count, dropped discovery scale, altered cell/band size, or holdout-informed tuning is allowed. If exact support fails, freeze that failure. If either untouched holdout fails either null gate, the global candidate dies.",
    "alternative_route_or_free_exploration_considered": "Closing the occupancy route after the misspecified null, adding a new color observable, and broad prime-gap exploration were considered. Repairing identifiability first is strictly more discriminating because the untouched holdouts are still available and no new observable is required.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent is terminal at null-misspecification scope and explicitly forbids in-task coarsening. A new publication is required to freeze the positive-support repair before residual evaluation while preserving the untouched holdout firewall."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime-Factor Semiprime Shell Positive-Support Second-Order Null

Status: `PUBLISHED_REGISTERED / CONTINUATION / POSITIVE-SUPPORT REPAIR`

## Mother question

For the same semiprime factor-shell observable, does any cross-scale residual survive two second-order null families after the conditioning cells are repaired so that every statistic used in the five-scale coherence test has **exactly positive conditional support** before any residual z-score is inspected?

The previous second-order generation is an unreviewed motivating result only. No arithmetic conclusion from it is a premise here.

## Frozen inputs and scope

Keep the primary observable unchanged:

\[
\mathcal S_{X,\eta}=\{pq:\ p\le q,\ p,q\ \text{prime},\ X<pq\le(1+\eta)X\},
\]

with

\[
X^{1/4}<p\le\sqrt{(1+\eta)X},
\qquad
\eta\in\{10^{-2},3\cdot10^{-3},10^{-3}\}.
\]

Discovery scales:

\[
X\in\{10^6,3\cdot10^6,10^7,3\cdot10^7,10^8\}.
\]

The still-untouched blind holdouts remain

\[
X\in\{3\cdot10^8,10^9\}.
\]

They must not be enumerated before the discovery candidate, sign, width, bin, exact support set, null rules and random seeds are frozen.

Use the same 32-bin coordinate

\[
u=\frac{\log p}{\log X},
\qquad
\xi_X(p)=1+\frac{\log(u/(1-u))}{\log3}.
\]

The square locus \(p=q\) remains excluded from the primary statistic.

For an integer \(q\ge210\), write

\[
t=\lfloor q/210\rfloor.
\]

### Corrected Null A — positive-support wheel-block shuffle

For \(t\ge8\), let

\[
k=\lfloor\log_2t\rfloor,
\qquad
s_A(k)=2^{\max(3,k-10)},
\qquad
j_A=\left\lfloor\frac{t-2^k}{s_A(k)}\right\rfloor.
\]

A full A-cell is the union of the \(s_A(k)\) complete consecutive 210-blocks with fixed \((k,j_A)\). Values with \(t<8\), or lying in an incomplete final A-cell of the current q-universe, are fixed.

Within each full A-cell and each residue \(r\bmod210\), preserve the exact observed prime count \(K\) and sample uniformly without replacement \(K\) of the \(s_A(k)\) positions carrying that residue. One surrogate q-set is shared across all discovery scales and shell widths.

This agrees asymptotically with a \(2^{-10}\) relative q-cell but imposes a hard minimum of eight wheel blocks, so a full conditioned residue stratum has at least eight candidate positions.

### Corrected Null B — positive-support wheel-gap cyclic surrogate

For \(t\ge16\), let

\[
k=\lfloor\log_2t\rfloor,
\qquad
s_B(k)=2^{\max(4,k-6)},
\qquad
j_B=\left\lfloor\frac{t-2^k}{s_B(k)}\right\rfloor.
\]

A full B-band is the union of \(s_B(k)\) complete consecutive 210-blocks with fixed \((k,j_B)\). Values with \(t<16\), or in an incomplete final B-band, are fixed.

Within each full B-band, cyclically translate the observed prime indicator by one uniformly chosen offset in \(\{0,\ldots,s_B(k)-1\}\) 210-blocks, wrapping inside that band. This preserves exact band prime count, every residue modulo 210, and the within-band circular gap multiset.

### Exact support gate before residual inspection

For a scale/width/bin feature \(f=(X,\eta,b)\), let \(w_f(q)\) be the exact number of admissible p-values in that feature for which q lies in

\[
I_p(X,\eta)=(X/p,(1+\eta)X/p],
\qquad q\ge p,
\]

with the square pair excluded.

Declare `SUPPORT_A(f)=true` iff some full A-cell/residue stratum has \(0<K<s_A\) and the values of \(w_f(q)\) over its candidate positions are not all equal.

Declare `SUPPORT_B(f)=true` iff some full B-band has two allowed cyclic shifts whose aggregate \(w_f\)-contributions differ.

A pair \((\eta,b)\) is eligible iff `SUPPORT_A` and `SUPPORT_B` are true for the corresponding feature at **all five** discovery scales.

Freeze the exact eligible set \(E\) before computing observed residual z-scores. If \(E=\varnothing\), terminate `POSITIVE_SUPPORT_NULL_FAILURE` without holdout access.

### Monte-Carlo statistic

Use 4096 fresh discovery replicates for each corrected null after \(E\) is frozen.

For each eligible feature,

\[
z_{X,\eta,b}
=
\frac{O_{X,\eta,b}-\mu_{X,\eta,b}}{\sigma_{X,\eta,b}}.
\]

If an exactly eligible feature nevertheless has empirical \(\sigma=0\) in either 4096-replicate run, terminate `POSITIVE_SUPPORT_NULL_FAILURE`; do not regularize.

For each \((\eta,b)\in E\),

\[
C_{\eta,b}=\frac1{\sqrt5}\sum_X z_{X,\eta,b},
\qquad
T=\max_{(\eta,b)\in E}|C_{\eta,b}|.
\]

Each null family supplies its own empirical 99% family-wise threshold from the same max statistic on \(E\).

Candidate tie-break: among cells clearing both thresholds, maximize the smaller of the two threshold margins; then choose smaller eta; then lower bin index. Freeze \((\eta,b,\mathrm{sign})\) before holdout access.

## Hard target and required outputs

Hard target:

`SEMIPRIME_FACTOR_SHELL_POSITIVE_SUPPORT_SECOND_ORDER_SURVIVOR_CLASSIFIED`.

Required outputs:

1. exact integer discovery enumeration and exact support masks for both nulls;
2. a machine-readable pre-residual freeze containing \(E\), seeds and all null parameters;
3. 4096-replicate discovery summaries for both corrected nulls;
4. family-wise thresholds and a frozen candidate or exact no-candidate result;
5. holdout access only after candidate freeze;
6. if a candidate exists, exact evaluation at both untouched holdouts under both null families;
7. deterministic structural and Monte-Carlo replay checks;
8. a durable terminal return.

## Research value to preserve

The first second-order attempt failed because conditioning was too fine relative to the 210 wheel and made the null deterministic. This generation repairs only that identifiability defect. It does not add a new observable and it does not weaken the requirement that local density, residues, shell overlap and short-gap structure be preserved.

If the signal disappears here, the naive factor-shell occupancy route is closed at substantially stronger nuisance-conditioning strength. If it survives both corrected nulls and both untouched holdouts, the survivor is a much sharper candidate for exact arithmetic study.

## Success, kill, and return criteria

Return `SECOND_ORDER_RESIDUAL_CANDIDATE` only if one cell in the pre-frozen eligible set:

- exceeds the 99% family-wise discovery threshold under both corrected nulls;
- has the frozen sign on at least four of five discovery scales under both standardizations;
- is frozen before holdout access;
- reproduces with the same sign on both untouched holdouts;
- exceeds the predeclared one-sided 99% holdout threshold under both null families at each holdout.

Return `SECOND_ORDER_DENSITY_ARTIFACT` if no eligible discovery candidate clears both nulls, or if a frozen candidate fails either null at either holdout.

Return `POSITIVE_SUPPORT_NULL_FAILURE` if the exact eligible set is empty or an exactly eligible feature produces zero empirical variance.

Return `LOCAL_ARITHMETIC_STRATUM_SURVIVOR` only for a separately predeclared fixed-stratum analysis; no post-hoc localization may rescue a failed global candidate.

Kill all post-hoc regularization, changed cell sizes, changed binning, dropped scales, new colors, holdout reuse for tuning, and null-family cherry-picking.
