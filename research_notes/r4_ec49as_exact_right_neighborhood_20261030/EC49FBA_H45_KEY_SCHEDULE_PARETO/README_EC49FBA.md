# EC49FBA — Exact H4/H5 key-schedule Pareto and H9 budget obstruction

Date: 2026-11-05 Asia/Shanghai. Status: AUTHOR_EXACT_FINITE_DP_CHECKED, INDEPENDENT_PYTHON_AND_MILP_CROSSCHECK, UNREVIEWED, NOT_ADMITTED.

Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Extends EC49FAV and EC49FAZ (read frontier `cb57aa91ce3aecdf59959ae346feaa007ebcef95`). The exact codeword model is the signed native X6 primitive expansion:
`a=(-1,-1)`, `c=(+1,+2,-1,-2)`, `d=(+2,+1,-2,-1)`, `e=(+3,+1,+1,-3)`, `f=(+1,-1)`, `g=(+2,-2)`.
A complete six-axis cache key counts **positive occurrences** of each primitive axis; terminal displacement is `(+2,0,0,0,0,0)`. Never discard primitive-step order or prefix identity.

## Exact finite theorem

Fix H2=`{fe,ge}`, H3=`{feg,gef}` (16 distinct signed primitive-prefix edges and three distinct complete cache keys). At H4 and H5 select arbitrary finite subsets of legal operation words, respectively of lengths 4 and 5, such that each window uses exactly one complete cache key (the two horizon keys may coincide). At both windows the union of allowed six observer signatures must have nine-history rational rank 9. Measure cost as the number of distinct signed primitive-prefix edges in H2–H5.

**The exact minimum is 24 edges.** There are exactly four attaining ordered key schedules, with (H4 key; H5 key):
`(3,2,1);(3,3,1)`, `(3,2,1);(4,2,1)`, `(4,1,1);(4,2,1)`, `(4,1,1);(5,1,1)`, each with trailing `0,0,0` coordinates. For example:
`H4={fegg,gefg}`, `H5={feggg,gefgg}` under the first key schedule. The two H4 and two H5 terminal paths each provide observer signatures F and G, hence rank 9. Independent literal prefix-union recount is 24.

There are **9** individually rank-nine-capable H4 keys and **17** H5 keys. All **153** ordered schedules are exhaustively evaluated with exact signed-prefix min-plus/OR dynamic programming. For an identical H4/H5 key the seven feasible schedules have minimum **38 edges**, attained by `K4=K5=(4,2,1,0,0,0)` with witnesses `H4={fegc,fegd,gefc,gefd}`, `H5={feggf,gefgf}` (the EC49FAZ early configuration).

## Key-budget consequence for the nine-window mother question

For a fixed complete key `K=(x,y,z,0,0,0)`, valid length-h words have `#c+#d=x+y-h-1 >= 0`; hence a key used at H9 must satisfy `x+y>=10`. Every rank-nine-capable H4 key in the finite census has `x+y<10`; the unique rank-nine-capable H5 key satisfying `x+y>=10` is `(6,4,1,0,0,0)`.

The fixed H2/H3 scheme already consumes three keys. If H4 and H5 use one key each, any extension to H9 with at most five complete keys must satisfy **either `K4=K5` or `K5=(6,4,1,0,0,0)`**. This is a necessary budget condition, not a sufficiency or an H6–H8 existence claim.

Exactly **16** of the 153 schedules satisfy that necessary condition; the best H2–H5 cost among them is **38 edges**. If H5 uses the H9-compatible key, the best early cost across all nine candidate H4 keys is **90 edges**, attained by `K4=(5,3,1)`, `K5=(6,4,1)`. Thus the attractive 24-edge local optima cannot be extended under this fixed H2/H3, one-key-per-H4/H5, five-total-key configuration: their two new keys are distinct and neither reaches H9.

## Algorithm and proof completeness

Enumerate all `6^4+6^5=9072` raw operation words using `a,c,d,e,f,g`; compute the native signed primitive steps, complete positive-step six-key, signed six-axis endpoint and frozen EC49FAX nine-state observer. Retain only endpoint `(+2,0,0,0,0,0)` and one of the six allowed signatures. Group by window and exact key. A key is individually eligible when its signature OR mask satisfies EC49FAR's four-clause rank-nine criterion `(E|F)&(C|F)&(D|G)&(J|G)`.

For each of the 153 schedules, put all eligible words into one **signed primitive-prefix trie**; mark the fixed H2/H3 prefixes free. At trie node v, `D_v[m]` is the minimum additional edge cost for a terminal-word selection whose two-window, 12-bit signature OR mask equals m. Initialize mask 0 at cost 0; terminal signatures enter at cost 0. Merge each child with `D_new[a OR b] = min(D_new[a OR b], D_old[a]+D_child[b])`; charge one for each selected non-free incoming native edge. Structural induction on the trie gives an exact bijection between reachable masks/costs and candidate prefix unions. Minimize over the two rank-nine window masks. This is an **exact exhaustive finite optimization** of the declared one-key-per-window domain.

`VERIFY_EC49FBA.js` was executed with Node.js v22.16.0; a separately implemented Python integer prefix-trie DP checked all 153 ordered schedule costs exactly. For three contrasting schedules (24, 38, 90 edges), independent 0/1 SciPy-HiGHS prefix-edge MILPs returned status optimal and gap 0; the integer DP is the mathematical finite certificate. The full list of 153 costs, explicit witnesses and cross-check are in the attached JSON files. Run: `node VERIFY_EC49FBA.js > EXACT_REPORT_EC49FBA.json`.

A fresh comparison of EC49FAZ's signed-primitive key function is warranted when reproducing archived versions: the valid cache key counts positive steps, not absolute occurrences. The locally re-executed positive-step version matched the published EC49FAZ 112-edge report (26,705 trie nodes, 21,972,032 merges). This statement concerns the exact locally inspected variants; later repository readback was consistent with the positive-step implementation.

## Open research unit

The 38-edge best early same-key schedule preserves one unused fifth key; EC49FAZ's fixed late schedule gives 112 total, and its extension was separately optimized in EC49FAZ. The immediate next useful unit is to **permit multiple cache keys within H4/H5**, or optimize the second late key across all H6–H9 to search for an `E<=93` explicit construction. Retain the global author's existing interval `80 <= E*_{H9} <= 94`; the present 24/38/90 results are exact for the stated fixed H2/H3, one-key-per-window family. Preserve P000, ACTIVE worldview, source pin and independent Driver admission.
