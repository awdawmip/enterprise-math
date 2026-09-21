# RS-CFD-TRAJECTORY-VERIFY-20260910 — forced-energy/source-work continuation

Researcher: `EM-CFD-VFY-9A71C4`  
Claim: `CLM-CFDVFY-9A71C4-20260921-1540`  
Status: `CONTINUATION_REQUIRED`

## Result

This continuation closes a verifier-contract gap left by the earlier Hermitian/physical-energy and Source-divergence work: forced trajectories now have an explicit **source-work diagnostic** without incorrectly turning source work into a total-energy acceptance gate.

For host real velocity `u`, define physical kinetic energy and instantaneous Source power by

`E(u) = 0.5 * mean(sum_i u_i^2)`

and

`P_F(u,t) = mean(sum_i u_i * Source_i(u,t))`.

For a classical RK4 step, the verifier records Source power on the actual four RK stages and forms

`W_F = dt * [P_F(stage1)/6 + P_F(stage2)/3 + P_F(stage3)/3 + P_F(stage4)/6]`.

This quantity is diagnostically useful but has a strict interpretation boundary. For the synthetic source-only ODE with constant Source, the RK4 weighted Source work equals the quadratic energy increment up to roundoff. For a full forced Navier–Stokes RHS, however, `delta E == W_F` is generally **not** a valid gate: viscosity and the remaining RHS terms also contribute to the total energy change, and their discrete work is not represented by `W_F`. A valid native-host forced run should therefore retain the physical energy series, the four stage Source powers, and per-step `W_F`, while treating a full energy budget as a separate instrumented obligation.

The source-work diagnostic is also orthogonal to incompressibility. A deliberately longitudinal Source can satisfy the source-only energy/work identity while violating `K·Source=0`; therefore energy/work agreement cannot substitute for the previously established per-stage transversality check. A convenient dynamic positive-control family is a time-dependent scalar amplitude multiplying a fixed divergence-free spatial Source mode, which changes coefficients while preserving `K·Source=0` up to roundoff.

## Validation

A deterministic NumPy checker with seed `20260921` was executed and passed **8/8** checks. Its `n=8`, `2π`-periodic transverse Source had `max|K·F_hat| = 2.3381594351524416e-14`; a deliberately longitudinal negative control had residual `256.0` and was detected. For constant source-only forcing, `delta E = 0.019999999999999997`, RK4 weighted Source work was `0.020000000000000004`, and the balance defect was `-6.938893903907228e-18`.

For the smooth dynamic Source `a(t)F0` with `a(t)=1+0.2 sin(t)`, the absolute source-only energy/work defects at `dt = 0.4, 0.2, 0.1, 0.05` were respectively approximately `1.03e-8`, `1.14e-10`, `1.44e-12`, and `2.01e-14`; the defect decreased on every halving. This is only a deterministic refinement witness and is **not** promoted to a claimed RK4 convergence order.

A dissipative forced toy RHS also demonstrated why Source work cannot be a total-energy gate: at `dt=0.1`, `delta E = 0.0064645889022968105`, Source work `= 0.009261808073949095`, leaving `delta E - W_F = -0.0027972191716522845`. Conversely, the deliberately longitudinal source-only negative control had energy/work defect `1.734723475976807e-18` while remaining strongly non-solenoidal. Thus the energy/work and divergence certificates test genuinely different obligations.

Validation commands executed in this run:

- `python RS_CFD_FORCED_ENERGY_DIAGNOSTICS_9A71C4.py` → 8/8 PASS;
- `python -m py_compile RS_CFD_FORCED_ENERGY_DIAGNOSTICS_9A71C4.py` → PASS;
- emitted result JSON parsed successfully.

## Durable outputs

- `research_checks/RS_CFD_FORCED_ENERGY_DIAGNOSTICS_9A71C4.py`
- `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_9A71C4/forced_energy_results.json`
- `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_9A71C4/forced_energy_contract.json`

## Native-host integration contract

On the exact pinned serial spectralDNS/shenfun/FFTW host, preserve the already required zero Source, transverse static Source, transverse dynamic Source, and deliberately longitudinal negative control. For every positive forced-control RK stage record both `P_F` and `max|K·Source_hat|`; for every completed step record physical `E`, weighted `W_F`, `max|K·U_hat|`, stored-plane Hermitian residual, and sparse/dense fallback state. Retain dense-vs-hybrid velocity/modified-pressure comparisons, same-final-time `dt=0.002` versus `dt=0.001`, and complete setup/allocation/compilation/trajectory timings.

Do **not** use `delta E == W_F` as a full Navier–Stokes acceptance condition unless all non-Source discrete work terms have separately been instrumented and justified. Do not mark the task DONE before the native rerun and independent acceptance are complete.

This return grants no continuous-PDE certificate, no universal speedup claim, and no native-host numerical acceptance.
