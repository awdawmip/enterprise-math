#!/usr/bin/env python3
"""PREFIX-666: exact local Taylor/Bernstein derivative certificate on expanded p strip.
Scientific recurrence and pin inherited from PREFIX-665 (f42f2906d77f24085c123f3ccfe9667d41caa96d).
Only exact rational arithmetic, integer survivor recurrence and native first-stop BRC readout.
"""
from PREFIX666_experiment import build,N,Q
from fractions import Fraction as F
from math import comb, factorial
import json

EPS=F(1,128); DELTA=F(1,4096); R=20


def delta_f(row,n,d):
    return sum(((-1)**(d-k)*comb(d,k)*F(row.get(k,0),comb(n,k)) for k in range(d+1)), F(0))

def fall(n,d):
    v=1
    for k in range(d):v*=n-k
    return v

def kernel(rows):
    t=[]; td=[]
    for m in range(N):
        ws=[F(v*Q.numerator**k*(Q.denominator-Q.numerator)**(m-k),Q.denominator**m) for k,v in rows[m].items()]
        t.append(sum(ws,F(0)))
        td.append(sum((w*(k-m*Q) for (k,v),w in zip(rows[m].items(),ws)),F(0))/(Q*(1-Q)))
    aa=[];bb=[];adz=[];bdz=[]
    for n in range(N):
        a,b,az,bz=F(1),F(n+1),F(0),F(0)
        for m in range(N):
            w=F(comb(n+m,n),2**(n+m+1))
            a-=w*t[m];b-=F(n+m+1,2)*w*t[m]
            az-=w*td[m];bz-=F(n+m+1,2)*w*td[m]
        aa.append(a);bb.append(b);adz.append(az);bdz.append(bz)
    assert all(0<=v<=1 for v in aa)
    assert all(0<=v<=n+1 for n,v in enumerate(bb))
    # From PREFIX-665, using |t'_m|<21, NB moments.
    assert all(abs(v)<=21 for v in adz)
    assert all(abs(v)<=21*(n+1) for n,v in enumerate(bdz))
    return aa,bb,adz,bdz,t

def derivative_poly_interval(rows, weights, d, eps, r, weight_cap):
    coeff=[]
    for j in range(r+1):
        k=d+j
        coeff.append(sum((weights[n]*fall(n,k)*delta_f(rows[n],n,k) for n in range(k,N)),F(0))/factorial(j))
    low=coeff[0]+sum((min(0,c)*eps**j for j,c in enumerate(coeff) if j),F(0))
    high=coeff[0]+sum((max(0,c)*eps**j for j,c in enumerate(coeff) if j),F(0))
    m=d+r+1
    # Absolute mth derivative |s_n^(m)|<=2^(m-1)*fall(n,m), thanks |Delta^m f|<=2^(m-1) for 0<=f<=1.
    # For 0<=f<=1, the signed alternating binomial sum has absolute bound 2^(m-1).
    tail=sum((weight_cap(n)*fall(n,m)*2**(m-1) for n in range(m,N)),F(0))*eps**(r+1)/factorial(r+1)
    return (low-tail,high+tail,tail,coeff)

def main():
    rows=build(); aa,bb,adz,bdz,t=kernel(rows)
    fields={}
    for name,vec,cap in [('mu_pp',aa,lambda n:F(1)),('H_pp',bb,lambda n:F(n+1)),
                         ('mu_ppz',adz,lambda n:F(21)),('H_ppz',bdz,lambda n:F(21*(n+1)) )]:
        lo,hi,rem,coeff=derivative_poly_interval(rows,vec,2,EPS,R,cap)
        fields[name]={'lower':str(lo),'upper':str(hi),'tail':str(rem), 'center':str(coeff[0]),
                      'small_coefficients': [str(x) for x in coeff[:5]]}
        print(name,'approx',float(lo),float(hi),'tail',float(rem))
        assert lo<=hi
    b=lambda name,key:F(fields[name][key])
    # Fresh uniform z-second-derivative enclosures: |s_n''(p)| is bounded by
    # n(n-1) sum_k binom(n-2,k) |Delta^2 f_n(k)| EPS^k for all p in [0,EPS].
    # NB moment bounds are |a_n,zz|<=2(n+1)(n+2),
    # |b_n,zz|<=2(n+1)(n+2)(n+3) at every z in J.
    Bs=[]
    for n in range(N):
        if n<2: Bs.append(F(0));continue
        f=lambda k:F(rows[n].get(k,0),comb(n,k))
        Bs.append(n*(n-1)*sum((comb(n-2,k)*abs(f(k+2)-2*f(k+1)+f(k))*EPS**k
                                    for k in range(n-1)),F(0)))
    z2mu=sum((Bs[n]*2*(n+1)*(n+2) for n in range(N)),F(0))
    z2h=sum((Bs[n]*2*(n+1)*(n+2)*(n+3) for n in range(N)),F(0))
    em=DELTA*max(abs(b('mu_ppz','lower')),abs(b('mu_ppz','upper')))+z2mu*DELTA**2/2
    eh=DELTA*max(abs(b('H_ppz','lower')),abs(b('H_ppz','upper')))+z2h*DELTA**2/2
    mupp_lower=b('mu_pp','lower')-em
    hpp_upper=b('H_pp','upper')+eh
    # Standalone |mu_p| bound from Bernstein coefficients and 0<=a_n(z)<=1.
    mp_bound=sum((n*sum((comb(n-1,k)*abs(F(rows[n].get(k+1,0),comb(n,k+1))
                                     -F(rows[n].get(k,0),comb(n,k)))*EPS**k
                          for k in range(n)),F(0)) for n in range(1,N)),F(0))
    # Reuse PREFIX-659 edge: mu(0,Q)>89.455 and |mu_z(0,z)|<3969 for z in J.
    mu_lower=F('89.455')-3969*DELTA-mp_bound*EPS
    wpp_upper=2*hpp_upper-2*mu_lower*mupp_lower
    print('error',float(em),float(eh),'mupp_lower',float(mupp_lower),'hpp_upper',float(hpp_upper))
    print('mu_lower',float(mu_lower),'Wpp_upper',float(wpp_upper))
    assert mu_lower>86 and mupp_lower>0 and wpp_upper<0
    # Use simple rational inequalities as the published strong-curvature certificate.
    assert mupp_lower>F(225) and hpp_upper<F(15400) and wpp_upper<F(-8000)
    out={ 'schema':'PREFIX666_THIRTYTWO_FOLD_SIGNED_CURVATURE_EXACT_V1','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
       'domain':{'p':['0',str(EPS)],'z':['607/4096','609/4096'],'q':['12','24']},
       'taylor_degree':R,'derivative_enclosures':fields,
       'z_errors':{'mu_pp':str(em),'H_pp':str(eh)},
       'uniform_second_z_derivative_bounds':{'mu_ppzz':str(z2mu),'H_ppzz':str(z2h)},
       'uniform_first_p_derivative_absolute_bound':str(mp_bound),
       'lower_mu':str(mu_lower),
       'lower_mu_pp':str(mupp_lower),'upper_H_pp':str(hpp_upper),'upper_W_pp':str(wpp_upper),
       'conclusions':['mu_pp>225','W_pp<-8000','V_q,pp<-8000*q^2',
                      'unique edge maximizer on new rectangle by PREFIX660 and PREFIX661'],
       'status':'AUTHOR_ANALYTIC_PROOF_AND_EXACT_BRC_RECURRENCE_CHECK/UNREVIEWED/NOT_ADMITTED'}
    with open('PREFIX666_results.json','w') as f:json.dump(out,f,indent=2)
    print('SUCCESS',len(rows))
if __name__=='__main__': main()
