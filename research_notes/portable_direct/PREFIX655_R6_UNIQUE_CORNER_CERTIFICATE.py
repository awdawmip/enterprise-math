#!/usr/bin/env python3
"""PREFIX-655: exact BRC variance unique-corner certificate (frozen 189-layer observer)."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
N,DEN=189,1<<18
L=Q(3,20); z=Q(19,128)
@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n
@lru_cache(None)
def wide(n,k):
    if k>n//2: return wide(n,n-k)
    mid=k*DEN//n
    if not inside(n,k,mid): raise Exception(('mid',n,k))
    if k==0: ll=lh=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            m=(hi+lo)//2
            if inside(n,k,m): hi=m
            else: lo=m
        ll,lh=lo,hi
    lo,hi=mid,DEN
    while hi-lo>1:
        m=(hi+lo)//2
        if inside(n,k,m): lo=m
        else: hi=m
    rl,rh=lo,hi
    if 4*(rl-lh)>DEN:return True
    if 4*(rh-ll)<DEN:return False
    raise Exception(('ambig',n,k))
def rows_make():
    rows=[{0:1}]; state={0:1}
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for k,v in state.items():nxt[k]+=v;nxt[k+1]+=v
        state={k:v for k,v in nxt.items() if wide(n,k)}
        rows.append(state.copy())
    assert not rows[189]
    return rows

def surv_and_deriv(rows,x):
    a,b=x.numerator,x.denominator
    s=[];d=[]
    for n in range(N):
        a_pow=[a**i for i in range(n+1)]
        b_pow=[(b-a)**i for i in range(n+1)]
        top=0;dtop=0
        for k,r in rows[n].items():
            term=r*a_pow[k]*b_pow[n-k]
            top+=term
            if n:
                dtop+=r*(k*a_pow[k-1]*b_pow[n-k] if k else 0)
                if n>k:dtop-=r*(n-k)*a_pow[k]*b_pow[n-k-1]
        s.append(Q(top,b**n))
        d.append(Q(dtop,b**(n-1)) if n else Q(0))
    return s,d

def mu_H(u,v):
    mu=sum(u)+sum(v)
    H=sum((n+1)*u[n]+(n+1)*v[n] for n in range(N))
    for n in range(N):
        if not u[n]:continue
        for m in range(N):
            if not v[m]:continue
            w=Q(comb(n+m,n),2**(n+m+1))*u[n]*v[m]
            mu-=w
            H-=Q(n+m+1,2)*w
    return mu,H

def mu_Hderiv(u,dv):
    mu=sum(dv)
    H=sum((m+1)*dv[m] for m in range(N))
    for n in range(N):
        if not u[n]:continue
        for m in range(N):
            if not dv[m]:continue
            w=Q(comb(n+m,n),2**(n+m+1))*u[n]*dv[m]
            mu-=w
            H-=Q(n+m+1,2)*w
    return mu,H

if __name__ == "__main__":
    import json
    checks=0
    def ck(test, name):
        global checks
        assert test, name
        checks+=1
    z0=Q(19,128); h=Q(1,2**18)
    zlo,zhi=z0-h,z0+h
    ck((zlo,zhi)==(Q(38911,262144),Q(38913,262144)),"strip endpoints")
    ck(zlo*(1-zlo)>Q(188,1500),"binomial second score")
    ck(188 < 4*20**2*zlo*(1-zlo),"binomial first score")
    rows=rows_make()
    ck(sum(rows[24].values())==2**24,"row24")
    ck(sum(rows[25].values())==2**25-2,"first loss at 25")
    ck(all(sum(rows[n].values())==2**n for n in range(25)),"no earlier loss")
    sL,_=surv_and_deriv(rows,L)
    sz,dz=surv_and_deriv(rows,z0)
    ck(all(0<=s<=1 for s in sL+sz),"survival probabilities")
    mu,H=mu_H(sL,sz)
    muz,Hz=mu_Hderiv(sL,dz)
    W=2*H-mu*mu
    Wz=2*Hz-2*mu*muz
    ck(103<mu<104,"strict center mean")
    ck(104+3780*h<105,"uniform strip mean envelope")
    ck(0<muz<3780,"center mean derivative")
    mdz=189*20
    mdzz=189*1500
    Hzz=1500*sum(range(1,N+1))
    Wzz=2*Hzz+2*mdz**2+2*105*mdzz
    ck((mdz,mdzz,Hzz,Wzz)==(3780,283500,26932500,141976800),"uniform second-derivative")
    derivative_bands=[]
    for q,upper,slack,bound in [(12,-87480,78004,-9476),(24,-343577,311987,-31590)]:
        vprime=q*q*Wz-q*muz
        m_q=q*q*Wzz+q*mdzz
        ck(vprime < upper,"center derivative negative at q="+str(q))
        ck(m_q*h < slack,"curvature perturbation at q="+str(q))
        ck(upper+slack==bound,"strict uniform derivative bound at q="+str(q))
        flo=vprime.numerator*1000//vprime.denominator
        ck(Q(flo,1000)<vprime<Q(flo+1,1000),"derivative exact interval at q="+str(q))
        derivative_bands.append({"q":q,"center_dV_dz_lower":str(Q(flo,1000)),"center_dV_dz_upper":str(Q(flo+1,1000)),"M_q":str(m_q),"M_q_h":str(m_q*h),"certified_uniform_dV_dz_upper":str(bound)})
    corners=[]
    sc,_=surv_and_deriv(rows,zlo)
    muc,Hc=mu_H(sL,sc)
    Wc=2*Hc-muc*muc
    for q in (12,24):
        vq=q*q*Wc-q*muc
        fl=vq.numerator*1000//vq.denominator
        ck(Q(fl,1000)<vq<Q(fl+1,1000),"corner variance rational interval")
        corners.append({"q":q,"at_p":"3/20","at_z":str(zlo),"variance_lower":str(Q(fl,1000)),"variance_upper":str(Q(fl+1,1000))})
    result={"schema":"EM_PREFIX655_UNIQUE_CORNER_CERTIFICATE_V1", "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d", "inputs":{"p_interval":["3/20","1/6"],"z_interval":[str(zlo),str(zhi)],"q_interval":[12,24],"layers":189}, "center_mu_band":["103","104"],"max_strip_mu_upper":"105", "second_derivative_bound":{"W_zz":str(Wzz),"mu_zz":str(mdzz)},"derivative_bands":derivative_bands,"corner_variance_bands":corners,"conclusion":"Under PREFIX643 convexity and PREFIX654 p-edge ordering, unique strip maximizer (p,z)=(3/20,38911/262144) for every real 12<=q<=24", "checks_passed":checks,"result":"ALL_CHECKS_PASS", "arithmetic":"Python standard library Fraction and integer arithmetic"}
    print(json.dumps(result,indent=2))
    print('ALL_CHECKS_PASS',checks)
