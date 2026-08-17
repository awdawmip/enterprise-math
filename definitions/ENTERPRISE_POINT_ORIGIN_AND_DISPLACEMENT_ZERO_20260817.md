# 进取点态原点与位移零元

Status: `ACTIVE / CANONICAL_FOUNDATIONAL_SEMANTIC`
Date: `2026-08-17`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

## Frozen decision

`ENTERPRISE_POINT_STATE_ORIGIN = 1`

`ENTERPRISE_DISPLACEMENT_ZERO = 0`

`rho = 1 + r`

where `rho>=1` is the native point-state level and `r>=0` is primitive displacement / step radius.

The center therefore has `rho=1` and `r=0` simultaneously. This is a semantic separation, not `0=1` and not a coordinate-wide shift.

All existing R059D displacement formulas remain zero-centered. In particular `(r,0)`, `(0,r)`, signed local coordinates, residuals and `R(a,b)=(-b,a+b)` keep the ordinary displacement zero `0`.

Ordinary algebra remains unchanged: additive identity `0`, multiplicative identity `1`.

For AG–AO, every existing radius variable `r` is retyped as `PRIMITIVE_DISPLACEMENT_RADIUS / STEP_RADIUS`. Native point-state level is `rho=r+1`. No accepted theorem is recomputed solely because of this semantic split.

Examples:

- center: `rho=1, r=0`;
- first outward layer: `rho=2, r=1`;
- `D(r)=2r+1` becomes `D(rho)=2rho-1` under point-state labeling;
- `V(0)=1` means zero displacement still contains one center existence-state.

Highest routing rule: every future use of “origin” must distinguish `POINT-STATE ORIGIN` from `DISPLACEMENT ZERO`.