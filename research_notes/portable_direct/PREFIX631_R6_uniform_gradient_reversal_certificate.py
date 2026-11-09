#!/usr/bin/env python3
"""PREFIX631: exact Bernstein certificate, uniform signed-BRC variance valley.
Science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Python standard library; first-passage recurrence from PREFIX621.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

DEN=1<<18
N=189
D=N-1
@lru_cache(None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(DEN-a)**(m-k)>DEN**m
@lru_cache(None)
def wide(m,k):
    if k>m//2:return wide(m,m-k)
    mid=k*DEN//m
    assert inside(m,k,mid)
    if k==0:ll=lh=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(m,k,x):hi=x
            else:lo=x
        ll,lh=lo,hi
    lo,hi=mid,DEN
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(m,k,x):lo=x
        else:hi=x
    rl,rh=lo,hi
    if 4*(rl-lh)>DEN:return True
    if 4*(rh-ll)<DEN:return False
    raise AssertionError(('dyadic ambiguity',m,k))

rows=[{0:1}]
state={0:1}
first=None
for m in range(1,N+1):
    next_state=defaultdict(int)
    for k,v in state.items():next_state[k]+=v;next_state[k+1]+=v
    state={k:v for k,v in next_state.items() if wide(m,k)}
    if first is None and sum(next_state.values())>sum(state.values()):first=m
    rows.append(state.copy())
assert first==25 and not rows[N] and sum(rows[25].values())==2**25-2

def s_and_d(p):
    a,b=p.numerator,p.denominator
    s=[];d=[]
    for n,row in enumerate(rows[:N]):
        v=sum(z*a**k*(b-a)**(n-k) for k,z in row.items())
        dv=sum(z*a**k*(b-a)**(n-k)*(b*k-n*a) for k,z in row.items())
        s.append(F(v,b**n))
        d.append(F(dv,a*(b-a)*b**(n-1)) if n else F(0))
    return s,d

# Degree-n s_n(p) in the exact power basis; s_n(p)=sum_j c[n][j]*p**j.
coeff=[]
for n,row in enumerate(rows[:N]):
    c=[0]*(n+1)
    for k,v in row.items():
        for j in range(k,n+1):c[j]+=(-1 if (j-k)%2 else 1)*v*comb(n-k,j-k)
    coeff.append(c)

lo=F(37,256)
hi=F(39,256)
def bernstein_on_interval(c):
    # Power-coefficient substitution p=lo+(hi-lo)*x; elevate to degree D.
    al=[lo**j for j in range(D+1)]
    dl=[(hi-lo)**j for j in range(D+1)]
    t=[dl[j]*sum((c[i]*comb(i,j)*al[i-j] for i in range(j,D+1)),F(0))
       for j in range(D+1)]
    return [sum((t[j]*F(comb(k,j),comb(D,j)) for j in range(k+1)),F(0))
            for k in range(D+1)]

def moments_bernstein(p1):
    s,d=s_and_d(p1)
    # mu=sum s + sum gamma[m]*s_m(p2); U=d_1mu; J=d_1H.
    gam=[];delta=[];eps=[]
    for m in range(N):
        gam.append(1-sum((F(comb(n+m,n),2**(n+m+1))*s[n] for n in range(N) if s[n]),F(0)))
        delta.append(-sum((F(comb(n+m,n),2**(n+m+1))*d[n] for n in range(N) if d[n]),F(0)))
        eps.append(-sum((F((n+m+1)*comb(n+m,n),2**(n+m+2))*d[n] for n in range(N) if d[n]),F(0)))
    result=[]
    for constant,weights in ((sum(s,F(0)),gam),(sum(d,F(0)),delta),
                             (sum(((n+1)*x for n,x in enumerate(d)),F(0)),eps)):
        power=[sum((weights[n]*coeff[n][j] for n in range(j,N)),F(0))
               for j in range(N)]
        power[0]+=constant
        result.append(bernstein_on_interval(power))
    return result

def elevate_or_product(a,b=None):
    # Degree D -> 2D, or product of two degree-D Bernstein polynomials.
    out=[]
    for k in range(2*D+1):
        numerator=sum((a[i]*(b[k-i] if b is not None else 1)*comb(D,i)*comb(D,k-i)
                   for i in range(max(0,k-D),min(D,k)+1)),F(0))
        out.append(numerator/comb(2*D,k))
    return out

results=[]
for p1,sign in ((F(3,20),-1),(F(1,6),1)):
    bm,bu,bj=moments_bernstein(p1)
    bW=[2*(x-y) for x,y in zip(elevate_or_product(bj),elevate_or_product(bm,bu))]
    bU=elevate_or_product(bu)
    bV12=[w-u/12 for w,u in zip(bW,bU)] # V'_q /q² at q=12
    assert len(bW)==377 and min(bU)>0
    assert (max(bW)<0 and max(bV12)<0) if sign<0 else (min(bW)>0 and min(bV12)>0)
    # A first/last Bernstein coefficient is the corresponding endpoint value.
    s,d=s_and_d(p1)
    for idx,p2 in ((0,lo),(-1,hi)):
        s2,_=s_and_d(p2)
        alpha=[1-sum((F(comb(n+m,n),2**(n+m+1))*s2[m] for m in range(N) if s2[m]),F(0)) for n in range(N)]
        beta=[(n+1)-sum((F((n+m+1)*comb(n+m,n),2**(n+m+2))*s2[m] for m in range(N) if s2[m]),F(0)) for n in range(N)]
        mu=sum(s2,F(0))+sum((x*y for x,y in zip(s,alpha)),F(0))
        U=sum((x*y for x,y in zip(d,alpha)),F(0))
        J=sum((x*y for x,y in zip(d,beta)),F(0))
        assert (bm[idx],bu[idx],bj[idx])==(mu,U,J)
        assert bW[idx]==2*(J-mu*U)
    results.append({'p1':str(p1),'sign':'NEGATIVE' if sign<0 else 'POSITIVE',
        'bernstein_coefficients_verified':377,
        'min_dV_q12_over_q2_display':str(round(float(min(bV12)),8)),
        'max_dV_q12_over_q2_display':str(round(float(max(bV12)),8)),
        'exact_inequality':'all 377 rational Bernstein coefficients have the certified sign'})

out={'schema':'PREFIX631_R6_UNIFORM_GRADIENT_VALLEY_V1','pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'parameter_scope':'p2 in [37/256,39/256]; q real >=12; p1 at 3/20 or 1/6',
'theorem':'For every p2 in bracket and every q>=12, dV/dp1<0 at p1=3/20 and >0 at p1=1/6; each slice has at least one interior local minimum in (3/20,1/6).',
'proof':'Exact degree-376 Bernstein coefficients of q-normalized derivative; positivity of basis; compactness and endpoint derivatives.',
'results':results,'verification':'ALL_CHECKS_PASS','status':'AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX631_R6_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL_CHECKS_PASS',[(x['p1'],x['sign']) for x in results])
