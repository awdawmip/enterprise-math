# R284CL — Exact 64-level k-fold support-radius spectrum on the frozen finite Port population

Date: 2026-11-21 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. Independent portable scientific continuation after R284CK, not a formally claimed Task or an accepted native BRC theorem.

## Fixed inputs and distinction of observers

Frozen 34-bit Port encoding: p=17,179,869,143; D=(1,120,832,6,13,1,651,128); Z=(0,390,139,394,465,1,497,639). The population is all C in {1,2}^{4x4}, each exactly once (65,536 indexed matrices), with original 8-byte-big-endian codeword stream SHA-256 b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4. The existing 64 coarse Port fiber arcs are indexed by the six lower C entries at zero-based lower-index positions SELECT=(0,1,2,4,5,6). Each is the closed circular interval A_j=[a_j,a_j+w_j], 0<w_j<p/2, with arc bounds reconstructed exactly by the previous frozen determinant extrema. Original R284CK supplies the all-real-circle k-fold radius spectrum T_k=2rho_k; its population is uniform *all circular observation points*, not these 65,536 codewords.

Let x(C) be the frozen Port residue and, for any circular point x and any arc A, let d(x,A)=min_{z in A} dist_circle(x,z). Define the finite-population k-fold support threshold for k=1,...,64:

U_k = min {rho>=0 : for EVERY C in {1,2}^{4x4}, #{j : d(x(C),A_j)<=rho} >= k}.

These are radii rho, not doubled radii 2rho.

## Theorem A — exact finite-population spectrum

For each x=x(C), write the 64 integer distances d(x,A_j) in nondecreasing order d_(1)(x),...,d_(64)(x). Then

**U_k=max_{C in {1,2}^{4x4}} d_(k)(x(C))**, for every k in {1,...,64}.

In particular U_k is attained, is an integer, and each threshold is sharp: for every rho<U_k, the stored witness matrix C_k has fewer than k candidate arcs; for rho>=U_k every frozen matrix has at least k candidate arcs.

The 64 exact values of U_k, in ascending k order, are supplied in the companion machine certificate and checked by the companion Python program. Selected values:

| k | U_k finite-population radius | R284CK T_k full-circle doubled radius | T_k - 2 U_k |
|---:|---:|---:|---:|
| 1 | 0 | 440613304 | 440613304 |
| 2 | 539127606 | 1081059415 | 2804203 |
| 4 | 765801463 | 1531656496 | 53570 |
| 8 | 1236647378 | 2508437496 | 35142740 |
| 16 | 2474503698 | 4957452505 | 8445109 |
| 32 | 4633230194 | 9266634632 | 174244 |
| 48 | 6914295042 | 13828836673 | 246589 |
| 64 | 8436072374 | 16872276929 | 132181 |

The full exact comparison is **T_k - 2 U_k > 0 for all 64 k**. Its minimum is 786 (at k=54). Thus the finite codeword observer reaches every uniform k-fold support level strictly earlier than the full-circle observer. This is a discrete sampling/support advantage, not a new full-matrix error-correction result.

## Theorem B — exact zero-radius fiber signature distribution

For the finite frozen population at rho=0, the cardinality of the set of covering coarse arcs has distribution

| Covering fiber arcs | Number of complete matrices |
|---:|---:|
| 1 | 23178 |
| 2 | 23094 |
| 3 | 16964 |
| 4 | 2300 |
| total | 65536 |

No codeword lies outside all arcs, because its *own labeled coarse fiber arc* contains it. The exact average is 129458/65536 = 1.975372314453125 candidate groups, whereas the circle-uniform Haar expectation from R284CK is 24072341088/17179869143 ≈ 1.401194670787604. The populations differ; averaging the Haar and finite measures would erase the difference. R284CG independently identified exactly 23,178 matrices with singleton group signature, matching the first cell of this histogram.

The complete exact candidate-count profiles at selected larger radii are saved in the machine certificate. For rho=8,400,000,000, exactly 62,416 matrices are covered by all 64 arcs and the remaining 3,120 by 63.

## Proof and complete finite certificate

For integer x, integer 0<=a<p, integer 0<w<p/2, set delta=(x-a) mod p in [0,p). Then the exact circular point-to-closed-arc distance is

d(x,A)=0 if delta<=w; otherwise d(x,A)=min(delta-w,p-delta).

All values are integers, computed without floating-point approximation. Membership under a closed radius-rho expansion is equivalently d<=rho, which remains exact for arbitrary *real* rho>=0.

Fix x and order its 64 distances. There are at least k covering arcs if and only if rho>=d_(k)(x). Taking the maximum over the entire finite codeword population proves Theorem A and proves both quantifiers. When rho<U_k, use a maximizing codeword as a strict witness. Each witness's exact codeword, original enumeration index and U_k are preserved in the certificate. The codeword enumeration is 4 top bits in lexicographic product order, followed by 12 lower bits in lexicographic product order. At k=1 the radius is 0; own-fiber membership holds for all 65,536 matrices.

Theorem B follows by evaluating the same 64 exact distance predicates at rho=0 and counting over all 65,536 codewords. No probabilistic sampling is involved. The mean is the histogram's exact first moment.

## Validation and reproduction

1. Companion Python checker regenerates all 65,536 determinants and matches the frozen ordered SHA-256, reconstructs all 64 arcs, evaluates 65,536*64=4,194,304 exact point-to-arc distances, sorts each codeword's 64 distances, retains a first maximizing witness for each k, and produces the full 64-element threshold list and radius-dependent distributions.
2. Independent local checks evaluated 4,096 explicit 4x4 Leibniz determinants against the compressed cofactor expression and separately enumerated all 65,536 complete matrices to verify the 64 groupwise min/max determinant extrema against the arc formula. All passed.
3. The R284CK full-circle thresholds are an already stored independent-input result; exact integer comparison of the 64 supplied values against 2U_k proved strict domination, with smallest margin 786 at k=54. The finite-population theorem does not re-prove R284CK's independent kinetic-circle certificate.
4. The machine certificate includes U_1,...,U_64, the 64 sharpness witnesses, exact finite multiplicity counts and selected comparison profiles; the executable checker regenerates a more detailed JSON containing all sums of ordered distances and all declared profiles.

Validation scope is this frozen finite Port population and these exact 64 closed coarse arcs. It supplies an exact discrete readout statistic, not an identity of Port labels with native X6 Cells or provenance-bearing BRC states. No new CLAIM, Review, Result or Foundation admission is inferred.

## Next questions

- Build an exact order-statistic/rank-select index for the 64 population thresholds U_k without recomputing all 4,194,304 point-arc distances, while preserving witness matrices.
- Explain the smallest full-circle-to-codeword slack (786 doubled-radius units at k=54) structurally from gap endpoints and forbidden Port positions, without assuming codeword uniformity.
- Measure complete Port decoding cost under the *actual finite codeword distribution* (including the distribution of candidate groups) versus the circle-uniform observer, with separate initialization cost and loaded-memory accounting. Preserve labels/provenance for any future-operation-sensitive compression.

## Sources / preservation

Frozen origin and circle baseline:
- R284CK: https://github.com/awdawmip/enterprise-math/blob/48df38cba882f7aa3148f784300755dcf72759c6/research_notes/portable_direct/R284CK_EXACT_KFOLD_CIRCULAR_COVERING_SPECTRUM_20261121.md
- R284CK checker: https://github.com/awdawmip/enterprise-math/blob/d2962ea69f7e0d941565b051fc401500f4a1e12a/research_notes/portable_direct/R284CK_kfold_coverage_checker.py
- Finite checker: research_notes/portable_direct/R284CL_finite_codeword_support_checker.py
- Machine certificate: research_notes/portable_direct/R284CL_finite_codeword_support_certificate.json

Source authorship retains the historical R284C* portable lineage. Prior researcher ID EM-DIRECT-20B766 and Activity RA-617F40704F37299B15489DCA remain historical origin, not a claim that this execution owns the original native session capability. Current owner inventory read is separate and observation-only. This note is unpublished for mathematical review (NOT_REVIEWED).
