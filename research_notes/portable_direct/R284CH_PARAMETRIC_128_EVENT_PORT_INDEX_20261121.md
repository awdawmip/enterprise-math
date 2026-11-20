# R284CH — Parametric 128-event circular-fiber index (frozen 34-bit Port)

Date: 2026-11-21 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. Independent portable continuation of R284CG, not a CLAIM/Result/Review and not an X6 world-model proof.

## Exact input, provenance and observer scope

Use exactly the frozen R284BZ/R284CG Port observer, with no scientific input rebase:
[
p=17179869143,quad D=(1120832,6,13,1651128),quad Z=(0,390139,394465,1497639).
]
For (Cin{1,2}^{4	imes4}), let (F(C)=det(mathrm{diag}(D)-C-sum_{j=1}^3 Z_jE_{0j})pmod p). Fix the six coordinates ((C_{10},C_{11},C_{12},C_{20},C_{21},C_{22})), indexed by (kin{0,ldots,63}). Denote by (A_k) the exact closed circular determinant arc of R284CE/R284CG, with start (a_k) and width (w_k). For any circular real observation (y) and radius (hoge0), retain the **key-labeled fiber signature**
[
Sigma_ho(y)={k:operatorname{dist}_{m circle}(y,A_k)leho}.
]
It is a coarse Port-observer index for a declared single observation, not a lossless reconstruction of the full matrix, future process, joint state, or native X6 Cell address. Keys/provenance remain recoverable; discarded matrix coordinates are not declared redundant for later operations.

Source: immutable R284CG note at `awdawmip/enterprise-math@92fbdc24e623fc311911bbbcb8f292cc3d72229d:research_notes/portable_direct/R284CG_MODULAR_FIBER_SIGNATURE_STABILITY_20261121.md`; R284CG checker at its frozen source. Original ordered 65,536-codeword SHA-256: `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`.

## Theorem: a universal radius-parametric event index

There is a *single*, order-preserving 128-event index, valid simultaneously for **every real** (0leho<1183/2=591.5), which returns (Sigma_ho(y)) for every real circle location (y) with at most **8 ordered-boundary comparisons**, followed by one indexed signature lookup and, only when (y) is exactly on an event, union with its predecessor's signature.

1. The 64 arcs yield exactly 128 **distinct** raw endpoints modulo (p), each typed ENTRY or EXIT. The minimum cyclic gap between consecutive endpoints is **4,226,124**; the closest endpoint to the chosen circle cut (0) is **23,581,912**. In a radius-expanded arc, ENTRY shifts by (-ho) and EXIT by (+ho). Since adjacent endpoints can approach each other by at most (2ho<1183), neither their order nor their crossing status changes within the claimed radius range. No endpoint crosses the cut. Thus the ordered event labels and the signature mask on each intervening open cell are **independent of (ho)**.
2. For each query, compare (y) with the 128 sorted affine boundaries (b_i+s_iho), (s_iin{-1,+1}), by binary search on the original order. If (y) equals a boundary, take the bitwise union of its left-cell and right-cell masks; this handles closed-arc endpoints exactly. The search needs at most (lceillog_2(129)ceil=8) comparisons and no online determinant or arc membership calculation.
3. Across the 128 open circular cells, the overlap-cardinality histogram is exactly **0:14, 1:43, 2:46, 3:21, 4:4**, so at most four of the 64 keys are live in any open cell. There are exactly **115** distinct cell signatures: one empty and 114 nonempty. All **114 nonempty** signatures occur at actual frozen matrix codewords (no extraneous nonempty signature type). These are *types*, not counts of distinct matrices; the R284CG codeword distribution remains **1:23178, 2:23094, 3:16964, 4:2300**.
4. Because each cell signature is a subset of 64 keys of size at most 4, it can be enumeratively ranked using (sum_{j=0}^4inom{64}{j}=mathbf{679121}<2^{20}) possibilities. A dense static index uses 128 raw endpoints of five bytes (640 B), 128 ENTRY/EXIT bits (16 B), and 128 20-bit mask ranks (320 B): **976 bytes total**, excluding shared model constants and decoder code. Ordered-key colex ranking/unranking recovers the exact 64-bit provenance mask. An uncompressed direct-mask alternative uses 1680 bytes. The 976-byte packed index is a proven *representation size*, not a measured machine-memory allocation or latency.
5. R284CG proves (delta=1183) for the minimum separation of an actual codeword from any excluded arc. By the circle metric triangle inequality, for any codeword (x) and any (y) with (operatorname{dist}(x,y)<ho<591.5), the index returns exactly (Sigma_ho(y)=Sigma_0(x)). Thus the previous key-forcing and 114-type statistics remain valid at this radius. **Full 16-coordinate matrix reconstruction still has its own, smaller radius (<29.5)** due to minimum full-code distance 59.

### Proof

Every group interval was established by the frozen cofactor/monotone determinant calculation; each interval's mod-(p) image is a closed arc. Its inflated membership is a piecewise-constant Boolean function with two and only two changes per period at the shifted endpoints. The finite exact endpoint certificate gives 128 distinct bases, minimum cyclic gap 4,226,124 and distance from circle cut 23,581,912. Since (2ho<1183<4226124) and (ho<591.5<23581912), no event collision, relative reorder or cut crossing is possible. Sweep once from cut zero: ENTRY sets its key bit, EXIT clears it. The mask following each event therefore describes the full signature on the next open cell for *all admissible radii*. For a boundary point, union with the preceding mask includes both adjacent closed-arc memberships; distinctness excludes ambiguous simultaneous events. Binary search over 128 fixed-order affine thresholds returns the correct cell; its comparison bound follows from binary-search worst-case depth. Exact subset cardinality, cell histogram, signature realizability, 64-key rank count and static packed byte count follow from the finite certificate. R284CG's previously verified (delta=1183) and the triangle inequality prove the stated uniform real-noise inheritance. QED.

## Verification coverage and limitations

Local standard-library exact checker reproduced all 65,536 ordered codewords and the frozen SHA-256; checked the 128-event raw endpoint geometry and all 128 boundary cases for each of (ho=0,29.5,591) (384 tests); performed **196,608** codeword-index lookups at these radii, checking them against original codeword signatures; and verified all 128 colex pack/unpack identities and the 976-byte packed index SHA-256 `af2d3ec14228af03eb9658a3301c732e3025d69f007e7e971da404f80c5fb155`. Tests are exact integer arithmetic. The universal real-(y), real-(ho) assertion is the event-order and boundary proof, **not** an inference from sampled real observations. Independent semantic review is not yet performed; no CPU timing/acceleration is asserted.

Companions: `research_notes/portable_direct/R284CH_parametric_event_index_checker.py` and `R284CH_parametric_event_index_verification.json`. The checker reconstructs the index from frozen parameters and independently recalculates the certificate. It does not model X6 native geometry, BRC positive-mass operations, force/Cell dynamics or physical laws.

## Cost / new question

This exact online trade-off replaces up to 64 arc-membership tests by up to 8 order comparisons plus one signature lookup, but spends 976 bytes for the static table (whereas R284CE could synthesize arcs without a stored table). It does **not** eliminate downstream lower-coordinate candidate search nor certify faster CPU latency. Next: benchmark R284CE/R284CD/R284CH under matched workloads; seek a smaller-than-976-byte constant-order index or a direct algebraic inverse of the remaining five/six lower bits while preserving the labeled fiber and full-matrix error semantics.

Persistence/authority: portable unclaimed Source note; prior researcher `EM-DIRECT-20B766` is provenance only, not proof that this turn possesses that SID's capability. No task/CLAIM/Activity/Review authorization inferred.