#!/usr/bin/env python3
"""PREFIX-716: stronger witness plus coupled Gamma-clock envelope exact certificate.
Frozen source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
Python integers and exact rationals; no floating-point acceptance criterion.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import json, sys, time

N=189
WD=1 << 18
G=int(sys.argv[1]) if len(sys.argv)>1 else 192
FINE=2*G
D=2*FINE
start=time.monotonic()

@lru_cache(None)
def inside(m,k,a):
    return 40*(m+1)*comb(m,k)*a**k*(WD-a)**(m-k)>WD**m
@lru_cache(None)
def wide(m,k):
    if k>m//2: return wide(m,m-k)
    mid=k*WD//m
    assert inside(m,k,mid)
    if k==0: left_lo=left_hi=0
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
    if 4*(right_lo-left_hi)>WD:return True
    if 4*(right_hi-left_lo)<WD:return False
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
print('rows built',time.monotonic()-start,flush=True)

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

L=D**(N-1)
R=L*L*Z
T=[]
for i in range(FINE+1):
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
print('axes prep',time.monotonic()-start,flush=True)

@lru_cache(None)
def pair(i,j):
    if j<i: i,j=j,i
    mu=(A[i]+A[j])*L*Z-sum(x*y for x,y in zip(T[i],K0[j]))
    m2=2*(B1[i]+B1[j])*L*Z-sum(x*y for x,y in zip(T[i],K1[j]))
    return mu,m2

factors={q:(b.numerator*q*R**2,b.denominator)
         for q,b in {q:W_e-mu_e/q for q in [2,12,24]}.items()}
inf_factor=(W_e.numerator*R**2,W_e.denominator)
base_floor=F(559812917,1000000)
base_factor=(base_floor.numerator*R**2,base_floor.denominator)

@lru_cache(None)
def is_certified(low_i,low_j,high_i,high_j,kind):
    lo=pair(low_i,low_j)[0]
    hi2=pair(high_i,high_j)[1]
    U=hi2*R-lo*lo
    if kind=='all':
        a=inf_factor[0]-inf_factor[1]*U>0
        b=factors[2][0]-factors[2][1]*(2*U-lo*R)>0
        return a and b
    if kind=='range':
        return all(factors[q][0]-factors[q][1]*(q*U-lo*R)>0 for q in (12,24))
    if kind=='base':
        return base_factor[0]-base_factor[1]*U>0
    raise ValueError(kind)


# PREFIX-713 exact first/second moment coupling, reusing frozen PREFIX-712 kernel
@lru_cache(None)
def influence(k):
    r=[(L*Z-K0[k][n],2*(n+1)*L*Z-K1[k][n]) for n in range(N)]
    assert all(x>0 and y>0 for x,y in r)
    return r

def maxratio(low,high):
    return max(F(x[1],y[0]) for x,y in zip(influence(low),influence(high)))

def bestC(a,b,c,d):
    return min(max(maxratio(c,c),maxratio(a,b)),
               max(maxratio(a,a),maxratio(c,d)))

def envelope(a,c,b,d,t):
    lmu,lm2=pair(a,c); hmu,hm2=pair(b,d)
    mu=F(lmu,R);m2=F(lm2,R)
    delta=F(hmu-lmu,R); B=F(hm2-lm2,R)
    assert delta>=0 and B>=0
    C=bestC(a,b,c,d)
    assert C>0
    kink=min(delta,B/C)
    ds=[F(0),delta,kink]
    vertex=(C-2*mu-t)/2
    if 0<=vertex<=kink:ds.append(vertex)
    increment=max(min(B,C*v)-(2*mu+t)*v-v*v for v in ds)
    new=(m2-mu*mu)-t*mu+increment
    old=F(hm2,R)-mu*mu-t*mu
    assert new<=old
    return new,old


assert G==192 and FINE==384 and D==768
mu_A,W_A=zero_clock_pair(149,1000)
assert W_A-W_e>F(5224,100000) and mu_e-mu_A>F(5474,10000)
groups=[(16,72),(24,64),(32,72),(0,80),(4,80),(8,72),(8,80),
        (16,80),(24,72),(24,80),(32,64)]
prior90=set()
for i,j in groups:
    for di in (0,1):
        for dj in (0,1):
            x,y=2*i+di,2*j+dj
            prior90.add((x,y));prior90.add((y,x))
prior90.add((9,145));prior90.add((145,9))
assert len(prior90)==90
seeds=[(1,79),(9,81),(21,85),(28,88),(30,89),(32,90),
       (34,91),(49,101),(57,163),(74,138)]
prior20=set(seeds)|{(j,i) for i,j in seeds}
assert len(prior20)==20 and not (prior20&prior90)
candidates=set()
for u,v in groups:
    for i in range(max(0,2*u-3),min(384,2*u+5)):
        for j in range(max(0,2*v-3),min(384,2*v+5)):
            if i<j:candidates.add((i,j))
for u,v in seeds:
    for i in range(max(0,u-3),min(384,u+4)):
        for j in range(max(0,v-3),min(384,v+4)):
            if i<j:candidates.add((i,j))
assert len(candidates)==1066
verified=[]
min_gap=None
for i,j in sorted(candidates):
    if (i,j) in prior90 or (i,j) in prior20:continue
    if is_certified(i,j,i+1,j+1,'all'):continue
    upper0,old0=envelope(i,j,i+1,j+1,F(0))
    gap0=W_A-upper0
    if gap0<=0:continue
    upperhalf,oldhalf=envelope(i,j,i+1,j+1,F(1,2))
    gaphalf=W_A-mu_A/2-upperhalf
    if gaphalf<=0:continue
    assert not is_certified(i,j,i+1,j+1,'all')
    assert upper0<=old0 and upperhalf<=oldhalf
    gap=min(gap0,gaphalf)
    if min_gap is None or gap<min_gap:min_gap=gap
    verified.append([i,j])
assert len(verified)==795 and min_gap>F(745380,1000000)
assert len({tuple(x) for x in verified})==795
assert all(x<y for x,y in verified)
import hashlib
digest=hashlib.sha256(json.dumps(verified,separators=(',',':')).encode()).hexdigest()
assert digest=='01ee0b393803fbdfe9b7b27bd80a1f50d5ebcd5ef3fc5a0b3bd115c0c13c33db'
total=137278+2*len(verified)
assert total==138868 and F(total,147456)==F(34717,36864)
result={'schema':'PREFIX716_R6_WITNESS_COUPLED_UNION_V1',
 'date':'2026-11-12','parent':'PREFIX-675',
 'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'grid_denominator':768,'grid_total':147456,
 'parent_prior_union':'PREFIX-714','prior_certified_all_q':137278,
 'search_half_square_candidates':len(candidates),
 'new_half_square_representatives':len(verified),
 'new_reflected_ordered_cells':2*len(verified),
 'certified_all_q_lower_bound':total,
 'certified_all_q_fraction':str(F(total,147456)),
 'minimum_new_gap_strict_lower':'745380/1000000',
 'representatives_compact_sha256':digest,'representatives':verified,
 'verification':'ALL_CHECKS_PASS PREFIX716-R6',
 'claim_status':'AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX716_R6_RESULTS.json').write_text(
 json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX716-R6',len(verified),total,str(F(total,147456)))
