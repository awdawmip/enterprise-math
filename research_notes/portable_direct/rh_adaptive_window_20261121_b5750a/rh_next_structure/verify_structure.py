#!/usr/bin/env python3
"""New structural checks, not a rerun of the preceding error-bound suite."""
from fractions import Fraction as F
from math import comb,factorial,prod
from pathlib import Path
from functools import lru_cache
import json
import mpmath as mp
mp.mp.dps=75

@lru_cache(None)
def factors(n):
    ps=[];p=2
    while p*p<=n:
        if n%p==0:
            ps.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:ps.append(n)
    return tuple(ps)

def add(x,y):return x[0]+y[0],x[1]+y[1]
def scale(x,c):return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def mul(x,y):
    vals=[a*b for a in x for b in y]
    return min(vals),max(vals)
def power(x,k):
    out=(F(1),F(1))
    for _ in range(k):out=mul(out,x)
    return out

def floor_root(n,k):
    lo=0;hi=1<<((n.bit_length()+k-1)//k)
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**k<=n:lo=mid
        else:hi=mid
    if hi**k<=n:lo=hi
    assert lo**k<=n<(lo+1)**k
    return lo

def inv_root(p,k):
    S=10**26;q=floor_root(p*S**k,k)
    return F(S,q+1),F(S,q)

def road_interval(n,j,hden):
    out=(F(1),F(1))
    for p in factors(n):
        x=power(inv_root(p,hden),j)
        out=mul(out,(1-x[1],1-x[0]))
    return out

def derivative_interval(n,m,hden):
    out=(F(0),F(0))
    for j in range(1,m+1):
        out=add(out,scale(road_interval(n,j,hden),F((-1)**(j+1)*comb(m,j)*hden,j)))
    return out

def interval_strings(x):
    S=10**16
    lo=x[0].numerator*S//x[0].denominator
    hi=-((-x[1].numerator*S)//x[1].denominator)
    def fmt(n):
        sign='-' if n<0 else '';n=abs(n)
        return f'{sign}{n//S}.{n%S:016d}'
    return {'lower':fmt(lo),'upper':fmt(hi),'kind':'OUTWARD_RATIONAL_DECIMAL'}

def stirling2(n,k):
    if n==k==0:return 1
    if n<1 or k<1:return 0
    return k*stirling2(n-1,k)+stirling2(n-1,k-1)

def mul_poly(a,b,N):
    c=[F(0)]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N:c[i+j]+=x*y
    return c

def positive_mixed_power(ls,q):
    r=len(ls)
    return sum((-1)**(r-mask.bit_count())*sum(ls[i] for i in range(r) if mask>>i&1)**q for mask in range(1<<r))

def numeric_road(n,h):return mp.fprod([-mp.expm1(-h*mp.log(p)) for p in factors(n)])
def numeric_D2(n,h):
    xs=[mp.exp(-h*mp.log(p)) for p in factors(n)]
    return mp.fprod([1-x for x in xs])*(4-mp.fprod([1+x for x in xs]))/(2*h)
def lam(n):
    ps=factors(n)
    return mp.log(ps[0]) if len(ps)==1 else mp.mpf(0)
def logs(n):return [mp.log(p) for p in factors(n)]
def eta_minus(n,h):
    ls=logs(n);r=len(ls);L=mp.fsum(ls)
    if r==1:return h*h*L**3/3
    if r==2:return mp.mpf(0)
    return min(h*h*L**3/3,(2**(r-1)-2)*h**(r-1)*mp.fprod(ls))
def eta_plus(n,h):
    ls=logs(n)
    if len(ls)!=2:return mp.mpf(0)
    return min(h*h*ls[0]*ls[1]*mp.fsum(ls),h*ls[0]*ls[1]/2)
def render(x):return mp.nstr(x,28)

def main():
    cases=[(2,30,20,-1),(2,30,2,1),(2,210,2,-1),(2,210,1,1),(3,210,20,1),(3,210,2,-1),(3,210,1,1),(3,30,20,-1),(3,30,1,1)]
    strict=[]
    for m,n,den,sign in cases:
        value=derivative_interval(n,m,den)
        assert value[0]>0 if sign>0 else value[1]<0
        strict.append({'m':m,'n':n,'omega':len(factors(n)),'h':f'1/{den}','sign':sign,'D':interval_strings(value)})
    exact_jet_checks=0
    for m in range(1,7):
        for r in range(2,8):
            ls=list(range(1,r+1));q0=max(r,m+1)
            coef=[F(1)]+[F(0)]*q0
            for L in ls:
                factor=[F(0)]+[F((-1)**(k+1)*L**k,factorial(k)) for k in range(1,q0+1)]
                coef=mul_poly(coef,factor,q0)
            Dcoef=[coef[q]*sum((-1)**(j+1)*comb(m,j)*j**(q-1) for j in range(1,m+1)) for q in range(1,q0+1)]
            assert all(c==0 for c in Dcoef[:q0-1])
            if r<=m+1:
                expected=F((-1)**r*positive_mixed_power(ls,m+1),m+1)
            else:expected=F((-1)**(m+1)*factorial(m)*stirling2(r-1,m)*prod(ls))
            assert Dcoef[-1]==expected
            exact_jet_checks+=1
    envelope_cases=0
    for n in (6,12,30,42,60,210,2310,30030):
        ls=logs(n);r=len(ls);L=mp.fsum(ls)
        for h in map(mp.mpf,['0.001','0.03','0.2','1']):
            val=numeric_D2(n,h)
            if r==2:
                assert val>0
                bound=min(h*h*mp.fprod(ls)*L,h*mp.fprod(ls)/2)
            else:bound=(2**(r-1)-2)*h**(r-1)*mp.fprod(ls)
            assert abs(val)<=bound+mp.mpf('1e-65')
            envelope_cases+=1
    window=[]
    for Z in (125,625,3125):
        theta=mp.mpf('0.75');Zmp=mp.mpf(Z);Y=Zmp**(mp.mpf(2)/3)
        entries=[]
        for n in range(2,Z+1):
            ls=logs(n);r=len(ls);L=mp.fsum(ls);ramp=Zmp/n-1
            if r==1:entries.append((r,hyp:=L**3*ramp/3,mp.mpf(0)))
            elif r>=3:entries.append((r,L**3*ramp/3,(2**(r-1)-2)*mp.fprod(ls)*ramp))
        def Cminus(h):
            return mp.fsum([h*h*a if r==1 else min(h*h*a,h**(r-1)*b) for r,a,b in entries])
        hcap=2*mp.log(2)/mp.log(Zmp);budget=Zmp**theta/2
        lo=mp.mpf(0);hi=hcap
        if Cminus(hi)<=budget:lo=hi
        else:
            for _ in range(100):
                mid=(lo+hi)/2
                if Cminus(mid)<=budget:lo=mid
                else:hi=mid
        h=lo*mp.mpf('0.99')
        hgeneric=mp.sqrt(mp.mpf('1.5'))*Zmp**(-(1-theta)/2)/mp.log(Zmp)**2
        checks=[]
        for y in (Y,mp.sqrt(Y*Zmp),Zmp):
            error=mp.fsum([(numeric_D2(n,h)-lam(n))*(y/n-1) for n in range(2,int(mp.floor(y))+1)])
            minus=mp.fsum([eta_minus(n,h)*(y/n-1) for n in range(2,int(mp.floor(y))+1)])
            plus=mp.fsum([eta_plus(n,h)*(y/n-1) for n in range(2,int(mp.floor(y))+1)])
            assert -minus-mp.mpf('1e-60')<=error<=plus+mp.mpf('1e-60')
            assert minus/y**theta<=Cminus(h)/Zmp**theta+mp.mpf('1e-60')
            checks.append({'y':render(y),'G_extrap_minus_G':render(error),'minus_envelope':render(minus),'plus_envelope':render(plus)})
        window.append({'Y':render(Y),'Z':Z,'theta':render(theta),'h_generic':render(hgeneric),'h_adaptive_selected':render(h),'ratio_to_generic':render(h/hgeneric),'orientation_cap':render(hcap),'endpoint_minus_envelope':render(Cminus(h)),'endpoint_budget':render(budget),'samples':checks,'evidence':'75-digit non-interval exploration; endpoint-monotonicity theorem is proved separately.'})
    report={'status':'ALL_NEW_STRUCTURE_CHECKS_PASSED','strict_sign_cases':strict,'exact_formal_log_jet_cases':exact_jet_checks,'D2_product_envelope_cases':envelope_cases,'adaptive_window_cases':window,'scope':['Strict sign cases use Fraction algebraic-root enclosures only.','Formal log jets are exact rational polynomial calculations.','Window/envelope explorations use mpmath 75 digits, not interval certificates.','No infinite-window energy estimate or RH implication is established by these computations.']}
    Path(__file__).with_name('structure_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'strict_sign_cases':strict,'exact_formal_log_jet_cases':exact_jet_checks,'D2_product_envelope_cases':envelope_cases,'adaptive_window_cases':[{k:v for k,v in row.items() if k!='samples'} for row in window]},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
