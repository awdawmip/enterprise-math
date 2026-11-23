# EC49FYG — Exact residual-fibre quotient of the 600-state Farey–CRT observer

Date: 2026-11-24, Asia/Shanghai. Frozen scientific input: BRC16943. Independent informed portable continuation of [EC49FYF@ea53a40c](https://github.com/awdawmip/enterprise-math/blob/ea53a40cb4224812bf5218d34b038ccd7f9e0c05/research_notes/portable_direct/EC49FYF_S11_COLUMN_SYMMETRY_AND_HARD_PREFIX_PRUNING.md).
Evidence: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED. The result concerns the normalized P10/C11 auxiliary observer, not native X6 dynamics. Existing global bound: 14 <= Q <= 15. Historical Research-4 lineage: RA-0F8055ACDE0F5F6A97CA5D6D; no new authenticated owner or CLAIM is asserted.

## Model

Take the exact frozen family F of fifty nonempty 10-bit row-support masks, eleven physical columns J={0,...,10}, and 600 physical states S=F × ({-1} ∪ J). State (U,-1) is a complete factor; state (U,h) removes column h. A query (t,j), t=0,...,9, returns W_(U,z)(t,j) = 1[t∈U] 1[z≠j]. All queries are noiseless, and no reflection spectrum is supplied for free.

## Theorem 1: exact sufficient residual state

For a physically realizable transcript P of tested locations and their bits, let K⊆J be the distinct tested columns and k=|K|. Define

A(P)={U∈F : for every observed (t,j,b), b=1[t∈U]}

and for each h∈K,

B_h(P)={U∈F : for every observed (t,j,b), b=1[t∈U]1[h≠j]}.

Then the exact surviving PHYSICAL state set is the disjoint union

S_P = [A(P)×({-1} ∪ (J\K))] ⊔ [ ⊔_(h∈K) B_h(P)×{h} ],

hence

|S_P| = (12-k)|A(P)| + Σ_(h∈K)|B_h(P)|.

Proof. For z=-1 or an untested hole z∉K, all past readings equal 1[t∈U]; this is equivalent to U∈A(P). If z=h∈K, substituting directly into W makes compatibility equivalent to U∈B_h(P). The different z labels make the blocks disjoint, and exhaust all possible states. Counting proves the formula. □

The quotient preserves the multiplicity of each unseen-hole label and a reversible mapping to the physical output column. Thus it is lossless for subsequent adaptive observations and final output, not a conflation of distinct physical states.

## Theorem 2: exact row-bitset transitions

Use the verified full column-permutation symmetry of EC49FYF to rename seen columns 0,...,k-1 and the next fresh column k. Let R_t={U∈F:t∈U}; F_t^1=R_t, F_t^0=F\R_t. Let (A,B_0,...,B_(k-1)) be the exact current residual state.

If a test in an existing column j<k returns b:
- A' = A∩F_t^b;
- B'_j = B_j if b=0, and ∅ if b=1;
- B'_h = B_h∩F_t^b for all h≠j.
Here k is unchanged.

If a test in a fresh column j=k<11 returns b:
- A' = A∩F_t^b;
- B'_h = B_h∩F_t^b for all previously seen h<k;
- B'_k = A (the OLD A) if b=0, and ∅ if b=1.
Here k increases by one.

Proof. A state with the hole at the tested column always returns 0, regardless of its row mask. Every other state returns 1[t∈U]. At a fresh column, its newly separated hole cohort was precisely the old A family, so the zero branch retains old A in the new B_k. This derives both transition formulas exhaustively. □

## Exact minimax reduction

Let D(A;B_0,...,B_(k-1)) denote the minimum remaining worst-case number of queries. It is zero exactly when (12-k)|A|+Σ|B_h|=1. Otherwise,

D = 1 + min_(t∈{0,...,9},j∈{0,...,min(k,10)}; nontrivial split)
         max(D(T_(t,j,0)), D(T_(t,j,1))).

The children T use Theorem 2. The min considers existing columns and at most one new column, by the previous exact S_11 symmetry theorem. Omit tests with one empty outcome (they cannot improve any decision tree). Every retained child is a strict candidate-set reduction, so this finite recursion is well founded. Starting state: k=0, A=F, B=[].

This is an exact computational reformulation of the original Q; it does not claim the global minimum has been computed.

## Finite independent verification

The companion Node.js standard-library script uses 50-bit BigInt sets for A and B, while separately representing all 600 original candidate states in a 600-bit BigInt oracle filtered directly by W. All nonempty canonical-query histories through depth 3 are generated. On every transition, the compressed state's complete expansion is compared with the independent original-state oracle.

| Depth | Distinct compressed states | Seen-column counts |
|---:|---:|---|
| 0 | 1 | k=0: 1 |
| 1 | 20 | k=1: 20 |
| 2 | 555 | k=1: 200; k=2: 355 |
| 3 | 11,639 | k=1: 1,130; k=2: 5,119; k=3: 5,390 |

Exactly 28,614 nonempty child transitions and 12,215 reconstructed states were checked, all with exact integers. The finite check validates the implementation through depth 3; arbitrary-depth correctness rests on the direct proofs above.

## Next question and limits

Use the residual-fibre state to memoize an exact bounded-depth Bellman search, integrating the necessary 14-query hard-mask certificates for U=101,788,833 from EC49FYD/EC49FYF. Seek a complete depth-14 tree with leaf readback or a complete infeasibility certificate; until then, Q∈{14,15}. The 600-state observer's correspondence to native X6 dynamics remains a separate bridge.

Control at this turn: the exact topic RS-EC49AS has no canonical publication directory at Source e2cc0722726afd6bfae134cecdd900e67ac7f85d; the response explicitly does not establish full native owner authority. Research was therefore published only as a new independent portable note, without CLAIM/Result/Review or claiming to update the historical Activity.
