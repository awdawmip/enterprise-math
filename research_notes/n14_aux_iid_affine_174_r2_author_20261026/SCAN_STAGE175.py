#!/usr/bin/env python3
"""Exact Stage175 dual-ray first action-gap closure; DUAL ONLY, no primal claim."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json

N=14
P=(F(1,8),F(1,24),F(5,6))
K0=L0=F(16044588,70019)
dK=dL=F(-1)
T=(8,2,0);Z=(14,0,0)
A=('P','Q','C')
fmt=lambda x:str(x.numerator)+('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return(s[0]+1,s[1]+(i==0),s[2]+(i==1))

@lru_cache(None)
def pair(s):
    vals=[(K0*ell(s),dK*ell(s)),(L0,dL)]
    if s[0]<N:
        ch=[pair(child(s,i)) for i in range(3)]
        vals.append((1+sum((P[i]*ch[i][0] for i in range(3)),F(0)),
                     sum((P[i]*ch[i][1] for i in range(3)),F(0))))
    min0=min(v[0] for v in vals)
    winners=[a for a,v in zip(A,vals) if v[0]==min0]
    if s==T:sel='P'
    elif s==Z:sel='Q'
    else:sel=winners[0]
    assert sel in winners
    deriv=min(vals[A.index(a)][1] for a in winners)
    assert vals[A.index(sel)][1]==deriv,(s,winners,sel,vals)
    return(*vals[A.index(sel)],dict(zip(A,vals)),sel,tuple(winners))

steps=[];zero=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b);v,d,opts,sel,w=pair(s)
            for ac,(v2,d2) in opts.items():
                if ac==sel:continue
                gap=v2-v;dg=d2-d
                assert gap>=0
                if gap==0:
                    zero.append((s,ac,dg))
                    assert dg>=0
                elif dg<0:steps.append((-gap/dg,s,ac,gap,dg))
assert steps
steps.sort()
minimum=steps[0][0]
close=[(s,ac,g,d) for t,s,ac,g,d in steps if t==minimum]
K=K0+dK*minimum;L=L0+dL*minimum

@lru_cache(None)
def bell(s):
    opts=[K*ell(s),L]
    if s[0]<N:opts.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
    m=min(opts)
    return m,tuple(a for a,v in zip(A,opts) if v==m),opts

ties={};positive=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b);v,w,opts=bell(s)
            if len(w)>1:ties[str(s)]=list(w)
            positive.extend(x-v for x in opts if x>v)
assert ties=={"(6, 3, 3)":['Q','C'],"(14, 0, 0)":['P','Q']}
assert minimum==F(4258982656225980,1535633560488809)
assert K==L==F(4964732675352,21931669411)
assert len(positive)==1238
assert min(positive)==F(39435024594685,2728650581438976)
H=bell((0,0,0))[0]
assert H==F(12727571546676169210383728225,75089267507105089342930944)
print('STAGE175_DUAL_ONLY_FIRST_GAP_PASS')
print('first_step',fmt(minimum),'K',fmt(K),'L',fmt(L),'H',fmt(H))
print('zero_gaps',[(s,a,fmt(d)) for s,a,d in zero])
print('closures',[(s,a,fmt(g),fmt(d)) for s,a,g,d in close])
print('positive_gaps',len(positive),'min',fmt(min(positive)),'ties',ties)
cert={'status':'STAGE175_DUAL_ONLY_NOT_PRIMAL_PROVED',
      'parent':'STAGE174_AUTHOR_EXACT',
      'model':'EXTERNAL_N14_TERNARY_IID',
      'ray':{'K174':fmt(K0),'L174':fmt(L0),'dK':fmt(dK),'dL':fmt(dL)},
      'candidate':{'step':fmt(minimum),'K':fmt(K),'L':fmt(L),'H':fmt(H),
                   'ties':ties,'strict_gaps':len(positive),'min_strict_gap':fmt(min(positive)),
                   'negative_slope_candidates':len(steps),
                   'closures':[{'state':list(s),'action':a,'gap':fmt(g),'derivative':fmt(d)} for s,a,g,d in close]}}
Path(__file__).with_name('dual175.json').write_text(json.dumps(cert,indent=2)+'\n')
