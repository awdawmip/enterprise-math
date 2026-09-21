# RS-CFD-TRAJECTORY-VERIFY-20260910 — cross-cycle dependence boundary AA1231

Status: `CONTINUATION_REQUIRED`  
Researcher: `EM-CFD-VFY-XCYCLE-AA1231`  
Claim: `CLM-CFDVFY-AA1231-20260922-0523`

## Reconciled frontier

This unit starts from the expired predecessor claim `CLM-CFDVFY-91D4E7-20260922-0158` only after reconciling its durable server branch head `d7e86fe1699ec7b1d5d9a77a8f1d370da5610bbb`. That frontier already contains the completed 23-cycle manifest and checker, so this unit does not replay or take credit for the predecessor's manifest freeze.

The frozen successor design has 23 cycles, six A/B/C triplets per cycle, 138 triplets and 414 arm executions. For each confirmatory component, a cycle is positive at >=4/6 strict-positive triplet contrasts and the primary count gate is >=16/23. Under independent cycles the frozen exact reference tail is `763/16384 ≈ 0.046569824`.

## Exact marginal-only dependence theorem

Let `X_1,...,X_n` be the cycle-success indicators for a null component gate. Assume only the per-cycle consequence supplied by the within-cycle central-symmetry argument,

`P(X_i=1) <= 1/2` for every cycle,

and allow otherwise arbitrary dependence across cycles. Put `S=sum_i X_i`. Then for every integer threshold `r>=1`,

`sup P(S>=r) = min(1, n/(2r)).`

The upper bound is immediate from `E[S] <= n/2` and Markov's inequality. It is sharp:

- if `r <= n/2`, choose a uniformly random `r`-subset on every draw; then every marginal is `r/n <= 1/2` and `S=r` surely;
- if `r > n/2`, with probability `p=n/(2r)` choose a uniformly random `r`-subset and otherwise choose the empty set. Then each marginal is exactly `p*r/n=1/2`, while `P(S>=r)=p=n/(2r)`.

This witness is exchangeable; the failure is therefore not an artifact of labeling or cycle order.

## Consequence for the frozen 23-cycle gate

For the frozen primary `n=23, r=16` gate, the exact arbitrary-cross-cycle-dependence supremum is

`23/32 = 0.71875`,

not the independent-binomial `763/16384 ≈ 0.046569824`. The worst-case null passage probability is therefore larger by the exact factor

`(23/32)/(763/16384) = 11776/763 ≈ 15.433814`.

For the alternate Bonferroni threshold `r=17`, the marginal-only supremum remains `23/34 ≈ 0.676471`. Even the strongest possible count threshold, all 23 cycles positive, has worst-case size `1/2`. Hence **no success-count threshold on 23 cycles can achieve alpha .05 from per-cycle validity alone**. Increasing cycle count does not repair this without additional joint-law information: at threshold `r=n`, the same sharp marginal-only bound is always `1/2`.

For the strict `AB AND CB` intersection-union target, this is also an exact global-null obstruction. One component may be null and attain the sharp witness while the other component passes deterministically; therefore the IUT's worst-case size under marginal-only cross-cycle information is also `23/32` at the frozen 16/23 gate. IUT removes the need for AB/CB *cross-gate* independence, but it does not remove the need to calibrate dependence *across cycles within a component*.

The AC `>=16/23` negative-control veto has the same `23/32` marginal-only worst-case trigger probability under a no-direction null. Since AC is a veto, this creates false-veto/instability risk rather than a false speedup acceptance, but the nominal binomial tail must likewise not be quoted without cross-cycle calibration.

## Machine verification

`research_checks/RS_CFD_TRAJECTORY_VERIFY_AA1231.py` uses exact `Fraction` arithmetic. It re-derives the frozen independent tails, checks the sharp arbitrary-dependence formula and exchangeable witness for every `(n,r)` with `1<=n<=64`, verifies the frozen `23/32`, `23/34`, and `1/2` values, proves by exhaustive threshold scan that alpha `.05` is unattainable from marginal validity alone, and checks the exact inflation factor `11776/763`. `py_compile` and checker execution pass.

The current execution host was also checked and does not contain `spectralDNS`, `shenfun`, `mpi4py`, `mpi4py_fft`, `pyfftw`, `mpicc`, `mpicxx`, or `mpirun`; no native run is asserted.

## Decision boundary and next action

The predecessor manifest's fail-closed statement is quantitatively confirmed and strengthened: per-cycle central sign symmetry gives only marginal block validity; by itself it cannot support any alpha-.05 count test, even with all 23 cycles positive. Independent cycles are sufficient but not logically necessary. Any replacement dependence calibration is admissible only if it is **predeclared and strong enough to prove the relevant joint tail bound** before interpreting new timing data.

The 91D4E7 manifest remains immutable. No native CFD timing, speedup/slowdown, generic CFD or industrial acceleration, continuous-PDE theorem, Working Truth, Foundation promotion, or final acceptance is claimed.

Next: on a pinned native host execute the frozen 23-cycle manifest exactly. Before confirmatory interpretation, either provide a defensible cross-cycle independence justification, or bind a separately predeclared joint dependence model/calibration whose null tail at the frozen gate is <=.05; otherwise all block-sign p-values remain descriptive and performance acceptance fails closed.
