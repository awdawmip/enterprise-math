# Source divergence / pressure-projection verification contract

Pinned source authority: `spectralDNS/spectralDNS` blob `6a11909d1e2c1d529d382952c4c9d77e7073645c` (`spectralDNS/solvers/NS.py`).

## Exact ordering in the pinned solver

`ComputeRHS` performs:
1. nonlinear convection,
2. optional Nyquist masking,
3. `add_pressure_diffusion`,
4. `rhs += Source`.

Inside `add_pressure_diffusion`,
`P_hat = (K·rhs)/K^2`, then `rhs <- rhs - K P_hat - nu K^2 U_hat`.
The zero mode is harmless because `K=0`.

Therefore, for nonzero modes,

`K·R_pre = K·N - K^2 (K·N)/K^2 - nu K^2 (K·U) = -nu K^2 (K·U)`.

If the stage velocity is solenoidal (`K·U=0`), the convection/pressure/diffusion result is solenoidal. But the Source is added **after** this pressure projection, so

`K·R_post = K·Source`.

This is independent of sparse/hybrid support handling.

## Verification consequence

A forced trajectory can count as an incompressible-valid verification case only if every RK-stage forcing satisfies `K·Source=0` within a declared floating tolerance. Static/dynamic Source support certification alone is insufficient. A longitudinal Source can still produce exact dense-vs-hybrid agreement while both routes violate the incompressibility invariant.

For native reruns:
- record `max |K·U_hat|` at initial state, every completed RK step, and final state;
- record `max |K·Source|` at every RK stage for forced cases;
- construct static/dynamic positive-control forcings by a declared Leray projection or an analytically transverse formula;
- retain at least one deliberately longitudinal Source as a **negative verifier control**, not a passing physical trajectory;
- do not silently project user Source inside the hybrid adapter unless solver semantics are explicitly changed and separately validated.

## Pressure consequence

The pinned `P_hat` is computed before Source addition. Therefore a non-solenoidal Source is not pressure-corrected by this `P_hat`. Matching `P_hat` between dense and hybrid routes cannot by itself certify incompressibility for arbitrary Source. For transverse Source this issue disappears because no longitudinal forcing correction is needed.

## Host-independent validation

`RS_CFD_SOURCE_DIVERGENCE_DIAGNOSTICS_0F326B.py` implements the pinned algebra on an `n=8` r2c wavevector grid and checks:
- solenoidal initial projection;
- pressure-projected convection + diffusion preserves solenoidality;
- transverse Source preserves RHS solenoidality;
- a longitudinal Source leaves a nonzero divergence residual;
- the pressure result is Source-blind under the pinned ordering;
- an RK4 step preserves solenoidality for zero/transverse Source;
- one longitudinal Source stage creates detectable final divergence.
