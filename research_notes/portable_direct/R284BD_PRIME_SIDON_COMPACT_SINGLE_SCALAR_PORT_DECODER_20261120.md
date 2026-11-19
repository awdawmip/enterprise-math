# R284BD — Quadratic prime-Sidon compression of the one-scalar star-Port decoder

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. Scientific lineage R284AT → R284AX → R284BC. Independent portable note; no active Task CLAIM or formal Result/Review is asserted. The exact finite directed-Port matrix observer is an auxiliary typed observer, **not** a new P000 native-world axiom or a claimed X6 dynamics result.

## Theorem BD1 (smaller deterministic weights)

Fix n≥3, known H≥2, and an unknown strictly positive integer matrix C∈{1,...,H}^{n×n}. A single scalar observation has the form

    y = det(diag(d_0,...,d_{n-1}) - C - Σ_{i=1}^{n-1} z_i E_{0i}).

There is an explicit, uniform choice of nonnegative integer diagonal controls d_i and nonnegative integer simultaneous star-Port edits z_i, and a direct deterministic polynomial-time exact decoder recovering every C_ij. All control values and y have O(n^5 log b) bit length, with

    log b = O(n log n + n log(H+1)).

For a specified finite rational absolute error bound δ≥0, a corresponding construction decodes every exact rational readout y+ε with |ε|≤δ. In this case replace the logarithmic factor by O(n log n+n log(H+1)+log(1+δ)). These bounds are deterministic **bit** bounds including input and output representation, not unit-cost arithmetic or physical instrument precision.

This improves the base-exponent estimate in R284BC from O(n^6) to O(n^5), preserving the R284BC coefficient decoder and its one-read model. No universal dynamic-range optimality or native X6 transfer is claimed.

## Lemma 1 — quadratic-mod-prime Sidon weights

Let p be the smallest odd prime p≥n. For 0≤j<n define

    r_j = j² mod p,                0≤r_j<p,
    a_j = 2pj + r_j.

Then all a_j are distinct, 0≤a_j≤2p(n−1)+p−1=O(n²), and the unordered sums a_i+a_j for distinct indices i<j are pairwise distinct.

Proof. If a_i+a_j=a_s+a_t, then write both sums as 2p(i+j)+(r_i+r_j), with 0≤r_i+r_j<2p. Uniqueness of Euclidean quotient and remainder gives i+j=s+t and r_i+r_j=r_s+r_t. Reducing the second equality modulo p gives i²+j²≡s²+t² (mod p). Since p is odd, 2ij≡(i+j)²−(i²+j²)≡2st (mod p), so ij≡st. Hence pairs {i,j} and {s,t} are the same root multiset of the monic quadratic X²−(i+j)X+ij over the field F_p. Each index lies in {0,...,n−1}⊂F_p, so the original unordered pairs coincide. Distinctness of individual a_j follows from strictly increasing 2pj blocks. Bertrand's postulate gives p<2n for n≥3; a deterministic trial-division search in [n,2n) is polynomial in n. QED.

## Lemma 2 — unique targeted exponents without all-subset uniqueness

Let A=max_j a_j, Q=nA+1, e_j=Q+a_j, S=Σ_j e_j, and T=n(Q+A)+1. For any subsets U,V⊆{0,...,n−1} with different cardinalities, their e-weight sums differ: their contributions from Q differ by ≥Q, while the difference in the a-sums has magnitude ≤nA<Q. For fixed equal cardinality n−1 the missing single index uniquely determines the sum; for cardinality n−2 the missing unordered pair uniquely determines the sum by Lemma 1.

Set b odd and choose d_j=b^{e_j}, z_i=b^{iT}. Because S≤n(Q+A)<T, the baseline F(d)=det(diag(d)−C) sits in block [0,T), while the coefficient G_i(d) of the row-zero edit z_i lies in its own block [iT,(i+1)T). Row-zero linearity eliminates z_i z_j products. All required single and unordered-pair missing-index coefficient addresses in F are collision-free. In G_i, the highest monomial (missing 0,i) and its singly deleted d_j monomials are uniquely addressable, even at n=3 when a cofactor constant remains.

Specifically, the identified coefficients are

    [b^{S−e_i}]F = −C_ii,
    [b^{S−e_i−e_j}]F = C_ii C_jj − C_ij C_ji,
    [b^{iT+S−e_0−e_i}] z_iG_i = −C_i0,
    [b^{iT+S−e_0−e_i−e_j}] z_iG_i = C_i0 C_jj − C_ij C_j0
         (i,j≥1, i≠j).

The bracket denotes the **aggregate algebraic coefficient at the displayed radix exponent** before numerical evaluation. Lower-degree collisions outside these addresses are permitted; their signed aggregate contributions remain bounded.

## Decoder and signed-digit bound

Let L=n·n!·(1+H)^n. The sum of absolute coefficients over all baseline/cofactor blocks is ≤L by determinant expansion and triangle inequality. Choose b=2L+1 for exact integer measurement. For each needed integer exponent k, the coefficient c_k has |c_k|≤L<b/2. Every contribution from lower places has magnitude at most L(b^k−1)/(b−1)<b^k/2. Therefore the nearest integer to y/b^k followed by a balanced residue modulo b retrieves c_k, even for negative output values.

The decoder sets C_ii from singleton coefficients, R_ij=C_ij C_ji from two-index coefficients, C_i0 from cofactor leading terms, then uses exact divisions:

    C_0i=R_0i/C_i0,
    C_ij=(C_i0 C_jj−g_ij)/C_j0  (i,j≥1, i≠j).

All divisors are positive. O(n²) chosen exponents and exact divisions suffice. For |ε|≤δ choose the stronger odd radix b=4L+2⌈4δ⌉+9. Each chosen exponent k≥1. The lower-place tail has magnitude <b^k/4 and |ε|<b/8≤b^k/8; nearest-integer extraction therefore stays strictly within the correct half-integer rounding cell for exact rational measurements. The same balanced residue yields c_k.

Finally p=O(n), A=O(n²), Q=O(n³), e_j=O(n³), T=O(n⁴). The highest exponent in the scalar star observer is <nT+S=O(n^5). Consequently every scalar control and the determinant output has O(n^5 log b) bits; a standard exact integer Bareiss determinant and coefficient divisions run in polynomial time in these bit lengths. Prime trial division is also polynomial in n.

## Author-side exact validation (2026-11-20)

Companions: R284BD_prime_sidon_single_scalar_checker.py and R284BD_prime_sidon_exact_verification.json. Python standard library only, signed unbounded integer Bareiss elimination, and seed-fixed matrices. Verification covers 512/512 matrices in {1,2}^{3×3}, plus 16 of (3,3), 8 each of (4,2) and (4,3), 3 of (5,2), 1 of (6,2): **548 reconstructed matrices**, all PASS. Additionally 64 fixed-seed adversarial integer disturbances ±7000 under known δ=7000 passed. The prime-Sidon pair-sum census passed for every 3≤n≤69. These are author-side finite checks, not a replacement for the general algebraic proof or independent review.

Representative comparison (same old/new b for each case, bit lengths in bits):

| n,H | Old R284BC max control bits | New max control bits | New max observed readout bits |
|---|---:|---:|---:|
| 3,2 | 7,227 | 3,177 | 3,644 |
| 4,2 | 70,391 | 28,616 | 32,920 |
| 5,2 | 392,555 | 89,752 | 102,225 |
| 6,2 | 1,566,042 | 351,787 | 395,357 |

The old control figures are computed from the prior published weight formula rather than rerunning the old determinant exhaustively.

## Research continuation

The proven improvement concerns numerical **encoding length and exact decoding**, with no assumption that huge-precision physical readings are cheap. Next independent research: (i) determine whether structured probe interpolation or direct coefficient-address optimization reduces the current O(n^5) exponent while retaining O(n²) decoding; (ii) compare total actual implementation cost and hardware/quantization error, counting full input generation, readout and verification; (iii) investigate whether the O(n^5) packing structure has unavoidable collisions under strictly sparser address families. Keep source observer and future-operation preservation explicit before any joint-Port collapse.

References: project Source R284BC_EXPLICIT_POLYNOMIAL_BIT_SINGLE_SCALAR_STAR_DECODER_20261120.md at Git blob 28758452c291eddcb8eec5a0726d5a5f09ead438; R284AT, R284AX, R284AZ, R284BB lineage. All source scientific input pins remain as in the inherited research route, without repinning P000 or formal Task publication.
