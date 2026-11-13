# R5: BP block-minimum index for exact certificate-prefix navigation

Date: 2026-11-12 (Asia/Shanghai). Author-side research continuation; unreviewed. External 28-coordinate / 15-atom P/Q–BRC Blackwell auxiliary model; no claim of transfer to native X6.

## Immutable provenance and comparison

Frozen scientific model: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551:research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`.
Frozen 1,065 selected legal ordered words: `awdawmip/enterprise-math@ad7013218d0474e1e942906e3beadec1eccb9213:research_notes/brc_r5_dual_zero_right_persistence_20261112/VERIFY_TRIE_CODEC.py`.
The previously validated indexed variable-width scheme and its 2,880-node tree: `awdawmip/enterprise-math@1ea46723f2d7db2702c63dc35e644cfe83266568`.
The Huffman-width followup: `awdawmip/enterprise-math@ab6b76d463d823de3fd4f9184a99117ff4d89419` (Draft PR #2171), with 41,087 bits / 5,136 bytes for B=64.
The unchanged suffix of 28,987 bits consists of incoming-operation labels, terminal flags, q-class masks, wavelet rows and rank directories, indexed by **preorder node number**. Its original-corpus proof and execution retain their prior status. This note changes only the tree-navigation representation.

## Theorem (indexed BP navigation, all ordered rooted trees)

Let T be any rooted, ordered tree with N nodes, labeled by preorder indices i=0,...,N-1. Its balanced-parentheses word P has exactly 2N bits: emit 1 on entry to a node and 0 on exit. Divide P into consecutive blocks of at most B bits. For each block j store:

* R_j = number of opening bits strictly before that block, using ceil(log2(N+1)) bits;
* M_j = minus the minimum local parenthesis excess (relative to the block start) among prefixes of that block, **including the empty prefix**, using ceil(log2(B+1)) bits.

No per-block total excess or close-position array is needed. For a complete block of length d, its excess change is exactly

    D_j = 2 (R_{j+1} - R_j) - d,

with the final sentinel R_last = N. The same formula uses the actual d for a final short block.

**select_open(i)**: find the last block whose R_j <= i using binary search, then scan within the block to its (i-R_j)-th opening. **rank_open(p)**: R_floor(p/B) plus the opening count from the block's start up to (excluding) p. These retain exact preorder identities.

For an opening position p, let h=2*rank_open(p)-p be its parenthesis excess before the opening. Scan the rest of its first block after p, starting with excess h+1. On a subsequent full block j entered with current excess e: if e-M_j>h, no prefix in that block returns to h, so skip it by adding D_j; otherwise scan the block to the first position whose after-bit excess equals h. This is exactly the matching close position q. The subtree size is (q-p+1)/2, so its preorder interval is [i,i+(q-p+1)/2). Direct children are enumerated by beginning at p+1 and repeatedly taking the matching close of the next opening, stopping at the parent close.

**Proof:** BP is the standard one-to-one encoding of finite ordered rooted trees. R_j is monotone and select/rank are exact by opening count. For a skipped complete block, e-M_j>h proves that every intermediate prefix excess is strictly above h. Otherwise scanning returns the first crossing of h. Every node opening has a unique first returning close in BP. Consequently the recovered subtree spans precisely its balanced pair interval; the opening count therein is half its length. By induction, every preorder node, child order, labeled path and terminal node is unchanged. Since the 28,987-bit suffix is indexed by identical preorder nodes, the old q-filtered Wavelet range-count answers C_p(r) transfer unchanged for all allowed parameters and prefixes.

The standalone index uses a fixed N and B, so no separate N/B header is counted. The 2N BP bits and all auxiliary fields are concatenated into one bitstream; only final byte padding is charged. A generic multi-model file would require its own scalar header. Complexity: select_open O(log ceil(2N/B)+B), rank_open O(B), match O(ceil(2N/B)+B) in the worst case under this simple linear block-skip design; subtree and child navigation remain exact.

## Exact space bound for frozen N=2,880 tree

At N=2,880, ceil(log2(N+1))=12, P takes 5,760 bits, and the untouched query suffix is 28,987 bits. For power-of-two block length B,

    F(B) = 5,760 + 28,987
           + ceil(5,760/B) * (12 + ceil(log2(B+1))) bits.

At B=64, there are 90 blocks; 12-bit opening ranks and 7-bit local minima cost 1,710 bits. Hence

    F(64)=5,760 + 28,987 + 1,710 = 36,457 bits
         = ceil(36,457/8)=4,558 bytes.

Compared with the previous B=64 Huffman-width full index of 5,136 bytes, the same **declared fixed-field payload budget** saves 578 bytes (11.25% of 5,136), at the price of block excess scans rather than direct size-code reads. Other B values are in EXACT_OUTPUT.json. This is a finite-model serialization budget, not measured resident memory, nor an asymptotic improvement of arbitrary succinct trees.

## Reproducible validation, boundary and next step

Run `node VERIFY_BP_BLOCK_MIN.js > EXACT_OUTPUT.json`. The actual executed tool result for this submission is in EXACT_OUTPUT.json. It independently enumerates every ordered rooted tree with 1..9 nodes (sum of Catalan numbers C_0+...+C_8 = 2,056 rooted trees), and checks select, rank, matching-close-derived subtree size, and every node's child sequence against a separate stack-based parse. It further tests four different 2,880-node shapes (star, chain, ternary, seeded random), checking all nodes. The executable checks block-excess reconstruction, all index variants' exact integer bit budget and B=64 bytes.

These are exact structural checks on generic trees. This turn has not executed the *original frozen R5 corpus integrated with wavelet outputs* under the new BP representation, nor measured construction CPU, packed-bit query wall time or peak heap. A useful next experiment builds the BP word from the actual 1,065 selected paths, proves bit-for-bit agreement with their 2,880 original preorder nodes, runs 57,600 identical prefix-parameter queries on Huffman and BP block-min indices, and records precise memory/latency plus B sensitivity. Both paths have a common immutable comparison fixture; no redefinition of P000 or user science pin is needed.
