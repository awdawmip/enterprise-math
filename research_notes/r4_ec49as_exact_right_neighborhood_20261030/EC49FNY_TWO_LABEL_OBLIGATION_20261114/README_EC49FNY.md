# EC49FNY — Two-label obligation certificate for BRC cut transfers

**2026-11-14 · frozen science** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` · **AUTHOR_PROVED_EXACT_FINITE / NOT_REVIEWED**.

Continuation of EC49FNX [PR #2338](https://github.com/awdawmip/enterprise-math/pull/2338) at immutable `37cdbf2c24156254d7b0d56c811208d0df79078e`. The 84 first-neutral exchanges (168 directed transfers), seven-cache-key configurations and native signed ordered-prefix word stock remain frozen. No 24-demand global optimization is rerun.

## Theorem: future-label forcing

Let `L={0,...,23}` be distinguishable demands, `R={03,05,06,07}` the lawful rooted native microsteps, `D_{K,r}(S)` the exact minimum prefix-cover cost for subset `S`, and `p` a target-lawful partial root assignment. Write `U(p)` for its unassigned labels, `S_r(p)` for already assigned demands under root `r`, and `R_K(l)` for lawful target roots of demand `l`. For nonempty `T⊆U(p)` define

```
H_T(p)=min_{rho∈Π_{l∈T}R_K(l)} Σ_{r∈R} D_{K,r}(S_r(p)∪{l∈T:rho(l)=r})
H_h(p)=max_{T⊆U(p), |T|=h} H_T(p),   H_0(p)=LB_K(p).
```

**Claim.** For every complete lawful assignment `a` extending `p` and every `0≤h≤|U(p)|`, `F_K(a)≥H_h(p)`, and `H_0(p)≤H_1(p)≤...≤H_|U|(p)`. Consequently `H_h(p)>B` certifies *all* extensions exceed cutoff `B`; a failed plain root lower bound `LB_K(p)≤B` does not prevent a short future-label certificate.

**Proof.** For any fixed subset `T`, every full lawful extension restricts to one of the assignments `rho` minimized in `H_T`. Root-cover monotonicity then gives `F_K(a)≥Σ_r D_{K,r}(S_r(p)∪rho^{-1}(r))≥H_T(p)`. The maximum of lower bounds remains a lower bound. If `T⊂T'`, every legal assignment on `T'` restricts to one on `T`, and root-cover monotonicity gives `H_{T'}≥H_T`; taking maxima proves monotonicity across horizons. All quantities use original signed ordered native prefix rooted DP, with label and root identities intact.

## Exact finite result and sharp one-step obstruction

EC49FNX's 16,876 source cuts include 16,624 target-lawful cuts. Rootwise margin grouping proves 16,550 directly; 74 target lower bounds remain to check, of which 18 satisfy `LB_target≤B=155`. All 18 occur in exactly `32315→32279` and `32318→32279`. Their target root-subset patterns are identical between the two directions: only **nine distinct witness patterns**.

For the 12 unresolved margin strata, even exact *joint* root-drop envelopes `max_p Σ_r(D_source-D_target)` cannot certify a stratum: each contains a true target-LB failure. Thus root-drop correlation alone cannot remove the need for additional future-demand information.

**One-label certificates:** 14/18 (`7/9` distinct patterns) have `H_1>155`. **Exactly four** (`2/9` distinct patterns, repeated twice) have `H_1≤155`, yet **every one of the 18** has `H_2>155`. The two distinct strict one-label obstructions have `(LB,H1,H2)=(152,155,158)` and `(150,153,156)`; hence horizon two is the smallest universal horizon within this `H_h` family for these residual cuts. The nine `H_2` values range from 156 to 164.

The new exact verifier needs **zero local cut-repair DFS visits**, compared with 84 visits in EC49FNX. It still checks 74 candidate current lower bounds and separately performs 592 search-node visits for four newly lawful target-root choices; the latter produce zero low-cost leaves. The 168 previously verified two-layer assignment maps remain stable; there is **no runtime-speedup or general complexity claim**.

## Provenance, files and verification

Frozen input hashes:
- `master_and_radius3_cases.txt`: SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`
- `EXACT_NATIVE_32000_32999.txt`: SHA256 `c9314021942397a0b5a3e7a90d965fb19a853bdc486f7610721fc748a057c0f9`
- `FIRST_NEUTRAL_EDGES_EC49FNS.txt`: SHA256 `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`

Attached `VERIFY_EC49FNY.cpp.xz.b64` decompresses into the executable C++17 verifier, SHA256 `10554598d51198026054b11fc8263836ef4a4a4b0301e671fbf8d1b6f85004dd`. Run as `g++ -std=c++17 -O2 VERIFY_EC49FNY.cpp -o verify; ./verify FIRST_NEUTRAL_EDGES_EC49FNS.txt EXACT_NATIVE_32000_32999.txt < master_and_radius3_cases.txt`. `-O2` and `-O3` produced byte-identical complete output.

`EC49FNY_CERT_ALL.txt.xz.b64` decompresses to **198** certificate rows (168 MARGIN, 12 JOINT, 18 WITNESS), SHA256 `708da9a677ecf1d7842daf732ea51c796262a2974ef3476c9ef34f2f4107b271`. `VERIFY_EC49FNY_INDEPENDENT.py.xz.b64`, SHA256 `07d0aab126af3186d6ebeb5919b9d80e0c25e1efca88f5753513cd9b21e2f68b`, independently reconstructs the **32279** target root tries and exact root-subset DP from all 178,850 original signed words, and recomputes the nine witness H1/H2 values. It reports nine distinct targets, seven one-step and two two-step witnesses, without borrowing C++ rooted cost tables.

Full summary: `directions=168 all_safe=166 source_cuts=16876 legal_cuts=16624 impossible_cuts=252 groups=3587 safe_groups=3575 unsafe_groups=12 paired_root_queries=47760 safe_cuts=16550 possible_cuts=74 fallback_checked=74 fallback_failed=18 repair_nodes=0 repair_leaves=0 target_only_pairs=4 target_only_nodes=592 target_only_leaves=0 joint_safe_groups=0 joint_safe_cuts=0 horizon_cut_witnesses=18 one_label=14 two_label=4`.

**Unresolved:** derive a compact criterion predicting the one-step/two-step obstruction from root-profile overlap, without enumerating all candidate labels, and test **non-stable** one-key neighbors to establish discriminating power. This exact finite author-side certificate is not an independently admitted theorem. P000, ACTIVE worldview, Task/CLAIM/Result and source-exposure requirements are unchanged.
