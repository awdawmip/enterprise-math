# R224 — Generic sharpness of the 250-dimensional Markov support-ideal recurrence bound

Date: 2026-11-17 Asia/Shanghai. Classification: AUTHOR_PROVED / EXACT_MACHINE_CERTIFIED_FINITE_WITNESS / NOT_REVIEWED. Native BRC EffectHistogram: NOT_EXECUTED.

## Scientific origin and declared scope

Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Direct inputs: R215 Stirling-fibre ideal T_r, R221 killed Markov-block source-survival representation, and R223 observable reduction. This is a scalar source-support query on the abstract paired-event monoid J_(12,6,2), not a physical X6 transition, complete 21-bit event/affine action, positive mass histogram, signed amplitude or provenance-preserving BRC branch carrier.

Set m=12, k=6, L=2, with source alphabet {0,...,6}, where 0 is neutral. Let pi=(1/7,...,1/7) be the initial probability row, not necessarily stationary for P. For each U subseteq {1,...,6}, put D_U={0} union U, P_U=P[D_U,D_U] and W_r=r!12^2 sum_(j=0)^min(r,2) Stirling2(3,j+1). Then

  W=[144,576,1440,4320,17280,86400,518400]
  f_n=E[F_n]=sum_U W_|U| pi_U P_U^(n-1)1,  n>=2.            (1)

The 64 killed blocks have total dimension D=sum_U(|U|+1)=256. For U=all six labels, pi P^(n-1)1=1 by row-stochasticity; that block contributes the scalar constant W_6. Replacing its original 7 dimensions by 1 gives an explicit rational linear realization of dimension 250. Therefore any rational P and any initial probability distribution have scalar recurrence degree at most 250.

R223 proved the exchangeable Markov interior family has order 7. The present theorem shows that 250 is the actual generic and worst-case order for an unrestricted positive rational Markov kernel.

## Explicit positive rational witness

Set P_ij=M_ij/d_i, where the rows of M are

  62 38 60 37 72 74 49
  79 61 12 35 39 30 14
  47 37 16 87 62 44 39
  63 63 72 96 44 19 27
  30 42 83 62 82 52 75
  45 71 49 82 79 46 86
  11 53 67 59 35  1 60

and row sums are d=(392,270,332,384,426,458,286). Thus P is strictly positive, rational and row-stochastic, with no extra structural assumptions.

Define the exact rational 250x250 Hankel matrix

  H_(i,j) = f_(2+i+j),  0<=i,j<250.                         (2)

A standard-library deterministic exact certificate computes the two reductions of H and returns:

  prime p=1000000007: rank(H mod p)=250, det(H) mod p=844129038
  prime p=1000000009: rank(H mod p)=250, det(H) mod p=225185489.

Every row sum d_i and 7 is coprime to both primes. The rational denominators in the sequence consist of products of those row sums and 7, so reduction modulo p preserves all operations. If det(H)=0 over Q, its image modulo each prime would be zero. Both nonzero residues therefore prove det(H) != 0 in Q.

Since rank(H) >=250 and the realization dimension is <=250, the rank is exactly 250. A constant-coefficient recurrence of degree d forces all Hankel matrices to have rank <=d. Thus the **minimal rational scalar recurrence degree for this exact source-label model is 250**. This is a witness with 49 small positive integers, not a numerical floating-point fit.

## Generic maximality theorem

For fixed pi and variable P in the affine space of row-stochastic 7x7 matrices, every f_n from (1) and the determinant (2) are polynomial functions of the matrix entries. The determinant is not identically zero, since the witness above is nonzero. Its nonvanishing locus is therefore nonempty Zariski open and Euclidean dense inside the open set of strictly positive row-stochastic matrices.

On that locus, the minimal scalar recurrence degree equals 250. Consequently 250 is **both worst-case sharp and generically attained** for the six-source depth-two ideal observer under freely varying positive Markov kernels with uniform initialization. At the same time R223's exchangeable kernel has true order 7, a proven strict low-rank symmetry stratum.

## Independent consistency test and reproducibility

The companion script R224_generic_markov_full_hankel_certificate.py uses Python standard-library integer modular arithmetic and Fraction only. It constructs all 64 killed blocks, evaluates 502 consecutive survival expectations, and performs pivoted elimination of the 250x250 Hankel matrix at both stated primes. Additionally, the first four exact rational f_n are independently computed by (a) propagation of Markov states (current source label, cumulative seen-source mask) with R215 ideal T_r, and (b) killed-block Boolean survival with W_r; they agree exactly.

R224_verification.json contains the entire 7x7 integer witness, row sums, determinants, modular sequence prefixes and four exact rational terms. Re-running requires no external libraries, remote services or unstated data. The signed/phase-sensitive native BRC EffectHistogram, explicit ports, joint source provenance and cross-moments were not exercised; the certificate applies only to its specified scalar query.

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED; formal Task CLAIM, Result or Foundation admission: NONE.

## Next problems

1. Compare a 250-dimensional reduced linear transfer to direct support/current-label state propagation (256 reachable states: one neutral-current option plus |S| nonneutral-current options per source-support set S) with full input-conversion, exact integer bit cost and query recovery.
2. Classify exact low-Hankel-rank strata (exchangeable, partially lumpable, reversible) in the full positive stochastic family; a 250→7 reduction is substantive only under its stated source symmetry.
3. Integrate the support readout with native typed BRC EffectHistogram while retaining signs, ports, branch identity, multiplicity and positive rational weights as distinct carriers.
