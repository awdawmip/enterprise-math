#!/usr/bin/env python3
"""Exact author verifier for the external N=14 ternary iid auxiliary model, Stage151."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from pathlib import Path

N=14
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(45154992,127757); L=F(6412152,18251)
B=(11,0,1); U=(9,4,1)
ALPHA150=F(18372793163552518325,52808422392537808896)
V150=F(318819628004877985013,26404211196268904448)

@lru_cache(None)
def h(s):
    n,a,b=s
    opts={'P': K * F(2**(a+b),3**a), 'Q': L}
    if n < N:
        opts['C'] = F(1)+sum(P[i]*h((n+1,a+(i==0),b+(i==1))) for i in range(3))
    opt=min(opts.values()); chosen=tuple(k for k,v in opts.items() if v==opt)
    return opt

@lru_cache(None)
def actions(s):
    n,a,b=s
    o={'P':K*F(2**(a+b),3**a), 'Q':L}
    if n<N: o['C']=F(1)+sum(P[i]*h((n+1,a+(i==0),b+(i==1))) for i in range(3))
    mn=min(o.values()); tied=tuple(t for t,c in o.items() if c==mn)
    return o,tied

STATES=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
ties=[(s,actions(s)[1]) for s in STATES if len(actions(s)[1])>1]
gaps=[c-min(options.values()) for s in STATES for options,_ in [actions(s)] for a,c in options.items() if c>min(options.values())]
assert len(STATES)==680
assert set(s for s,_ in ties)=={B,U},ties
assert actions(B)[1]==('Q','C') and actions(U)[1]==('P','C'),ties
assert len(gaps)==1238 and all(z>0 for z in gaps)
assert h((0,0,0))==F(3601141501561668677150701,13997190082164839940096)

zero=(F(0),)*4

def add(*terms): return tuple(sum(x[i] for x in terms) for i in range(4))
def mul(p,q,x): return (p*x[0],q*x[1],p*x[2],q*x[3])

def obs(b,u):
    @lru_cache(None)
    def f(s):
        if s==B:
            stop=b
            # Q stop + C
            if b==1:return (F(1),F(0),F(0),F(0))
        elif s==U:
            stop=u
            if u==1:return (F(0),F(1),F(0),F(0))
        else: stop=None
        o,t=actions(s)
        choice=t[0] if len(t)==1 else 'C'
        if choice=='P':return (F(0),F(1),F(0),F(0))
        if choice=='Q':return (F(1),F(0),F(0),F(0))
        n,a,c=s
        z=add(*(mul(P[i],Q[i],f((n+1,a+(i==0),c+(i==1)))) for i in range(3)))
        z=(z[0],z[1],1+z[2],1+z[3])
        if s==B:return add(tuple(b*vv for vv in (F(1),F(0),F(0),F(0))),tuple((1-b)*vv for vv in z))
        if s==U:return add(tuple(u*vv for vv in (F(0),F(1),F(0),F(0))),tuple((1-u)*vv for vv in z))
        return z
    return f((0,0,0))

corners={(i,j):obs(F(i),F(j)) for i,j in product((0,1), repeat=2)}
m00=corners[0,0]; dB=tuple(corners[1,0][i]-m00[i] for i in range(4)); dU=tuple(corners[0,1][i]-m00[i] for i in range(4))
cross=tuple(corners[1,1][i]-corners[1,0][i]-corners[0,1][i]+m00[i] for i in range(4))
assert cross==zero

# Solve equal errors: M.eP-M.eQ= A + b*Bcoef + u*Ucoef = 0 -> b(u) = intercept + slope*u.
a0=(m00[1]-m00[0])/(dB[0]-dB[1]); a1=(dU[1]-dU[0])/(dB[0]-dB[1])
b0=a0;b1=a0+a1
alpha0=m00[0]+b0*dB[0]
alpha1=m00[0]+b1*dB[0]+dU[0]
eta=alpha1-alpha0
v0=m00[2]+b0*dB[2]
v1=m00[2]+b1*dB[2]+dU[2]
qtime0=m00[3]+b0*dB[3]
qtime1=m00[3]+b1*dB[3]+dU[3]
res={"K":K,"L":L,"H":h((0,0,0)),"ties":ties,"n_states":len(STATES),"positive_gaps":len(gaps),"min_gap":min(gaps),"M00":m00,"dB":dB,"dU":dU,"cross":cross,"b0":b0,"b1":b1,"b_slope":a1,"alpha0":alpha0,"alpha1":alpha1,"eta":eta,"V0":v0,"V1":v1,"tP_minus_tQ0":v0-qtime0,"tP_minus_tQ1":v1-qtime1,"slope":K+L,"duals_eq0":v0+(K+L)*alpha0-h((0,0,0)),"duals_eq1":v1+(K+L)*alpha1-h((0,0,0)),"alpha150":ALPHA150,"V150":V150,"ref_start":alpha0==ALPHA150 and v0==V150}

assert alpha0==ALPHA150 and v0==V150
assert 0<b0<b1<1 and eta>0 and v0>qtime0 and v1>qtime1
assert v0+(K+L)*alpha0==h((0,0,0))
assert v1+(K+L)*alpha1==h((0,0,0))

if __name__=='__main__':
  for k,v in res.items():
    if isinstance(v,(list,tuple)): print(k,':', [str(q) for q in v])
    else:print(k,':',v)
  with open(Path(__file__).resolve().parent / 'main_exact.json','w') as fp:json.dump({k: ([str(x) for x in v] if isinstance(v,tuple) and k!='ties' else str(v)) for k,v in res.items()},fp,indent=2)
