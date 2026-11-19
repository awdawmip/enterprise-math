# PREFIX-925 — Exact 24-row same-start alias contribution to the three-family collision union

Date: 2026-11-19 (Asia/Shanghai), 进取数论研究6. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_IMPLEMENTATION_AGREEMENT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Direct precedents: PREFIX-917 equal-start collision support, PREFIX-923 two-sided bucket-capacity, PREFIX-924 exact zero/zero/bucket union. No native X6 CLAIM or native dynamics equivalence asserted.

## Definition and exact theorem

Let p=32, N=2^32 and Q={262145,262147,...,524287} (131072 odd moduli). The named XOR observer sends Z_x=(x,x) and F_x^i=(x,x XOR 2^i), with type/start/source-bit labels, to (start mod a, endpoint mod b), for each ordered (a,b) in Q^2.

Use these three previously established collision mechanisms:
- B: violation of at least one PREFIX-923 two-sided capacity condition, b>=33 ceil(N/a) and a>=33 ceil(N/b).
- Z: a zero-step/zero-step collision, equivalently lcm(a,b)<N, by PREFIX-924.
- S: a same-start, differently source-labeled one-flip/one-flip collision.

**New exact three-family statement:**

| Set | Cardinality of ordered modulus pairs |
| --- | ---: |
| S (all same-start support) | 3,145,728 |
| S intersect B | 1,493,890 |
| S intersect Z | 93,092 |
| S intersect B intersect Z | 54,763 |
| **S outside (B union Z)** | **1,613,509** |
| B union Z (PREFIX-924) | 7,460,895,462 |
| **B union Z union S** | **7,462,508,971** |
| Q^2 outside three-family union | 9,717,360,213 |

This is a globally exact count **within these three declared mechanisms**. It is not a fresh globally disjoint increment against the previously published full signed-power/mixed-flip/other PREFIX certificate ledger.

## Structural criterion and explicit witnesses

For odd b>1, the same-start, differently labeled F^i/F^j collision exists iff

b divides 2^d-1 or 2^d+1 for some 1<=d<=p-1.

Proof: at a fixed start x, the two one-bit XOR endpoints differ by one of ±2^i±2^j, with i≠j. Factoring out 2^min(i,j), invertible modulo odd b, yields the stated condition. Conversely choose i=d,j=0:
- If b | 2^d-1, F_0^d=(0,2^d) and F_0^0=(0,1) have identical first-port observation and congruent endpoints mod b.
- If b | 2^d+1, F_1^d=(1,1+2^d) and F_1^0=(1,0) do so.
All endpoints lie in [0,N) because 1<=d<=p-1. Both traces retain distinct source labels, and a is arbitrary.

Thus the full second-modulus support is D={b in Q: W_32(b)>0}, using PREFIX-917's

W_32(b)=sum_{d=1}^{31}(32-d)(1_{b | (2^d-1)}+1_{b | (2^d+1)}).

The exact modular recurrence r_1=2 mod b, r_{d+1}=2r_d mod b selects precisely **24** moduli in D, yielding |S|=24*131072=3,145,728. The entire 24-element set and its 4-way row partitions are in the accompanying JSON.

Example: b=262145=2^18+1: F_1^18=(1,262145) and F_1^0=(1,0) collide for **every** a. b=524287=2^19-1: F_0^19=(0,524288) and F_0^0=(0,1) collide for every a.

## Exact overlap algorithm and certificate

For each of the 24 selected b and **every** a in Q (3,145,728 exact ordered pairs):
1. Test capacity safety directly with both integer inequalities.
2. Test zero-zero support with (a/gcd(a,b))*b < 2^32.
3. Assign the pair uniquely to four cases: B-and-Z, B-only, Z-only outside B, neither B nor Z.

The complete four-class totals across S are:
- B without Z: 1,439,127
- B intersect Z: 54,763
- outside B with Z: 38,329
- outside B and Z: **1,613,509**.

The partition totals 3,145,728. Hence S∩B=1,493,890 and S∩Z=93,092. Inclusion-exclusion gives the stated new union total exactly.

A standard-library-only Python 3 implementation and an independently written C++17 implementation both scan the exact D recurrence and all a, obtaining identical five intersection totals, without floating-point approximations. The Python program emits all 24 four-class row records; the JSON freezes those exact records for cross-checks.

Files:
- PREFIX925_R6_SAME_START_UNION_CHECK.py
- PREFIX925_R6_SAME_START_UNION.cpp
- PREFIX925_R6_SAME_START_UNION_RESULTS.json
Run: python3 <python_file> and g++ -O2 -std=c++17 <cpp_file> -o prefix925 && ./prefix925.

## Next precise task

Intersect this fully deduplicated three-family certificate with older named two-flip and mixed zero/one collision unions, using their **actual published pair-set encodings** rather than adding totals. This reduces double-count uncertainty on Q^2 without pretending these auxiliary findings solve the native X6 mother question B_fix,odd(32) in {19,20}. Compare the six-axis P000-native target only through an explicitly proved typed transfer.
