# Response-model transfer by singular-value perturbation and defect capacity

Record ID: `FINDING-EM-NT-RESPONSE-MODEL-TRANSFER-CAPACITY-20260906`
Type: `FINDING`
Status: `VERIFIED`
Effective: `2026-09-06`
Scope: `project:enterprise-math`
Projects: `enterprise-math`
Topics: `operator model; singular values; Weyl-Mirsky; Hilbert-Schmidt defect; effective rank; predictive response; prolate; BRC capacity`
Entities: `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA; T6_OPERATION_SAFE_QUOTIENT; FINDING-EM-NT-RESPONSE-OPTIMAL-SVD-REPAIR-20260906`
Sensitivity: `normal`
Confidence: `high`

## Statement

A complicated normalized future-response operator can inherit a finite effective-rank theorem from a simpler model without matching eigenvectors mode-by-mode. It is enough to bound the operator or Hilbert-Schmidt defect between the two responses.

This produces an explicit **extra-dangerous-mode capacity** from model error and is especially suited to transferring time-band/prolate spectral information into a target arithmetic response.

This is a composition of existing Enterprise capacity/quotient machinery plus standard singular-value perturbation theory, not a new top-level tool family.

## 1. Operator-norm transfer

Let `C` be the target compact response operator and `C0` a model response. Let singular values be decreasing:

`sigma_1 >= sigma_2 >= ...`.

If

`||C-C0|| <= eps`,

then the singular-value perturbation bound gives

`|sigma_j(C)-sigma_j(C0)| <= eps`

for every `j`.

For threshold `eta>eps`, define

`r_C(eta)=#{j:sigma_j(C)>=eta}`.

Then

`r_C(eta) <= r_C0(eta-eps)`.

Thus a model effective-rank theorem transfers directly once the response-model operator-norm error is below the desired threshold margin.

## 2. Hilbert-Schmidt defect-capacity transfer

Suppose only

`||C-C0||_HS <= E`.

Mirsky/Hoffman-Wielandt-type singular-value control gives

`sum_j |sigma_j(C)-sigma_j(C0)|^2 <= E^2`.

Fix `delta>0` and threshold `eta>delta`. Let

`r0=r_C0(eta-delta)`.

For every index `j>r0` with `sigma_j(C)>=eta`, one has

`sigma_j(C)-sigma_j(C0) > delta`.

Therefore if `m` such extra indices exist,

`m delta^2 <= E^2`,

hence

`r_C(eta) <= r0 + floor(E^2/delta^2)`

(up to the harmless strict/equality convention at the thresholds).

Interpretation:

`MODEL EFFECTIVE RANK + GLOBAL L2 OPERATOR DEFECT -> FINITE EXTRA REPAIR CAPACITY`.

The model need not approximate every singular vector; total defect can create only finitely many additional threshold-crossing directions.

## 3. Predictive-port meaning

This theorem should be applied to **normalized response operators**, e.g.

`C=A^(-1/2) B D^(-1/2)`,

not blindly to the old-state operator `A`.

The model `C0` must preserve the declared future-operation semantics. A good spectral model for `A` that ignores the old-to-future port `B` is not sufficient.

## 4. Prolate/time-band specialization

For a time-band concentration model `C0`, classical Landau-Pollak-Widom theory controls the singular/eigenvalue count through the Shannon number and the logarithmic plunge region.

To transfer that theorem to a Weil/RH response `C_L`, it is enough to prove one of:

- `||C_L-C0_L|| <= eps_L`, or
- `||C_L-C0_L||_HS <= E_L`,

with an error scale small enough relative to the response threshold of interest.

This is strictly weaker than proving convergence of individual eigenfunctions or exact equality of spectral projectors.

A particularly useful target is a bound that gives, for some fixed `eta<1`,

`r_(C_L)(eta) <= Shannon(L) + O(log Shannon(L)) + defect_capacity(L)`.

The final defect term is explicitly controlled by the model-response error rather than hidden in a qualitative approximation statement.

## 5. BRC / reuse resolution

Coverage verdict: `COMPOSE_EXISTING_TOOLS`.

- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`; `C0` is an admissible surrogate only for the declared future response and only with an explicit error lease.
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: `REUSE_APPLIED`; Hilbert-Schmidt error is converted into a finite count of additional unresolved/dangerous response directions.
- Standard singular-value perturbation / Mirsky theory supplies the quantitative transfer law.

BRC lesson:

`MODEL ERROR NEED NOT VANISH -> IT CAN BE RETAINED AS A FINITE REPAIR-CAPACITY DEFECT`.

This is preferable to either pretending the model is exact or retaining the entire raw state.

## 6. Relation to certified inertia counting

`FINDING-EM-NT-RESPONSE-INERTIA-THRESHOLD-CERT-20260906` gives a direct way to certify `r_C(eta)` for finite sections by block inertia.

Therefore the practical validation loop is:

1. derive a model `C0` and theoretical response-rank bound;
2. derive an operator/HS defect estimate;
3. predict an upper bound for `r_C(eta)`;
4. independently certify finite-section threshold counts through interval `LDL*` inertia;
5. use discrepancies as falsifiers for the model-transfer estimate.

## 7. Hard boundaries

1. Hilbert-Schmidt control gives a count defect, not uniform singular-value control.
2. If `E/delta` grows faster than the model effective dimension, the transfer may be useless even though mathematically correct.
3. Finite-section HS/operator error must include truncation tails before it is an infinite-operator theorem.
4. Model closeness of old-state operators does not imply normalized-response closeness when inverse square roots amplify near-null modes; the comparison must be made after the correct response normalization or with a theorem controlling that amplification.
5. This theorem transfers a spectral-capacity bound; it does not itself prove the threshold-one positivity required for RH.

## Provenance

- Source kind: `exact mathematical derivation from standard singular-value perturbation theory + current RH/BRC response audit`
- Source reference: `FINDING-EM-NT-RESPONSE-OPTIMAL-SVD-REPAIR-20260906; FINDING-EM-NT-RESPONSE-INERTIA-THRESHOLD-CERT-20260906; classical Landau-Pollak-Widom time-band limiting`
- Observed/recorded at: `2026-09-06`

## Relations

- Supersedes: `none`
- Superseded by: `none`
- Updates: `HYPOTHESIS-EM-NT-RH-LANDAU-WIDOM-REPAIR-BAND-20260906`
- Conflicts with: `none`
- Related: `FINDING-EM-NT-SPECTRAL-TAIL-FESHBACH-CERT-20260906; FINDING-EM-NT-RESPONSE-INERTIA-THRESHOLD-CERT-20260906`
