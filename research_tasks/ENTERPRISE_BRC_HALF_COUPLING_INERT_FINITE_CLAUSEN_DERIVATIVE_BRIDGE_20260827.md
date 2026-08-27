<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-FINITE-CLAUSEN-DERIVATIVE-BRIDGE",
  "title": "Enterprise BRC Half-Coupling Inert Finite Clausen Derivative Bridge",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-inert-finite-clausen-derivative-bridge",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Close or exactly obstruct the inert-prime finite-Clausen derivative correction that remains after the all-prime half-coupling p-adic proof task isolated the split-prime modular boundary and the surviving valuation-1/valuation-2 middle blocks.",
  "next_action": "Work only on inert primes p congruent to 13,17,19,23 modulo 24. Derive an exact finite truncation identity or p-adic expansion controlling the degree at least p Clausen convolution correction and the two surviving middle valuation blocks modulo p^3, with the Frobenius sign (p/3) produced rather than assumed.",
  "dependencies": [
    "research_tasks/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF_20260827.md@main",
    "research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-PADIC-ALL-PRIME-PROOF/RR-3BF9820BB7FE480FAEAE.json@5abd65d786b1841ef7711a4150f3048c7724ef04",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF_RETURN_20260827.md@5abd65d786b1841ef7711a4150f3048c7724ef04"
  ],
  "source_refs": [
    "Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665, Conjecture A14(ii)",
    "Frits Beukers, Supercongruences using modular forms, arXiv:2403.03301",
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF_RETURN_20260827.md@5abd65d786b1841ef7711a4150f3048c7724ef04"
  ],
  "evidence_status": "PARENT_PROOF_TASK_BLOCKED_WITH_EXACT_INERT_FRONTIER / ALL_PRIME_TARGET_UNPROVED_AND_UNREFUTED",
  "last_progress_ref": "Parent result RR-3BF9820BB7FE480FAEAE proved the exact valuation stratification, refuted whole-tail vanishing, matched the split-prime modular framework only on split residue classes, and isolated the inert finite-Clausen derivative correction as the smallest unresolved lemma.",
  "last_progress_at": "2026-08-27T11:05:00+08:00",
  "hard_block": null,
  "tags": [
    "p-adic",
    "supercongruence",
    "Clausen",
    "hypergeometric",
    "inert-primes",
    "finite-truncation",
    "derivative-weight",
    "exact-proof"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-FINITE-CLAUSEN-DERIVATIVE-BRIDGE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP3",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-PADIC-ALL-PRIME-PROOF",
  "successor_gate": {
    "new_information_gap": "The parent proof task reduced the all-prime problem to the inert residue classes and identified the finite-Clausen derivative correction plus valuation-1/valuation-2 middle blocks as the sole exact unresolved bridge.",
    "why_parent_result_does_not_close_it": "The parent proved the valuation stratification and killed a naive tail argument, but neither the split-prime modular theorem nor formal Clausen identity controls the finite convolution correction modulo p^3 for inert primes.",
    "discriminating_outcomes": [
      "A complete inert-prime bridge yielding the target congruence for p congruent to 13,17,19,23 modulo 24.",
      "A weaker exact identity that controls one inert sign class and isolates the remaining class.",
      "An exact obstruction showing that one proposed WZ or p-adic-Gamma mechanism cannot supply the required finite correction.",
      "An exact counterexample to the inert-prime target, which refutes the all-prime conjecture."
    ],
    "kill_condition": "Any exact inert prime counterexample kills the target after independent recomputation. Any route that replaces the finite p-term truncation by the infinite Clausen identity without controlling degree at least p corrections is rejected as non-closing.",
    "alternative_route_or_free_exploration_considered": "The preferred routes are a p-deformed terminating hypergeometric or WZ identity with p^3-divisible boundary terms, and a p-adic-Gamma expansion pairing the two middle valuation blocks with the lower block. A finite-field or Dwork route is allowed if it proves the exact finite bridge rather than assuming it.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent all-prime task has already frozen the global proof search and its exact negative frontier. A focused successor prevents repeated split-prime work and concentrates proof effort on the only unresolved inert mechanism without rewriting the parent result."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC Half-Coupling Inert Finite Clausen Derivative Bridge

Status: `PUBLISHED_REGISTERED / DIRECT_USER_DIRECTION / CONTINUATION / EXACT_PROOF_FRONTIER`

## Mother question

For every inert prime

\[
p>3,\qquad p\equiv 13,17,19,23\pmod{24},
\]

settle the exact finite bridge needed to prove or refute

\[
S_p=\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
\equiv p\left(\frac{p}{3}\right)\pmod{p^3}.
\]

The parent task has already established that the split-prime modular route does not cover these residue classes and that the terms with valuations one and two cannot be discarded. The question here is therefore narrower:

> Can the finite Clausen convolution correction and the two surviving middle p-adic blocks be coupled exactly so that the inert Frobenius sign emerges modulo p^3?

## Frozen inputs and scope

Let

\[
A_n=\binom{2n}{n}^2\binom{3n}{n},
\qquad
F_{p-1}(z)=\sum_{n=0}^{p-1}
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}z^n,
\]

and

\[
G_{p-1}(z)=\sum_{n=0}^{p-1}
\frac{(1/6)_n(1/3)_n}{(n!)^2}z^n.
\]

The formal infinite-series identity

\[
{}_3F_2(1/3,1/2,2/3;1,1;z)
={}_2F_1(1/6,1/3;1;z)^2
\]

may be used only as an algebraic guide. It does not by itself identify the finite degree-`p-1` truncations.

The parent result has frozen the exact valuation theorem

\[
v_p(A_n)=\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor,
\qquad 0\le n<p.
\]

Hence the valuation blocks are exactly:

- valuation 0 for `0 <= n < p/3`;
- valuation 1 for `p/3 < n < p/2`;
- valuation 2 for `p/2 < n < 2p/3`;
- valuation 3 for `2p/3 < n < p`.

Only the final block vanishes termwise modulo `p^3`. The middle blocks are load-bearing.

The exact object to control is the finite correction

\[
(1+6\theta)\bigl(G_{p-1}(z)^2-F_{p-1}(z)\bigr)\big|_{z=1/2},
\]

including the convolution degrees `p,...,2p-2` and the interaction with the valuation-1 and valuation-2 blocks.

At least two structurally distinct proof mechanisms must be seriously tested unless one already closes or refutes the target. Preferred mechanisms are:

1. a terminating p-deformed hypergeometric or WZ identity whose boundary terms have explicit p-adic order at least three;
2. a p-adic Gamma expansion of the finite Clausen correction with exact pairing of the surviving blocks;
3. a Dwork or finite-field bridge only if it is proved at the finite truncation and derivative-weight precision required here.

Do not spend the task merely extending finite prime regression. Do not re-use split-prime modularity as if it covered inert primes. Do not assume the desired sign `(p/3)` inside a transformation whose purpose is to derive that sign.

## Hard target and required outputs

Hard target:

`INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_PROVED_REFUTED_OR_EXACTLY_OBSTRUCTED`

Required outputs:

1. An exact theorem or exact obstruction stated specifically for the inert residue classes modulo 24.
2. A complete finite-truncation derivation showing how degrees at least `p` are controlled modulo `p^3`.
3. Explicit treatment of both inert target signs: classes `13,19` and classes `17,23` modulo 24.
4. Full p-adic bookkeeping for the valuation-1 and valuation-2 blocks.
5. For a WZ or terminating deformation route, exact boundary terms and their p-adic valuations.
6. For a p-adic-Gamma route, the expansion order and every character/sign contribution used.
7. An exact dependency map separating formal Clausen algebra, imported p-adic theorems, and newly proved finite identities.
8. A deterministic checker used only as regression support for the exact identities, never as proof of the all-prime statement.
9. A durable return under `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md`.

A partial restricted-class proof is admissible only if the complementary inert classes and smallest unresolved lemma are frozen exactly.

## Research value to preserve

The parent proof search has already removed two major sources of ambiguity: the target is an exact prior conjecture rather than an Enterprise novelty claim, and the modular framework currently audited covers only the split half. It also proved that a naive termwise tail argument is false.

This leaves a much sharper mathematical problem: a finite p-adic truncation correction at a mixed hypergeometric/CM point. Solving this bridge could close the entire all-prime congruence when combined with a separately verified split-prime specialization. Refuting it or proving a route-specific no-go would be equally valuable because it prevents further false closures around formal Clausen squaring.

The task is purely arithmetic. No physical half-coupling interpretation, BRC theorem, packet/path theorem, or Foundation promotion is part of its target.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `INERT_BRIDGE_PROVED` — the finite correction is controlled for all four inert residue classes and yields the target modulo `p^3`;
- `INERT_TARGET_REFUTED` — an exact inert prime counterexample is found and independently recomputed;
- `INERT_RESTRICTED_CLASSES_PROVED` — a proper subset of inert classes is proved and the complementary classes are isolated exactly;
- `FINITE_CLAUSEN_ROUTE_NO_GO` — a proposed finite-Clausen mechanism is exactly obstructed without refuting the target;
- `PROOF_NOT_CLOSED` — serious distinct routes are exhausted and a strictly smaller unresolved lemma is frozen.

Immediate refutation rule: any exact inert prime violating the target must be recomputed by a second exact method and returned as `INERT_TARGET_REFUTED`.

Success requires exact finite-truncation control. An infinite-series identity, a numerical CM match, or arbitrarily long finite regression cannot substitute for the missing p-adic bridge.

The task must stop at the strongest exact statement reached and must not self-promote any arithmetic result into BRC, physics, or Foundation semantics.
