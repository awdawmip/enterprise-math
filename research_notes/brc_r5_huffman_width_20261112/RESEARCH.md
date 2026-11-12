# R5: Huffman-coded subtree-width tags, exact 5,136-byte indexed-prefix construction

Date: 2026-11-12 (Asia/Shanghai). Author-side TASK_RESEARCH, external P/Q–BRC Blackwell auxiliary model, no change to native X6 or P000.

## Frozen scientific ancestry and target

The immutable 28-coordinate / 15-labeled-atom model is at awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551:research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py. The 1,065 selected double-zero legal words were fixed at awdawmip/enterprise-math@ad7013218d0474e1e942906e3beadec1eccb9213:research_notes/brc_r5_dual_zero_right_persistence_20261112/VERIFY_TRIE_CODEC.py. The immediately preceding full indexed structure is awdawmip/enterprise-math@1ea46723f2d7db2702c63dc35e644cfe83266568:research_notes/brc_r5_variable_skip_full_20261112/RESEARCH.md, accompanied by the executable exact verifier. This stacked branch changes only the width-class tag code; it reuses the exact 1,065 words, 2,880-node preorder tree and 28,987-bit indexed-query suffix.

The previous variable-width skip representation consumes 43,143 bits (5,393 bytes) at block stride B=64. Its four subtree-size payload widths are 2,4,8,12 bits; a 2-bit width tag precedes each payload. The actual frozen tree has 2,182, 572, 122 and 4 nodes in these respective width classes.

## Theorem: optimal binary prefix tags for the existing four classes

Retain the original size payload bits and their class boundaries:
- size 1..3: width=2, tag 0;
- size 4..15: width=4, tag 10;
- size 16..255: width=8, tag 110;
- size 256..2880: width=12, tag 111.

All four tags are prefix-free. They decode uniquely without knowing the size of the next subtree or its children. At every stride-B block start, store an exact 16-bit offset to the first tagged symbol. The decoder visits at most B-1 preceding symbols to recover a node's size. In the frozen N=2,880-node tree, every such bit offset is below 2^16.

Among **binary prefix-free codeword assignments to these four fixed width categories** this assignment minimizes total tag bits for the frozen frequencies. Proof: the Huffman bottom-up merges of ascending frequencies are (4,122)->126, (126,572)->698, and (698,2182)->2880; the standard binary prefix-code exchange argument states that a minimum-weight prefix tree places the two least frequent symbols as deepest siblings and contracts them recursively. The resulting code lengths are (1,2,3,3), with weighted bit length

  H = 2182*1 + 572*2 + 122*3 + 4*3 = 3704 bits.

The previous constant two-bit tag uses 2*N=5,760 bits. Thus exactly 2,056 tag bits are removed, with all 7,676 size payload bits unchanged. The *new* tagged-size bitstring has exactly 11,380 bits instead of 13,436.

The proposition is an optimum only inside this specified four-class, one-prefix-tag-per-size family. It does not claim global entropy compression optimality.

## Exact total serialized size and navigation proof

There are ceil(2880/B) sampled 16-bit offsets and 28,987 unchanged suffix bits (incoming labels, terminal flags, q-class masks, 29 wavelet rows, and all 32 rank directories). Therefore, for any positive stride B whose offsets fit in 16 bits, the exact serialized bit budget is

  H_F(B) = 3704 + 7676 + 28987 + 16*ceil(2880/B)
         = 40367 + 16*ceil(2880/B).

For B=64, 45 offsets occupy 720 bits. Total = 41,087 bits = 5,136 bytes after packing, a **257-byte reduction** from 5,393 bytes (2,056 bits, approximately 4.77% of its rounded byte size). Against the earlier 7,944-byte fixed-width full indexed representation, the saving is 2,808 bytes (35.35% of that rounded total). All sizes refer to the **same declared indexed fixed-field payload**; none includes fixture bytes, Python interpreter memory, startup cost or external file metadata.

| B | New bits | Packed bytes | Maximum earlier tags parsed for one size |
|---:|---:|---:|---:|
| 8 | 46127 | 5766 | 7 |
| 16 | 43247 | 5406 | 15 |
| 32 | 41807 | 5226 | 31 |
| 64 | 41087 | 5136 | 63 |
| 128 | 40735 | 5092 | 127 |
| 256 | 40559 | 5070 | 255 |
| 512 | 40463 | 5058 | 511 |

Proof of semantics: each decoded size s_i is exactly its former unsigned integer, since the new prefix tag only identifies its former payload width. Consequently the preorder subtree remains [i,i+s_i). Child enumeration still advances from i+1 to the parent's end by c <- c+s_c, retaining every incoming operation label and source path. Terminal ranks and q-filtered wavelet matrix intervals depend only on the identical preorder structure, source terminal bitvector and immutable suffix. Thus for each prefix p and allowed real parameter r, the exact previously established C_p(r) follows with the identical arithmetic and observer.

The worst-case number of preceding codewords scanned per size query remains B-1. Codeword bit work changes with the Huffman lengths; full-query timing has to be measured on the same original corpus and workload.

## Verification and status

Two distinct validation scopes are preserved:

1. **Executed in this session**: VERIFY_HUFFMAN_ARITHMETIC.py checked the integer/Huffman formula, the full exact byte counts for B in {8,16,32,64,128,256,512}, and 2,880 codec round trips for each stride using a deterministic synthetic value sequence with the **same four width frequencies**. Exact program output is captured in EXACT_OUTPUT.txt; the passing line is PASS_R5_HUFFMAN_ARITHMETIC_SYNTHETIC_2880. This is a complete check of the tag codec and bit accounting under those input class counts.
2. **Published source for original-corpus execution**: VERIFY_HUFFMAN_WIDTH_FULL.py imports the pinned prior full exact R5 corpus verifier from the stacked ancestor and adds new packed-stream decoding, all 2,880 node size checks for every stride, recovery of the original 1,065 labeled paths, and 57,600 prefix-parameter comparisons against the prior exact query. As of this draft, this branch-level integration program has not been independently executed from the immutable remote checkout; its PASS line is an expected assertion, **not an observed run result**.

The frequency vector and original query verification are sourced from the previous committed and connector-read original-corpus evidence; this session independently recomputed the proposed codec arithmetic and synthetic round trips. The live R5 formal task owner/CLAIM and native research registration must be resolved from their original control receipts; this note is source material and author research, not a formal Result or independent mathematical review.

## Next scientific test

Run the published full-corps verifier against the exact stacked source and obtain the true output. Then compare B=16/32/64 Huffman and old two-bit tags with the same 1,065-word input, the same 57,600-query workload, direct packed decoding (not only pre-expanded Python lists), construction CPU, wall latency and peak resident heap, while preserving the original immutables. Test whether a two-level block-group code with partial local index can improve the time/space frontier without sacrificing exact subtree navigation.
