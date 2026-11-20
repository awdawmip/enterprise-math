# R284CD — Coordinate-mask arc frontier for the fixed 34-bit Port observer

Date: 2026-11-20/21 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. Portable continuation of R284CC.

## Frozen finite observer and question

Preserve the R284BZ–R284CC finite observer and all frozen scientific input pins:

\[
F_C=\det(\operatorname{diag}(d_0,6,13,d_3)-C-z_1E_{01}-z_2E_{02}-z_3E_{03})\pmod p,
\]

where \((p,d_0,d_3,z_1,z_2,z_3)=(17179869143,1120832,1651128,390139,394465,1497639)\) and \(C\in\{1,2\}^{4\times4}\).

The lower-row coordinate list, in its frozen order, is

\[
L=(u_1,a_{11},x,y,u_2,w,a_{22},z,u_3,g,h,r)\in\{1,2\}^{12}.
\]

Each of the 4,096 lower states has 16 possible top-row states. The global minimum circular distance between the 65,536 codewords is 59, as certified by R284BZ/R284CC.

For any coordinate subset \(S\subseteq\{0,\ldots,11\}\), partition the lower states by their values at exactly those positions. Each of the \(2^{|S|}\) groups has \(2^{12-|S|}\) lower states and \(2^{16-|S|}\) full codewords. Form its shortest closed covering circle arc \(A_G\) by deleting the largest empty cyclic gap between sorted codewords. Define

\[
Q(S)=\max_{y\in\mathbb R/p\mathbb Z}
\#\{G:\operatorname{dist}_{\mathrm{circle}}(y,A_G)\le59/2\}.
\]

At any permitted circular observation error \(\rho<59/2\), the true group survives arc pruning. The decoder reconstructs at most \(Q(S)2^{12-|S|}\) candidate lower states; the four top-row bits are recovered by the previously proved R284CB threshold rule.

## Exact finite theorem: all 4,096 coordinate masks

Exhaustive integer computation over every \(\sum_{k=0}^{12}\binom{12}{k}=4096\) mask establishes the following minima of \(Q(S)\) for each mask size \(k\):

| Selected coordinates \(k\) | Stored arcs | Minimum worst-case groups | Optimal-mask count | Maximum lower reconstructions |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 4,096 |
| 1 | 2 | 2 | 12 | 4,096 |
| 2 | 4 | 4 | 66 | 4,096 |
| 3 | 8 | 6 | 2 | 3,072 |
| 4 | 16 | 8 | 3 | 2,048 |
| 5 | 32 | 8 | 1 | 1,024 |
| **6** | **64** | **4** | **1** | **256** |
| **7** | **128** | **7** | **1** | **224** |
| 8 | 256 | 13 | 2 | 208 |
| 9 | 512 | 22 | 1 | 176 |
| 10 | 1,024 | 39 | 1 | 156 |
| 11 | 2,048 | 70 | 1 | 140 |
| 12 | 4,096 | 128 | 1 | 128 |

The **unique optimal six-coordinate selection** is

\[
S_6=(u_1,a_{11},x,u_2,w,a_{22}),\quad Q(S_6)=4.
\]

Its 64 stored arc pairs require at most \(4\cdot64=256\) lower-state reconstructions and \(4\cdot256=1024\) top-row threshold comparisons. Compared with R284CC's 128 arc pairs and the same 256-reconstruction ceiling, index record count is halved.

The **unique optimal seven-coordinate selection** is

\[
S_7=(u_1,a_{11},x,u_2,w,a_{22},u_3),\quad Q(S_7)=7.
\]

Its 128 arc pairs require at most \(7\cdot32=224\) lower-state reconstructions and 896 top-row comparisons. This improves the prior seven-prefix R284CC index's 256 reconstructions and 1,024 comparisons at the same 128 records. The 34-bit encoding, all 65,536 codewords, minimum distance 59 and integer-noise guarantee ±29 are unchanged.

These optima concern **coordinate-subset partitions with one minimum covering circular arc per group**. Other nonlinear, parity or multiarc representations remain open.

## Proof and exact verification

**Exhaustive coverage.** For every selected subset, the checker groups all 4,096 lower states by their exact selected coordinates, expands all 16 top-row possibilities, sorts the resulting full codewords, and deletes the largest cyclic gap. This produces the shortest possible *single* covering arc for that group's codewords. All \(\binom{12}{k}\) masks are enumerated without sampling.

**Every real query position.** Work in doubled circle coordinates modulo \(2p\). A group arc of integer start \(a\) and width \(w\), expanded by \(59/2\), becomes a closed circular interval starting at \(2a-59\) with width \(2w+118\). Split wrapping intervals at the seam. The overlap count is piecewise constant between the finitely many endpoints; processing start events before finish events at coincident coordinates includes all closed boundaries. Exhaustive event sweeps thus compute the maximum for every real circular query, not merely integer noise samples.

**Independent checks.** Direct modular-membership evaluation at every endpoint and the seam independently confirms the selected six- and seven-coordinate bounds, across 129 and 257 distinct coordinates, respectively. Their shared maximal-overlap witness is \(2y=9213470267\) modulo \(2p\). The complete frozen codeword stream in top-row/lexicographic-lower order has SHA-256 \`b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4\`. All 4,096 exact overlap scores, serialized as sorted 12-bit mask integer and integer peak, have SHA-256 \`d18f850b3240eba3c369f3860ef103f90c26476986e7caa119c24b43b4d6dc2e\`.

The companion [checker](R284CD_coordinate_arc_mask_checker.py) is an independently executable Python 3/NumPy reproduction; [verification JSON](R284CD_coordinate_arc_mask_verification.json) includes the complete optimized 64-arc and 128-arc indices, all-size frontier, the endpoint counts and digest. Integer arithmetic is exact and all operations fit the respective Python integers / signed 64-bit NumPy bounds. Formalized proof or independent mathematical review has not been performed.

## Interpretation, control boundaries, next research

This is a finite auxiliary Port observer theorem whose BRC-relevant feature is **lossless observer-fiber pruning under a declared future readout and a fixed noise horizon**. It does not relabel the Port matrix as the P000 native X6 state. P000 V4 and the ACTIVE worldview, six-dimensional discrete spatial premise and protected Foundation status remain intact.

Frozen prior source: [R284CC at immutable commit 020c12db](https://github.com/awdawmip/enterprise-math/blob/020c12dbfdc8ebefe1d02d74457f26e6f0fb9649/research_notes/portable_direct/R284CC_128_ARC_RESIDUAL_COARSE_DECODER_20261120.md). This R284CD contribution is portable, without a new formal Task or CLAIM.

Next: investigate parity/affine partitions or a direct suffix residual inverse to reduce the 64-index/four-group cost, and benchmark whole decoder cost (index bytes, preprocessing, per-query arithmetic and final verification). The prior separate question of a 33-bit code retaining gap 59 remains open.
