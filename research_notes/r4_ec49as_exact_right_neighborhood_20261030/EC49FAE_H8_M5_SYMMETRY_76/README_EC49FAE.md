# EC49FAE — signed-X6 BRC prefix-tree involution and seven exact 76-cutoff certificates

2026-11-04 · Author-side finite proof / exact integer calculations / portable draft / independent review pending.

**Scientific inputs remain frozen:** Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; global scientific source `773d538180bfb49e24cffeb35c3ee75eb0628e2e`. Previous author-side frontier EC49FAD: `668eb626e4a735fd79f18c755f90829e35123897`, 3,163 arrangements not excluded below 76.

## Theorem, within the frozen 12,356-case double-collision finite catalog

The restricted native primitive signed-X6 codewords are

`a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`.

Let `τ` exchange `c↔d`, `f↔g`, leaving `a,e` fixed on **operation words**, not on raw spatial axes. For every window with complete BRC cache key `(u,v,w)` and required signature number `t∈{2,4}`, set `τ(u,v,w)=(v+2w,u−2w,w)`, retaining window h and t. In this exact catalog every schedule S has a distinct catalog partner τ(S), τ²(S)=S, and

`E_min(S)=E_min(τ(S))`.

Thus all 12,356 double-collision arrangements form **6,178 disjoint, cost-isomorphic pairs**. The 3,163 earlier unresolved arrangements contain five one-sided pairs whose other member already passed EC49FAD and 1,579 wholly unresolved pairs. Once the five prior certificates transfer, 3,158 unresolved schedules remain as 1,579 pairs.

### Proof and finite verification

The operation code is prefix-free. Among distinct symbols the only positive signed-native prefix overlaps are `LCP(c,f)=LCP(d,g)=1`; `τ` swaps these two and preserves all codeword lengths. Every pair of concatenated operation words therefore has the same signed-native longest common prefix length as the transformed pair, and the native prefix-tree edge cost is preserved. The 28 prepaid signed-native edges from the mandatory words `{ce,de,ec,ed}` are invariant as a set.

For a source key define `r=u+v−h−1, n_a=w−1, n_f=u−r−2w, n_g=v−r`, with `n_c+n_d=r, n_e=w`. Swapping c/d and f/g preserves r and w while exchanging their respective multiplicities, exactly producing the declared transformed full BRC key. The existing 9-history observation transducer is also preserved on the **declared finite model**: exhaustive checking of **137 distinct (h,key,t) families and 120,852 signature-qualified operation-word instances** confirms bijection and within-window color permutation. For four-color families the mapping is `1836687↔1872656, 1867942↔1873981`; for two-color families `1836425↔1866380`. All 12,356 source schedules and their partners were enumerated and the involution identities verified. Therefore any eligible observation-covering subtree corresponds to a transformed equal-cost subtree and conversely. This proves the claimed equality of exact minima on this finite source catalog.

This is an **operation-code** and finite observation symmetry, not a claimed universal global interchange of spatial axes E1/E2; e in particular stays unchanged.

## New exact integer 76-cutoff runs

The unchanged EC49FAD/EC49EXJ C++17 integer OR-mask trie DP was executed on seven new **24-observation-color** arrangements. Every case returned `BOUND_PASS minimum_total_at_least=76`. At cutoff 76, the fixed 28 prepaid edges leave a strict sublevel of incremental cost <48. The complete root-mask DP excludes such a covering in each fixed arrangement.

| Source rank | Symmetry partner | Valid words | Native trie nodes |
|---:|---:|---:|---:|
| 432 | 433 | 238 | 1150 |
| 514 | 515 | 249 | 1150 |
| 580 | 581 | 258 | 1150 |
| 618 | 619 | 265 | 1150 |
| 784 | 785 | 281 | 1475 |
| 1238 | 1239 | 343 | 1990 |
| 2580 | 2581 | 451 | 2222 |

Seven direct DP certificates transfer to seven distinct partners: **14 newly excluded**. Five previously one-sided EC49FAD certificates transfer `3830→3835`, `3833→3836`, `3832→3837`, `3829→3838`, `3828→3839`. All 19 targets were in the inherited 3,163 set and do not overlap. Consequently:

`3163 − (14+5) = 3144` arrangements remain unexcluded for `E<76`, arranged in **1,572 full symmetry pairs**. The global bound stays `63≤E*≤76`. Finding a <76 witness or proving all remaining pairs impossible is open.

## Reproduction and evidence

The frozen source catalog `EC49EXY_DOUBLE_CANDIDATES.tsv` is already published in this PR under `EC49EXY_H8_M5_EXACT_CROSS_FIBER_CAPS`: Git blob `61ffbcdba1679479fade3cfd052c2d9d6bbf30ce`, SHA256 `1e5f75bdc2491f355db6e2632fb6789a55397f7943c77c6ebf249807ee20712a`. The adjacent `VERIFY_EC49FAE.py.gz.b64` is the complete Python 3 standard-library program used for the finite catalog/family proof, seven native trie-input SHA256 checks, and optional solver re-execution. Decode using `base64 -d VERIFY_EC49FAE.py.gz.b64 | gzip -dc > VERIFY_EC49FAE.py`; run `python VERIFY_EC49FAE.py --tsv EC49EXY_DOUBLE_CANDIDATES.tsv`. For optional exact DP replay add `--binary ./exact_or_mask_dp` with the earlier frozen compiled C++17 solver.

`EC49FAE_REPORT.json` contains the seven individual input hashes, involution mappings and finite verification counts. Author-side verified: full catalog/family checker PASS, seven separate cutoff solver runs BOUND_PASS, EC49FAD source audit PASS. A single later attempt to combine all seven solver reruns hit the local execution time limit; it is not counted as completed. No native CLAIM, Result, independent Driver review or canonical mathematical admission is claimed.

**Next EC49FAF:** solve only the 1,572 unresolved orbit representatives, prioritizing small native tries and 24-observation and 22-observation families, and apply a separately verified symmetric transfer. Keep source/observer/algorithm frozen; verify any <76 signed-X6 witness independently before changing the global bound.
