# PREFIX-577-R6: exact full third cumulant tensor (native X6-BRC + gate)

2026-11-08 | `TASK_RESEARCH / AUTHOR_EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED`

## Frozen input and observer

Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; native 96-port / 48 signed phases, 6 labeled equiprobable actions per port. Exact kernel input `PREFIX565_positive_marginal_certificate.py` blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`; published 7-reward covariance/root-gauge input `PREFIX577_R6_published_certificate.py` blob `2784c78e6acc2a696f75a011628925223a51ddc3`. Every edge preserves its action and target port, with full native six-axis and gate rewards.

Let `W_d=(R1,R2,R3,R4,R5,R6,K)`. Each asymptotic third joint cumulant `C_abc=lim_{d→∞} cum(Wa(d),Wb(d),Wc(d))/d` is a rational number. Due to the **exact pathwise zero-root identity** `R6=d-R1-R2-R3-R4-R5`, the full symmetric 7-variable third tensor (84 entries) can be reconstructed from the 56 entries on `(R1,R2,R3,R4,R5,K)`; the root gauge endpoint identity preserves the rates for all nine frozen roots. This is an exact observer-specific reduction, not a claim of a smaller native state or lossless global quotient.

## Exact verification

Use the stationary row vector `π=(1/96,...,1/96)`, `T(t)_{ij}=Σ_(i→j)(1/6) exp(t·w)` and its locally analytic Perron eigenpair `λ(t),v(t)` normalized by `π v(t)=1`. For every multi-index A, `M_A=∂_A T(0)`, `P=T(0)`. The 6 first derivatives and 21 second mixed derivatives of `v` solve 27 Poisson equations with exact zero-mean normalization. The exact algorithm verifies all 27×96=2592 row equations and the already published exact 6×6 covariance of `(R1..R5,K)`. The third derivatives are

`λ_abc = π[M_abc 1 + M_ab u_c + M_ac u_b + M_bc u_a + M_a u_bc + M_b u_ac + M_c u_ab]`,

`C_abc=λ_abc-λ_abλ_c-λ_acλ_b-λ_bcλ_a+2λ_aλ_bλ_c`.

A **separate exact integer path-moment recursion**, not the Poisson solver, checks 7 distinct linear projections using stationary-start third cumulants at depths 1024 and 1026 (two-step increment, accounting for native chain period 2). Each difference from the exact rational rate has absolute error below `10^-14` (actual maximum `<4e-243`). This is an independent finite-depth regression; the exact Poisson equations provide the rational proof kernel.

Exact all-56 certificate (index order `0..5 = R1,R2,R3,R4,R5,K`; triples sorted):

```text
0,0,0 -49/5184
0,0,1 11/5184
0,0,2 19/10368
0,0,3 19/10368
0,0,4 19/10368
0,0,5 -49/165888
0,1,1 11/5184
0,1,2 -11/10368
0,1,3 -11/10368
0,1,4 -11/10368
0,1,5 11/165888
0,2,2 19/10368
0,2,3 -11/10368
0,2,4 -1/1296
0,2,5 199/331776
0,3,3 19/10368
0,3,4 -1/1296
0,3,5 -23/82944
0,4,4 19/10368
0,4,5 -31/663552
0,5,5 32501/21233664
1,1,1 -49/5184
1,1,2 19/10368
1,1,3 19/10368
1,1,4 19/10368
1,1,5 11/165888
1,2,2 19/10368
1,2,3 -11/10368
1,2,4 -1/1296
1,2,5 -23/82944
1,3,3 19/10368
1,3,4 -1/1296
1,3,5 49/331776
1,4,4 19/10368
1,4,5 -1/663552
1,5,5 -20395/21233664
2,2,2 -49/5184
2,2,3 11/5184
2,2,4 19/10368
2,2,5 -49/165888
2,3,3 11/5184
2,3,4 -11/10368
2,3,5 11/165888
2,4,4 19/10368
2,4,5 -31/663552
2,5,5 32501/21233664
3,3,3 -49/5184
3,3,4 19/10368
3,3,5 11/165888
3,4,4 19/10368
3,4,5 -1/663552
3,5,5 -20395/21233664
4,4,4 -49/5184
4,4,5 19/82944
4,5,5 -6053/10616832
5,5,5 206963/42467328
```

Highlights: `C(R1,R3,K)=199/331776`; `C(R5,K,K)=-6053/10616832`; `C(K,K,K)=206963/42467328`. Under the pathwise reconstruction, `C(R5+R6,K,K)=-6053/5308416` and `C(R5-R6,R5-R6,K)=5/6912` (old scope may overlap PREFIX-578-R2).

## Evidence provenance and current control boundary

Current-run executable files and full certificates exist in a 6-file portable ZIP within the author conversation. SHA-256: `0de084589a7ea3fda8cdc39bd547ef32ee3476c28656a4f5f5655ba8087fe19b`. Its main exact certificate SHA-256 is `098dcd963b2223b30217aae0a583f4c48d3a3785bd478bfc1c5d11bfa5a5ac08`, and independent finite-depth certificate SHA-256 is `366e618a11d237a56cd08c16df843a165e29534cdd978df3884a73a7efef3032`. GitHub holds this authored exact conclusion/evidence index; the ZIP remains conversation-local.

At 2026-11-08 service read, `em_status` and historic receipt queries failed `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`; Site `research_authority_granted=false`. This note is **neutral author-side preservation**, not a native session, Source CLAIM/checkpoint, Result, formal Review or Working Truth. No canonical `completed_units` were asserted from portable staging. The genuine Source owner and recovery queue remain unknown.

Next scientific check: cross-read same-pin PREFIX-578-R2 already-published three-way overlaps; then choose a nonduplicate fourth-order or exact symmetry unit. Original UR V2 94,687-byte bundle with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` remains unlocated; recover original bytes and Source read/credential separately, then supplement only provenance/checkpoint without repeating UR proof.
