<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL",
  "title": "Prime-Factor Semiprime Shell Second-Order Density/Covariance Null",
  "kind": "RESEARCH",
  "owner": "research/prime-factor-semiprime-shell-second-order-density-null",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Determine whether any factor-coordinate semiprime-shell residual survives nulls that preserve exact local q-prime density, wheel residues, shell-overlap covariance, and empirical short-gap structure, rather than only first-order smooth density.",
  "next_action": "Freeze the conditional microcell and wheel-cyclic surrogate generators plus the 32-bin cross-scale coherence statistic before evaluating new holdout scales; then run exact discovery reanalysis and reserve 3e8 and 1e9 as untouched holdouts.",
  "dependencies": [
    "research_tasks/PRIME_FACTOR_SEMIPRIME_SHELL_RESIDUAL_VALIDATION_20260827.md@main"
  ],
  "source_refs": [],
  "evidence_status": "DIRECT_USER_CONTINUATION / PARENT_RESULT_UNREVIEWED / NO_WORKING_TRUTH_GRANT / SECOND_ORDER_NULL_GATE_OPEN",
  "last_progress_ref": "RR-3287C6124F8D8A1F0901",
  "last_progress_at": "2026-08-28T04:56:00+00:00",
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "semiprimes",
    "prime-factor-coordinates",
    "conditional-randomization",
    "wheel-210",
    "overlap-covariance",
    "prime-gaps",
    "blind-holdout",
    "falsification"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL",
  "parent_objective_id": "PROGRESSIVE_PLANE_PRIME_SEMIPRIME_COORDINATE_DISCOVERY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFSS2",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION",
  "successor_gate": {
    "new_information_gap": "The parent execution found a preregistered cross-scale signal that blind-replicated but was reproduced by a first-order local-density surrogate; it did not test conditional nulls preserving local prime counts, overlap covariance, and short-gap structure simultaneously.",
    "why_parent_result_does_not_close_it": "Even if the unreviewed parent density-artifact diagnosis is correct, first-order correction does not decide whether a smaller second-order survivor remains after conditioning on fine local density and empirical gap structure.",
    "discriminating_outcomes": [
      "All cross-scale residuals fall inside both density-conditioned second-order null families, closing the occupancy route at SECOND_ORDER_DENSITY_ARTIFACT strength.",
      "One preregistered feature exceeds family-wise thresholds under both nulls and reproduces with frozen sign and location on both new holdouts, yielding SECOND_ORDER_RESIDUAL_CANDIDATE.",
      "The two null families disagree materially, yielding NULL_MODEL_MISSPECIFICATION and a strictly smaller covariance or gap-model frontier.",
      "A survivor is confined to one fixed wheel or gap stratum, reducing the problem to a local arithmetic interaction rather than a global visual pattern."
    ],
    "kill_condition": "Do not count the already exposed 3e7 and 1e8 scales as blind validation. Any candidate chosen after inspecting 3e8 or 1e9, any feature surviving only one null family, or any conclusion that assumes the parent unreviewed verdict as Working Truth is non-closing.",
    "alternative_route_or_free_exploration_considered": "Closing the factor-shell route immediately, switching to prime-gap colorings, and broad free exploration were considered. A second-order conditional null is preferred because it directly tests the exact failure mode exposed by the parent without adding a new observable.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent hard target was first-order occupancy validation and is already frozen at task scope. The new work changes the null hypothesis, preserves stronger nuisance structure, uses fresh holdouts, and has a distinct falsifiable endpoint."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime-Factor Semiprime Shell Second-Order Density/Covariance Null

Status: `PUBLISHED_REGISTERED / CONTINUATION / SECOND-ORDER NULL`

## Mother question

For semiprime shells

\[
\mathcal S_{X,\eta}=\{pq:\ p\le q,\ p,q\ \text{prime},\ X<pq\le(1+\eta)X\},
\]

does any factor-coordinate residual remain after conditioning not merely on smooth prime density, but on fine local \(q\)-prime counts, admissible wheel residues, exact overlap of the shell intervals, and empirical short-gap structure?

The parent result `RR-3287C6124F8D8A1F0901` is currently unreviewed. It is motivation only, not a frozen premise.

## Frozen inputs and scope

Primary factor range:

\[
X^{1/4}<p\le \sqrt{(1+\eta)X},\qquad p\le q.
\]

Use exposed discovery scales

\[
X\in\{10^6,3\cdot10^6,10^7,3\cdot10^7,10^8\}
\]

and shell widths

\[
\eta\in\{10^{-2},3\cdot10^{-3},10^{-3}\}.
\]

The already exposed \(3\cdot10^7\) and \(10^8\) layers are discovery data here, not holdouts. Reserve new blind holdouts

\[
X\in\{3\cdot10^8,10^9\}.
\]

No statistic, bin, sign, band width, or surrogate parameter may be changed after inspecting either new holdout.

Use

\[
u=\frac{\log p}{\log X},\qquad
\xi_X(p)=1+\frac{\log(u/(1-u))}{\log 3},
\]

with 32 equal \(\xi\)-bins. Exclude \(p=q\) from the primary statistic and report it separately.

### Null A — conditional microcell wheel shuffle

Partition the global \(q\)-axis into deterministic logarithmic microcells with relative width \(2^{-10}\). Within each microcell and each admissible residue class modulo 210, preserve the exact observed number of primes and uniformly resample that many admissible integer locations without replacement. One surrogate \(q\)-set is shared across all scales, preserving covariance induced by common \(q\)-locations and overlapping shell intervals.

### Null B — wheel-preserving cyclic gap surrogate

Partition the same \(q\)-axis into deterministic logarithmic bands with relative width \(2^{-6}\), with endpoints aligned to multiples of 210. Within each band cyclically translate the observed prime indicator by a uniformly chosen multiple of 210, wrapping inside the band. This preserves local prime count, the within-band cyclic gap sequence, and residues modulo 210 while breaking alignment with the factor-shell interval family.

For both nulls, the exact shell interval attached to a prime \(p\) is

\[
I_p(X,\eta)=\left(X/p,(1+\eta)X/p\right],
\]

with \(q\ge p\). Recompute occupancy from each surrogate \(q\)-set; do not replace interval overlap by independent bin noise.

For each scale, width and bin define

\[
z_{X,\eta,b}=\frac{O_{X,\eta,b}-\mu_{X,\eta,b}}{\sigma_{X,\eta,b}},
\]

where \(\mu,\sigma\) are frozen from 4096 null replicates. For each width and bin define

\[
C_{\eta,b}=\frac1{\sqrt5}\sum_X z_{X,\eta,b},
\qquad
T=\max_{\eta,b}|C_{\eta,b}|.
\]

Use the empirical 99% quantile of the same max statistic under each null family. Freeze the winning \((\eta,b,\operatorname{sign})\) before holdout evaluation.

## Hard target and required outputs

Hard target:

`SEMIPRIME_FACTOR_SHELL_SECOND_ORDER_NULL_SURVIVOR_CLASSIFIED`.

Required outputs:

1. exact-integer shell enumeration with an exact prime generator;
2. deterministic implementations of Null A and Null B from frozen seeds;
3. 4096-replicate null summaries with per-cell means, variances, covariance diagnostics, and family-wise max-statistic thresholds;
4. discovery profiles and a frozen winning width, bin and sign, or an exact no-candidate return;
5. untouched evaluation at \(3\cdot10^8\) and \(10^9\);
6. an independent spot-check path for shell counts and surrogate invariants;
7. explicit checks that local counts and wheel residues are preserved in both nulls and that Null B preserves the within-band cyclic gap multiset;
8. a durable return using one of the terminal classes below.

## Research value to preserve

The parent experiment exposed how a visually and statistically strong first-order signal can still be generated by density and shell geometry. This task asks the sharper question: is the apparent phase entirely generated by covariance from overlapping shell intervals and ordinary local prime-gap structure?

A clean negative result closes the naive semiprime occupancy geometry much more strongly than a smooth-density correction. A positive result isolates a residual conditioned on substantially more of the known prime process and justifies a later exact arithmetic investigation.

No new color observable, holonomy value, Prime Fusion phase, or next-prime annotation may be introduced to rescue a failed occupancy result.

## Success, kill, and return criteria

Return `SECOND_ORDER_RESIDUAL_CANDIDATE` only if one discovery-selected feature:

- exceeds the 99% family-wise max-statistic threshold under both Null A and Null B;
- has the same sign on at least four of five discovery scales;
- is not carried by the excluded square locus;
- freezes one shell width, one \(\xi\)-bin, and one sign before holdout;
- reproduces with that sign on both new holdouts and exceeds the predeclared one-sided 99% null threshold under both null families on each holdout.

Return `SECOND_ORDER_DENSITY_ARTIFACT` if no discovery feature clears both nulls or the frozen feature fails either holdout.

Return `NULL_MODEL_MISSPECIFICATION` if Null A and Null B give materially incompatible covariance or threshold structure and the discrepancy itself survives deterministic replay; freeze the smallest cause rather than choosing the more favorable null.

Return `LOCAL_ARITHMETIC_STRATUM_SURVIVOR` only if the global candidate disappears after a predeclared wheel or gap stratification but one fixed stratum survives both nulls and both holdouts. This is a narrower follow-up interface, not a global semiprime-shell law.

Kill post-hoc bin changes, holdout reuse, null-family cherry-picking, larger scans used as proof, and any attempt to reinterpret an empirical survivor as a factorization shortcut or all-scale theorem.
