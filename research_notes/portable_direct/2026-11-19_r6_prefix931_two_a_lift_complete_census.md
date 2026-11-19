# PREFIX-931 — Two-multiple named two-flip certificates: exact census and overlap with PREFIX-930

Date: 2026-11-19. Lane: 进取数论研究6.
Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Status: AUTHOR_PROVED / INDEPENDENT_CPP_AND_NUMPY_EXACT_ENUMERATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
This concerns the auxiliary provenance-aware named XOR two-port observer only, not a native X6 dynamical equivalence.

## Theorem A (complete declared W2 certificate family)

Let N=2^32, Q={262145,262147,...,524287} (|Q|=131072). Named traces are Z_x=(x,x) and F_x^j=(x,x XOR 2^j), for 0<=x<N and 0<=j<32. Observe Phi_(a,b)(u,v)=(u mod a,v mod b), retaining all source labels.

Define W2 as the set of ordered pairs (a,b) in Q^2 for which there exist integers 0<=i,j<=18 and t>=1 with

    abs(((2a) XOR 2^j) - 2^i) = t*b.

Every (a,b) in W2 is noninjective. Two actual different named traces are

    F_0^i=(0,2^i),     F_(2a)^j=(2a,(2a) XOR 2^j).

Their first-port residues are both zero because the starts differ by 2a; their second-port residues agree by the displayed divisibility. All four endpoints are in [0,N). Since 2a is between 524290 and 1048574, bit j<=18 cannot change its high 2^19 bit, giving 2^19 <= (2a XOR 2^j) < 2^20. Also 2^i<=2^18, so d=((2a XOR 2^j)-2^i) is positive and below 2^20. Since b>=262145, t must be 1,2 or 3. Thus exhaustive integer enumeration of all a in Q, all 19^2 index pairs and t=1,2,3 covers precisely W2.

## Theorem B (dyadic lift and finite W1 containment)

If F_0^i and F_a^j collide under Phi_(a,b), then for any r>=0 with 2^r a < N and i+r,j+r<p the shifted traces F_0^(i+r) and F_(2^r a)^(j+r) collide. The identity

    (2^r a) XOR 2^(j+r) = 2^r (a XOR 2^j)

shows their endpoint gap is multiplied by 2^r and remains divisible by b. All named bit indices remain explicit. The finite exact 19-bit enumeration further verifies that every one of the prior W1 family's 29,360,142 ordered pairs belongs to W2, including the cases requiring a different within-cutoff witness when the elementary shifted index exceeds 18. This full finite containment is computationally certified; it is not an unrestricted index-bound theorem.

## Exact counts and disjoint priority classification

The prior PREFIX-930 union B union Z union S union U union V union W1 had 7,522,177,912 pairs. B is the two-sided capacity obstruction, Z zero-zero, S same-start source alias, U the PREFIX-928 32-bit mixed-zero 5,295,478-ID set, V 104 complete moduli lines/transposes and 1024 high-band seeds/transposes, and W1 the PREFIX-930 explicit a-start two-flip construction.

| Exact integer measurement | Count |
|---|---:|
| W2 raw (a,i,j,t) parameter witnesses | 36,787,554 |
| Raw witnesses t=1 / t=2 / t=3 | 131,072 / 35,913,744 / 742,738 |
| W2 distinct ordered pairs | 30,211,412 |
| W2 intersect B/Z/S | 13,544,621 |
| W2 intersect U outside B/Z/S | 8,689 |
| W2 intersect V outside B/Z/S/U | 62,870 |
| W2 intersect W1 outside B/Z/S/U/V | 16,217,848 |
| **W2 new pairs outside PREFIX-930 union** | **377,384** |

These priority categories are pairwise disjoint and sum exactly to |W2|.

Hence the exact enlarged certificate union has 7,522,555,296 ordered modulus pairs. The complement in |Q^2|=17,179,869,184 contains 9,657,313,888 pairs; these are unclassified by this particular certificate union, not proved injective.

An explicit genuinely new collision is (a,b)=(274527,516287), i=15, j=0, t=1:

    F_0^15=(0,32768)
    F_549054^0=(549054,549055)

Both observations equal (0,32768), since 549054=2*274527 and 549055-32768=516287. The pair also satisfies both sharp B capacity inequalities (at equality on one side), and exact enumeration places it outside prior U/V/W1 and Z/S.

## Independent finite verification and reproduction

The actual C++17 code enumerated all (a,j,i,t), verified actual modular equalities, sorted/deduplicated 30,211,412 uint64 IDs, regenerated W1, and classified the exact intersection with B/Z/S/U/V/W1. A separately implemented vectorized NumPy code enumerated all a simultaneously for each (j,i,t), independently recomputed gcd/capacity/row masks and intersections via searchsorted. The two resulting W2 binary files were byte-identical (241,691,296 bytes); both partition counts match exactly.

W2 sorted uint64 little-endian SHA-256:
bceb588c6c3aee31ce627fadaa6d0d3ec56ea3f865ddea9d39daec13365e6150

The independently regenerated W1 sorted binary (29,360,142 entries) matched its previous SHA-256:
b7d00da2269ac6d56ca1c612e9526a81a11aa8f47840db74780523a4e90ffba6

The frozen U input (5,295,478 entries) was read from the preserved PREFIX-928 reproducibility archive and matched its earlier SHA-256:
15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad

Sources and reproducibility:
- PREFIX931_R6_DOUBLE_MULTIPLE_CENSUS.cpp (C++17 -O3, input PREFIX928_R6_SORTED_PAIR_IDS.bin; optional sorted W2/W1 outputs).
- PREFIX931_R6_INDEPENDENT_NUMPY.py (NumPy, input same U and the C++-reproduced W1 binary).
- PREFIX931_R6_RESULTS.json (all scope boundaries, counts, digests and explicit witness).
- Prior proof and certified 7,522,177,912 count: PREFIX-930@709c940a09a20dbb4dc6e1a438df4896c2f0fe89.

Researcher provenance: EM-DIRECT-58C410 / SID MCP-31edc522830749ad8775ca012e02ef30, Activity RA-25432C4AAE9BF66A907F5115. Activity association, shared CLAIM, Result and independent Review are separate from GitHub scientific preservation.

Next discriminating questions: extend to odd multiples k=3; extend i,j to bit 31; intersect all genuinely new source families with the exact certified union rather than counting raw witnesses as new pairs.
