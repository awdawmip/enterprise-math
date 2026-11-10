#!/usr/bin/env python3
"""PREFIX-665: exact finite 189-layer BRC boundary-strip p-concavity certificate.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run with Python 3 standard library; exact Fraction/integer comparisons throughout.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json

N, DEN = 189, 2**18
Q, DELTA, EPS = F(19,128), F(1,4096), F(1,4096)
checks=0

def ck(expr, label):
    global checks
    assert expr, label
    checks+=1

@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n

@lru_cache(None)
def wide(n,k):
    if k>n//2: return wide(n,n-k)
    mid=k*DEN//n
    ck(inside(n,k,mid),('central',n,k))
    if k==0: left_low=left_high=0
    else:
        low,high=0,mid
        while high-low>1:
            m=(low+high)//2
            if inside(n,k,m): high=m
            else: low=m
        left_low,left_high=low,high
    low,high=mid,DEN
    while high-low>1:
        m=(low+high)//2
        if inside(n,k,m): low=m
        else: high=m
    right_low,right_high=low,high
    if 4*(right_low-left_high)>DEN:return True
    if 4*(right_high-left_low)<DEN:return False
    raise AssertionError(('ambiguous frozen predicate',n,k))

def calc():
    state={0:1}; rows=[state.copy()]
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for k,v in state.items():nxt[k]+=v;nxt[k+1]+=v
        state={k:v for k,v in nxt.items() if wide(n,k)}
        rows.append(state.copy())
    ck(not rows[N] and len(rows)==N+1,'full 189-layer stop')
    ck(all(sum(rows[n].values())==2**n for n in range(25)),'initial 25 survival layers')
    ck(all(0<=v<=comb(n,k) for n,row in enumerate(rows) for k,v in row.items()),'coefficient bounds')
    ck(4*21**2*(Q-DELTA)*(1-Q+DELTA)>188,'score <21 throughout z band')
    t=[]; td=[]
    for n,row in enumerate(rows[:N]):
        weights={k:F(v*Q.numerator**k*(Q.denominator-Q.numerator)**(n-k),Q.denominator**n)
                 for k,v in row.items()}
        t.append(sum(weights.values(), F(0)))
        td.append(sum((w*(k-n*Q) for k,w in weights.items()),F(0))/(Q*(1-Q)))
    a=[];b=[];az=[];bz=[]
    for n in range(N):
        aa,bb,da,db=F(1),F(n+1),F(0),F(0)
        for m in range(N):
            if not t[m] and not td[m]:continue
            w=F(comb(n+m,n),2**(n+m+1))
            aa-=w*t[m];bb-=F(n+m+1,2)*w*t[m]
            da-=w*td[m];db-=F(n+m+1,2)*w*td[m]
        a.append(aa);b.append(bb);az.append(da);bz.append(db)
    ck(all(0<=a[n]<=1 and 0<=b[n]<=n+1 for n in range(N)),'nonnegative moment kernels')
    d2=[];d3=[];e0=[];e1=[]
    for n in range(N):
        f=[F(rows[n].get(k,0),comb(n,k)) for k in range(min(6,n+1))]
        d2.append(n*(n-1)*(f[2]-2*f[1]+f[0]) if n>=2 else F(0))
        d3.append(n*(n-1)*(n-2)*(f[3]-3*f[2]+3*f[1]-f[0]) if n>=3 else F(0))
        e0.append(f[4]-4*f[3]+6*f[2]-4*f[1]+f[0] if n>=4 else F(0))
        e1.append(f[5]-4*f[4]+6*f[3]-4*f[2]+f[1] if n>=5 else F(0))
    mu0=sum(t)+sum(a[n] for n in range(25))
    mp2=sum(a[n]*d2[n] for n in range(N))
    hp2=sum(b[n]*d2[n] for n in range(N))
    mp3=sum(a[n]*d3[n] for n in range(N))
    hp3=sum(b[n]*d3[n] for n in range(N))
    mp2z=sum(az[n]*d2[n] for n in range(N))
    hp2z=sum(bz[n]*d2[n] for n in range(N))
    ck(F('89.455')<mu0<F('89.456'),'exact mean center bracket')
    ck(231<mp2<232 and 10472<hp2<10474,'center second derivatives')
    ck(8308<mp3<8310 and 526257<hp3<526260,'center third derivatives')
    ck(-7322<mp2z<-7320 and -330968<hp2z<-330964,'center mixed derivatives')
    z2m=sum(abs(d2[n])*2*(n+1)*(n+2) for n in range(N))
    z2h=sum(abs(d2[n])*2*(n+1)*(n+2)*(n+3) for n in range(N))
    z1m3=21*sum(abs(x) for x in d3)
    z1h3=21*sum((n+1)*abs(d3[n]) for n in range(N))
    ck((z2m,z2h,z1m3,z1h3)==(35752800,1373274000,22503600,911030400),'weighted derivative budgets')
    cap4m=cap4h=F(0)
    for n in range(4,N):
        u=n*(n-1)*(n-2)*(n-3)
        cap=u*(abs(e0[n])+(n-4)*EPS*abs(e1[n])+8*comb(n-4,2)*EPS**2)
        cap4m+=cap;cap4h+=(n+1)*cap
    em=7322*DELTA+F(z2m,2)*DELTA**2+EPS*(8310+z1m3*DELTA)+EPS**2*cap4m/2
    eh=330968*DELTA+F(z2h,2)*DELTA**2+EPS*(526260+z1h3*DELTA)+EPS**2*cap4h/2
    # Boundary first derivative |mu_p(0,z)|<=225 and Bernstein second-derivative envelope.
    U1=225+13800*EPS+F(670800,2)*EPS**2+F(45727338888,3)*EPS**3
    ck(U1<229,'uniform |mu_p| <229')
    mu_lower=F('89.455')-3969*DELTA-229*EPS
    mp2_lower=231-em
    hp2_upper=10474+eh
    wpp_upper=2*hp2_upper-2*mu_lower*mp2_lower
    ck(mu_lower>88 and mp2_lower>210 and hp2_upper<12217,'signed curvature envelopes')
    ck(wpp_upper < -12000, 'strict uniform W_pp < -12000')
    ck(EPS/F(1,2**15)==8, 'eightfold strip enlargement')
    return {
      'schema':'EM_PREFIX665_R6_SIGNED_P_CURVATURE_STRIP_V1',
      'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'domain':{'p':['0','1/4096'],'z':['607/4096','609/4096'],'q':['12','24']},
      'center_exact_rational_brackets':{
        'mu':['89.455','89.456'],'mu_pp':['231','232'],'H_pp':['10472','10474'],
        'mu_ppp':['8308','8310'],'H_ppp':['526257','526260'],
        'mu_ppz':['-7322','-7320'],'H_ppz':['-330968','-330964']},
      'signed_enclosures':{
        'mean_lower_rational':str(mu_lower),
        'mu_pp_error_upper_rational':str(em),
        'H_pp_error_upper_rational':str(eh),
        'mu_pp_lower_rational':str(mp2_lower),
        'H_pp_upper_rational':str(hp2_upper),
        'W_pp_upper_rational':str(wpp_upper)},
      'theorem':'mu_pp>210; W_pp<-12000; V_q,pp<-12000*q^2 on rectangle for all real 12<=q<=24',
      'stability':'M_q - V_q(p,z) >= 76650*p + 6000*q^2*p^2 + 6400000*(z-z_star(q))^2',
      'unique_maximizer':'(0,z_star(q))',
      'area_gain_vs_PREFIX664':8,
      'proof_dependencies':['PREFIX-659 frozen model and edge mean','PREFIX-660 strict boundary z curvature',
                            'PREFIX-661 boundary p-gradient','PREFIX-664 kernel and Bernstein derivation'],
      'checks_passed':checks,'result':'ALL_CHECKS_PASS',
      'status':'AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED'
    }

if __name__=='__main__':
    result=calc()
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',result['checks_passed'])
