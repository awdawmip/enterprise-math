# R284CH — 128-event parameterized modular-fiber index for the frozen 34-bit Port observer

Date: 2026-11-21 (Asia/Shanghai). Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. This is an independent, unclaimed portable continuation of R284CG, not a Task CLAIM, Result, Review, native-X6 theorem or worldview update.

## Frozen observer and its declared information boundary

Fix **exactly** the prior R284BZ/R284CG input:
\[
p=17179869143,\quad D=(1120832,6,13,1651128),\quad Z=(0,390139,394465,1497639).
\]
For \(C\in\{1,2\}^{4\times4}\), use \(F(C)=\det(\operatorname{diag}(D)-C-\sum_{j=1}^3 Z_jE_{0j})\pmod p\). The six lower key coordinates are \((C_{10},C_{11},C_{12},C_{20},C_{21},C_{22})\), indexed by \(k\in\{0,\ldots,63\}\). Let \(A_k\) be the previously established exact *closed* circular determinant arc, beginning at \(a_k\) with width \(w_k\). Define the labeled fiber signature for a circular real measurement \(y\) and error radius \(\rho\ge0\):
\[
\Sigma_\rho(y)=\{k:\operatorname{dist}_{\rm circle}(y,A_k)\le\rho\}.
\]
This index retains the **64-key provenance mask** but deliberately does not claim to preserve the hidden ten matrix coordinates, later operations, joint-state information or native X6 world geometry. Safe compression is established **only for this declared one-observation signature**. Full-state ambiguity remains as a structural residual.

Frozen reference: `awdawmip/enterprise-math@92fbdc24e623fc311911bbbcb8f292cc3d72229d:research_notes/portable_direct/R284CG_MODULAR_FIBER_SIGNATURE_STABILITY_20261121.md`. Its codeword SHA-256 is `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`.

## Exact theorem

**For every real** \(\rho\) in \(0\le\rho<1183/2=591.5\), and every real observation \(y\) on the circle of circumference \(p\), the 64-arc signature \(\Sigma_\rho(y)\) is recoverable using one shared fixed-order 128-event index, **at most 8 ordered-boundary comparisons**, and at most two stored key masks to handle exact boundary equality. No online determinant evaluation or scan through 64 arcs is needed.

* All 128 raw ENTRY/EXIT endpoints are distinct. The **minimum cyclic endpoint separation** is \(4,226,124\); their **minimum distance from the chosen cut at zero** is \(23,581,912\). Under radius expansion, each ENTRY moves by \(-\rho\) and each EXIT by \(+\rho\). Since \(2\rho<1183<4,226,124\), none can cross or reorder; also no endpoint can pass the origin. Consequently the ordering of all events and the mask on each open event cell are **independent of the radius** throughout the stated range.
* For a query, binary-search the sorted affine endpoints \(b_i+s_i\rho\), with \(s_i\in\{-1,+1\}\). The selected cell's mask is the answer except at exact equality, where the union of the masks immediately before and after the boundary is returned because every arc is closed.
* Among the 128 open circular cells, exact overlap-cardinality counts are \(\{0:14,\ 1:43,\ 2:46,\ 3:21,\ 4:4\}\). Thus a cell mask has at most four live keys. There are exactly **115** distinct cell masks: one empty and **114 nonempty**; all 114 nonempty masks are attained by at least one of the original 65,536 codewords. The exact full codeword histogram remains \(\{1:23178,2:23094,3:16964,4:2300\}\).
* The number of subsets of \(\{0,\ldots,63\}\) of cardinality at most four is
\[
\sum_{j=0}^{4}\binom{64}{j}=679121<2^{20}.
\]
Enumerative colex ranks require exactly 20 bits per stored cell mask. The static compact representation needs **128×5=640 bytes** for base circle endpoints, **16 bytes** for signed ENTRY/EXIT shifts and **128×20/8=320 bytes** for the mask ranks: **976 bytes total** excluding shared model constants and decoder implementation. Each mask can be recovered losslessly from its colex rank; this is an exact *packed representation size*, not measured RAM consumption.
* The R284CG outside-fiber separation \(\delta=1183\) remains in force. If \(x\) is any exact matrix codeword and \(\operatorname{dist}_{\rm circle}(x,y)<\rho<591.5\), then
\[
\Sigma_\rho(y)=\Sigma_0(x).
\]
Therefore the 114 signature types and forced-six-coordinate statistics of R284CG are recovered without loss under this coarse-observer error condition. **Full matrix correction still requires** \(\rho<29.5\), from full-codeword minimum distance 59.

## Proof and independent checks

An expanded closed arc changes membership only at its radius-shifted ENTRY and EXIT. The exact finite endpoint certificate ensures no collisions, order changes or origin crossings for the entire allowed real radius interval. Sweeping the events once at \(\rho=0\), setting a labeled bit on ENTRY and clearing it on EXIT, yields the signature mask for every open cell. Since event order never changes, the same masks apply at every \(\rho\) in range. At an endpoint, unioning its predecessor and successor masks includes that endpoint's membership in the closed arc; distinctness precludes simultaneous boundary ambiguity. Binary search among 128 affine thresholds needs no more than \(\lceil\log_2(129)\rceil=8\) comparisons. The exact local exhaustive certificate establishes the histogram, maximal overlap, realized type set, endpoint gaps and fixed 976-byte coding. Finally the circle-metric triangle inequality and R284CG's \(\delta=1183\) prove uniform real-noise signature stability. QED.

The local standard-library calculation reproduced all **65,536** codewords and the frozen SHA-256, tested **196,608** codeword index queries (at radii \(0,29.5,591\)) against original signatures, checked **384** exact boundary queries (128 boundaries at each radius), and checked the 128 mask ranks. The compact index SHA-256 is `af2d3ec14228af03eb9658a3301c732e3025d69f007e7e971da404f80c5fb155`. Universal real claims follow from the proof; the finite checker is the exact endpoint/histogram certificate, not floating-point extrapolation.

Companions: `research_notes/portable_direct/R284CH_parametric_event_index_checker.py`, `research_notes/portable_direct/R284CH_parametric_event_index_verification.json`. The prior codeword and arc identities are preserved. This script is a reproducible *alternative derivation*, not an assertion of independent mathematical review.

## Cost, unproved assertions and continuation

The 128-event index trades **976 static packed bytes** for online 8-comparison signature lookup, compared with prior zero-stored-arc synthesis in R284CE and stored 64-arc approaches in R284CD. Neither CPU speedup nor memory-layout advantage over all competitors has been measured. It does not directly invert the remaining matrix coordinates. Next experiments should benchmark these methods on matched inputs and ask whether an even smaller exact radius-parametric index or a true algebraic inverse is possible. The X6/P000 native ontology, formal Task state, other owners and source provenance are unchanged. Prior `EM-DIRECT-20B766` is historical contribution evidence, not a current execution capability.