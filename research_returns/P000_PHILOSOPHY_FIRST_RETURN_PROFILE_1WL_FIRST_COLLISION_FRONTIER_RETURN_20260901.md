# P000 Philosophy-First Q25 — Return-Profile initialized 1-WL first-collision frontier

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-FIRST-COLLISION-FRONTIER`  
Publication: `TP2-00DBAF3804A8CB88ED06`  
Researcher: `EM-PQ25-9B31E4`  
Claim: `chatgpt-p000q25-g2-20260902-0745-9b31e4`  
Execution branch: `research/p000-phil-q25-return-profile-1wl-collision-em-pq25-9b31e4`  
Hard target: `P000_RETURN_PROFILE_1WL_FIRST_COLLISION_OR_EXTENDED_LOWER_BOUND_EXACTLY_CLASSIFIED`

## Terminal verdict

`SUCCESS / RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_STRICTLY_EXTENDED`

The Q22 observable is held fixed without modification:

\[
c_0(x)=m_X(x),\qquad
c_{t+1}(x)=\Bigl(c_t(x),\operatorname{multiset}_{y\sim x} c_t(y)\Bigr),
\]

where `m_X(x)` is the primitive simple-cycle multiplicity profile through root `x`, and the graph-level output is the anonymous stabilized packet `R_inf(X)`.

Q22 already proved exact injectivity on `U_BR(n)` for `4<=n<=9`. Q25 now proves exact injectivity also on `U_BR(10)`. Therefore the rigorous collision-free frontier is extended to

\[
4\le n\le 10.
\]

No collision-free claim is made for `n>=11`, and no claim is made that the frozen 1-WL observable reconstructs all finite `U_BR` objects.

## 1. Exact n=10 classification

For `n=10`, let `r` be the number of degree-3 Cells. Handshaking forces `r` even, and the admissible sectors are

\[
r\in\{2,4,6,8,10\}.
\]

As in Q22, normalize labels so that the degree-3 Cells are exactly `0,...,r-1`. The deterministic checker proves the following exact sector census:

| degree-3 count `r` | exact normalized connected realizations | graph-isomorphism types | stable packets | collision? |
|---:|---:|---:|---:|:---|
| 2 | 433,440 | 18 | 18 | no |
| 4 | 866,520 | 109 | 109 | no |
| 6 | 1,847,340 | 198 | 198 | no |
| 8 | 4,329,360 | 113 | 113 | no |
| 10 | 11,166,120 | 19 | 19 | no |
| **total** | **18,642,780** | **457** | **457** | **no** |

Hence every exact equal-packet fiber at ten Cells contains exactly one graph-isomorphism type.

Together with Q22, the exact prefix through ten Cells contains:

- normalized connected realizations: `566,557 + 18,642,780 = 19,209,337`;
- graph-isomorphism types / stable packets: `241 + 457 = 698`.

## 2. Why the finite cover is complete

The final certificate does **not** rely on random sampling or on trusting the representative-discovery procedure.

For each degree sector `3^r 2^(10-r)`, the checker first computes the exact number of labeled simple realizations by a deterministic degree-state recurrence. A distinguished labeled vertex is connected to subsets of the remaining degree classes; binomial coefficients count the choices of labels, and the residual degree multiset is recursed on. Connected counts are then obtained by subtracting all realizations in which the connected component of one distinguished vertex is proper.

The same recurrence is regression-checked against every Q22 normalized connected sector count for `4<=n<=9`:

- `n=4`: `1,1`;
- `n=5`: `7,6`;
- `n=6`: `54,54,70`;
- `n=7`: `450,552,810`;
- `n=8`: `4080,6012,10080,19320`;
- `n=9`: `40320,69840,132660,282240`.

It reproduces all Q22 counts exactly before the new ten-Cell certificate is accepted.

For each frozen ten-Cell representative `G`, the checker independently recomputes its exact automorphism-group order by adjacency-preserving backtracking, using only isomorphism invariants to prune candidate images. Because graph automorphisms preserve degree, the number of normalized labelings represented by `G` in sector `r` is exactly

\[
\frac{r!(10-r)!}{|\operatorname{Aut}(G)|}.
\]

The sum of these orbit sizes over the frozen representatives agrees **exactly**, sector by sector, with the independently computed normalized connected count:

\[
\sum_{[G]}\frac{r!(10-r)!}{|\operatorname{Aut}(G)|}
= N_{10,r}.
\]

The five equalities are respectively

`433440, 866520, 1847340, 4329360, 11166120`.

Thus the frozen representative list contains every graph-isomorphism class in `U_BR(10)` exactly once. Completeness is certified by orbit-stabilizer accounting, not by an assumed stopping criterion of the discovery search.

## 3. Exact packet separation

For every one of the 457 representatives, the checker recomputes from adjacency alone:

1. every primitive simple unoriented cycle and each root profile `m_X(x)`;
2. the frozen Q22 iterative color update;
3. the stabilized anonymous semantic packet, represented by the same lossless finite-DAG compression used in Q22;
4. the exact automorphism-group order.

No hash decides packet equality. SHA256 is used only after the complete packet serializations have been constructed, to pin the already verified finite image.

All 457 packet serializations are distinct, including across degree sectors. Therefore

\[
R_\infty(X)=R_\infty(Y),\quad X,Y\in U_{BR}(10)
\Longrightarrow X\cong Y.
\]

The whole ten-Cell packet image digest is

`fc81927d21515e237caf5ed8023ebcb51835b160d133c112d2c89b870b1f53ba`.

Per-sector packet-image SHA256:

- `r=2`: `f034566dd7235f7e57cbc78a429308891d92ef24f513162d299c7db1bc702d12`
- `r=4`: `65bff91bc0e1adde28934bc29a7f45be942a84b36c3e2d7aa2b6431de3337519`
- `r=6`: `dfd66a85fccf3f0562bbe09b8c38aaa50bf87d7f1205091f876a34e4cf014611`
- `r=8`: `faa3b5c11095881c27d933bc09f9e91fda71ea47bf0b11d5057b48d288650dda`
- `r=10`: `5b046818781ca6c0ac5aa5395bcab17d3df40dafd410f249174bb0f3127c0fa9`

Machine artifact:

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_FIRST_COLLISION_FRONTIER/P000_Q25_RETURN_PROFILE_1WL_N10_EXACT_ORBIT_CERTIFICATE_V1.json`

The artifact compactly stores the 457 representatives as graph6 strings, aligned exact automorphism orders, exact orbit sums, regression counts, and packet-image digests.

## 4. The observable is still not a hidden canonical labeling

The ten-Cell stable root partitions have stabilization-index census

`0:150, 1:185, 2:106, 3:16`.

The maximum stabilization index therefore remains `3` on the exact prefix through ten Cells.

Stable root-color class counts on the 457 ten-Cell isomorphism types are

`1:3, 2:2, 3:38, 4:34, 5:46, 6:85, 7:59, 8:39, 9:51, 10:100`.

Only `100/457` ten-Cell objects have a discrete stable root partition; `357/457` retain nontrivial anonymous root classes. Thus the bounded graph-level injectivity at `n=10` is not evidence that the root refinement became a vertex-by-vertex canonical encoding.

This preserves the Q22/Q25 abstraction boundary: the task measures the actual strength of the frozen low-order observable and does not import 2-WL, spectra, zeta data, full cycle incidence, or canonical labels.

## 5. Search route and authority boundary

Countermodel-first structural search was used to discover candidate representatives, beginning with degree-2/3 suppression-kernel structure and then broadening to all five degree sectors. That search procedure is not itself the completeness authority.

The terminal conclusion rests only on the deterministic certificate described above:

- exact degree-sequence realization recurrence;
- exact connected-sector subtraction;
- exact automorphism counts;
- exact orbit-stabilizer cover equality;
- exact recomputation and uniqueness of all 457 frozen stable packets.

The deterministic checker is standard-library only. On the frozen artifact it returns:

`PASS Q25 n=10 exact orbit certificate: representatives=457 normalized_connected=18642780 stable_packets=457 collision=0 lower_bound=n<=10`

## 6. Terminal boundary and next question

The accepted terminal class requested by the taskbook is

`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_STRICTLY_EXTENDED`.

What remains open is the first collision at `n>=11`, if one exists. Q25 does not authorize repairing a future collision or escalating the observable. Any continuation must keep the Q22 observable fixed and must be separately published by the Driver, with an explicit finite or structural target.

No Working Truth, Foundation, L4, novelty, universal reconstruction theorem, or higher-WL promotion is claimed here.
