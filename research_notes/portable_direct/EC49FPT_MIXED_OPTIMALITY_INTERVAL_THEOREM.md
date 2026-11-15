# EC49FPT — A nonempty native-BRC sensor-price interval in which every globally optimal strategy is mixed

**2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.** Independent portable scientific continuation of EC49FPS, frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. No P000/worldview change or formal Task/CLAIM/Result/Review is asserted.

## Exact question and prior results

Take the *entire* legal-root domain first represented by configuration 16995 in the frozen original native-BRC instance. It has **242 original configurations** with a uniform prior, **112 distinct named-root cost profiles**, **324 legal complete-allocation terminal scalar observations (T)** and **96 named-root/optional-demand-subset scalar observations (R)**. All responses are exact integers from the pinned rooted-Trie cost table. An adaptive decision tree must terminate at a unique rooted-cost profile; one R query costs `r>0`, one T query costs `t>0`. This is an exact finite static-observation problem over the original typed BRC substrate; the original configurations, root labels, demand subsets and provenance are retained.

Previous *globally optimal pure-sensor* expected costs on exactly this population are:

`E_R = 841r/242` (EC49FPS's globally optimal half-price mixed Bellman calculation has a root-only witness of 841 weighted R queries; any shorter root-only tree would contradict that proved global optimum);

`E_T = 641t/242` (EC49FPN's terminal-only exact Bellman optimum and decision-tree witness).

Prior fully recorded proof sources: [EC49FPN / PR #2479](https://github.com/awdawmip/enterprise-math/pull/2479), [EC49FPS / PR #2490](https://github.com/awdawmip/enterprise-math/pull/2490), and the exact EC49FPS machine certificate at commit `ab9f585d097492931704a4dd408afdc3948d439d`. These prior works were author-verified, not yet independently admitted by project Review.

Frozen raw master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Native rooted-cost CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

## New finite construction, fully explicit

Start with EC49FPS's certified **41-internal-node all-R tree**, weighted root-query total **841**. At its uniquely identified internal node querying original action **354** (named root 6, optional subset mask **2228224**), the candidate set contains **9 rooted profiles** with source-configuration mass **44**; the original root-only descendant costs **121 weighted root queries**.

Replace that one query by the legal complete-allocation terminal scalar query **117**, then restrict the original root-only descendant tree to each of the exact T-response fibers, skipping R observations that have become constant within the fiber. The fibers are:

| T response | Rooted profiles | Configuration mass | Weighted subsequent R queries |
|---:|---:|---:|---:|
| 207 | 1 | 1 | 0 |
| 210 | 3 | 3 | 5 |
| 211 | 1 | 1 | 0 |
| 212 | 1 | 1 | 0 |
| 213 | 1 | 1 | 0 |
| 214 | 2 | 37 | 37 |
| **Total** | **9** | **44** | **42** |

The locally substituted policy saves **79** weighted R queries (121 − 42) and adds **44** weighted T queries. Hence the complete mixed tree on all 242 source configurations uses exactly **762 weighted R queries** (841 − 79) and **44 weighted T queries**, giving a constructive upper bound

`E_mixed = (762r + 44t)/242`.

The fully explicit mixed tree, original configuration/profile weights and all observation keys are saved in [EC49FPT_MIXED_POLICY_EXACT_REPLAY_CERT.json](EC49FPT_MIXED_POLICY_EXACT_REPLAY_CERT.json). Its terminal query occurs only on the 44 configurations reaching the specified node.

## Theorem — a rigorously nonempty optimal-mixing interval

**For every positive query price pair satisfying**

`44/79 < r/t < 199/254`,

**every globally optimal adaptive identification strategy must use both named-root observations and complete-allocation terminal observations on positive-probability paths.**

**Proof.** The exhibited mixed tree beats *every* pure R policy exactly when

`762r + 44t < 841r`, i.e. `r/t > 44/79`.

It beats *every* pure T policy exactly when

`762r + 44t < 641t`, i.e. `r/t < (641-44)/762 = 597/762 = 199/254`.

These inequalities overlap strictly since `44*254=11176 < 15721=79*199`. Any optimal policy using a single query type on all positive-probability paths would cost at least the corresponding pure-sensor optimum, contradicted by the displayed feasible mixed tree. A global minimum exists: positive-cost noninformative queries can be deleted, and each informative observation strictly refines a finite candidate set, so the Bellman minimum is attained by a finite tree. This establishes the stated necessity of *some* genuine mixing by every global optimum. QED.

**Exact rational witness:** at `r=3t/5`, the best pure-R expected cost is `2523t/1210`, the best pure-T expected cost is `3205t/1210`, and the constructed mixed tree costs `2506t/1210`. The strict saving against the better pure strategy is `17t/1210`.

## Completeness and independent replay

The new decision-tree upper bound was constructed by reparsing the SHA256-verified raw original master and complete BRC root-cost table. The builder enumerated the **41 internal nodes × 324 candidate T observations** of *one pinned EC49FPS root-only witness* and computed exact response-fiber restrictions; within that **restricted single-splice family** the first improvement threshold is `44/79`. This auxiliary fact is intentionally scoped to that one original tree and one insertion.

The second, independently written original-configuration verifier reparses the two raw frozen files, regenerates all 242 class members and 112 root profiles and all query responses, and replays **all 242 original configurations** through the explicit mixed tree. It checks every leaf identity and obtains precisely `R=762, T=44`, with the sole T-action index 117; local output `EC49FPT_INDEPENDENT_FULL_REPLAY_PASS`. Reproduce using:

```bash
python3 VERIFY_EC49FPT_INDEPENDENT.py /path/to/frozen_inputs EC49FPT_MIXED_POLICY_EXACT_REPLAY_CERT.json
```

The finite *lower bounds* 841 and 641 are carried by the cited earlier Bellman certificates; the present work independently verifies the mixed *upper bound*. Full raw input, exact construction/single-splice scan script, previous Bellman certificates, full leaf-replay source and execution logs are also in the EC49FPT portable evidence archive. This does not assert that the displayed mixed tree is globally best at any interior price.

## Remaining mathematical frontier

EC49FPS had proved root-only optimality for `0 < r/t <= 1/2`. The present theorem shows departure from root-only optimality no later than the new bound `44/79` (and proves an open price interval that *forces* true mixing). The exact first global price breakpoint lies in `[1/2,44/79]` as a threshold bound; it remains to be computed. A natural next exact Bellman target is `r/t=3/5` with all **420** observation keys, to determine the global optimum and characterize which mixed decisions improve the exhibited tree. The ongoing full legal-root classification count stays **565/625**, as this work optimizes a previously classified domain.

No broader physical or cross-model claim is made. The original named-root distinction and the terminal observation quotient are typed by their declared scalar response and decision-tree horizon, with source provenance preserved.
