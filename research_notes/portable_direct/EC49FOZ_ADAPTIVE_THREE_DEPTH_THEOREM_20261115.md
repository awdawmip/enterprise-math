# EC49FOZ — Adaptive BRC terminal observation depth is exactly three in two original classes

Research state: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
This is independently preserved portable research, not an accepted Result, a formal CLAIM, a new task or a Foundation change.

## Scientific scope

Use immutable BRC science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab and frozen input SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5. There are 94 cache keys, 24 named demands, four named roots 03/05/06/07 and 38,169 original configurations. In each of the two complete legal-root-domain classes represented by original configuration 14304 or 14309 there are 75 configurations, 40 distinct reachable named-root cost profiles and 432 complete legal allocations. The original byte-level prefix-Trie BRC root costs are reused from EC49FOX/EC49FOY (see provenance).

An unknown fixed profile p can be queried at any selected complete legal allocation a, revealing its exact integer terminal cost T_p(a). A subsequent query may depend on previously observed integer answers. The adaptive query complexity d is the minimum, over decision trees that identify every possible profile, of the maximum number of sequential complete-allocation observations on any branch. This is a repeated-query finite observer problem, not a claim about actual physical measurement cost.

## Theorem — strict adaptivity gap

For both frozen classes, the **optimal worst-case adaptive observation depth is 3**:

    d_adaptive(14304) = d_adaptive(14309) = 3.

The previous theorem EC49FOY gives the optimal number of **fixed nonadaptive** complete terminal observations as 5 for each class. Therefore the exact gap in this declared model is 2 observations (five fixed versus three adaptively chosen). Root names, profile identities, labels, input provenance and full original cost vectors remain preserved. This finite result is not a computational complexity improvement to generating the BRC costs.

## Exact lower bound (all two-query adaptive strategies)

For first query a and observed value v, let F(a,v)={p: T_p(a)=v}. An adaptive decision tree of depth at most two distinguishes all profiles if and only if **every** non-singleton first-response fiber F(a,v) admits a second query b(v) on which p ↦ T_p(b(v)) is injective. Necessity follows because two profiles agreeing on both answers reach the same leaf. Sufficiency follows by choosing that b(v) after reading v.

The executable checker enumerated all 432 possible first allocations in each class; for every first choice it found a non-singleton response fiber on which **none of the 432 candidate second allocations is injective**. Every cost comparison is over exact integers. Hence d_adaptive is at least 3, including arbitrary branching by the observed value. The minimum obstructing first-response fiber size across these 432 checks is 4 in both classes.

## Exact upper bound (constructive three-query strategy)

For class 14304 choose complete-allocation index 78 as the first observation. For class 14309 choose index 119. Indexing is zero-based, with optional labels ascending and legal named roots in the order (03,05,06,07) for each Cartesian component. Each first observation yields exactly 22 distinct values: 15 singleton outcome fibers and 7 nonsingleton fibers.

For each of these 7 fibers, select the smallest-index second allocation whose response fibers are either singleton or admit at least one injective third allocation. Within a second-response fiber requiring the final query, use the smallest-index injective third allocation. The checker enumerates all 432 candidates to show the required second allocations exist, and verifies that every remaining nonsingleton fiber admits a third query. The resulting policy has 22 first-result branches, 7 second-query nodes, 7 third-query nodes and 40 correctly distinguishable leaves. Thus d_adaptive is at most 3. The lower and upper bounds agree.

The decision-tree rule is deterministic given the frozen source; no unrecorded heuristic or probabilistic answer is used.

## Reproducibility

Source files and exact hashes:
- Frozen original input: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5.
- Rooted CSV for 14304: 03c030adfd11fd833a4d7234dd3b963511eb6ae14cb4c6010e8e667a03f3d52f.
- Rooted CSV for 14309: cc734f77d2d142651fdfcb41d38b20ae93b0d85f7b49fa90f2e868f92c0de7f6.

The standalone [exact verifier](EC49FOZ_ADAPTIVE_THREE_DEPTH_VERIFY_20261115.py) accepts the source layout of the prior EC49FOY evidence archive. Place that archive's SOURCE directory beside the verifier as SOURCE/; run Python 3.10+ on the script. It verifies the source hashes, reconstructs both full legal-root classes from all 38,169 original cases, uses the original named-root profile rows, enumerates every complete allocation and first/second-query alternative, and certifies the specified three-step policies. The checker was run locally with the following full output:

    PASS 14304 depth2 excluded for all 432 first actions; depth3 attained first 78 nodes 22 7 7
    PASS 14309 depth2 excluded for all 432 first actions; depth3 attained first 119 nodes 22 7 7
    EXACT_ADAPTIVE_MINIMUM_3_BOTH

Original local verifier SHA256 c6b623912428cc3a61797033d9d7bf16eec1b9cc802faa0aac1a8667e0616e92. A separately implemented recursive decision-tree solver generated complete 40-leaf policies for both classes and independently found depth 3. The supporting local evidence archive, EC49FOZ_ADAPTIVE_THREE_DEPTH_EVIDENCE_20261115.tar.xz, contains both solvers, the original frozen input, native root-cost CSVs, all decision trees, independent check results and logs; its SHA256 is 87885adf5ea5b87093ec4d07b961df42dec468954c792ff6779f3c51a88f18f3.

Source provenance: [EC49FOX PR #2445](https://github.com/awdawmip/enterprise-math/pull/2445) and [EC49FOY PR #2448](https://github.com/awdawmip/enterprise-math/pull/2448). Their claims are separate finite rooted-cost and fixed-observation results; this note advances only adaptive terminal observation under the exact same pinned corpus and legal-root classes.

## Next question and authorization status

Compare the adaptive and fixed observation complexities in other complete original legal-root-domain classes. In particular test whether the quartic subset-dependent cross-root gauge witnesses of EC49FOT [PR #2433](https://github.com/awdawmip/enterprise-math/pull/2433) force an irreducible ambiguity or admit similarly short adaptive separation, without collapsing named-root provenance.

Prior historical source attribution: EM-DIRECT-FA54A5 and RA-A7F2089A3138AD0D2DF8033C. This new portable research publication does not claim current possession of the original private session capability or update that Activity without authorization. The exact RS-EC49AS topic lookup on 2026-11-14T22:29:14Z, pinned to control source 9c5f14762899a21bd84cc086512fd6e40174a88e, found NO_CANONICAL_PUBLICATION_DIRECTORY, not a live formal Task/CLAIM. Formal result promotion and independent review remain separate.
