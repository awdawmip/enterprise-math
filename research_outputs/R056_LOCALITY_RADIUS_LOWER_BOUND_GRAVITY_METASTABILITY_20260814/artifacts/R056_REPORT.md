# R056 Final Report — Locality-Radius Lower Bounds for Fixed-N Gravity Metastability

Researcher-ID: `EM-R056-BEC623`

Primary classification: **`FINITE_LOCAL_COOPERATIVE_ESCAPE_FOUND`**.

## Frozen conclusions

- `BOUNDED_SUPPORT_STRICT_DESCENT_OBSTRUCTION = FALSE`.
- The exact fixed local family `u=(r,0) -> v=(r-2,3)` is an admissible `D(1,3)` strict descent for every integer `r>=7`.
- `rho_m(r)=3` for each `m in {1,2,3}` and every `r>=7`.
- minimal moved-cell count = `1`.
- minimal support radius within the frozen class = `3`.
- no cooperative multi-cell move is required.
- R055 radius-1 D1 metastability is therefore not a universal obstruction for fixed-locality strict descent.

## Exact algebra retained

`DeltaG = N*DeltaQsum - L(S,DeltaS) - Q(DeltaS)`.

For centered shells:

`DeltaG = N_r*DeltaQsum - Q(DeltaS)`.

At `r=7` the escape family has `DeltaQsum=0`, `DeltaS=(-2,3)`, `Q(DeltaS)=7`, and `DeltaG=-7`; this is the decisive centroid-correction equality case.

## Stage C construction results

| r | N_r | exact m=1 | frozen m=2,3 status |
|---:|---:|:---|:---|
| 2 | 19 | rho_1=infinity | rho_2,rho_3 >= 4 (completed exact lower bound through rho=3; larger support unresolved) |
| 3 | 37 | rho_1=infinity | rho_2,rho_3 >= 4 (completed exact lower bound through rho=3; larger support unresolved) |
| 4 | 61 | rho_1=infinity | rho_2,rho_3 >= 4 (completed exact lower bound through rho=3; larger support unresolved) |
| 5 | 91 | rho_1=infinity | rho_2,rho_3 >= 4 (completed exact lower bound through rho=3; larger support unresolved) |
| 6 | 127 | rho_1=13 | 4 <= rho_2,rho_3 <= 13 (completed exact lower bound through rho=3) |
| 8 | 217 | rho_1=3 (theorem) | rho_2=rho_3=3 (theorem) |
| 10 | 331 | rho_1=3 (theorem) | rho_2=rho_3=3 (theorem) |
| 12 | 469 | rho_1=3 (theorem) | rho_2=rho_3=3 (theorem) |
| 16 | 817 | rho_1=3 (theorem) | rho_2=rho_3=3 (theorem) |

For `r=2..6`, the one-cell search is globally exhaustive. It gives no strict one-cell relocation at `r=2,3,4,5`, hence `rho_1=infinity` there, and gives `rho_1(6)=13`. At `r=6` there are 24 minimum-support one-cell moves forming 2 `D6` classes; representatives have `(DeltaQsum,Q(DeltaS),DeltaG)=(1,133,-6)` and `(1,139,-12)`.

For `m=2,3` at `r=2..6`, no global cooperative search was attempted. The exact bounded layer `support diameter<=3` was completely enumerated and contains no negative-energy replacement. Accordingly the atlas reports only the completed lower bound `rho_m>=4`; at `r=6`, the known one-cell move also gives the upper bound `rho_m<=13`. No unresolved bounded search is called infinity.

For non-holdout radii `r>=7` through `r=64`, `rho_1=3` is filled directly from the frozen symbolic theorem; no brute-force regression is used.

## Strict holdout

The strict holdout `[7,9,11,13,17,24]` was instantiated only after the theorem/counterexample ledger and the pre-holdout construction atlas existed. No parameter or protocol changed.

| r | N_r | DeltaQsum | Q(DeltaS) | DeltaG | rho_1=rho_2=rho_3 |
|---:|---:|---:|---:|---:|:---:|
| 7 | 169 | 0 | 7 | -7 | 3 |
| 9 | 271 | -2 | 7 | -549 | 3 |
| 11 | 397 | -4 | 7 | -1595 | 3 |
| 13 | 547 | -6 | 7 | -3289 | 3 |
| 17 | 919 | -10 | 7 | -9197 | 3 |
| 24 | 1801 | -17 | 7 | -30624 | 3 |

Every holdout witness passed: support diameter exactly 3, connectedness, frozen hole-free test, full centroid/full-G recomputation, strict `DeltaG<0`, and the exact `rho<=2` exclusion. The single-pair support-2 minimum `DeltaQsum` is exactly 3 on every holdout; for `k<=3`, `DeltaG >= k(3N_r-4k)>0` closes the cooperative support-2 class.

## Interpretation

R056 does **not** show that nonlocal motion is necessary. It shows the opposite for this frozen model: a fixed finite locality radius already escapes the R055 shell family. The minimal established escape needs only one moved cell and support diameter 3. D2 remains a nonlocal reference and is not reinterpreted as local.

No plateau/uphill dynamics, stochastic dynamics, new `m`, new `rho` convention, circle/pi target, or post-holdout model repair was introduced.
