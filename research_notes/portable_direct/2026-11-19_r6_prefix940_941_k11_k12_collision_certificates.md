# PREFIX-940–941: k=11 odd-core census and k=12 two-adic boundary

Research date: 2026-11-19. Scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Auxiliary *named XOR two-port observer*, not a native X6 result. Prior frontier: PREFIX-939 cumulative collision certificate union `7,552,811,074`. Historical provenance: Researcher `EM-DIRECT-58C410`, SID `MCP-31edc522830749ad8775ca012e02ef30`, Activity `RA-25432C4AAE9BF66A907F5115`. Mathematical status: `AUTHOR_PROVED / EXACT_FINITE_COMPUTED / INDEPENDENT_ENUMERATORS_AGREE / NOT_REVIEWED / NOT_ADMITTED`.

## Model and certificate correctness

Let `N=2^32`, `Q={262145,262147,...,524287}`, `|Q|=131072`. For legal named endpoint histories `F_x^j=(x,x XOR 2^j)` with `0<=x,x XOR 2^j<N`, the auxiliary ordered two-port observer is `Phi_(a,b)(u,v)=(u mod a,v mod b)`. For each `a,b in Q`, `0<=i,j<=18`, and positive `k`, define

`D_k(a;i,j)=(ka XOR 2^j)-2^i`.

If `b|D_k` and endpoints are legal, the two distinct named histories `F_0^i=(0,2^i)` and `F_(ka)^j=(ka,ka XOR 2^j)` collide: their starting residues modulo `a` both vanish, and the terminal residues modulo `b` coincide.

## PREFIX-940: exact full k=11

`11a` ranges from `2,883,595` to `5,767,157`. Thus `2,359,307 <= D_11 <= 6,029,300 < 23*262145 = 6,029,335`; testing every positive integer quotient `1<=t<=22` exhausts `D_11=t*b`. Enumerate all `131072*19*19` choices of `(a,i,j)`, invert the quotient, check `b in Q`, and sort/unique integer pair IDs `((a-262145)/2)*131072+(b-262145)/2`.

There are **16,974,425** raw parameter witnesses and **13,144,330** unique ordered pairs. The exact disjoint priority partition relative to the previously published B/Z/S, U, V, W2, W3, D4, W5, D6, W7, D8, W9 and D10 sets is:

| Priority source | Count |
|---|---:|
| B/Z/S | 6,510,937 |
| U / V | 2,356 / 25,991 |
| W2 / W3 / D4 | 711,646 / 765 / 283 |
| W5 / D6 / W7 / D8 | 768 / 501 / 710 / 414 |
| W9 / D10 | 942 / 103 |
| **New to the union** | **5,888,914** |

Hence cumulative union after PREFIX-940 is **7,558,699,988**. The first lexicographically new pair is `(a,b)=(272161,520807)`, with `i=0,j=17,t=6`: `11a=2993771`, `2993771 XOR 131072=3124843`, and `3124843-1=6*520807`.

## PREFIX-941: exact k=12 boundary

Writing `12a=4(3a)`, for `i,j>=2` there is an exact identity:

`(12a XOR 2^j)-2^i = 4*((3a XOR 2^(j-2))-2^(i-2))`.

Because `b` is odd, divisibility by `b` is exactly equivalent before/after removing the factor four. All 289 interior source-bit combinations thus belong to the already fully enumerated W3 set; only `361-289=72` combinations with `i<2` or `j<2` may add coverage. On the finite domain, `2,621,452<=D_12<=6,553,587<25*262145=6,553,625`, so `1<=t<=24` is exhaustive.

There are **3,719,345** boundary witnesses, representing **3,522,575** unique ordered pairs. Disjoint priority overlap including W11 is:

| Priority source | Count |
|---|---:|
| B/Z/S | 1,815,500 |
| U / V | 642 / 6,440 |
| W2 / W3 / D4 | 22,382 / 520 / 58,200 |
| W5 / D6 / W7 / D8 | 302 / 739,631 / 369 / 9 |
| W9 / D10 / W11 | 185 / 10 / 213 |
| **New to the union** | **878,172** |

The final union is therefore **7,559,578,160** out of `|Q|^2=17,179,869,184`, leaving **9,620,291,024** ordered pairs outside these explicit collision-certificate families. For example `(a,b)=(276843,512037)`, `i=0,j=18,t=7`: `12a=3322116`, `3322116 XOR 262144=3584260` and `3584260-1=7*512037`.

## Exact computation and independently checked bytes

One C++17 scalar program per k performed complete exact integer enumeration, mandatory modular checks, sorting/uniqueness and priority-disjoint membership against historical sorted sets. Independent Python/NumPy implementations formed XOR endpoints as `x+(1-2*bit_j(x))*2^j`, independently inverted the bounded quotients and rebuilt B/Z/S, U and V and all sorted-input overlaps. Both paths agree on *every quotient count, every partition category and the complete binary bytes* of the source and new-only sets:

| Sorted little-endian uint64 IDs | IDs | Bytes | SHA-256 |
|---|---:|---:|---|
| W11.bin | 13,144,330 | 105,154,640 | `8212f0472ebe72ae93db8a205c8631f5eb96abbe952588cc08a5eb4087aeecf5` |
| NEW11.bin | 5,888,914 | 47,111,312 | `b17896465cb38ca5b87e48f88ebaf7d709888a9d0ef343c1c056916fb6c03ad9` |
| D12.bin | 3,522,575 | 28,180,600 | `8674cab718a62897ac2189499a4c060508a9ab759ca5ed5ea5e531ea8ea90b64` |
| NEW12.bin | 878,172 | 7,025,376 | `a0e3bca93ac8fbf3eb97c1850a3190a40b55e7f80f1b889ffd523da48eb38581` |

Frozen exact inputs: `PREFIX928_R6_SORTED_PAIR_IDS.bin`, `W2.bin`, `W3.bin`, `D4_sorted_cpp.bin`, `W5.bin`, `D6.bin`, `W7.bin`, `D8.bin`, `W9.bin`, `D10.bin` and, for k12, `W11.bin`. Published source formulas supply earlier closed B/Z/S and V tests. Full binary evidence and checksummed local reproduction packages are retained alongside this conversation; executable sources and summary result JSON are stored in the project.

**Scope:** The complement has no proven injectivity status. Mother problem `B_fix,odd(32) in {19,20}` remains open; independent mathematical review, formal Result/CLAIM and native X6 transfer are separate matters.

**Next question:** Test an odd-core residue/quotient sieve for `k=13`, compare actual new coverage with the PREFIX-941 full union, and reuse the dyadic reduction for `k=2^r*m` without re-enumerating covered interior source-bit pairs.
