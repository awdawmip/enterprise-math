# R5 — Exact 7,944-byte preorder-skip prefix activation index

Date: 2026-11-12 (Asia/Shanghai). Scope: frozen **external** P/Q–BRC Blackwell 28-coordinate / 15-labeled-operation auxiliary model; algorithmic extension of the selected dual-zero certificates. Author-side mathematical construction. Project P000/native X6 unchanged.

## Pinned predecessor inputs and distinct scope

- Original frozen mass and atom fixture: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551:research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`.
- Selected 1,065 ordered (q,n) certificates: Draft PR #2152 commit `ad7013218d0474e1e942906e3beadec1eccb9213` (VERIFY_RIGHT_PERSISTENCE.py, VERIFY_TRIE_CODEC.py).
- Predecessor BP/wavelet index: Draft PR #2161 commit `eb3a80abe45ddd2305c7a0247a45eeba9bef04d3` (RESEARCH.md, VERIFY_R5_BP_WAVELET_PORTABLE.py); reported 2,880 prefix nodes, 1,065 terminals, three q families of 538, 298 and 229 words and n-widths 10, 10 and 9 bits. Do not substitute current control HEAD for frozen mathematical input pins.
- Earlier stateful indexed trie comparison: Draft PR #2155 / `d37154e58cf971457da190d80a95d4ffdd72ee0c`, 8,210 logical packed bytes including prefix counters, for a different mutable-current-parameter workload.

The new result is **a fully specified size and query-cost construction conditional on the previously selected R5 word corpus**. The accompanying runnable checker exhaustively validates the generic representation on a separate, explicitly synthetic trie with the same shape and family cardinalities; independent execution on the frozen original word corpus remains a specific next check.

## Proposition: preorder subtree skips replace balanced parentheses plus close navigation

Take any rooted trie with N=2,880 preorder nodes, T=1,065 terminal words, distinct child labels from {1,...,15}, and the three fixed q-class cardinalities, widths and monotone activation formula in the predecessor. Number preorder nodes `0,...,N-1` and store `s[v]`, the number of nodes in the subtree rooted at v. Since `1 <= s[v] <= 2880 < 2^12`, every size has a 12-bit representation. Store the incoming edge label of every nonroot node in 4 bits and one terminal flag per node.

**Lemma 1 (interval/child recovery).** The nodes beneath v are precisely `[v,v+s[v])`. Its first child, if any, has number `v+1`; each next child follows the preceding child's entire subtree and is obtained by adding that child's `s`. The loop stops at `v+s[v]`. Hence a prefix of length k can be located by testing at most 15 child labels at each step, using O(15k) constant-width accesses, without `findclose`, BP matching, a parent array, or materialized terminal interval endpoints.

Proof: preorder completes each child subtree before the next child; the rooted subtree forms a contiguous block. Each direct child is the first node in its consecutive child block. Induction over children proves exact partition and enumeration. The invariant holds even if a terminal is an ancestor of another terminal.

**Lemma 2 (terminal/class range).** Let `rank_T(j)` count terminal flags before preorder node j. For v define `L=rank_T(v)`, `R=rank_T(v+s[v])`. These are precisely the terminal DFS ranks in v's subtree. Over the T terminal ranks, store q=3 and q=12 indicator vectors M3,M12; q=15 is their complement. Their family-specific subranges are
`[rank_M3(L),rank_M3(R))`,
`[rank_M12(L),rank_M12(R))`, and
`[L-rank_M3(L)-rank_M12(L), R-rank_M3(R)-rank_M12(R))`.
Both endpoints use only rank queries; each q-filtered sequence is stable relative to terminal DFS order.

**Lemma 3 (parameter query).** For all declared real `r<1/23` in the original allowed interval, and any selected prefix p, the count of activated certificates extending p is
`C_p(r)=sum_{q=3,12,15} WaveletCount_q(L_q,R_q, floor(36q/(1-23r)))`.
At `r=1/23`, the declared zero-scale endpoint convention counts all terminals below p. For rational `r=a/b`, `b>0`, compute each cutoff exactly as `floor(36qb/(b-23a))` using integer arithmetic. Proof: the predecessor wall `r >= (1-36q/n)/23` is equivalent to `n(1-23r)<=36q`; stable class filtering and wavelet range counting apply exactly.

## Rank directory (complete fixed-width serialization)

Represent each needed bitvector by its own contiguous bit array, 64-bit popcount blocks and 512-bit superblocks. For length m, let `B=ceil(m/64)`, `S=ceil(m/512)`. Store the accumulated global count at the beginning of all but the first superblock, each with `ceil(log2(m+1))` bits. Store the rank since superblock start at each non-first 64-bit block of a superblock, 9 bits per entry (the preceding block count is at most 7*64=448). Thus the directory uses exactly
`D(m)=(S-1)*ceil(log2(m+1))+(B-S)*9`
bits. For position k, add the superblock prefix, within-superblock block prefix, and the popcount of at most 63 trailing bits; total rank is constant time with a fixed-size 64-bit popcount primitive. A query at k=m is served by the total bitcount precomputed at load. This is a serialized field-layout model; loading and auxiliary in-memory allocations have separate resource cost.

Use one terminal-flag rank vector of m=2,880, two q-class rank vectors of m=1,065, and 29 independent wavelet row rank vectors: 10 rows length 538, 10 rows length 298, 9 rows length 229. For a row, zero counts are derived from its bitvector at load. A complete query needs at most `2*(10+10+9)+2+4=64` such rank evaluations, plus O(15k) prefix navigation and rational threshold arithmetic. With 64-bit popcount, each rank evaluation requires a constant number of integer operations; the bit complexity of arbitrary-size rational r still depends on numerator and denominator lengths.

## Exact packed-size accounting

| Component | Exact bits |
|---|---:|
| 2,880 preorder subtree sizes, 12 bits each | 34,560 |
| 2,879 incoming edge labels, 4 bits each | 11,516 |
| 2,880 terminal flags | 2,880 |
| Two class-membership masks, 1,065 bits each | 2,130 |
| Three wavelet matrices, 538*10+298*10+229*9 | 10,421 |
| Rank directory for terminal flags, D(2880) | 411 |
| Rank directories for two class masks, 2*D(1065) | 296 |
| Wavelet row directories, 10*D(538)+10*D(298)+9*D(229) | 1,333 |
| **Total** | **63,547** |
| **Single packed fixed-schema byte stream** | **7,944 bytes** |

This includes explicit random-access subtree traversal, q-class filtering, wavelet row rank support and terminal-rank support, unlike the earlier 3,823-byte core BP/wavelet payload that deliberately omitted navigation/rank auxiliary indices. Both have different fields. Compared with the earlier **8,210 logical packed bytes** stateful trie, this particular fully indexed *stateless historical-parameter count* representation is 266 bytes smaller, while serving a different workload; it does not establish a runtime-speed or general dominance result. Fixed schema and known dimensions are external to the quoted bitstream; runtime heap objects, executable, representation of the original frozen masses, and independent evidence ledger are additional costs.

## Executed checks and remaining scientific unit

The adjacent standalone JavaScript verifier creates a deterministic 1,065-terminal, 2,880-node **synthetic** ordered-label trie, constructs actual preorder subtree skips, 64/512 rank directory values, two q masks, and 29 wavelet rows with the published shape. It checks every rank boundary of every constructed bitvector; all 2,880 node subtree partitions and each direct child traversal; and compares wavelet prefix activation counts with direct exact BigInt threshold comparison for nine rational parameters at every node. Its output is recorded in EXACT_OUTPUT.txt. The test validates the representation and lookup theorem at that shape; it neither imports nor independently verifies the frozen 28-coordinate R5 certificates.

**Next:** instantiate this new index on the immutable original 1,065 selected ordered words, perform actual byte packing and decoding of all fixed-width fields, benchmark full build/lookup CPU and in-memory allocations against both the old BP/wavelet representation and the 8,210-byte active-counter trie under their separate workload contracts; then pursue independent mathematical review and formal Source binding when real TASK authority permits.
