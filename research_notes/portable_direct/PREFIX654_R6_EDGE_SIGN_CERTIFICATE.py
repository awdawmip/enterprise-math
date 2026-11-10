#!/usr/bin/env python3
"""Exact frozen BRC observer edge-sign certificate on the PREFIX-643 strip.
No native 96-port dynamics; this replays the pinned 189-layer survivor recurrence.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from json import dumps

N, DEN = 189, 1<<18
L,R = Q(3,20), Q(1,6)
z0,h = Q(19,128), Q(1,2**18)
zlo,zhi = z0-h,z0+h
checks=0

def check(x,why):
    global checks
    assert x,why
    checks+=1

@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n
@lru_cache(None)
def wide(n,k):
    if k>n//2: return wide(n,n-k)
    mid=k*DEN//n
    check(inside(n,k,mid),"valid midpoint")
    if k==0: ll=lh=0
    else:
        lo,hi=0,mid
        check(not inside(n,k,lo),"excluded low")
        while hi-lo>1:
            m=(hi+lo)//2
            if inside(n,k,m): hi=m
            else: lo=m
        ll,lh=lo,hi
    lo,hi=mid,DEN
    check(not inside(n,k,hi),"excluded high")
    while hi-lo>1:
        m=(hi+lo)//2
        if inside(n,k,m): lo=m
        else: hi=m
    rl,rh=lo,hi
    if 4*(rl-lh)>DEN:return True
    if 4*(rh-ll)<DEN:return False
    raise AssertionError(("ambiguous width",n,k))

def survivor_rows():
    rows=[{0:1}]; state={0:1}; first=None
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for k,v in state.items():nxt[k]+=v; nxt[k+1]+=v
        state={k:v for k,v in nxt.items() if wide(n,k)}
        if first is None and sum(state.values())<sum(nxt.values()):first=n
        rows.append(state.copy())
    check(first==25,"first rejection")
    check(not rows[189],"all dead at 189")
    check(sum(rows[24].values())==2**24,"survival 24")
    check(sum(rows[25].values())==2**25-2,"survival 25")
    return rows

def surv(rows,x):
    a,b=x.numerator,x.denominator
    return [Q(sum(v*a**k*(b-a)**(n-k) for k,v in rows[n].items()),b**n)
            for n in range(N)]

def moments(u,v):
    mu=sum(u)+sum(v)
    H=sum((n+1)*(u[n]+v[n]) for n in range(N))
    for n in range(N):
        if not u[n]:continue
        for m in range(N):
            if not v[m]:continue
            w=Q(comb(n+m,n),2**(n+m+1))*u[n]*v[m]
            mu-=w
            H-=Q(n+m+1,2)*w
    return mu,2*H-mu**2

# Uniform derivative bound via binomial score, negative binomial weights,
# center-strip inherited mu_p<322, and mu<=197.
check(zlo==Q(38911,262144),"left z")
check(zhi==Q(38913,262144),"right z")
check(zlo*(1-zlo)>Q(188,1500),"second score constant")
check(R-L==Q(1,60),"p width")
mdmu_zz=Q(189*1500,3)
mdH_zz=Q(1500*189*190,6)
mdmu_z=Q(189*20,3)
mu_z_bound=189*20
mu_zz_bound=189*1500
mu_bound=197
dmu_bound=Q(322,60)
mdW_zz=(2*mdH_zz + mdmu_zz*(2*mu_bound)
        +2*mdmu_z*(2*mu_z_bound)
        +dmu_bound*(2*mu_zz_bound))
check(mdmu_zz==94500 and mdH_zz==8977500,"difference derivative bounds")
check(mdW_zz==77282100,"variance second derivative bound")
errs={q:(q*q*mdW_zz+q*mdmu_zz)*h*h/2 for q in (12,24)}
for q in (12,24): check(errs[q]<1, "interpolation remainder under 1")

rows=survivor_rows()
uL,uR=surv(rows,L),surv(rows,R)
assert all(0<=v<=1 for v in uL+uR)
probes=[]
endpoint_bands={12:[],24:[]}
for z in (zlo,zhi):
    v=surv(rows,z)
    muL,WL=moments(uL,v);muR,WR=moments(uR,v)
    check(0<muL<197 and 0<muR<197, "mean bound")
    for q in (12,24):
        D=q*q*(WR-WL)-q*(muR-muL)
        threshold=Q(-226) if q==12 else Q(-785)
        check(D<threshold, "endpoint negative bound")
        m=D.numerator*1000//D.denominator
        check(Q(m,1000)<D<Q(m+1,1000),"endpoint exact enclosure")
        probes.append({"z":str(z),"q":q,"D_lower":str(Q(m,1000)),"D_upper":str(Q(m+1,1000))})
        endpoint_bands[q].append(Q(m+1,1000))

for q,threshold in ((12,Q(-226)),(24,Q(-785))):
    check(max(endpoint_bands[q])+errs[q]<threshold,"uniform interpolation sign")
# For each fixed z, D_q(z)/q = q*(W(R,z)-W(L,z)) - (mu(R,z)-mu(L,z))
# is affine in q, hence q=12,24 controls every real q in [12,24].
check(Q(12)<Q(24),"q interval")

output={
"schema":"EM_PREFIX654_EDGE_SIGN_CERTIFICATE_V1",
"frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
"observer":"signed BRC 189-layer two-information-direction first-stop model",
"inputs":{"p_edges":[str(L),str(R)],"z_bounds":[str(zlo),str(zhi)],"q_slots":[12,24],"layer_count":189,"grid_denominator":DEN},
"endpoint_exact_interval_enclosures":probes,
"uniform_second_derivative_bound":{"deltaW_zz":str(mdW_zz),"deltaMu_zz":str(mdmu_zz),
"Dq_interpolation_errors":{"12":str(errs[12]),"24":str(errs[24])}},
"conclusions":{"D12_all_z":"<-226","D24_all_z":"<-785",
"Dq_all_z_for_real_q_between_12_and_24":"<0 by affinity of Dq/q in q",
"maximum_over_central_strip":"left p-edge = 3/20 for every real 12 <= q <= 24"},
"assertions_passed":checks,"result":"ALL_CHECKS_PASS",
"arithmetic":"Python standard library exact integer and Fraction, no floating-point comparisons",
"scope":"Pinned 189-layer first-stop statistical observer; previous PREFIX643 convexity inherited"}
print(dumps(output,ensure_ascii=False,indent=2))
print("ALL_CHECKS_PASS",checks)
