# R123.3 — Multi-time mechanical lift and direct S23 signature cross-check

Date: 2026-11-13. Uses the R123.1 rational two-integer counting oracle without changing the original frozen scientific-input commit `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

For `m>=2`, mechanical lift words `q_i=floor(alpha+i*beta)`, `0<=alpha,beta<1`, arise from a finite rational arrangement of the lines `alpha+i*beta=h` (`1<=i<m`, `1<=h<=i`). The supplementary checker constructs line intersections exactly with `Fraction`, samples rational interiors and half-open boundaries, and obtains the known finite Sturmian vocabulary. The resulting joint word is coupled through **one common** rational `theta`, integers `n,k`, and the original S23 qualification inequalities, which are projected to R123.1's planar lattice feasibility problem.

The verifier in [check_r123_multi.py.gz.b64](check_r123_multi.py.gz.b64) (gzip/base64 of Python 3 source) compares the full set of `2^m` signature decisions against an independent direct rational critical-point enumeration, **including singleton crossing points**. In this implementation the original S23 special case remains `a=j=0,c=1`, `0<theta<1`; the time sequence is `t_i=N+i*d`, signed `N` and nonzero signed `d`.

Deterministic seed `12332026`, exact output `R123_MULTI_LIFT_PASS` in [verification_r123_multi.json.gz.b64](verification_r123_multi.json.gz.b64):

| m | Signed random instances | Complete signature queries | Reachable signatures | Lattice chunks |
|---:|---:|---:|---:|---:|
| 3 | 16 | 128 | 118 | 1,174 |
| 4 | 7 | 112 | 77 | 1,718 |

Also checks the mechanical-word counts for `m=2..8`: `2,4,8,14,24,36,54`, matching the published finite Sturmian count. Every returned rational witness was evaluated by the original qualification predicate. This is finite implementation validation; the exact general-m deduction depends on the stated R121/R122 mechanical-lift and R123.1 reduction proofs.

## Reproduce

In the directory with decoded `check_r123.py`, decode the added `check_r123_multi.py.gz.b64` via `base64 -d | gzip -d` and run `python3 check_r123_multi.py`. It prints exact JSON and writes `/mnt/data/em_r123/verification_r123_multi.json`; for execution outside this environment change that final output path. No external library is required.

## Next

R124: generate arbitrary directed half-open S23 arcs with all parameters `a,j,c` in the proof's affine segment representation, integrate the generic multi-time oracle, measure full costs and cross-check the six-affine critical-point cut enumerator. Preserve separation from native six-dimensional Cell/Link/Port licensing and from formal CLAIM/independent review.
