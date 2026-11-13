#!/usr/bin/env python3
"""PREFIX-667: exact native BRC first-stop variance certificate, p in [0,1/64]."""
from PREFIX666_experiment import build, N, Q
from PREFIX666_certificate import kernel
from fractions import Fraction as F
from math import comb
import json

DELTA = F(1,4096)
EPS = F(1,64)

def setup(rows):
    df=[]
    for n in range(N):
        v=[F(rows[n].get(k,0),comb(n,k)) for k in range(n+1)]
        z=[v]
        for d in range(1,4):
            z.append([z[-1][k+1]-z[-1][k] for k in range(len(z[-1])-1)])
        df.append(z)
    return df

def eval_derivative(df,p,d):
    out=[]
    for n in range(N):
        if n<d:
            out.append(F(0));continue
        m=n-d
        fall=1
        for i in range(d):fall*=n-i
        out.append(fall*sum((comb(m,k)*v*p**k*(1-p)**(m-k)
                             for k,v in enumerate(df[n][d]) if v),F()))
    return out

def bound_derivative(df,a,b,d):
    out=[]
    for n in range(N):
        if n<d:
            out.append(F(0));continue
        m=n-d
        fall=1
        for i in range(d):fall*=n-i
        out.append(fall*sum((comb(m,k)*abs(v)*b**k*(1-a)**(m-k)
                             for k,v in enumerate(df[n][d]) if v),F()))
    return out

def certify():
    rows=build()
    df=setup(rows)
    aa,bb,az,bz,tt=kernel(rows)
    assert len(rows)==190 and not rows[-1]
    B1_global=bound_derivative(df,F(0),EPS,1)
    Cp_global=sum(B1_global,F(0))
    out=[]
    for jj in range(16):
        lo=F(jj,1024);hi=F(jj+1,1024)
        mid=(lo+hi)/2;radius=(hi-lo)/2
        ev0=eval_derivative(df,mid,0)
        ev2=eval_derivative(df,mid,2)
        B1=bound_derivative(df,lo,hi,1)
        B2=bound_derivative(df,lo,hi,2)
        B3=bound_derivative(df,lo,hi,3)
        muQ=sum((aa[n]*ev0[n] for n in range(N)),sum(tt,F(0)))
        mppQ=sum((aa[n]*ev2[n] for n in range(N)),F(0))
        hppQ=sum((bb[n]*ev2[n] for n in range(N)),F(0))
        mppzQ=sum((az[n]*ev2[n] for n in range(N)),F(0))
        hppzQ=sum((bz[n]*ev2[n] for n in range(N)),F(0))
        z2mu=sum((2*(n+1)*(n+2)*B2[n] for n in range(N)),F(0))
        z2h=sum((2*(n+1)*(n+2)*(n+3)*B2[n] for n in range(N)),F(0))
        mu_p_err=radius*sum((aa[n]*B1[n] for n in range(N)),F(0))
        mu3err=radius*sum((aa[n]*B3[n] for n in range(N)),F(0))
        h3err=radius*sum((bb[n]*B3[n] for n in range(N)),F(0))
        mu3zerr=radius*sum((abs(az[n])*B3[n] for n in range(N)),F(0))
        h3zerr=radius*sum((abs(bz[n])*B3[n] for n in range(N)),F(0))
        # Global B1 is essential: integration in mu_z runs from p=0 to p.
        mu_lower=muQ-mu_p_err-DELTA*(3969+21*hi*Cp_global)
        mupp_lower=mppQ-mu3err-DELTA*(abs(mppzQ)+mu3zerr)-DELTA**2*z2mu/2
        hpp_upper=hppQ+h3err+DELTA*(abs(hppzQ)+h3zerr)+DELTA**2*z2h/2
        wpp_upper=2*hpp_upper-2*mu_lower*mupp_lower
        assert mu_lower>88 and mupp_lower>200
        assert hpp_upper<24000 and wpp_upper<-8000
        out.append(dict(p_lo=str(lo),p_hi=str(hi),
                        mu_lower=float(mu_lower),mupp_lower=float(mupp_lower),
                        hpp_upper=float(hpp_upper),wpp_upper=float(wpp_upper),
                        exact_tests_pass=True))
        print("interval",str(lo),str(hi),
              "muL",float(mu_lower),"muppL",float(mupp_lower),
              "hppU",float(hpp_upper),"wppU",float(wpp_upper),flush=True)
    with open("PREFIX667_interval_results.json","w") as f:
        json.dump(dict(schema="PREFIX667_CURVATURE_1_64_SUBDIVIDED_EXACT_V1",
                       source_pin="f42f2906d77f24085c123f3ccfe9667d41caa96d",
                       certificate_kind="Fraction exact comparison; decimal output only diagnostics",
                       segments=out),f,indent=2)
    print("ALL_INTERVALS_CERTIFIED",len(out))

if __name__=="__main__":
    certify()
