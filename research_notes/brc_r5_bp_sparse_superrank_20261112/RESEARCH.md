# R5 — Sparse opening-rank anchors for BP block-minimum navigation (frozen original corpus)

Date: 2026-11-12 (Asia/Shanghai). Status: author-side exact research, not an independently reviewed Source Result. Scope: frozen external P/Q–BRC Blackwell 28-coordinate / 15-atom auxiliary model; no native X6 transfer is claimed.

## Scientific pins and continuity

- Frozen scientific input: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551:research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py.
- Canonical 1,065 selected dual-zero paths (2,880 preorder trie nodes): awdawmip/enterprise-math@ad7013218d0474e1e942906e3beadec1eccb9213:research_notes/brc_r5_dual_zero_right_persistence_20261112/VERIFY_TRIE_CODEC.py.
- Full BP/Wavelet query test: awdawmip/enterprise-math@eb3a80abe45ddd2305c7a0247a45eeba9bef04d3:research_notes/brc_r5_bp_wavelet_prefix_20261112/VERIFY_R5_BP_WAVELET_PORTABLE.py.
- Complete rank/Wavelet suffix and variable-width bitstream: awdawmip/enterprise-math@1ea46723f2d7db2702c63dc35e644cfe83266568:research_notes/brc_r5_variable_skip_full_20261112/VERIFY_R5_VARIABLE_SKIP_FULL.py.
- Immediate BP block-minimum baseline (Draft PR #2174): awdawmip/enterprise-math@8c71703b427c096b9d0007f46b6dbcc26b6f1c02:research_notes/brc_r5_bp_block_min_20261112/RESEARCH.md.

Frozen scientific pins remain unchanged; only the indexing of the same ordered source-labeled paths changes.

## New theorem: rank superblock sparsification

Let P be the balanced-parentheses encoding of an ordered rooted tree with N nodes; opening = 1, closing = 0. Let B be the fixed block width, and G≥1 an integer number of blocks per superblock. Retain for every block j its negative minimum local excess M_j (including the empty prefix) as in the previous BP block-min scheme, but retain the absolute opening rank R_j only at every G-th block, namely A_s=rank_1(P,sGB). The stored BP word itself supplies every omitted opening rank:

    rank_1(P,p) = A_floor(p/(GB)) +
                  popcount(P[floor(p/(GB))*GB : p]).

For p at the end of the word, choose the final existing superblock anchor and count the suffix. Each value is exact, because the intervals concatenate and A_s counts openings strictly before the anchor.

For opening select(i), binary search the nondecreasing anchor values for the last anchor A_s≤i and scan its superblock until the i-th opening (0-based). A later anchor, if any, is >i, so the requested opening lies in the selected superblock. Repeated equal anchor counts are handled by selecting the last such anchor.

For match(p), recover the original before-opening excess h=2rank_1(P,p)-p. Scan the rest of the first block. In every subsequent block entered with excess e, skip the whole block if e-M_j>h, updating e exactly by 2popcount(block)-block_length; otherwise search the block for the first prefix reaching h. The old block-min proof applies verbatim. The matched close recovers subtree_size=(close-p+1)/2 and its contiguous preorder node interval; thus all terminal intervals, ordered word labels, and original Wavelet range-count answers are preserved.

This is a general finite ordered-tree exactness theorem. In a bit-operation model, superblock rank/select take O(GB); BP matching takes O((2N/B)*B+B) in the worst case when skipped block popcounts cost O(B). For B fitting a native machine word with constant-time popcount, matching becomes O(2N/B+B), with rank/select O(G) word-popcounts plus a bounded final bit scan. The theorem concerns exact queries; no unmeasured CPU, heap, or asymptotic superiority is asserted.

## Exact frozen-corpus storage result

At N=2,880 and B=64, P takes 5,760 bits. There are J=90 blocks, each M_j stored in 7 bits (630 bits). Choose G=8, so 12 rank anchors use 12 bits each (144 bits). Preserve unchanged the 28,987-bit complete labels, terminals, q-masks, Wavelet rows, and fixed-width rank directory from the baseline. Total:

    5,760 + 90*7 + 12*12 + 28,987
      = 35,521 bits = 4,441 bytes (with final byte padding).

Baseline B=64 BP block-minimum storing a 12-bit rank at every block:

    5,760 + 90*(12+7) + 28,987
      = 36,457 bits = 4,558 bytes.

Thus the exact same-field serializable bit budget is reduced by 117 bytes, i.e. 936 bits (about 2.57%). In this fixed geometry and representation, no header is needed for N/B/G. Generic containers require explicit dimensions and framing; resident memory, indexing initialization, and latency need separate measurement.

A parameterized exact bit budget is

    F(N,B,G,S) =
      2N + ceil(2N/B)*ceil(log2(B+1))
         + ceil(ceil(2N/B)/G)*ceil(log2(N+1))
         + S,

where S is the unchanged suffix bit budget. The formula applies when each M_j and anchor uses the indicated fixed-width fields, and the final byte cost is ceil(F/8).

## Executed proof checks and replay

A standalone stdlib Python test reconstructed the actual frozen X, H, integer port vectors, all 32,768 masks, and selected the canonical shortest masks and legal orders. Its executed output (in EXACT_OUTPUT.json) verified:

- 1,065 pair–word witnesses, 2,880 preorder nodes, 953 activation thresholds;
- actual bitstream construction and decode: 35,521 bits / 4,441 bytes, including the unchanged 28,987-bit suffix and its rank directories;
- all 2,880 node select/rank/match/subtree checks against independently built BP;
- 57,600 exact prefix–parameter activation comparisons over 20 rational parameters; C_root(0)=605.

VERIFY_R5_BP_SPARSE_SUPERRANK.py is the repository-integrated replay program: it reuses the already pinned original-corpus checker and complete suffix, changes only BP navigation, then reruns 57,600 exact comparisons. This newly published version has not yet been executed from its remote bytes in a clean checkout; the local standalone reconstruction was executed and passed. Its expected terminal marker is PASS_R5_BP_SPARSE_SUPERRANK_REAL_1065. This distinction matters when promoting the result to independent review.

## Next scientific unit

Run the published integrated script from its immutable commit in a clean checkout. Benchmark B=16/32/64, G=1/2/4/8/16 using fixed identical query order and repeated trials, reporting serialization bytes, initialization time, complete query latency distribution, peak resident heap, and actual decomposition of rank/select vs match vs Wavelet work. A simple two-level superblock directory or native word-popcount may move the practical Pareto frontier.
