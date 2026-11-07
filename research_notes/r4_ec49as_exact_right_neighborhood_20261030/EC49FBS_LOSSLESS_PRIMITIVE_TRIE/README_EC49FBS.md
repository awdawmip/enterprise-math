# EC49FBS — lossless signed-X6 primitive-prefix trie compression

Date: 2026-11-05. Research level: author-side **exact combinatorial theorem** with finite integer verification. Frozen science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Predecessor EC49FBR commit: 23c63afc9f878514cbd9b1637b844aa0e0db0745.

## Theorem: exact native-prefix cost

Use the frozen signed-native primitive-step operation code:

| operation | native signed steps | length |
|---|---|---:|
| a | (-1,-1) | 2 |
| c | (1,2,-1,-2) | 4 |
| d | (2,1,-2,-1) | 4 |
| e | (3,1,1,-3) | 4 |
| f | (1,-1) | 2 |
| g | (2,-2) | 2 |

For **every finite** set W of operation words over Σ={a,c,d,e,f,g}, let P(W) be the set of all nonempty primitive-step prefixes of native expansions of words in W, retaining the full ordered signed-axis steps. Let U(W) include the empty root and every *complete operation* prefix of words in W. At each u, A(u) denotes the set of immediately following operation letters. Set I_cf(u)=1 iff both c and f belong to A(u), otherwise 0, and define I_dg analogously.

**Exact primitive-prefix union identity:**

\[
\boxed{|P(W)|=\sum_{u\in U(W)}\left(\sum_{s\in A(u)}\ell(s)-I_{cf}(u)-I_{dg}(u)\right).}
\]

The formula counts primitive prefixes ending inside a four-step operation and is valid for any finite W, irrespective of its observer, cache-key and horizon restrictions.

**Proof.** The ordered pairs consisting of the first two primitive signed steps of the six operation codes are respectively (-1,-1), (1,2), (2,1), (3,1), (1,-1), and (2,-2). All are different, hence the set of six codewords is prefix-free and every valid concatenation has a unique left-to-right parsing. Prefix descendants arising at different complete operation-prefix nodes are therefore distinct. At one such node, different outgoing codewords can share an initial primitive edge only when their first signed steps coincide. Exactly the pairs (c,f) and (d,g) have this property. In each pair their second signed steps differ, so they share exactly **one** primitive edge. All other outgoing branches are disjoint. Sum the full lengths of outgoing operation codes at every complete operation-prefix node and subtract these exact single-edge duplicates. This counts every primitive edge once and proves the identity. QED.

For W={c,f}, the naive weighted operation-edge sum is 4+2=6, while the primitive union size is 5, because c and f share the first native +1 step. The identity preserves this difference exactly.

## Exact compressed 0–1 model

For a trie of all permitted operation words, use a binary x_(u,s) for each operation-prefix edge and a binary y_(u,cf) or y_(u,dg) wherever the corresponding pair exists. Use the original observer terminal-coverage clauses and parent activation constraints. Enforce the Boolean AND identity y=x1 AND x2 with y<=x1, y<=x2, and y>=x1+x2-1. Minimize:

\[
\sum_{(u,s)}\ell(s)x_{u,s}-\sum_{u}y_{u,cf}-\sum_{u}y_{u,dg}.
\]

Every selected terminal set has exactly the same objective value as its full signed-native primitive prefix union, by the theorem. A feasible closed trie with terminal coverage corresponds to a legal set of terminal witnesses; extra edges can be dropped without raising cost. Therefore this reduced integer formulation has the **same optimum** as the original primitive-edge formulation for any fixed candidate family. The compressed MILP itself has not yet been executed; this is a proved formulation for the next solve.

## Executed verification

The executable verifier VERIFY_EC49FBS.js recomputes direct native signed-prefix unions and the separate weighted operation-prefix formula, then asserts equality. It enumerates candidates with the frozen EC49FBR nine-state observer and exact operation-count identities. The candidate family has fixed H2={fe,ge}, H3={feg,gef}, L=(4,2,1) in H4/H5, M=(7,3,2) in H6–H9.

| Set | weighted op-edge cost | c/f discount | d/g discount | primitive union |
|---|---:|---:|---:|---:|
| EC49FBR M=(6,4,1), 24-word witness | 124 | 4 | 4 | **116** |
| EC49FBR M=(7,3,2), 24-word witness | 178 | 5 | 7 | **166** |
| Union of all 16,156 candidate words including four frozen roots | 114,378 | 2,203 | 2,203 | **109,972** |

The complete candidate union has 25,359 operation-prefix nodes and 41,438 operation edges. Adding 4,406 potential overlap binary variables gives **45,844** binary cost variables, versus **109,972** primitive-edge variables. The exact reduction is **64,128 variables (58.31%)** for this candidate family; coverage and parent constraints are separate. This is a representation size comparison, not a measured solver-speed result and not the union cost of a selected legal solution.

The actual V8 execution checked 16,156 singleton candidate sets and **all 18,336 unordered pairs** among the 192 accepted words at H4(L), H5(L) and H6(M), with zero mismatches. The theorem is proved generally; the finite checks independently audit the implementation. EXACT_REPORT_EC49FBS.json contains the numerical run summary.

## Next research unit EC49FBT

Use the exact compressed MILP to release the EC49FBQ six-word H8/H9 pin for L=(4,2,1), M=(7,3,2) and optimize all H4–H9 clauses jointly. Retain the frozen primitive science and the signed-native cost objective. Extract an explicit H2–H9 witness and verify it with the independent direct primitive-prefix checker; compare its cost with the conditional fixed-late 166 and the mother benchmark E<=93. A bounded incumbent or a certified local cutset is independently useful if a complete solve is costly.

Provenance: EC49FBR source VERIFY_EC49FBR.py and its independent explicit-witness certificate EXACT_REPORT_EC49FBR.json. This note's computations use identical primitive-operation vectors, count identities and frozen observer. No classical physics computation or native-to-continuous substitution is introduced.
