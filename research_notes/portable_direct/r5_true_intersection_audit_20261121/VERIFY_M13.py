#!/usr/bin/env python3
"""Independent exact certificates for the R5 primitive-16 m=13 counterexample."""
from collections import defaultdict
import json

ZERO=(0,)*8
ONE=(1,)+(0,)*7
S=[set(range(214,219)), {214,216,217,218,219,220,221}, set(range(215,222))]
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def scale(x,a):return tuple(a*v for v in x)
def mon(k):
    k%=16
    return tuple(1 if k==i else (-1 if k==i+8 else 0) for i in range(8))
def mul(x,y):
    c=[0]*16
    for i,a in enumerate(x):
        for j,b in enumerate(y):c[(i+j)%16]+=a*b
    return tuple(c[i]-c[i+8] for i in range(8))
def weight(P):
    w=ONE
    for p in sorted(P):w=mul(w,add(ONE,scale(mon(p),-1)))
    return w

def event_state_dp(m):
    out=ZERO
    for mask in range(1,8):
        selected=[S[j] for j in range(3) if mask>>j&1]
        U=sorted(set.union(*selected))
        state={(tuple([0]*len(selected)),0):1}
        for p in U:
            flags=[int(p in T) for T in selected]
            new=defaultdict(int)
            for (loads,phase),count in state.items():
                allowed=min(m-1-loads[j] for j,flag in enumerate(flags) if flag)
                for a in range(allowed+1):
                    new[(tuple(loads[j]+a*flags[j] for j in range(len(flags))),
                         (phase+p*a)%16)]+=count
            state=new
        h=[0]*16
        for (_,phase),count in state.items():h[phase]+=count
        coeff=tuple(h[j]-h[j+8] for j in range(8))
        out=add(out,scale(mul(weight(U),coeff),1 if len(selected)%2 else -1))
    return out

def by_total(P,M):
    h=[[0]*16 for _ in range(M)]
    h[0][0]=1
    for p in P:
        q=p%16
        for n in range(1,M):
            for k,v in enumerate(h[n-1]):h[n][(k+q)%16]+=v
    return h

def convolution(x,y):
    h=[0]*16
    for i,a in enumerate(x):
        for j,b in enumerate(y):h[(i+j)%16]+=a*b
    return h

def grouped_independent(m):
    out=ZERO
    for P in S:
        hh=by_total(sorted(P),m)
        v=tuple(sum(hh[n][j]-hh[n][j+8] for n in range(m)) for j in range(8))
        out=add(out,mul(weight(P),v))
    C=by_total([216,217,218],m)
    D=by_total([219,220,221],m)
    correction=[0]*16
    for c in range(m):
        for d in range(m):
            cd=convolution(C[c],D[d])
            for a in range(m):
                for b in range(m):
                    t=int(a+b+c<m)+int(a+c+d<m)+int(b+c+d<m)
                    if t<2:continue
                    shift=(214*a+215*b)%16
                    for k,v in enumerate(cd):correction[(k+shift)%16]-=(t-1)*v
    q=tuple(correction[j]-correction[j+8] for j in range(8))
    return add(out,mul(weight(range(214,222)),q))

if __name__=='__main__':
    expected={13:(60,36,4,-36,-60,-84,-84,-76),
              16:(-32,32,96,136,160,152,128,88)}
    results={}
    for m,known in expected.items():
        a=event_state_dp(m); b=grouped_independent(m)
        assert a==b==known,(m,a,b)
        assert a!=ZERO
        results[str(m)]={'state_DP':list(a),'grouped_convolution':list(b),'nonzero':True}
    assert 360360%16!=0
    print(json.dumps({'status':'PASS','field':'Z[z]/(z^8+1)',
       'methods':['per-mask multiconstraint state DP','grouped event-count convolution'],
       'certificates':results,'prior_m13_period':360360,
       'primitive_16_divides_actual_m13_minimum_period':True,
       'prior_m13_minimum_period_falsified':True,
       'review':'NOT_REVIEWED'},indent=2))
