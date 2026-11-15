# EC49FPY — Exact global first sensor-price transition and full sensor-use phase diagram (native BRC 16995)

**2026-11-15 | AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**

Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (unchanged). Scientific predecessors EC49FPN (PR #2479), EC49FPS (PR #2490), EC49FPT (PR #2494), EC49FPX (PR #2501). This is a **finite** result, not a general complexity claim.

## Hypotheses and exact theorem

The complete native-BRC legal root-domain class represented by original configuration 16995 contains 242 source configurations, 112 distinct **named-root cost states**, 324 legal complete-allocation scalar observations T of price `t>0`, and 96 legal named-root/subset scalar observations R of price `r>0`. Weights are **source-configuration multiplicities**, so the prior is uniform on all 242 configurations rather than on the 112 profiles. The identification target retains named roots and subset/source semantics; tests have exact integer responses and finite, unrestricted adaptive decision trees. Put `x=r/t`.

**Global theorem:**

* `0<x<44/79`: every optimal identifying tree uses **only R**; expected optimum `841r/242`.
* `x=44/79`: a pure-R tree and a mixed R+T tree both attain the global expected optimum `841r/242=(1682/869)t`.
* `44/79<x<1`: **every** global optimum uses both R and T with positive source weight.
* `x=1`: a pure-T and a mixed R+T tree both attain `641t/242`.
* `x>1`: **every** global optimum uses **only T**, with expected optimum `641t/242`.

The theorem determines optimal **sensor-use types** throughout all positive price ratios; it does **not** claim a closed formula for the numerical optimum inside the open mixed interval.

## New exhaustive boundary proof

Scale the prices to `r=44,t=79`. For each subset `M` of the 112 named-root profiles, let `w(M)` denote its total source-configuration multiplicity. An observation `q` partitions M into nonempty response fibers `M_{q,v}`. A nonsplitting query can be removed because its price is positive. The exact Bellman equation, with no depth limit, is

```
F({i}) = 0
F(M) = min_{q splitting M} { c(q) w(M) + sum_{v: |M_{q,v}|>1} F(M_{q,v}) }.
```

The frozen native named-root table completely determines **all 420** query response vectors. Deduplicating equivalent response partitions while retaining the cheaper type at `r<=t` gives **395 distinct partitions**. Every tree is represented by this recurrence because every strictly splitting observation reduces the finite remaining state set. Conversely, each minimizing action and child subtree determines a feasible identifying tree.

The complete exact-integer Bellman check gives

```
F(all 112 profiles; r=44,t=79) = 37004 = 841*44
optimal first original action indices = 346, 354
```

Its exhaustive solver uses the actual pure-root identifying tree as a feasible upper bound and the admissible lower bound `F(child)>=44*w(child)` for any nonsingleton response child. Branches are discarded only when this bound cannot improve the current valid upper bound. The first implementation computed 22,818 distinct nonsingleton Bellman masks. A separate proof run using **only** the pure-root incumbent calculated 20,107 nonsingleton masks with the same optimum. (Different bounds/visit orders need not have identical cache sizes.) A separate 242-original-configuration replay of the resulting tree verified exact response fibers and source labels, with weighted (R,T) path-count histogram:

```
(1,0):3  (2,0):65  (2,1):4  (3,0):58
(3,1):38 (4,0):35 (4,1):2  (5,0):37
```

The weighted sum `44 R + 79 T` over those 242 source paths equals **37004**. A second exact exhaustive ratio `(r,t)=(3,5)` gives **2491** weighted price units, matching the earlier EC49FPU feasible construction and settling its open exact-optimality question.

## Derivation of the full price phase diagram

For any fixed identifying policy `P`, let `R(P), T(P)` be nonnegative integer source-configuration-weighted sensor counts. Its total price is `R(P)r + T(P)t`. A feasible pure-root tree has weighted count `(841,0)`. New boundary optimality at `x=44/79` proves

`(R(P)-841)*(44/79) + T(P) >= 0`

for **every** policy P. At `x=0`, the same difference equals `T(P)>=0`. The difference is affine in x, and hence nonnegative throughout `0<=x<=44/79`. If `T(P)>0`, strict positivity holds throughout `0<x<44/79`; therefore every optimal policy there is pure root. At the endpoint the previously exactly replayed EC49FPT mixed witness `(R,T)=(762,44)` has `762*44+44*79=37004` and ties the pure-root optimum.

The EC49FPT mixed witness strictly beats **both** pure-type optima for `44/79<x<199/254`. The EC49FPX independently verified mixed witness `(37,604)` strictly beats both for `151/201<x<1`. These intervals overlap (`151/201<199/254`) and cover `(44/79,1)`; hence no pure-type strategy can be globally optimal anywhere in that open interval. This proves unavoidable mixed use, without assuming that either witness is the best mixed strategy.

At `x=1`, the prior complete 420-action Bellman result (EC49FPQ and EC49FPN) establishes the pure-terminal value `641`. EC49FPX gives `37+604=641`, an actual mixed co-optimum. For `x>1`, the cost difference of any fixed policy from `(0,641)` equals `R(P)x+T(P)-641`, is nonnegative at x=1, and increases strictly with x whenever `R(P)>0`. Every optimum is therefore pure terminal with value `641t/242`.

## Immutable inputs, reproducibility and limitations

* Frozen original master: `frozen_original_master.txt`, SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
* Native root-cost table: `EC49FPG_PROFILE.csv`, SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.
* The required pure-root incumbent certificate is `research_notes/portable_direct/EC49FPS_CONFIG_WEIGHTED_HALF_PRICE_CERT.json` at PR #2490 commit `ab9f585d097492931704a4dd408afdc3948d439d`.
* Run the accompanying `VERIFY_EC49FPY.py` with those **unchanged** three source files; it checks both SHA256 digests, reconstructs the original-domain class, all 420 queries and 395 response partitions, and proves `F=37004` with exact integer arithmetic.
* The supporting standalone evidence archive retains the full 242-row replay, 3:5 Bellman computation, previous certificates and frozen input files. The raw root-cost table is an earlier native Trie output and is *not* newly inferred from a different model. This manuscript claims neither Lean formal verification nor independent mathematical Review.

**Current governance:** formal topic `RS-EC49AS` has no immutable task publication directory at the last current-read snapshot. This work is an independent non-CLAIM portable research result; no Result/Review/Working Truth/Foundation authority is inferred.

**Next unresolved scientific unit:** find the **numeric** piecewise-linear optimum and all switch prices strictly inside `44/79<r/t<1`, while preserving full source weights and named-root observables. Independently continue the remaining 60 root-domain families, particularly nonconstant-subset invisible residuals of class 16943.
