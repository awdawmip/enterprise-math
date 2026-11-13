# EC49FNU — Reusable one-sided sensitivity frontiers for rooted native BRC

**2026-11-14 | frozen science pin** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` | author exact proof and finite validation; **NOT_REVIEWED**.

Continues [EC49FNT #2325](https://github.com/awdawmip/enterprise-math/pull/2325) and [EC49FNS #2318](https://github.com/awdawmip/enterprise-math/pull/2318), using original [EC49FNN #2298](https://github.com/awdawmip/enterprise-math/pull/2298) frozen words, cases and native exact-cost table without repeating the global 1,000-case optimization. This note tests the same 84 first-neutral cache-key exchanges within IDs 32000–32999, with 24 distinct demands and native signed ordered roots 03,05,06,07.

## Theorem: transfer the old cutoff search frontier

For source configuration `A` and target `B` with the **same legal demand-label set at each root**, let `D_{K,r}(S)` denote the exact minimum number of nonempty native ordered signed rooted-prefix nodes to cover label set `S`, allowing additional covered labels. For any complete legal root allocation `a`, `F_K(a)=sum_r D_{K,r}(S_r(a))`. These exact rooted functions are monotone in inclusion.

For each partial allocated label set `S`, define
```
h_r(S) = max(0, max_{T: S subseteq T subseteq L_r}
                   ( D_{A,r}(T) - D_{B,r}(T) ))
L_{A->B}(p) = sum_r ( D_{A,r}(S_r(p)) - h_r(S_r(p)) ).
```
Then for every complete legal allocation `a` extending partial allocation `p`,
`F_B(a) >= L_{A->B}(p)`. Indeed, for each final `T_r` containing `S_r(p)`, the definition of `h` gives `D_B(T_r)>=D_A(T_r)-h_r(S_r(p))`; rooted monotonicity gives `D_A(T_r)>=D_A(S_r(p))`. Sum the inequalities.

Run one exact `A` cutoff enumeration at integer threshold `b`, and preserve its surviving complete leaves plus its **disjoint first-pruned partial subtree roots**. For every old pruned subtree root `p`, if `L_{A->B}(p)>b`, the entire subtree remains safely pruned for `B`. Only expand the unsafe frontier roots; evaluate `F_B` at these newly reached leaves and the old surviving leaves. This obtains exactly the target allocation-identity/cost map at and below `b`, without reconstructing a complete target allocation search. If this map equals the old map and both contain the first two distinct costs `C<S<=b`, the optimal cost `C`, its multiplicity `m`, and gap `g=S-C` are preserved. The `h` tables are computed by superset-max subset DP in `O(sum_r |L_r| 2^|L_r|)` operations once both native rooted tables are available.

## Frozen 84-edge exact certificate

The executed C++17 `VERIFY_EC49FNU_FRONTIER.cpp` regenerated the six distinct **source** cutoff frontiers exactly once and reused them across all 84 edges. It compared every transferred map with the independent direct target low-layer enumeration inherited from EC49FNT.

| Measured finite item | Exact count |
|---|---:|
| Source configurations and their initial visited nodes | 6; 951 |
| Initial first-pruned partial states / low leaves across six source runs | 534 / 20 |
| Same-root-domain edges | 82 |
| Edges needing no new subtree traversal | **60** |
| Of the above, edges with changed full rooted functions | **30** |
| Edges requiring selective expansion of unsafe frontier roots | 22 |
| Unsafe pruned subtree roots across edges | 390 |
| Additional selectively visited nodes / complete leaves | **1,266 / 128** |
| Independent target cutoff DFS visits over the 82 edges, for comparison only | 14,129 |
| Verified transferred low-layer maps matching independently calculated target maps | **82 / 82** |

The 82 common-domain edges comprise 30 unchanged-root-profile edges and 52 changed-root-profile edges. Of the latter, 30 require *zero* target subtree traversal, while 22 require selective exploration. Node counts describe allocation search trees only, not end-to-end wall-clock complexity (rooted-table computation and independent checking are additional).

### Two genuine domain-expansion cases

The remaining edges `32315 -> 32279` and `32318 -> 32279` add exactly two target-only legal choices at root 03, for labels 11 and 13. The theorem's equal-domain hypothesis is **not** invoked there. Instead the independently executed `VERIFY_EC49FNU_DOMAIN.cpp` splits each target domain into **648 shared** allocations and **1,296 target-only** allocations (1,944 total). It checks exact costs of all cases. For each edge, the target-only minimum is **156**, uniquely attained, and none cost at most `S=155`. The three shared low-layer allocations of cost at most 155 have precisely the same identities and costs at source and target; no discrepancy was found. Thus the original first-two-layer equality holds across both expanded-domain edges too.

**Joint conclusion:** 84/84 selected edges possess equal first-two-layer identity/cost maps. New contribution: reusable one-sided sensitivity certificates needing no extra subtree expansion for 60/82 same-domain edges, and bounded selective expansion for the other 22. These are complete finite and theorem-level author-side results for the declared model, not universal claims for arbitrary BRC key families.

## Reproducibility and saved evidence

`EC49FNU_NEW_CODE_RESULTS.tar.xz.b64` in this folder is lossless base64 of an xz tar containing both **actually executed** C++17 validators, their full 84-edge and two-domain output tables, stderr results, and the new-file SHA256 manifest. Decode with `base64 -d EC49FNU_NEW_CODE_RESULTS.tar.xz.b64 | tar -xJf -`. Decompressed tar SHA256: `cacbfbad303096b547fd58a78e879f0f916590e94949b48eff921cd8f9a7181e`.

The unchanged original input names are `master_and_radius3_cases.txt`, `FIRST_NEUTRAL_EDGES_EC49FNS.txt`, and `EXACT_NATIVE_32000_32999.txt` from the prior EC49FNN/EC49FNS/EC49FNT evidence. Compile `g++ -O2 -std=c++17 VERIFY_EC49FNU_FRONTIER.cpp -o verify_frontier`; run `./verify_frontier FIRST_NEUTRAL_EDGES_EC49FNS.txt EXACT_NATIVE_32000_32999.txt < master_and_radius3_cases.txt > EC49FNU_FRONTIER_RESULTS.txt`. Compile the domain verifier similarly; run `./verify_domain EXACT_NATIVE_32000_32999.txt < master_and_radius3_cases.txt > EC49FNU_DOMAIN_RESULTS.txt`.

**Next question:** derive a reusable domain-change transfer bound for newly legal root assignments, and sharpen the superset deviation envelope at the 390 still-unsafe partial frontiers to avoid all 22 remaining selective subtree expansions. Formal task claim, Result and mathematical review remain separate from this author-side saved research.
