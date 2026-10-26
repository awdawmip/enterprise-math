# EC48A — Exact likelihood-threshold signature sweep for convexified BRC memory

**Date:** 2026-10-27. **Status:** author-side proved derivation, exact finite verification; not native Result, Driver review, mathematical admission, or Heartbeat dynamics.

## Frozen sources and relationship

GLOBAL_KNOWLEDGE_V1 canonical main at `59e3da7b1c0781ca47152f09faaa5e5af0ae73b4` (bootstrap/manual, P000, ACTIVE worldview, BRC and math policies). Enterprise Math canonical main at `c317e3a87685f1e6b089e9d9b808404ad6c26ab2` (portable protocol, weighted-BRC positive branch substrate). Exact research predecessor: EC47 at immutable commit `85a523ba6a887395c47d924fe037f772242f6a25`, `research_notes/r4_ec47_threshold_memory_20261026/EC47_THRESHOLD_MEMORY_ROC_REGION.md`. Parallel current research in `research_notes/brc_n4_exact_semialgebraic_policy_20261027_r5/` addresses variable-depth four-vector behavioral fidelity and is not claimed here. Registered activity: `RA-EMR4-20261027-0055-EC48SWEEP`; locally assigned Researcher-ID `EM-DIRECT-E48A27` (NOT native-verified or a task CLAIM).

This note *refines the executable consequence* of EC47.1–EC47.2: their finite family of general graph-coloring problems reduces to one exact rational-event sweep with no graph-coloring oracle. It does NOT solve EC47's still-open implication `conv(S_K)=Z => S_K=Z`.

## Model and declared observer

Fix nonempty finite historical label set H, future symbol set Y, and strictly positive rational joint source probabilities p(h,y),q(h,y) under P,Q respectively, normalized separately to 1. Preserve ordered source labels (h,y) and their weights. A K-state memory encoder chooses m by the hypothesis-independent stochastic kernel pi_h(m); after observing y, the terminal decoder declares P with probability u_m(y). Thus the full declaration matrix is w(h,y)=sum_m pi_h(m)u_m(y). Let alpha=sum p(h,y)w(h,y), beta=sum q(h,y)w(h,y), and S_K={(alpha,beta): permitted K-state policies}. The unrestricted full-history region is the planar zonotope Z=sum_(h,y)[0,(p(h,y),q(h,y))]. The two error coordinates are (1-alpha,beta). Both models observe exactly two stages, so their other two declared coordinates are fixed (2,2). A convex hull of S_K corresponds to permitting an initial persistent public seed or ex ante mixtures; S_K itself does not automatically permit that seed.

For lambda>0 put r_hy=p(h,y)/q(h,y) and sigma_lambda(h,y)=sign(p(h,y)-lambda q(h,y)). All ratios are positive rationals.

## Theorem — generic-signature formula and exact event algorithm

Write R={r_hy} as a sorted set of m<=|H||Y| distinct rationals. For each connected component I of (0,infinity)\R, choose one lambda_I within it and let

    n(I) = number of distinct sign vectors
           (sigma_lambda_I(h,y))_(y in Y), as h ranges over H.

**Then the exact least memory for convexified full region preservation is**

    K_hull := min{K : conv(S_K)=Z} = max_I n(I).                 (EC48A.1)

The maximum is attained away from all ratio breakpoints. It can be computed by exact rational sorting and a bitset-frequency sweep: initialize every history's |Y|-bit sign vector to all 1s for lambda<min R, sort all ratio events, group equal ratios, flip every affected (h,y) bit together, update only the affected histories' signature frequencies, and record the number of nonzero signature frequencies after each group. The maximum recorded count is K_hull.

**Proof.** EC47.1 proves that at any lambda, the least K achieving max_{(alpha,beta) in Z}(alpha-lambda beta) is the chromatic number of the graph linking two histories if they have opposite nonzero signs at some common y. Away from R, every sign is + or -. Two histories conflict iff their complete sign vectors differ. Hence this graph is complete multipartite, with one independent color class per distinct sign vector; its chromatic number is exactly n(I). At a breakpoint lambda0 in R, ties delete conflicts, while all strictly signed cells keep the same signs in both sufficiently near generic intervals. Consequently its edge set is contained in EACH adjacent generic conflict graph, and chi(G_lambda0)<=min(n(I_left),n(I_right)). No breakpoint can increase the global maximum. EC47.2 identifies convex-hull equality with support equality for every lambda>0, therefore with K at least this maximal chromatic number. This proves (EC48A.1).

Each cell's sign flips exactly once as lambda increases; simultaneous equal-ratio events must be processed as one batch, because zero-sign configurations at the breakpoints are not open intervals. The sweep is therefore exact. There are n=|H||Y| events, at most n batches, at most n bit updates, and at most |H| initial bitsets. With a dictionary for sign vectors it uses O(n log n) exact rational comparisons for sorting plus O(n) expected dictionary updates and O(|H|+n) stored words/event records. Exact rational comparison uses cross products; arbitrary-precision bit costs and large |Y|-bit signatures are NOT constant time. QED.

**Sharpened capacity bound.** K_hull <= min(|H|,2^|Y|). If one ordering y_1,...,y_s of Y satisfies r_(h,y_1) <= ... <= r_(h,y_s) for EVERY h, every generic sign vector is a suffix of +'s preceded by -'s, hence K_hull<=min(|H|,|Y|+1). The latter bound is sharp: choose |Y|+1 histories indexed by j=0,...,|Y|, uniform positive Q counts, and positive P counts equal to 1 on the first j labels and 3 on the remaining |Y|-j labels. After separate normalization, a threshold strictly between the resulting two ratio values produces all |Y|+1 different signatures.

## Exact positive-integer worked witness

Take H={a,b,c,d}, Y={x,y}. Specify unnormalized integer joint counts P=[[4,4],[4,1],[1,4],[1,1]] (total 20) and Q=[[1,1],[1,1],[1,1],[1,1]] (total 8). Independently normalize each measure. The likelihood ratios are 2/5 and 8/5. As lambda ranges over the three open intervals, the numbers of distinct history sign vectors are exactly (1,4,1). At lambda=1 all four ++,+-,-+,-- occur, so K_hull=4.

For alpha-beta the full best value is 48/160=3/10. At K=3 the exact optimum is 36/160=9/40: any three-state deterministic encoding must merge two distinct sign profiles, losing at least one nonzero cell coefficient of absolute integer numerator 12; merging two adjacent profiles loses exactly 12. A stochastic encoder/decoder cannot improve this bilinear objective beyond deterministic vertices, by successive optimization over their finite product of simplexes. Thus the exact strict loss is 12/160=3/40. The K=1,2,3,4 best numerators are respectively 0,24,36,48.

This is a memory *convex-hull support* witness, not a proof that seedless S_K fails to fill some point once K=K_hull. It also supplies no native six-axis coordinate realization, three-dimensional slice embedding, heartbeat time law, or physical inference.

## Verification and method reuse

The executable `EC48_VERIFY.js` (BigInt products and integer exact optimization) generates deterministic positive joint-count pairs with identical total mass under P/Q by permutation; it compares sweep signatures with direct sign evaluation in every generic interval, and compares the predicted minimum K with exhaustive deterministic memory-encoder and decoder optima. It also computes the exact chromatic number at every rational tie and verifies the tie cannot raise the maximum. `EC48_REPORT.json` gives the actual counts and worked witness. No floating-point comparison, QE/CAD, or tested finite bound is presented as the universal proof.

**Reuse resolution:** `REUSE_APPLIED` to EC47 threshold conflict graph and positive weighted BRC source semantics; `EXTEND_EXISTING_TOOL` for a strictly narrower algorithmic sweep specialization. Curated `enterprise_toolbox_registry.json` / `research_method_inventory.json` were checked at the pinned EM snapshot; no existing exact sign-profile sweep was identified in their matching records. No new Foundation-level tool family is asserted.

## Limits and next problem

Theorem is only for a two-stage **terminal binary decision** and equality of **convexified** ROC/error regions (time coordinates fixed). Finite source positivity and exact rational probabilities are assumptions. Histories observed at stage 1 remain eligible for memory encoding; no variable stop/continue actions or multi-stage forgetful dynamics are covered. This result does not upgrade the author's EC47 proof to independent mathematical acceptance.

**Next unit:** Resolve whether under the same positive-rational two-stage model and K>=2 one always has `conv(S_K)=Z => S_K=Z`, or construct a rational explicit counterexample with a full-policy point and an exact semialgebraic infeasibility certificate. For the parallel N4 variable-depth branch, test behavioral polynomial inclusion directly, not by silently replacing it with the signed LP certificate. Native Source owner/CLAIM and independent Driver review remain pending.
