# EC49FYH — Exact seen-column multiset quotient of the Farey–CRT observer

Date: 2026-11-24 (Asia/Shanghai). Science pin: BRC16943.
Parent: [EC49FYG@b76275e1968a006005b16e96c9cb1c0f18b08bd6](https://github.com/awdawmip/enterprise-math/blob/b76275e1968a006005b16e96c9cb1c0f18b08bd6/research_notes/portable_direct/EC49FYG_EXACT_RESIDUAL_FIBRE_QUOTIENT_THEOREM.md).
Evidence class: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.
Scope: frozen 50-support, 11-column, 600-physical-state P10/C11 *auxiliary observer*, not an assertion about native X6 dynamics. A current authenticated Researcher/Activity writer is not asserted; Research-4 historical Activity provenance RA-0F8055ACDE0F5F6A97CA5D6D is retained without mutation.

## Model and previous lossless quotient

Let F be the frozen 50 nonempty masks U on 10 rows. Physical states are (U,z), where z=-1 indicates no missing column and z=0,...,10 indicates one missing column. A query (t,j), with t in 0,...,9 and j in 0,...,10, reads

    W_(U,z)(t,j) = 1[t in U] * 1[z != j].

For a transcript whose distinct probed columns are labeled 0,...,k-1, the previous EC49FYG theorem gives the exact candidate set

    S = (A x ({-1} union {k,...,10})) disjoint_union
        ((B_0 x {0}) union ... union (B_(k-1) x {k-1})),

with the exact physical candidate count

    |S| = (12-k)|A| + sum_{j<k}|B_j|.

Here A and each B_j are subsets of F, encoded by 50-bit integers. The original B-list is ordered by the order in which distinct columns were first probed.

## New theorem: unordered seen-hole fibres preserve minimax depth

**Theorem.** Fix any reachable residual tuple (k,A,B_0,...,B_(k-1)). Its optimal remaining worst-case adaptive identification cost depends only on k, A, and the **multiset** of B_j, including repetitions. In particular, the canonical key

    Q(k,A,B_0,...,B_(k-1)) =
      (k,A,sort_integer_ascending(B_0,...,B_(k-1)))

is lossless for *minimax computation*. The physical-column-to-canonical-slot permutation must be retained as a decoder when constructing a physically executable decision tree or naming a final hole.

**Proof.** Let π be an arbitrary permutation of the k already probed physical columns, extended to a permutation of all eleven columns by any bijection on the unprobed columns. Act on physical states by (U,-1)->(U,-1) and (U,z)->(U,π(z)), and on queries by (t,j)->(t,π(j)). By the exact observation definition, W_(U,π(z))(t,π(j))=W_(U,z)(t,j). Thus every adaptive decision tree on one candidate set transports, with the same answer bits, depth, and distinct physical-state leaf labels, to a tree on the permuted candidate set; the inverse permutation restores leaf labels. In the residual representation, A is unchanged and the B_j are permuted. Any two B-lists with the same multiset are related by such a π, so both optimal depths are equal. This proves the claim and also shows why dropping the output-label decoder would not be valid. □

For an **existing** seen column j, the EC49FYG transition updates that particular B_j by keeping it on a zero outcome or clearing it on a one outcome, and intersects all other B_h with the row test. Two occurrences of an equal B_j give identical *canonicalized* children after sorting. For a **fresh** column, EC49FYG appends old A on the zero branch or 0 on the one branch; this is likewise invariant under permutation of the existing list. Hence the canonicalized Bellman recursion can consider one representative of each *distinct* seen B value and at most one fresh-column action. Infeasible or deterministic queries are omitted exactly as in the parent.

A canonical state is not the full physical history: the output decoder and actual current column names are maintained alongside a chosen path when instantiating the winning tree. The multiplicity of equal B values is kept; merging equal B entries or treating unprobed column labels as one physical output would lose information.

## Exact verification

Companion script: EC49FYH_SORTED_FIBRE_ORBIT_VERIFY.py.
It independently filters all 600 *labeled* original states using exact 600-bit oracle bitsets for each query and reconstructs the complete candidate set from (k,A,B). It enumerates **all nonempty canonical query histories through depth 4**, retaining each distinct ordered residual state. It then groups them by the new sorted-multiset key. For depths 0 through 3, it also verifies that all ordered representatives of every orbit have the same complete set of nontrivial canonical child-pairs (both Boolean responses), after canonicalization. All arithmetic uses exact integers.

| Query-depth | Ordered residual states | Unordered seen-column orbits | Largest orbit |
| ---: | ---: | ---: | ---: |
| 0 | 1 | 1 | 1 |
| 1 | 20 | 20 | 1 |
| 2 | 555 | 410 | 2 |
| 3 | 11,639 | 5,443 | 6 |
| 4 | 185,224 | 45,888 | 24 |

Total exact candidate-oracle checks: **197,439**. Nonempty generated transitions through depth 4: **756,555**. Distinct orbit transition signatures cross-checked at depths 0–3: **5,874**. All assertions passed. At depth 4, the new quotient stores 45,888 rather than 185,224 canonical history states, a **4.0364x** reduction in distinct state count. This is a state-count reduction for the tested layers, not a measured runtime speedup and not a proof that the full depth-14 search will fit in memory.

The abstract theorem holds at arbitrary depth, because it is an exact group-action isomorphism. The finite numerical census is verified only through depth 4.

## Current frontier and next discriminating unit

The known global auxiliary-observer bound remains **14 <= Q_adaptive <= 15**, with a depth-15 construction and unresolved depth-14 feasibility. Replace EC49FYG's ordered B-vector memo keys by the exact new multiset keys, retaining a physical-label decoder for a successful tree. Combine with the hard-state 14-query certificate requirements for U=101, 788, 833. Then either exhibit a complete depth-14 tree with original 600-state leaf verification or provide an exhaustive infeasibility certificate. No global optimum, native X6 transfer, formal Result, or independent Review is asserted in this note.
