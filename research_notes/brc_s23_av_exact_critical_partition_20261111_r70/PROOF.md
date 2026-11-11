# Enterprise Math R70 — exact finite-event interval certificate and cache admission

2026-11-11 · Predecessor R69 commit `4c1cc9305f368600ea41c8ecf3fc8e7846b5f75e` · Frozen scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged).

**Scientific object.** This is the auxiliary exact rational circle-source observer. For `a,b,t≥0`, rational `I=[L,U]⊂(0,1)`, the original-labelled nonwrapping arc is `A(θ)=[{aθ},{bθ})`; a source t qualifies iff `P_t(θ): {aθ}≤{tθ}<{bθ}`. Full events retain `(time,branch)` identities for future independent deletion. The current readout is the greatest qualifying time or empty. Neither this auxiliary carrier nor its ordinary rational arithmetic is claimed to implement native BRC/X6 dynamics.

## R70.1 — compile invariant arc boundaries

Assume `floor(aL)=floor(aU)=k_a`, `floor(bL)=floor(bU)=k_b`, and `{aE}<{bE}` at both E=L,U. Then the boundaries are affine throughout I and the arc remains nonwrapping. Precompute the floors and endpoint residues of a,b once per query. Per source t, test only its two floors and residues, then use R69's same IN/OUT/UNKNOWN inequalities. This is exactly equivalent to R69's endpoint classifier by substitution. For K sources taking the full path, the 12K source-level floor/remainder evaluations become 4K+8 including precomputation, saving 8(K−1) such operations; early exits and complete integer bit/time costs vary.

## R70.2 — finite critical-point completeness theorem

For fixed t and the above stable arc, let `k0=floor(tL)`, `k1=floor(tU)`. Form the finite set containing L,U and all strictly interior rational roots, for integers k from k0−1 to k1+1, of:

`tθ=k`, `(t−a)θ=k−k_a`, `(t−b)θ=k−k_b`.

For a zero coefficient, ignore the corresponding identically constant equality. At each sorted critical point and at one exact rational midpoint between successive points, evaluate P_t. **Then P_t is constant TRUE on the whole closed interval I exactly when all evaluations are TRUE; constant FALSE exactly when all are FALSE; otherwise it changes value.** Proof: between consecutive critical points, source wrap index and both affine comparison signs are fixed, hence P_t is constant on each open cell. Sampling critical points independently resolves source jumps and the inclusive lower/exclusive upper arc boundaries. The finite set covers every possible change, so these samples prove an all-real-parameter statement, not merely a grid claim.

The unrestricted procedure is complete. The checker uses a 12-winding explicit budget; when `floor(tU)−floor(tL)>12` it returns UNKNOWN. This is a precise resource-aware partial procedure, with O(W log W) exact-rational sorting for W candidate winding events in the fallback.

**Strict new witness.** `a=1,b=2,t=4,I=[249/1000,251/1000]`. At θ=1/4 the source wraps from near 1 to 0, remaining outside the arc [θ,2θ) before, at and after the wrap. R69 returns UNKNOWN because the t-floor changes. R70 proves OUT for **every real θ in I**. The left boundary is included (t=a) and the right boundary excluded (t=b).

## R70.3 — fixed-scan LRU thrash theorem

Let repeated identical scans access K distinct source keys in the same order, with LRU capacity B<K. Between consecutive appearances of any key lie K−1≥B distinct keys, so every repeated lookup misses. A scan-level policy that bypasses caching when its working-set cardinality exceeds B preserves exact decisions and avoids futile cache maintenance in this family. It is not a universal cache optimum. Cache signatures in production must bind immutable source/subtree identity, arc/original label, observation and anchor; t-only keys are safe only inside this isolated fixed-signature benchmark.

## Executed evidence

The full checker `check_r70.py` was locally executed using Python exact `Fraction` and the predecessor `check_r69.py`. Frozen input unchanged. There were 36 matched workloads: m∈{8,128}, n∈{16,256,1024}, source time offsets 0 and 10^18, and 1/4/16 queries per workload. Each of four methods executed 252 queries; 1,260 independent direct latest-source oracle checks at exact rational parameters all agreed. For 16-repeat workloads (4 cases each n), R69/R70 source event visits were 784/8,496/10,144 respectively; LRU misses were 49/8,211/9,979, and LRU evictions 0/8,064/9,840.

At n=16, R69 / compiled / LRU / adaptive time was 7.60 / 9.63 / 7.94 / 7.55 ms; at n=256, 86.06 / 90.76 / 90.81 / 92.64 ms; at n=1024, 101.93 / 108.53 / 117.07 / 100.47 ms. One-host runs: fewer integer operations do not ensure faster Python wall time. The model and exact outputs were matched; tree building/persistent update costs and full generic bit-operation accounting remain for R71.

Independent boundary-focused checks covered 671 exact (t,a,b,I) cases. R69 returned UNKNOWN while the complete R70 fallback made an exact IN/OUT decision in 86 cases; 101 exact rational points per certified case checked the implementation. Membership-change cases return UNKNOWN. Standalone verification program `check_r70_min.py` was executed and printed `R70_MIN_PASS 671 86 315` (315 cases with observed 101-point transitions). Full local scripts, per-case JSON certificate and expanded proof are retained in the R70 research bundle.

**Status.** Author-side derived mathematical proposition with finite exact execution, pending independent mathematical review and formal task adoption. No shared CLAIM or native BRC execution asserted.

**Next.** See NEXT_R71.md: wrap-aware immutable-subtree exclusion, original R66–R68 matched total cost, branch identities and observer-specific cache keys.
