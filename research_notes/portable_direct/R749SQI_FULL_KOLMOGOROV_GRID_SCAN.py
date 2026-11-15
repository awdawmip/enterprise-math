#!/usr/bin/env python3
"""Exact integer exhaustive Kolmogorov zero-atom maximizer scan, all r=1..3360.
Scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389; auxiliary Walsh only.
Depends on the sibling R749SQI_WALSH_CUBIC_SUBLEADING_CERT.py (stdlib).
"""
import runpy,io,json,contextlib
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    state=runpy.run_path(str(Path(__file__).with_name('R749SQI_WALSH_CUBIC_SUBLEADING_CERT.py')))
C=state['C']
MAX_R=len(C)
verified=0
support_edges_compared=0
largest_gap=0
for r in range(1,MAX_R+1):
    total=C[r-1]
    # At x=0 the discrete CDF jumps by mass K=0; continuous beta CDF is zero.
    atom_zero=total-(C[r-4] if r>3 else 0)
    target=atom_zero*(r**23)
    denominator=r**23
    for k in range((r-1)//3+1):
        t=r-3*k
        real_survival_times_total=total*(t**23)
        # CDF discrepancy immediately left/right of x=3k/r; at x=0,
        # left limit corresponds to x<0 and is trivially zero.
        left_C=C[t-1] if t>0 else 0
        right_C=C[t-4] if t>3 else 0
        lhs=abs(real_survival_times_total-left_C*denominator)
        rhs=abs(real_survival_times_total-right_C*denominator)
        if lhs>target or rhs>target:
            raise AssertionError({'r':r,'k':k,'lhs':lhs,'rhs':rhs,'threshold':target})
        support_edges_compared+=2
    verified+=1
    largest_gap=max(largest_gap,atom_zero)
assert verified==MAX_R and support_edges_compared>0
result={
  'schema':'R749SQI_FULL_KOLMOGOROV_GRID_SCAN_V1',
  'status':'PASS',
  'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
  'mode':'exhaustive integer Kolmogorov CDF endpoint scan',
  'domain':f'all integer r in 1..{MAX_R}',
  'integer_grid_sizes':verified,
  'cdf_boundary_comparisons':support_edges_compared,
  'assertion':'For every tested r, d_K(L(3K_r/r),Beta(1,23)) = P(K_r=0) = 1-C_(r-3)/C_r',
  'arithmetic':'pure Python integer exact comparisons; no float, Fraction not needed in final scan',
  'interpretation':'finite exact verification; does not prove all positive r'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
