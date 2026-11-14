# EC49FPA — Exact expectation-optimal depth-three adaptive BRC terminal sensing

Date: 2026-11-15 (Asia/Shanghai). Research state: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable research continuation of EC49FOZ, without a new formal CLAIM or Result.

## Fixed original BRC input and precise statistical question

Frozen science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Frozen original data SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
Original evidence: EC49FOZ archive SHA256 `87885adf5ea5b87093ec4d07b961df42dec468954c792ff6779f3c51a88f18f3`; source [PR #2454](https://github.com/awdawmip/enterprise-math/pull/2454), immutable commit `62826f378a05a2243472e67ff4fb94752d75f20c`. Root-subset profile CSV SHA256 for 14304: `03c030adfd11fd833a4d7234dd3b963511eb6ae14cb4c6010e8e667a03f3d52f`; for 14309: `cc734f77d2d142651fdfcb41d38b20ae93b0d85f7b49fa90f2e868f92c0de7f6`.

Each of two complete original legal-root-domain classes, represented by configuration indices 14304 and 14309, contains 75 native configurations, 40 distinct reachable-root cost profiles, and exactly 432 complete legal root assignments. Let `T_p(a)` be the exact integer terminal cost of profile `p` under assignment `a`. A deterministic adaptive query policy selects its next complete assignment from earlier observed exact costs, identifies the unknown **root profile**, and uses at most **three queries** in its worst case. EC49FOZ proved that three is the optimal worst-case depth (versus five fixed observations). Here minimize the *expected* number of queries **within this depth-three class**, under two distinct uniform-prior models: (i) uniform over the 40 different root profiles and (ii) uniform over the 75 original configurations. For the latter model, 38 profiles have multiplicity 1, one has multiplicity 2, and one has multiplicity 35 in each class. Duplicate configurations of one root profile are intentionally treated as observationally equivalent.

## Exact finite theorem

| Class | Minimal expectation, 40-profile prior | Minimal expectation, 75-config prior | Unique expectation-optimal first query |
|---|---:|---:|---:|
| 14304 | **73/40 = 1.825** | **177/75 = 2.36** | 78 |
| 14309 | **73/40 = 1.825** | **177/75 = 2.36** | 119 |

In either class, *exactly three of the 432* possible first observations permit complete discrimination within depth three. Full classification (the totals are sums of path lengths, divided by 40 or 75 as appropriate):

| Class | First query | Profile-weight query total | Configuration-weight query total | Profiles requiring second / third | Configurations requiring second / third |
|---|---:|---:|---:|---:|---:|
| 14304 | 78 | **73** | **177** | 25 / 8 | 60 / 42 |
| 14304 | 201 | 76 | 181 | 29 / 7 | 64 / 42 |
| 14304 | 198 | 78 | 183 | 31 / 7 | 66 / 42 |
| 14309 | 119 | **73** | **177** | 25 / 8 | 60 / 42 |
| 14309 | 181 | 76 | 181 | 29 / 7 | 64 / 42 |
| 14309 | 180 | 78 | 183 | 31 / 7 | 66 / 42 |

At the optimal first query, the 40 distinct profiles split into 22 cost fibers, 15 singleton and 7 nonsingleton; in the optimal tree, 15 profiles stop at depth 1, 17 at depth 2, and 8 at depth 3, giving `15 + 2*17 + 3*8 = 73`. A concrete optimal decision tree, including each per-fiber action and exact cost branch, appears in the companion result certificate `EC49FPA_DEPTH3_EXACT_RESULT.json`. The other 429 first queries each admit a concrete obstructing first-readout fiber.

## Proof by exhaustive, exact dynamic programming

Let `C` be all 40 distinct profiles and `Q` the 432 complete assignment queries. For nonempty `F ⊆ C`, let `Π_a(F)` be the partition by the exact integer `T_p(a)`. Choose nonnegative integer profile weights `w_p`, with `w_p=1` (40-profile prior) or the exact original-configuration multiplicity (75-config prior). Put `w(F)=Σ_(p∈F) w_p`.

Define `I(G)` to mean that `|G|≤1` or **some** `c∈Q` is injective on `G`. After a first query has left a nonsingleton fiber `F`, an adaptive two-query continuation exists **if and only if** some second query `b∈Q` satisfies `I(G)` for **every** `G∈Π_b(F)`. On this domain, the minimum total weight of profiles needing a third query is exactly

```
B_w(F) = min_(b∈Q; all G∈Π_b(F) satisfy I(G))
             Σ_(G∈Π_b(F); |G|>1) w(G).
```

For fixed first query `a`, a depth-three decision tree exists exactly when `B_w(F)` exists for all nonsingleton `F∈Π_a(C)`. In that case, its **minimum total weighted number of queries** is precisely

```
S_w(a) = w(C)
       + Σ_(F∈Π_a(C); |F|>1) w(F)
       + Σ_(F∈Π_a(C); |F|>1) B_w(F).
```

This is an equality, not only a bound. Every surviving state pays the first observation; all states in nonsingleton first fibers must pay a second; and states in nonsingleton second fibers must pay a third. Branches from different observed first/second integer costs are independent and may choose different queries. Conversely, these minima assemble into a valid policy on the entire finite state set.

An exhaustive enumerator tested all 432 first queries, all 432 second choices for each relevant fiber, and all 432 potential distinguishing third queries for each remaining fiber. It returned exactly the six feasible (class, first-query) rows shown above, and excluded 429 other first queries per class. Two algorithms agreed: (A) direct profile-value partition optimization; (B) independent exact-integer **780-pair collision-bitset** feasibility and weighted-cost verification. Both priors were checked by both engines. Source costs were reconstructed with native signed-byte-prefix Trie machinery and immutable CSV/root-subset records inherited from EC49FOZ; no floating-point comparison is involved. Locally generated explicit 429-witness tables and full source are preserved in the accompanying integrity-checked evidence archive.

The theorem is scoped to the **two finite original legal-root-domain classes**, exact terminal-cost queries, their stated priors, and worst-case adaptive depth at most three. It does not identify the minimum expectation among policies of *unrestricted* depth.

## Evidence and next questions

Primary optimizers: `EC49FPA_OPTIMAL_EXPECTED_3.py` and `EC49FPA_CONFIG_WEIGHTED_3.py`; independent verifier: `EC49FPA_independent_certificate.py`. Machine certificates: `EC49FPA_DEPTH3_EXACT_RESULT.json`. Locally retained evidence additionally includes full frozen original input, both root profile CSV files, two per-class 429-obstruction TSVs, both program outputs, source byte hashes, and the exact preceding FOZ verification scripts. Their original input and intermediate rooted-cost tables are preserved, rather than replaced by approximate arithmetic.

Next: (1) optimize **unrestricted** expected depth, which may have a different optimum; (2) classify priors on the original configurations rather than equiprobable root profiles; (3) extend collision-mask policy optimization to other root domains; (4) for terminal-invisible original BRC gauge pairs, prove inductively that no adaptive policy observing only the same entire terminal cost function can distinguish their underlying root representation.

No change to P000, ACTIVE worldview, or research review/admission state.
