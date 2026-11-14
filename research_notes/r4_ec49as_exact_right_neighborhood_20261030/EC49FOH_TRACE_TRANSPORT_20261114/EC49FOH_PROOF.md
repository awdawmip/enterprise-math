# EC49FOH — Single-trace transport certificates across 84 neutral BRC cache exchanges

**Frozen science:** task pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; original signed-prefix input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; frozen 84-edge list SHA256 `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`. Exact integer model; **author-verified finite research / NOT_REVIEWED**.

## Theorem: transport full DFS traces using only a source trace

The four native roots are 03,05,06,07; demand labels are 0..23. Each seven-key cache K determines exact ordered signed-prefix cover costs `D^K_r(S)`, admissible roots `E^K(l)` in root order, and the deterministic demand priority `o_K`: increasing admissible-root count, decreasing minimum singleton root cost, then increasing label. On a visited prefix p=(S_03,S_05,S_06,S_07) of depth d, let `LB_K(p)=sum_r D^K_r(S_r)` and `cut_K(p)=[LB_K(p)>155]`. Non-cut internal nodes visit children for the next demand `o_K[d]`, in the prescribed root order.

**One-trajectory transport theorem.** Given A's complete ordered visited-node trace T_A, suppose for *each visited p in T_A*: (i) `cut_B(p)=cut_A(p)`; (ii) for each A-non-cut internal p at depth d, `o_B[d]=o_A[d]` and the ordered admissible root lists `E^B(o_B[d])=E^A(o_A[d])`. Then B and A have exactly the same ordered labelled DFS visit trace and cut flags. B's complete DFS need not be run to certify equality.

**Proof.** The root prefix is identical. Inductively, identical visited prefixes have the same cut status by (i). If not cut, (ii) gives the same next demand and same ordered child roots. Their child assignment masks coincide, so the entire finite recursion (through depth 24) has identical ordered visits and cuts. Any earlier source branch illegal in B causes (ii) to fail at its parent, preventing a vacuous certificate. Failure of this sufficient test does not itself prove unequal visit counts.

## Exact finite census and evidence

An exact C++17 signed-prefix trie DP reconstructs all rooted cost functions for the 51 distinct configurations in the original **84 neutral exchange edges** (168 distinct computed root-signature profiles). For every edge with its original orientation, it evaluates the B cut and branching decisions solely on A's visited prefixes. It then runs the complete B DFS *only as a separate comparison check* and compares all ordered labelled root-assignment masks, depths, and cut flags.

| Verified observer | Exact count |
|---|---:|
| Neutral exchange edges tested | 84 |
| Certified identical full ordered DFS traces | **76** |
| Different full ordered DFS traces | **8** |
| False-positive certificates | **0** |
| Certified edges with changed source-visited lower bounds | **44** |
| Source-prefix comparisons, all edges | 14,877 |
| Source-prefix comparisons, certified edges | 13,493 |
| Changed source-prefix costs within certified edges | 431 |
| Largest absolute changed cost on certified edges | 2 |

The **eight differing edges** are:
- `32315→32279`, `32318→32279`: 173→436 visited nodes, each with 9 source-prefix cutoff sign flips;
- `32315→32292`, `32315→32293`, `32318→32292`, `32318→32293`: 173→182 visits; all source-prefix cut flags stay fixed, but branch priorities change;
- `32315→32324`, `32318→32324`: both 173→173 visits, yet *different ordered labelled traces*, starting from a differing next demand at depth 7.

In particular, visit-count equality is weaker than ordered-trace equality. In the other direction, even hundreds of changed lower-bound values can be decision-invisible: 431 altered values appear on the 76 certified edges without any change to a visited cut or branch.

The verifier asserts that every passed certificate implies direct equality of the two independently enumerated traces. C++17 `-O2` and `-O3` results were byte-identical. A separately implemented Python signed-prefix trie DP and DFS checker reconstructed five cache configurations and confirmed four representative edges:
`32315→32274` (173→173, 23 changed cost values but same trace);
`32315→32279` (9 cut flips, 71 branch mismatches);
`32315→32292` (0 cut flips, 53 branch mismatches);
`32315→32324` (173→173 with two changed branch points).

**Reproduce:** `g++ -std=c++17 -O2 VERIFY_EC49FOH.cpp -o verify_foh`, then `./verify_foh FIRST_NEUTRAL_EDGES_EC49FNS.txt < master_and_radius3_cases.txt > FOH_RESULTS.csv`. Inputs are preserved in the accompanying evidence bundle; the verifier consumes the original frozen 94-key, 178,850-word and 38,169-cache-set file. Full 84-row results and the independent Python checker are part of that bundle.

**Scope / next research question:** The theorem applies to the stated deterministic additive root-cost cutoff DFS. The 76/84 census is for this frozen input, B=155 and exact native priority; the method removes target DFS exploration when successful, but still requires B's rooted cost tables. Derive local lower/upper bounds directly from the exchanged key's ordered signed-prefix trie paths, eliminating full target root-table recalculation. Examine the eight divergent edges for minimal witnesses of reordered-but-equal-count trajectories.

**Prior contributions:** EC49FOF PR #2375, EC49FOG PR #2378, EC49FNS edge list. Existing researcher provenance `EM-DIRECT-204C14`, Activity `RA-6893088D0A7347CE7F4D8720`. Formal topic `RS-EC49AS` was last read as unpublished; this paper does not create a CLAIM or formal Result.
