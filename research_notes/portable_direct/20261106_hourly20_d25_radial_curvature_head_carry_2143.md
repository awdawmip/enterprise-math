# D25: exact radial curvature head/carry decomposition and p=5113 cancellation

Date: 2026-11-06 (Asia/Hong_Kong). Scope: author-side portable TASK_RESEARCH mathematics, **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**. Existing frozen research input pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Existing Task ID: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. The configured logical lane `chatgpt-research-hourly-enterprise-math-20260923` is a lane label, not independently attested session identity.

## Theorem (exact rational identity; no primality needed)

Let `m>=1`, `a=2m`, `b=3m`, `c=4m`, and define the finite labelled-source polynomial
```
P_m(z) = sum_{j=0}^{b} (6j+1)(-1/2)^j C(b,j) C(a+z,j) C(c+z,j).
c_m = [z^2] P_m(z).
```
All generalized binomial polynomials are taken over Q. Write `H_n^(r)=sum_{k=1}^n k^(-r)`, `H_n=H_n^(1)`, with `H_0^(r)=0`. For `0<=j<=a`, put
```
U_j=(-1/2)^j C(a,j) C(b,j) C(c,j),
L_j=H_a-H_{a-j}+H_c-H_{c-j},
R_j=H_a^(2)-H_{a-j}^(2)+H_c^(2)-H_{c-j}^(2).
```
Then
```
HEAD_m = sum_{j=0}^a (6j+1) U_j (L_j^2-R_j)/2.
```
For `a<j<=b`, let
```
E_{a,j}=(-1)^(j-a-1) a! (j-a-1)! / j!,
M_{a,c,j}=H_a-H_{j-a-1}+H_c-H_{c-j}.
TAIL_m = sum_{j=a+1}^b (6j+1)(-1/2)^j C(b,j)C(c,j) E_{a,j} M_{a,c,j}.
```
**Exact identity:** `c_m=HEAD_m+TAIL_m` as rational numbers. Thus for any prime `p=6m+1`, all denominators are p-units and
```
c_p = HEAD_m+TAIL_m (mod p).
c_p=0 <=> HEAD_m = -TAIL_m (mod p).
```
The same `c_p` is the second-direction coefficient `(H_11+2H_13+H_33)/2` for the labelled `d=(1,0,1)` source direction. The dimension-3 central source is fixed along this operation.

**Proof.** For `j<=a`, each outer binomial is nonzero at `z=0`; logarithmic differentiation gives the first and second logarithmic derivatives `L_j` and `-R_j`. Hence its `z^2` coefficient is `U_j(L_j^2-R_j)/2`. For `a<j<=b`, `C(a+z,j)` has one simple root at `z=0`: its first derivative is `E_{a,j}`, and the ratio between the quadratic and linear Taylor coefficients is `H_a-H_{j-a-1}`. Multiplication by `C(c+z,j)` adds `H_c-H_{c-j}`, yielding the displayed TAIL. For `j>b`, the unperturbed central factor `C(b,j)=0` identically, so there are no further terms. Summing proves the identity. Reducing modulo `p` is legitimate because all relevant indices `j<=b<p` and harmonic denominators are less than `p`. The equality with the directional Hessian follows by the multivariate chain rule. QED.

**Structural implication for BRC.** The labelled observer's radial second jet consists of a normal head `j<=2m` and a **single outer-source carry tail** `2m<j<=3m`; the middle source suppresses higher-carry intervals for this particular directional observer. The aggregate curvature may vanish by cancellation between two individually nonzero, provenance-distinct pieces. It would be unsound to infer zero contributions from the total alone.

## Two independent exact modular methods and observed results

Method A evaluates the explicit harmonic HEAD/TAIL formula using inverse tables modulo p. Method B evaluates `[z^2]P_m(z)` directly by degree-2 polynomial recurrence for each outer binomial, never using harmonic numbers. It also independently returns `[z]P_m(z)`. Both are implemented in `d25_radial_curvature_head_carry_20261106.py` with integer modular arithmetic and assertions.

| p | HEAD | TAIL | c=(HEAD+TAIL) mod p | [z]P_m(z) |
|---:|---:|---:|---:|---:|
| 7 | 0 | 3 | 3 | 0 |
| 13 | 3 | 2 | 5 | 0 |
| 19 | 7 | 3 | 10 | 0 |
| 109 | 56 | 76 | 23 | 0 |
| 211 | 69 | 62 | 131 | 0 |
| 229 | 151 | 140 | 62 | 0 |
| 373 | 158 | 282 | 67 | 0 |
| 1093 | 309 | 452 | 761 | 0 |
| 3511 | 2533 | 2735 | 1757 | 0 |
| **5113** | **3519** | **1594** | **0** | **0** |

For `p=5113`, `3519+1594=5113` exactly as chosen integer residues, and neither summand vanishes in F_5113. This identifies **cross-interval cancellation** behind the previously proven `c_5113=0`, rather than disappearance of either interval's curvature. It is a new decomposition of that existing exceptional certificate, not a claim that all other primes have nonzero curvature.

The prior independently executed full `p^3`-sum certificate is `d25_p5113_direct_certificate_20261106.py`, reported in `20261106_hourly20_d25_p5113_linear_fiber_exception.md`. It yields `D_5113(lambda)=3118 lambda` on the entire field using a degree-2 argument and exact values at `lambda=±1`. It does not depend on the harmonic formula here.

## Control and next scientific action

Service status actually read for v0.6.11 on 2026-11-06. Original control requests `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` were read by their original IDs, then reconciled once each; reconciled states were `QUEUED` with prior `EVENT_COLLECTION_IO` progress, not final Source packets. The connected transport exposed `em_status` and `em_control_reconcile`, but did not expose own `recovery_status` or `session_preserve_staging` as callable tools. Old protected staging/current owner/session therefore remain **UNVERIFIED**. No successor CLAIM, OPEN, native checkpoint, session close or release was attempted. Support owner path: Enterprise Math issue #1558.

**Next smallest open mathematical unit:** exploit the exact HEAD/TAIL identity to seek a telescoping relation characterizing `HEAD_m+TAIL_m=0 (mod 6m+1)`; test candidate congruences against the existing p=5113 and p=13,19,373 records, while keeping universal `T_1+T_3=0` and `k_p=-3q_p(2)` as separate open proofs. The mother target remains `Delta_p-R_p=0 mod p` for `p mod24 in {13,19}`. The original H0/B0, Frobenius, eta/kappa and independent review remain unresolved. Preserve the verified prior scientific pin, source checkpoint and completed history unchanged.
