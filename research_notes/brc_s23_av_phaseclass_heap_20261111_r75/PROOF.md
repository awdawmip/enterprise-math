# R75 / S23-AV: Phase-class group exclusions with a globally ordered latest-time heap

**Author-side scope:** Frozen auxiliary rational-circle S23/AV input 43ec6098b1330ae86d0a7863be336c5d97f6ef34, unchanged. Not a heartbeat-native BRC theorem or authorized Task CLAIM, Result, independent Review, or mathematical acceptance. Reuses R71 group exclusion at 0b5319d7a0caf90dcd210e291152c6c06bbc2828, R72 identity-preserving grouping at 917f62a46d986a757476e0e4bc35ad603eba4fb9, and R74 complete latest-time oracle at 2021a3ab0aace0ab978bc6395e7d0e5f7bbf87c1.

## Target and exact state

Finite source identities (t,branch), t integer; a fixed rational anchor theta0=p/q in reduced form (q>0), rational query interval [L,U] containing theta0, rational phase x, integer observer j, and stable original-labelled target arc [{a theta},{b theta}) with boundary floors constant, no wrapping and strict order on the entire interval. Same-time branches have the same auxiliary phase; all identities are preserved in the index. Desired output is exactly the R74 all-real-parameter latest-time classifier: STABLE_NONE, STABLE t, or CHANGES with exact rational witnesses having different latest times.

Build a reusable source index keyed by exact residue r=(t*p mod q). Each nonempty phase class stores its complete (t,branch) identities and a descending list of its distinct source times; t_min and t_max are maintained. This source aggregation is a query representation, not deletion of branch provenance.

## R71 group exclusion as sound pruning

For one group with anchor residue rho={t theta0}, let beta={rho+x-j theta0}, d_min=t_min-j and d_max=t_max-j. For delta in [L-theta0,U-theta0], the lifted source phase lies within S=[s_min,s_max] where s_min and s_max are beta plus minimum/maximum of the four products of d_min,d_max with interval delta endpoints. Let A(theta)=a theta-k_a and B(theta)=b theta-k_b with fixed floor values; set Q_min=min(A(L),A(U)) and Q_max=max(B(L),B(U)). Membership would require an integer k with overlapping shifted target envelope, hence

    s_min-Q_max <= k <= s_max-Q_min.

Thus if ceil(s_min-Q_max)>floor(s_max-Q_min), the **entire class** is excluded for every real theta in I. An unsuccessful certificate says only UNKNOWN for the group. This exact integer test is the already proved R71 sufficient exclusion rule, retaining original labels and source grouping.

## Ordered heap composition theorem

Create a max-heap containing the largest **remaining** time of every group. Extract the largest time globally. On first visiting a class, try the R71 whole-group exclusion: if it succeeds, drop the entire class from the heap; otherwise mark the group unresolved. For an unresolved class, run R74's complete two-oracle time classification on the extracted time. If it is ALL_OUT, push the next remaining time from the same class into the heap. If it is ALL_IN or MIXED, return R74's STABLE-time or CHANGES-with-two-witnesses answer immediately. If all heap entries are exhausted, return STABLE_NONE.

**Proof of correctness:** At any extraction, the heap head is the maximum remaining time across all nonexcluded classes. Dropped groups contain no matching source at any theta by the sound R71 certificate. Every earlier discarded time is ALL_OUT by the complete R74 oracle. Hence the first surviving time that is not ALL_OUT is exactly the first non-ALL_OUT time in a full global descending scan. The necessary-and-sufficient R74 latest-time theorem applies, and its witnesses are unchanged. Source identities/ties remain retained in their original groups. No group-relative earlier time is chosen before an uninspected larger time from another group.

A key warning follows from the proof: scanning each phase group independently and returning the first local survivor is NOT correct; groups must be interleaved by global source-time order. The heap enforces this.

## Cost scope

For g phase groups and n distinct times, preprocessing with a hash map and per-class sorted descending lists costs O(n+sum_r n_r log n_r) ordinary comparisons/assignments, and retains O(n) identities. A query constructs a g-head heap, costs O(g) initial heapify, and uses at most g group-exclusion tests and k individual R74 classification tests, where k<=n is the number of inspected times. Each accepted class elimination skips its entire remaining times. With heap operations, the query has O(g+k log g) structural operations plus O(g+k) rational arithmetic calls, excluding integer bit costs. The exact magnitude of rational numerators/denominators and persistent path-copy update costs remain explicit engineering measurements, not hidden in unit-cost labels. The test implementation uses a reusable in-memory sorted-class index; integration with R72's *persistent* treaps and proof of their update guarantees remains an open follow-up.

## Exact executable tests

The Python Fraction checker imports the existing R74 exact classifier rather than replacing its mathematical oracle. On seed 751126, it compared the grouped-heap output against independent full R74 descending-time results for **2200** matched complete interval queries, including duplicate-time branches and negative t. All outputs agreed. In 797 queries at least one complete phase group was excluded; across the random tests this skipped 2604 distinct source times. Every CHANGES result also had its two rational witnesses directly evaluated for unequal latest times.

On the previously proved two-phase family C_N={(4k,b_k),(4k-1,b'_k):1<=k<=N}, theta0=1/4, I_N=[1/4-1/(100N),1/4+1/(100N)], a=1,b=2, j=x=0, both groups are excluded for N in {16,64,256,1024,4096}. Even for 8192 source identities, both groups were excluded and **zero per-time exact classifications** were needed. The attached verification.json records index construction separately from twenty reused queries. Single-run timings are observations, not uniform benchmarks or bit-complexity proofs.

## Next R76

Replace the sorted-class reference index with R72's two-level persistent treaps, preserve independent branch deletions and historical versions, and compare consistent complete interval latest-time outputs using exact integer-bit operation and memory accounting. Benchmark random, sparse-group, broad-interval and adversarial alternating-owner query sequences. Address same-time branch-dependent phase semantics only through an explicitly typed interface and treat parameter intervals crossing original arc ordering boundaries by separately certified pieces. No change to P000, ACTIVE worldview or frozen S23/AV inputs.
