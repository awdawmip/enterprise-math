# EC49FNL supplement — complete four-root assignment gap for two 96-prefix profiles

**Date:** 2026-11-13. **Scientific pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** author-side exact finite result; NOT_REVIEWED; no native CLAIM/Result asserted.

## Lineage, scope and nonduplication

The existing EC49FNL [PR #2282](https://github.com/awdawmip/enterprise-math/pull/2282) already computes the full **30500–31499** interval and identifies the 94-prefix cases 31310 and 31323. This supplement does **not** add 220 to that already published interval count. It independently reruns and verifies 220 cases [30500,30719] from the original frozen BRC source and proves a new, narrower, *four-root* structural statement about cases 30709 and 30711 that is not the 05/06/07 theorem for the 94-prefix configurations.

For the original nine-state BRC, 178,850 lawful operation words, 94 complete raw cache keys and 24 observation demands, C(K) minimizes the union cardinality of nonempty **ordered, signed, native-X6 microstep prefixes** among lawful selected words. The immutable science and word grammar are retained; scalar length and unsigned or endpoint-only signatures are not substituted.

The original `scan_cached_radius3.cpp` trie/mask DP ran three separately completed intervals **[30500,30600), [30600,30700), [30700,30720)**; each log says `FINISHED`, with 220 consecutive rows total. Within this *cross-check interval*,

```
min_{30500 <= i < 30720} C(K_i) = 96,
minimizers = {30709, 30711},
max = 206 at 30697.
```

The minimizers are K_30709=`[0,4,5,11,33,35,37]` and K_30711=`[0,4,5,11,33,35,50]`. For each, a separate original-lawful 24-word certificate has native-prefix count **48+48=96**. Independently rebuilt Python prefix tries/demand-subset DP give **96** for both cases.

## Four-root theorem including alternative root 03

Both profiles have baseline 12-label first-root 05 and disjoint 12-label first-root 06 assignments. Optional first-root 07 may take exactly the original label indices

`Q={5,7,11,13,15,17,19,21}`,

and optional first-root 03 may take exactly

`P={11,13,15,17,19,21}`,

so P is strictly contained in Q. For the six labels in P there are three distinct admissible destinations (baseline/03/07); for the remaining two in Q\P there are two destinations (baseline/07). The other 16 labels remain at baseline. Consequently there are exactly

`3^6 * 2^2 = 2916`

complete root-assignment functions. For each rooted trie, `f_r(S)` is the exact integer minimum prefix count to cover required subset S, allowing incidental demands. Distinct first roots have disjoint nonempty prefixes, hence

`F_K(alpha) = f_03(S_03(alpha)) + f_05(S_05(alpha)) + f_06(S_06(alpha)) + f_07(S_07(alpha))`

is the exact global cost for every allocation alpha.

**Theorem (finite, sharp, complete 03/07 root-allocation margin):** For *each* K in {K_30709,K_30711},

```
F_K(alpha_baseline) = 96,
min_{alpha != alpha_baseline} F_K(alpha) = 104.
```

The baseline 05/06 allocation is therefore the **unique globally optimal root assignment**. All 2916 admissible assignments were evaluated using the complete exact four-root mask tables for the frozen original word set. Exactly three altered allocations achieve cost 104: transfer label 5 alone to 07; transfer label 7 alone to 07; or transfer both 5 and 7 to 07. None of the equality cases assigns a label to root 03. This extends the previously explored 07-only exchange argument to all original 03/07 simultaneous choices in these two configurations.

The one-key substitution **37→50** preserves the 96 optimum, the sharp eight-prefix gap, and the three equality allocations, while changing the complete assignment cost landscape. Across the 2916 allocations, K_30709 is strictly cheaper on 137, K_30711 is strictly cheaper on 1177, and they tie on 1602; the maximum absolute cost difference is three. Thus equality of a whole objective and all sharp alternative allocations does not require equality of the underlying cost function.

## Reproducibility and audit

The accompanying `COMPACT_EVIDENCE_EC49FNL.b64` is base64(zlib(JSON)) containing: lossless 220-case index/cost/assignment-count rows, all **four** root-cost arrays for each minimizer (64+4096+4096+256 values per configuration), both reconstructed 24-word lawful witnesses with original key types, and the exhaustive 2916-allocation margin tables/sharp assignments. Uncompressed canonical JSON SHA256: `2bae5c339f2174b1336c2c38b69402033a5860d4bf4d9d10c1dcf0a573db4156`.

The verifier `VERIFY_SUPPLEMENT_EC49FNL.py` decompresses this exact payload, checks the 220 rows and finite extrema, checks root masks/complete allocation counts and reproduces the strict 8-margin and cost-comparison counts. The two independent Python reoptimizations were actually executed, returning `INDEPENDENT_PASS 30709 96` and `INDEPENDENT_PASS 30711 96`. A separate complete local archive also retains original input, actual three FINISHED logs, root-dump source/output, native 24-word prefix paths, original C++ scanner and independent Python implementation.

Frozen original master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Frozen cases SHA256: `d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33`.

**Research continuation:** consume already-saved PR #2282 as the 31500 index frontier, then find a structural key-swap criterion sufficient to preserve complete root costs or the sharp gap without checking 2916 allocations. Preserve full ordered signed native provenance and distinguish this finite observation optimum from the unrestricted seven-key mother problem, which has an earlier 84-prefix feasible upper bound.

**Control:** Author-side evidence only. Exact native task/ownership receipt failed with `BACKEND_IDENTITY_CHECK_UNAVAILABLE` and `operation_sent=false`; do not represent Source artifact publication, registration or this supplement as an active CLAIM, formal Result or independent mathematical admission.
