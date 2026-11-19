# PREFIX-943 — Full-prior-union exact W13 noninjectivity census
Date: 2026-11-20 (Asia/Shanghai). Lane: Enterprise Math / R6 portable direct auxiliary research. Scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged). Scientific status: AUTHOR-PROVED / EXACT-FINITE-COMPUTED / TWO INDEPENDENT COMPUTATIONAL PATHS AGREE / NOT MATHEMATICALLY INDEPENDENTLY REVIEWED / NOT ADMITTED. This is the auxiliary named XOR two-port observer, not a native X6/BRC dynamical theorem. It preserves names of source events and the pair of observation ports.

## Exact scope and new result

Fix `L=262145, H=524287, Q={L,L+2,...,H}` with `|Q|=131072`, endpoint bound `N=2^32`, and named bit indices `0<=i,j<=18`. Define `F_x^j=(x,x XOR 2^j)` and `Phi_(a,b)(u,v)=(u mod a,v mod b)`. For `k=13`, let `W13` be the set of ordered `(a,b) in Q²` for which there exist i,j and positive integer t satisfying

`(13*a XOR 2^j)-2^i=t*b`.

Every such pair yields the distinct legal paths `F_0^i` and `F_(13a)^j` with identical two-port readings. Starts agree modulo a because 13a is divisible by a; endpoints agree modulo b by the displayed equality. Both endpoints are below 2^32 since 13H+2^18<2^32. The witness search is complete: each `D=(13a XOR 2^j)-2^i` is computed exactly and `ceil(D/H)<=t<=floor(D/L)` enumerates all positive t with candidate b in Q. No floating point, sampling, or source-bit-name collapse.

Let `P12` be the previously reported global union through PREFIX-940 (all B/Z/S/U/V/W2/W3/D4/W5/D6/W7/D8/W9/D10/W11 certificate families). Its verified historical cardinality, reused as a frozen predecessor fact, is `|P12|=7,558,699,988`. This checkpoint computes the exact *new* family increment `W13\P12` using its precise prior predicates and sorted sets.

**Exact result:**

- Raw distinct parameter witnesses (a,b,i,j,t) for k=13: **16,796,156**.
- Distinct ordered modulus pairs `|W13|=12,993,739`.
- `|W11 intersection W13|=134,197`.
- `|W13\P12|=5,826,892`.
- Updated certified union size: `7,564,526,880` of `131072²=17,179,869,184` ordered pairs.
- Remaining outside this finite certificate union: `9,615,342,304`. Those outside may admit other noninjectivity witnesses; "not covered by these families" is the exact inference.

## Disjoint priority partition of W13

The following ordered buckets apply first-match classification, making every count disjoint. BZS is the combined original arithmetic/small-residue predicates, U is the 5,295,478-element PREFIX-928 ID set, and V is the previously specified exceptional-residue rule. All later W/D labels are historical sorted ID sets, and W11 is the previous odd-core set.

| Priority bucket | Exact unique-pair count |
|---|---:|
| BZS | 6,526,046 |
| U | 2,242 |
| V | 25,712 |
| W2 | 501,872 |
| W3 | 104,480 |
| D4 | 123 |
| W5 | 846 |
| D6 | 728 |
| W7 | 1,268 |
| D8 | 168 |
| W9 | 1,706 |
| D10 | 262 |
| W11 | 1,394 |
| **NEW13** | **5,826,892** |
| **Total W13** | **12,993,739** |

**Partition proof:** For any `p in W13` take the least index in the ordered family of predicates true at p, or NEW if none. This produces a disjoint, exhaustive partition of W13. Each predicate is deterministic on (a,b); exact counting consists of lexicographically sorting and deduplicating pair IDs, then applying those predicates in order. The previous P12 union is precisely the logical OR of those predicates/sets as specified in the predecessor code; consequently NEW is exactly `W13\P12`. The old full-union count is an inherited predecessor certificate, not independently recounted across all 17.18 billion pairs here.

## First genuinely new witness

`a=271267, b=522505, i=3, j=17, t=7`.
`13a=3526471`, `13a XOR 2^17=3657543`, and
`3657543-8=3657535=7*522505`.
Thus `(0,8)` and `(3526471,3657543)` are distinct legal named histories with identical `Phi_(a,b)` observations. Their shared observation is `(0,8)`.

## Independent exact verification

1. C++17 scalar implementation enumerated all 131072 values of a, all 361 pairs of source bits, and the provably complete t interval. It sorted/uniqued 16,796,156 raw witnesses and streamed each resulting ID past ten frozen historical ID sets plus independently generated W11, applying BZS/V predicates. It also reproduced the earlier raw W11 count, unique W11 count and W11 intersection W13.
2. Separate NumPy integer-array implementation independently generated W11, and independently generated the full sorted W13. Its W13 bytes matched the C++17 output exactly. It calculated BZS/V with vectorized exact-integer operations and checked old set membership using `searchsorted`, yielding exactly the same fourteen priority counts. The NumPy NEW13 SHA-256 matched the C++17 NEW13 bytes.
3. Inputs were extracted from the earlier immutable-user-provided `PREFIX939_R6_full_reproduction_bundle.zip` and all ten input SHA-256 values matched its original `SHA256_MANIFEST.json`. This preserves frozen scientific inputs without treating current behavioral-policy head as a mathematical input change.

Important evidence:
- `W13.bin` sorted uint64 little-endian pairs, size 103,949,912 bytes, SHA-256 `cca46c6869592a231c694d2d221f91ace3ec8043873c29cfbc5a1a1029dd7adc`.
- `NEW13.bin` sorted uint64 little-endian pairs, size 46,615,136 bytes, SHA-256 `7bf2c2654405ffe78029a3958c8679923f3f3a576fd9f30755b30c5cee355d37`.
- Pair ID formula `id=((a-L)/2)*131072+(b-L)/2`, no duplicates.
- Primary C++17 and independent NumPy counting sources and their machine-readable results are published next to this paper. Full binary arrays, frozen input references and checksums are preserved in the user-facing reproduction archive.

## Control, provenance and next scientific question

Original R6 provenance: researcher `EM-DIRECT-58C410`, SID `MCP-31edc522830749ad8775ca012e02ef30`, Activity `RA-25432C4AAE9BF66A907F5115`. Source-level paper publication does not grant a shared CLAIM, formal Task Result, independent review, or theorem admission. Shared X6 continuation request `r6-20261120-0058-x6-current-owner-read` was RUNNING when last observed; no mutation or owner takeover attempted. The mother question `B_fix,odd(32) in {19,20}` stays open.

The next high-information independent unit is the k=15 and k=17 full-prior-union comparisons (existing exact raw counts 20,708,178 and 19,318,164), and a method to count distinct union pairs from modular cells without materializing every candidate ID. These can be advanced without resetting PREFIX-943 or republishing any old inputs.
