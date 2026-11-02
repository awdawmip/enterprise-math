#!/usr/bin/env python3
"""D25: exact CM quotient-square repair for the second p-adic digit.

Uses the already-published original mother-observer validator in the same
research_notes/portable_direct directory, without modifying its scientific
inputs.  New quotient/gauge ports use mod p^2; the parent divided
observer also requires the ordinary Gauss root modulo p^3.
Author-side research certificate only; no native H0/B0 computation.
"""
from __future__ import annotations
from math import comb
import json
import argparse
from pathlib import Path
from d25_ordinary_second_jet_checker_20261102 import one, primes


def product_poly(a,b,M):
    out=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): out[i+j]=(out[i+j]+ai*bj)%M
    return out


def new_port(p, include_direct_pair=False):
    assert p>3 and p%6==1
    m=(p-1)//6
    M=p*p
    inv=[0]+[pow(j,-1,M) for j in range(1,2*m+2)]
    inv2=inv[2]
    beta=[comb(m,k)*comb(2*m,k)*pow(inv2,k,M)%M for k in range(m+1)]
    eps=sum(beta)%M
    J=sum(k*bk for k,bk in enumerate(beta))%M
    H=[0]*(2*m+1);H2=[0]*(2*m+1)
    for k in range(1,2*m+1):
        H[k]=(H[k-1]+inv[k])%M
        H2[k]=(H2[k-1]+inv[k]*inv[k])%M
    C=sum(beta[k]*H[k] for k in range(m+1))%M
    Cth=sum(k*beta[k]*H[k] for k in range(m+1))%M
    # The exact polynomial quotient (Y(t)-Y(1))/(1-t).
    tail=0
    Q=[0]*m
    for k in range(m-1,-1,-1):
        tail=(tail+beta[k+1])%M
        Q[k]=-tail%M
    assert (eps+Q[0])%M==beta[0]
    assert (sum(Q)+J)%M==0
    for k in range(1,m):
        assert (Q[k]-Q[k-1])%M==beta[k]
    assert (-Q[-1])%M==beta[m]
    sq=product_poly(Q,Q,M)
    integral=sum(sk*(5*inv[k+1]+inv[k+2]) for k,sk in enumerate(sq))%M
    conv=product_poly(beta,beta,M)
    g=[(1+6*k)*v%M for k,v in enumerate(conv)]
    H1_original=sum(g[k]*H[k] for k in range(2*m+1))%M
    H2_original=sum(g[k]*(9*H[k]**2-5*H2[k]) for k in range(2*m+1))%M
    correction=(2*eps*(C+6*Cth))%M
    assert (integral+correction)%M==H1_original,(p,'H1 exact quotient-square repair')
    # First-order displacement of the *deformed* Gauss square, which enters
    # the actual frozen Clausen correction in the original source formula.
    Cpoly=[beta[k]*H[k]%M for k in range(m+1)]
    Pc=product_poly(beta,Cpoly,M)
    Tdef=sum((1+6*k)*Pc[k]*H[k] for k in range(2*m+1))%p
    # Independent terminating deformed Gauss recurrence (not derived from
    # the first-order expansion) tests the deformation correction directly.
    dcoef=[1]
    for k in range(m):
        dcoef.append((dcoef[-1]*(k-m)*(k-2*m)*inv[k+1]*
                     pow((k+1-p*inv2)%M,-1,M)*inv2)%M)
    assert all(dcoef[k]==beta[k]*(1+p*inv2*H[k])%M for k in range(m+1))
    dconv=product_poly(dcoef,dcoef,M)
    H1_deformed=sum((1+6*k)*dconv[k]*H[k] for k in range(2*m+1))%M
    assert H1_deformed==(H1_original+p*Tdef)%M,(p,'deformed-first-port direct')
    # An independent degree-<p double-integral representation of H2.
    tail2=0
    h2_square=0;h2_diag=0;prefix_inverse=0
    tails=[0]*(2*m)
    for j in range(2*m-1,-1,-1):
        tail2=(tail2+g[j+1])%M
        tails[j]=tail2
    for j in range(2*m):
        h2_square=(h2_square+tails[j]*(inv[j+1]**2+2*inv[j+1]*prefix_inverse))%M
        h2_diag=(h2_diag+tails[j]*inv[j+1]**2)%M
        prefix_inverse=(prefix_inverse+inv[j+1])%M
    assert (9*h2_square-5*h2_diag)%M==H2_original,(p,'H2 exact double-integral tail')
    if include_direct_pair:
        Xi_direct=sum((1+6*(i+j))*beta[i]*beta[j]*(H[i+j]-H[i]-H[j])
                      for i in range(m+1) for j in range(m+1))%p
        assert Xi_direct==(H1_original-12*J*C)%p,(p,'ordered source Xi')
    out={'p':p,'m':m,'epsilon_mod_p2':eps,'J_mod_p':J%p,'C_mod_p':C%p,
         'Ctheta_mod_p':Cth%p,'H1_ordinary_mod_p2':H1_original,'H1_deformed_mod_p2':H1_deformed,
         'integral_mod_p2':integral,'repair_mod_p2':correction,
         'H2_mod_p':H2_original%p,'H2_bivariate_mod_p':(9*h2_square-5*h2_diag)%p,
         'CM_root':eps%p==0,'deformation_weighted_cross_mod_p':Tdef}
    if eps%p==0:
        eps_full=sum(comb(m,k)*comb(2*m,k)*pow(pow(2,-1,p**3),k,p**3) for k in range(m+1))%(p**3)
        assert eps_full%M==eps
        c=(eps_full//p)%(p*p)
        assert correction%p==0
        prior=one(p,check_direct=p in (13,19,37,373,1171))
        A=(c+inv2*C)%M
        # The same band A1+B1 is consumed from the published original checker.
        A1=prior['A1'];B1=prior['B1']
        Nflat=(12*J*A-3*inv2*integral+A1+B1-1)%M
        assert Nflat%p==0,(p,'flat bracket divisibility')
        root_repair=(-3*c*(C+6*Cth))%p
        deformation_repair=(-3*inv2*Tdef)%p
        corrected=(root_repair+deformation_repair)%p
        assert (Nflat//p+corrected)%p==prior['first_bracket_divided'],(p,'mother-source repair',Nflat//p,root_repair,deformation_repair,prior['first_bracket_divided'])
        quad=(A*A+6*A*Cth+3*inv2*J*prior['D2'])%p
        gauge=H2_original*pow(8,-1,p)%p
        parent=(Nflat//p+corrected+quad+gauge+prior['three_band_second'])%p
        assert parent==prior['new_LIFT_digit']==0,(p,'original scalar target finite check')
        out.update({'c_mod_p':c%p,'c_lift_mod_p2':c,'flat_bracket_divided':Nflat//p,
                    'quotient_repair_digit':corrected,'root_repair_digit':root_repair,
                    'deformation_repair_digit':deformation_repair,'gauss_quadratic':quad,
                    'clausen_h2_eighth':gauge,'three_band_second':prior['three_band_second'],
                    'new_LIFT_digit':parent,'old_N_divided':prior['first_bracket_divided']})
    else:
        out['non_CM_control_only']=True
    return out


def run(limit=3000,output='d25_cm_quotient_h1_second_digit_20261102.check.json'):
    ps=[p for p in primes(limit) if p%24 in (13,19)]
    cases=[new_port(p,include_direct_pair=p in (13,19,37,373,1171)) for p in ps]
    nc=new_port(7)
    assert not nc['CM_root']
    summary={'schema':'D25_CM_QUOTIENT_SQUARE_P2_FAITHFUL_PORT_V1',
             'source_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
             'date':'2026-11-02','evidence_class':'AUTHOR_DERIVED_EXACT_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED',
             'target_primes_max':limit,'target_primes_count':len(cases),'all_tests_passed':True,
             'non_CM_control':nc,'focus':{str(x['p']):x for x in cases if x['p'] in (13,19,37,373,1171)},
             'repair_nonzero_count':sum(x['quotient_repair_digit']!=0 for x in cases),
             'all_cases':cases}
    Path(output).write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')
    return summary

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--limit',type=int,default=3000)
    ap.add_argument('--output',default='d25_cm_quotient_h1_second_digit_20261102.check.json')
    a=ap.parse_args()
    r=run(a.limit,a.output)
    print(json.dumps({'count':r['target_primes_count'],'all_tests_passed':r['all_tests_passed'],
                      'repair_nonzero_count':r['repair_nonzero_count'],
                      'focus':{k:{z:v for z,v in x.items() if z in
                       ('p','c_mod_p','c_lift_mod_p2','H1_ordinary_mod_p2','H1_deformed_mod_p2','integral_mod_p2','repair_mod_p2','flat_bracket_divided','quotient_repair_digit','gauss_quadratic','clausen_h2_eighth','three_band_second','new_LIFT_digit')}
                       for k,x in r['focus'].items()}},ensure_ascii=False))
