# PREFIX-932 — Exact three-multiple named-XOR collision census beyond PREFIX-931

Date: 2026-11-19. Lane: 进取数论研究6. Scientific status: AUTHOR_PROVED / TWO_INDEPENDENT_EXACT_ENUMERATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Immediate dependency: PREFIX-931 two-multiple complete census (W2), plus previously published B/Z/S/U/V certificates. This is the auxiliary typed named-XOR two-port observer, not native X6 dynamics.

## Theorem A: complete W3 construction
Let N=2^32, Q={262145,262147,...,524287} (|Q|=131072). Preserve named source labels on Z_x=(x,x) and F_x^i=(x,x XOR 2^i), 0<=x<N, 0<=i<32. The observer Phi_(a,b)(u,v)=(u mod a,v mod b) observes two residues, but does not erase the identity of the named input trace.

Define W3 to contain precisely the ordered pairs (a,b) in Q^2 for which there are 0<=i,j<=18 and positive integer t such that
    ((3a) XOR 2^j) - 2^i = t*b.
Every W3 pair is a true noninjective observer: the distinct traces
    F_0^i=(0,2^i), F_(3a)^j=(3a,(3a) XOR 2^j)
have equal first-port residues (zero) and equal second-port residues (because the endpoint gap is t*b). All endpoints are within [0,N). This is constructive for each enumerated witness, retaining both source-bit names.

For Q and 0<=i,j<=18, 3a lies in [786435,1572861]. Toggling bit j changes the value by exactly +2^j or -2^j, and 2^i<=262144. Therefore
    262147 <= ((3a) XOR 2^j)-2^i <= 1835004.
Since b>=262145, every valid quotient has 1<=t<=6. The loops over all 131072 a, 19^2 bit pairs and t=1,...,6 are an *exhaustive* enumeration of W3 as defined; no untested quotient or sign remains.

The first new witness beyond the prior certificate union is a=272007,b=521109,i=15,j=18,t=1. Here (3a)=816021, ((3a) XOR 2^18)=553877 and 553877-32768=521109. Thus F_0^15=(0,32768) and F_816021^18=(816021,553877) both give observation (0,32768). In particular this pair is not covered by the exact prior B/Z/S/U/V/W2 union.

## Theorem B: complete exact intersection with existing certificates
Reuse the previously defined, frozen certificates:
- B: b<33*ceil(N/a) or a<33*ceil(N/b) (two-sided bucket capacity);
- Z: lcm(a,b)<N;
- S: 24 second-port same-start alias moduli detected by small signed-power order;
- U: PREFIX-928 sorted 5,295,478 ordered pairs, SHA-256 15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad, proven disjoint from B/Z/S;
- V: 104 complete second-port rows and their transposes, plus 1024 exact PREFIX-923 high-band seeds and their transposes;
- W2: PREFIX-931 complete k=2 certificate family (contains previous W1 as finite verified subset). Exact sorted W2 SHA-256 bceb588c6c3aee31ce627fadaa6d0d3ec56ea3f865ddea9d39daec13365e6150.

The exact PREFIX-931 prior union B union Z union S union U union V union W2 has 7,522,555,296 ordered pairs.

The W3 raw parameter count is 24,319,678, by t=1..6 respectively:
    [87381,830136,20112264,764599,2525298,0].
After deduplication W3 contains exactly 19,413,088 distinct ordered modulus pairs. The pairwise disjoint *priority* partition is:
    W3 intersection B/Z/S                                       8,752,594
    W3 intersection U outside B/Z/S                                 6,617
    W3 intersection V outside B/Z/S/U                              42,286
    W3 intersection W2 outside B/Z/S/U/V                         2,342,742
    W3 outside the entire PREFIX-931 union                       8,268,849
    Total                                                       19,413,088

Therefore the rigorously certified, explicitly named-collision union grows to
    7,530,824,145 ordered pairs,
leaving 9,649,045,039 pairs unclassified by these certificates within |Q^2|=17,179,869,184.
These are *certificate-complement* counts, not a proof of injectivity of the remaining observers.

## Verification and reproduction
A scalar C++17 exact-integer program generates W2 and W3 from every legal named trace, sorts uint64 pair IDs and merge-intersects U/W2 with separately reconstructed B/Z/S/V membership; it checks direct endpoint congruence for each raw W3 witness. It reproduces the PREFIX-931 W2 raw/unique counts and the W2 SHA-256 above.

An independent NumPy implementation forms entire start vectors and bit-toggle/difference matrices, enumerates all t, validates the named endpoints, sorts/uniques its own W3 IDs, then uses vectorized gcd, boolean masks and searchsorted in bounded chunks rather than the C++ membership procedure. Both implementations report identical category counts and *byte-identical* W3 sorted uint64 LE output of 155,304,704 bytes, SHA-256:
    3f501ca25d0b8c55b284b621d26251f8be2c8c771ce294206f24b1daa10051a9

Reproduction inputs: original PREFIX-928 U sorted uint64 LE binary (5,295,478 entries, immutable archived digest as above), regenerate W2 using C++ program, and compare the NumPy W3 output against the C++ W3. To compile: g++ -O3 -std=c++17 PREFIX932_R6_TRIPLE_A_EXACT_CPP.cpp -o prefix932; run ./prefix932 PREFIX928_R6_SORTED_PAIR_IDS.bin W2_sorted.bin W3_sorted.bin. For independent audit: python PREFIX932_R6_TRIPLE_A_INDEPENDENT_NUMPY.py PREFIX928_R6_SORTED_PAIR_IDS.bin W2_sorted.bin W3_sorted.bin. Python 3 + NumPy required.

Files: PREFIX932_R6_TRIPLE_A_EXACT_CPP.cpp, PREFIX932_R6_TRIPLE_A_INDEPENDENT_NUMPY.py, PREFIX932_R6_TRIPLE_A_RESULTS.json. The sorted W3 binary is a reproducibility output rather than a Git-embedded 155 MB artifact; its exact digest and regeneration instructions are above.

## Provenance and research boundary
Reuse the preserved in-conversation original own Researcher-ID EM-DIRECT-58C410, SID MCP-31edc522830749ad8775ca012e02ef30, Activity RA-25432C4AAE9BF66A907F5115, subject to real same-session authority; no claim of separate shared X6 ownership or formal Result/Review. GitHub publication and Source Activity linkage are separately verified.

Next discriminating research: examine k=4 and higher dyadic/odd multiples with rigorous quotient ceilings, or extend bit i,j beyond 18 while preserving the complete auxiliary source-type model. Before counting new claims, subtract the exact accumulated B/Z/S/U/V/W2/W3 union and retain every immutable set digest.
