<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-QRF-R1-INDEPENDENT-FOUNDATION-VERIFICATION",
  "title": "QRF-R1 Independent Foundation Verification — Scale Coherence and First-Fiber Tightness",
  "kind": "RESEARCH",
  "owner": "research/qrf-r1-independent-foundation-verification",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Independent falsification-oriented verification of one audited quadratic-refoundation replacement candidate.",
  "next_action": "Reconstruct the candidate from frozen premises, attack the weakest hypothesis set, and return a proof, counterexample, or exact downgrade.",
  "dependencies": [
    "QRF Phase-B validation packet",
    "Enterprise Math source snapshot main@d16877c3b62a7d3b7568780c732f610c260c13c1",
    "current foundational-logic and native-semantics contracts"
  ],
  "source_refs": [
    "awdawmip/chatgpt-global-knowledge@1f037142d90ed3f326cabffc5d5d8d2c6274d4a1:journal/enterprise-math/2026-08-22/20260822T152200+0800-quadratic-refoundation-phase-b-validation.md",
    "awdawmip/enterprise-math@d16877c3b62a7d3b7568780c732f610c260c13c1:research_axiom_candidate_state_machine.json",
    "awdawmip/enterprise-math@d16877c3b62a7d3b7568780c732f610c260c13c1:FOUNDATIONAL_LOGIC.md",
    "awdawmip/enterprise-math@d16877c3b62a7d3b7568780c732f610c260c13c1:native_semantics_admissibility.json"
  ],
  "evidence_status": "INDEPENDENT_VERIFICATION_TASK_READY",
  "last_progress_ref": "awdawmip/chatgpt-global-knowledge@1f037142d90ed3f326cabffc5d5d8d2c6274d4a1:journal/enterprise-math/2026-08-22/20260822T152200+0800-quadratic-refoundation-phase-b-validation.md",
  "last_progress_at": "2026-08-22T15:22:00+08:00",
  "hard_block": null,
  "tags": [
    "qrf",
    "foundation-facing",
    "falsification",
    "independent-verification",
    "replacement-candidate"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "QRF1",
  "origin_kind": "FREE_AXIOM_CANDIDATE",
  "origin_candidate_id": "QRF-R1",
  "origin_candidate_state": "AUDITED_REPLACEMENT_CANDIDATE",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9cb0f9abbec5b946fb67557c2ef8e7d371df3e5aa059d409da1192a55cf0eac2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# QRF-R1 Independent Foundation Verification — Scale Coherence and First-Fiber Tightness

Status: `READY / DRIVER_APPROVED / DISPATCHABLE`

## 0. Task-local mother question

Can QRF-R1 be reconstructed, without importing the target quadratic law, as a sound replacement explanation that uniquely selects exponent `p=2` from a strictly weaker and non-circular primitive package?

The task is adversarial. The preferred outcome is the most accurate classification, including falsification or downgrade.

## 1. Frozen task-local inputs and scope

Treat the Phase-B packet only as the object under test, not as a proof authority.

Candidate premises to audit separately:

1. `S: N_{>0} -> N_{>0}` is strictly increasing.
2. `S(mn)=S(m)S(n)` for all positive integers.
3. The coarse inverse is max-safe: `R_S(N)=max{k:S(k)<=N}`.
4. There is a single root/refinement family used both for coarse collapse and for resolving the first nontrivial fiber.
5. At the first nontrivial fiber, lossless refinement succeeds exactly at the information-capacity lower bound: refinement radix equals fiber cardinality.
6. The identity case is not a nontrivial collapse.

Do not use `S(n)=n^2`, the square-basin identity, or the current quadratic axis law as premises.

The current square law may be used only after an independent derivation, as target-side comparison evidence.

## 2. Required mathematical / executable / formal outputs

### A. Rigidity chain audit

Reconstruct or precisely cite the theorem chain from strict monotone complete multiplicativity to `S(n)=n^alpha`, and then from integer-valued `n^alpha` on all positive integers to integral `alpha`.

State every hypothesis actually used. If the cited classical theorem does not match the candidate hypotheses exactly, either repair the proof from the stated premises or expose the missing assumption.

### B. Non-circular first-fiber semantics

Give a definition of the refinement/detail family that does not already encode the desired exponent.

The verification must answer whether “same family resolves the first fiber at the lower bound” is an independently stated semantic constraint or merely a disguised insertion of the target root formula.

### C. Exact exclusion of competing exponents

For each admissible integral exponent `p>=2`, analyze the first nontrivial fiber of `S(n)=n^p`.

Replace bounded evidence by theorem-level reasoning wherever possible. In particular, either prove that `p=2` is the unique exponent whose first fiber is losslessly resolvable at radix `2^p-1`, or produce a competing exponent/family satisfying the frozen premises.

### D. Orientation separation

Test max-safe orientation independently from exponent selection.

The return must explicitly separate:
- exponent rigidity;
- lower-bound fiber tightness;
- downward/max-safe orientation.

A capacity-tight nearest-cell or other alternative orientation counts as evidence that orientation is an additional primitive, not as a failure of exponent selection.

### E. Primitive-strength audit

Compare the candidate package against retaining the quadratic axis law directly.

Determine whether the replacement is genuinely weaker, merely equivalent after unpacking, or stronger because first-fiber semantics already smuggles in more structure than the target law.

## 3. Success, kill, and return criteria

Return exactly one leading verdict:

- `VERIFY_R1_STRICT_REPLACEMENT`
- `VERIFY_R1_ONLY_AFTER_NARROWING`
- `DOWNGRADE_R1_EQUIVALENT_REFORMULATION`
- `REJECT_R1_CIRCULAR_OR_FALSE`

A strict verification requires all of the following:

1. no target-law premise leakage;
2. an exact route from the stated scale premises to integral `p`;
3. a non-circular lower-bound refinement definition;
4. uniqueness of `p=2` under that definition;
5. explicit separation of max-safe orientation;
6. a weakest-hypothesis statement and negative boundary.

Kill or downgrade immediately if any of the following occurs:

- an admissible `p>=3` model satisfies every frozen premise at the same lower bound;
- the refinement family can only be defined by presupposing the selected exponent in the decisive step;
- the monotone-multiplicative rigidity step needs a missing hypothesis that cannot be derived;
- the replacement package is shown to be no weaker than directly assuming the square law and has no independent semantic content.

The return must include proof or counterexample evidence, exact hypothesis scope, relation to prior art, and a recommendation limited to this candidate.
