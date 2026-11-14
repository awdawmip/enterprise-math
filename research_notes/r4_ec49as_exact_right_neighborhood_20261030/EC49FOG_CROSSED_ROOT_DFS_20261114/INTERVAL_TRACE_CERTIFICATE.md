# EC49FOG refinement — One-trace interval certificate for 05/06 root-table changes

Fix the 24 labelled demands, four exact native signed-prefix rooted cover functions and cutoff B=155 of EC49FOG. The root03 and root07 cost tables and one DFS label ordering are fixed. Root05 and root06 independently choose either cache A=32279 or cache B=32315 cost table, each with the same root-specific label support in both caches.

For any visited partial root-assignment prefix p under the (05=A,06=A) baseline trace, define

```
C(p) = D_03(S_03) + D_07(S_07)
L(p) = C(p) + min(D_05^A(S_05),D_05^B(S_05))
             + min(D_06^A(S_06),D_06^B(S_06))
U(p) = C(p) + max(D_05^A(S_05),D_05^B(S_05))
             + max(D_06^A(S_06),D_06^B(S_06))
```

**Sufficient exact trace-transfer theorem.** If every baseline visited prefix p obeys `U(p) ≤ B` at a baseline-unpruned node and `L(p) > B` at a baseline cut node, then *all four* choices of the two varying root tables have identical ordered labelled DFS visitation and cut flags. Proof is induction on DFS depth and child order: the legal root-choice set is identical (same support at 05 and 06, fixed remaining roots). At every shared visited prefix the additive root bound for any choice is between L and U, so the cutoff Boolean matches. Hence the algorithm makes the same child expansions and visits the same successor prefixes in the same order, proving the claim. This directly preserves the declared DFS-trace observer, not the full rooted-cost table.

This test requires **one baseline DFS trace plus two exact rooted-cost lookups per varying root for each visited prefix**, in place of executing the other three DFS traversals. It is a sufficient certificate, not a proven speedup in elapsed time.

All eight choices of fixed (root03,root07,order) passed:

| 03 from B | 07 from B | order from B | visited | pruned | min(B-U) live | min(L-B) cut | changed-bound prefixes | max U-L |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0|0|0|436|275|0|1|0|0|
|0|0|1|397|235|0|1|13|4|
|0|1|0|418|263|0|1|0|0|
|0|1|1|361|211|0|1|13|4|
|1|0|0|259|149|0|1|0|0|
|1|0|1|206|121|0|1|7|4|
|1|1|0|245|141|0|1|0|0|
|1|1|1|173|99|0|1|7|4|

Thus 05/06 rooted DP arrays genuinely change at 308 and 3 masks, while their changes are precisely invisible to the **B=155 two-priority DFS-cut trace** under these interval certificates. The maximal interval width is 4; all pruned nodes have at least one integer cost unit of positive safety margin, and all uncut nodes remain at or below 155.

The independently reconstructed signed-prefix Python verifier `VERIFY_EC49FOG_INTERVAL.py` computes this certificate using the frozen master input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, importing the original `VERIFY_EC49FNY_INDEPENDENT.py` from PR #2375. The conclusion uses the same frozen scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Author-verified finite scope; NOT_REVIEWED.

**Next:** derive cheaper structural sufficient bounds on L and U from root-key differences without rebuilding the full rooted DP, then test these transfers on the remaining neutral edges with changed native workload.
