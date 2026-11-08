# PREFIX577-R6 — Nine-root invariant-start polytope: Hilbert series, face lattice and integer-resolution counts

Date: 2026-11-08. Status: **AUTHOR-DERIVED / EXACT-INTEGER-CHECKED / UNREVIEWED / NOT_ADMITTED**. This is a *new combinatorial corollary* of already published author evidence; not a new native Source CLAIM, checkpoint, Result, review, UR theorem or D25 LIFT experiment.

## Frozen input and prior theorem

Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Reused 96-original-port, seven-observer all-depth symmetry classification: [prior nine-root author proof](https://github.com/awdawmip/enterprise-math/blob/0509d95df420e2283bda86257d0dab90bc60d63e/research_notes/portable_direct/2026-11-08_prefix577_r6_all_nine_frozen_roots_initial_law_author_portable.md), blob SHA-1 9f18656f81f0ac073c4a51db80debc18a04a3819. It establishes the same 16 pair-of-pairs mass balances for each of the *nine frozen roots only* 0, ±e1, ±e2, ±e3, ±e4. No new native dynamics or root generality is inferred.

Let the 16 **disjoint** blocks be A_j ∪ C_j, where |A_j|=|C_j|=2, and let S comprise the other 32 ports. The exact invariant-start polytope P consists of μ_i≥0, Σ_i μ_i=1 and Σ_(i∈A_j) μ_i=Σ_(i∈C_j) μ_i for all j. The original port sets are given explicitly in the linked prior source. These retained labeled A/C fiber balances are the BRC provenance-preserving carrier; total-only summaries would lose the constraint.

## Result 1 — exact join and every face count

Each block-supported normalized starting law is a square Q_j ≅ Δ_1×Δ_1, whose four vertices are (e_a+e_c)/2 with a∈A_j and c∈C_j. The 32 singleton-supported laws form Δ_31. Every μ∈P decomposes uniquely by its disjoint-support factor weights w_S=Σ_(i∈S)μ_i and w_j=Σ_(i∈A_j∪C_j)μ_i (their sum is 1). Normalizing the nonzero restrictions gives:

**P = Δ_31 * Q_1 * ... * Q_16,  dim P = 31 + 16·2 + 16 = 79.**

Here * denotes convex join in disjoint coordinate supports. The exact face polynomial (empty face contributes 1; coefficient of t^(d+1) counts d-dimensional faces) is

**F_P(t)=(1+t)^32(1+4t+4t²+t³)^16=(1+t)^48(1+3t+t²)^16.**

Proof: the simplex has face polynomial (1+t)^32; the square has empty/vertices/edges/full counts (1,4,4,1); the face lattice of a join is the product of factor face lattices. Consequently P has exactly 96 vertices, 4528 edges, 4528 codimension-two faces (dim 77) and 96 facets (dim 78). Coefficients are palindromic; the face lattice is combinatorially self-dual.

## Result 2 — exact integer semigroup and Hilbert/Ehrhart series

For nonnegative integer port counts m_i, impose the same 16 block balances. Let L_P(N) count balanced vectors with total mass Σ m_i=N, with L_P(0)=1. For N≥1 these are precisely invariant starting laws resolved in units 1/N (under the parent nine-root theorem).

The minimal Hilbert basis of the balanced nonnegative integer semigroup consists of **exactly 96 primitive generators**: 32 singleton e_s (s∈S) and 64 pair vectors e_a+e_c (a∈A_j,c∈C_j). Proof: integer counts with equal mass n on each half of any block can be paired token-by-token into n A/C cross pairs; singleton masses split into e_s. The displayed 96 generators are indecomposable (singleton degree 1; any nonzero balanced block component has degree ≥2).

On a single balanced block with n units on each side there are (n+1)^2 possible integer four-port configurations, of total degree 2n. Since Σ_(n≥0)(n+1)^2 x^n=(1+x)/(1−x)^3, the exact Hilbert/Ehrhart generating series is

**H(t)=Σ_(N≥0)L_P(N)t^N = (1+t²)^16 / ((1−t)^32(1−t²)^48).**

An explicit finite integer formula (binom(a,b)=0 for a<b or a<0) is

**L_P(N)=Σ_(j=0)^16 Σ_(m≥0) binom(16,j) binom(m+47,47) binom(N−2j−2m+31,31).**

Equivalently H(t)=(1+t²)^16/((1−t)^80(1+t)^48). There are exact poles of orders 80 at +1 and 48 at −1, with nonzero principal coefficients 2^(−32) and 2^(−64), respectively. Consequently **L_P(N)=P_79(N)+(−1)^N Q_47(N)** for all N≥0, where P_79,Q_47 are rational-coefficient polynomials of degrees exactly 79 and 47, and their respective leading coefficients are **1/(2^32·79!)** and **1/(2^64·47!)**. Thus the arithmetic quasipolynomial has *minimal exact period 2*, with parity variation confined to a lower-degree term.

All 96 nonnegativity coordinates define facets, hence a strictly positive integer point of degree N requires m_i≥1 for every i. Subtraction of the 96-vector of ones preserves all balances. With L_P°(0)=0 by convention, the positive-degree relative-interior generating series equals **t^96 H(t)**, so L_P°(N)=0 for N<96 and L_P°(N)=L_P(N−96) for N≥96. The first full-support integer-resolution law occurs at N=96 and is the uniform 96-port start. This threshold concerns discrete representation, not strictly-positive real starting measures.

## Reproducibility and semantic limits

An exact stdlib-only author checker parsed all 16 disjoint 2+2 native blocks (64 distinct ports, plus 32 fixed singleton ports) from the frozen parent proof. It verified all 96 primitive ray/vertex descriptions, all 81 face polynomial coefficients, and compared two separate exact algorithms for L_P(N), N=0..26: (i) direct four-tuple counting per block with integer convolution and (ii) the rational generating-function binomial coefficient expansion. All checked coefficients agree; L_P(0..5)=(1, 32, 592, 8032, 88216, 826016). The finite regression is not the proof of the infinite-N identities; the displayed combinatorial and partial-fraction arguments establish those.

Checker SHA-256 df63cf60abf986415e88888a8eaaa7c27ff15b53275fe7f4e5cd1b274808b14f; JSON exact certificate SHA-256 14648cfb1315d0dcb9327064dd7376d82539fe698a5180e3ab94160a3b4266c7; expanded proof SHA-256 e6802fe6332096287f313bad2ebd06ebc2cac246f4ee23565f253068c231cce1. Their original bytes are in the local user-visible portable bundle for this turn; this compact publication is the self-contained immutable theorem summary.

The prior nine-root full-joint-law theorem is **consumed**, not independently reproved. This is author-level exact finite combinatorics, not Source admission, not a claim about arbitrary roots, not an external physical-law result, and not an algorithmic complexity improvement. D25's original-class H0/B0, [X]U mod p², Frobenius, κ and Δ_p−R_p remain unsolved; D24 Result/Review remain terminal. Native Source recovery/claim authority has not been granted for this author publication.

Next useful science: obtain actual constraints for a specified *different observer* (e.g. gate-only) before counting its admissible starts, or test an explicitly selected outside-nine-root input by genuinely re-executing the pinned native dynamics; do not infer more roots from this factorization.