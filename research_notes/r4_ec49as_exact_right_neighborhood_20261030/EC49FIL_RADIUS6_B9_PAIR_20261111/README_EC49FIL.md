# EC49FIL — Complete B=9 two-demand screen for B-witness six-path BRC neighborhoods (2026-11-11)

**Frozen scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; original nine-state BRC observer, 178850 legal words, signed ordered native-X6 prefixes and seven raw complete cache keys. Original 94-prefix witness B is read from the pinned EC49FGW/EC49FGJ sibling source. This extends EC49FIK's exact pairwise screen to the **previously unverified B-witness budget 9 class**; it reuses the same algorithmic method, and is a finite enumerative result rather than a novel algorithm claim.

## Exact domain, predicate, and result

Let Q be a six-label subset of the original 24 distinct observation demands such that (i) Q contains no H2 demand; (ii) the unchanged 18 witness paths retain all seven original complete keys; (iii) |F(Q)|=84, so the 93-prefix target leaves B(Q)=9 new prefixes. These conditions identify **8700** Q.

For a replacement candidate w of label j with one of these seven full raw keys, let D_Q(w)=P(w)\F(Q) be the set of its nonempty ordered signed-X6 prefixes not already fixed. Every six-path completion of total cost <=93 must supply, for *every* pair j,k in Q, legal candidates u,v with |D_Q(u) union D_Q(v)|<=9. The checker computes every admissible candidate difference set, removes supersets (sound under union), and tests all pairs. If a pair has no feasible candidate union, the six-path completion is impossible.

| B witness, B(Q)=9 | Count |
| --- | ---: |
| Exhaustively enumerated Q | 8,700 |
| Single-demand passes | 8,700 |
| Additional pairwise impossibilities | **8,568** |
| Pairwise survivors (six-way feasibility not yet decided) | **132** |

The first failed-pair histogram is eight pairs with 934 cases each and four pairs with 274 each; the full ordered surviving Q list is in the encoded JSON artifact. The exact B=9 counts coincide with EC49FIK's already verified A-witness B=9 counts.

**Consequence:** Updating the disjoint EC49FIK B-witness unresolved count from 32,691 to **24,123**; fixed-seven-key unresolved from 30,679 to **22,111**, and released-key 2,012 unchanged. These counts are relative to the precise EC49FIJ+EC49FIK screens, not a global minimum proof.

## Reproduction / validation

From the repository's containing research_notes directory, run:
`python EC49FIL_RADIUS6_B9_PAIR_20261111/VERIFY_EC49FIL.py`

The program imports `EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py` and its witness JSON. It runs the original exact catalog generator and signed-prefix classifier. Local observed output: `all=8700, singleton_pass=8700, pair_reject=8568, pair_pass=132`; elapsed 14.291 seconds, Python process peak RSS 327180 KiB on the local executor. No timing-performance claim follows beyond that run.

The full 10,087-byte JSON report (including all 132 surviving six-position sets, bad-pair counts and resources) is stored losslessly as `EXACT_REPORT_EC49FIL.json.gz.b64`: `base64 -d ... | gzip -dc > EXACT_REPORT_EC49FIL.json`. Original uncompressed SHA256: `2ec5df55cae0bba6a7efa08824d7ebf46c386fdc959260e71da4fe58cecdee90`. Local executed script SHA256: `986b7a6f176f3887bc503cfa9b4b734257d2532652eee56068276824a46d650d`. All paths, source witness versions, observation model and complete-key semantics remain frozen.

## Next discriminating unit

Take the 132 B=9 pairwise survivors: check exact six-way union minimum by the native-prefix-tree DP (key set fixed), then advance B=11 pair screening. Separately retain the 2,012 released-key positions for explicit cache-key allocation. The mother question remains whether seven raw keys can realize at most 93 original native prefixes; no formal Result or independent Driver acceptance is asserted here.
