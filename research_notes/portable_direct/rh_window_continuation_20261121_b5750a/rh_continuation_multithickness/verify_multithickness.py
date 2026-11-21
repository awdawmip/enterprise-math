#!/usr/bin/env python3
"""Finite crosschecks for the proved multithickness road-observer identities.

No RH or infinite-window energy estimate is tested or inferred.  Arithmetic
moment checks are exact Fraction computations; transcendental checks use
mpmath at 90 digits and are not interval certificates.
"""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 90


def factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out


def road(n,a):
    return mp.fprod([-mp.expm1(-a*mp.log(p)) for p in factors(n)])


def von_mangoldt(n):
    ps=factors(n)
    return mp.log(ps[0]) if len(ps)==1 else mp.mpf(0)


def weights(m):
    return [Fraction((-1)**(j+1)*comb(m,j),j) for j in range(1,m+1)]


def derivative_readout(n,m,h,correct_unit=True):
    value=mp.fsum([mp.mpf(w.numerator)/w.denominator*road(n,j*h)
                   for j,w in enumerate(weights(m),1)])/h
    if n==1 and correct_unit:
        value-=mp.fsum([mp.mpf(1)/j for j in range(1,m+1)])/h
    return value


def road_derivative(n,k,a):
    ps=factors(n)
    terms=[]
    for mask in range(1<<len(ps)):
        size=mask.bit_count()
        logd=mp.fsum([mp.log(p) for i,p in enumerate(ps) if mask>>i&1])
        terms.append((-1)**size*(-logd)**k*mp.exp(-a*logd))
    return mp.fsum(terms)


def center(y):
    return y*mp.log(y)-(1+mp.euler)*y


def smoothed(m,h,y):
    return mp.fsum([derivative_readout(n,m,h)*(y/n-1)
                    for n in range(2,int(mp.floor(y))+1)])-center(y)


def smoothed_single(a,y):
    return mp.fsum([road(n,a)/a*(y/n-1)
                    for n in range(2,int(mp.floor(y))+1)])-center(y)


def fixed_G(y):
    return mp.fsum([von_mangoldt(n)*(y/n-1)
                    for n in range(2,int(mp.floor(y))+1)])-center(y)


def render(x):return mp.nstr(x,35)


def main():
    exact_count=0
    kernel_count=0
    for m in range(1,9):
        ws=weights(m)
        harmonic=sum((Fraction(1,j) for j in range(1,m+1)),Fraction(0))
        assert sum(ws)==harmonic
        exact_count+=1
        for k in range(1,m+1):
            actual=sum((w*j**k for j,w in enumerate(ws,1)),Fraction(0))
            assert actual==(1 if k==1 else 0)
            exact_count+=1
        moment=sum((w*j**(m+1) for j,w in enumerate(ws,1)),Fraction(0))
        assert moment==(-1)**(m+1)*factorial(m)
        exact_count+=1
        assert sum(abs(w) for w in ws)==sum((Fraction(2**j-1,j) for j in range(1,m+1)),Fraction(0))
        exact_count+=1
        assert sum(comb(m,j) for j in range(1,m+1))==2**m-1
        exact_count+=1
        for i in range(129):
            t=Fraction(m*i,128)
            kernel=sum((w*max(Fraction(j)-t,Fraction(0))**m for j,w in enumerate(ws,1)),Fraction(0))/factorial(m)
            assert (-1)**(m+1)*kernel>=0
            kernel_count+=1
    derivative_cases=0
    derivative_max=mp.mpf(0)
    ns=[2,4,8,6,12,30,42,60,210,2310,30030]
    for n in ns:
        L=mp.fsum([mp.log(p) for p in factors(n)])
        for a in map(mp.mpf,['0','0.001','0.1','0.75','2']):
            for k in range(1,9):
                ratio=abs(road_derivative(n,k,a))/L**k
                assert ratio<=1+mp.mpf('1e-75')
                derivative_max=max(derivative_max,ratio)
                derivative_cases+=1
    error_cases=0
    error_max=mp.mpf(0)
    for m in range(1,7):
        for h in map(mp.mpf,['0.001','0.01','0.05','0.25']):
            for n in range(2,151):
                L=mp.fsum([mp.log(p) for p in factors(n)])
                D=derivative_readout(n,m,h)
                error=abs(D-von_mangoldt(n))
                bound=h**m*L**(m+1)/(m+1)
                ratio=error/bound
                assert ratio<=1+mp.mpf('1e-65')
                error_max=max(error_max,ratio)
                error_cases+=1
            unit=derivative_readout(1,m,h)
            assert abs(unit)<mp.mpf('1e-75')
    sharpness=[]
    for m in range(1,7):
        h=mp.mpf('1e-7');n=8;L=mp.log(2)
        deficit=L-derivative_readout(n,m,h)
        integral=mp.quad(lambda t:(-mp.expm1(-h*t))**m,[0,L])
        assert abs(deficit-integral)<mp.mpf('1e-75')
        ratio=deficit/(h**m*L**(m+1)/(m+1))
        assert abs(1-ratio)<mp.mpf('1e-6')
        sharpness.append({'m':m,'h':render(h),'n':n,'bound_ratio':render(ratio)})
    window_cases=0
    window_max=mp.mpf(0)
    combination_max_abs=mp.mpf(0)
    rows=[]
    for m in (1,2,3,4):
        for theta in map(mp.mpf,['0.6','0.8']):
            for lam in map(mp.mpf,['1.5','2']):
                for Y in map(mp.mpf,['3','10','25']):
                    candidate=((m+1)/mp.mpf(2))**(mp.mpf(1)/m)*Y**(-lam*(1-theta)/m)/(lam*mp.log(Y))**(1+mp.mpf(2)/m)
                    h=min(mp.mpf(1)/(2*m),candidate)
                    for y in (Y,Y**((1+lam)/2),Y**lam):
                        observer=smoothed(m,h,y)
                        err=abs(observer-fixed_G(y))
                        ratio=err/(mp.mpf('0.5')*y**theta)
                        assert ratio<=1+mp.mpf('1e-65')
                        alternate=mp.fsum([(-1)**(j+1)*comb(m,j)*smoothed_single(j*h,y) for j in range(1,m+1)])
                        residual=abs(observer-alternate)
                        assert residual<mp.mpf('1e-65')
                        window_max=max(window_max,ratio)
                        combination_max_abs=max(combination_max_abs,residual)
                        window_cases+=1
                    rows.append({'m':m,'theta':render(theta),'lambda':render(lam),'Y':render(Y),'h':render(h),'max_thickness':render(m*h)})
    report={
      'status':'ALL_CHECKS_PASSED',
      'interpretation':'Finite consistency checks; general error estimates are proved in NOTES.md. No RH or uniform road energy bound inferred.',
      'arithmetic':'Fraction exact for moments and kernel grid; mpmath 90 digits for transcendental checks; not interval arithmetic',
      'exact_moment_and_weight_checks':exact_count,
      'exact_peano_kernel_sign_grid_checks':kernel_count,
      'road_derivative_cases':derivative_cases,
      'max_road_derivative_ratio':render(derivative_max),
      'pointwise_extrapolation_cases':error_cases,
      'max_pointwise_error_bound_ratio':render(error_max),
      'prime_power_sharpness':sharpness,
      'window_horizon_cases':window_cases,
      'max_window_error_half_budget_ratio':render(window_max),
      'max_normalized_combination_absolute_residual':render(combination_max_abs),
      'window_parameters':rows,
      'limits':['Fixed finite m; no uniform m-growth conclusion.','Input coefficient amplification and negative weights are explicitly retained.','n=1 is corrected using R_0(1)=1.','All integer n<=floor(y) are included in each finite smoothing sum.']
    }
    dest=Path(__file__).with_name('multithickness_results.json')
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('window_parameters','prime_power_sharpness')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
