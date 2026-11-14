# EC49FOI — Exact threshold-terminal invariance despite divergent BRC DFS traces

**Date:** 2026-11-14. **Frozen scientific pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Parent:** [EC49FOH, PR #2382](https://github.com/awdawmip/enterprise-math/pull/2382) at `9dc3a1efb101acad90d466c477f8785d9265599d`. Native ordered signed-prefix input SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; 84 oriented exchange pairs SHA256: `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`.

## Exact proposition and proof

Fix a finite set of demand labels, four named legal roots, and a cache K. The native prefix-cover cost D^K_r(S) is monotone: S subset T implies D^K_r(S) <= D^K_r(T). For a full legal root assignment rho let Phi_K(rho)=sum_r D^K_r(S_r(rho)). Define the terminal observer at threshold B by F_B(K)={(rho,Phi_K(rho)): rho is legal and Phi_K(rho)<=B}.

**Terminal completeness lemma.** Deterministic DFS that processes all demand labels in any fixed permutation, branches over every legal root, and cuts a partial assignment precisely when its rooted cost sum exceeds B, visits exactly the assignments in F_B(K) as uncut depth-|labels| leaves.

**Proof.** Each full assignment's partial-label sets are subsets of its final root-label sets. By rooted-cost monotonicity, every prefix on a full assignment of cost <=B has cost <=B; all its ancestors and the leaf are visited. Conversely each uncut complete leaf is legal and its cost <=B. Each demand is assigned once, so the same full assignment cannot arise twice. QED.

**Finite census theorem (B=155).** Rebuilding exact integer signed-prefix trie DPs for 51 configurations and performing the specified 84-edge comparison establishes F_155(a)=F_155(b) **with the full assignment-to-cost mapping** on every exchange edge. The 84-edge graph has five connected components; exact equality propagates to every pair within a component by transitivity. The five component terminal observers are pairwise different.

| Component representative | Cache configurations | Exact feasible leaves | Complete cost histogram |
|---|---:|---:|---|
| 32264 | 41 | 3 | 154:1; 155:2 |
| 32276 | 3 | 12 | 152:1; 153:3; 154:4; 155:4 |
| 32691 | 3 | 11 | 152:1; 153:3; 154:3; 155:4 |
| 32275 | 2 | 36 | 144:1,145:2,146:2,147:4,148:3,149:3,150:4,151:2,152:3,153:4,154:3,155:5 |
| 32689 | 2 | 36 | 144:1,145:2,146:2,147:3,148:3,149:5,150:2,151:4,152:1,153:5,154:3,155:5 |

All 336 complete terminal certificates are reproducibly emitted by the attached C++ verifier as `FOI_TERMINAL_CERTIFICATES_51.csv`. Each certificate records case ID, four named-root bitmasks and exact integer terminal cost; the 84-row `FOI_CENSUS_84.csv` gives every edge result.

## Strict search-history residual: eight earliest divergence certificates

Full ordered DFS traces agree on 76 edges and differ on eight; in all eight the **first** distinguishing event is a different next-demand label at a shared unpruned prefix. The common prefix has exactly d+1 visited nodes, where d is first changed demand-order depth:

| Exchange edges | First changed depth d | Shared trace nodes | Visits | Changed eligibility labels | Full terminal observer |
|---|---:|---:|---|---:|---|
| 32315/32318 -> 32279 (2 edges) | 0 | 1 | 173 -> 436 | 2 | identical; costs 154,155,155 |
| 32315/32318 -> 32292/32293 (4) | 3 | 4 | 173 -> 182 | 0 | identical; costs 154,155,155 |
| 32315/32318 -> 32324 (2) | 7 | 8 | 173 -> 173 | 0 | identical; costs 154,155,155 |

In the first pair, 9 later source-trace cutoff flags differ. In the middle four, there is no source-trace cutoff flip. In the final two, visited internal assignment-mask sets differ while total visit counts (173), cutoff-mask sets and complete terminal cost maps remain identical. This is a concrete observer-dependent residual: the terminal assignment-cost readout is invariant, although the ordered partial-state exploration carries additional information.

Of the 76 edges with identical full traces, 44 have changed intermediate rooted lower bounds (431 changed source-prefix evaluations in total). Exact trace equality therefore also admits variation in partial numerical lower bounds.

## Validation, scope, and next problem

The standalone C++17 verification source starts from the frozen 94-key native signed-prefix file, caches 168 distinct rooted signature profiles, builds all 51 exact DFS traces, compares all 84 full terminal assignment-cost maps, and can emit all 336 terminal certificates. `-O2` and `-O3` produced byte-identical 84-row results. A separate independent Python trie-DP implementation directly reconstructed all **eight** trace-changing edges, their first divergence positions, full feasible assignment/cost maps and root eligibility. Computations use exact integer arithmetic. Complete source inputs, 336 certificates, 84-row result table, both executed implementations and logs are preserved in the evidence bundle.

The census concerns the exact frozen four-root, 24-label model, B=155 and 84 specified exchanges. It addresses full assignment costs up to 155, not all assignments beyond the cutoff. Author checked; **NOT_REVIEWED**.

**Next:** derive a cache-key-local sufficient condition for preserving F_B using changed signed-prefix paths, avoiding full target-root DP reconstruction. Within the 41-configuration class, explain when perturbations remain invisible to the terminal observer but change the earliest DFS decision at depths 0, 3 or 7.

**Shared-state provenance:** existing Researcher-ID `EM-DIRECT-204C14`, Activity `RA-6893088D0A7347CE7F4D8720`. The last exact `RS-EC49AS` task query found no formal publication directory. This research note is not a formal CLAIM, Result or reviewed promotion.
