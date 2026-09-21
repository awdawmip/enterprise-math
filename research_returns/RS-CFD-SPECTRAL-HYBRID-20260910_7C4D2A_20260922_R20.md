# CFD continuation R20: exact fail-closed ceiling under incomplete route telemetry

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`  
Publication: `TP2-C3B717C14153D5AC45BF`  
Researcher: `EM-CFD-HR11-7C4D2A`  
Claim: `CLM-CFD-7C4D2A-20260922-R20`  
State: `CONTINUATION_REQUIRED / EXACT TELEMETRY-COMPLETENESS GATE / NO NATIVE SPEEDUP CLAIM`

## Consumed frontier and execution boundary

This unit consumes R19 at immutable commit `043e0a563c60dabc141a51387865feb364a4cc6a` without replay. R19 proved the whole-trajectory sparse-attributable ceiling

`S <= 1 / (1 - alpha_bar*f_bar*w + h_floor)`

and, when all route labels are known and exactly `k` calls are sparse-eligible among `n`, the R18/R19 envelope

`w <= k*rho/(k*rho+n-k)`.

The current execution environment was rechecked before extending the theorem. `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft`, and `pyfftw` are absent, as are `mpicc`, `mpicxx`, and `mpirun`. Therefore the frozen native dense/guarded-hybrid/forced-fallback experiment cannot honestly be run here; this unit does not substitute a Python semantic model for that required native host.

## BRC applicability and retained carrier

BRC resolution: `REUSE_APPLIED` at the information-retention layer. The relevant positive carrier is the labeled population of nonlinear calls with positive paired dense costs `D_i`, route-certainty labels (`certified eligible`, `certified ineligible`, `unknown`), and the future observer `sum_{i in E} D_i / sum_i D_i`. Collapsing this carrier to a route count erases exactly the dense-cost weighting needed for the trajectory speedup ceiling. The R20 result therefore preserves route provenance and positive weights; it does not manufacture a branching law beyond that typed use.

## New theorem: sharp eligible-work envelope with missing route labels

Consider `n >= 1` nonlinear calls with positive paired dense costs `D_i`. Let `K` be the certified sparse-eligible calls, `|K|=k`, and let `U` be calls whose route label is missing/unknown, `|U|=u`, where `0 <= u <= n-k`. The true eligible set satisfies

`K subseteq E subseteq K union U`.

Assume a separately certified finite dense-call heterogeneity bound

`max_i D_i / min_i D_i <= rho`, with `rho >= 1`.

Set `m=k+u`. Then the worst-case fraction of dense nonlinear work that could be eligible is

`w_E = sum_{i in E} D_i / sum_i D_i <= w_max = m*rho/(m*rho+n-m)`.

This is sharp under exactly this information model.

### Proof

Let `d_min=min_i D_i>0`. At most `m` calls can be eligible. Their total dense cost is at most `m*rho*d_min`; every remaining call costs at least `d_min`. Hence

`w_E <= m*rho*d_min / [m*rho*d_min + (n-m)d_min] = m*rho/(m*rho+n-m)`.

Equality is attained by declaring every unknown call eligible, assigning dense cost `rho*d_min` to all `m` potentially eligible calls, and `d_min` to each of the remaining `n-m` calls. Thus no smaller universal upper bound follows from only `(n,k,u,rho)`.

The theorem is deliberately fail-closed: every missing route label is treated as eligible in the extremizer. Missing telemetry can therefore weaken a performance-impossibility certificate, but can never make it spuriously stronger.

## Whole-trajectory ceiling with route uncertainty

Retain R19's assumptions: the sparse path can save at most an `alpha_bar` fraction of paired dense eligible-call cost; dense nonlinear work is at most fraction `f_bar` of the dense trajectory; additive hybrid-only overhead is at least fraction `h_floor` of the dense trajectory; unrelated fallback effects are not credited as sparse savings. Whenever the resulting denominator is positive,

`S <= 1 / (1 - alpha_bar*f_bar*[m*rho/(m*rho+n-m)] + h_floor)`.

Therefore a native run with incomplete route logging must use `m=k+u`, not only the observed eligible count `k`. Treating unknown calls as ineligible would be an information-loss error.

## Exact telemetry-completeness inversion for a target speedup

For target `q>1` and `alpha_bar*f_bar>0`, define

`tau = (1 - 1/q + h_floor)/(alpha_bar*f_bar)`.

The R20 ceiling certifies `S <= q` exactly when `w_max <= tau`. If `tau >= 1`, every route-uncertainty pattern passes this particular ceiling test because `w_max<=1`. If `0<tau<1`, the condition is equivalent to

`m <= tau*n / [rho*(1-tau)+tau]`.

Hence the maximum total number of calls that may be either certified eligible or route-unknown while retaining the `S<=q` certificate is

`m_max = floor(tau*n / [rho*(1-tau)+tau])`,

and the maximum number of missing route labels is

`u_max = m_max-k`.

If `u_max<0`, the target cannot already be ruled out from the certified eligible calls alone. If `alpha_bar*f_bar=0`, sparse arithmetic has no modeled trajectory-saving channel and the ceiling is at most `1/(1+h_floor)<=1`, so every `q>1` is automatically above the ceiling.

This integer threshold is sharp: once `m` exceeds `m_max`, the extremal cost assignment from the preceding proof violates the target certificate.

## Frozen R19 illustration only: one missing route can destroy the 1.10x impossibility certificate

Reuse R19's explicitly hypothetical values, not native measurements:

`n=20, rho=2, alpha_bar=7/10, f_bar=4/5, h_floor=1/50, q=11/10`.

Then

`tau = 61/308`

and

`m_max = floor[(61/308)*20 / (2*(247/308)+61/308)] = floor(244/111) = 2`.

Consequences:

- if `k=2`, then `u_max=0`; one missing route label is enough to destroy this finite `S<=1.10` certificate;
- if `k=1`, then `u_max=1`;
- if `k=0`, then `u_max=2`.

For the `k=2` case, complete telemetry gives the R19 ceiling `110/101 ~= 1.0891089x`. With just one unknown route call, the fail-closed envelope uses `m=3`, giving `w_max=6/23` and a weakened ceiling

`S <= 230/201 ~= 1.1442786x`,

which no longer rules out `1.10x`. This is not evidence that the unknown call was actually sparse or that `1.10x` occurred; it is a precise statement that the existing finite attribution certificate has lost enough information to exclude it.

## Machine verification

`research_checks/RS_CFD_SPECTRAL_HYBRID_7C4D2A_R20.py` uses exact `fractions.Fraction` arithmetic and completed successfully after `py_compile`. Its persisted certificate records:

- 20,048 exact finite route/cost-grid checks of the upper envelope;
- 220 exact sharpness witnesses;
- 13,680 exact target-inversion equivalence checks;
- 12 zero-effect boundary checks;
- the illustrative exact identities `tau=61/308`, `m_max=2`, `110/101`, and `230/201`.

The finite checker supports the algebra and boundary handling; the general theorem itself is the preceding symbolic inequality, not an inference from finite enumeration.

## Boundary and next decisive unit

R20 is an exact finite cost-identifiability/telemetry theorem. It is not a spectralDNS/shenfun/MPI/FFTW native benchmark, not a measured speedup or slowdown, not a general 3D CFD acceleration claim, not a continuous-PDE theorem, and not independent verification. The parent task remains `CONTINUATION_REQUIRED`.

On an already provisioned pinned native host, execute the frozen dense/guarded-hybrid/forced-fallback A/B/C held-out RK4 experiment. In addition to R19's paired dense costs, `T0`, `D`, sparse-call savings, and additive hybrid overhead, record an explicit route label for every nonlinear call plus the count of missing/invalid route records. Before any speedup attribution, apply R20 with the observed `u`; if `u>u_max` for the stated target and validated bounds, mark the finite impossibility certificate unavailable rather than silently treating missing calls as fallback. Then route the immutable native checkpoint to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review.
