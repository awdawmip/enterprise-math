# BRC-X6 five-pair source-action matching and improved native determinant bound

2026-11-09. **AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_VERIFIED / UNREVIEWED / NOT_ADMITTED**.

Frozen original scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. The 38 lawful source-labelled deterministic policies are four-tuples of actions in {0,...,5} for sources (6,7,28,29), signed (+,-,-,+). The original kernel preserves all nine frozen roots and full signed next-port / seven-reward joint observations. The unchanged 24-by-38 incidence matrix has rational rank 13. This is author-portable mathematics, not D25 original-class native Frobenius/CM execution or a Source Result.

## Theorem 1 — every 13 lawful policies contain five disjoint shared-source pairs

More generally, let C be any set of 13 distinct length-four words over a six-letter alphabet with minimum Hamming distance at least two. Join two words when they agree at at least one *same labelled coordinate*. Their overlap graph contains a matching of at least five edges.

**Proof.** If its matching number were at most four, Tutte–Berge would supply a set U of t vertices with o(G-U)-t >= 13-2*4 =5, where o counts odd connected components. The components use mutually disjoint alphabets at each coordinate, and thus G-U has at most six components. The inequality forces t<=4. For t>=2 it requires at least seven odd components, impossible. For t=1 it requires six odd components among 12 remaining words. Six components must each consume exactly one letter per coordinate, hence be singleton components, contradicting 12 remaining words.

For t=0 the graph must have five or six components. Six components would all be singletons, giving at most six words. In the five-component case let s(i,j) be the number of coordinate-j letters used by component i and set k(i)=sum_j(s(i,j)-1). Since component alphabets are disjoint and each coordinate has six possible letters, sum_i k(i) <=4*(6-5)=4. If k(i)=0 that component has one word. If k(i)>0, delete one coordinate having at least two letters. This projection is injective on the component (otherwise two different words would differ at only one coordinate), so its size is at most product of the remaining alphabet sizes, bounded by 2^(k(i)-1) using s<=2^(s-1). The largest possible sum of these bounds for five components and total budget at most four is 8+1+1+1+1=12, contradicting 13. QED.

The 13 threshold is SHARP for the abstract four-coordinate six-letter distance-two code: eight even-parity binary tuples together with (2,2,2,2),(3,3,3,3),(4,4,4,4),(5,5,5,5) give 12 words, four isolated vertices and maximum matching four. This abstract extremizer is not asserted to consist of native lawful policies.

**Native bridge.** The six original actions at each source have pairwise distinct (next-port, full reward) outcomes already at the zero root. Two distinct lawful policies therefore cannot differ at exactly one source: their signed observation difference would be two unequal point masses supported at that source. Direct exact reconstruction finds 38 policies from 1296 candidates and verifies nine-root lawful status; among 703 unordered pairs the Hamming distances are 2:160, 3:120, 4:423. Hence the theorem applies to EVERY 13-subset of the frozen 38 policies. The PREVIOUSLY published 13-subset [0,7,8,11,15,21,22,23,29,31,33,34,35] has maximum matching exactly five by exact subset DP: it refuted a universal six-pair guarantee and now also establishes five-pair sharpness in this native family. No recredit of its discovery.

## Theorem 2 — every labelled incidence minor of order <=13 has absolute determinant <=6971

For k<=12, the 24-dimensional policy column has four ones and squared norm four, giving Hadamard |det|<=2^k<=4096. For k=13 repeated columns give determinant zero. Otherwise Theorem 1 gives five disjoint pairs sharing an identical labelled source/action coordinate, plus three singleton columns. For the full 24-by-13 matrix U, each paired 2-by-2 Gram block has determinant at most 4*4-1=15, and each singleton block has determinant four. Hadamard–Fischer yields det(U^T U)<=15^5*4^3=48,600,000. Cauchy–Binet expresses that determinant as the sum of squared integer 13-by-13 row minors. Therefore every minor magnitude <=floor(sqrt(48,600,000))=6971, since 6971^2=48,594,841 <48,600,000<6972^2=48,608,784. This improves the PREVIOUS 7200 bound by 229.

## Explicit tighter-base witnesses (original policies unchanged)

Use precisely the previously published legal prefix, in order:
```
(0,0,2,2) (1,0,3,2) (2,2,4,4) (3,3,5,5) (4,4,0,0)
(4,4,5,5) (4,5,0,1) (5,1,1,3) (5,5,5,5)
(0,0,0,0) (0,0,1,1) (0,0,4,4) (0,1,2,3)
```
Set B=6972, D_k=sum_{j=0}^{k-1} B^j and X_k=(sum_{j=0}^{k-1}B^j c(v_j))/D_k for k=9,10,11,12,13. Each prefix has rational rank k and covers every one of the 24 native source/action cells; all original nine-root signed joint observations cancel exactly, and all probability cells are positive.

For optimality, if X_k lay in the span of <=k-1 legal columns, extend those to k-1 independent legal columns S (the full rank is 13). Some prefix column is outside span(S), yielding a nontrivial determinant functional L(z)=det([S,z]_R) on a selection of k original rows. Theorem 2 gives integers a_j=L(c(v_j)) with |a_j|<=6971=B-1. For the largest d with a_d nonzero, |a_d|B^d>=B^d while the preceding weighted sum has magnitude <=(B-1)(B^d-1)/(B-1)=B^d-1. Thus L(D_k X_k) is nonzero, a contradiction. Hence minSupport(X_k)=k.

Unreduced exact denominators and binary bit lengths:
- k=9: 5583690314315592031005006494221 (103 bits)
- k=10: 38929488871408307640166905277708813 (115 bits)
- k=11: 271416396411458720867243663596185844237 (128 bits)
- k=12: 1892315115780690201886422822592607706020365 (141 bits)
- k=13: 13193220987222972087552139919115660926373984781 (154 bits)

Relative to the previously published B=7201, k=10 and k=11 denominators each save one bit; k=9,12,13 have smaller exact integer values but unchanged bit lengths. The historical 35-bit 13-support EXISTENCE theorem is separate from any explicit 35-bit witness.

## Exact check and attribution

Author-side standalone verifier: `verify_matching5_base6972.py` with unchanged frozen `frozen_native_kernel_prefix577.py` (SHA-256 `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`). Local exact run: all 1296 candidates / 38 lawful / nine roots, Hamming distance histogram, sharp 12-word matching DP=4, previous 13-word matching DP=5, 24-dimensional rational rank, exact denominators, source row masses, strict positivity and all signed observers PASS. The universal matching theorem is SYMBOLIC (Tutte–Berge and coordinate budget), not a sampled or billions-subsets assertion. The full local five-file ZIP, including the checker and machine-readable exact certificate, was produced in this same Chat run; its SHA-256 is `f997a7cc81744b06cff14a6fce705d6ae3da76ea29e91a38102466e2b02b1a63`. A ZIP digest does not itself imply remote Source storage.

Prior attributed authorship: `awdawmip/enterprise-math@b0850ea4d01d18202243badbff597282df75b93c` for the 7200 bound, 7201 radix and prior six-pair counterexample. NEW unit: universal five-pair matching theorem with sharp 13 threshold, 6971 bound and B=6972 arithmetic. P000 and ACTIVE worldview unchanged.

Original D25 current Source frontier: H0/B0 original-class divided power, [X]U mod p², native eta Frobenius and kappa/Delta-R/CM remain UNFINISHED; prior historical D25 continuation succeeded with execution_authorized=false. Original UR four-file V2 archive target 94,687 bytes / SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` remains unfound in the currently mounted files. Our previously issued researcher/session RA persists but its private session capability is unavailable, and no winning CLAIM or formal native checkpoint is asserted. Preserve the original session ID and request; do not register another identity or borrow old credentials. This note is author evidence only, awaiting lawful writer/provenance and independent Driver review.

Next portable discriminator: an explicit <=35-bit full-positive 13-minimal rational witness with a complete lower-support impossibility certificate, improving the old existential-only 35-bit bound if constructible.