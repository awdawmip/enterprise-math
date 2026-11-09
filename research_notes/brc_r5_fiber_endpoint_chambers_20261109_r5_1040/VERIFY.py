#!/usr/bin/env python3
"""Exact 11-chamber endpoint classification in the R5 g=b FULL_HIST flow face.
Self-contained proof audit; every fraction is exact. The absence of the 12th
chamber is established separately by a symbolic rational inequality in RESEARCH.md.
"""
from fractions import Fraction as F
K=tuple(map(F,'-49400/295513 -49400/295513 -49400/295513 -33345/591026 132145/295513 -33345/591026 1'.split()))

def slack(f):
    g,a,b,u,v,w,z=f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

D=tuple(a-b for a,b in zip(slack(K),slack((F(0),)*7)))
assert D==(F(-49400,295513),F(0),F(49400,295513),F(-49400,295513),F(0),
          F(-33345,591026),F(0),F(-33345,591026),F(0),F(1),
          F(-300453,295513),F(-163368,295513),F(152253,295513))
LOW=(2,9,12)
UP=(5,7,10,11)
WITNESSES={
  (2,5):(1992,1985,8,132,664,53),
  (2,7):(1992,1985,662,132,8,53),
  (2,10):(1976,1951,634,197,640,171),
  (2,11):(1980,1960,642,159,647,139),
  (9,5):(1990,1980,10,112,661,10),
  (9,7):(1990,1980,659,112,10,10),
  (9,10):(1909,1818,524,191,547,91),
  (9,11):(1951,1901,593,99,605,49),
  (12,5):(1991,1982,9,465,662,27),
  (12,7):(1991,1982,660,465,9,27),
  (12,10):(1952,1903,595,533,607,142),
}
assert len(WITNESSES)==11
assert F(9,40)-F(152253,2955130)>F(163368,3004530)
for (li,ui),v in WITNESSES.items():
    g,a,u,vv,w,z=[F(c,2000) for c in v]
    f=(g,a,g,u,vv,w,z)
    S=slack(f)
    assert S[4]==0 and all(S[i]>0 for i in range(13) if i!=4)
    lo={i:-S[i]/D[i] for i in LOW}
    hi={i:-S[i]/D[i] for i in UP}
    assert lo[li]>max(lo[j] for j in LOW if j!=li),(li,ui,'lower')
    assert hi[ui]<min(hi[j] for j in UP if j!=ui),(li,ui,'upper')
    assert hi[ui] < min(-S[j]/D[j] for j in (0,3)),(li,ui,'domination')
    assert lo[li]<0<hi[ui]
    def add(f,t): return tuple(a+t*b for a,b in zip(f,K))
    for t in (lo[li],hi[ui]):
        assert all(ss>=0 for ss in slack(add(f,t)))
    h=(lo[li]+hi[ui])/3
    sh=slack(add(f,h))
    loh=max(-sh[j]/D[j] for j in LOW)
    hih=min(-sh[j]/D[j] for j in UP)
    assert loh==lo[li]-h and hih==hi[ui]-h
    assert add(add(f,h),loh)==add(f,lo[li])
    assert add(add(f,h),hih)==add(f,hi[ui])
    print('PASS_CHAMBER',li,ui,'witness_scaled_2000',v)
print('PASS_ALL_11_STRICT_RATIONAL_WITNESSES')
print('PASS_FORBIDDEN_PAIR_INEQUALITY',F(9,40)-F(152253,2955130),F(163368,3004530))
print('THEOREM_R5_g_eq_b_FIBER_ENDPOINTS_11_FULL_DIMENSIONAL_CHAMBERS')
