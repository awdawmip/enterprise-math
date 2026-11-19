# PREFIX-936 — complete sevenfold-origin named-XOR collision census and priority-disjoint union

2026-11-19 (Asia/Shanghai). Independent auxiliary observer research, continuing PREFIX-935. Researcher contribution: EM-DIRECT-58C410; original SID MCP-31edc522830749ad8775ca012e02ef30 (historical authenticated registration; this document does not claim shared TASK ownership). Frozen scientific input \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; no input rebasing. Status: AUTHOR_PROVED / TWO_INDEPENDENT_EXACT_COMPUTATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Exact theorem

Let \`N=2^32\`, \`Q={262145,262147,...,524287}\`, \`|Q|=131072\`. Retain source-labeled traces \`F_x^i=(x,x XOR 2^i)\`, for \`0<=x<N\`, \`0<=i<32\`, and the ordered observation \`Phi_(a,b)(u,v)=(u mod a,v mod b)\`. Define the k=7 certificate \`W7\` by the existence of \`0<=i,j<=18\` and positive integer \`t\` such that

    ((7*a) XOR 2^j) - 2^i = t*b,   (a,b) in Q^2.

Every \`(a,b)\` in W7 has a legal, different-start named collision:

    F_0^i = (0, 2^i),      F_(7a)^j = (7a, (7a XOR 2^j)).

The first readings are \`0 mod a\`; the terminal readings differ by \`t*b\`. Their source histories and named bit indices are not merged or discarded. For the specified \`a\`, the terminal value is positive and less than \`N\`.

## Proof of exhaustive finite quotient range

For all \`a in Q\`, \`7*a >= 1,835,015\`. Flipping \`2^j\` shifts the integer by exactly \`±2^j\`, with \`2^j<=262144\`, while \`2^i<=262144\`. Hence

    0 < 1,310,727 <= D := (7a XOR 2^j)-2^i <= 3,932,152.

As \`b>=262145\`, \`D=t*b\` forces \`1<=t<=14\`, since \`15*262145=3,932,175\`. Exhausting \`a\` over every odd modulus in Q, \`i,j=0..18\`, and \`t=1..14\`, with exact divisibility and range/parity tests, therefore exhausts W7 **as defined**, not an arbitrary subset. This exhaustiveness makes no claim about all possible named-XOR collisions.

## Exact enumeration

The scalar C++17 enumerator sweeps \`(a,j,i,t)\`. Independent Python/NumPy vectorization instead sweeps \`(j,t)\` and evaluates all \`(i,a)\` at once, then independently reconstructs previous-certificate membership. Both perform integer operations and yield byte-identical sorted little-endian uint64 IDs

    id = ((a-262145)/2)*131072 + ((b-262145)/2).

Raw parameter witnesses: **17,671,889**. Distinct W7 pairs: **14,698,334**, 117,586,672 bytes, SHA-256 \`8405169b6adaf6409e2355c4d65e8616176b413e8605ed76a40c6f1cf2f77d77\`.

Raw counts by \`t=1..14\`:
\`[0,0,12483,177885,3786131,567983,6930756,500901,3306017,265890,1598406,109225,416212,0]\`.

All overlaps are **priority-disjoint** in this exact order, reusing precisely the frozen PREFIX-935 predicates and sorted sets:

| Earlier certificate | W7 members assigned here |
|---|---:|
| B/Z/S (capacity, zero trace, same-start) | 7,132,689 |
| U (PREFIX-928 original all-bit set) | 3,778 |
| V (104 complete rows, highband and transposes) | 30,562 |
| W2 | 1,020,355 |
| W3 | 266,727 |
| D4 | 462 |
| W5 | 882 |
| D6 | 204 |
| **NEW beyond all eight preceding classes** | **6,242,675** |

The entries total 14,698,334 exactly. The new-only ordered-ID file contains 6,242,675 values, 49,941,400 bytes, SHA-256 \`4b9accdd187203f3a778b8a235fb0bf144f0658931eb6e27d1628965d8d51ee8\`.

Thus the certified union rises from 7,538,643,174 to **7,544,885,849**, leaving **9,634,983,335** pairs in Q² outside precisely these certificates.

First lexicographic NEW pair: \`(a,b)=(270989,523081)\`, \`i=16,j=18,t=3\`. The traces are \`F_0^16=(0,65536)\`, \`F_(7a)^18=(1896923,1634779)\`. Check \`7a=1896923\`, \`1896923 XOR 262144=1634779\`, \`1634779-65536=1569243=3*523081\`. Both endpoints are <2^32 and first residues both zero.

## Reproducibility and exact scope

Existing input set IDs and their validated sizes are reused without reclassifying scientific authority: U=5,295,478 (SHA-256 \`15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad\`), W2=30,211,412, W3=19,413,088, D4=1,793,182, W5=15,406,809 (SHA-256 \`ed2ff4c1961e29a619ccb404e834150028b4a689d5816ae03b2fa41fbc49de95\`), D6=1,771,013 (SHA-256 \`718e94ea98ba2931760b473a04eaf38ef189b4444548d9160ab5d861d1fc9c60\`). The two executed implementations and their original stdout, full sorted sets and SHA-256 are preserved in the reproducibility bundle; the published computation uses exact 64-bit integer IDs, not floating-point or random sampling.

The predicate for B/Z/S is the exact previous \`b < 33 ceil(2^32/a)\` or symmetric form, a known same-start bit port, or \`lcm(a,b)<2^32\`; V uses the exact 104 source-labeled complete rows, 1024 highband seeds (with first endpoint >=500001), and their transposes. No new certification of all remaining pairs is claimed.

## Next research frontier

1. Because 8=2^3, prove the k=8 internal two-flip condition reduces to the already-counted k=2 case; enumerate the low-bit boundary only.
2. Deduplicate that boundary against the union including W7 and then examine k=9 or a symbolic odd-core reduction.
3. Distinguish auxiliary observer collision obstructions from any native X6/BRC task ownership and proof-admission results.

Mother question \`B_fix,odd(32) in {19,20}\` remains open. Source publication, Activity association, shared CLAIM, Result and independent review are separate records.
