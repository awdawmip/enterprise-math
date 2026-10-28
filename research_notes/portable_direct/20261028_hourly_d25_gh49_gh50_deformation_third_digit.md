# GH-49/GH-50 — Unified affine deformation and p³ source certificate

Date 2026-10-28. Author-derived / exact-computed / **UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` OPEN; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Science Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remains frozen. This report is not a native CLAIM, OPEN, Source checkpoint, Result, independent Driver review or mathematics admission.

The present Research lane uses logical conversation `chatgpt-research-hourly-enterprise-math-20260923` only for provenance; it does not use maintenance identity `chatgpt-hourly-enterprise-math-20260921`. The current service session/claim/run is not verified as owned. Scalar auxiliary hypergeometric calculations are **not** a native P000 X6/3D-slice result or a substitute for the original W/S/Hasse six ports.

## GH-49: exact one-parameter boundary deformation

Let `d>=1` be any integer and `p=4d+3` an integer parameter (not assumed prime here). Let `t` be a formal auxiliary parameter independent of `d,p`. Define

```text
gamma_0(t)=1
gamma_(r+1)(t)/gamma_r(t)
  =4(4r+4-t)(4r+3-t)/(8r+13-2t)^2      (0<=r<d)
Gamma_d(u,t)=sum_(r=0)^d gamma_r(t)u^r
g_n(t)=[u^n]Gamma_d(u,t)^2
```

With `D=u d/du`, `h=t/4`, define

```text
A_h=u(D+1-h)(D+3/4-h)-(D+5/8-h)^2
S_h=u(D+2-2h)(D+3/2-2h)(D+7/4-2h)-(D+5/4-2h)^3
K_h=-(5/8-h)^2
E_h(t)=(p+1-t)(p-t)*gamma_d(t)/16
```

**Exact identities in Q(t)[u]** (no discarded upper boundary):

```text
A_h Gamma_d = K_h + E_h(t)*u^(d+1)
S_h(Gamma_d^2)=K_h*(6D+5-2t)*Gamma_d
  + E_h(t)*u^(d+1)*(6D+2d+7-2t)*Gamma_d
```

The first identity follows from the coefficient ratio for ranks 1..d, with constant `K_h` and sole upper residual `(d+1-h)(d+3/4-h)gamma_d=E_h`. For any `A_h G=K(u)`, direct differentiation yields `S_h(G^2)=6K DG+[2DK+(5-2t)K]G`; substituting this affine source proves the second identity. Equating coefficients, setting out-of-range coefficients to zero, gives for **all** `0<=n<=2d+1`:

```text
(4n+5-2t)^3 g_n(t)
=4(2n+2-t)(2n+1-t)(4n+3-2t)g_(n-1)(t)
 +(5-2t)^2(6n+5-2t)gamma_n(t)
 -64 E_h(t)(6n-4d+1-2t)gamma_(n-d-1)(t).      (49.1)
```

At `t=0`, `gamma=beta`, `g=v`, `E_h=p(d+1)beta_d/4`: this is GH-47, **including** its p-valued upper forcing. At `t=p`, `gamma_r=a_(d-r)/a_d`, `E_h=0`: this is GH-48. The new result is the exact *entire parameter family*, including its moving boundary and the ability to differentiate between the two prior slices; merely dropping the upper term would invalidate the higher-precision calculation.

## GH-50: second ordered-pair jet and third-digit congruence

Now assume `p=4d+3>=7` prime and work in `Z_(p)`. Define

```text
H_r=sum_(j<r)(4/(8j+13)-1/(4j+4)-1/(4j+3))
L_r=(H_r^2+sum_(j<r)(8/(8j+13)^2
                        -1/(4j+4)^2-1/(4j+3)^2))/2
```

The exact coefficient ratio `gamma_r(p)/beta_r` equals
`prod_(j<r) [(1-p/(4j+4))(1-p/(4j+3)) /(1-2p/(8j+13))^2]`.
Taking its p-local logarithmic expansion through order two proves

```text
gamma_r(p) = beta_r [1+p H_r+p^2 L_r]        (mod p^3).
```

Preserve the original **ordered** source-pair labels:

```text
v_n      =sum_(i+j=n) beta_i beta_j
lambda_n =sum_(i+j=n) beta_i beta_j (H_i+H_j)
mu_n     =sum_(i+j=n) beta_i beta_j (L_i+L_j+H_i H_j)
g_n(p)   =v_n+p lambda_n+p^2 mu_n           (mod p^3).    (50.1)
```

The `mu_n` cross term `H_i H_j` and both individual `L` values are mathematically necessary: `mu_n` is not `lambda_n^2/2`. Evaluating (49.1) in the Taylor ring `Z_(p)[t]/(t^3)` determines `v_n,lambda_n,mu_n` in **O(d)** ring operations. All divisors `4n+5` for `0<=n<=2d` and `8r+13` for `0<=r<d` are p-units. The upper source `E_h(t)`, containing `p-t`, must be differentiated, not deleted.

Define `u=1/9`, and sum only over `0<=n<d`:

```text
M0=sum v_n u^n;              M1=sum lambda_n u^n
W0=sum (8n+11)v_n u^n;       W1=sum (8n+11)lambda_n u^n
W2=sum (8n+11)mu_n u^n
```

With original GH-38/39 `B_d(z),Q_d(z),T_d(z),a_d,E_d(z)`, direct reversal of the entire Gauss-square tail (no approximation) gives

```text
E_d(9)=a_d^2*9^(2d)*[4p*M_Gamma(1/9)-W_Gamma(1/9)]
9^(2d)=3^(p-1)/9
```

and `q_p(3)=(3^(p-1)-1)/p` is an integer. Substituting in the exact `T=BQ-E` identity and using (50.1) gives the **third-digit precision certificate**:

```text
T_d(9) == B_d(9)Q_d(9) + (a_d^2/9)*[
    W0
  + p*(q_p(3)*W0+W1-4*M0)
  + p^2*(W2+q_p(3)*W1-4*M1-4*q_p(3)*M0)
]                                                   (mod p^3). (50.2)
```

Here `W0` must be known mod p³, `q_p(3),W1,M0` mod p² and `W2,M1` mod p. This general formula upgrades the GH-42/GH-48 second-digit source preservation, but does **not** independently evaluate the special value `W_{d-1}(1/9)`, prove `T_d(9)=0 mod p`, or merge distinct native Hasse/observer ports.

## Executed proof checks and research boundaries

The Python standard-library checker ran: exact rational identity (49.1), including terminal rank `2d+1`, for `d=1..8`, `t=-2,0,1,2,p`; and all **86 primes** `7<=p<1000`, `p≡3 mod4`, by independent ordered-pair convolutions. At each prime it verified the truncated Taylor ring `Z/p^3[t]/t^3`, all individual first/second coefficient jets, complete high-degree reverse Gauss source, and (50.2) against the **direct original** `T_d(9)`. All checks passed. Selected `(p,T mod p^3,W2 mod p)`: `(7,133,0), (11,253,3), (19,5035,6), (23,4830,10), (43,14577,7), (67,260563,52)`. These finite checks are **not** a universal GH-3 proof. They are also not a native `p=373` experiment, Lean formal verification, an independent Driver review or a Source-admitted Result.

BRC source preservation: retain ordered indices, valuation, origin of `v/lambda/mu`, additive and multiplicative corrections, and evaluator/rank/t precision. No assumption that collapsed scalar cancellation implies native X6 evolution, future observer equivalence or six-port vanishing.

**Next open discriminator:** seek an *independent* finite-character, CM/Frobenius or nonlocal WZ certificate for `W_{d-1}(1/9)` versus `B_d(9)Q_d(9)`, especially all `p≡19 mod24`; alternatively find an exact counterexample. Use the second-jet evaluator to disprove overstrong mod-p²/p³ conjectures. Preserve GH-20/GH-21, original W/S, six Hasse ports, R23/R36 and native `p=373` as separate obligations. The mother Objective stays OPEN, frozen Source pin unchanged.

**Native status:** fresh typed continuation returned `INVALID_ARGUMENT / CONTROL_QUOTA` on 2026-10-28, with Site metadata `backend_version_pin=0.6.11`, `research_authority_granted=false`; no new session, claim, run, native checkpoint or review. Existing staged records and past requests were not changed. Control support remains at issue #1558. A separately generated portable archive holds the author's complete executable checker and actual stdout; GitHub text storage is not canonical Research execution registration.
