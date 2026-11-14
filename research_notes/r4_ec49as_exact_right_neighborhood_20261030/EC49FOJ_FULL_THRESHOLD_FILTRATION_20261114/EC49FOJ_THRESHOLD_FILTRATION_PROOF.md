# EC49FOJ — Exact threshold filtration of native BRC terminal observers

Date: 2026-11-14. Scientific input remains frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Continues EC49FOI [PR #2385](https://github.com/awdawmip/enterprise-math/pull/2385) at `a3a84742d87d7ded7fa00eee911df6daa4877121`. Status: reproducible exact finite author verification; `NOT_REVIEWED`.

## Finite model and theorem

There are 24 named demand labels and four named roots 03,05,06,07. For each cache configuration K, let A(K) be the set of *complete legal labelled root assignments*. Each root's exact cost D^K_r(S) is the minimum ordered signed-prefix union-cover cost obtained by native rooted trie DP. Define C_K(ρ) = Σ_r D^K_r(S_r(ρ)) for legal ρ and +∞ otherwise. Define the exact cost-labelled terminal observer at integer budget b:

```
F_b(K) = { (ρ,C_K(ρ)) : C_K(ρ) <= b }.
```

For any configurations A,B let

```
τ(A,B) = min_{ρ : C_A(ρ) != C_B(ρ)} min(C_A(ρ),C_B(ρ)),
```

with min of an empty set = +∞.

**First-separation theorem.** For every finite integer b, F_b(A)=F_b(B) **if and only if** b<τ(A,B). Proof: For b<τ, a cost-labelled assignment appearing in one observer must have the same cost in the other, or its smaller finite cost would contradict τ>b. Conversely, choose an assignment attaining finite τ; at b≥τ the cheaper exact cost-labelled pair belongs to one observer, while the other either omits that pair or attaches a different cost. Finite-domain attainment proves the claim. If the costs agree on every assignment, τ=+∞ and the observers agree for all b. QED.

Consequently the equality partitions of configurations refine monotonically as the threshold grows. This theorem holds for any finite exact cost-labelled root-assignment model, independently of DFS traversal order.

## Frozen exhaustive census

Input: original `master_and_radius3_cases.txt`, **94 keys, 178850 signed-prefix words, 38169 seven-key configurations**; SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Frozen 84 exchanges: `FIRST_NEUTRAL_EDGES_EC49FNS.txt`; SHA256 `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`. The original model's native BRC prefix-cover arithmetic and source pin are unchanged.

There are 51 distinct configurations. Fifty have **648** legal complete root assignments each; the remaining configuration 32279 has **1944**. Their exact **34344 complete assignment-cost records** are fully enumerated. For each configuration, the number visited under an exact B=210 cutoff equals the independently calculated product of legal root-choice counts; all exact terminal costs are at most **195**, so the enumeration covers the entire finite legal assignment domain.

| First separating budget τ among the 84 original edges | Edges |
|---|---:|
| 156 | 14 |
| 157 | 4 |
| 164 | 30 |
| 165 | 1 |
| 171 | 1 |
| 174 | 2 |
| +∞ (all-budget equality) | **32** |
| Total | **84** |

At b=155, all 84 exchanges preserve their entire cost-labelled terminal observer (EC49FOI). This new exhaustive computation distinguishes **32 exchanges preserving the full complete-assignment cost map at every budget** from **52 with exact finite first-separation budgets**. Thirty of the 32 all-budget equalities have identical four rooted DP tables and label domains. Two preserve the entire complete-assignment cost map despite at least one differing rooted table: `32315→32308` and `32315→32324`. The latter also changes the ordered DFS trace, as independently established in EC49FOH/FOI.

All-pairs equality comparisons across the 51 *entire* cost-labelled maps yield exactly **15 all-budget observer classes**, a refinement of the five classes at b=155:

| Budget b | Exact number of equivalence classes |
|---:|---:|
| 155 | 5 |
| 156 | 7 |
| 157 | 10 |
| 164 | 12 |
| 165 | 13 |
| 171 | 14 |
| 174 | 15 |
| 195 and every larger budget | **15** |

The full class members are reproducible as `FOJ_PARTITIONS.csv` using `VERIFY_EC49FOJ.cpp`, and the original complete 51-case certificate has 34344 rows.

Selected exact witness pairs, written (source-cost,target-cost) for a distinguishing complete assignment: `32315→32279`: τ=156 (illegal,156); `32315→32296`: τ=157 (158,157); `32318→32264`: τ=164 (164,165); `32315→32292`: τ=165 (166,165); `32315→32293`: τ=171 (173,171); `32315→32294`: τ=174 (178,174). These are exact integer native-prefix costs.

## Validation and next frontier

A C++17 exact rooted-trie DP enumerated every legal complete assignment of all 51 configurations and compared each pair of observer maps. Its `-O2` and `-O3` outputs were byte identical for the 84-edge and class-partition CSVs. A separate Python implementation rebuilt the original native trie and independently enumerated full assignments for **11 configurations / nine edges** covering all six finite separation levels and all-budget equality. No floating point, analytic trigonometry, or surrogate propagation was used.

The next problem is an exact **local key-path certificate** for all-budget equivalence avoiding full rooted DP regeneration. In particular, determine why `32315→32308` and `32315→32324` preserve full costs despite differing rooted tables, and classify local minimal distinguishing rooted-label subsets for the 52 separating edges.

Reproduction requires the original immutable signed-prefix input and 84-edge list. A complete self-contained frozen-input archive, full 34344-row certificate, source, executable verification commands, complete logs, and SHA256 manifest are in the accompanying EC49FOJ evidence package; the project's earlier source pin remains authoritative.

Provenance: original R4 Researcher-ID `EM-DIRECT-204C14`, Activity `RA-6893088D0A7347CE7F4D8720`. Last confirmed `RS-EC49AS` lookup found no canonical publication directory; this research record does not assert a formal CLAIM/Result or independent mathematical review.