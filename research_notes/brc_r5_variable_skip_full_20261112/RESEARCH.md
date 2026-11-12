# R5 — Full frozen-corpus variable-width subtree-skip index (5,393 bytes)

Date: 2026-11-12 (Asia/Shanghai). Role: author-side independent algorithmic research; **external** P/Q–BRC Blackwell 28-mass-coordinate, 15-labeled-operation auxiliary model. P000/native-X6 research premises are unchanged.

## Exact immutable scientific ancestry

- Original 28-coordinate / 15-atom input: \`awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551:research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py\`.
- The 1,065 selected shortest legal pair-words and original exact selection: \`awdawmip/enterprise-math@ad7013218d0474e1e942906e3beadec1eccb9213:research_notes/brc_r5_dual_zero_right_persistence_20261112/{VERIFY_RIGHT_PERSISTENCE.py,VERIFY_TRIE_CODEC.py}\`.
- Existing fixed-width index: \`awdawmip/enterprise-math@bc37fd6bb2e9f7802c15c78a9b31d13e5ff04e1a:research_notes/brc_r5_preorder_skip_rank_20261112/RESEARCH.md\`, with 2,880 nodes, 1,065 terminal words, and 63,547 bits / 7,944 bytes of explicitly indexed fields. Previous synthetic-shape verification in that branch is **not** the original-corpus execution.
- To preserve these inputs without duplicating/copying the historical sources, this experimental branch forks the immutable \`eb3a80abe45ddd2305c7a0247a45eeba9bef04d3\` PR #2161 commit, where the pair-word selector and its pinned source already exist. This is a **stacked branch**, not a canonical-main mathematical acceptance.

## Proposition: sampled variable-width preorder subtree sizes

Let \`N=2880\` and \`T=1065\` denote the actual selected-word trie sizes. In preorder, let \`s_i\` be the number of nodes in the subtree rooted at node \`i\`; \`1 <= s_i <= 2880\`. Encode each \`s_i\` by a **two-bit width tag** and one of 2, 4, 8, 12 payload bits:

| Subtree size \`s_i\` | Tag | Size bits (tag included) | Count in frozen trie |
|---|---|---:|---:|
| 1–3 | \`00\` | 4 | 2,182 |
| 4–15 | \`01\` | 6 | 572 |
| 16–255 | \`10\` | 10 | 122 |
| 256–2880 | \`11\` | 14 | 4 |

Store a 16-bit start-bit offset for the variable-coded entry at every 64th preorder node (indices 0,64,128,...,2816); there are 45 offsets and the maximum offset is below \`2^16\`.

**Lemma 1 (exact random node decoding).** To retrieve \`s_i\`, choose block \`b=floor(i/64)\`, read its 16-bit offset, parse the tag/payload codes of at most \`i-64b <= 63\` preceding nodes, then decode \`s_i\`. The result is exact, regardless of subtree shape. At most 63 prior variable codes are traversed; thus this is a fixed-bound indexed lookup for the given 64-node blocks, without storing a per-node bit offset.

**Lemma 2 (tree navigation).** Preorder puts a subtree in the node interval \`[i,i+s_i)\`. Enumerate the children by starting at \`c=i+1\` and repeatedly setting \`c <- c+s_c\` until reaching \`i+s_i\`. A child label is its incoming 4-bit label. Each step locates the next sibling precisely. Given a path of length \`k\` and at most 15 distinct child labels per node, prefix traversal uses at most \`15k\` such skip decodings, with at most 63 tag scans each. This bound is independent of the number of stored certificates for the fixed block size and label alphabet.

**Lemma 3 (exact prefix activation count).** The terminal preorder ranks of \`i\` are \`[rank_T(i), rank_T(i+s_i))\`. With the unchanged two q masks and three wavelet matrices, for each prefix \`p\` and allowed \`r < 1/23\`,
\[
C_p(r)=\sum_{q\in\{3,12,15\}}\#\{(q,n)\in D_p:n\le\lfloor36q/(1-23r)\rfloor\}.
\]
For exact rational \`r=a/b\`, \`b>0\`, use \`floor(36qb/(b-23a))\`; at the \`r=1/23\` zero-scale endpoint return all terminals below \`p\`. The 64/512 rank-directory semantics and 29 wavelet rows are unchanged from the previous fixed-width index. Therefore the full query algorithm is exact.

## Complete serialized size: original selected corpus

Variable subtree codes, by exhaustive original-corpus enumeration:
\[
2182\cdot4+572\cdot6+122\cdot10+4\cdot14=13,436\ \mathrm{bits}.
\]
The 45 sampled offsets consume \`45*16=720\` bits. Everything else in the predecessor fixed-schema index is unchanged:

| Serialized field | Bits |
|---|---:|
| Variable subtree size codes | 13,436 |
| Sampled 64-node block offsets | 720 |
| 2,879 incoming 4-bit labels | 11,516 |
| 2,880 terminal bits | 2,880 |
| Two 1,065-bit q-class flags | 2,130 |
| 29 wavelet bit rows | 10,421 |
| 64/512 rank directories for all 32 bitvectors | 2,040 |
| **Total** | **43,143** |
| **Single bit-packed byte stream** | **5,393 bytes** |

Relative to the earlier **7,944-byte** fully indexed predecessor with the *same q-prefix activation query*, this construction saves **2,551 bytes = 32.11% of the earlier rounded byte length**. The exact bit saving is \`63,547-43,143=20,404\` bits: the 21,124-bit subtree-code saving minus 720 bits of sampled offsets. Retained 4-byte outer schema/fixed dimensions are not included in either number; both use the same external schema convention. No runtime heap, startup CPU, or input-fixture storage is counted in either quoted serialization.

For larger trees the tag-widths and 16-bit sampled offsets require corresponding bound changes. Fixed-width rank cost and bigint parameter arithmetic remain part of the actual query cost. The 64-tag scan makes a different time/space tradeoff from the earlier constant-access 12-bit subtree sizes.

## Executed mathematical evidence and verification coverage

An independently reconstructed author-side frozen fixture used the original 28 mass coordinates, original \`R\`, coefficients and 15 signed operation vectors. With exact Python \`Fraction\` calculations it enumerated all 32,768 subsets, recovered 1,065 eligible \`(q,n)\` pairs and 2,935 candidate masks, selected the same \`(bitcount,mask)\` minimizer and legal canonical dynamic-programming word, and reproduced 2,880 nodes, 6,379 path labels, 953 activation thresholds and root count \`C_empty(0)=605\`.

The local implementation created the actual 5,393-byte bitstream, decoded all seven fields and all rank directories, recovered every 1,065 labeled word/pair, verified 2,879 child subtree jumps and 15,463 rank positions, and matched 57,600 exact node-by-parameter activation counts against direct per-certificate enumeration (2,880 nodes x 20 rational parameters). All tests passed. \`VERIFY_R5_VARIABLE_SKIP_FULL.py\` is the portable, compact verifier of the **same** bitstream/query mechanism using the pinned 1,065-word source included in this branch's ancestry. The compact verifier was also executed locally against the independently reconstructed exact word corpus with a module shim, and passed. Re-execution of the remote file against the immutable predecessor's actual imported Python modules is a separate next reproduction check.

Observed author-side terminal output:
\`\`\`text
ORIGINAL_FROZEN_SELECTED_WORDS 1065 PREORDER_NODES 2880
SUBTREE_SIZE_WIDTH_DISTRIBUTION (2182, 572, 122, 4)
VARIABLE_SIZES_BITS 13436 BLOCK_OFFSETS_BITS 720
FULL_PACKED_BITS 43143 BYTES 5393
EXACT_RANK_CHECKS 15463 PREFIX_PARAMETER_CHECKS 57600
PASS_R5_VARIABLE_SKIP_FULL_FROZEN_CORPUS_INDEX
\`\`\`

## Remaining question / next experiment

Benchmark decoded-vs-bitstream direct skip access, full index build time, query latency distribution and peak process memory for the fixed-width 7,944-byte predecessor and the variable-width 5,393-byte index **on the same original word corpus and query distribution**. Explore an alternative block width or succinct excess/BP navigation as additional time-space choices. Preserve the frozen 28-coordinate input and report each cost separately. Formal Source Result, independent Driver mathematical review and TASK owner binding are separate pending operations, not consequences of this proof or GitHub publication.
