<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-1195-RANK5-SELECTOR-GALOIS-CLASSFIELD",
  "title": "1195: Rank-5 Selector Galois and Class-Field Theorem",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "The scalar c=1 pi-free selector is already identified with Borwein/Masser class-field data and is Galois-equivariant. For rank 5, CP15 gives an exact pi-free projective selector [A:B:C] as the cross product of two Picard-Fuchs odd covectors written in mirror-map and Yukawa data. What is not proved is that this rank-5 selector lies in the relevant ring-class field at CM/arithmetic points, or that it transports Galois-equivariantly; the general-c extension is still open.",
  "next_action": "Choose one rank-5 Calabi-Yau/Ramanujan kernel with an explicit arithmetic or CM specialization, rewrite the two CP15 odd covectors after a single declared period normalization, and determine whether all transcendental period factors cancel projectively so that the selector coordinates lie in the same algebraic field as the modular data. Prove the resulting Galois transport or exhibit the first exact obstruction.",
  "dependencies": [],
  "source_refs": [
    "research_notes/1195_research_handoff_index_20260909.md",
    "issue:1195#issuecomment-5533885992",
    "issue:1195#issuecomment-5540836463",
    "issue:1195#issuecomment-5533689202",
    "issue:1195#issuecomment-5533745356"
  ],
  "evidence_status": "RESEARCH_HANDOFF_INTEGRATION_V1",
  "last_progress_ref": "research_notes/1195_research_handoff_index_20260909.md",
  "last_progress_at": "2026-09-09T00:50:00+08:00",
  "hard_block": "RANK5_SELECTOR_CLASSFIELD_AND_GALOIS_TRANSPORT",
  "tags": [
    "1195",
    "pi-power",
    "rank5",
    "selector",
    "Picard-Fuchs",
    "mirror-map",
    "Yukawa",
    "CM",
    "class-field",
    "Galois"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-1195-RANK5-SELECTOR-GALOIS-CLASSFIELD",
  "parent_objective_id": "EM-PI-POWER-SPECTRAL-SELECTOR",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1195G",
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

# 1195: Rank-5 Selector Galois and Class-Field Theorem

Status: `READY / DIRECT USER RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

For the rank-5 Ramanujan/Calabi-Yau `1/pi^2` setting, does the target-free odd-selector ray `[A:B:C]` defined by Picard-Fuchs periods descend at CM or arithmetic specializations to the same class field as the modular data and satisfy Galois equivariance; if so, what hypotheses and period normalization make this exact, and what survives for general rank `2c+1`?

## 1. Frozen inputs and scope

Read `research_notes/1195_research_handoff_index_20260909.md` first. Consume, do not replay, the scalar `c=1` Borwein/Masser class-field bridge and the rank-5 CP15 selector formula.

The rank-5 starting point is the exact pair

`P(theta) w1 = 0`,

`P(theta)(w3 - h zeta(3) w0) = 0`,

with `P(theta)=A+B theta+C theta^2`, together with the mirror/Yukawa cross-product expression recorded in the handoff. The task may use classical Picard-Fuchs, mirror-map, CM-period, modular-form, and class-field results with explicit prior-art attribution. It must not use the final `1/pi^2` evaluation as an input to prove selector algebraicity.

The `c=1` identity `B/A=6/(1-s2(tau))` and its Masser Galois transport are frozen completed background. Formal skew-self-adjointness of the complement-symmetric operator is also background and is known to be insufficient by itself.

## 2. Hard target and required outputs

Hard target: `RANK5_SELECTOR_CLASSFIELD_THEOREM_OR_EXACT_OBSTRUCTION`.

Deliver all of the following, or an exact negative boundary replacing an impossible item:

1. Fix at least one nontrivial rank-5 hypergeometric/Calabi-Yau family with a documented arithmetic or CM specialization and state its exact Picard-Fuchs and period data used by the proof.
2. Starting from the two pi-free odd covectors, exhibit a single explicit period normalization under which the projective selector `[A:B:C]` is algebraic, or prove that no such cancellation follows from the stated data.
3. If algebraicity holds, identify the smallest proven field containing the selector and prove the Galois transport law for conjugate arithmetic/CM points. Do not infer field equality merely from matching numerical degrees.
4. Separate projective algebraicity from the later even-coordinate `1/pi^2` completion. State exactly which step uses CM/arithmetic specialization and which holds for generic `z`.
5. Compare the result with the completed scalar `c=1` Borwein/Masser case and isolate the genuinely new rank-5 ingredient: extra period extension, Yukawa data, zeta(3) extension, or another exact object.
6. Test at least one conjugate pair or higher-degree orbit exactly or with a rigorously certified algebraic polynomial, not only decimal matching.
7. State the strongest justified general-rank conjecture or no-go after the rank-5 result, including the first obstruction to a `P^c(K_ring)` theorem when it fails.

A successful negative result may show that the selector requires a larger period field, mixed extension, or non-class-field datum; it must identify the exact failed cancellation rather than merely report unsuccessful symbolic simplification.

## 3. Research value to preserve

The scalar route already shows that a pi-free finite selector can recover a genuine class-field observable before the analytic completion labels the sum by `pi`. CP15 upgrades the selector from a scalar to a rank-5 projective period covector. The unresolved scientific question is whether this inverse-reconstruction phenomenon is intrinsically Galois/class-field compatible in higher rank or is special to the elliptic/signature-6 case.

A proof would turn finite selector recovery into a class-field coordinate mechanism for `1/pi^2` and provide the correct target for general `1/pi^c`. A precise obstruction is equally valuable because it identifies where higher Calabi-Yau period extensions depart from the elliptic CM picture.

## 4. Success, kill, and return criteria

Success is a theorem with explicit hypotheses proving rank-5 selector algebraicity and Galois transport at a nontrivial arithmetic/CM family, together with a clear general-rank interface; or an exact counterexample/obstruction locating the first non-algebraic or larger-field datum.

Kill any route that merely redoes the `c=1` Masser proof, treats formal self-duality as sufficient for arithmetic specialization, uses the target `1/pi^2` equality to infer the selector coefficients, identifies class fields from floating-point recognition alone, or suppresses the fixed zeta(3)/period normalization needed by the rank-5 odd covector.

Do not broaden into a catalog-wide numerical scan before the single-family period-normalization question is resolved. Return the first exact class-field theorem, exact obstruction, or sharply reduced period-field frontier.