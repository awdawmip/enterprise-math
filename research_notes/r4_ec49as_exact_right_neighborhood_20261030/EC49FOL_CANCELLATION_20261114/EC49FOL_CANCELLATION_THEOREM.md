# EC49FOL — Exact cross-root cancellation and terminal first-separation theorem

Date: 2026-11-14. Author-checked mathematics and exact finite enumeration; **NOT_REVIEWED**. Scientific parent: EC49FOK PR #2393 @ `ba72605fed95280371a262362997e5aceee2564c` and EC49FOJ PR #2390; frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Theorem — first separation for changing legal domains

For each configuration K, let L be finite named demand labels and R finite named roots, each E_K(l) a nonempty admissible root domain. With exact integer root costs D_r^K(S), the legal complete assignments are A_K=∏_{l∈L}E_K(l) and C_K(ρ)=Σ_r D_r^K({l:ρ(l)=r}). Define the exact named terminal graph G_K={(ρ,C_K(ρ)):ρ∈A_K} and filtration F_K(B)={(ρ,c)∈G_K:c≤B}.

**Result.** The two filtrations are equal for every integer B exactly when G_A=G_B. Otherwise, their first distinct threshold is B_*=min{c:(ρ,c)∈G_A △ G_B}.

**Proof.** Below B_* every pair in the symmetric difference lies outside both threshold restrictions, so the restrictions coincide. At B_* a pair in the difference belongs to exactly one restricted graph. QED.

When the legal assignment domains coincide, this reduces to B_*=min_{ρ:C_A(ρ)≠C_B(ρ)}min(C_A(ρ),C_B(ρ)), with empty minimum +∞. Each common assignment has component changes δ_r(ρ)=D_r^B(S_r(ρ))-D_r^A(S_r(ρ)); its exact *total* cost is invariant iff Σ_r δ_r(ρ)=0. Componentwise projected-root equality (EC49FOK) suffices for all-budget invariance, but signed root changes can cancel at specific named assignments.

## Frozen BRC census

Input: `master_and_radius3_cases.txt`, SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, 94 source keys, 178850 root-labelled signed-prefix words, 38169 cases. Directed edge list `FIRST_NEUTRAL_EDGES_EC49FNS.txt`, SHA256 `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41` (both preserved in the preceding EC49FOK evidence). Independent reference: `FOJ_EDGE_FIRST_SEPARATION_84.csv` from PR #2390.

The C++17 verifier rebuilds the native signed-prefix trie and exact integer rooted cover DP for each of 51 configurations. It enumerates **648 named full assignments per shared-domain edge** for **82** edges (53,136 total comparisons). The two changed-domain edges have assignment-map sizes 648 and 1944, respectively. All **84** first-separation levels agree with the independently saved EC49FOJ reference.

| Exact category | Count |
|---|---:|
| Shared legal root domains; all-budget terminal maps identical | 32 edges |
| Shared domains; terminal maps differ | 50 edges |
| Changed legal domains; first separation at B=156 | 2 edges |
| Shared-domain full assignments with changed summed cost | 3,795 |
| Shared-domain full assignments with at least one changed root cost | 3,799 |
| Changed-root assignments with **exact zero-sum cancellation** | **4** |
| Edges containing cancellation | **2** |
| Edges containing opposite-signed root deltas | 5 |

Of the 50 different shared-domain edges, exact first-separation thresholds are 156 (12), 157 (4), 164 (30), 165 (1), 171 (1), 174 (2). The complete 84-row classification is in `EC49FOL_CANCELLATION_84.csv`; no sampling is used.

### Two native witnesses

Each of the edges `32318→32274` and `32318→32287` has exactly two legal assignments with nonzero rooted changes that cancel. Their root-order (03,05,06,07) difference vector is **(-1,0,0,+1)**.

Demand labels 0…23 assigned in order:

- `5 6 5 6 6 5 5 6 5 6 6 7 5 6 6 3 5 3 6 7 5 3 5 6`: exact total cost 180 on both sides;
- `5 6 5 6 6 5 5 6 5 6 6 7 5 6 6 5 5 3 6 7 5 3 5 6`: exact total cost 182 on both sides.

Each affected edge has 648 legal assignments, 244 assignments with nonzero root-level deltas, 242 assignments with nonzero summed deltas and exactly 2 cancellations. These two edges nevertheless first separate at B=156. The witnesses establish **assignment-specific cross-root cancellation** inside the frozen native model.

## Verification and provenance

`VERIFY_EC49FOL.cpp` performs exact integer enumeration with the original trie-DP and compares all 84 first separation values with independently published EC49FOJ. GCC C++17 -O2 and -O3 produced byte-identical result CSVs. `VERIFY_EC49FOL_INDEPENDENT.py` uses the distinct Python trie-DP from the earlier EC49FOK source, independently reconstructs the two cancellation edges, all 648 assignments per edge, both witness costs, delta vectors and the first threshold 156. The observed summary was:
`EC49FOL_EXACT_PASS stable_domains=82 all_budget_equal=32 differing=50 domain_changes=2 assignments=53136 changed_assignments=3795 canceled_components=4 edges_with_cancellation=2 edges_with_mixed_delta=5 cached_root_profiles=168`.
Independent Python conclusion: `EC49FOL_INDEPENDENT_EXACT_PASS`.

This is finite exact author validation for the frozen 51 configurations/84 directed edges, and an elementary theorem for finite named cost-labelled graphs. It adds no new formal CLAIM, Result or mathematical acceptance. Historical researcher/activity provenance: `EM-DIRECT-204C14` / `RA-6893088D0A7347CE7F4D8720`; the last verified lookup of `RS-EC49AS` returned `NO_CANONICAL_PUBLICATION_DIRECTORY`.

## Next unit

Characterize whether nonzero reachable-root deltas can cancel *identically for every complete assignment*, and derive a computable rigidity criterion. One approach is the zero-sum kernel of root Boolean-cube Möbius coefficients under per-label one-hot constraints. Preserve the named source/path observation layer when considering any later updates.
