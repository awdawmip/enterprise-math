# RS-CFD-TRAJECTORY-VERIFY-20260910 — Source divergence continuation

Researcher: `EM-CFD-VFY-0F326B`  
Claim: `CLM-CFDVFY-0F326B-20260921-1440`  
Status: `CONTINUATION_REQUIRED`

## New result

The pinned spectralDNS `NS.py` blob `6a11909d1e2c1d529d382952c4c9d77e7073645c` exposes an additional verifier obligation that was not captured by the prior Source-support guard.

`ComputeRHS` applies convection, Nyquist masking, pressure/diffusion, and **only then** executes `rhs += Source`. In `add_pressure_diffusion`, the code computes

`P_hat = (K·N)/K²`, `R_pre = N - K P_hat - nu K² U`.

Hence, for nonzero modes,

`K·R_pre = -nu K²(K·U)`.

A solenoidal stage velocity therefore remains solenoidal through convection/pressure/diffusion. After the pinned `rhs += Source` ordering, however,

`K·R_post = K·Source`.

So the static/dynamic Source **support envelope** contract from the implementation lane is necessary for exact support routing but is not sufficient for an incompressible-valid trajectory certificate. Every forced positive-control trajectory must also make its stage Source transverse (`K·Source=0`, up to a declared floating tolerance). A longitudinal Source can make dense and hybrid trajectories agree perfectly while both violate incompressibility.

This also sharpens pressure interpretation: the pinned `P_hat` is computed before Source addition. It does not project away a longitudinal Source component. Therefore dense-vs-hybrid agreement of modified pressure cannot certify incompressibility for arbitrary Source.

## Validation

A deterministic host-independent r2c witness (`n=8`, seed `20260921`) reproduced the pinned projection algebra and ran 9 checks, all passing.

Key metrics:

- initial projected `max|K·U|`: `3.2023728339893772e-15`
- projected convection+diffusion `max|K·R|`: `6.4047456679787543e-15`
- transverse Source `max|K·Source|`: `2.7465400791133423e-15`
- RHS with transverse Source `max|K·R|`: `7.1607233460988954e-15`
- longitudinal Source `max|K·Source|`: `7.8746428490440126`
- RHS with longitudinal Source `max|K·R|`: `7.8746428490440135`
- pressure recomputation difference when only Source changes: `0`
- RK4 final `max|K·U|`, transverse Source: `3.2023728339893772e-15`
- RK4 final `max|K·U|`, one longitudinal Source stage: `0.026193802754119935`

The longitudinal negative control is intentionally not a passing incompressible case; it verifies that the checker catches exactly the failure implied by the pinned host ordering.

## Updated native-host matrix

For the previously required zero/static/dynamic Source reruns:

1. zero Source remains a positive control;
2. static Source positive control must use a declared support envelope **and** a transverse forcing construction;
3. dynamic Source positive control must enforce both support-escape handling and per-stage transversality;
4. add one longitudinal Source negative control to prove the verifier rejects incompressibility even if dense-vs-hybrid numerical equality holds;
5. record `max|K·Source|` at every RK stage and `max|K·U_hat|` at initial/every completed RK/final state;
6. preserve the prior Hermitian, physical-energy, same-final-time `dt=0.002` vs `0.001`, fallback-state and complete-cost diagnostics.

Do not silently project an arbitrary user Source inside the hybrid adapter: that would alter solver semantics. If a projected forcing is used, it must be declared as test construction or as an explicit solver change with separate validation.

## Durable outputs

- `research_checks/RS_CFD_SOURCE_DIVERGENCE_DIAGNOSTICS_0F326B.py`
- `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_0F326B/source_divergence_contract.md`
- `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_0F326B/diagnostic_result.json`

## Remaining boundary

The exact native spectralDNS/shenfun/FFTW host still has not been rerun in this unit. This return does not grant native trajectory acceptance, a continuous-PDE certificate, or a universal speedup claim. The next minimal unit is now stricter: execute the pinned host with verifier-generated transverse static/dynamic forcing plus the longitudinal negative control, together with the already frozen Hermitian/energy/timestep/cost diagnostics.
