<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-BLIND-PADIC-FINGERPRINT",
  "title": "Enterprise BRC Half-Coupling Blind p-adic Fingerprint",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-blind-padic-fingerprint",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine, under a source-whitelisted blind-forward protocol, whether the frozen Enterprise integer kernel at the BRC half-coupling m=2 has a simple uniform p-adic fingerprint that survives an untouched holdout prime set and is not shared by preregistered m=3 and m=4 controls.",
  "next_action": "Using only this taskbook and the whitelisted Enterprise sources, implement two independent exact-integer modular evaluators for the preregistered R_p(m) observables, compute the discovery-prime vectors for m=2,3,4, freeze the raw vectors and SHA256 fingerprints, and only then fit the preregistered grammar before opening the holdout set or any external identification source.",
  "dependencies": [
    "PACKET_PATH_FOUNDATION.md@ab2349187749d1fad3479cc93754ea3d007df724",
    "definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@ab2349187749d1fad3479cc93754ea3d007df724"
  ],
  "source_refs": [
    "definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@ab2349187749d1fad3479cc93754ea3d007df724"
  ],
  "evidence_status": "BLIND_PROTOCOL_PREREGISTERED / TARGET_UNSEEN / NO_EXTERNAL_IDENTIFICATION_ALLOWED_BEFORE_RAW_FREEZE",
  "last_progress_ref": "User explicitly requested registration of a new blind test after the post-pi multi-domain validation stage; this task is an independent arithmetic-domain falsification route rather than another analytic/FCC identification pass.",
  "last_progress_at": "2026-08-26T18:39:00+08:00",
  "hard_block": null,
  "tags": [
    "blind-test",
    "p-adic",
    "BRC",
    "half-coupling",
    "supercongruence-audit",
    "negative-controls",
    "holdout",
    "independent-validation"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-BLIND-PADIC-FINGERPRINT",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:aad427281b91d39273ba54d3f3d5779600ff28f651927cc9b44c20d6694acb58",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Half-Coupling Blind p-adic Fingerprint

Status: `PUBLISHED_REGISTERED / DIRECT_USER_DIRECTION / NEW_DIRECTION / BLIND_FORWARD`

## Mother question

Does the frozen Enterprise combinatorial kernel exhibit a reproducible arithmetic law at the BRC-selected half-coupling that is detectable without external target knowledge, survives an untouched holdout prime set, and is absent or strictly weaker at preregistered non-half-coupling controls?

The purpose is falsification, not confirmation. A clean negative result is a valid task outcome. No constant, modular form, supercongruence, character law, or prior literature identity is assumed in advance.

## Frozen inputs and scope

### Task-local blind input

For every integer `n >= 0`, define the exact integer kernel

`A_n = (2n)! (3n)! / (n!)^5`.

For `m in {2,3,4}` and every prime `p >= 5`, define

`R_p(m) = sum_{n=0}^{p-1} (6n+1) A_n (108m)^(-n) mod p^3`,

where `(108m)^(-n)` is computed in `Z/(p^3)Z`. Because `p >= 5`, all three preregistered denominators are invertible.

Interpretation is frozen only at the task-local level:

- `m=2` is the primary half-coupling sample motivated by the current minimal BRC `2 witnesses -> 1 support` structure;
- `m=3` and `m=4` are negative controls;
- no claim that any of these residues encode physics, modularity, or a known special function is an input to Phase A.

### Blind-forward source whitelist — Phase A

Before the raw freeze, the researcher may read only:

1. this taskbook;
2. `PACKET_PATH_FOUNDATION.md` at the pinned source state;
3. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` at the pinned source state;
4. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md` at the pinned source state;
5. standard local language/runtime documentation needed to implement exact integer arithmetic.

Before the raw freeze, do not search the repository outside this whitelist for the kernel, do not read project/global journals or prior conversations about post-pi/FCC/Ramanujan/Borwein work, and do not consult external sequence databases, modular-form databases, p-adic/supercongruence literature, special-function tables, or internet search results that could identify the target.

### Exact preregistered prime split

Discovery primes:

`P_discovery = {p prime : 5 <= p <= 97}`.

Holdout primes:

`P_holdout = {p prime : 101 <= p <= 199}`.

The holdout residues must not be computed or inspected until the discovery vectors, discovery-law candidate and raw-freeze hashes are frozen.

### Two independent evaluators

Phase A must implement two exact evaluators that do not share their load-bearing recurrence:

- Evaluator F: direct exact factorial/binomial construction of `A_n`, reduced modulo `p^3` only after exact integer construction or an exactly equivalent prime-safe binomial formula;
- Evaluator R: the exact recurrence

`A_0 = 1`,

`A_{n+1}/A_n = 6(2n+1)(3n+1)(3n+2)/(n+1)^3`,

implemented in an exact-integer form that never performs an invalid modular division when `p | n+1`.

The two evaluators must agree for every frozen residue. If they disagree, the task stops with `CHECKER_DIVERGENCE` until the discrepancy is resolved; no identification phase may begin.

### Preregistered discovery grammar

For each `m`, and only using discovery primes, test in this order:

1. the largest uniform divisibility level `k in {0,1,2,3}` such that `p^k | R_p(m)` as an integer residue representative for every discovery prime;
2. if `k < 3`, form the normalized residue `R_p(m)/p^k mod p`;
3. test whether that normalized residue equals `c * chi_d(p) mod p` for every discovery prime, where
   - `c` is one integer in `[-12,12]`,
   - `d` belongs to the frozen set `D = {1,-1,2,-2,3,-3,6,-6}`,
   - `chi_1(p)=1`, and for `d != 1`, `chi_d(p)` is the Kronecker/Legendre character `(d/p)`.

Choose the first law in the stated order of increasing `k`-normalized description length, breaking ties by smaller `|c|` and then the listed order of `D`. Do not expand the grammar after seeing discovery data.

No change of truncation length, denominator, prime range, residue modulus, control values, or character family is permitted during Phase A.

### Phase B — post-freeze identification

Only after the raw discovery freeze and holdout evaluation are complete may the researcher open external identification sources and current broader project/tool context.

Phase B must distinguish:

- an independently rediscovered known congruence;
- a law implied by already-known hypergeometric machinery;
- a genuinely stronger or differently typed arithmetic statement;
- an accidental finite-range fit;
- no uniform law.

No novelty claim is allowed without explicit post-freeze prior-art/dedup audit.

## Hard target and required outputs

Hard target:

`ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_CLASSIFIED_OR_REFUTED`

Required outputs:

1. exact discovery vectors `R_p(m)` modulo `p^3` for every `p in P_discovery` and `m in {2,3,4}`;
2. SHA256 fingerprints of the canonical serialized discovery vectors before holdout evaluation;
3. the preregistered-grammar verdict for each `m`, with the exact selected `(k,c,d)` when one exists;
4. exact holdout vectors for every `p in P_holdout`, generated only after item 2 is frozen;
5. a binary holdout result for every discovery-law candidate: `HOLDOUT_PASS` or `HOLDOUT_FAIL`;
6. a comparative statement of whether `m=2` has strictly stronger uniform p-adic structure than both controls under the same grammar;
7. an exact proof of any surviving infinite-prime law, or a precise statement that the evidence remains finite/computational only;
8. post-freeze external identification and prior-art audit;
9. two independent exact checker implementations plus a machine-readable raw result artifact;
10. a durable return at `research_returns/ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_RETURN_20260826.md`.

The raw freeze artifact must record a monotone phase marker so that discovery freeze, holdout evaluation and post-freeze identification cannot be retrospectively conflated.

## Research value to preserve

The current Enterprise route already has strong analytic and lattice-spectrum alignments. Those do not by themselves establish that the same frozen combinatorics carries independent arithmetic rigidity.

This task therefore moves into a separate arithmetic domain and preregisters both controls and a holdout set. If `m=2` alone exhibits a simple law that survives holdout and admits an exact proof, that is materially stronger evidence that the BRC-selected half-coupling is structurally special across domains. If the controls behave equally well, or if the discovery law fails holdout, that is equally valuable because it narrows or falsifies the stronger interpretation.

The task is intentionally useful even on failure: it prevents post-hoc selection of primes, characters or alternative denominators and creates a reusable blind-test protocol for future Enterprise claims.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `BLIND_HALF_COUPLING_ARITHMETIC_PASS` — `m=2` has a preregistered simple law that survives every holdout prime, the two evaluators agree, and both `m=3,4` controls are strictly weaker under the same grammar;
- `BLIND_SHARED_ARITHMETIC_STRUCTURE` — `m=2` has a surviving law, but at least one control has equal-strength structure, so half-coupling uniqueness is not supported;
- `BLIND_DISCOVERY_OVERFIT` — a discovery law exists but fails at least one holdout prime;
- `BLIND_NULL` — no preregistered simple law exists for `m=2` on the discovery set;
- `BLINDNESS_BROKEN` — external/forbidden target information was consulted before raw freeze, or the preregistered grammar/ranges were changed after discovery data were seen;
- `CHECKER_DIVERGENCE` — the two independent evaluators disagree and the discrepancy is not resolved within task scope.

A `BLIND_HALF_COUPLING_ARITHMETIC_PASS` is still not a Foundation or physics theorem. It establishes only the exact arithmetic statement proved by the task and the comparative blind-test result.

Kill the current route immediately on `BLINDNESS_BROKEN`; do not salvage the same run by relabeling it blind. If the discovery grammar returns `BLIND_NULL`, do not widen the grammar inside this task. A richer arithmetic search, if later justified, requires a separately registered task.

If a holdout law survives but no exact proof is obtained, return the strongest finite statement and do not promote it to an all-prime theorem. If prior art is found after freeze, preserve the independent rediscovery provenance but classify novelty accordingly.
