# PREFIX-614-R6 — Exact stopping-time moments for native BRC signed-label coverage

Date: 2026-11-09 (Asia/Shanghai)
Status: AUTHOR_PROVED / TWO_INDEPENDENT_EXACT_RATIONAL_CHECKS / UNREVIEWED / NOT_ADMITTED
Scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Inherited native model: PREFIX-565 Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`.
Immediate dependencies: PREFIX-610--613, especially PREFIX-612's exact count-only occupancy law. No new native graph execution is claimed.

## Exact problem, native observer and scope

Fix `1 <= k <= 6`, `d=2k<=12`, and a legal simultaneously critical weighted BRC source-phase contrast family `pi_theta`, with independent one-step native trials. The carried observer is terminal native phase jointly with one Boolean action-slot tag. The already derived sufficient signed-label law for the declared family is

`P_theta(Y=(ell,s))=(1+48*s*theta_ell)/(2q)`, `s=+1,-1`, `ell=1,...,d`,
and `P_theta(Y=neutral)=1-d/q`.
Here `q=12` for slot0 and `q=24` for slot1 or slot2. The information direction index has probability `1/q` for each ell, independent of theta. The sign and underlying native branch/provenance remain available for later parameter inference; ONLY the stopping rule below projects to the label index and count.

For integer `r>=1`, define `T_{q,d,r}` as the first number of independent native one-step trials after which **each** of the `d` direction labels has appeared at least `r` times. This is the signed-label sampling cost of a count-only stopping rule, NOT a single length-T native trajectory.

## Theorem A — exact closed-form mean and variance, all d and r

Let `G_1,...,G_d` be independent Gamma distributions with **integer shape r and rate 1**, and `Z=max(G_1,...,G_d)`. Put `P_{r-1}(t)=sum_{j=0}^{r-1} t^j/j!`. Then

`F_Z(t)=[1-exp(-t) P_{r-1}(t)]^d`, for `t>=0`.

Write `mu=E Z` and `v=Var Z`. These are *rational numbers*, obtained by the finite exact sums
```
mu = sum_{a=1}^d (-1)^(a+1) C(d,a) *
      sum_{n=0}^{a(r-1)} [t^n] P_{r-1}(t)^a * n! / a^(n+1)

m2 = 2 * sum_{a=1}^d (-1)^(a+1) C(d,a) *
      sum_{n=0}^{a(r-1)} [t^n] P_{r-1}(t)^a * (n+1)! / a^(n+2)

v = m2 - mu^2.
```

For every legal theta and integer `q>=d`:
```
E T_{q,d,r} = q * mu
Var(T_{q,d,r}) = q^2 * v - q * mu.
```
In particular for the native BRC Boolean slot observers, at all `d<=12` and `r>=1`:
```
E T_{24,d,r} = 2 E T_{12,d,r}
Var(T_{24,d,r}) = 4 Var(T_{12,d,r}) + E T_{24,d,r}.
```
The mean comparison holds with no unknown-parameter dependence. It concerns count-only recovery coverage, not a claim about all error metrics or external physical runtime.

**Proof.** Poissonize the trial clock by independent exponential(`q`) waiting times, leaving all original BRC labels untouched. Every direction label now occurs as an independent rate-1 Poisson subprocess (marking/thinning theorem). The `r`th occurrence time for each label is `Gamma(r,1)`, so the Poissonized stopping time equals `Z`. The number `T` of event marks before that time is determined by marks and independent of the exponential holding times. Therefore `E Z=E T/q`, and the conditional-variance identity gives `Var Z=(E T+Var T)/q^2`. Solving yields the mean and variance formulas. For integer r, integrate `P(Z>t)` and `2t P(Z>t)`, expand `[1-exp(-t)P]^d`, and apply `integral_0^infty t^n exp(-a t) dt=n!/a^(n+1)` to obtain the displayed exact rational sums. QED.

## Theorem B — independent finite native-label recurrence certificate

A second exact derivation uses only the count-state Markov chain. Let `n_j` count the number of labels observed exactly `j` times for `0<=j<r`, and `n_r` count capped labels at least r. Let `s=sum_{j<r} n_j`. With `E=E T` and `Q=E T^2`, at the absorbing all-complete state both are zero. At any other state, let `h^{(j)}` move one label from count j to j+1. Then
```
E(h) = [q + sum_{j<r} n_j * E(h^(j))]/s,
Q(h) = [2*q*E(h) - q + sum_{j<r} n_j * Q(h^(j))]/s.
```
These follow by conditioning on one subsequent trial, including the probability `(q-s)/q` that no uncapped label advances. Each recurrence terminates after at most dr capped progress events, and evaluates rationally. An executable Python certificate independently matches the Poisson-integral values against this recurrence for `d=1,2,6,12`, `r=1,2,3,4`, `q=12,24`.

## Reproducible results for all twelve information directions

The following are displays rounded to 12 decimals; the certificate generates the **full exact numerator/denominator** JSON for every case.

| threshold r | E T slot0 (q=12) | E T slot1/2 (q=24) | Var T slot0 | Var T slot1/2 |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 37.238528138528 | 74.477056277056 | 188.118107794082 | 826.949487453384 |
| 2 | 58.045033902078 | 116.090067804156 | 261.819499503551 | 1163.368065818361 |
| 3 | 76.564095144714 | 153.128190289428 | 325.525653971372 | 1455.230806174916 |
| 4 | 93.980348360588 | 187.960696721175 | 384.419456452171 | 1725.638522529861 |

At `r=1`, `mu=H_d=sum_{j=1}^d 1/j`, hence for `d=12`: `E T_12=86021/2310` exactly and `E T_24=86021/1155` exactly.

The finite stopping-distribution tail `P(T<=N)=D_d(N)/q^N` is unchanged from PREFIX-612. The new results supply the exact first two *unbounded-time moments*, which quantify typical sampling consumption and variability rather than only selected percentile thresholds.

## Verification, source and next work

`PREFIX614_R6_exact_waiting_cost_certificate.py` uses Python standard-library `Fraction`, integer combinatorics, two algebraically independent implementations (gamma-tail finite rational sums and symmetry-compressed finite Markov recurrences), and 148 asserted exact checks. Executed locally on 2026-11-09 Asia/Shanghai: `ALL_CHECKS_PASS 148`. Its companion full machine-readable output is `PREFIX614_R6_RESULTS.json`, generated from the script itself. No Monte Carlo, floating-point inference, or new PREFIX-565 native graph run enters the proof; decimals above are only display values. This is a source-typed result under the PREFIX-610 signed-label model. Independent Source mathematical review and formal task admission are still open.

Next: combine the exact `T_{q,d,r}` cost with PREFIX-613's deterministic anytime confidence-width envelope, choosing the smallest r that implies a target width, and assess whether expected sample cost is optimal against sign-adaptive stopping. Retain the native endpoint/tag and branch provenance for future observables; index-only reduction is certified for the present count stopping law.
