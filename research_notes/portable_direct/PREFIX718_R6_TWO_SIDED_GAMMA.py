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



# PREFIX-718 exact complementary-moment lower slope.
# Prefix reused from immutable PREFIX-716, preserving the frozen Gamma kernel.
import hashlib
assert G==192 and FINE==384 and D==768

@lru_cache(None)
def minratio(low,high):
    # Per-survivor second-moment/mean influence, lower over parameter interval.
    return min(F(y[1],x[0]) for x,y in zip(influence(low),influence(high)))

def tail_lower(a,b,c,d):
    # Arbitrary x -> upper corner: two coordinate-update orders.
    return max(min(minratio(c,d),minratio(b,b)),
               min(minratio(a,b),minratio(d,d)))

@lru_cache(None)
def bounds2(a,c,t):
    b,d=a+1,c+1
    nmu,nm2=pair(a,c); hmu,hm2=pair(b,d)
    mu=F(nmu,R); m2=F(nm2,R)
    delta=F(hmu-nmu,R); B=F(hm2-nm2,R)
    upper=bestC(a,b,c,d)
    lower=tail_lower(a,b,c,d)
    assert 0<lower<=upper and delta>=0 and lower*delta<=B<=upper*delta
    cap=F(0) if upper==lower else (B-lower*delta)/(upper-lower)
    assert 0<=cap<=delta
    ds=[F(0),delta,cap]
    for slope in (upper,lower):
        vertex=(slope-2*mu-t)/2
        if 0<=vertex<=delta:ds.append(vertex)
    def extra(x):
        return min(upper*x,B-lower*(delta-x))-(2*mu+t)*x-x*x
    new=m2-mu*mu-t*mu+max(extra(x) for x in ds)
    old,_=envelope(a,c,b,d,t)
    assert new<=old
    return old,new

mu_A,W_A=zero_clock_pair(149,1000)
mu_B,W_B=zero_clock_pair(146,1000)
assert W_A>W_B and mu_A>mu_B
tstar=(W_A-W_B)/(mu_A-mu_B)
assert F(23,100)<tstar<F(24,100)
times=(F(0),tstar,F(1,2))

def witness(t):
    return max(W_A-t*mu_A,W_B-t*mu_B)

windows=((36,48,110,123),(25,56,123,141))
all_new=[];counts=[];margins=[]
for i0,i1,j0,j1 in windows:
    cur=[]
    for i in range(i0,i1):
        for j in range(j0,j1):
            assert i<j
            vals=[(witness(t)-bounds2(i,j,t)[0],
                   witness(t)-bounds2(i,j,t)[1]) for t in times]
            old_min=min(x for x,y in vals)
            new_min=min(y for x,y in vals)
            if old_min<=0 and new_min>0:
                cur.append([i,j])
                margins.append(new_min)
    counts.append(len(cur));all_new.extend(cur)
assert counts==[28,47]
assert len(all_new)==75 and len({tuple(x) for x in all_new})==75
prior_multi={(1,79),(9,81),(21,85),(28,88),(30,89),(32,90),
             (34,91),(49,101),(57,163),(74,138)}
prior_multi|={(j,i) for i,j in list(prior_multi)}
assert not prior_multi.intersection({tuple(x) for x in all_new})
digest=hashlib.sha256(json.dumps(all_new,separators=(',',':')).encode()).hexdigest()
assert digest=='31a2225e3da3c3c35515caddd297eeb3e66942062ae5ecb5a980c507cfa97cf1'
assert min(margins)>F(130048,1000000)
new_ordered=2*len(all_new)
certified=138868+new_ordered
assert certified==139018 and F(certified,147456)==F(69509,73728)
result={
    'schema':'PREFIX718_R6_COMPLEMENTARY_ENDPOINT_SLOPE_V1',
    'date':'2026-11-12',
    'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'model':'189-row BRC Gamma maximum, not stopping-count maximum',
    'inherited_prefix716_all_q':138868,
    'windows_half_open':[[a,b,c,d] for a,b,c,d in windows],
    'new_half_square_counts':counts,
    'new_half_square_representatives':all_new,
    'new_half_square_digest':digest,
    'new_reflected_ordered_cells':new_ordered,
    'new_closed_cell_margin_lower':'130048/1000000',
    'certified_all_q_lower_bound':certified,
    'total_fine_cells':147456,
    'certified_all_q_fraction':str(F(certified,147456)),
    'claim_status':'AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED',
    'verification':'ALL_CHECKS_PASS PREFIX718-R6',
}
Path(__file__).with_name('PREFIX718_R6_RESULTS.json').write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX718-R6',counts,certified,str(F(certified,147456)))
