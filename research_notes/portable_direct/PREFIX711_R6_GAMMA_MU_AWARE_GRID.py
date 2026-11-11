#!/usr/bin/env python3
"""PREFIX-711: exact mean-aware gamma-clock max interval certificate.
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import sys, json

N, WD = 189, 1 << 18
G = int(sys.argv[1]) if len(sys.argv) > 1 else 192

@lru_cache(None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(WD-a)**(m-k) > WD**m

@lru_cache(None)
def wide(m,k):
    if k > m//2:
        return wide(m,m-k)
    mid=k*WD//m
    assert inside(m,k,mid)
    if k==0:
        left_lo=left_hi=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            x=(lo+hi)//2
            if inside(m,k,x): hi=x
            else: lo=x
        left_lo,left_hi=lo,hi
    lo,hi=mid,WD
    while hi-lo>1:
        x=(lo+hi)//2
        if inside(m,k,x): lo=x
        else: hi=x
    right_lo,right_hi=lo,hi
    if 4*(right_lo-left_hi)>WD: return True
    if 4*(right_hi-left_lo)<WD: return False
    raise AssertionError(('width undecided',m,k))

rows=[{0:1}]
for m in range(1,N+1):
    new=defaultdict(int)
    for k,v in rows[-1].items():
        new[k]+=v
        new[k+1]+=v
    rows.append({k:v for k,v in new.items() if wide(m,k)})
assert rows[-1]=={} and sum(map(len,rows[:N]))==9529
assert rows[25]=={k:comb(25,k) for k in range(1,25)}

coeff=[[comb(n+m,n)*2**(2*N-2-n-m) for m in range(N)] for n in range(N)]
Z=2**(2*N-1)

def zero_clock_pair(znum,zden):
    zscale=zden**(N-1)
    pa=[1];pb=[1]
    for _ in range(N):
        pa.append(pa[-1]*znum)
        pb.append(pb[-1]*(zden-znum))
    tz=[sum(v*pa[k]*pb[n-k] for k,v in row.items())*zden**(N-1-n)
        for n,row in enumerate(rows[:N])]
    cross0=sum(tz[m]*sum(coeff[n][m] for n in range(25)) for m in range(N))
    cross1=sum(tz[m]*sum((n+m+1)*coeff[n][m] for n in range(25)) for m in range(N))
    den=zscale*Z
    mu_num=(25*zscale+sum(tz))*Z-cross0
    m2_num=2*(325*zscale+sum((m+1)*v for m,v in enumerate(tz)))*Z-cross1
    mu=F(mu_num,den)
    return mu,F(m2_num,den)-mu*mu

mu_e,W_e=zero_clock_pair(3,20)
assert F(559812917,10**6)<W_e-mu_e/2<F(559812918,10**6)

D=2*G
L=D**(N-1)
R=L*L*Z
T=[]
for i in range(G+1):
    a,b=i,D-i
    ap=[1];bp=[1]
    for _ in range(N):
        ap.append(ap[-1]*a)
        bp.append(bp[-1]*b)
    T.append([sum(v*ap[k]*bp[n-k] for k,v in row.items())*D**(N-1-n)
              for n,row in enumerate(rows[:N])])
A=[sum(t) for t in T]
B1=[sum((n+1)*v for n,v in enumerate(t)) for t in T]
K0=[];K1=[]
for tj in T:
    active=[(m,v) for m,v in enumerate(tj) if v]
    K0.append([sum(coeff[n][m]*v for m,v in active) for n in range(N)])
    K1.append([sum((n+m+1)*coeff[n][m]*v for m,v in active) for n in range(N)])

def gamma_pair(i,j):
    mu=(A[i]+A[j])*L*Z-sum(x*y for x,y in zip(T[i],K0[j]))
    m2=2*(B1[i]+B1[j])*L*Z-sum(x*y for x,y in zip(T[i],K1[j]))
    return mu,m2

mu00,m200=gamma_pair(0,0)
assert F(mu00,R)==F(3913470354001175,140737488355328)
assert F(m200*R-mu00**2,R**2)>19

M=[[None]*(G+1) for _ in range(G+1)]
S=[[None]*(G+1) for _ in range(G+1)]
for i in range(G+1):
    for j in range(i,G+1):
        mu,m2=gamma_pair(i,j)
        M[i][j]=M[j][i]=mu
        S[i][j]=S[j][i]=m2

Bq={q:W_e-mu_e/q for q in [2,12,24]}
factors={q:(b.numerator*q*R**2,b.denominator) for q,b in Bq.items()}
inf_factor=(W_e.numerator*R**2,W_e.denominator)
base_floor=F(559812917,1000000)
base_factor=(base_floor.numerator*R**2,base_floor.denominator)

counts=dict(PREFIX710=0,all_q=0,q12to24=0,all_q_extra=0,q12to24_extra=0)
for i in range(G):
    for j in range(i,G):
        lo=M[i][j]
        hi2=S[i+1][j+1]
        U=hi2*R-lo*lo
        def positive(q):
            num,den=factors[q]
            return num-den*(q*U-lo*R)>0
        infty=inf_factor[0]-inf_factor[1]*U>0
        allq=infty and positive(2)
        sub=positive(12) and positive(24)
        base=base_factor[0]-base_factor[1]*U>0
        mult=1 if i==j else 2
        counts['PREFIX710']+=mult*base
        counts['all_q']+=mult*allq
        counts['q12to24']+=mult*sub
        counts['all_q_extra']+=mult*(allq and not base)
        counts['q12to24_extra']+=mult*(sub and not base)

if G==192:
    assert counts==dict(PREFIX710=26445,all_q=28724,q12to24=28871,
                        all_q_extra=2279,q12to24_extra=2426)
assert counts['all_q']>=counts['PREFIX710']
assert counts['q12to24']>=counts['all_q']

res={
    'schema':'PREFIX711_R6_MEAN_AWARE_GAMMA_INTERVAL_V1',
    'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'model':'independent Gamma(N_p,1) clocks; Y=max(T_p,T_z)',
    'grid_per_axis':G,
    'total_ordered_cells':G*G,
    'survivor_rows':189,
    'surviving_count_cells':9529,
    'certified_counts':counts,
    'certified_fractions':{k:str(F(v,G*G)) for k,v in counts.items()},
    'comparison_witness':'(0,3/20)',
    'all_q_certificate':'two affine endpoint tests at t=0 and t=1/2',
    'bounded_q_certificate':'two affine endpoint tests at t=1/24 and t=1/12',
    'verification':'ALL_CHECKS_PASS PREFIX711-R6',
    'grade':'AUTHOR_RECOMPUTED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED'
}
Path(__file__).with_name('PREFIX711_R6_RESULTS.json').write_text(
    json.dumps(res,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(res,indent=2))
