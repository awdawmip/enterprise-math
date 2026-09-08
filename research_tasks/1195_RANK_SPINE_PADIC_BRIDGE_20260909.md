<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-1195-RANK-SPINE-PADIC-BRIDGE",
  "title": "1195: Test the 2c+1 Rank-Spine to p-adic Supercongruence Bridge",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "CP3 proves an archimedean/bilateral rank spine: for rank r=2c+1, negative shifted modes activate first at order x^r and the first nonzero negative-mode jet is the upside-down companion. CP1 records that the same Cohen–Guillera formula class has baseline supercongruence depth p^(2c+1). No causal valuation or filtration theorem connecting these appearances of 2c+1 is known in this route.",
  "next_action": "Fix one c=2 and one c=3 rational hypergeometric identity from the documented catalog, write the exact finite p-adic truncation and its shifted/bilateral coefficient data, and test whether the order-r negative-mode activation can be translated into a Dwork, finite-difference, or valuation filtration that forces p-adic divisibility r. Produce either a theorem on a nontrivial subfamily or the first exact counterexample to the proposed bridge.",
  "dependencies": [],
  "source_refs": [
    "research_notes/1195_research_handoff_index_20260909.md",
    "issue:1195#issuecomment-5533600396",
    "issue:1195#issuecomment-5533544516",
    "issue:1195#issuecomment-5533621206"
  ],
  "evidence_status": "RESEARCH_HANDOFF_INTEGRATION_V1",
  "last_progress_ref": "research_notes/1195_research_handoff_index_20260909.md",
  "last_progress_at": "2026-09-09T00:50:00+08:00",
  "hard_block": "RANK_SPINE_TO_PADIC_VALUATION_BRIDGE_OR_NO_GO",
  "tags": [
    "1195",
    "pi-power",
    "rank-spine",
    "supercongruence",
    "p-adic",
    "bilateral",
    "Dwork",
    "upside-down-series"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-1195-RANK-SPINE-PADIC-BRIDGE",
  "parent_objective_id": "EM-PI-POWER-SPECTRAL-SELECTOR",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1195P",
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

# 1195: Test the 2c+1 Rank-Spine to p-adic Supercongruence Bridge

Status: `READY / DIRECT USER RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Does the odd rank `r=2c+1` that controls the archimedean hypergeometric kernel, the first activation order of bilateral negative modes, and the upside-down companion also control the baseline `p^r` supercongruence depth through a genuine p-adic filtration or valuation theorem, or is the repeated exponent only a catalog-level coincidence?

## 1. Frozen inputs and scope

Read `research_notes/1195_research_handoff_index_20260909.md` first. Consume CP1 and CP3. The following are already established in this route and must not be presented as new:

- complement-symmetric rank `2c+1` produces the universal critical archimedean exponent after multiplication by a degree-`c` polynomial;
- bilateral negative modes first occur at shifted order `x^(2c+1)`;
- the first nonzero negative-mode coefficient matches the upside-down companion structure;
- the Cohen–Guillera survey records baseline supercongruence exponent `p^(2c+1)` for the same class.

The equality of these integers is only a research lead. This task may use classical Dwork, WZ, hypergeometric supercongruence, finite-field, p-adic gamma, and motive results with exact attribution. It must not infer a p-adic theorem from complex Taylor vanishing alone.

## 2. Hard target and required outputs

Hard target: `RANK_SPINE_PADIC_BRIDGE_PROVED_OR_KILLED`.

Deliver all of the following, or an exact negative boundary replacing an impossible item:

1. Choose one explicit `c=2` and one explicit `c=3` rational hypergeometric identity and state the exact finite sums, primes excluded by denominators, and claimed baseline congruence depth.
2. Rewrite the relevant shifted/bilateral coefficient relation at rank `r=2c+1` in a form meaningful over the chosen p-adic domain. State precisely which complex-analytic ingredients disappear and which algebraic coefficient identities survive.
3. Identify a candidate p-adic filtration, valuation, finite-difference operator, Dwork congruence, or gamma-factor mechanism whose length is exactly `r`, or prove that the bilateral rank datum cannot determine such a filtration.
4. Prove on at least one nontrivial subfamily that the rank-spine mechanism forces valuation at least `r`, or give an explicit identity/prime family showing that identical archimedean rank data can have different supercongruence depth.
5. Distinguish baseline `p^r` divisibility from refined `p^(r+1)` corrections and from accidental extra divisibility at exceptional primes.
6. Explain the role, if any, of the upside-down companion in the p-adic proof. Do not claim causal relevance merely because the same denominator power appears.
7. Return a clear prior-art map: which valuation theorem is classical, which translation from the pi-free rank spine is new synthesis, and which proposed bridge remains conjectural.

A successful negative result may show that supercongruence depth depends on Frobenius/unit-root data invisible to the archimedean selector rank; it must provide an exact separating example or theorem, not only a conceptual warning.

## 3. Research value to preserve

The project currently has an exact finite archimedean rank spine and an independently recorded p-adic exponent with the same value `2c+1`. Establishing a common filtration would connect spectral precision, bilateral completion, upside-down companions, and supercongruence depth across two absolute-value regimes. Killing the bridge would be equally important because it prevents an attractive but false adelic unification from contaminating later precision theory.

Preserve the distinction between numerical coincidence, shared hypergeometric rank, and an actual mechanism. The scientific value lies in proving the implication or locating the missing arithmetic datum.

## 4. Success, kill, and return criteria

Success is an exact p-adic theorem on a nontrivial `c>=2` family deriving the baseline rank-sized valuation from a clearly identified finite mechanism, together with a second test showing its scope; or an exact counterexample/no-go demonstrating that the archimedean rank spine is insufficient and identifying what additional p-adic structure is required.

Kill any route that argues from the repeated symbol `2c+1` alone, treats complex Taylor zeros as p-adic divisibility without an integral bridge, reports prime-by-prime numerics as proof, or folds refined `p^(r+1)` corrections into the baseline statement.

Do not attempt a general motivic unification before the two explicit low-rank tests are resolved. Return the first theorem, exact separating counterexample, or sharply identified missing filtration datum.