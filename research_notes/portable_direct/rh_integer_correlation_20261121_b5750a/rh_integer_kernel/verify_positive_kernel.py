#!/usr/bin/env python3
"""Exact rational identities plus scoped non-interval kernel/road checks."""
from fractions import Fraction as F
from math import prod
from pathlib import Path
import json
import mpmath as mp


def weights(nodes):
    return [prod(b/(b-a) for k,b in enumerate(nodes) if k!=j)
            for j,a in enumerate(nodes)]


def rational_identities():
    count=0
    for nodes in [[F(1,8),F(3,10)], [F(1,7),F(2,5),F(3,4)],
                  [F(1,9),F(1,3),F(2,3),F(7,8)],
                  [F(j,13) for j in range(1,7)]]:
        v=weights(nodes)
        for k in range(len(nodes)):
            assert sum(w*a**k for w,a in zip(v,nodes))==(1 if k==0 else 0)
            count+=1
        assert sum(w/a for w,a in zip(v,nodes))==sum(1/a for a in nodes)
        count+=1
        for z in [F(1,3),F(1),F(3,2)]:
            assert prod(a/(a+z) for a in nodes)==sum(w*a/(a+z) for w,a in zip(v,nodes))
            count+=1
    return count


def cheb(m,A):
    d=m-1;s=mp.acosh(3);t=s/d;b=A*mp.tanh(t/2)**2
    a=[b+(A-b)*mp.sin(j*mp.pi/(2*d))**2 for j in range(m)]
    v=[(-1)**j*(mp.mpf('.5') if j in (0,d) else 1)*mp.sinh(t)*mp.sinh(s)
       /(d*(2*mp.sinh(t/2)**2+2*mp.sin(j*mp.pi/(2*d))**2)) for j in range(m)]
    return a,v


def kernel_checks():
    out=[]
    for aa in [('0.125','0.3'),('0.142857142857142857142857142857','0.4','0.75')]:
        a=list(map(mp.mpf,aa));v=weights(a)
        def f2(t):
            x,y=a[:2]
            return x*y*mp.exp(-x*t)*(-mp.expm1(-(y-x)*t))/(y-x)
        def density(t):
            if len(a)==2:return f2(t)
            return mp.quad(lambda x:a[2]*mp.exp(-a[2]*x)*f2(t-x),[0,t])
        for t in map(mp.mpf,['0.5','2']):
            direct=t-sum(w*(-mp.expm1(-x*t))/x for w,x in zip(v,a))
            positive=mp.quad(lambda u:(t-u)*density(u),[0,t])
            error=abs(direct-positive)
            assert error<mp.mpf('1e-65')
            sigma=mp.mpf('.5')
            bound=mp.exp(sigma*t-1)/sigma*prod(x/(x+sigma) for x in a)
            assert 0<positive<=bound
            out.append({'rates':aa,'t':str(t),'I_positive_integral':mp.nstr(positive,40),
                        'identity_error':mp.nstr(error,8),'chernoff_ratio':mp.nstr(positive/bound,25)})
    return out


def factor_sets(limit):
    spf=list(range(limit+1))
    for p in range(2,limit+1):
        if spf[p]==p:
            for n in range(p*p,limit+1,p):
                if spf[n]==n:spf[n]=p
    data=[]
    for n in range(2,limit+1):
        x=n;fac=[]
        while x>1:
            p=spf[x];fac.append(p)
            while x%p==0:x//=p
        data.append((n,tuple(fac)))
    return data


def actual_road_checks():
    m=10;A=mp.mpf('.5');a,v=cheb(m,A);limit=3000
    assert abs(sum(abs(w) for w in v)-3)<mp.mpf('1e-65')
    logs={};cache={};counts={};min_signed={};max_ratio=mp.mpf(0)
    sigma=mp.mpf('.5');lt=prod(x/(x+sigma) for x in a)
    for n,fac in factor_sets(limit):
        for p in fac:
            if p not in logs:logs[p]=mp.log(p)
        if fac not in cache:
            cache[fac]=sum(w*prod(-mp.expm1(-x*logs[p]) for p in fac)/x for w,x in zip(v,a))
        value=cache[fac];r=len(fac);counts[r]=counts.get(r,0)+1
        if r==1:assert 0<value<logs[fac[0]]
        if r in (2,3,4):
            signed=(-1)**r*value
            assert signed>0
            min_signed[r]=min(min_signed.get(r,mp.inf),signed)
        target=logs[fac[0]] if r==1 else 0
        bound=lt/(mp.e*sigma)*(prod(1+mp.exp(sigma*logs[p]) for p in fac)-1)
        ratio=abs(value-target)/bound
        assert ratio<=1
        max_ratio=max(max_ratio,ratio)
    return {'m':m,'A':str(A),'all_integer_inputs':limit-1,
            'factor_layer_counts':counts,'minimum_signed_values_for_proved_layers':{k:mp.nstr(v,35) for k,v in min_signed.items()},
            'max_actual_error_over_laplace_bound':mp.nstr(max_ratio,35),
            'scope':'All 2<=n<=3000, complete factor supports retained. Higher layers computed but no universal sign asserted.'}


def product_checks():
    result=[];s=mp.acosh(3)
    for m,A in [(5,mp.mpf('.5')),(10,mp.mpf('.5')),(30,mp.mpf('2'))]:
        a,v=cheb(m,A);d=m-1;t=s/d;b=a[0];delta=(A-b)/2
        for sigma in map(mp.mpf,['0.2','0.5','2']):
            u=mp.acosh(mp.cosh(t)+sigma/delta)
            closed=mp.sinh(t)*mp.sinh(s)/(mp.sinh(u)*mp.sinh(d*u))
            direct=prod(x/(x+sigma) for x in a)
            error=abs(closed/direct-1)
            assert error<mp.mpf('1e-65')
            result.append({'m':m,'A':str(A),'sigma':str(sigma),'relative_error':mp.nstr(error,8)})
        port=(mp.coth(t)+d*mp.coth(s))/(A*mp.tanh(t/2))
        assert abs(port/sum(1/x for x in a)-1)<mp.mpf('1e-65')
    return result


def omega_bound(L):
    primes=[];total=mp.mpf(0);n=2;r=0
    while True:
        if all(n%p for p in primes if p*p<=n):
            primes.append(n);total+=mp.log(n)
            if total>L:return r,primes
            r+=1
        n+=1


def finite_designs():
    s=mp.acosh(3);sigma=mp.mpf('.5');out=[]
    for L in [10,20,50,100,200,500,1000]:
        rmax,primes=omega_bound(L)
        for m in [2*L,L*L]:
            d=m-1;t=s/d
            def bound_log(b):
                A=b/mp.tanh(t/2)**2;delta=(A-b)/2
                u=mp.acosh(mp.cosh(t)+sigma/delta)
                loglt=mp.log(mp.sinh(t))+mp.log(mp.sinh(s))-mp.log(mp.sinh(u))-mp.log(mp.sinh(d*u))
                logbudget=(mp.log(mp.mpf(2)**rmax-1)-1-mp.log(sigma)+sigma*L+loglt
                           +mp.log(L)+mp.mpf('.5')*L+mp.log(2))
                return logbudget,A
            lo=mp.mpf('1e-12');hi=mp.mpf(1)
            assert bound_log(lo)[0]<0<bound_log(hi)[0]
            for _ in range(220):
                mid=(lo+hi)/2
                if bound_log(mid)[0]<0:lo=mid
                else:hi=mid
            b=lo*mp.mpf('.9');logbudget,A=bound_log(b)
            old_b=mp.mpf('.5')*mp.tanh(s/(2*(L-1)))**2
            out.append({'log_Z':L,'m':m,'omega_max_numerical_primorial_bracket':rmax,
                        'last_prime':primes[-2],'next_prime':primes[-1],
                        'b':mp.nstr(b,40),'A':mp.nstr(A,40),'sigma':'0.5','theta':'0.5',
                        'b_over_previous_A_half_m_L':mp.nstr(b/old_b,30),
                        'log_twice_uniform_error_budget':mp.nstr(logbudget,30),
                        'arithmetic':'80-digit non-interval parameter exploration; no actual population through exp(L) was enumerated.'})
    return out


def main():
    mp.mp.dps=80
    report={'status':'PASS','exact_rational_identity_checks':rational_identities(),
            'positive_convolution_checks':kernel_checks(),'whole_road_checks':actual_road_checks(),
            'chebyshev_product_checks':product_checks(),'finite_designs':finite_designs(),
            'evidence_scope':'Exact rational checks separately identified. Other calculations use 80-digit mpmath, non-interval. Universal statements are proved in POSITIVE_KERNEL_AND_LAPLACE_BOUND.md.'}
    Path(__file__).with_name('positive_kernel_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'exact_checks':report['exact_rational_identity_checks'],
                      'positive_integrals':len(report['positive_convolution_checks']),
                      'whole_road_inputs':report['whole_road_checks']['all_integer_inputs'],
                      'product_cases':len(report['chebyshev_product_checks']),
                      'finite_designs':len(report['finite_designs'])}))


if __name__=='__main__':main()
