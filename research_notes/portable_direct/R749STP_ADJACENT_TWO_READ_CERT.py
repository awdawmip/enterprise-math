#!/usr/bin/env python3
"""Exact Fraction certificate for R749STP; no floating-point arithmetic."""
from fractions import Fraction as F
import json
from pathlib import Path

W = (1, 1, 2, 3, 6)
N = 271
part = [0]*(N+1)
part[0] = 1
for w in W:
    for k in range(w,N+1):
        part[k] += part[k-w]
C = [0]*(N+1)
T = [0]*(N+1)
for n in range(1,N+1):
    C[n] = C[n-1]+part[n-1]
    T[n] = T[n-1]+C[n-1]

def s(n):
    return 18*n**4+54*n**3-345*n**2+2070*n-16315

def y(n,e,d):
    return F(n**3*(T[n]+e),C[n]+d)-F(s(n),108)

def diff6(n,e,d):
    return y(n,e,d)-y(n+6,e,d)

def signs(n):
    t=n+6
    assert C[n]>2 and C[t]>2 and T[n]>2 and T[t]>2
    # Bound d/d e [Y_n-Y_{n+6}] below for every d in [-2,2]
    re=F(n**3,C[n]+2)-F(t**3,C[t]-2)
    # Bound -d/d d [Y_n-Y_{n+6}] below for every e,d in [-2,2]
    rd=F(n**3*(T[n]-2),(C[n]+2)**2)-F(t**3*(T[t]+2),(C[t]-2)**2)
    assert re>0 and rd>0
    return re,rd

assert (C[73],T[73],C[79],T[79])==(707343,8931013,1020943,13914446)
assert (C[265],T[265],C[271],T[271])==(338147679,15099942957,377285215,17225006406)
assert all(signs(n)[k]>0 for n in (73,265) for k in (0,1))
# With H=F_0-F_1 = D_73(e,d)-D_265(E,D), monotonicity
# makes this its exact global minimum over the full real parameter cube.
delta=diff6(73,-2,2)-diff6(265,2,-2)
assert delta==F(980722950443484973593733668,6142123829965035791412569735)
assert delta>0
# One read is insufficient: the range of F_0 straddles zero,
# and F_0 is continuous on the connected nuisance box.
lo=y(73,-2,2)-y(265,2,-2)
hi=y(73,2,-2)-y(265,-2,2)
assert lo<0<hi

out = {
  'unit':'R749STP','frozen_science_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
  'evidence':'AUTHOR_EXACT_NOT_REVIEWED',
  'weights':list(W),'comparison':[73,265], 'read_indices':[0,1],
  'counts':{str(n):{'C':C[n],'T':T[n]} for n in (73,79,265,271)},
  'local_diff_derivative_lower_bounds':{
      str(n):{'positive_d_e':str(signs(n)[0]),'positive_minus_d_d':str(signs(n)[1])}
      for n in (73,265)},
  'exact_min_F0_minus_F1':str(delta),
  'exact_strict_noise_per_raw_read':'eta < '+str(delta/4),
  'one_read_F0_extremes':[str(lo),str(hi)],
  'conclusion':'Minimal number of successive initial exact reads distinguishing q=73 from p=265 is exactly two.',
  'scope':'Fixed nuisance pair per candidate across both reads; four nuisance parameters range independently over the full real square [-2,2]^2 each. Auxiliary scalar observer only.',
  'next':'Determine general exact adjacent two-read separators by phase/gap; prove source-preserving typed BRC readout correspondence.'
}
path=Path(__file__).with_name('R749STP_ADJACENT_TWO_READ_RESULTS.json')
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: C,T counts; 4 global derivative bounds; exact positive H minimum; first-read collision; noise threshold')
print('delta=',delta,'noise_eta<',delta/4)
