# R762HN — Exact repeated-Port BRC return and six-axis local-limit law

**Scientific status:** AUTHOR-PROVED (explicit combinatorial/Fourier proof) / EXACT INTEGER CHECK / NOT_REVIEWED. Scope: composite signed six-axis named-Port candidate; not P000-native primitive TRIADIC_CLOSURE_E.

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Researcher provenance EM-X6-3050F6, original session MCP-4b2d70a97f594366a7c94a0f8b45df38. Frozen source awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000, signed X6 Cell torsor, joint-relation preservation). Prior preserved science: R762HG@f19346110bdca4c9aa237ed766fedc612210293c, R762HK@0778045cdbe977bf86e1d3f7557162e1ed6b33d8, R762HM@a53758b529d02262fce09ed927b1acac1279830a. R762HM native receipt emr3-20261121-0638-r762hm-native-progress-v1 was verified SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED. This note is a new result for repetitions, not a redo of HM's bounded census.

## Model and exact positive BRC identity

Let w=(P_0,...,P_m=P_0) be an ordered named-Port walk, each Port a two-subset of six native labels, with |P_t ∩ P_(t+1)|=1. Put h_t=1_(P_t ∪ P_(t+1)) ∈ Z^6, with three unit entries. These supports represent *composite candidate* Cell shifts, not primitive one-axis steps. For k positive, w^k is the concatenation of k copies, retaining event order and provenance.

Use six Laurent variables and define F_w(z)= product over t of (z^(h_t)+z^(-h_t)). The exact positive-source multiplicity of six-axis zero-Cell signed returns is

  Z_k(w) = CT (F_w(z)^k).

All sign choices and their ordered sources count with nonnegative integer coefficients; signed Cell displacement is tested for zero, not positive BRC weight cancellation. If A_r(v)=[z^v]F_w(z)^r, inversion symmetry yields the exact half-word Gram identity

  Z_(2r)(w) = sum over v in Z^6 of A_r(v)^2.

Consequently Z_(2r) >= 2^(m r) for every r>=1, by selecting arbitrary signs for the first r copies and their negatives for the last r copies. All even repetitions are signable.

When the base word has even length m, this gives a stronger *one-block* construction in the R762HJ/HM alternating-sign convention: start with epsilon_t=(-1)^t and reverse precisely the contiguous final r full copies of the 2r-fold history. The baseline per-copy signed displacement is identical because m is even, hence the first and last r copies cancel. The 14-event two-block obstruction from R762HK therefore becomes one-block repairable after every even repetition.

## R762HN theorem — full-rank six-dimensional local limit

**Theorem.** Fix any finite list of h_t ∈ Z^6 spanning a rank-six lattice L=sum_t Z h_t, with q=[Z^6:L] finite and C=sum_t h_t h_t^T positive definite. For even integers k tending to infinity,

  Z_k(w) = 2^(m k) * [ 64 q / ((2 pi)^3 sqrt(det C)) ] * k^(-3) * (1+O(k^(-1))).

This is an asymptotic of the single fixed ordered candidate word repeated k times. It retains the six native spatial coordinates and their lattice-index residual. It does not claim an all-words asymptotic, native force law, or a theorem for varying words.

**Proof.** Exact Laurent coefficient extraction, normalized by the 2^(mk) equiprobable sign source words, gives a torus integral

  Z_k(w)/2^(m k) = (2 pi)^(-6) ∫_[−pi,pi]^6 [product_t cos(<h_t,theta>)]^k dtheta.

The integrand's absolute value equals 1 precisely when <h_t,theta> ∈ pi Z for every t, i.e., the character theta annihilates 2L modulo 2pi. Since L is full rank there are [Z^6:2L]=2^6 q=64q isolated such points. At each one, the cosine product is ±1; for *even* k, all their contributions are positive. Write theta=theta_0+u. Uniformly at each such point,

  log |product_t cos(<h_t,theta_0+u>)| = -(1/2)u^T C u + O(||u||^4).

Gaussian integration of exp(−(k/2)u^T C u) in six dimensions yields (2pi/k)^3 / sqrt(det C). Off disjoint neighborhoods of these isolated maxima, compactness gives a uniform absolute bound rho<1, so that contribution is exponentially small. Rescaling u=k^(-1/2)v and using analyticity/evenness with a bounded fourth-order remainder yields the stated relative O(k^(-1)) expansion. Summing the 64q maxima and multiplying by (2pi)^(-6) establishes the formula. QED.

## Exact specialization: the R762HK closed 14-event Port word

The original named Ports in order are:

  01 -> 15 -> 12 -> 25 -> 24 -> 04 -> 05 -> 03 -> 04 -> 24 -> 23 -> 25 -> 35 -> 05 -> 01.

The 14 ordered three-axis supports are:

  015, 125, 125, 245, 024, 045, 035, 034, 024, 234, 235, 235, 035, 015.

Each column has total coordinate sum 3; hence every integral combination belongs to the index-three sublattice sum_i x_i ≡ 0 (mod 3). The 6x6 minor formed by zero-based event columns 0,1,3,4,6,7 has determinant −3 (explicit code checks it). Thus L has **exactly index q=3**.

The exact symmetric Gram matrix C is:

~~~
8 2 2 3 4 5
2 4 2 0 0 4
2 2 8 3 4 5
3 0 3 6 2 4
4 0 4 2 6
5 4 5 4 2 10
~~~

Its determinant is 3456=24^2*6. Therefore the prefactor 64*3/((2pi)^3 sqrt(3456)) simplifies exactly to 1/(pi^3 sqrt(6)), yielding, as **even k -> infinity**,

  Z_k(w) = [2^(14k)/(pi^3 sqrt(6) k^3)] * (1+O(1/k)).

The factor q=3 is a genuine integral-span residual. Dropping it would give the wrong leading constant.

## Exact integer checks and limitations

R762HN_CHECK.cpp uses the ordered Port list, explicit integer minors, fraction-free Bareiss determinants, and two independent exact combinatorial computations: a forward integer dynamic program for CT F^k and Gram squares of half-history coefficient distributions. Six signed coordinates are encoded in independent biased 8-bit lanes in one uint64_t (bias 128; all absolute components <=56 for the tested 56 events), with no inter-lane carries. Counts fit uint64_t at the checked lengths. The source reports PASS with:

| Repetitions k | Events | Direct Z_k | Half-history Gram | Final DP states |
|---:|---:|---:|---:|---:|
| 2 | 28 | 313080 | 313080 | — |
| 4 | 56 | 12464855922680 | 12464855922680 | 2546073 |

R762HK previously supplied Z_1=104; this turn reused, not recalculated, its original source. The exact normalized proportions for k=2,4 are 0.001166313886642456 and 0.00017298462554993232 respectively. The leading formula gives 0.0016458292246487635 and 0.00020572865308109543, so exact-to-leading ratios are approximately 0.70864818 and 0.84083876. The finite computations corroborate the implementation but the displayed Fourier proof, not a numerical extrapolation, supports the limit.

Reproduce with:
~~~bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic R762HN_CHECK.cpp -o r762hn
./r762hn
~~~

Review=NOT_REVIEWED. No formal Result, Review, Working Truth, Foundation promotion, or primitive TRIADIC_CLOSURE_E admission is asserted.

## Next questions

Classify lattice rank/index and C for other fixed Port words, derive the rank-deficient lower-dimensional limit while preserving omitted native-axis state, decide full-length parity-even signability or find a genuine unsignable closed Port history, and construct primitive P000 TRIADIC_CLOSURE_E force/Cell/Link/Port/time/rotation permission independently of this composite candidate.
