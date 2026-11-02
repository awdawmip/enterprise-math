#!/usr/bin/env python3
"""Exact integer modular replay: D25 original W216 vs Le Lan 2026 Cauchy source.
All inverses have denominators prime to p for indices <p, p>3.
Proof is in companion Markdown; this checker is finite, non-formal evidence.
"""
from math import comb
import json


def primes_upto(n):
    ans=[]
    for p in range(5,n+1):
        if all(p%d for d in range(2,int(p**.5)+1)):
            ans.append(p)
    return ans

def product_mod(a,b,mod,n):
    out=[0]*n
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b[:n-i]):
            out[i+j]=(out[i+j]+x*y)%mod
    return out

def calculate(p):
    mod=p*p
    F=[1]; A=[1]; B=[1]; E=[1]
    for k in range(1,p):
        F.append(F[-1]*(2*k-1)*(3*k-2)*(3*k-1)*pow(18*k**3,-1,mod)%mod)
        A.append(A[-1]*(3*k-2)*(6*k-5)*pow(18*k*k,-1,mod)%mod)
        B.append(B[-1]*(3*k-1)*(6*k-1)*pow(18*k*k,-1,mod)%mod)
        E.append(E[-1]*(2*k-1)*pow(2*k,-1,mod)%mod)
    C=product_mod(A,B,mod,p)
    D=product_mod(E,F,mod,p)
    assert C==D,(p,'Cauchy exact modulo p2')
    M=(p-1)//6
    if p%6==1:
        ell=[comb(M,k)*comb(2*M,k)%p for k in range(M+1)]
        ell2=product_mod(ell,ell,p,p)
        e0=[((-1)**k)*comb((p-1)//2,k)%p for k in range((p+1)//2)]
        rhs=product_mod(e0,ell2,p,p)
        assert [c%p for c in C]==rhs,(p,'full-polynomial mod p')
        # Original F_p = ell_m(z)^2 mod p, coefficientwise.
        assert [f%p for f in F]==ell2,(p,'original Clausen')
    z=pow(2,-1,mod)
    powz=1
    W=LW=thetaW=thetaL=0
    for n in range(p):
        b=F[n]*powz%mod
        cn=C[n]*powz%mod
        W=(W+(6*n+1)*b)%mod
        LW=(LW+(3*n-1)*cn)%mod
        thetaW=(thetaW+n*(6*n+1)*b)%mod
        thetaL=(thetaL+n*(3*n-1)*cn)%mod
        powz=powz*z%mod
    record={'p':p,'W_mod_p2':W,'Cauchy_mod_p2':LW,
            'theta_W_mod_p':thetaW%p,'theta_Cauchy_mod_p':thetaL%p}
    if p%6==1:
        ell_val=sum(ell[k]*pow(pow(2,-1,p),k,p) for k in range(M+1))%p
        record['ell_root_mod_p']=ell_val
        if ell_val==0:
            chi2=pow(2,(p-1)//2,p)
            chi2=-1 if chi2==p-1 else 1
            assert (2*thetaL-chi2*thetaW)%p==0,(p,'twisted signed first-jet transport')
            d_ell=sum(k*ell[k]*pow(pow(2,-1,p),k-1,p) for k in range(1,M+1))%p
            assert d_ell!=0,(p,'root must be simple')
            record['chi2']=chi2
            record['ell_prime_mod_p']=d_ell
            record['signed_jet_discrepancy_over_p_mod_p']=((2*thetaL-chi2*thetaW)%mod)//p
            if chi2==-1:
                # Exact p^2-lift repair with truncation kept explicit.
                el2=[comb(M,k)*comb(2*M,k)%mod for k in range(M+1)]
                L2=product_mod(el2,el2,mod,p)
                e02=[(-1)**k*comb(3*M,k)%mod for k in range(3*M+1)]
                RA=[((F[n]-(L2[n] if n<len(L2) else 0))%mod)//p for n in range(p)]
                RE=[((E[n]-(e02[n] if n<len(e02) else 0))%mod)//p for n in range(p)]
                RC1=product_mod([x%p for x in e02],RA,p,p)
                RC2=product_mod(RE,ell2,p,p)
                RC=[(x+y)%p for x,y in zip(RC1,RC2)]
                Z2=product_mod(e02,L2,mod,p)
                check_RC=[((C[n]-Z2[n])%mod)//p for n in range(p)]
                assert RC==check_RC,(p,'source-preserving correction polynomials')
                ell_value_p2=sum(el2[k]*pow(2,-k,mod) for k in range(M+1))%mod
                assert ell_value_p2%p==0
                g=ell_value_p2//p
                j=sum(k*ell[k]*pow(2,-k,p) for k in range(M+1))%p
                e_at_half=pow(2,-3*M,mod)
                assert (1+e_at_half)%p==0
                delta=((1+e_at_half)%mod)//p
                base=(-6*g*j+12*delta*j*j)%p
                corr=(sum((2*n*(3*n-1)*RC[n]+n*(6*n+1)*RA[n])*pow(2,-n,p)
                          for n in range(p)))%p
                lhs=record['signed_jet_discrepancy_over_p_mod_p']
                assert (base+corr)%p==lhs,(p,'second-digit full source repair',base,corr,lhs)
                record.update({'CM_quotient_g':g,'theta_ell_j':j,'quadratic_multiplier_digit_delta':delta,
                               'base_root_and_multiplier_digit':base,'source_truncation_repair_digit':corr})
    return record


def main():
    targets=[p for p in primes_upto(1000) if p%24 in (13,19)]
    controls=[5,7,11,17,23,31,47]
    cases=sorted(set(targets+controls+[373,1171]))
    rec=[calculate(p) for p in cases]
    for r in rec:
        if r['p']%24 in (13,19):
            assert r['ell_root_mod_p']==0,(r['p'],'CM root required')
            assert r['chi2']==-1
    examples={str(p):next(r for r in rec if r['p']==p) for p in (7,13,19,37,43,373,1171)}
    out={'scope':'original W216 and published 2026 Cauchy product; modular integer arithmetic, no division by p',
         'primes_tested':len(cases),'target_primes_tested':len(targets),
         'full_coefficient_comparisons':sum(c['p'] for c in rec),
         'passed':True, 'examples':examples,
         'status':'AUTHOR-DERIVED; EXACT ALGEBRA; FINITE CHECKED; UNREVIEWED; NOT_ADMITTED; NATIVE_NOT_EXECUTED'}
    print(json.dumps(out,indent=2,ensure_ascii=False))
    with open('/mnt/data/d25_cauchy_signed_jet_check_summary_20261102.json','w') as f:
        json.dump(out,f,indent=2,ensure_ascii=False)
if __name__=='__main__':main()
