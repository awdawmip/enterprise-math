# Response-optimal SVD repair and predictive effective rank

Record ID: `FINDING-EM-NT-RESPONSE-OPTIMAL-SVD-REPAIR-20260906`
Type: `FINDING`
Status: `VERIFIED`
Effective: `2026-09-06`
Scope: `project:enterprise-math`
Projects: `enterprise-math`
Topics: `predictive quotient; response operator; singular values; SVD; Eckart-Young; optimal repair subspace; Schur complement; BRC`
Entities: `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA; T6_OPERATION_SAFE_QUOTIENT; FINDING-EM-NT-SPECTRAL-TAIL-FESHBACH-CERT-20260906`
Sensitivity: `normal`
Confidence: `high`

## Statement

For a positive block problem, the mathematically optimal finite repair carrier is determined by the **normalized future-response operator**, not in general by the lowest eigenmodes of the old-state operator.

This yields a precise `RESPONSE_EFFECTIVE_RANK` theorem and a BRC rule:

`REPAIR DIMENSION IS FUTURE-OBSERVER RELATIVE`.

It is a composition/extension of existing quotient/capacity machinery, not a new top-level tool family.

## 1. Whitened response operator

Let

`M = [[A,B],[B*,D]]`

with `A>0` and `D>0`. Define

`C := A^(-1/2) B D^(-1/2)`.

Congruence by `diag(A^(-1/2),D^(-1/2))` gives

`M ~ [[I,C],[C*,I]]`.

Hence

`M>0 <=> ||C||<1`.

The normalized old-to-future response is

`C C*` on the old side and `C* C` on the future side.

Thus all dimensions and truncations relevant to the declared next operation should be measured relative to `C`, not to `A` or `D` separately.

## 2. Optimal rank-r old repair subspace

Assume `C` is compact (finite matrices are the immediate special case) with singular values

`sigma_1 >= sigma_2 >= ... >=0`.

For any rank-`r` orthogonal projector `P` on the old whitened space, the discarded future-visible tail is

`||(I-P) C||`.

By the Schmidt/Eckart-Young min-max theorem,

`inf_(rank P=r) ||(I-P)C|| = sigma_(r+1)(C)`.

The infimum is attained by choosing `P` to span the first `r` **left singular vectors** of `C`.

Therefore the response-optimal finite repair carrier is the dominant left singular subspace of the normalized cross-coupling.

A low-energy eigenspace of `A` is optimal only when an additional structural theorem aligns it with those singular directions.

## 3. Predictive effective rank

For a tolerance `0<eta<1`, define

`r_resp(eta) := min { r : sigma_(r+1)(C) < eta }`.

Then a rank-`r_resp(eta)` response-optimal port captures the normalized coupling up to operator-norm tail `<eta`.

Equivalent counting form:

`r_resp(eta) = #{ j : sigma_j(C) >= eta }`

when the threshold is not itself an accumulation ambiguity.

This is the natural BRC **predictive effective dimension** for the declared old-to-future operation.

It differs from:

- raw Hilbert-space dimension;
- number of low eigenvalues of `A`;
- numerical rank of `B` without energy normalization;
- Shannon/time-band dimension unless a theorem identifies the normalized response with a time-band operator.

## 4. Relation to finite Feshbach certification

Choosing the optimal response subspace does not by itself prove positivity; it supplies the best finite carrier for the future coupling.

Combined with `SPECTRAL_TAIL_FESHBACH_CERTIFICATE`, one may either:

1. use a spectral projector of `A` because it gives a direct energy denominator and then prove its response tail is small; or
2. work in whitened coordinates, retain the dominant singular directions of `C`, and certify the resulting finite block directly.

The second route is optimal for approximation of the declared normalized response; the first may be easier to certify analytically when `A` has a known spectral theorem.

## 5. BRC / reuse resolution

Coverage verdict: `COMPOSE_EXISTING_TOOLS`.

- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`. The SVD chooses the coarsest rank-constrained repair that best preserves the declared future linear operation in operator norm.
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: `REUSE_APPLIED` conceptually for effective dimension / first unresolved singular scales.
- standard compact-operator/SVD/Eckart-Young theory supplies the exact approximation theorem.

BRC rule:

`STATE-ENERGY IMPORTANCE != FUTURE-PORT IMPORTANCE`.

A mode with small old energy may be irrelevant to the future port, while a higher-energy mode can be essential if the coupling sees it strongly.

## 6. RH square-shell consequence

For the square-shell Weil step define

`C_n=A_n^(-1/2) B_n D_n^(-1/2)`.

The exact Schur criterion is

`A_(n+1)>0 <=> ||C_n||<1`

assuming `A_n,D_n>0`.

The new candidate Landau-Widom statement should therefore be phrased in terms of the **singular-value distribution of `C_n` or an analytically equivalent response operator**, not simply the low-eigenvalue count of `A_n`.

The 2026-09-06 floating low-mode experiments showed that keeping `A_n`'s first `r` eigenmodes restores shell coercivity near a dimension numerically comparable to `4 n^2 log n` for `n=2,3,4`. A first whitened-response probe also showed a cluster of singular values extremely close to one. These observations motivate, but do not prove, a response-side Landau-Widom plunge.

The sharpened research hypothesis is:

`NORMALIZED WEIL RESPONSE C_L HAS A PROLATE-LIKE SINGULAR-VALUE TRANSITION AT RESPONSE EFFECTIVE DIMENSION ~4 L exp(2L)`.

This replaces the stronger and less justified statement that the old Weil operator itself must have exactly that low-mode count.

## 7. Hard boundaries

1. `ECKART-YOUNG OPTIMAL APPROXIMATION != POSITIVITY PROOF`.
2. The response-optimal projector is future-operation dependent; a different shell/operation may require a different subspace.
3. SVD of a finite truncation is not the singular spectrum of the infinite operator without certified truncation/tail error.
4. A cluster of singular values near one is critical behavior, not evidence that they remain below one.
5. Time-band/Shannon dimension cannot be imported without identifying or comparing the actual normalized response operator to the prolate concentration operator.

## Provenance

- Source kind: `exact operator-algebra derivation + standard Schmidt/Eckart-Young theorem + 2026-09-06 RH response audit`
- Source reference: `FINDING-EM-NT-SPECTRAL-TAIL-FESHBACH-CERT-20260906; HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`
- Observed/recorded at: `2026-09-06`

## Relations

- Supersedes: `none`
- Superseded by: `none`
- Updates: `HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`
- Conflicts with: `none`
- Related: `FINDING-EM-NT-SPECTRAL-TAIL-FESHBACH-CERT-20260906; FINDING-EM-NT-RH-SQUARE-SHELL-MELLIN-HAAR-SCHUR-20260905`
