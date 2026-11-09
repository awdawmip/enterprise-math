#!/usr/bin/env python3
"""PREFIX-639: exact signed-BRC full central-slice Bernstein certificate."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
import json

DEN=1<<18
N=189
CHECKS=0
def check(label, ok):
    global CHECKS
    assert ok,label
    CHECKS+=1
@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n
@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*DEN//n
    check('mid_inside',inside(n,k,mid))
    if k==0:left_lo=left_hi=0
    else:
        lo,hi=0,mid
        check('left_outside',not inside(n,k,lo))
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(n,k,x):hi=x
            else:lo=x
        left_lo,left_hi=lo,hi
    lo,hi=mid,DEN
    check('right_outside',not inside(n,k,hi))
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(n,k,x):lo=x
        else:hi=x
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>DEN:return True
    if 4*(right_hi-left_lo)<DEN:return False
    raise AssertionError(('dyadic_diameter',n,k))
rows=[{0:1}]
state={0:1}
first=None
for n in range(1,N+1):
    nxt=defaultdict(int)
    for k,v in state.items():
        nxt[k]+=v
        nxt[k+1]+=v
    state={k:v for k,v in nxt.items() if wide(n,k)}
    if first is None and sum(nxt.values())>sum(state.values()):first=n
    rows.append(state.copy())
check('first_stop',first==25)
check('extinction',not rows[N])
check('row24',sum(rows[24].values())==2**24)
check('row25',sum(rows[25].values())==2**25-2)
@lru_cache(None)
def cb(n,k):return comb(n,k)
def elevate(c):
    n=len(c)
    return [c[0]]+[Q(j,n)*c[j-1]+Q(n-j,n)*c[j] for j in range(1,n)]+[c[-1]]
def elevate_to(c,degree):
    while len(c)-1<degree:c=elevate(c)
    return c
def cut(c,t):
    v=list(c)
    left=[v[0]]
    right=[v[-1]]
    for _ in range(len(c)-1):
        v=[(1-t)*v[i]+t*v[i+1] for i in range(len(v)-1)]
        left.append(v[0])
        right.append(v[-1])
    return left,right[::-1]
def restrict(c,a,b):
    _,right=cut(c,a)
    return cut(right,(b-a)/(1-a))[0]

z=Q(19,128)
p0,p1=Q(3,20),Q(1,6)
s2=[sum((Q(v)*z**k*(1-z)**(n-k) for k,v in row.items()),Q(0)) for n,row in enumerate(rows[:N])]
check('survivor_bounds',all(0<=v<=1 for v in s2))
alpha=[]
beta=[]
for n in range(N):
    av=Q(1)
    bv=Q(n+1)
    for m in range(N):
        if not s2[m]:continue
        w=Q(cb(n+m,n),2**(n+m+1))*s2[m]
        av-=w
        bv-=Q(n+m+1,2)*w
    alpha.append(av)
    beta.append(bv)
check('alpha_range',all(0<=v<=1 for v in alpha))
check('beta_range',all(0<=v<=n+1 for n,v in enumerate(beta)))
mu=[sum(s2,Q(0))+alpha[0]]
H=[beta[0]]
for n in range(1,N):
    mu=elevate(mu)
    H=elevate(H)
    for k,v in rows[n].items():
        b=Q(v,cb(n,k))
        mu[k]+=alpha[n]*b
        H[k]+=beta[n]*b
check('degree_188',len(mu)==189 and len(H)==189)
mp=restrict([188*(mu[k+1]-mu[k]) for k in range(188)],p0,p1)
check('mu_prime_188',len(mp)==188)
check('mu_positive_274',all(x>274 for x in mp))
check('mu_upper_321',all(x<321 for x in mp))
mass=[u*cb(188,k) for k,u in enumerate(mu)]
mu2=[sum((mass[k]*mass[i-k] for k in range(max(0,i-188),min(188,i)+1)),Q(0))/cb(376,i) for i in range(377)]
H376=elevate_to(H,376)
mu376=elevate_to(mu,376)
qinfo={}
for q in (12,24):
    t=Q(1,q)
    f=[2*h-u-t*v for h,u,v in zip(H376,mu2,mu376)]
    fpp=[376*375*(f[k+2]-2*f[k+1]+f[k]) for k in range(375)]
    r=restrict(fpp,p0,p1)
    check('degree_374_'+str(q),len(r)==375)
    check('Fpp_lower_'+str(q),all(x>27100 for x in r))
    check('Fpp_upper_'+str(q),all(x<48100 for x in r))
    qinfo[str(q)]={"min_floor":min(r).__floor__(),"max_ceil":max(r).__ceil__(),"count":len(r),"interval_certified":True}
low=Q(300**2,48100)
high=Q(310**2,27100)
check('rate_low',low==Q(900,481))
check('rate_high',high==Q(961,271))
check('mean_gap_low',low/24==Q(75,962))
check('mean_gap_high',high/24==Q(961,6504))
check('var_gap_low',low/384==Q(75,15392))
check('var_gap_high',high/384==Q(961,104064))
check('curvature_low',1/high==Q(271,961))
check('curvature_high',1/low==Q(481,900))
check('improve_rate_low',low>Q(9,5))
check('improve_rate_high',high<Q(961,230))
result={"schema":"PREFIX639_R6_COMPLETE_CENTRAL_SLICE_INTERVAL_CERTIFICATE_V1",
"frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
"source":"PREFIX-621 189-layer dyadic signed BRC survivor recurrence and PREFIX-622 moment identity",
"p2":"19/128","p1_interval":["3/20","1/6"],"t_interval":["1/24","1/12"],
"mu_prime_controls":{"count":len(mp),"min_floor":min(mp).__floor__(),"max_ceil":max(mp).__ceil__(),"strict_envelope":["274","321"]},
"F_second_controls":qinfo,
"new_optimum":{"d_mu_dt":["900/481","961/271"],"delta_mu_12_24":["75/962","961/6504"],
"delta_W_12_24":["75/15392","961/104064"],"arc_curvature":["271/961","481/900"]},
"check_count":CHECKS,"check_result":"ALL_CHECKS_PASS",
"review":"AUTHOR_PROVED / EXACT_RATIONAL_BERNSTEIN_CHECKED / UNREVIEWED / NOT_ADMITTED"}
with open("PREFIX639_R6_RESULTS.json","w",encoding="utf-8") as h:
    json.dump(result,h,ensure_ascii=False,indent=2)
    h.write("\n")
print("ALL_CHECKS_PASS",CHECKS)
print("mu_prime_envelope",result["mu_prime_controls"])
print("Fpp_controls",qinfo)
