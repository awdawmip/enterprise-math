<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
  "title": "T6 Exact Shape-Moment Threshold: Global Lower-Bound Closure",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Exact T1=6, T2=20, T3=105, T4=301, T5=941 are closed. A degree-6 L=360 witness gives T6<=2332 and the whole L=360 degree-6 integer kernel has minimum max-side mass 2332. All maximal prime factors p>=29 and the entire maximal-p=23 layer are eliminated below 2332. For maximal p=19, global vertical orders 0 through 8 are eliminated. The smallest unfinished mathematical unit is p=19 vertical order 9, split (3,6) and (4,5), followed by orders 10-12 if order 9 is empty.",
  "next_action": "Starting from the certified p=19 saturated q0 congruence lattice, clear vertical order 9 blocks (3,6) and (4,5) with exact side-mass budgets 2331 and exact mixed congruences. If order 9 is empty, clear orders 10-12. If p=19 is completely eliminated, descend the maximal-prime frontier to p=17,13,11 and then the remaining small-prime layers until either T6=2332 is proved globally or an exact cheaper collision is produced.",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/chatgpt-global-knowledge/commit/ec3ab6f84c9cb0d2dc48dcec7c5d3980f98df910",
    "https://github.com/awdawmip/chatgpt-global-knowledge/commit/7b2115cc09517be5f26fbf5e1739742cd9119154",
    "https://github.com/awdawmip/chatgpt-global-knowledge/commit/047b47aedbd129d5fb2c2a0af136704f5d802592",
    "https://github.com/awdawmip/chatgpt-global-knowledge/commit/ba91e9b844886f3f9581392ae4f4c80409adf327",
    "https://github.com/awdawmip/chatgpt-global-knowledge/commit/5fb0a1695269ee914e5620e03439333a1a70ec91",
    "https://github.com/awdawmip/chatgpt-global-knowledge/commit/8cdc2272e4d75859002686222dc81d3974a26b1c",
    "research_artifacts/T6_SHAPE_MOMENT_PERSISTENT_LINE_DRIVER_20260909/dossier.md"
  ],
  "evidence_status": "DURABLE_FREE_RESEARCH_FRONTIER_IMPORTED_FOR_TASK_EXECUTION",
  "last_progress_ref": "https://github.com/awdawmip/chatgpt-global-knowledge/commit/8cdc2272e4d75859002686222dc81d3974a26b1c",
  "last_progress_at": "2026-09-06T08:47:32+08:00",
  "hard_block": "MAXIMAL_P19_VERTICAL_ORDERS_9_12_THEN_LOWER_PRIME_DESCENT",
  "tags": [
    "T6",
    "shape-moment",
    "BRC",
    "valuation",
    "Tarry-Escott",
    "p-adic",
    "exact-threshold"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
  "parent_objective_id": "EM-T6-SHAPE-MOMENT-EXACT-THRESHOLD",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "T6SM",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# T6 Exact Shape-Moment Threshold: Global Lower-Bound Closure

Status: `READY / PUBLISHED_REGISTERED`

## Mother question

Is the sixth finite shape-moment resolution threshold exactly
\[
T_6=2332,
\]
or does there exist an exact collision of two exponent shapes with both side exponent masses at most 2331 and identical \(H_0,\ldots,H_6\)?

The task begins at the highest verified durable frontier rather than replaying prior work.

## Frozen inputs and scope

Use the full integer/exponent carrier. For an exponent shape \(\lambda=(e_i)\), retain the exact denominators \(a_i=e_i+1\), prime valuations, signed multiplicities, side masses, and the exact additive shape moments
\[
H_k(\lambda)=\sum_i\left(\frac{e_i}{e_i+1}\right)^k.
\]

Frozen verified inputs:

- \(T_1=6,T_2=20,T_3=105,T_4=301,T_5=941\).
- The explicit degree-6 \(L=360\) witness has maximum side mass 2332, and 2332 is the exact minimum over the whole \(L=360\) degree-6 integer kernel.
- Every maximal prime factor \(p\ge29\) is excluded below 2332.
- The maximal-\(p=23\) layer is globally excluded, including inactive residues and higher-digit rescue.
- For maximal \(p=19\), global vertical orders 0 through 8 are excluded.
- The first unresolved unit is maximal \(p=19\), vertical order 9, with side splits \((3,6)\) and \((4,5)\) up to global sign.

Do not repeat the closed \(p\ge29\), \(p=23\), or \(p=19\) order-0-through-8 audits unless an integrity check identifies an actual defect. Preserve the exact BRC/valuation carrier; prime-only, total-only, or logarithmic compression is insufficient for the theorem.

The durable line dossier is `research_artifacts/T6_SHAPE_MOMENT_PERSISTENT_LINE_DRIVER_20260909/dossier.md`.

## Hard target and required outputs

Hard target: `EXACT_GLOBAL_T6_THRESHOLD_OR_CHEAPER_COLLISION`.

Produce one of the following terminal mathematical outcomes:

1. An exact proof that no degree-6 collision exists below side mass 2332, hence \(T_6=2332\); or
2. An exact cheaper collision, with both exponent shapes, all six moment equalities, side masses, first hidden moment, and an independently checkable certificate.

Required route discipline:

1. Close maximal \(p=19\) vertical order 9 first, then orders 10-12 if needed.
2. If \(p=19\) is eliminated, descend maximal primes in order \(17,13,11,\ldots\), using exact saturated congruence lattices, valuation-layer arguments, or equally strong integer certificates.
3. For every maximal-prime elimination, close zero-first-digit and higher-digit rescue mechanisms that are compatible with the true side budgets; a first-digit-only statement is not global closure.
4. If a genuine modular kernel appears at any maximal-prime layer, stop that elimination and solve the lower-prime completion problem rather than discarding the kernel.
5. Preserve exact integer/rational arithmetic in the proof state. Numerical optimization may generate candidates but is not theorem evidence.
6. Persist any checker, proof certificate, finite census summary, and exact recovery frontier needed by the next researcher.

## Research value to preserve

This task converts a long free-research derivation into a claimable exact problem without losing the expensive verified frontier. The threshold sequence
\[
6,20,105,301,941,\ldots
\]
measures when the finite BRC shape observer \(H_0,\ldots,H_m\) first ceases to recover exponent shape under a finite mass budget. Closing \(T_6\) tests whether the small-prime/valuation skeleton continues to control the next exact observer-resolution boundary.

The key research value is not only the number 2332. It is the reusable proof architecture linking divisor-supported finite-difference codes, p-adic valuation layers, exact side budgets, and observer-safe BRC compression.

## Success, kill, and return criteria

Success is an exact global proof \(T_6=2332\), or an exact collision below 2332.

Kill any branch that:
- redoes a verified closed layer without an identified integrity defect;
- removes even numbers or obvious small-prime composites as preprocessing;
- replaces signed/exponent/valuation data by total mass before proving that quotient safe;
- relies on floating-point near-equality for moment identities or lattice emptiness;
- treats a support-local or first-digit result as a global maximal-prime elimination.

If the whole target cannot be closed in one execution, return the smallest exact unfinished unit together with all durable certificates needed to resume it. Do not return a vague “continue p-adic search” frontier.
