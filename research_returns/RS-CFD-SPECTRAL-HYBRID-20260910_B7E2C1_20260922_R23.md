# CFD continuation R23: sharp deterministic measurement-error envelope for the R19 trajectory ceiling

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-CFD-B7E2C1`  
Claim: `CLM-CFD-B7E2C1-20260922-R23`  
State: `CONTINUATION_REQUIRED / ROBUST COST-ATTRIBUTION CERTIFICATE / NO NATIVE SPEEDUP CLAIM`

## Consumed canonical frontier

This unit consumes canonical R19 at immutable commit `043e0a563c60dabc141a51387865feb364a4cc6a` without replay. R19 established the full-trajectory sparse-attributable ceiling

`S <= 1 / (1 - alpha_bar*f_bar*w_bar + h_floor)`

and required a pinned spectralDNS/shenfun/MPI/FFTW host for the decisive dense / guarded-hybrid / forced-fallback RK4 experiment.

The host gate was re-run before doing any surrogate work. The present runtime still lacks `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft`, `pyfftw`, `mpicc`, `mpicxx`, `mpi.h`, `fftw3.h`, and an MPI shared library; only the FFTW dynamic library `libfftw3.so.3` is visible. Therefore `native_ready=false`. No native RK4 trajectory or native speedup/slowdown is claimed.

## New theorem: sharp box-error propagation without splitting the shared denominator

Write the R19 bound before normalization as

`T_hybrid >= T + H - A D`,

where `T>0` is the dense-reference trajectory time, `D>=0` is the dense nonlinear work to which the route-share bound applies, `H>=0` is hybrid-only additive cost retained by R19, and

`A = alpha_bar * w_bar`, `0 <= A <= 1`.

Hence the speedup satisfies

`S <= 1 / g`, with `g = 1 + (H - A D)/T`, whenever `g>0`.

Suppose instrumentation provides deterministic aggregate error boxes

- `T in [T_hat-e_T, T_hat+e_T]`, with `T_- = T_hat-e_T > 0`;
- `D <= D_+ = D_hat+e_D`;
- `H >= H_- = max(0, H_hat-e_H)`;
- and the consistency condition `D_+ <= T_-`.

Set

`N_- = H_- - A D_+`.

Then the exact worst-case denominator allowed by this information is

`g_rob = 1 + N_-/T_+` if `N_- >= 0`,

and

`g_rob = 1 + N_-/T_-` if `N_- < 0`,

where `T_+ = T_hat+e_T`.

Therefore, if `g_rob>0`, every admissible true timing triple obeys

`S <= 1/g_rob`.

For a target `q>1`, a fail-closed rejection certificate is simply

`g_rob > 1/q`.

### Proof and sharpness

For fixed `T`, the denominator `1+(H-A D)/T` decreases monotonically as `D` increases and increases monotonically as `H` increases, so its minimum is attained at `D=D_+`, `H=H_-`. It then equals `1+N_-/T`. If `N_- >= 0`, this decreases with `T` and is minimized at `T=T_+`; if `N_-<0`, it increases with `T` and is minimized at `T=T_-`. These endpoint choices are admissible under the stated box and `D_+<=T_-`, so the bound is sharp under this measurement-information model.

The point of retaining `(H-A D)/T` as one ratio is that `D/T` and `H/T` share the same uncertain baseline `T`. Bounding the two normalized ratios independently is safe but generally looser because it can combine incompatible choices `T=T_-` and `T=T_+` in the same worst case. The formula above propagates the common-denominator uncertainty exactly.

## Exact instrumentation-precision threshold for the frozen R19 illustration

This subsection is deliberately an illustration, not a native measurement. Normalize the observed dense baseline to `T_hat=1` and reuse R19's illustrative values for the `k=2,n=20,rho=2` route pattern:

- `A = alpha_bar*w_bar = (7/10)*(2/11) = 7/55`;
- `D_hat/T_hat = 4/5`;
- `H_hat/T_hat = 1/50`;
- target `q=11/10`.

Assume a symmetric deterministic aggregate error budget `delta*T_hat` for each of `T,D,H`. In the interior regime

`delta < min(h_hat, (1-f_hat)/2)`,

we have `H_-=h_hat-delta>0` and `D_+=f_hat+delta<T_-=1-delta`. For this example `H_- - A D_+<0`, so the sharp robust denominator uses `T_-`.

The zero-error target-rejection margin is exactly

`(1-1/q) + h_hat - A f_hat = 1/110`.

After propagating the common baseline error exactly, the target-rejection inequality becomes the linear condition

`1/110 - (1 - 1/q + 1 + A) delta > 0`.

Since `1 - 1/q + 1 + A = 67/55`, the exact critical error is

`delta_crit = (1/110)/(67/55) = 1/134 ~= 0.0074626866`.

Thus, under this deterministic symmetric error model, **an aggregate timing-error guarantee strictly below about 0.7463% of the observed dense baseline is sufficient to preserve the illustrative 1.10x impossibility certificate**. At `delta=1/134`, `g_rob=10/11=1/q` exactly, so the strict rejection certificate is lost at equality. For reference, exact checks give:

- `delta=1/200`: `g_rob=9983/10945 > 10/11`, target rejected;
- `delta=1/134`: `g_rob=10/11`, boundary/equality, not rejected;
- `delta=1/100`: `g_rob=4933/5445 < 10/11`, this information alone cannot reject the target.

This converts the R19 attribution ceiling into a concrete instrumentation requirement: timing uncertainty is not a harmless reporting detail when the speedup ceiling sits close to a target threshold.

## Machine verification

`research_checks/RS_CFD_SPECTRAL_HYBRID_B7E2C1_R23.py` uses exact `fractions.Fraction` arithmetic. It checks the endpoint extremum on 1,296 admissible finite-grid boxes, verifies the exact `1/134` threshold and the three rational denominator values above, and contains the same fail-closed native-host probe. The persisted JSON certificate records the current host gate and exact arithmetic results.

## Boundary and next unit

This is a deterministic measurement-identifiability result layered on canonical R19. It is not a spectralDNS/shenfun/MPI/FFTW native benchmark, not a measured speedup, not a claim that the illustrative error model matches future hardware, and not independent trajectory verification. The parent task remains `CONTINUATION_REQUIRED`.

The smallest decisive next unit remains the frozen 32^3 Taylor-Green dense / guarded-hybrid / forced-fallback A/B/C RK4 experiment on an already provisioned pinned host. In addition to R19's `T,D,H,alpha,w` quantities, that run should publish deterministic or statistically justified uncertainty bounds for the aggregate timing measurements. The verifier can then evaluate `g_rob` directly and reject any target speedup whose robust attributable ceiling is below the target rather than comparing point estimates alone.
