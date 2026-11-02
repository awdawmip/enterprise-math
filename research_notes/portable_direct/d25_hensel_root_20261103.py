#!/usr/bin/env python3
"""D25 author-side exact modular arithmetic. Not a native H0/B0 execution.

Two independently defined polynomial sources: the terminating Gauss G and
original 216/Clausen F. Preserves integer p-adic lifts and local root digits.
"""
import json
from math import isqrt


def primes(n):
    s=bytearray(b'\1')*(n+1);s[:2]=b'\0\0'
    for q in range(2,isqrt(n)+1):
        if s[q]:s[q*q::q]=b'\0'*((n-q*q)//q+1)
    return [p for p in range(7,n+1) if s[p] and p%24 in (13,19)]


def gauss_coefficients(p, exponent):
    mod=p**exponent
    vals=[1]
    for k in range(p-1):
        den=18*(k+1)*(k+1)
        vals.append(vals[-1]*(6*k+1)*(3*k+1)*pow(den,-1,mod)%mod)
    return vals


def original_coefficients(p, exponent):
    mod=p**exponent
    vals=[1]
    for k in range(p-1):
        den=18*(k+1)**3
        vals.append(vals[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(den,-1,mod)%mod)
    return vals


def ell_coefficients(p, exponent):
    r=(p-1)//6;mod=p**exponent
    vals=[1]
    for k in range(r):
        vals.append(vals[-1]*(r-k)*(2*r-k)*pow((k+1)**2,-1,mod)%mod)
    return vals


def jets(vals,z,mod):
    f=d=dd=0
    for c in reversed(vals):
        dd=(dd*z+2*d)%mod
        d=(d*z+f)%mod
        f=(f*z+c)%mod
    return f,d,dd


def check(p, higher=False):
    m=p*p; z0=pow(2,-1,m)
    ell=ell_coefficients(p,2)
    G=gauss_coefficients(p,2)
    lv,ld,_=jets(ell,z0,m)
    gv,gd,_=jets(G,z0,m)
    assert lv%p==gv%p==0 and gd%p==ld%p
    j=(z0*ld)%p
    assert j!=0
    g=(lv//p)%p; q=((gv-lv)%m//p)%p; h=(gv//p)%p
    assert (g+q)%p==h
    omega=(-q*j)%p
    dell=(-g*pow(2*j,-1,p))%p
    dG=(-h*pow(2*j,-1,p))%p
    dpred=(-pow(24*j*j,-1,p))%p
    alpha=(z0+p*dell)%m
    beta=(z0+p*dG)%m
    beta_pred=(z0+p*dpred)%m
    assert jets(ell,alpha,m)[0]==0
    assert jets(G,beta,m)[0]==0
    assert (dG-dell)%p==omega*pow(2*j*j,-1,p)%p
    assert ((12*j*h-1)%p==0)==(jets(G,beta_pred,m)[0]==0)
    assert (12*j*h-1)%p==0,('second-carry finite counterexample',p)
    row={"p":p,"r":(p-1)//6,"j":j,"g":g,"Q_half":q,
         "Omega_half":omega,"G_half_div_p":h,"ell_root_delta":dell,
         "Gauss_root_delta":dG,"predicted_delta":dpred,
         "beta_mod_p2":beta,"Hensel_test":"PASS","first_digit_target_finite_test":"PASS"}
    if higher:
        m3=p**3;z03=pow(2,-1,m3)
        G3=gauss_coefficients(p,3)
        F3=original_coefficients(p,3)
        g0,g1,g2=jets(G3,z03,m3)
        f0,f1,_=jets(F3,z03,m3)
        assert g0%p==0 and g1%p==2*j%p
        beta1=(z03+p*dG)%m3
        root_res=jets(G3,beta1,m3)[0]
        assert root_res%p**2==0
        eps=(-((root_res//(p*p))%p)*pow(g1,-1,p))%p
        beta2=(beta1+p*p*eps)%m3
        assert jets(G3,beta2,m3)[0]==0
        mod2=p*p
        d=g1%mod2;e=g2%p
        squared=(g0*g0+6*g0*g1)%m3
        assert squared%p==0
        coeff=(-6*dG*d*d + p*(dG*dG*d*d-6*eps*d*d-3*dG*dG*e*d))%mod2
        assert (squared//p)%mod2 == coeff,(p,'second-order polynomial-root formula')
        simplified=(-6*dG*d*d+p*(4*dG*dG*d*d-6*eps*d*d))%mod2
        assert (d+e)%p==0 and coeff==simplified
        W=(f0+3*f1)%m3
        assert W%p==0
        difference=(W-squared)%m3
        assert difference%(p*p)==0,(p,'Clausen defect observer')
        E=(difference//(p*p))%p
        assert W//p%mod2==(coeff+p*E)%mod2
        row.update({"Gauss_root_second_delta":eps,"beta_mod_p3":beta2,
                    "Gprime_mod_p2":d,"Gsecond_mod_p":e,
                    "weighted_Gsquare_div_p_mod_p2":squared//p,
                    "root_jet_reconstruction":coeff,
                    "Clausen_defect_observer":E,
                    "original_W_div_p_mod_p2":W//p,
                    "original_W_mod_p3":W,
                    "p3_second_digit":(W//p-1)//p%p if (W//p)%p==1 else None,
                    "p3_original_source_check":"PASS"})
    return row


def main():
    points=[13,19,37,43,73,181,373,1171]
    higher={p for p in points if p%24 in (13,19)}
    records=[check(p,higher=(p in higher)) for p in primes(10000)]
    out={"schema":"D25_GAUSS_HENSEL_SECOND_CARRY_COORDINATE_V1",
         "research_lane":"chatgpt-research-hourly-enterprise-math-20260923",
         "frozen_science_pin":"c47e13e4aba0e006366f989d6334d443f6333ae3",
         "range":"all primes 7<=p<=10000 and p mod24 in {13,19}",
         "checked":len(records),"first_order":"PASS",
         "second_order_cases":[x['p'] for x in records if 'Gauss_root_second_delta' in x],
         "second_order":"PASS",
         "samples":[x for x in records if x['p'] in points],
         "universal_second_carry":"OPEN",
         "native_H0_B0":"NOT_EXECUTED","admission":"UNREVIEWED_NOT_ADMITTED"}
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
