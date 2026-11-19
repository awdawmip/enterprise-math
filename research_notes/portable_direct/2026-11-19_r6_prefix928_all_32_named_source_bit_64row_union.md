# PREFIX-928 — All 32 named XOR source-bit mixed certificates across 64 odd-modulus rows

Date: 2026-11-19. Lane: 进取数论研究6. Type: independent auxiliary provenance-aware BRC observer research. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_INDEPENDENT_EXHAUSTIVE_ENUMERATION_ORDERS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

Frozen scientific input `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Exact prior frontier: PREFIX-927, `research_notes/portable_direct/2026-11-19_r6_prefix927_bits0to3_mixed_64_row_increment.md`, with 4-bit family count 1,091,862. Retain PREFIX-925's verified `|B ∪ Z ∪ S|=7,462,508,971`; this is the exact **old-family** union only.

## Statement, types and finite domain

Let `p=32`, `N=2^32`, `Q={262145,262147,...,524287}`, `|Q|=131072`, and `R={400001,400003,...,400127}` (64 fixed second-port rows). The **named** traces `Z_x=(x,x)` and `F_x^i=(x,x XOR 2^i)` retain the `Z/F` type, start x, and bit source label `0<=i<32`. The two-port observer is `Phi_(a,b)(u,v)=(u mod a,v mod b)`, where `a,b ∈ Q`.

For each bit `i`, define `T_i` as the set of ordered modulus pairs `(a,b)∈Q²` with a direct witness of one of the following two specific forms at a second modulus `b∈R`, **or the time-reversed swapped-port witness** at `a∈R`:

- For some `k>=1`, `A=ka<N`, `H=2^i`, `b|(A-H)`: `F_0^i=(0,H)` versus `Z_A=(A,A)`. Their common observation is `(0,H mod b)`.
- For some `k>=1`, `A+H<N`, `b|(A+H)`: `F_H^i=(H,0)` versus `Z_(A+H)=(A+H,A+H)`. Their common observation is `(H mod a,0)`.

Both witness pairs consist of distinct legal named traces. Time reversal maps `F_x^i` to `F_(x XOR 2^i)^i` and `Z_x` to itself; swapping ports therefore preserves equality of observations in the reverse orientation. This construction makes no claim of exhausting *all* possible mixed or double-flip collisions.

Let `B` be the two-sided bucket-capacity collision set (PREFIX-923), `Z` the `lcm(a,b)<N` zero-zero collision set (PREFIX-924), and `S` the same-start flip-source set with `2^d ≡ +/-1 (mod b)` for some `1<=d<=31` (PREFIX-925). These are **oriented** sets: in particular the `S` predicate is tested against the second modulus of each orientation.

## Theorem A — exact constructive enumeration

All pairs in `T_i` can be found exhaustively by visiting `b∈R`, `1<=k<=floor((N-1)/262145)=16383` and both signs. Since `b` is odd, every solution `b | (ka±2^i)` has `gcd(k,b)=1`. Write `v=k^{-1} mod b`. For the minus branch solve `a≡2^i v (mod b)`; for the plus branch solve `a≡-2^i v (mod b)`. Since `max(Q)-min(Q)=262142<b`, each congruence class contains at most one `a∈Q`. Check its odd parity and endpoints; then add the actual orientation and its transpose. All enumerated integer pairs are directly validated by the corresponding named traces.

Conversely each witness of either displayed form has a `k` within that bound, forces `gcd(k,b)=1` and must yield the unique listed `a`. Thus the enumeration is exact for these two templates, with no omission or accidental source-bit quotient. A second algorithm can instead iterate `b,a`, solve `k≡±2^i a^{-1} mod b` and require the exact `k<=floor((N-1)/a)` cutoff. These are distinct exhaustive parameterizations and both directly validate the real XOR endpoints.

## Theorem B — exact 32-bit net union

Define `U_j=((T_0 ∪ ... ∪ T_j) \ (B ∪ Z ∪ S))` for `0<=j<=31`. Independent exhaustive C++17 implementations (algorithm A iterates `(b,a)`, algorithm B iterates `(b,k)`) gave **identical** 32-by-32 bit-specific counts and progressive union counts and an identical ordered binary file of set members:

```text
|U_0| = 437,560
|U_3| = 1,091,862    (exactly PREFIX-927)
|U_7| = 1,933,241
|U_15|= 3,345,584
|U_23|= 4,461,579
|U_31|= 5,295,478
```

Encoding each ordered pair by `id=((a-262145)/2)*131072+(b-262145)/2` and serializing sorted IDs as little-endian unsigned 64-bit values yields exactly `42,363,824` bytes, with SHA-256

```text
15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad
```

Therefore the net **new** set of ordered pairs relative to the four-bit PREFIX-927 family has size `5,295,478-1,091,862=4,203,616`. Including the old three certified families gives

```text
|B ∪ Z ∪ S ∪ T_0 ∪ ... ∪ T_31| = 7,467,804,449,
|Q² \ (B ∪ Z ∪ S ∪ T_0 ∪ ... ∪ T_31)| = 9,712,064,735.
```

The second number is a remaining *certificate complement*, not an assertion that those observers are injective. Intersections with previously published other double-flip, generic mixed and complete-row witnesses have not yet been globally deduplicated.

Two explicit first-new-source examples, outside `B ∪ Z ∪ S` and all earlier `T_j` (`j<i`):

1. `i=4,(a,b)=(354255,400099),k=6179`: `F_0^4=(0,16)` versus `Z_2188941645=(2188941645,2188941645)`; both observe `(0,16)`. Indeed `2188941645=6179*354255` and `2188941645-16=5471*400099`.
2. `i=31,(a,b)=(354257,400121),k=1683`: `F_0^31=(0,2147483648)` versus `Z_596214531=(596214531,596214531)`; both observe `(0,34241)`; `596214531=1683*354257` and `596214531-2147483648=-3877*400121`.

The first-new-source property for these two examples follows from the complete 32-bit mask computed by independent algorithm B, rather than from checking only the displayed trajectory congruences.

## Reproducibility, verification and provenance

Source artifacts: `PREFIX928_R6_ALL32_BA_ENUM.cpp`, `PREFIX928_R6_ALL32_BK_ENUM.cpp` and `PREFIX928_R6_ALL_32_BITS_RESULTS.json` under `research_notes/portable_direct/`.

Compile each with `g++ -std=c++17 -O3` and run with a path for the sorted binary output. Compare all 32 printed lines, compare sorted output files byte for byte, and check the SHA-256 above. Each enumerator uses exact integer arithmetic, tests every actual witness endpoint, respects `N` at bit 31, and deduplicates oriented `(a,b)` pairs by their exact integer ID. No randomization, floating point or external libraries enter the computation.

The two locally executed enumeration programs agreed exactly. The large sorted-ID file is reproducible but is not uploaded to the GitHub Source repository because the two deterministic code paths and digest already provide its compact reproduction; it remains a local computed artifact. The JSON result contains the complete 32-line count series and provenance.

Limitations: no independently appointed mathematical review/admission; no proof of auxiliary-observer equivalence to the native X6 dynamics or native three-dimensional slice. Keep the current P000 six-dimensional discrete space, independent time, native 120° enterprise angle, signed-axis provenance and three-dimensional slice semantics unchanged.

Next discriminating unit: compute the **actual oriented-pair intersection** between this 32-bit set and older complete-row/double-flip certificate sets, or extend the exact row domain `R` without double-counting. Separately, search for surviving injective auxiliary observers and test typed transfer to the native X6 model. The mother target `B_fix,odd(32)∈{19,20}` remains open.
