# C266 — 8 new certified four-free pair hulls (author-level exact rational evidence)

**Status:** AUTHOR_EXACT_AUXILIARY, no native CLAIM, no Source Result, not independently Driver-admitted. This research handoff is not a theorem about native 6D GF(2)-BRC Cell geometry.

## Immutable inputs / scope
- Global knowledge: `GLOBAL_KNOWLEDGE_V1 main@7b33f8066e9993e7c941959a9d738ed405248eb8`
- Enterprise Math reference: `main@1da5fc197dab4e64dc27c97f298cb347475b2e6f`
- Complete inherited C265 parent ZIP SHA256: `dcf541ec1158d872eec5559548296197908e496da209a539f172955cbc73ff31`
- Input: the same 79 strictly ordered rational nodes as C265, explicit NUM/DEN in the independent compact checker; active indices (5,50,55,56); Q=2^128, H=2^166, Z=141421356237309504880/10^20, A=6912·50000²/17².
- Exact auxiliary function:
  `F(v) = Σ_{j∉I} B_j Π_{p∈I} (Z-v_p)/(Z-u_p) · |u_j-u_p|/|u_j-v_p| + Σ_{k∈I} QA/(H((2-v_k²)(3-v_k²))³) Π_{j∉I} (Z-u_j)/|v_k-u_j| Π_{p∈I\{k}} (Z-v_p)/|v_k-v_p|`;
  `B_j= floor(QA/[H((2-u_j²)(3-u_j²))³] Π_{r≠j}(Z-u_r)/|u_j-u_r|)>0`.

## Strict theorem

For every admissible real vector `v=(v5,v50,v55,v56)` in any of the six boxes below,

`F(v) >= 2^128 + 903503865712265886784690054399388 > 2^128`.

Every coordinate interval below is closed and rational; columns are ordered v5, v50, v55, v56.

| Original two parent-box IDs | Four exact intervals | Exact leaves | Splits | Minimum integer margin floor(LB)-Q | Newly included pair IDs |
|---|---|---:|---:|---:|---|
| 23,29 | [1/104,6/409], [34/49,27/38], [18/23,34/43], [19/24,4/5] | 66 | 65 | 25754627181721861699725646546279580 | (23,29) |
| 12,29 | [3/371,6/409], [7/10,27/38], [18/23,53/67], [19/24,4/5] | 88 | 87 | 46890424184761894156170614618712718 | (12,29) |
| 23,28 | [1/104,2/137], [34/49,7/10], [18/23,34/43], [4/5,9/11] | 162 | 161 | 1788669815076504029785421006152887 | (23,28) |
| 27,30 | [2/189,3/205], [7/10,12/17], [32/41,37/47], [4/5,17/21] | 360 | 359 | 4638422976475146033089763949860511 | (27,30) |
| 16,28 | [1/119,3/205], [16/23,12/17], [18/23,15/19], [13/16,9/11] | 381 | 380 | 1441085415662878829686364295197984 | (16,28),(17,28) |
| 4,26 | [2/271,6/409], [7/10,42/59], [60/77,11/14], [4/5,13/16] | 473 | 472 | 903503865712265886784690054399388 | (4,26),(4,30) |

There are **1530 strictly certified leaves and 1524 exact rational midpoint splits**, yielding **8 newly classified pair hulls**. Relative to inherited C265 classification over 363 legal pair hulls, strict negative 213 remains unchanged; strict positive increases 103→111; unresolved reduces 47→39. The 8 new pair IDs are (4,26),(4,30),(12,29),(16,28),(17,28),(23,28),(23,29),(27,30).

## Why this is a proof of full continuous boxes

For each fixed positive branch, `(Z-t)/|u_j-t|` is monotone on its legal pole-free interval; coordinate endpoints give global branch lower bounds. Each positive moving branch has
`(log f)'' = 6(2+t²)/(2-t²)² + 6(3+t²)/(3-t²)² + Σ_{j∉I}1/(t-u_j)² + Σ_{p≠k}1/(t-e_p)² >0`,
and is convex. A shared positive fixed-plus-moving one-variable sum is also convex. At each leaf, exact rational `BASE` or `SHARED_k` endpoint/convex tangent bounds yield `floor(LB)-Q > 0`. The full preorder binary-tree certificate splits closed boxes at exact rational midpoints, so all leaves cover their root boxes without sampling gaps. Numerical heuristics only selected the trees; all claims were checked using `fractions.Fraction`.

Author cross-check used (i) C257-style exact bounds on the fully expanded 1530 leaves and (ii) a separate from-raw-79-nodes Fraction implementation, rechecking the six complete trees (66/88/162/360/381/473 leaves), every midpoint, and every exact margin. This is *not* independent Driver review.

## Limits / open scientific frontier

This round inherited the previous 213 negative and 103 positive classifications, and did not rerun the original 15,685 candidate search; it does not compress the original 35 base rectangles. The 79-node model is an auxiliary scalar model. Native phase, labels, ports, residual BRC and future-operation preservation are not bridged. Next: classify the remaining 39 four-free pair hulls, especially the large (0,16) hull, with joint two-variable rigorous Hessian bounds or an exact rational counterexample.

## Source-control status / preservation

Authenticated GitHub identity: `awdawmip`. Native `em_control_tasks` returned `CONTROL_QUOTA`, and `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. There is no formal session, active-owner confirmation, CLAIM, Source Result or independent admission. This is an author-only unmerged research branch, not main. Google Drive was not used to evade access denial.

Full local author packet contains C266_THEOREM_AND_PROOF.zh-CN.md, 1530-leaf JSON certificate, C266_STANDALONE_REPLAY.py, author dual audit, logs, and unchanged C265 parent ZIP; ZIP SHA256 `16e52481eb12a627d6875f2dc289d04fc00b13bfbdd9b0051d94afed77c0a131`. The full ZIP itself is NOT asserted to be remotely stored.
