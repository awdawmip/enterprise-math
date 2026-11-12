# R5: exact 2,520-byte reconstructible BP certificate index

Date: 2026-11-12 (Asia/Shanghai). Status: author-side theorem and exact synthetic checks. Frozen external P/Q–BRC Blackwell 28-coordinate, 15-labeled-atom auxiliary model. This is not a new native-X6 claim.

## Frozen inputs and provenance

- The original 28-coordinate atoms and legal-word selection are fixed at enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551 and the exact words at @ad7013218d0474e1e942906e3beadec1eccb9213 (VERIFY_TRIE_CODEC.py).
- The full 2,880-node BP/Wavelet frozen-corpus validator is @eb3a80abe45ddd2305c7a0247a45eeba9bef04d3.
- Immediate predecessor: Draft PR #2176, commit 7ea3e43a4621ac5700dede72f1a1985b163368e5, 4,441-byte indexed payload (35,521 bits). Its 28,987-bit suffix consists of complete terminal/q/wavelet/rank auxiliary fields, each deterministically constructible from the original labeled terminal paths.
- Preserve all original scientific pins. Here we change only storage and deterministic initialization.

## Theorem: recoverable-index factorization

Fix a finite rooted trie of ordered distinct atom-label paths with N nodes, labels in {1,...,15}, and terminal flags. Let BP be its 2N-bit depth-first balanced-parentheses word (1=open); let edge labels be a 4-bit sequence ordered at the opening of each nonroot node; let TERM be the N preorder terminal bits. Assume an externally fixed immutable port table of integer coefficients W_a, K_a, and that every terminal path p has n(p)=-sum_{a in p} W_a > 0 and q(p)=-sum_{a in p} K_a / 36 in {3,12,15}, with the division exact. This is satisfied by the frozen R5 corpus, as checked in the pinned prior validators.

Then the concatenation BP || LABELS || TERM suffices to deterministically rebuild: (1) the entire labeled ordered trie, all node subtree lengths, and every selected terminal word; (2) every (q,n) pair, its terminal-class masks and the three stable-partition Wavelet matrices; (3) the Wavelet and bitvector rank directories, and any BP block-minimum / sparse opening-rank auxiliary arrays. Consequently the exact arbitrary-prefix activation count can be answered with the same reconstructed indexed query algorithm as the 4,441-byte predecessor, including exact rational r.

Proof: A balanced-parentheses word uniquely determines the rooted ordered tree. Each nonroot open consumes one label, so by a stack traversal LABELS uniquely reconstructs the ordered paths; TERM chooses the terminal nodes. At each terminal, accumulate fixed W,K along its path, giving the unique exact pair. The preorder terminal sequence is thus determined; for each q, stable-filter n, then apply the deterministic bitwise stable partitions to obtain each Wavelet level. Every rank directory is a deterministic prefix sum of its derived bitvector. BP local minimum depths and opening ranks are likewise functions of the BP bits. Finally every node subtree forms a contiguous preorder interval; the terminal ranks give its terminal interval. The previously proved cutoff n <= floor(36q/(1-23r)) (for r<1/23), together with the zero-scale convention at r=1/23, yields the same C_p(r). No information from the removed fields is needed at query time after initialization.

For N=2880 and E=2879, the actual fixed-model representation is:

| Persisted field | Exact bits |
|---|---:|
| BP topology, 2N | 5,760 |
| Four-bit labels, 4E | 11,516 |
| Terminal bits, N | 2,880 |
| **Total** | **20,156 bits = 2,520 packed bytes** |

The previous full 4,441-byte indexed payload has 35,521 bits. This representation saves 15,365 bits of derived fields and 1,921 packed bytes (about 43.26%). The older LOUDS unindexed certificate payload had 20,155 bits, also rounding to 2,520 bytes; our BP layout is a distinct, reconstructible query-index seed. Model constants, stream dimensions, self-description, decoder, and execution code are external fixed-model knowledge and are not billed as part of these 2,520 bytes. For a generic self-describing format they must be included.

Initialization takes O(N+E+M log U) unit-cost word operations to traverse the trie, recover M terminals, construct three integer Wavelet matrices (U bounding n) and build ranks, plus the selected BP-navigation block scans. The original fast query behavior can then be retained at the cost of the reconstructed runtime arrays and a one-time build. This result establishes an exact *serialized-input versus initialization* tradeoff; it makes no claim of reduced initialized heap or latency. If the immutable port table changes or is unavailable, its bytes must be restored/reaccounted.

## Evidence and checks

Executed locally using Python stdlib:
- VERIFY_R5_DERIVED_BP_DIRECTORIES.py: all 2,056 rooted ordered trees with 1..9 nodes, six (block width, stride) settings per tree, plus six configurations on a deterministic 2,880-node tree. 122,742 node navigation checks passed; reconstructing 90 minima and 12 anchors, and 4,344-byte intermediate BP+old-suffix bitstream, was verified.
- VERIFY_BP_TERMINAL_REGEN_SYNTHETIC.py: independent synthetic frozen-like three-port integer model, 198 terminal words and 235-node ordered trie. Pack/decode of BP+label+term, port recovery, reconstructed numeric Wavelet range counts vs direct prefix activation across 12,690 exact cases passed.
- VERIFY_R5_REBUILD_FROM_BP_LABELS.py: published integrated original-corpus checker (imports frozen stacked-branch verifier, rebuilds all fields from the new 2,520-byte payload, rechecks 57,600 prefix-parameter queries). Syntax checked locally. End-to-end execution against original immutable dependencies remains a distinct pending validation.

The first two executed programs are synthetic, not a substitute for the third original-corpus integration. The full proof assumes the previous R5 exact source/witness contract; independent mathematical review and formal Result intake remain governed by their existing Source roles.

## Next discriminating experiment

Run the published integrated checker on its stacked branch, compare its generated bitvectors and rank directories byte-for-byte to PR #2176, then measure fixed-query initialization time, steady-state complete latency and peak heap for 2,520-byte rebuilt vs 4,441-byte preindexed streams. Explore selective persistence of only the expensive derived fields (some Wavelet rows, sparse ranks) to obtain a practical Pareto frontier. Recheck current TASK owner and do not infer CLAIM from an author PR.