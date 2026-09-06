# Response singular-value threshold by block inertia

Record ID: `FINDING-EM-NT-RESPONSE-INERTIA-THRESHOLD-CERT-20260906`
Type: `FINDING`
Status: `VERIFIED`
Effective: `2026-09-06`
Scope: `project:enterprise-math`
Projects: `enterprise-math`
Topics: `Schur complement; singular values; generalized eigenvalues; inertia; LDL; interval certification; response rank; predictive quotient`
Entities: `T2_BLOCK_FINITE_CERTIFICATE; T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA; T6_OPERATION_SAFE_QUOTIENT; FINDING-EM-NT-RESPONSE-OPTIMAL-SVD-REPAIR-20260906`
Sensitivity: `normal`
Confidence: `high`

## Statement

The number of normalized response singular values above any threshold can be certified **without explicitly forming inverse square roots or generalized eigenvectors**. It is exactly the negative inertia of a simple thresholded block matrix.

This gives a numerically stable and interval-certifiable interface for `RESPONSE_EFFECTIVE_RANK`.

## 1. Setup

Let

`M = [[A,B],[B*,D]]`

with finite-dimensional Hermitian `A>0`, `D>0`, and define the whitened response

`C=A^(-1/2) B D^(-1/2)`.

For a threshold `eta>=0`, set

`M_eta := [[eta^2 A, B], [B*, D]]`.

## 2. Inertia threshold theorem

Schur complement with respect to `D` gives

`M_eta ~ D direct_sum [eta^2 A - B D^(-1) B*]`

under an invertible block congruence.

Since `D>0`, Sylvester's law of inertia implies

`n_-(M_eta) = n_-[eta^2 A - B D^(-1)B*]`.

Congruence by `A^(-1/2)` turns the second block into

`eta^2 I - C C*`.

Therefore

`n_-(M_eta) = #{ j : sigma_j(C)^2 > eta^2 }`.

For `eta>=0`, equivalently

`#{ j : sigma_j(C) > eta } = n_-(M_eta)`.

This is exact, including multiplicity, provided no singular value lies exactly at the threshold when a strict count is required. Threshold equality corresponds to zero inertia/pivots and should be reported explicitly.

## 3. Important special cases

### eta=1

`M_1=M`, so

`#{sigma_j(C)>1}=n_-(M)`.

Thus ordinary block positivity is the threshold-one response certificate.

### effective-rank query

For `0<eta<1`, a certified `LDL*` factorization of `M_eta` determines the response effective rank

`r_resp(eta)=#{sigma_j(C)>=eta}`

up to explicit handling of equality at `eta`.

No tiny eigenvalue of `A` needs to be inverted or square-rooted.

## 4. Generalized-eigenvalue interpretation

The squared singular values `mu=sigma^2` are generalized eigenvalues of

`B D^(-1)B* u = mu A u`.

The inertia formulation is preferable for proof certification because it replaces an ill-conditioned eigenvector computation with a sign count of a Hermitian block matrix.

This is particularly useful when `A` has extremely small positive eigenvalues: direct formation of `A^(-1/2)` can lose hundreds of digits, while a high-precision/interval `LDL*` can certify inertia directly.

## 5. Certified computational architecture

Recommended checker:

`INPUT: interval/rational enclosures for A,B,D and threshold eta`

`-> BUILD M_eta`

`-> INTERVAL LDL* / symmetric-indefinite factorization`

`-> CERTIFY pivot/block signs`

`-> RETURN (n_pos,n_zero,n_neg)`

`-> RESPONSE_RANK_CERT = n_neg`.

If a pivot interval contains zero, increase precision or use a verified block-pivot/inertia algorithm; never guess the sign.

This architecture follows the project rule

`UNTRUSTED HEAVY NUMERICS -> EXPLICIT FINITE MATRIX -> SMALL CERTIFIED INERTIA CHECKER`.

## 6. BRC / reuse resolution

Coverage verdict: `COMPOSE_EXISTING_TOOLS`.

- `T2_BLOCK_FINITE_CERTIFICATE`: `REUSE_APPLIED` for block Schur/inertia certificates.
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`; the counted singular modes are exactly the distinctions required by the declared normalized future response.
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: `REUSE_APPLIED` for threshold/effective-dimension readout.
- standard Sylvester inertia law and Schur complement supply the theorem; no new top-level family.

## 7. RH square-shell use

For the square-shell Weil step,

`C_n=A_n^(-1/2)B_nD_n^(-1/2)`.

Direct double-precision SVD becomes unreliable because `A_n` has extremely small positive modes. Instead, for thresholds such as `eta=0.9,0.99,1`, construct

`M_(n,eta)=[[eta^2 A_n,B_n],[B_n*,D_n]]`

and certify its inertia.

This directly answers:

`HOW MANY RESPONSE MODES ARE WITHIN eta OF THE SCHUR CRITICAL BOUNDARY?`

and provides a stable test of any proposed Landau-Widom response-rank law.

## 8. Hard boundaries

1. Finite-section inertia is not infinite-operator inertia without a certified truncation/tail theorem.
2. If a singular value equals the threshold, strict `>` versus `>=` must be separated using the null inertia.
3. A count below one does not prove the largest singular value is below one unless the threshold-one matrix itself is certified positive semidefinite/definite.
4. Numerical `LDL` is not a proof unless pivot/inertia signs are rigorously enclosed.

## Provenance

- Source kind: `exact Schur-complement and Sylvester-inertia derivation`
- Source reference: `FINDING-EM-NT-RESPONSE-OPTIMAL-SVD-REPAIR-20260906; standard Hermitian generalized-eigenvalue theory`
- Observed/recorded at: `2026-09-06`

## Relations

- Supersedes: `none`
- Superseded by: `none`
- Updates: `FINDING-EM-NT-RESPONSE-OPTIMAL-SVD-REPAIR-20260906`
- Conflicts with: `none`
- Related: `FINDING-EM-NT-SPECTRAL-TAIL-FESHBACH-CERT-20260906; HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`
