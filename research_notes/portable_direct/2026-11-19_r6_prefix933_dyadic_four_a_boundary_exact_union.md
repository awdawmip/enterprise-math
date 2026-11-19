# PREFIX-933 — Four-a dyadic reduction and complete named-XOR boundary census

2026-11-19; 进取数论研究6. Frozen scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d. Evidence: AUTHOR_PROVED / TWO_INDEPENDENT_EXACT_ENUMERATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Scope and theorem A

Let N=2^32 and Q={262145,262147,...,524287}. Preserve typed zero and one-XOR-flip traces Z_x=(x,x), F_x^i=(x,x XOR 2^i), including source type, bit i, and start x. Observe Phi_(a,b)(u,v)=(u mod a,v mod b). This is an auxiliary two-port observer; native X6 equivalence is not claimed.

Define W4 as those ordered (a,b) in Q^2 admitting 0<=i,j<=18 and positive t with

    (4a XOR 2^j) - 2^i = t*b.

The named traces F_0^i=(0,2^i) and F_(4a)^j=(4a,4a XOR 2^j) are then distinct with equal two-port observations.

**Dyadic reduction lemma.** For i>=1, j>=1,

    (4a XOR 2^j) - 2^i = 2*((2a XOR 2^(j-1))-2^(i-1)).

Since b is odd, b divides the left side exactly when it divides the parenthesized term. Thus the entire i,j>=1 portion of W4 is contained in the earlier complete W2 family. For W2, (2a XOR 2^j)-2^i is positive and less than 2^20, while 4b>2^20, so the earlier t<=3 enumeration is exhaustive.

Put D4={W4 witnesses with i=0 OR j=0}. The set identity W4 minus W2 = D4 minus W2 follows. The boundary differences satisfy 524292 <= (4a XOR 2^j)-2^i <= 2359291, so exhaustive quotients are t=2,...,8. Exactly one zero bit yields odd t; i=j=0 produces t=4,b=a. The same divisibility reduction applies to dyadic factors 2^r whenever both source-bit indices are >=r.

## Theorem B: exact finite census

Two independent algorithms (scalar C++17 priority membership and vectorized NumPy with independent predicate reconstruction) obtain identical counts and **byte-identical** sorted uint64-LE D4 pair IDs. Encoding: ((a-262145)/2)*131072 + ((b-262145)/2). An extra complete 19x19 source-bit C++17 enumeration confirms the dyadic reduction and all XOR endpoints.

D4 has **1793182 raw / 1793182 distinct ordered pairs**: t3=808275, t4=131072, t5=694676, t7=159159; other t=0. D4 output bytes=14345456, SHA-256=d66d467d5c48d62f6bdb2cdf02a081830eba4a32f28447b10d8c425350bdb664.

Complete W4 has 35347626 raw, 29263013 distinct; its interior i,j>=1 has 27601589 distinct, boundary has 1793182 distinct, overlap=131758; all interior pairs occur in W2. The complete W4 set outside W2 has 1661107 pairs. Full W4 output bytes=234104104, SHA-256=96156361dd43343abb580f5adc5fb25dc3319dee68c9f4b30f7cb04f1cc1247c.

Priority-disjoint intersection of D4 with previously certified B/Z/S/U/V/W2/W3:

| category | count |
|---|---:|
| B/Z/S | 963504 |
| U, outside earlier classes | 212 |
| V, outside earlier classes | 3155 |
| W2, outside earlier classes | 314 |
| W3, outside earlier classes | 342 |
| **New outside PREFIX-932** | **825655** |
| Total | 1793182 |

Hence the exact certificate union grows from 7530824145 to **7531649800** out of 17179869184 ordered pairs. The complement 9648219384 is still unclassified by these certificates.

First new pair: (a,b)=(294927,480617), source bits (i,j)=(0,18), quotient t=3. The named collision is F_0^0=(0,1), F_1179708^18=(1179708,1441852): first residues both 0; endpoint difference 1441852-1=1441851=3*480617. The prior union excludes this pair.

## Reproduction

Reuse frozen sorted uint64-LE U from PREFIX-928, 5295478 entries, SHA256=15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad. Recreate the sorted W2 30211412 entries (SHA256=bceb588c6c3aee31ce627fadaa6d0d3ec56ea3f865ddea9d39daec13365e6150) and W3 19413088 entries (SHA256=3f501ca25d0b8c55b284b621d26251f8be2c8c771ce294206f24b1daa10051a9) with PREFIX-932 code.

Compile C++17 -O3. Boundary C++ accepts [U,W2,W3,D4 output]; complete-source C++ accepts [W2,D4 output,W4 output]; independent Python3/NumPy accepts [U,W2,W3,D4 output]. Exact-integer arithmetic only, compare output digests and classifications. All named XOR endpoints and modulo constraints were checked during generation; independent mathematical review and admission are separate.

Next discriminating unit: k=5 and general 2-adic odd-core/low-bit-boundary normal forms; deduplicate against the entire prior certificate union rather than counting raw witness multiplicity as new pairs. Historical author identity: EM-DIRECT-58C410, SID MCP-31edc522830749ad8775ca012e02ef30, Activity RA-25432C4AAE9BF66A907F5115. Shared X6 not claimed.
