# D25/LIFT — diagonal-base semilinear top-digit gauge resonance and complete square-block observer

2026-10-25 | **TASK_RESEARCH portable author derivation** | AUTHOR-PROVED / AUTHOR-CHECKED; **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM / NO_NEW_NATIVE_CHECKPOINT**.

## Authority, provenance and exact scope

Parent: D25/LIFT/JT2 **OPEN**. Existing Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Preserve **frozen scientific Source pin** `c47e13e4aba0e006366f989d6334d443f6333ae3`. Previously verified native checkpoint `220ee1ba360f21152912d0b4c1abdf867a1e4496` already contains the rank-one ordinary-Hesse norm/Hilbert-90 author units. Follow-on project-native portable proofs `8960b1d0453f0ac74400843b61faa5df5e798e3a` and `a1105620739118fffdc40d4bc73c128736b706d1` established, respectively, a rank-two information-loss witness and the **identity-base** last-digit classification `D_+`. Those units are **consumed, not recredited**.

The new question is what changes when the base semilinear matrix is an *arbitrary invertible diagonal matrix*, rather than the identity. This is a finite-ring conditional structural lemma for a hypothetical original-class source module; it does **not** establish that the actual CM/divided-power module has any particular rank, basis or Frobenius matrix.

Let `p` be odd with `(2/p)=-1` (in particular `p=13,19 mod 24`), `r>=2`, `A=Z/p^r Z`, `R=A[T]/(T^2-2)`, `sigma(a+bT)=a-bT`, `K=R/pR=F_{p^2}`, and `q=p^{r-1}`. Work over the *free rank-n coefficient module*, not over an Enterprise native spatial plane. Fix `C0=diag(a_1,...,a_n)` with `a_i in R^×`. Set
```
C_D=C0(I+qD),     F_D(v)=C_D sigma(v),
P_X=I+qX,         C_D' = P_X^(-1) C_D sigma(P_X),
S_D=F_D²=C_D sigma(C_D),    S0=C0 sigma(C0)=diag(s_i),
s_i=N(a_i) in A^×,    K_D=(S_D-S0)/q mod p in M_n(K).
```
Here `D,X` are matrices over `K`; choose arbitrary lifts to `R`. Multiplication by `q` makes all lifts equivalent. Let bars denote mod-`p` reductions and define `lambda_ij=bar(a_j)/bar(a_i)` in `K^×`.

## Theorem — complete diagonal-base top-digit gauge classification

For *every* `n>=1` and the declared `p,r,C0`, the following are equivalent:

1. `C_D` and `C_D'` are related by a **near-identity** semilinear change of basis `P_X=I+qX`.
2. For **every pair** `(i,j)` with `bar(s_i)=bar(s_j)` in `F_p`, the full quadratic-square coefficient `(K_D)_ij` equals `(K_D')_ij` in `K`.
3. The full squares `S_D` and `S_D'` are similar under a near-identity `P_Y=I+qY`.

Thus the **resonant blocks**
```
RES(C_D) := ((K_D)_ij : bar(s_i)=bar(s_j))
```
are a *complete* observer for this explicitly bounded gauge problem. If `bar(s_i)!=bar(s_j)`, the `(i,j)` last-digit perturbation is pure near-identity gauge and has no independent orbit invariant. For the identity base `C0=I`, every pair is resonant, and the previous full even-matrix invariant `D_+` is recovered; it is **not** a base-independent invariant outside this scope.

### Constructive proof

Since `q²=p^{2r-2}=0 mod p^r` and `pq=0`, matrix multiplication is exact:
```
P_X^(-1) C_D sigma(P_X)
    = C0 [ I + q(D + sigma(X) - C0^(-1) X C0) ],
D'_ij-D_ij = L_ij(X_ij),    L_ij(x)=sigma(x)-lambda_ij*x.
```
Put `lambda=lambda_ij`, `z=D'_ij-D_ij`. All norms below are computed in `F_p` from `K`.

**Nonresonant case.** `N(lambda)=bar(s_j)/bar(s_i) !=1`. The `F_p`-linear map `L_ij` is invertible, with the explicit solution
```
x = [sigma(z)+sigma(lambda)*z] / [1-N(lambda)].
```
Indeed `sigma(x)-lambda*x=z` follows by applying `sigma` to the equation and eliminating `sigma(x)`. Hence **every** off-block last digit is removable.

**Resonant case.** `N(lambda)=1`. Define the twisted trace `Q_lambda(z)=z+lambda*sigma(z)`. Then
```
z is in image(L_ij)  <=>  Q_lambda(z)=0.
```
Necessity follows by substituting `z=sigma(x)-lambda*x`. Sufficiency is constructive: if `Q_lambda(z)=0`, choose `x=-z/(2*lambda)`; using `sigma(lambda)=lambda^(-1)` gives `L_ij(x)=z`. No noncanonical division by `p`, no assumed Frobenius normal form and no extension to uncontrolled gauges are involved.

To identify the *observable* obstruction, expand the **full** square:
```
S_D = S0+qK_D,
(K_D)_ij = bar(a_i)*sigma(bar(a_j))*D_ij + bar(s_i)*sigma(D_ij).
```
When `bar(s_i)=bar(s_j)`, one has `N(lambda)=1`, and
```
(K_D)_ij = bar(s_i)*sigma(lambda_ij)*
            [ D_ij + lambda_ij*sigma(D_ij) ].
```
The prefactor is a unit, so equality of the resonant `K_ij` is **exactly** the solvability condition for each `L_ij(X_ij)=D'_ij-D_ij`. Entrywise explicit solutions give the same `X` simultaneously; this proves (2) => (1). The reverse implication holds because `Q_lambda(L_ij(X_ij))=0`.

Finally, under the near-identity gauge,
```
K_D' = K_D + bar(S0)*X - X*bar(S0),
(K_D')_ij=(K_D)_ij+(bar(s_i)-bar(s_j))*X_ij.
```
Therefore the resonant `K_ij` are exactly the fixed entries under near-identity **square** similarity, and nonresonant entries can be adjusted freely. This proves (2) <=> (3), concluding the theorem. **Only similarity, not equality of the fixed-coordinate matrices, is claimed.**

## Two explicit contrasting certificates

**Universal contrast at the same odd prime.** For any declared `p,r` put `C0=diag(2+T,1)`, whose square-base norm spectrum is `(2,1)`; these two eigenvalues remain distinct modulo `p`. For `D=E_12` take `X=(-4-T)E_12`. Directly, with `lambda=(2+T)^(-1)=(2-T)/2`,
```
sigma(-4-T) - lambda*(-4-T) = -1.
```
Hence `P_X^(-1) C0(I+qE_12) sigma(P_X)=C0` **exactly modulo `p^r`**: the even off-diagonal top-digit perturbation is pure gauge. Conversely, around `C0=I`, the *same* `D=E_12` has `S_D=I+2qE_12 != I` and cannot be gauged to the identity; this is the previously proven resonant obstruction. The correct observer depends on the *base-square norm spectrum*, not on the raw parity of `D` alone.

**p=373 ordinary-Hesse conditional check.** Reuse the previously **native-published ordinary-Hesse coefficient**, not a CM Frobenius identification:
```
alpha = 92060+21788*T (mod 139129),
N(alpha)=122102 (mod 139129),  N(bar(alpha))=131 (mod 373).
```
Let `C0=diag(alpha,1)`, `D=E_12`, and `X=(143+280T)E_12`. Then `lambda_12=bar(alpha)^(-1)=8+238T (mod 373)`, `N(lambda_12)=168 !=1`, and
```
sigma(143+280T) - (8+238T)(143+280T) = -1 (mod 373).
```
The exact author-calculated matrices modulo `373²=139129` satisfy
```
P_X[1,2]=53339+104440T,
S_D[1,2]=22380+57442T = 373(60+154T),
P_X^(-1) C_D sigma(P_X) = C0.
```
Thus the prior **nonzero raw square off-diagonal** is *not by itself* an invariant away from the resonant identity base: `bar(s_1)-bar(s_2)=130` permits its exact conjugation away. This refines, rather than contradicts, the older rank-two identity-base nilpotent witness. It is not an original `H0/B0` observation.

## Exact author verification and method reuse

Standalone exact checker: [`20261025_hourly_d25_diagonal_norm_resonance_check.py`](20261025_hourly_d25_diagonal_norm_resonance_check.py), immutable code blob `6ec73aad8c8dd90944b610c00654e8da2f01b815`. It uses standard-library integers and pair arithmetic in `R_r`; author execution succeeded for all six uniform `p in {13,19,373}, r in {2,3}` comparisons, as well as the `p=373` Hesse conditional lifts `r=2,3` and the explicit `p²` square digits. There is **no exhaustive native-class check and no independent proof review**. The universal conclusion rests on the displayed exact algebra, not the finite samples.

Existing-method resolution: `COMPOSE_APPLIED` using the precise prior identity-base finite-ring gauge theorem and earlier rank-one norm law, combined with current `T0_BRC` provenance-aware observer/fiber discipline. The carrier here is a labeled finite-matrix branch family over exact rings. The observer is the resonance-restricted `RES`, with future operations restricted to near-identity semilinear gauge and square similarity. Its sufficiency is proved above. The coarser trace/determinant projection remains unsafe inside equal-norm blocks; the raw even `D_+` projection is unnecessarily fine when square-base norms differ. This is *not* a claim of positive-mass cancellation, two-dimensional native Enterprise geometry, or an all-purpose BRC tool.

## Immutable frontier, status and next action

**Completed in this portable author unit:** rank-`n` diagonal-base near-identity semilinear orbit theorem, explicit inverse in nonresonant blocks and exact twisted-trace obstruction in resonant blocks; proof of square-conjugacy completeness at the stated top-digit precision; universal identity-vs-separated-norm countercontrast and `p=373` exact Hesse comparison. These are **UNREVIEWED / NOT_ADMITTED** author results until actual independent Source review.

**Native control boundary:** this genuine Research lane attempted a fresh scoped `em_control_task` read for this exact Task; the v0.6.11 Gateway returned `CONTROL_QUOTA`. Its separate `recovery_status` operation was listed by `em_status` but not exposed as an invocable native tool in this host. No own current winning CLAIM/run/session was freshly authorized; no `session_start`, `continuation_prepare`, `CLAIM`, `OPEN`, `publish_checkpoint`, `freeze` or native CM experiment is asserted. The most recently independently verified historical Source checkpoint remains `220ee1ba...` and the canonical HANDOFF in Issue #240. This proof is an ordinary project artifact, not a replacement Source checkpoint. Existing support responsibility is Issue #1558; `CONTROL_QUOTA` is **not** `NO_DISPATCH`.

**Smallest next scientific unit:** first obtain the actual source-authenticated same-prime, same-original-class divided-power `H0/B0` module and exact `[X]U mod p²`, establish actual rank, sigma direction, operator invertibility, basis and normalization. *Only if* its real mod-`p` coefficient matrix can legitimately be diagonalized over the stated coefficient field should one compute its diagonal `s_i=N(a_i)` and resonant blocks as above. Otherwise do **not** impose this diagonal classification; retain the full matrix `C sigma(C)` and original signed/odd ports. Compare the original `omega+6 nabla_lambda omega`, `kappa` and `Delta_p-R_p` only across a proven source/observer map. Original native CM experiment remains `NOT_RUN`; D25/LIFT/JT2 **OPEN**. Do not repeat the already completed WZ/Green or ten-million-prime scan, previous Hilbert-90, identity-base even-jet, or this diagonal theorem.
