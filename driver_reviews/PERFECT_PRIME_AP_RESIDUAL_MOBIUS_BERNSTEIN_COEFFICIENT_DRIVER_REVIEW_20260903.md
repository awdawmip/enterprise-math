# Driver Review — Perfect Prime AP residual Möbius–Bernstein coefficient interface

Driver-ID: `EM-DVR-P8H4Q2`
Review-ID: `DR-23D512CBD58341BB6BDC`
Task: `RS-PERFECT-PRIME-AP-RESIDUAL-MOBIUS-BERNSTEIN-COEFFICIENT-POSITIVITY`
Publication: `TP2-8C910B14D7B854905F6E`
Result: `RR-23D512CBD58341BB6BDB`
Execution: `ER-D37BD9F8D1CA513EBBF2`

## Disposition

`ACCEPTED / EXACT_INTERFACE_REDUCTION / FOLLOWUP_TASK`.

The Result is accepted at its exact declared strength. It does not prove all-`m` coefficient positivity of `Bhat_m`, and it does not prove the parent cofactor/determinant nonvanishing theorem. It does prove a new all-`m` algebraic interface that reduces the remaining coefficient-sign problem to a signed-secant finite-difference condition.

## Envelope audit

The immutable Result record is Git blob `e5ed3c63d3f9cc0449bf6d6e1ba7efee270fa1b2`, with independently reconstructed SHA-256 `c9e89b1b54d21e196ac6ba23a810d4f701bedc9b879b9d3d2fee8cb3dea40a21`.

Its manifest resolves to the declared Git blobs:

- Return: `19a0bcf5eee3c6100443d66ed9a53d2979a5ace0`;
- checker: `8081c1908629f4f7bb0a52c2061e73885bda17ea`;
- signed-secant/Hausdorff certificate: `8b0360da2ad197f1d8595bff7d4de92d63a95d06`;
- execution record: `bf87f5c9ad787ea4d67852f652723951f3717925`.

The taskbook binding is `290e507c7bf7a651b2f3608ced64ff09de47bed5`. The execution record uses an extra `record_state=CLAIM_INTENT` label, but the active execution contract does not make that field authoritative or required; all required claim/publication/researcher/branch/base/output bindings match the authorized Issue #240 CLAIM.

## Accepted all-m structural reduction

Put `n=m-1`, `D=2m-1`, and `d=n(2m-3)`. In the accepted gauge-fixed atomic Gram representation, every nonzero `D`-atom Cauchy–Binet basis must meet every outer `j`-group. If `k_j` atoms are selected in group `j`, then

`sum_j (k_j-1)=n`.

After choosing one reference layer in every group and subtracting reference rows, the full atom minor factors into a fixed outer Vandermonde factor and an `n x n` within-group secant-difference determinant `Delta_I`. Hence

`(det R_I)^2 = V_y^2 (det Delta_I)^2`.

For each nonzero basis `I`, if `A_I` is the sum of selected layer indices, the combinatorics gives

`n <= A_I <= n(D-1)`.

Therefore every individual Cauchy–Binet contribution already contains `x^n(1+x)^n`. The accepted double-endpoint factor is termwise, not a cancellation artifact.

After dividing the endpoint factor, the Result proves the exact all-`m` signed squared-secant Bernstein expansion

`Bhat_m(x) = (1/V_x^2) sum_I eps_I Gamma_I x^(a_I) (1+x)^(d-a_I)`

with `Gamma_I>0`, `a_I=A_I-n`, and both signs genuinely present.

Equivalently,

`q_(m,a) = (1/V_x^2) sum_(I: A_I=n+a) eps_I Gamma_I`

and

`[x^k] Bhat_m(x) = sum_(a<=k) q_(m,a) binom(d-a,k-a)`.

## Accepted finite-difference equivalence

Define

`h_(m,a)=(-1)^a q_(m,a)/binom(d,a)`.

The Result proves algebraically

`[x^k] Bhat_m(x)/binom(d,k) = (-1)^k Delta^k h_(m,0)`.

Thus the original strict coefficient-positivity target is exactly equivalent to

`HCM0(m,k): (-1)^k Delta^k h_(m,0) > 0`

for every `m>=2` and `0<=k<=d`.

This equivalence is accepted as an all-`m` theorem.

The stronger shifted condition

`(-1)^k Delta^k h_(m,r)>0`

for all admissible `r,k` is **not** accepted beyond finite evidence. Exact rational regression verifies it only for `2<=m<=10`. No bounded census, alternating-sign observation, moment heuristic, or continuity argument is promoted.

## Route status

Freeze as resolved:

- the coefficient problem now has a precise signed-secant Bernstein formula;
- the target is exactly the HCM0 initial finite-difference row;
- full finite Hausdorff complete monotonicity is only a stronger candidate route.

Remain OPEN:

- all-`m` HCM0 positivity;
- all-`m` coefficient positivity of `Bhat_m`;
- the parent Perfect Prime critical-cofactor/nonvanishing objective.

A failure of full shifted Hausdorff monotonicity would not by itself refute HCM0 or the parent determinant theorem.

## Successor decision

Publish one P0/HIGH continuation `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT` / `TP2-7A2D91C5E40B836F19D2`.

The successor must attack the new arithmetic interface, not restart canonical flags, inertia, generic block-LDL, or bounded interpolation. It may prove HCM0 directly, derive a positive Hausdorff/moment representation that implies HCM0, or freeze the first exact HCM0 obstruction. Full shifted HCM is optional and may not replace the weaker load-bearing target.

## Gate decisions

- `MATHEMATICAL_CONTINUATION = REQUIRED`.
- `LEAN_FORMALIZATION = NOT_REQUIRED` — the load-bearing all-`m` theorem remains open.
- `EXTERNAL_PRIOR_ART_DUPLICATION = SATISFIED_BY_EXISTING_CONTROL_ASSET` via `DR-5D1B8E24C79A6F30B442`.
- `INDEPENDENT_REPLICATION = NOT_REQUIRED_AT_THIS_CHECKPOINT`.
- `INTEGRATION_OR_TOOL_HARVEST = NOT_REQUIRED` — `method_harvest=RESULT_ONLY`.
- `ADVERSARIAL_AUDIT = SATISFIED_BY_REVIEWED_RESULT` — the checker/certificate explicitly separates symbolic all-`m` claims from finite HCM discovery and the review freezes the non-implications.

No Working Truth, Foundation authority, L4 status, novelty, canonical promotion, or parent-objective closure is granted.
