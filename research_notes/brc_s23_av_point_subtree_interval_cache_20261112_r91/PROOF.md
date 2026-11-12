# R91 — exact point-witness subtree pruning and polarity interval-entailment cache

Date: 2026-11-12. Status: author-side proved lemmas and executable exact checks.
Model: auxiliary rational circular-source model only, frozen scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: R90, `e8435d251eb02e2c8c868e1632a61c439a166f57`.
Source implementation: `check_r91.py.gz.b64` (decode with `base64 -d check_r91.py.gz.b64 | gzip -dc > check_r91.py`) and prior R90 `check_r90.py`.
Run `python check_r91.py` after placing R90's plaintext script beside it.

## Model and exact target

Fix a finite set of integer source identities E={(t,b)}, a rational x, integer j,a,b and a closed rational query interval I=[L,U]. For real theta, define s_t(theta)={x+(t-j)theta}, A(theta)={a theta}, B(theta)={b theta}; membership M_t(theta) is membership of s_t in the directed half-open circle arc [A,B), empty when A=B. W_E(theta) is the latest qualifying (t,b) in lexicographic order or NONE. R90 classified the complete real interval as STABLE_NONE, STABLE(identity), or CHANGES with two directly checkable rational witness parameters. Its subtree OUT boxes already certify whole-interval exclusion but its initial and recovered point witnesses still used an unpruned descending linear walk.

## Theorem R91.1 — singleton-certificate point pruning

For any source-time AVL subtree v, parameter z in I, and query signature sigma=(j,x,a,b), if matching verified R89 OUT rectangles jointly cover every R90 residue summary rectangle {z} × [min_t(v,r), max_t(v,r)], then the subtree contains no qualifying source at theta=z. During a descending latest-source point search, discarding every such subtree preserves the exact latest (time, branch) identity and NONE outcome.

Proof: Fix any identity (t,b) in v. Its residue r has min_t≤t≤max_t. Rectangle coverage places (z,t) in a certified OUT rectangle with the same sigma; hence ¬M_t(z). It cannot win. All remaining identities are evaluated in descending time/branch order, so the first qualifying one is precisely W_E(z). Source identity fibers, branch tie-breaking, endpoint equality and every historical persistent root are retained. The covering test includes closed singleton endpoints, not only open-cell samples. A failed cover test merely causes normal traversal.

Consequently, applying point pruning both to the baseline parameter L and to a CHANGES witness returned by an exact polarity oracle preserves R90's all-real classification theorem. Its worst case remains O(m), and cover costs may exceed savings for small/non-coverable inputs.

## Theorem R91.2 — exact interval containment for both polarities

Let I'⊆I be closed rational intervals, with the same t, signature sigma and Boolean polarity p∈{true,false}. An exact polarity oracle asks for a parameter z∈I where M_t(z)=p, or returns NONE after exhaustive six-family rational critical partition verification.

(i) A stored witness z remains a valid positive oracle answer for I' exactly when z∈I'. (ii) A certified NONE for I proves NONE for every I'⊆I. (iii) When the stored witness lies outside I', the cached positive finding alone does not decide I'; and a NONE on I' does not decide a superinterval.

Proof: (i) directly re-evaluate the unchanged predicate at the same z. (ii) is monotonicity of a universal absence statement under domain restriction. (iii) follows because quantification over the removed portion can change existence; the implementation recomputes instead of inferring. This logic applies independently to presence and absence polarity (R87's P_t and N_t), and only under the exact original signature. Cache entries are per time, not per source branch/version: branch changes affect latest identity recovery but not M_t.

Implementation: bucket entries by (time, polarity, exact signature). For a requested interval, reuse a matching exact entry, an existing witness inside the subinterval, or an exact NONE on a containing interval; otherwise invoke the original precise R90 oracle. The present bucket scans prior entries linearly. A future interval index can accelerate lookups without altering semantics.

## Independent exact verification

The verification program imports the unchanged, source-pinned R90 executable checker. It compares R91 and R90 against R90's separate full six-family critical partition reference for 128 randomly selected historical queries after 128 persistent identity edits. Among these, 108 are CHANGES, and their rational parameter witnesses were directly checked. All 129 historical roots remain valid; the retained graph has 368 distinct AVL objects. Additional regression checks cover witness loss on a subinterval, certified absence on a subinterval, positive witness containment, signature mismatch and closed endpoints.

A separately constructed stable-champion family uses
E_n={(5,1)} ∪ {(18+16k,0): 0≤k<n}, sigma=(0,0,4,8), theta0=1/16,
I_n=[theta0−1/(10000(n+1)),theta0+1/(10000(n+1))].
One conservatively generated R90 OUT box excludes all higher source times. The same R87 exact oracle is used by (a) a fresh R75-style heap built from unordered identities each query, (b) R90 persistent AVL with interval pruning but linear point reads, and (c) R91 persistent AVL with both interval and singleton pruning. Nine cold queries per variant were measured within one Python process.

| Higher OUT sources | Heap median ms | R90 median ms | R91 median ms | Heap / R90 / R91 point member tests |
|---:|---:|---:|---:|---:|
| 16 | 0.812 | 0.345 | 0.310 | 17 / 17 / 4 |
| 64 | 3.412 | 0.834 | 0.535 | 65 / 65 / 6 |
| 256 | 13.224 | 2.246 | 0.662 | 257 / 257 / 8 |

At n=256, singleton pruning reduced point-level tests from 257 to 8, while preserving the existing eight polarity-oracle calls. In this illustrative run the full R91 cold query was ~3.40× faster than R90 and ~19.98× faster than the fresh-heap implementation for the specified family. These are measured local workloads, not universal complexity claims.

For 60 distinct nested query intervals on the same 65-identity root, exact-key R90 cache incurred 360 polarity oracle evaluations; R91's containment cache required six, with 354 sound cache inferences. On the 128 historical random queries, R90's exact-key cache made 183 oracle evaluations; R91 made 37 (90 positive-witness and 56 negative-absence interval inferences). The benchmark also measured 17,664 shallow AVL-node bytes and 79,304 shallow residue-summary bytes across the retained historical graph (Python object shallow sizes; shared nested integers and allocator overhead excluded).

## Cost and scope

Creating persistent AVL states in the three controlled families allocated 95/509/2555 nodes for 17/65/257 identities, with one-pass build times roughly 0.270/1.250/5.865 ms. GCD/phase-summary scans took ~0.016/0.031/0.082 ms and generating the single exclusion box ~0.087/0.046/0.048 ms. The three families' exact critical-rational counts were 34/130/514 and the maximum denominator bit lengths 17/19/21. These figures include a local scan of GCD and phase groups as a cost probe, not the implementation of the full R82 triple-index update path.

The ratio of measured (build+box) costs to (fresh heap query−R91 query) is below 1 for these three fixed-champion families; an illustrative single-query cost crossover is already observed when the persisted AVL construction is charged once. This uses one-process timings and does not account for all source-ingestion, storage, integer multiplication algorithms, or R86's complete persistent merged-profile construction. A complete R82/R83/R86/R90 multi-version end-to-end comparison remains an open engineering task.

The R91 combined correctness is exact for the stated finite source sets and all real theta in closed rational intervals, because the only oracle is the exact prior R90 one and all pruning uses certified OUT covers. The experiments are direct author-side checks, not independent review or native task admission.

## Status, owner, and next unit

The Source exact-task request `r91-20261112-research1-s23-lookup-v1` returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION` for task `RS-S23-AV`. Native RESEARCHER session issuance `r91-20261112-research1-session-v1` was refused with `SESSION_ISSUANCE_QUOTA`. This author-side artifact has no new authenticated RA, shared CLAIM, formal Result or independent Review; it retains the frozen input pin and precedes no P000 promotion.

Next R92: combine the R91 singleton and interval-entailment cache with an indexed set of variable-width certified OUT rectangles, and perform a full R82 three-index + R86 merged-profile comparison on an identical versioned STABLE/CHANGES workload, counting byte-size, retained memory, rational bit-operation proxies, cold/warm CPU, witness recovery and index update work.
