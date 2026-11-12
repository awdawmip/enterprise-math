# R5 — Exact arbitrary-prefix activation via a balanced-parentheses / wavelet index

Date: 2026-11-12 (Asia/Shanghai). Mode: author-side mathematical derivation and finite exact test in the **external** 28-coordinate P/Q–BRC Blackwell auxiliary model. No native X6 lift or formal Result acceptance is claimed.

## Fixed provenance and scope

- Frozen original 15 labeled atoms and 28 mass coordinates: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551:research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`.
- Earlier scientific pins: account `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`.
- Existing minimal deterministic 1,065 selected `(q,n) -> labeled ordered word` certificates: PR #2152 / `ad7013218d0474e1e942906e3beadec1eccb9213`, `VERIFY_RIGHT_PERSISTENCE.py` and `VERIFY_TRIE_CODEC.py`, copied byte-for-byte to this source branch as executable pinned dependencies.
- Prior direct 283-byte **root-only** activation index: PR #2159 / `c15d631dac00b0dd553f757da4f28c71c8bf5a17`.

The previous certificates contain 1,065 different `(q,n)` pairs with `q in {3,12,15}`, each paired with one 28-coordinate prefix-legal word and an exact monotone activation wall
`tau(q,n)=(1-36q/n)/23`. This note uses their previously established legality and independently checks the new indexing and prefix counting claims.

## Proposition 1: arbitrary-prefix exact count

For any prefix `p` of a selected certificate, let `D_p` be the set of `(q,n)` whose selected ordered words begin with `p`. Let `I=[L,1/23]` with
`L=-427508577031693280/628800490619`. Define

```
C_p(r) = #{ (q,n) in D_p : r >= (1 - 36q/n)/23 }.
```

At `r=1/23` use the established zero-scale endpoint convention. For every `L<=r<1/23`, with `delta=1-23r>0`,

```
C_p(r) = sum_{q in {3,12,15}} count{ (q,n) in D_p : n <= floor(36q/delta) }.
```

**Proof.** Each pair activates iff `23r >= 1-36q/n`, or equivalently `n*delta<=36q`. Since `n` is a positive integer this is exactly the displayed integer cutoff. The three `q`-labeled families are disjoint. The endpoint follows from the inherited convention. This is an exact statement for real `r`; for rational `r=a/b`, `b>0`, the cutoff is `floor(36qb/(b-23a))`, calculated by integer division.

## Proposition 2: contiguous terminal rank intervals from BP topology

Construct the rooted trie of exactly the 1,065 words, with distinct atom labels `1..15`. Traverse it in preorder, visiting children in ascending label order, writing `1` on node entry and `0` on node exit (balanced parentheses, BP); also write the four-bit incoming edge label for each nonroot node and one terminal bit per preorder node. Every prefix identifies one node `v`. Its full descendant subtree is contiguous in preorder from the entry parenthesis to its matching exit parenthesis. Consequently its terminals occupy a contiguous interval `[lo(v),hi(v))` in the lexicographic DFS terminal sequence, obtained by ranks of the terminal flag over the node range.

**Proof.** Depth-first traversal completes all descendants before leaving any subtree and visits no external node between them. Terminal flags restricted to that contiguous node interval occupy exactly the terminals under the prefix. Preorder terminal rank before the node and after its closing parenthesis gives the two endpoints. No `2*11`-bit per-node terminal interval table is necessary in the serialized representation.

For each of the three `q` families, stable-filter the terminal sequence to its `n` values. Use the decoded word labels and frozen signed port coefficients `W,K` to obtain terminal `(q,n)` and rebuild family membership masks. A wavelet matrix on the integer `n` values supports `#{n<=t}` in any contiguous filtered interval using one descending bit traversal. Composition gives the exact `C_p(r)` query.

## Finite reconstruction and exact storage result

The full frozen corpus was reconstructed from all `2^15=32,768` masks and original 28-coordinate legality, using the exact predecessor's shortest-mask and deterministic ordered-prefix rule. Independent local scripts `VERIFY_PREFIX_WAVELET.py` and `VERIFY_PREFIX_BP_CODEC.py` rebuilt the corpus from exact rational input; the publication script `VERIFY_R5_BP_WAVELET_PORTABLE.py` imports the original pinned 28-coordinate verifier.

| Stream | Exact bits |
|---|---:|
| Balanced-parentheses topology: 2*2,880 nodes | 5,760 |
| 4-bit edge labels: 2,879 edges | 11,516 |
| Terminal flags: 2,880 nodes | 2,880 |
| Three wavelet matrices: 538*10 + 298*10 + 229*9 | 10,421 |
| **Packed indexed payload** | **30,577 bits = 3,823 bytes** |

This fixed-corpus payload excludes model constants, executable code, a generic decoder header, auxiliary bit-rank directories and reconstructed in-memory navigation tables. The previous 2,520-byte LOUDS representation stored only the words, while this new 3,823-byte representation additionally stores the three random-range-count wavelet matrices. It does **not** claim information-theoretic optimality or measured CPU speed.

A straightforward alternative using LOUDS plus two 11-bit terminal interval endpoints for each node, three `q` terminal-class bitmaps, and three wavelet matrices would consume `97,131 bits = 12,142 bytes` under its explicitly specified fields. BP removes the costly materialized interval table from this comparison.

## Decoder/correctness test

The new program serializes and reads back the actual bitstream; checks exact balanced-parentheses nesting, 2,880 decoded ordered prefix nodes and all 1,065 original labeled terminal paths; derives the `(q,n)` keys from frozen port sums; checks all wavelet row bits; checks exact `C_p(r)` at **all 2,880 prefixes for 20 rational parameter samples (57,600 comparisons)** and at the root for **all 953 event walls**.

Exact outputs include `C_empty(0)=605`, `C_empty(1/23)=1065`. The local execution passed with a local adapter that exposes the full independent 28-coordinate reconstruction. The publication code was syntax-checked and its Git blob matched the locally tested source; a second execution using the newly published pinned dependencies in a clean environment remains to be done.

With precomputed rank and parenthesis/navigation support, the algorithm uses three wavelet traversals of at most 10, 10 and 9 levels for each query, plus prefix-node lookup and class interval translation. Such runtime support has a memory/initialization cost not contained in the stated 3,823-byte packed payload; the reference Python implementation uses arbitrary-length integer `bit_count` on prefixes instead of a fixed-time 64-bit rank directory. Integer bit complexity also depends on input numerator/denominator length.

## Next unit

Measure the entire runtime representation (BP close/rank support, `q` class-rank support, wavelet rank directories), query latency and initialization cost against the prior 7,444-event-update/8,210-byte **indexed dynamic current-parameter** trie. Examine succinct BP `findclose` and `rank/select` indexes without losing reversible labels, and test scaling beyond 15 atoms while preserving complete observer/provenance typing. Compare the distinct query workloads: arbitrary historical `r` vs. one mutable current `r`.

**State:** standalone author-side exact finite algorithm/bitstream result; GitHub evidence publication is distinct from native activity/checkpoint, formal Source Result and independent mathematical review.
