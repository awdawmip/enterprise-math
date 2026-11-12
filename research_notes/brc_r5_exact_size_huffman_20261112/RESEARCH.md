# R5 exact-subtree-size canonical Huffman index: full-corpus verification

Date: 2026-11-12. Scope: the immutable R5 28-coordinate / 15-operation auxiliary model and the 1,065 minimal legal double-zero certificate paths. This is independent author-side mathematical/tooling research, not a formal Source Result or an independent Driver review. The branch inherits Draft PR #2171 solely as the pinned verification ancestry.

## Theorem and constructive proof

The 1,065 legal paths yield a deterministic labeled preorder trie with 2,880 nodes. For every node v, let s(v) be the size of its preorder subtree. The previously verified 4-class width-prefix representation encodes those integers in 11,380 bits, before its 45*16-bit stride-64 offset directory and its unchanged 28,987-bit wavelet/rank/label suffix.

On this **exact frozen corpus**, the sizes take exactly 78 distinct positive integer values (largest 2,880), with frequent counts including s=1:1,056, s=2:793, s=3:333, s=4:197. Use a binary Huffman tree for the *exact size symbols* rather than for their four width classes. Stable tie resolution and canonical reindexing by (codeword length, numeric size) produce a reproducible prefix-free code. The complete weighted codeword sum is **8,472 bits**, with maximum codeword length 12. Ordinary Huffman sibling contraction gives minimum weighted code length for this exact 78-symbol distribution when codebook cost is excluded.

To make the representation independently decodable, store the full canonical codebook as (i) a 7-bit distinct-symbol count, followed by (ii) 78 sorted pairs of 12-bit size and 5-bit code length. This is exactly 7+78*(12+5)=**1,333 bits**. All sizes fit 12 bits and all lengths fit 5 bits. At stride B=64, 45 offsets each use 16 bits; every code offset is below 65,536. The remaining suffix remains bit-for-bit unchanged.

Thus the full self-describing fixed-corpus index at B=64 is:

```
1,333 bits  self-describing canonical Huffman dictionary
8,472 bits  exact-size encoded preorder stream
  720 bits  45 x 16-bit stride-64 bit offsets
28,987 bits unchanged label/terminal/q/wavelet/rank suffix
---------
39,512 bits = 4,939 bytes
```

The previous four-class Huffman representation uses 41,087 bits, 5,136 bytes on the same accounting basis. The new construction saves 1,575 bits or **197 packed bytes (3.84%)**. The size stream saves 2,908 bits before charging its new 1,333-bit dictionary. For stride B in {8,16,32,64,128}, its exact total is 38,792 + 16*ceil(2880/B) bits, giving packed byte counts {5,569; 5,209; 5,029; 4,939; 4,895}. This is a finite, concrete time-space option, not a universal lower bound for all encoders.

Decoding retrieves the canonical codebook from serialized bytes and decodes each subtree size from its nearest stride offset. The decoded integer is exactly the original s(v). Hence all preorder subtree intervals [v,v+s(v)), child transitions, terminal ranks and q-filtered wavelet ranges are unchanged. At every valid parameter r, the exact original activation count C_p(r) follows by equality of these observer inputs. This is an exact functional equivalence proof for the frozen certificate set.

## Evidence and check coverage

A standalone independent local Python stdlib reproduction reconstructed the original 28 coordinates, 15 atoms and all 32,768 subsets from the immutable source parameters, selected all 1,065 shortest eligible word masks with exact Fraction prefix legality, rebuilt the 2,880-node trie, serialized the full 28,987-bit suffix and exact-size codebook, and decoded **all 2,880 sizes** for each of 5 strides. It also checked **57,600 exact prefix/parameter activation comparisons** against individual certified words and a separately reconstructed wavelet query. The local run observed `PASS_R5_CANONICAL_EXACT_SIZE_HUFFMAN_FULL_FROZEN_CORPUS`, with actual numerical record `LOCAL_REPRODUCTION_OUTPUT.txt`.

`VERIFY_EXACT_SIZE_HUFFMAN.py` is the portable, source-pinned full-corpus verifier published with this note. It independently checks canonical dictionary recovery, packed stream decode, and 57,600 fresh direct-word comparisons, importing the existing pinned R5 source code. Its own remote-byte execution is a follow-up independent check; the local observed record comes from an independently written, standalone reproduction, not from claiming to have run this GitHub file.

## Source pins and remaining experiment

Original 15-operation/28-coordinate fixture: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551:research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`. Legal-path selection and order: `@ad7013218d0474e1e942906e3beadec1eccb9213:research_notes/brc_r5_dual_zero_right_persistence_20261112/VERIFY_TRIE_CODEC.py`. Full existing indexed stream: `@1ea46723f2d7db2702c63dc35e644cfe83266568:research_notes/brc_r5_variable_skip_full_20261112/VERIFY_R5_VARIABLE_SKIP_FULL.py`. Immediate four-class Huffman ancestor: `@ab6b76d463d823de3fd4f9184a99117ff4d89419`.

Next: execute the published portable verifier independently from exact immutable bytes; benchmark B=16/32/64 against the preceding four-class code with an identical full query workload and report CPU, wall time and peak memory including dictionary reconstruction. Explore a two-level compact codebook or direct rank/select over exact-size classes. Formal R5 Task/CLAIM ownership and result acceptance remain separate control questions.
