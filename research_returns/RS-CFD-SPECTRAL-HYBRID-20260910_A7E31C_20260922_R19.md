# CFD continuation R19: full-trajectory sparse-attributable cost ceiling

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-CFD-A7E31C`  
Claim: `CLM-CFD-A7E31C-20260922-R19`  
State: `CONTINUATION_REQUIRED / EXACT COST CEILING / NO NATIVE SPEEDUP CLAIM`

## Consumed frontier

This unit consumes R18 (`c30a94558e521428cb0545945340118cd6fbc070`) without replay. R18 proved the sharp route-count/heterogeneity envelope

`w_sparse <= k rho / (k rho + n-k)`

for `k` sparse-eligible calls among `n` nonlinear calls when paired dense-reference call costs have ratio at most `rho`. R18 also established that route counts alone cannot identify weighted sparse work when `rho` is unbounded.

The unresolved native experiment still requires an already provisioned pinned spectralDNS/shenfun/MPI/FFTW host. This unit does not claim such execution.

## New theorem: trajectory-level ceiling with unchanged work and additive overhead retained

Let the dense-reference trajectory cost be

`T0 = R + D`, where `D = sum_i D_i` is the total dense nonlinear-call cost and `R >= 0` is all other baseline trajectory work.

Let `E` be the sparse-eligible call set with `|E|=k`, `0<k<n`, and suppose:

1. `max_i D_i / min_i D_i <= rho`, `rho >= 1`;
2. the sparse route can save at most an `alpha_bar` fraction of the paired dense cost on any eligible call, with `0 <= alpha_bar <= 1`;
3. the dense nonlinear fraction obeys `D/T0 <= f_bar`, `0 <= f_bar <= 1`;
4. additive hybrid-only cost not already included in the sparse/fallback paired costs is at least `H_floor`, with `h_floor = H_floor/T0 >= 0`;
5. fallback/non-eligible execution does not create an unrelated negative cost delta. Equivalently, after isolating sparse savings, the hybrid trajectory obeys

`T_hybrid >= T0 - alpha_bar * sum_{i in E} D_i + H_floor`.

Then, writing `w = sum_{i in E}D_i / D`,

`T_hybrid/T0 >= 1 - alpha_bar * f_bar * w + h_floor`.

Using the R18 sharp upper envelope for `w` gives

`S = T0/T_hybrid <= 1 / (1 - alpha_bar*f_bar*[k rho/(k rho+n-k)] + h_floor)`

whenever the denominator is positive.

This is a sparse-attributable full-trajectory ceiling, not merely a nonlinear-kernel ceiling. It explicitly keeps unchanged trajectory work and additive guard/setup/fallback overhead rather than silently setting both to zero.

### Sharpness under this information model

For fixed admissible `(k,n,rho,alpha_bar,f_bar,h_floor)`, the bound is attained by an extremal construction whenever the stated ratios are jointly realizable: assign dense cost `rho` to every eligible call and `1` to every ineligible call, choose unchanged work so `D/T0=f_bar`, make every eligible call realize exactly the allowed fractional saving `alpha_bar`, and set additive hybrid-only cost exactly to `h_floor*T0`. Therefore no smaller universal ceiling follows from only these inputs.

## Exact target-speedup inversion

For a target `q>1`, define

`tau = (1 - 1/q + h_floor)/(alpha_bar*f_bar)`

when `alpha_bar*f_bar>0`.

For `0<k<n` and finite `rho`, reaching even the information-theoretic ceiling `S>=q` requires `tau<1` and

`rho >= max(1, tau*(n-k)/(k*(1-tau)))`.

If `alpha_bar*f_bar=0`, or if `tau>=1`, no finite `rho` can make the target feasible under this model. The formula is exact: at the raw threshold above, the ceiling equals `q`.

This turns the native experiment into a fail-closed attribution check. A claimed target speedup must be compatible simultaneously with measured/bounded dense-call heterogeneity, the nonlinear share of baseline time, the maximum sparse-route fractional saving, and the additive hybrid-only overhead. A route-count argument that drops any of these terms can overstate the attainable whole-trajectory benefit.

## Frozen R10 route-count illustration only

The following values are deliberately illustrative and are **not measurements** from a native spectralDNS host. Keep the frozen route counts from R10, set `rho=2`, and use hypothetical bounds `alpha_bar=7/10`, `f_bar=4/5`, `h_floor=1/50`.

For `k=2,n=20`:

- `w_sparse <= 2/11`;
- `S <= 110/101 ~= 1.0891089x`.

For `k=1,n=20`:

- `w_sparse <= 2/21`;
- `S <= 30/29 ~= 1.0344828x`.

Thus, under these illustrative finite bounds, `1.10x` is already impossible at `rho=2` for both frozen route patterns even though R18's overhead-free/nonlinear-only idealization could look less restrictive.

For target `q=11/10`, the exact required eligible-work share is

`tau = 61/308`.

The corresponding minimum dense-call heterogeneity is:

- `rho >= 549/247 ~= 2.2226721` for `k=2,n=20`;
- `rho >= 61/13 ~= 4.6923077` for `k=1,n=20`.

At each exact threshold the trajectory ceiling is exactly `11/10`.

## Machine verification

`trajectory_cost_ceiling.py` uses only `fractions.Fraction` and checks:

- the R18 sharp lower/upper `w_sparse` envelopes on a finite exact grid and their extremal constructions;
- the exact frozen-route ceilings `110/101` and `30/29` for the stated illustrative parameters;
- the target inversion `tau=61/308`, `rho_min=549/247` and `61/13`;
- equality to `11/10` at each threshold;
- monotonicity of the ceiling in `rho` for the frozen routes;
- a fail-closed case where `tau>1` correctly returns no finite heterogeneity threshold.

Local `python -m py_compile` and execution both passed; the emitted JSON certificate is persisted beside the checker.

## Boundary and next unit

This result is an exact finite cost-identifiability theorem layered on R18. It is not a spectralDNS/shenfun/MPI/FFTW native benchmark, not a measured speedup or slowdown, not a general CFD acceleration claim, and not independent verification. The parent task must remain `CONTINUATION_REQUIRED`.

The smallest decisive next unit remains the frozen native dense / guarded-hybrid / forced-fallback A/B/C held-out RK4 experiment on an already provisioned pinned host. In addition to R18's paired dense per-call costs and actual `w_sparse`, record total dense baseline `T0`, nonlinear dense total `D`, all additive hybrid-only guard/setup/allocation/compilation/fallback deltas, and sparse-call paired savings. The verifier can then evaluate this R19 ceiling with measured `f`, `h`, `alpha` rather than illustrative values and reject any claimed whole-trajectory speedup that exceeds the attributable bound.
