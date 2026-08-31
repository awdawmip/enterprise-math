# PCF7 Classification Matrix

Task: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION`  
Researcher: `EM-PCF7R-8595E3`  
Date: `2026-08-31`

## Load-bearing accepted candidates

| Axis | Fixed-public-prefix bridge | N-only valuation-wall streaming splitter |
|---|---|---|
| Exact observable | `gcd(F_L,N)` with `F_L` independent of hidden factors | modular recurrence for `A_s=(2s)!(3s)!/(s!)^5`, dyadic gcd probes, exact synchronized fallback |
| Online success | seed-dependent | deterministic on distinct semiprimes `3<p<q` |
| Success lower bound | none uniformly over semiprimes for fixed finite factor-independent support | 1 on theorem domain |
| Per-probe/per-step cost | polynomial in `n+L` | `O(M(n) log n)` conservatively |
| Total accepted work | polynomial per fixed probe, but generic success can be zero | `O(p M(n) log n)` |
| Balanced semiprime | adversarial support can force all gcds to 1 | `p=Theta(sqrt(N))`, hence sqrt-scale |
| Unbalanced semiprime | same support no-go | cost tracks smaller factor `p` |
| Synchronization | `gcd=N` is a failure to split | `gcd=N` is repaired by `t=floor(sqrt(N)/3)` and `t+1` |
| Peak memory | `O(n+L)` streaming | `O(n)` streaming |
| Exact unmodded integer growth | polynomial bits in `L` for normalized `F_L` | `log A_s=Theta(s)`, exponentially large in `n` at balanced wall |
| Primary verdict | `SUCCESS_PROBABILITY_NOT_LOWER_BOUNDED` | `SQRT_SCALE_OR_WORSE_PROVED` |

Portfolio: `COMPLEXITY_FRONTIER_FROZEN`.

## Failure-family atlas

| Family | Fixed-prefix bridge | N-only wall |
|---|---|---|
| Balanced semiprime | infinite outside-support adversarial family | theorem succeeds; sqrt-scale work |
| Unbalanced semiprime | outside-support adversarial family | theorem succeeds; work `Theta(p)` |
| Near-twin | exact support criterion; no infinite-family extrapolation | theorem succeeds; still balanced |
| Prime power | outside-support primes force gcd 1 at every allowed seed | outside theorem |
| Multifactor | extracts only supported factor subset; all-outside gives gcd 1 | outside theorem |
| Carmichael / strong pseudoprime | labels are secondary; prime support is decisive | outside theorem |
| synchronized/equal response | both factors supported can return `N` | exact fallback resolves synchronization |
| exceptional congruence | represented by `p | F_L` | covered by valuation wall on theorem domain |

## Common-metric baseline

The common metric is bit operations plus peak working memory, with `n=ceil(log2 N)` and multiplication cost `M(n)`.

- Trial division: `O(p M(n))` up to division/polylog factors.
- Fermat: exact increment count approximately `(p+q)/2-sqrt(N)`; excellent near twins, poor when unbalanced.
- Pollard rho: classical heuristic expected `O(sqrt(p))` modular steps.
- Pollard `p-1`: bound/smoothness-dependent; no universal fixed-bound success.
- Frozen blind benchmark: finite regression evidence only; raw algorithm-local counters are not treated as common bit-cost units.

## Checker freeze

`research_checks/PRIME_COORD_FACTOR_COMPLEXITY_FAILURE_CLASSIFICATION_CHECK_20260831.py`

Expected terminal line begins with `PASS` and includes:

- `recurrence_checks=40`
- `fixed_prefix_adversarial_semiprimes=30`
- `alpha_zero_cases=30`
- `prime_power_checks=60`
- `multifactor_checks=10`
- `nonly_semiprimes=13695`
- `nonly_synchronized=2996`
- modes `DYADIC=10699`, `FALLBACK_T=2925`, `FALLBACK_T1=71`

Finite runs are regression certificates, not universal theorem premises.
