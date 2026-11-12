# R91 — Full-history exact crossover: heap, profile AVL and certified subtree AVL

Date: 2026-11-12. Status: author-side mathematical theorem and exact Fraction verification. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is the auxiliary rational circle-source model, not a native X6/P000 promotion.

## Exact common output

For finite integer identities `E={(t,branch)}`, integers `j,a,b`, rational `x`, closed rational `I=[L,U]`, let `M_t(theta)` assert that the fractional part of `x+(t-j)theta` lies in the directed half-open circle arc from `{a theta}` to `{b theta}` (empty when endpoints coincide). Let `W_E(theta)` be the lexicographically latest qualifying identity or NONE. All evaluated methods return the exact all-real statuses STABLE_NONE, STABLE(identity), or CHANGES with two rational parameters whose directly evaluated winners differ.

H: R83-style ephemeral heap, rebuilt per query, with the same R90 exact polarity oracle (so unlike the earlier specialized R83 certificate-only prototype, it handles arbitrary signatures). P: the actual R86 persistent full-winner-profile AVL. C: the actual R90 persistent residue-summary AVL with certified OUT box pruning. H reconstructs the per-version heap from a single shared event log, while P/C retain every historical root. H/C reuse their same exact per-time oracle answers across versions. All were tested on identical source histories in one Python process.

## Theorem R91.1 — an exact special-family complexity separation

Let `N>=1`, `theta0=1/16`, `delta=1/(10000(N+1))`, `I_N=[theta0-delta,theta0+delta]`, with `j=x=0`, `a=4`, `b=8`. Form nested source prefixes of

`E_N={(5,1)} union {(18+16k,0):0<=k<N}`.

For **every** prefix and **every real** `theta in I_N`, `W_E(theta)=(5,1)`. Every R86 source critical partition for this family has only the two endpoint values of I_N, so every overlay stores only two endpoint atoms and one open-interval atom. The original R86 profile AVL therefore takes O(N log N + QN) constant-size profile-overlay operations over N updates and Q exact queries per historical version. R83's repeated heap construction needs Theta(QN^2) entry operations across the same complete history. The original R90 classifier also incurs Theta(QN^2) initial point-membership tests across this family, **even though certified subtree exclusion makes its number of new polarity-oracle calls small**.

Proof: write `theta=1/16+e`, `|e|<=delta`. Then `4theta<5theta<8theta<1`, so source 5 belongs throughout. For any `t=18+16k`, the fractional part of `t theta` is `1/8+te` because `|te|<18/10000`; it is at most 0.1268, whereas `4theta>=0.2496). Hence every later source is excluded. At theta0 all six R77 critical linear forms (slopes 4,8,-4,t,t-4,t-8 and their constant offsets) lie at least 1/16 from their nearest integer; throughout I_N their displacements are at most 18/10000, hence no interior crossing occurs. An AVL insertion builds O(log(k+1)) nodes and each R86 overlay has bounded three-atom work. H builds k heap entries per query for historical version k. R90 starts each query with its descending `point(root,L)` scan, and source 5 is the last examined, giving k tests. Summing k proves the respective totals. The theorem counts the displayed structural and rational operations; actual integer bit complexity depends on operand lengths.

This also yields a concrete repair mechanism: for fixed `(L,j,x,a,b)`, augment every persistent node with `C_v=max(C_left,(t,max_branch) if M_t(L) else NONE,C_right)`. By the associative max law, the root supplies the exact initial champion at O(1) query cost, and AVL edits rebuild it along changed paths. A different query endpoint/signature selects a different summary.

## Executed exact experiments

Stable-family complete build plus all historical queries, medians of 3 trials in milliseconds:

| later OUT sources N | queries/version Q | H heap | P R86 profile | C R90 boxes |
|---:|---:|---:|---:|---:|
|16|1|2.53|3.31|3.02|
|16|4|7.56|3.29|12.62|
|64|1|25.43|17.34|29.51|
|64|4|83.49|17.45|110.85|
|128|1|87.04|39.68|95.44|
|128|4|339.67|39.74|371.86|

For N=128,Q=1, the exact oracle calls were H=129 and C=7; P builds and reuses its exact merged profiles. Python retained algorithm-specific deep-size estimates, counting shared objects once, were H=18,420, P=462,737 and C=323,456 bytes; P/C each allocated 1,148 persistent structural nodes. P recorded 2,865 merged profile atoms. These estimates exclude the common input log, ephemeral heap and process RSS.

A second, much wider rational interval I=[-1/4,3/5] with j=2,x=1/7,a=1,b=3 gives CHANGES at every prefix in the tested families. The exact six-family reference partition and two distinct rational witnesses were verified for every historical version. No valid OUT box was supplied in this regime.

| higher sources N | Q | H heap ms | P profile ms | C lazy AVL ms |
|---:|---:|---:|---:|---:|
|8|1|11.30|436.29|9.39|
|8|4|8.86|474.20|9.06|
|16|1|30.81|3444.48|31.45|
|16|4|34.13|3614.94|38.77|

At N=16, P executed 202,522 merged profile-atom evaluations during historical root construction. Together the two regimes provide an exact, discriminating algorithm choice: few-cell stable winners favor P on repeated queries; wide, changing profiles favor lazy exact polarity evaluation. C's oracle-call reduction is real, but its present champion scan can dominate wall time.

All code uses standard-library Fraction. The actual local suite checked the all-real R90 reference profile at every prefix in the stable family, checked every OUT cover and compared R86/R90 representative retained historical trees; the wide suite checked every prefix and every reported CHANGES witness directly. All assertions passed. CPU results are illustrative wall times rather than universal machine bounds. Full input-transform, source update, query, exact rational computations, branch recovery and retained-history footprint are separately represented; independent big-integer bit-operation instrumentation remains a concrete R92 task.

## Provenance and current controls

The local full reproduction bundle contains PROOF.md, README.md, check_r91.py, bench_dynamic_r91.py, verification_r91.json and verification_r91_wide.json together with exact predecessor code snapshots. R86 predecessor: `awdawmip/enterprise-math@5b4f6fa4f442358fe721e9c2c0eb3b238f588845`; R90 predecessor: `awdawmip/enterprise-math@e8435d251eb02e2c8c868e1632a61c439a166f57`; R83 reference comparison: `d4451a0d8ffd359ec43565fa681f23932b6b0405`. All are author-side scientific observations.

Native exact task lookup on 2026-11-12 returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION` for `RS-S23-AV`, and new session issuance returned `SESSION_ISSUANCE_QUOTA`. A new Researcher-ID, RA, shared CLAIM, Result and independent Review therefore were not obtained in this run. Preserve these provenance and authority limits.

Next R92: implement fixed-anchor champion summaries in C, test the same two regimes with exact witness restoration; add changed left-endpoint invalidation, rational bit-cost counters and certified box-index update accounting.