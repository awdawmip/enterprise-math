# Driver Review — Perfect Prime AP outer conditional-covariance reduction

Driver-ID: `EM-DVR-P8H4Q2`
Review-ID: `DR-9986FE430DB065EA8EF2`
Task: `RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY`
Publication: `TP2-5A3E91C7D2B40F681AC3`
Result: `RR-A4EBF925BE07691C8C16`
Execution: `ER-5061202400CCD679FFE6`

## Disposition

`ACCEPTED / EXACT_NEGATIVE_BOUNDARY / FOLLOWUP_TASK`.

The Result is accepted at its exact stated strength. It does not prove or refute the Perfect Prime parent all-`m` nonvanishing theorem. It makes two load-bearing advances: it reduces the full canonical cofactor exactly to one `(m-1)x(m-1)` outer alternating conditional-covariance determinant, and it proves that a natural inner-block positivity/conditional-variance/termwise-Andreief closure is impossible for every `m>=3` because every inner block is indefinite.

## Envelope audit

The Result record is complete. The four declared frozen outputs resolve to the exact Git blobs in the execution branch:

- Return: `340a17c17156e633f0c107023507ceb5498a3763`;
- checker: `0beaf76c3485e81de82b0b6e331e435cf7f0fc2b`;
- exact covariance certificate: `0e317106c82c3ab53124cda050c8f78c11b76d16`;
- execution record: `5ab612fecdf6ff2401cf7c0693052679cc9956f8`.

The taskbook binding is the current published blob `9b11446b5d2bc9bcca186c13bad361064990734e`. Finite checks are treated only as regression/discovery evidence, consistently with the taskbook.

## Accepted exact reduction

With the frozen AP deformation and canonical gauge cofactor `tau_m(t)`, the Result defines signed layer weights `lambda_(j,s)(t)`, positive aggregate masses `Dcal_j(t)>0`, inner signed conditional-covariance blocks `C_j(t)`, and

`S_m(t)=sum_j w_j C_j(t)`

on nonconstant polynomial coordinates. The square-completion and Vandermonde coordinate changes give the exact identity

`tau_m(t) = [prod_j w_j Dcal_j(t)] det S_m(t) / [prod_(k=1)^(m-1) k!]^2`.

Because every `Dcal_j(t)>0` and every `w_j` is nonzero on `0<t<=1`, the parent fixed-point target is now exactly equivalent to

`det S_m(t) != 0`

for every `m>=2` and `0<t<=1`.

The direct-vs-reduced cofactor identity is also checked by exact arithmetic for `m=2..6` at `t=1/2,1`; those finite checks guard the symbolic reduction but do not establish the all-`m` theorem.

## Accepted inner-block obstruction

For each `j`, the signed covariance form is the pullback of

`A_j = Lambda_j - lambda_j lambda_j^T / Dcal_j`.

The diagonal `Lambda_j` has alternating-sign inertia. The bordered form

`G_j=[[Dcal_j,lambda_j^T],[lambda_j,Lambda_j]]`

has quadratic form `sum_s lambda_(j,s)(r+x_s)^2`, hence inertia equal to that of `Lambda_j` plus the single gauge zero. Since `Dcal_j>0`, Schur-complement inertia gives, after removing the constant direction,

`In(C_j)=(floor((m-1)/2), ceil((m-1)/2), 0)`.

Therefore every inner block is indefinite for every `m>=3`, every `j`, and every `0<t<=1`. The explicit `m=3,j=0,t=1` block has determinant `-6561/4030` and is a valid smallest regression witness.

This freezes the following route closure:

- direct conditional-variance positivity: `CLOSED`;
- termwise positive inner Andreief closure: `CLOSED`;
- any proof requiring each `C_j` to be positive or negative definite: `CLOSED`.

This does **not** imply that the outer alternating sum `S_m(t)` is singular or indefinite in a way that defeats the parent theorem.

## Endpoint and polynomial evidence

The accepted reduction reproduces the forced order

`ord_(t=0) tau_m(t)=m-1`

from the previously accepted nondegenerate crossing form. At the double-Cauchy endpoint, the transformed residual polynomial `Bhat_m(x)` has strictly positive coefficients in exact finite regression through `m=10`. This is meaningful route evidence, but it is not an all-`m` theorem.

A claimed fixed inertia of `S_m(t)` cannot be justified merely by continuity, because preventing inertia change already requires excluding `det S_m(t)=0`. Any fixed-inertia proof must derive the inertia from additional exact structure without assuming the target.

## Gate decisions

- `MATHEMATICAL_CONTINUATION = REQUIRED` — the parent objective remains open at one explicit outer determinant.
- `LEAN_FORMALIZATION = NOT_REQUIRED` — the load-bearing all-`m` determinant theorem is not closed.
- `EXTERNAL_PRIOR_ART_DUPLICATION = SATISFIED_BY_EXISTING_REVIEWED_BOUNDARY` — no new broad prior-art task is justified before the outer theorem stabilizes.
- `INDEPENDENT_REPLICATION = NOT_REQUIRED_AT_THIS_CHECKPOINT` — reconsider after a positive all-`m` theorem.
- `ADVERSARIAL_AUDIT = BUILT_INTO_SUCCESSOR` — the next task must preserve the indefinite-inner-block counterexample and reject circular inertia arguments.

## Follow-up

Publish exactly one P0/HIGH continuation centered on the exact outer determinant `det S_m(t)`. It may close the target either by a noncircular structural fixed-inertia/nonvanishing theorem for `S_m(t)` or by an all-`m` proof of positivity for the equivalent double-endpoint residual Bernstein coefficients. A counterexample or a sharper operator-specific obstruction is also terminally acceptable.

No Working Truth, Foundation, L4, novelty, or closure of `OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M` is granted.