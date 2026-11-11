#!/usr/bin/env python3
"""PREFIX-712: sparse dyadic refinement of PREFIX-711 exact Gamma-clock certificates.
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

assert G==192
groups=[(16,72),(24,64),(32,72),(0,80),(4,80),
        (8,72),(8,80),(16,80),(24,72),(24,80),(32,64)]
single=(4,72,1,1)
evidence=[]
def verify(i,j,di,dj):
    a,c=2*i+di,2*j+dj
    assert i<j
    n0,o0=envelope(a,c,a+1,c+1,F(0))
    n1,o1=envelope(a,c,a+1,c+1,F(1,2))
    oldmargin=min(W_e-o0,W_e-mu_e/2-o1)
    newmargin=min(W_e-n0,W_e-mu_e/2-n1)
    assert oldmargin<=0 and newmargin>0,(i,j,di,dj)
    evidence.append({'parent':[i,j],'child':[di,dj],
       'strict_new_margin_integer_floor':newmargin.numerator//newmargin.denominator})
for i,j in groups:
    for di in (0,1):
        for dj in (0,1):verify(i,j,di,dj)
verify(*single)
assert len(evidence)==45
added=2*len(evidence)
assert added==90 and F(137168+added,147456)==F(68629,73728)
result={'schema':'PREFIX713_COUPLED_MOMENT_CERTIFICATE_V1',
 'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'verified_half_square_new_cells':len(evidence),
 'additional_reflected_cells':added,
 'prefix712_certified':137168,'combined_certified_lower_bound':137168+added,
 'grid_total':147456,'certified_fraction':str(F(137168+added,147456)),
 'increment_fraction':str(F(added,147456)),'evidence':evidence,
 'complete_search':False,'verification':'ALL_CHECKS_PASS PREFIX713-R6',
 'grade':'AUTHOR_DERIVED / EXACT_FRACTION_WITNESSES / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX713_R6_RESULTS.json').write_text(
  json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX713-R6',len(evidence),added,result['certified_fraction'])
