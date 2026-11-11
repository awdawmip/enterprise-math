#!/usr/bin/env python3
"""PREFIX-700-R6 exact corner witness for the frozen 189-row BRC observer.
Science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
This is finite auxiliary-observer arithmetic, not a native BRC state update.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

D=2**18
N=189

@lru_cache(None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(D-a)**(m-k)>D**m

@lru_cache(None)
def wide(m,k):
    if k>m//2: return wide(m,m-k)
    mid=k*D//m
    assert inside(m,k,mid)
    if k==0: left_lo=left_hi=0
    else:
        lo,hi=0,mid
        assert not inside(m,k,lo)
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(m,k,x): hi=x
            else:lo=x
        left_lo,left_hi=lo,hi
    lo,hi=mid,D
    assert not inside(m,k,hi)
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(m,k,x):lo=x
        else:hi=x
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>D:return True
    if 4*(right_hi-left_lo)<D:return False
    raise AssertionError(("uncertified width",m,k))

rows=[{0:1}]
for m in range(1,N+1):
    nxt=defaultdict(int)
    for k,v in rows[-1].items():
        nxt[k]+=v
        nxt[k+1]+=v
    rows.append({k:v for k,v in nxt.items() if wide(m,k)})
assert len(rows)==190 and not rows[189]
assert sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}
for m in range(N):
    assert all(rows[m].get(k,0)==rows[m].get(m-k,0) for k in rows[m])

@lru_cache(None)
def survive(p):
    a,b=p.numerator,p.denominator
    return tuple(F(sum(v*a**k*(b-a)**(n-k) for k,v in row.items()),b**n)
                 for n,row in enumerate(rows[:N]))

@lru_cache(None)
def moments(p,z):
    s,t=survive(p),survive(z)
    mu=sum(s,F(0))+sum(t,F(0))
    H=sum(((n+1)*(s[n]+t[n]) for n in range(N)),F(0))
    for n,sn in enumerate(s):
        if not sn:continue
        for m,tm in enumerate(t):
            if not tm:continue
            cross=sn*tm*F(comb(n+m,n),2**(n+m+1))
            mu-=cross
            H-=F(n+m+1,2)*cross
    return mu,2*H-mu**2

e=(F(0),F(1,8))
cases={"zero_zero":(F(0),F(0)),"zero_half":(F(0),F(1,2)),
       "half_half":(F(1,2),F(1,2))}
me,we=moments(*e)
checks=[]
for name,corner in cases.items():
    mc,wc=moments(*corner)
    dm,dw=me-mc,we-wc
    assert dw>0 and 2*dw-dm>0
    if name=="zero_zero":
        assert dm>0 and 10*dm<dw
    else:
        assert dm<0
    ticks={}
    for key,val in [("delta_mu",dm),("delta_W",dw),
                    ("q2_margin_over_q",2*dw-dm)]:
        lower=(val*10**6).__floor__()
        assert F(lower,10**6)<=val<F(lower+1,10**6)
        ticks[key]=[lower,lower+1]
    checks.append({"corner":name,"strict_sign_check":"PASS",
                   "decimal_1e6_ticks":ticks})
record={"schema":"PREFIX700_R6_STRICT_ALL_REAL_Q_OPTIMIZER_ORDER_V1",
        "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "surviving_cells":sum(map(len,rows[:N])),
        "witness":"(0,1/8)",
        "corner_exact_sign_checks":checks,
        "endpoint":"q=2", "extension":"all real q>=2",
        "strict_optimal_pair_order":
          "For 2<=q1<q2, every global optimizer pair has strictly increasing mu and W.",
        "analytic_dependencies":["PREFIX625 Theorem A","PREFIX625 Theorem B"],
        "verification":"ALL_CHECKS_PASS PREFIX700-R6",
        "admission":"AUTHOR_RECOMPUTED; UNREVIEWED; NOT_ADMITTED"}
out=Path(__file__).with_name("PREFIX700_R6_RESULTS.json")
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("ALL_CHECKS_PASS PREFIX700-R6")
for r in checks:print(r["corner"],r["decimal_1e6_ticks"])
