# EC49FZU — Forced-hole row domination and conditioned saturated certificates

2026-11-25. Parent EC49FZT @ b6c9d3593cc6aeaad8e01a3a60cac80b405c4802:research_notes/portable_direct/EC49FZT_FIXED_QUERY_RESIDUAL_CERTIFICATE.md. Frozen BRC16943, 10 rows, m=25, h=14, fourth-level budget 15. Verified parent local reproduction SHA256SUMS; fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923. Topic r4-20261125-1727-ec49as-read SUCCEEDED at 5906a4e763dca22078236b0ade6fd24b7d00589d, NO_CANONICAL_PUBLICATION_DIRECTORY; no native owner projection. Historical researcher EM-DIRECT-23537B; current private binding unconfirmed, independent portable derivation; no shared CLAIM, Result or Review. P000 unchanged.

## New theorem: eliminate optional forced-hole features using historical zero witnesses

Let a genuine physical AND-query history with common positive anchor (r0,j0) give the state family x=(U,H), W(r,j)=1_{r in U}1_{j notin H}, |H|<=h. Let C be columns not fixed normal by a positive observation (including the anchor); D_j the rows tested negative in column j. For a compatible support V let B_V={j in C:D_j intersects V}; its fiber is B_V subset K subset C, |K|<=h. A support contradicting any positive row/column or with |B_V|>h is absent. A saturated fiber can equivalently be represented with upper bound B_V. A target x has forced holes B=B_U, free missing holes O=H minus B.

For every j in B, choose s_j in D_j intersect U. The row feature (s_j,j0) dominates the missing-column feature (r0,j): a rival (V,K) with j notin K must have s_j notin V, otherwise it contradicts the earlier zero. Thus every rival excluded by the missing-column feature is also excluded by the positive row feature. This argument needs a real historical zero witness, not just an arbitrary interval lower bound.

Under FZT's exact feature cost c_x(T,S)=|T minus U|+|S intersect H|+max(|T intersect U|,|S minus H|), replace any selected forced hole j by s_j. The negative-column cost drops by one; the positive-row term increases by at most one. Coverage only grows. Repeated replacement eliminates ALL optional forced-hole features without increasing cost. This is an exact optimal-certificate reduction, not a deletion of physical observations from the adaptive search. It also applies to unsaturated targets, though their free-column obligations remain.

For saturated |H|=h every O feature is mandatory (rival (U,H minus {j}) for each j in O). For V != U with |B_V union O|<=h define R_V=U xor V and L_V=B_V minus H. The remaining rivals for V are excluded iff T intersects R_V or P intersects L_V, where P is a chosen normal-column set. Proof: if neither condition holds, K=B_V union O is a genuine surviving rival: O subset C, B_V subset C, K avoids P, and |K|<=h. If either condition holds the row or forced normal-column discrepancy eliminates the entire fiber. If |B_V union O|>h, O alone eliminates the fiber. For U, observing O and saturation plus forced B imply K=H. Therefore
  C_sat(U,H)=|O| + min_T [ |T minus U|+max(|T intersect U|, tau(Q minus r(T))) ],
where Q indexes V with |B_V union O|<=h, V!=U; r(T) covers clauses by row differences, and tau(E) is the FZO exact normal-column set cover on residual clauses E, with tau(empty)=0 and infinity if impossible. The original FZO optional-hole subset J need not be enumerated on genuine histories. For h=14, this removes the full 2^|B| optional-hole enumeration (up to 16384 candidate subsets), not a proven overall runtime speedup.

## Exact first-query contraction

Condition on actual target answer q=(r,j). For yes retain V containing r with j notin B_V, remove j from common potential C. For no, on V containing r force j into B_V (drop if j was not allowed or capacity exceeded); V not containing r is unchanged. Retain original positive anchor. Normalize saturated upper bounds after the transition. The child remains a genuine history, so the forced-hole domination theorem applies again, including a newly forced j with witness r. For a saturated target the exact fixed-first cost is 1+C_sat(child;x) by FZT. Do not replace q by a marginal feature before conditioning; this preserves its joint effect. The cost optimizer may compress after conditioning only. This formula provides exact necessary candidate-first-query tests but not a sufficient adaptive-depth test.

## Evidence and reproducibility

Ran forced_hole.py on 120 seeded small genuine histories (3x4 h=2 and 4x5 h=3; RNG 16943), up to two saturated targets each, all physical first queries. Independent exhaustive physical-query cover DP agrees with new optimizer on 3772 fixed-first comparisons; explicit fiber equality and uniqueness also asserted. On frozen fourth.json sample roots 0,31,...,2387 (78 roots), one deterministic saturated target per root, original FZO optimizer agrees on all 78 unconditioned costs. Four seeded physical first queries per root: 312 exact child-fiber equality and certificate replays, 277451 explicit child states compared. Fixed-first costs minus unconstrained costs: 0 in 50, 1 in 262. No assertion failures. Frozen child tests establish exact child recovery by theorem and replay; independent brute optimality is on small models, and original FZO equality on 78 roots only. New oracle is standalone, not integrated into adaptive C++ solver. Full raw u_cert.csv SHA256 a3e410aad4097966cd94420fb5f9002e0174735e488a2a9a965c5b88adca3230 (14483 bytes); actual code SHA256 3105a1b3d230055c3e44d4d5bce9e7699b1746771d03dfde506de9fc28051233 (4775 bytes); local reproduction archive retains both and existing frozen input.

## Independent continued fourth-level classification

Used unchanged parent tight.cpp, g++ -O3 -std=c++17. In retry_t.py append t.csv to file list, assert 521 remaining, then python retry_u.py 0 18 300000 > u.in and feed tight. Process timed out after six complete rows, remaining twelve not counted. All 3 YES replayed (4187 physical-label states). 2 NO crosschecked using unmodified union.cpp at cap 350000 on precisely those roots. Raw complete rows (root,n,status,calls,envelopePrunes):
```csv
1529,1237,1,218226,1273
1773,1451,0,300001,9108
1782,1458,1,106966,1289
1787,1462,-1,103744,2340
1809,1491,-1,246520,1215
1810,1492,1,114211,744
```
NO crosscheck:
```csv
1787,1462,-1,104990,3584
1809,1491,-1,247476,2171
```
1089668 calls on completed rows only. 3 new YES, 2 new NO, 1 still open; 12 unfinished planned inputs remain open. Totals 1857 YES, 20 NO, 516 open of 2393. Ordered totals 3744 YES, 37 NO, 914 open of 4695. 25<=M14<=27 remains. Preserve all previously decided roots. Next: implement reduced saturation oracle in low-budget adaptive nodes, compare with unchanged tight.cpp; process remaining 516 open. No speed claim. AUTHOR_PROVED / EXACT_FINITE_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
