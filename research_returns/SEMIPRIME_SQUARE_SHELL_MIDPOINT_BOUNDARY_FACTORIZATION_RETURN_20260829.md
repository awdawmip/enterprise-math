# 半素数平方壳中点—边界—邻近素数分解广域探索：研究回报

Researcher-ID: `EM-SSMF1-5A7C2E`  
Task: `RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION`  
Publication: `TP2-12778A2D48A1D5A57BA9`  
Claim: `chatgpt-ssmf1-20260829-1240-5a7c2e`  
Branch: `research/semiprime-square-shell-midpoint-boundary-em-ssmf1-5a7c2e`

Status: `TERMINAL_RESEARCH_RETURN / EXACT_STRUCTURE_PLUS_REPRODUCIBLE_NO_GO / NO_WORKING_TRUTH_GRANT`

## 1. Terminal classification

Hard-target disposition:

`EXACT_STRUCTURE_WITHOUT_NEW_FACTORIZATION_ADVANTAGE + REPRODUCIBLE_FEATURE_FAMILY_NO_GO`

The result is B+C, not a new factoring algorithm.

- Single-shell midpoint search is exactly Fermat difference-of-squares in square-shell coordinates.
- Local neighboring-prime features do not stably predict the hidden factor prime-rank; scanning those primes is descending trial division.
- Raw multi-k shell residuals are multiplier-Fermat coordinates and sit inside the Lehman/Hart family.
- A finite-window residual-priority multiplier heuristic survives as a narrow empirical residue, but its coverage collapses with bit size and no total-cost or asymptotic advantage is proved.

This does **not** claim a lower bound for general factorization or a no-go for every nonlinear N-only feature.

## 2. Exact theorem: shell midpoint = Fermat

For a distinct odd semiprime

`N=pq`, `3<=p<q`,

let

`s=floor(sqrt(N))`, `A0=s+1`, `b=A0^2-N`,
`A=(p+q)/2`, `B=(q-p)/2`, `T=A-A0`.

Define

`F_N(t)=b+2*A0*t+t^2=(A0+t)^2-N`.

Then

`T = min {t>=0 : F_N(t) is a perfect square}`.

At `t=T`, `F_N(T)=B^2`. Conversely, if `F_N(t)=y^2`, then

`N=(A0+t-y)(A0+t+y)`.

A distinct semiprime has only the positive factor pairs `(p,q)` and `(1,N)`; the nontrivial midpoint is `A`, while `(N+1)/2>A`. Hence the first square residual from `A0` occurs exactly at `T`.

Therefore the task identity

`B^2=b+2*A0*T+T^2`

is not merely close to Fermat; it is an exact coordinate form of Fermat scanning.

### Modular filtering

For any modulus `m`, a necessary condition for candidate `t` is that `F_N(t)` be a quadratic residue mod `m`. This is exactly a Fermat quadratic-residue sieve.

In a fixed 3000-row census sample, with

`M=6720=64*3*5*7`,

the median survivor fraction of `t mod M` is `0.0285714286`; about `97.142857%` of expensive square tests can be rejected by the modular filter. This is a useful constant-factor baseline, not a new shell law.

## 3. Exact factor-ratio decomposition

Let

`lambda=q/p >= 1`, `h=(1/2)log(lambda)`.

Then

`A=sqrt(N) cosh(h)`.

Writing

`delta=A0-sqrt(N)=b/(A0+sqrt(N))`, with `0<delta<1`,

gives the exact identity

`T=sqrt(N)(cosh(h)-1)-delta`.

Equivalently,

`A-sqrt(N)=(sqrt(q)-sqrt(p))^2/2`.

Thus the square shell contributes only the subunit rounding correction `delta`; the macroscopic midpoint displacement comes from the hidden factor ratio. The coordinates `(s,b)` or `(L,D)` remain reversible encodings of `N`; any algorithmic gain must come from a cheaper selector/search order, not from treating the encoding as extra information.

## 4. Exact census through 10^7

Population:

all odd nonsquare semiprimes `N=pq<=10^7`, `3<=p<q`, `p,q` prime.

Count:

`1,555,366`.

All exhaustive rows passed:

- `a+b=L`;
- `4N-1=L^2-2D`;
- `B^2=b+2*A0*T+T^2`.

A deterministic sparse audit also passed the task's exact multi-k transport identity

`D_k=kD+(L_k^2-kL^2+1-k)/2`.

Task-specific checker:

`research_checks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CHECK_20260829.py`

Observed checker result in this execution:

`PASS`, with zero shell, bridge, multi-k, and counterexample failures.

### Correlations

Let `u=b/(2s+1)`.

| observable | Pearson correlation |
|---|---:|
| `u` vs `log(1+T)` | `0.0073965413` |
| `u` vs `T/A0` | `-0.0002188409` |
| `u` vs `log(q/p)` | `0.0026841966` |
| `u` vs `log(1+J_p)` | `0.0175963309` |
| local two-sided prime gap vs `log(1+J_p)` | `0.1139426530` |

The last value is the strongest simple surface correlation seen, but it is a size/density confound. By N bands `[1e5,1e6)`, `[1e6,3e6)`, `[3e6,6e6)`, `[6e6,1e7]`, the same gap/rank correlation is approximately `0.0600, 0.0168, -0.0091, 0.0147`.

### Independent holdout

Discovery/training: `1e6<=N<8e6`, fixed random sample `300,000`.  
Holdout: `8e6<=N<=1e7`, fixed random sample `120,000`.  
Target: `log(1+T)`.

A HistGradientBoostingRegressor using only `log N` gave:

- holdout `R^2=-0.0007864106`;
- MAE `2.2187763454`.

Adding `u`, local neighboring-prime distances/gap, and normalized multi-k shell residual phases for `k=2..16` gave:

- holdout `R^2=-0.0015425947`;
- MAE `2.2274852191`.

Thus the tested shell-rich features do not produce a transferable midpoint predictor.

## 5. Systematic counterexamples

### Same shell index and same local prime neighborhood

`9,917,459 = 3079*3221`:

- `s=3149`, `b=5041`;
- `PrevPrime(s)=3137`, `NextPrime(s)=3163`;
- `T=0`, `q/p≈1.04612`.

Only two integers away,

`9,917,461 = 1009*9829`:

- `s=3149`, `b=5039`;
- exactly the same neighboring primes `3137/3163`;
- `T=2269`, `q/p≈9.74133`.

### Extreme amplification

`9,990,157 = 3119*3203`: `s=3160`, `b=1764`, `T=0`.

`9,990,159 = 3*3,330,053`: `s=3160`, `b=1762`, `T=1,661,867`.

Again the shell index and local prime neighborhood are identical and `b` differs by only two.

### Exact same b

`5,157,223 = 2203*2341` and `9,979,063 = 1013*9851` both have `b=218`, while their `T` values are `1` and `2273`.

These examples do not prove a complexity lower bound. They falsify the candidate claim that local boundary residual / local prime environment approximately determines the true midpoint or factor ratio.

## 6. Neighbor-prime route

Define

`J_p=pi(s)-pi(p)`.

A scan of primes downward from the largest prime `<=s` reaches `p` after exactly `J_p+1` prime candidates. This is descending prime trial division. `J_p` itself is an oracle label because it uses the hidden factor `p`.

For `N>=10^6`, median candidate counts by hidden ratio stratum are:

| `q/p` | prime candidates `J_p+1` | Fermat candidates `T+1` |
|---|---:|---:|
| `[1,1.01)` | 1 | 1 |
| `[1.01,1.05)` | 4 | 1 |
| `[1.05,1.1)` | 10 | 2 |
| `[1.1,1.25)` | 22 | 7 |
| `[1.25,1.5)` | 42 | 27 |
| `[1.5,2)` | 70 | 81 |
| `[2,4)` | 117 | 290 |
| `[4,10)` | 181 | 970 |
| `[10,100)` | 255 | 4038 |
| `[100,inf)` | 336 | 173883 |

The crossover for imbalanced factors is a comparison of two classical search orders, not a shell-predicted rank.

On the 24/32/40/48/64-bit sample, median two-sided local prime gaps around `floor(sqrt(N))` are `12/14/20/24/32`, with 95th percentiles `28/36/50/66/90`. Computing the local neighborhood itself therefore has a primality/prime-generation cost and does not reveal the hidden lower endpoint `p`.

## 7. Multi-k route = multiplier Fermat / Lehman / Hart

For `k>=1`, let

`x_k=ceil(sqrt(4kN))`,
`e_k=x_k^2-4kN`.

If `e_k=y^2`, then

`x_k^2-y^2=4kN`

and `gcd(x_k±y,N)` tests for a nontrivial factor. If the first point fails, increasing `x` is exactly multiplier Fermat on `4kN`.

The task's multi-k shell residual therefore lies in the same search object used by classical multiplier methods.

Baseline references:

- R. Sherman Lehman, *Factoring Large Integers*, Mathematics of Computation 28 (1974), 637–646, DOI `10.1090/S0025-5718-1974-0340163-2`.
- William B. Hart, *A One Line Factoring Algorithm*, Journal of the Australian Mathematical Society 92 (2012), 61–69, DOI `10.1017/S1446788712000146`.

Hart explicitly iterates a multiplier and tests the near-square residual; Lehman systematizes multiplier/Fermat search. So a new result here would require a new proved `k` selector, jump rule, or lower-cost residual transport—not a new name for the residual.

### Raw multi-k empirical check

On a fixed 300,000-row small-integer sample for `k=1..32`:

- maximum absolute correlation of normalized `u_k` with `log(1+T)` was about `0.00951`;
- maximum absolute correlation with `log(1+J_p)` was about `0.01876`.

A second dataset used 5000 stratified 24/32/40/48/64-bit semiprimes, 1000 per bit and 250 per factor-bit split. Post-hoc maximum absolute within-stratum correlations over `k=1..32` reach about `0.195`, but the maximizing `k` and sign change across strata; no cross-scale rule survives.

## 8. Narrow surviving residue: residual-priority multipliers

For `k<=64`, define the factor-blind score

`score(k)=e_k/(2*x_k-1)`.

Conditional on an immediate productive multiplier existing inside the window:

- all `N<=10^6`: hit coverage `29.57%`; median ordinary k-rank `18`, residual-score rank `5`;
- discovery `1e6..8e6`, 50k sample: hit coverage `19.81%`; median rank `27 -> 12`;
- holdout `8e6..1e7`, 50k sample: hit coverage `16.33%`; median rank `30 -> 14`.

But `k<=64` immediate-hit coverage across bit sizes collapses:

| bits | hit rate |
|---|---:|
| 24 | 43.3% |
| 32 | 8.8% |
| 40 | 2.2% |
| 48 | 0.6% |
| 64 | 0% |

This is recorded only as

`FINITE_WINDOW_RESIDUAL_PRIORITY_HEURISTIC / NOT_A_FACTORIZATION_RESULT`.

A full score ordering also requires generating every `x_k/e_k` and adds sorting/selection overhead. Candidate-rank improvement alone is not total-cost improvement.

## 9. Cost accounting

### Single-shell/Fermat

- midpoint candidates: `T+1`;
- naive square tests: up to `T+1`;
- modular sieve: one or more cheap residue checks per candidate / periodic skip, reducing expensive square tests by a constant factor;
- gcd: constant number at a successful square;
- shell coordinates require one integer sqrt plus O(1) arithmetic and do not shorten T by themselves.

### Neighbor-prime scan

- prime candidates/divisibility tests: `J_p+1`;
- local PrevPrime/NextPrime preprocessing adds primality/prime-generation work;
- knowing `J_p` directly would leak `p`.

### Multiplier shell

For K multipliers:

- K ceil-sqrt computations or equivalent exact state updates;
- up to K residual square tests before modular filtering;
- gcd on successful residuals;
- full residual-priority sorting adds O(K log K), unless a streaming/bucket rule is used and its cost is counted.

## 10. Tool reuse gate

Current `enterprise_toolbox_registry.json` was checked after the problem structure was understood. `T1 Enterprise Scale Enumeration / Valuation Calculus` has a generic `shell` trigger, but its accepted scope concerns scale enumeration/finite-difference/valuation shell extraction, not integer square-boundary factorization.

No accepted toolbox item replaces the exact-integer Fermat/multiplier/trial-division audit here.

Classification:

`NOT_APPLICABLE_FOR_FACTORIZATION_CORE`.

Only a task-specific checker is added; no new general tool family is claimed.

## 11. Exact no-go boundary

Within the tested feature family:

- adjacent-square shell local/normalized coordinates;
- local nearest-prime distances/gap around `sqrt(N)`;
- finite raw multi-k shell phases;

there is no observed factor-blind rule that transfers to an independent scale holdout and reduces total search cost below the corresponding Fermat, trial-division, or multiplier-Fermat baseline.

Exact equivalence boundaries:

- single-shell midpoint scan -> Fermat;
- congruence filtering -> Fermat quadratic-residue sieve;
- neighboring-prime rank scan -> prime trial-division order;
- raw multi-k near-square residual -> multiplier-Fermat / Lehman / Hart family.

## 12. Minimal unresolved question

Keep only:

`RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT`.

Question: with `K(N)` scaled into a Lehman/Hart-relevant range rather than fixed 64, can a streaming threshold/bucket order on the upper-square residual reduce **total** cost after charging for sqrt/transport, modular filters, square tests, gcds, and queue/bucket maintenance?

Kill condition:

- only conditional hit rank improves while total k-generation/sqrt cost does not;
- coverage continues to collapse with bit size; or
- the method reduces to known Hart multiplier order plus standard modular sieving.

Do not spend another generation expanding static single-shell/midpoint correlation tables; the exact equivalence and counterexamples already identify the main obstruction.

## 13. Reproducible outputs

- `research_returns/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_RETURN_20260829.md`
- `research_checks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CHECK_20260829.py`
- `research_artifacts/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY/experiment_summary_20260829.json`

No Working Truth, Foundation authority, or canonical-promotion claim is made.
