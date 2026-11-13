# R5 — Exact enumerative compression of the frozen checkpoint-center gaps

Date: 2026-11-13. Status: author-side proof and executed exact finite tests, **not a formal Task Result or independent review**. Frozen scientific input commit: 435e77af0d180eac32bd1f9c4c464bc4010b7551 (unchanged).

## Exact source and scientific scope

The original frozen auxiliary certificate query uses 28 rational coordinates, 15 labeled operations, 1,065 activation certificates, 953 distinct rational activation thresholds, and a 2,520-byte original certificate seed. This result changes only the optional checkpoint-center cache. It does not repin the original input, modify certificate identities, ordered branches, event multiplicity, activation criteria or BRC residual semantics.

Immediate predecessor: Draft PR #2232, immutable commit 1353a03177bb2c095495ce0de22d9bdedcc5dddb, research_notes/brc_r5_radius_gap_codec_20261113/R5_CENTERS_56B.hex. The 56 decoded bytes have SHA-256 bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326 and derive from the real predecessor 1,382-byte sidecar in Draft PR #2227. The predecessor's bytes were read from GitHub and the exact 56-byte value supplied to the executed regression program.

The decoded centers have K=213, first s_0=1, last s_212=952. Their 212 positive gaps have alphabet {3,4,5}, respective counts (16,77,119) and total span 951. This particular frozen list is a known radius-2 cover in the predecessor's stated scope. The proof below concerns **losslessly reconstructing its center indexes**, not reconstructing the full activation count array E(b).

## Theorem 1: exact fixed-histogram rank coding

For an ordered alphabet with prescribed nonnegative symbol counts c_1,...,c_q totaling n, the exact number of words having these counts is

\[
 M=\frac{n!}{\prod_{j=1}^{q}c_j!}.
\]

Order such words lexicographically. There is an exact bijection to the integers 0,...,M-1. In particular, for c=(16,77,119), n=212, the cardinality M is

27954562172850508443296387793405995252390774025479430615209789826152785664016000,

with bit length 264. Therefore an injective *fixed-width byte encoding of every word in this particular histogram class* requires at least 33 bytes and 33 bytes suffice. This is not an unconditional lower bound over checkpoint lists additionally constrained by the actual E(b), nor over the one already known frozen sequence.

Proof by constructive prefix partition: with t positions remaining, remaining multiplicities c_j and m permissible suffix words, the number beginning with symbol j is exactly m*c_j/t. These are nonnegative integers whose sum is m. Ranking adds the sizes of all prior lexicographic prefix blocks and then restricts to the actual symbol's block. Unranking locates the unique consecutive block containing its current rank, subtracts its offset, consumes the corresponding symbol, and repeats until the word is exhausted. At each stage the blocks are disjoint and exhaustive. Induction on t proves that rank and unrank are mutually inverse. The pigeonhole bound requires at least ceil(log_256 M)=33 bytes for this declared source class; representing the rank as a 33-byte big-endian integer attains it.

The 33-byte format treats K=213, initial center s_0=1, and counts (16,77,119) as known decoder parameters. Their availability is an input contract, not implicit compression for arbitrary center arrays.

## Theorem 2: exact fixed-span rank without histogram input

For gap words in {3,4,5} of length n and total sum L, suppose the symbol counts are a,b,c. They satisfy

\[
 a+b+c=n,\quad 3a+4b+5c=L,\quad b=5n-L-2a,\quad c=n-a-b.
\]

Define the exact number of words in this fixed-span class by

\[
 T(n,L)=\sum_{\substack{0\le a\le n\\ b,c\ge0}}\frac{n!}{a!b!c!}.
\]

Order admissible histograms by increasing a and, within each histogram, use the lexicographic order of Theorem 1. The global rank is the sum of multinomial cardinalities of preceding histogram blocks plus the fixed-histogram rank of the word. Conversely, an integer in [0,T) belongs to exactly one of these consecutive histogram blocks and the preceding unranking procedure reconstructs the corresponding word. This establishes a bijection including repeated symbols, unbalanced counts and the empty-word case.

For n=212 and L=951, there are 55 possible nonnegative histograms. T is

43238460278605276751226501913190848199841244337559724275404587140697800213579145152,

which has bit length 275. Exactly **35 fixed bytes** suffice, and fewer cannot encode all words in this declared full fixed-span class. The decoder no longer needs the 16/77/119 histogram, but still needs n=212, L=951, the allowed gap alphabet and initial center 1. Neither theorem claims a 33/35-byte information lower bound for the narrower family of radius-2-valid checkpoint covers for the particular rational-source E.

An optional 37-byte derivative record stores four one-byte fields (K, first, c3, c4) followed by the 33-byte rank, with c5=K-1-c3-c4. Its 37-byte size is for the **actual observed histogram**, not a universal capacity for arbitrary 213-gap alphabets.

## Exact equivalence and validation

The executed Python standard-library verifier decodes and checks the prior GitHub-published 56-byte value, recovers 213 indexed centers, and checks s_0=1, s_212=952 and the exact histogram. It creates the 33-, 35- and 37-byte derivative encodings, then independently decodes all three and compares **all 213 center integers** with the predecessor. The input is not a fabricated center list.

For independent finite algorithm validation, all 9,841 ternary words with lengths 0 through 8 were exhaustively enumerated. Every word passed both fixed-histogram rank/unrank and fixed-span rank/unrank. Four invalid rank boundary cases were rejected. The exact rank byte strings and SHA-256 values are preserved in EXACT_OUTPUT.json. The test script is VERIFY_R5_ENUMERATIVE_CODEC.py, and in a stacked checkout it reads the actual prior hex directly from the adjacent PR #2232 directory.

The local 11-round CPython microbenchmark measured approximately 24.969 microseconds per 56-byte prior decode, 80.502 microseconds per 33-byte fixed-count unrank, and 454.541 microseconds per 35-byte fixed-span unrank. These are local function-level measurements from the executed verification program; values may vary across implementations and hosts. The GitHub-published portable script is separately reproducible but is not claimed to have been re-executed from its remote blob in this run.

### Storage and performance interpretation

Compared with the 56-byte optional prior center encoding, the 33-byte rank is 41.07% smaller; the 35-byte fixed-span rank is 37.50% smaller; the 37-byte header alternative is 33.93% smaller. Original seed plus optional center payload: 2,553 bytes (33-byte rank), 2,555 bytes (35-byte rank), or 2,576 bytes (56-byte prior). No claim is made that E, checkpoint bitmaps, the old 954-entry direct-address directory, hashing or runtime object memory fits in these totals. In particular, the original scientific seed and all full rational input reconstruction costs are unaffected.

The new encodings are a **precise persistent-space versus cold-decode-time tradeoff**; none proves faster queries or a universally smaller complete in-memory representation. Existing predecessor claims that a radius-2 set and 1,070 total event correction count are valid are reused as published input claims; this unit did **not** reconstruct E from its frozen original corpus, rerun the 2,747,520 boundary-prefix comparisons, or independently reprove the predecessor's optimum.

## Scientific status and recovery

Proved: both finite enumerative bijections, conditional fixed-width byte capacity bounds for their exact word classes, and the preservation of the 213 indexed centers under the implemented encodings. Executed: exact frozen-predecessor sidecar conversion and 9,841 exhaustive small-word cases. The result remains an author-side independent scientific derivative, not a formally admitted EM Task Result, not independent reviewer approval, and not native X6 Foundation promotion.

Next decisive unit: reconstruct cumulative event array E(b) from the original 435e77... pinned science in an independently checked environment, use the 35-byte codec to recover 213 centers, rebuild the O(W+K) nearest-center directory and bitmaps, and compare all original rational boundary-prefix counts. Measure end-to-end seed decode, bitmaps, cold peak RSS, query work and serialization under equal total-memory budgets. Keep R5's frozen scientific pins and current actual owner/CLAIM separate from this derivative research record.
