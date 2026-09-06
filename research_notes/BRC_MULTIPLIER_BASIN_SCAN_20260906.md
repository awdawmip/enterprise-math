# BRC Multiplier Basin Scan — m=1..100

Status: `RESEARCH EXPERIMENT / FINITE CHECK + PROVED ELEMENTARY IDENTITIES / NO FOUNDATION CLAIM`
Date: `2026-09-06`
Base main snapshot: `ac194888ca0f3d816b4bd98d9f6729e9eca03039`
Tool-reuse resolution: `EXTEND_EXISTING_TOOL`

## Question

For an arbitrary positive integer `n`, how does its square-root BRC collapse state change after multiplication by `m`?  Sweep every multiplier `1 <= m <= 100`, and inspect both the collapse-basin transfer and the exact `+/-` edit costs.

This experiment keeps three observers separate:

1. point state: root index plus exact remainder;
2. Boolean basin support: which target BRC basins are reached;
3. Weighted-BRC multiplicity: how many source states land in each target basin.

The canonical root collapse remains downward.  The `addition_cost` below is only an experimental next-square completion readout; it does not redefine BRC.

## Canonical reuse

The experiment reuses:

- `src/enterprise_math/core.py::integer_nth_root`;
- `src/enterprise_math/core.py::basin_for_root`;
- T0 BRC root-collapse semantics;
- `src/enterprise_math/brc_weighted.py::CWMState` for unit-weight branch multiplicity;
- T1 scale/enumeration and T6 observer-safe quotient discipline.

Boolean support, multiplicity and source provenance are not silently identified.

## Exact point law

Let

`k = floor(sqrt(n))`, `n = k^2 + r`, `0 <= r <= 2k`.

After multiplying by `m`, define

`j = floor(sqrt(mn))`.

Then the canonical subtraction cost and experimental addition cost are

`C_-(mn) = mn - j^2`,

`C_+(mn) = (j+1)^2 - mn`.

Therefore

`C_-(mn) + C_+(mn) = 2j + 1`.

So the two costs are complementary coordinates inside the target BRC basin.  Multiplication does not make the local edit budget scale by `m`; its basin-width scale is governed by `sqrt(m)`:

`(C_- + C_+)/(2k+1) -> sqrt(m)`

uniformly across one source basin as `k -> infinity` for fixed `m`.

Within one fixed target basin, increasing the source number by `1` increases `C_-` by `m` and decreases `C_+` by `m`; crossing a target-square boundary causes the exact sawtooth reset.

## Exact basin pushforward

The source basin is

`B_k = {k^2, ..., (k+1)^2-1}`

with `2k+1` source states.

A target root `j` receives precisely the source interval

`max(k^2, ceil(j^2/m)) <= n <= min((k+1)^2-1, floor(((j+1)^2-1)/m))`.

Hence its exact branch multiplicity is the integer length of that interval.  For unit source weights this is represented as

`CWM_j = (count_j, count_j, 1)`.

The same interval gives the add/sub totals without enumerating its points:

`SUM_- = m * SUM(n) - count_j * j^2`,

`SUM_+ = count_j * (j+1)^2 - m * SUM(n)`.

Thus the experiment is an exact interval/histogram computation, not a floating square-root simulation.

## Stable m<=100 regime

For every `m<=100` and every scanned source root `k>=5`,

`m <= 4k^2`.

This is a sufficient condition that adjacent source integers cross at most one target root boundary.  The finite scan confirmed **zero nonconsecutive target-support cases** for all `m=1..100`, `k=5..5000`.

Consequently in this regime the target support is a consecutive block and its size is

`H_m(k) = floor(sqrt(m*((k+1)^2-1))) - floor(k*sqrt(m)) + 1`.

No floating value is needed to evaluate this formula: the implementation uses exact integer roots.

## Square multipliers: exact regular family in the scan

For `m=s^2`, the next-square endpoint has zero defect.  In the stable regime the source basin maps to exactly

`sk, sk+1, ..., s(k+1)-1`,

so

`H_{s^2}(k)=s`.

For all ten square multipliers up to 100,

`1,4,9,16,25,36,49,64,81,100`,

the complete `k=5..5000` scan verified:

- support size is exactly `sqrt(m)` for every source basin;
- target support is consecutive;
- unit-weight branch multiplicities differ by at most `1` inside each source basin;
- no square-multiplier balance failure occurred.

Example at `k=100`:

- `m=4`: counts `(101,100)` across target roots `(200,201)`;
- `m=9`: counts `(67,67,67)` across `(300,301,302)`.

This is the cleanest multiplication family found in round 1.

## Non-square multipliers: Beatty step + Pell-type endpoint resonance

Let `q=k+1`,

`t=floor(q*sqrt(m)) = floor(sqrt(m*q^2))`,

and define the exact near-square defect

`D_m(q)=m*q^2-t^2`.

The source basin ends at `m(q^2-1)=mq^2-m`.  In the present stable window the final target root drops by one exactly when

`D_m(q)<m`.

For non-square `m`, the equations

`t^2 - m q^2 = -D`, `1 <= D < m`,

are generalized Pell-type near-square conditions.  These endpoint events are rare in the finite scan, but real; they are the exceptional corrections to the ordinary Beatty-step pattern.

Examples:

- `m=2`: 3 endpoint resonances for `k=5..5000`; first at `k=28,168,984`, all with defect `1`;
- `m=3`: 5 resonances; first at `k=10,40,152,570,2130`, defect `2`;
- across non-square `m<=100`, the largest observed resonance count was `42` (for `m=95` and also some nearby cases), out of 4996 source basins.

Ignoring the sparse endpoint correction, the increment

`floor((k+1)*sqrt(m)) - floor(k*sqrt(m))`

is one of the two adjacent integers around `sqrt(m)`.  This explains why the ordinary support size concentrates around `sqrt(m)+1` for non-squares, whereas perfect squares sit on the exceptional exact law `sqrt(m)`.

The asymptotic zero-density statement for the generalized Pell correction is **not promoted here as an Enterprise theorem**; it is the next proof target.

## Round-1 100-multiplier sample

The committed CSV contains all multipliers.  Selected rows:

| m | type | support-size histogram over k=5..5000 | endpoint resonances |
|---:|---|---|---:|
| 2 | nonsquare | `2:2930; 3:2066` | 3 |
| 3 | nonsquare | `2:1344; 3:3652` | 5 |
| 4 | square | `2:4996` | 4996 (zero-defect square endpoint) |
| 5 | nonsquare | `3:3826; 4:1170` | 9 |
| 8 | nonsquare, squarefree kernel 2 | `3:869; 4:4127` | 11 |
| 9 | square | `3:4996` | 4996 |
| 26 | nonsquare | `5:1; 6:4519; 7:476` | 20 |
| 50 | nonsquare, squarefree kernel 2 | `7:3; 8:4660; 9:333` | 25 |
| 100 | square | `10:4996` | 4996 |

The rare lower support values such as the single `H_26(k)=5` case are endpoint-resonance witnesses that disappear if only the coarse `sqrt(m)+1` heuristic is kept.

## Squarefree multiplier families

Writing

`m = a^2 d`

with `d` squarefree exposes a natural family coordinate.  Multipliers sharing `d` share the same quadratic irrational direction `sqrt(d)` and differ by the integer refinement factor `a`.

Example `d=2` family below 100:

`2,8,18,32,50,72,98`.

Their mean support sizes over the finite scan track `a*sqrt(2)+1`, with sparse endpoint corrections.  This suggests a useful decomposition:

`non-square irrational phase (d) + square refinement depth (a)`.

However, composing through an intermediate BRC collapse is exact only if root remainder/provenance is retained.  Boolean support alone is not enough to reconstruct the later cost state.  This is an explicit observer-loss witness supporting the current BRC rule that erased detail cannot be inferred back.

## Cost finding

The clean invariant is not either cost separately but their sum:

`C_- + C_+ = target basin width = 2 floor(sqrt(mn)) + 1`.

Individual `C_-` and `C_+` form complementary sawtooth coordinates.  Their envelopes scale as `O(sqrt(mn))`; across large source basins their average scale is therefore `sqrt(m)` times the original basin scale.  The multiplier-specific information lives mainly in the phase/reset pattern and in the Weighted-BRC target histogram.

This suggests that future algebra should keep the pair

`(target_root, remainder)`

rather than only a scalar edit cost.

## Reuse / novelty status

`coverage_verdict = EXTEND_EXISTING_TOOL`.

This experiment does **not** create a new BRC family.  It composes canonical root-collapse with unit-weight Weighted-BRC multiplicity and adds one new application surface: exact multiplier-induced point/basin transfer with complementary add/sub edit observables.

No theorem ledger or Foundation file is modified in this round.

## Next research units

1. prove the exact square-multiplier balance law beyond the finite `m<=100, k<=5000` window;
2. formalize the generalized Pell endpoint-resonance set and its density/growth;
3. derive the composition law for `m=a^2 d` while explicitly retaining remainder/provenance;
4. test whether normalized cost phase supplies a useful multiplicative coordinate for factorization/RSA routes;
5. if the above survives, promote the experiment from `experiments/` to a reusable `src/enterprise_math` BRC subtool and add regression tests/tool registry metadata.

## Artifacts

- `experiments/brc_multiplier_basin_scan.py`
- `research_artifacts/brc_multiplier_scan_m1_100_k5_5000.csv`

The CSV is exact finite evidence for `m=1..100`, `k=5..5000`; fractions are stored as numerator/denominator pairs.
