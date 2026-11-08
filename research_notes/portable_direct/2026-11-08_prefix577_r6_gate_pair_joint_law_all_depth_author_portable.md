# PREFIX577-R6 — exact all-depth joint law symmetry for the native BRC gate and axes 5/6

Date: 2026-11-08 UTC. Status: TASK_RESEARCH author-side exact result; UNREVIEWED / NOT_ADMITTED.
Frozen science pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Immutable original native kernel: `PREFIX565_positive_marginal_certificate.py`, Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41` (read directly by GitHub blob ID this turn).
Author continuation: prior order-eight scalar moment result in `research_notes/portable_direct/2026-11-08_prefix577_r6_orthogonal_gate_fourth_cumulant_author_portable.md`, blob `85c81c0c224818848122636ea0f3fa81e40d0eff`. This note strengthens that earlier author result.

## Exact theorem

On the frozen 96-port native zero-root X6-BRC chain (six equiprobable labeled actions per port), initialize the native port uniformly among all 96. Let K_n be the accumulated gate count and R_{5,n}, R_{6,n} the corresponding native-axis rewards after n labeled steps. For **every** integer n≥0 and every pair of nonnegative integers a,b,

`P(K_n=a, R_{5,n}=b) = P(K_n=a, R_{6,n}=b).`

Equivalently, the full two-variable probability generating polynomials satisfy, coefficientwise,

`E[x^(K_n) y^(R_{5,n})] = E[x^(K_n) y^(R_{6,n})]`.

Hence all finite-length joint mixed moments, mixed cumulants and scalar readouts of these two bivariate observations agree, at every finite n and all orders. This subsumes the previously checked order-eight scalar equality for K+R5/K+R6 without re-claiming that earlier work.

## Finite exact proof via Cayley–Hamilton over Z[x,y]

For i=5,6 define the 96×96 matrix over the commutative polynomial ring Z[x,y]:

`A_i(x,y)[u,v] = Σ_{e:u→v} x^(k(e)) y^(r_i(e))`,

where **each** of the six original labeled actions is counted separately and native gate/axis edge increments are used unchanged. Let `1` be the 96-component ones vector and

`P_n^(i)(x,y) = 1ᵀ A_i(x,y)^n 1`.

Coefficient (a,b) of this polynomial counts all 96-start labeled length-n paths with gate count a and R_i count b. Dividing by exactly 96·6^n gives the stationary-start bivariate probability distribution.

Put `U(x,y)=A_5(x,y) ⊕ A_6(x,y)`. This is a 192×192 matrix over Z[x,y]. The scalar polynomial difference `D_n=P_n^(5)-P_n^(6)` is a fixed linear readout of `U^n`. Because Z[x,y] is commutative, Cayley–Hamilton applies: with `χ_U(t)=t^192+c_191(x,y)t^191+…+c_0(x,y)`,

`D_(n+192) = - Σ_(j=0)^191 c_j(x,y) D_(n+j)`.

Thus exact coefficientwise equality of `D_n=0` for the **192 lengths n=0,…,191** proves `D_n=0` for all n≥0. The recurrence is a formal polynomial identity, with no floating-point or extrapolation error.

An arbitrary-precision GMP C++ program enumerated the full joint path-count coefficient dictionaries separately for i=5 and i=6 at **every n=0,…,191** and found exact equality of every coefficient. At n=191, both polynomial supports contain **3,049** (gate count, axis count) pairs; the total coefficient mass exactly equals `96*6^191`, a 151-digit integer. The final run explicitly returned `PASS_ALL_192_BIVARIATE_POLYNOMIALS; CH_DIM_192; EXACT_Zxy`.

A separate Python implementation re-derived the native edges and checked every bivariate coefficient at all depths n=0,…,64, in exact integer arithmetic. Its regression JSON SHA-256 is `c0cb43fe1feef3334ddc84665e8bb6d83aa272bb065c89e00060102acdcb222d`. The original kernel's `STARS, PHASES, NEXT, ACTIONS, TARGET, sg, edge` definitions were compared against the present frozen model, preserving the gate and 576 labeled edges.

## Explicit scope witness

The uniform-start condition is substantive. At **fixed source native port 16**, phase `(0,1,-6)` and bit 0, every one of the six possible single actions has `(K,R5)=(0,0)` but `(K,R6)=(0,1)`. The full joint equality is an ensemble equality, not an assertion of pointwise equality at each start.

## Reproducible evidence and continuation

Conversation-local reproducible bundle: `PREFIX577_R6_GATE_PAIR_FULL_JOINT_LAW_PORTABLE_20261108.zip`, 15,885 bytes, SHA-256 `348a9d69cce423403b3c9a30a43b07a65a5884fe2cfaf33785e8e74aefcf9e46`, containing:

- the complete expanded mathematical theorem and proof (`PREFIX577_R6_GATE_PAIR_FULL_JOINT_LAW_THEOREM_20261108.md`);
- exact GMP C++ polynomial checker (`exact_joint_gate_pair_all_distribution_gmp.cpp`, SHA-256 `fe93d1ceb78426153b5bab15de541bbe6124351c1943fc097d0c393747647f5a`);
- the 576 labeled frozen edges (`native_edge_snapshot.csv`, SHA-256 `c2691e652d07d9a819b3cb3d1f79eb1797f3ee1aa8a4b4906dcd83b48353d138`);
- exact program output, independent Python checker/JSON, prior pinned native derivation and scalar polynomial crosscheck.

The bundle is a **conversation-local** portable artifact; its digest does not assert Source publication. This GitHub document is neutral author-side persistence, not native session/CLAIM/run/checkpoint, mathematical admission, independent review or Result.

The Source `em_status` read in this turn still returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE` with `operation_sent=false`. Current Source owner/session/recovery remains to be authenticated; no mutation or new dispatch was attempted. Original UR V2 debt is separate: locate the exact 94,687-byte four-file object with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, then add only lawful writer/provenance/checkpoint. Do not re-prove UR or substitute four older files for the original bundle. On current-input seed, perform complete input readback and preserve predecessor `completed_units=[]`.

**Next scientific question:** derive a smaller weighted automaton quotient or explicit boundary-preserving transformation explaining this full all-depth bivariate identity; avoid duplicate live-owner work. **Next control action:** reconcile the original request and exact Source continuation after authentic backend recovery before any owner mutation. Prior identifiers are provenance, not permissions.
