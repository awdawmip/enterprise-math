# EC49FNZ — Exact residual-label obstruction graph and disjoint-root two-label forcing

Date: 2026-11-14. Mode: **author-proved exact finite / NOT_REVIEWED**, independent scientific research note (not a formal Task Result or CLAIM).

## Scope and frozen evidence

Continue EC49FNY [PR #2343](https://github.com/awdawmip/enterprise-math/pull/2343) at immutable commit `635225c8dbc3b5861bd79419037a1af977742b78`; preserve science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The 94 cache keys, 178,850 native signed ordered-prefix words, 24 distinguishable demands, 4 rooted microsteps (03/05/06/07), and nine exact target-32279 residual cuts are unchanged. We **did not rerun the global 24-demand optimization**.

Read exact original data as `master_and_radius3_cases.txt` (SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`) and `EC49FNY_CERT_ALL.txt` (SHA256 `708da9a677ecf1d7842daf732ea51c796262a2974ef3476c9ef34f2f4107b271`), available in the FNY original archive. The previous independent Python root-cover trie DP is the basis of the new enumerator, not any saved C++ DP table.

## General lemma: exact two-label root-choice matrix

Let `p` be a lawful partial assignment, `S_r` its assigned demands at root `r`, and `D_r(S)` the exact minimum native rooted prefix-cover cost. Set `L=Σ_r D_r(S_r)`. For two unassigned distinguishable demands `i,j`, let `R_i,R_j` denote their lawful roots. Define

`α_i(r)=D_r(S_r∪{i})-D_r(S_r)`; `a_i=min_{r∈R_i} α_i(r)`, and similarly for `j`. For common roots define `β_ij(r)=D_r(S_r∪{i,j})-D_r(S_r)`.

Then the exact two-demand lower bound is

`H_{i,j}=L+min( min_{r∈R_i,s∈R_j,r≠s}(α_i(r)+α_j(s)), min_{r∈R_i∩R_j} β_ij(r))`,

with an empty minimum taken as +infinity. This is an **identity**, not an independence approximation: different-root allocations contribute independent root-cover costs, whereas same-root allocations use the joint rooted DP.

**Disjoint-minimizer criterion.** If the individual minima `a_i,a_j` can be attained on *different* roots, and every common-root joint increment satisfies `β_ij(r)≥a_i+a_j`, then `H_{i,j}=L+a_i+a_j`. Proof: each distinct-root assignment is at least `a_i+a_j`, and one attains it; every same-root option is no cheaper by the hypothesis. Consequently, if `L+a_i≤B`, `L+a_j≤B`, but `L+a_i+a_j>B`, the pair is a **strictly irreducible two-label forcing certificate**. No assumption of global submodularity of the rooted set-cover cost is made.

Every complete lawful assignment extending `p` induces one of these pair placements. Root-cover monotonicity shows its full cost ≥ `H_{i,j}`, so `H_{i,j}>B` excludes the entire extension tree.

## Exact finite census and correction of horizon semantics

The previous nine unique witness patterns have unassigned-demand counts `[1,1,2,2,2,2,2,3,3]`: **two with one label, five with two, two with three**. Thus, across all nine patterns, only **11** distinct unassigned-demand pairs exist, rather than an assumed 24-label search. All 11 pair bounds exceed the frozen threshold `B=155`; two pairs, one at each of the following patterns, are **irreducible** (neither singleton bound exceeds 155).

**Important semantic refinement of EC49FNY:** the prior C++ verifier computes `h=min(requested_h, number_of_unassigned_labels)`. Its reported `H2` on the two one-label patterns is in fact **H1**, not a mathematically defined size-two maximum. The accurate uniform assertion is `H_{min(2,|U|)} > 155` for all nine patterns. This correction preserves the branch-exclusion result but avoids assigning a nonexistent two-label witness to a single-label cut. Across the original 18 directional cuts, these nine patterns occur twice each: 4 one-label, 10 two-label, 4 three-label cuts.

| Encoded witness | L | |U| | H1 | H[min(2,|U|)] | #pairs | #irreducible |
|---|---:|---:|---:|---:|---:|---:|
| 159572696880793 | 155 | 3 | 159 | 162 | 3 | 0 |
| 159609271197337 | 155 | 2 | 158 | 161 | 1 | 0 |
| 159881934509721 | 155 | 1 | 159 | 159 (H1) | 0 | 0 |
| 159609271195289 | 152 | 2 | 155 | 158 | 1 | **1** |
| 159624303580825 | 153 | 2 | 156 | 159 | 1 | 0 |
| 160451084785305 | 154 | 1 | 157 | 157 (H1) | 0 | 0 |
| 159607123728025 | 155 | 2 | 158 | 161 | 1 | 0 |
| 159607123711641 | 150 | 2 | 153 | 156 | 1 | **1** |
| 159571690231449 | 153 | 3 | 161 | 164 | 3 | 0 |

All maximizing two-label pairs are subsets of `{17,19,21}`. There are exactly two genuine pair-only obstructions, **both on labels (19,21)**, not an arbitrary collection of many low-cost future demands.

### Exact common-root and distinct-root certificate

At witness `159609271195289`, `L=152`. Both singleton minima are `155` (increment 3); they occur at disjoint roots `19→07` and `21→06`. The pair minimum is `158=L+6`. The only shared legal roots are 03 and 07, where the exact *total* pair costs are 178 and 162, respectively. Hence all same-root alternatives exceed 158.

At witness `159607123711641`, `L=150`. Both singleton minima are `153` (increment 3), achieved at distinct roots `19→05`, `21→06`. The pair minimum is `156=L+6`; shared-root total costs at 03 and 07 are 176 and 166, respectively.

Thus the strict two-label effect here is **not caused by forcing both demands onto one root**. Distinct roots already require two simultaneous positive marginal costs. The exact 3×3 lawful-root matrices, including all alternatives, appear in the companion verification log.

## Reproduction and evidence limits

Run the companion Python verifier with exactly these two frozen files:
`python VERIFY_EC49FNZ_OBSTRUCTION_GRAPH.py master_and_radius3_cases.txt EC49FNY_CERT_ALL.txt`.
It reconstructs the rooted native prefix trie / subset DP from the raw frozen word file, enumerates the true lawful options for each *unassigned* label, checks every individual and every pair, and asserts the nine prior H1/H2 projections and the new counts. Output ends in `EC49FNZ_EXACT_CHECK_PASS patterns=9 singles=2 doubles=5 triples=2 pairs=11 forcing=11 irreducible=2`.

Reproduction scope: exactly nine target-32279 residual patterns, appearing in 18 directed cuts. No claim concerning all stable exchanges, non-stable edges, wall-clock speed, general complexity, formal proof-assistant verification, independent peer review, or native event publication is made. This result only uses the original frozen BRC signed-root-prefix words.

**Next frontier:** test whether the disjoint-minimizer/cheap-same-root criterion predicts horizon-one versus horizon-two in a genuinely earlier cut layer with >3 unassigned demands; then evaluate non-stable single-key neighbors to measure actual discriminating power. The previous exact finite base remains unchanged.
