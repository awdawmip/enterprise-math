# R123 local end-to-end scaling experiment

Date: 2026-11-13. Exact S23 special case `m=2,a=j=0,c=1` with `x=3/11`, `J=(1/8,7/8)`, `N=3d+7`, positive `d`. The *entire* four-signature evaluation (`00,01,10,11`), including rational projection, active-envelope intersections, exact signed floor sums, integer witness recovery and exact qualification assertions, was timed three times per input using Python `time.perf_counter`, reporting the median. No baseline fiber solver was timed, and clock timings are illustrative process-local measurements only.

| d | Approx. k-band count | 2D chunk evaluations (all signatures) | Median seconds |
|---:|---:|---:|---:|
| 2 | 1.5 | 16 | 0.004786 |
| 100 | 75 | 72 | 0.007740 |
| 10,000 | 7,500 | 68 | 0.008070 |
| 10^10 | 7.5×10^9 | 68 | 0.009689 |
| 10^30 | 7.5×10^29 | 68 | 0.015675 |
| 10^100 | 7.5×10^99 | 68 | 0.023849 |

All four joint signatures were reachable for all six instances, with rational witnesses verified by the original S23 predicate. Chunk counts correspond to the actual generated 2D polyhedron arrangement; they are bounded by the constraint-line intersection complexity rather than the numerical k-band count. Input bit length and rational arithmetic still affect runtime.

The exact experiment driver is:

```python
from check_r123 import solve_signatures
from fractions import Fraction as F
from time import perf_counter
from statistics import median
for d in [2,10**2,10**4,10**10,10**30,10**100]:
    N=3*d+7
    times=[]
    for _ in range(3):
        start=perf_counter()
        out=solve_signatures(F(3,11),N,d,F(1,8),F(7,8))
        times.append(perf_counter()-start)
    print(d,sum(v['chunks'] for v in out.values()),median(times))
```

This experiment supplements the exact R123 proof and the deterministic verification data at the same branch. Broader benchmarking should include the per-k R122 solver, preprocessing, memory allocation and uncertainty from machine conditions.
