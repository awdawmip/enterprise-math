#!/usr/bin/env python3
"""Exact modular checks of a sourced ordered-pair / quotient-square bridge.

This is author-side mathematical evidence, not an authenticated Source run.
No external dependencies. All coefficients are in Z/p^2Z; no floats.
"""
from math import isqrt
import json


def primes_up_to(limit):
    result=[]
    for n in range(5,limit+1):
        if all(n%d for d in range(2,isqrt(n)+1)):
            result.append(n)
    return result


def verify_prime(p):
    assert p>=7 and p%6==1
    m=(p-1)//6
    M=p*p
    inv=[0]+[pow(a,-1,M) for a in range(1,2*m+3)]
    H=[0]*(2*m+2)
    for i in range(1,2*m+2):
        H[i]=(H[i-1]+inv[i])%M
    beta=[1]
    d=[1]
    for r in range(m):
        num=(m-r)*(2*m-r)
        beta.append(beta[-1]*num*pow(2*(r+1)**2,-1,M)%M)
        d.append(d[-1]*num*pow((r+1)*(2*(r+1)-p),-1,M)%M)
    eps=sum(beta)%M
    J=sum(i*beta[i] for i in range(m+1))%M
    C=sum(beta[i]*H[i] for i in range(m+1))%M
    Ctheta=sum(i*beta[i]*H[i] for i in range(m+1))%M

    # Q=(Y-epsilon)/(1-t), coefficients are -strict upper beta tails.
    q=[];tail=0
    for r in range(m,0,-1):
        tail=(tail+beta[r])%M
        q.append((-tail)%M)
    q=q[::-1]
    assert sum(q)%M == (-J)%M

    # Independent direct pair observer: preserve each (i,j), its sign and H_{i+j}.
    Xi=0
    Tdef=0
    Hd=0
    for i in range(m+1):
        for j in range(m+1):
            k=i+j
            weight=1+6*k
            Xi=(Xi+beta[i]*beta[j]*weight*(H[k]-H[i]-H[j]))%M
            Hd=(Hd+d[i]*d[j]*weight*H[k])%M
            Tdef=(Tdef+beta[i]*beta[j]*H[j]*weight*H[k])%M

    # Independent quotient-square path: convolution, not reusing Xi.
    qc=[0]*(2*m-1)
    for i in range(m):
        for j in range(m):
            qc[i+j]=(qc[i+j]+q[i]*q[j])%M
    integral=sum(qc[k]*(5*inv[k+1]+inv[k+2]) for k in range(2*m-1))%M
    xi_from_q=(integral-12*J*C)%M
    assert Xi==xi_from_q,(p,'Xi mismatch',Xi,xi_from_q)

    root=(2*eps*(C+6*Ctheta))%M
    repair=(p*Tdef)%M
    predicted_deformed=(integral+root+repair)%M
    assert predicted_deformed==Hd,(p,'deformation mismatch',predicted_deformed,Hd)
    predicted_deformed_joint=(Xi+12*J*C+root+repair)%M
    assert predicted_deformed_joint==Hd

    # Native/p-adic domain check: no denominator index >= p used.
    assert 2*m+1<p
    return {
        'p':p, 'm':m,'modulus':M,
        'epsilon_mod_p':eps%p, 'J_mod_p':J%p,'C_mod_p':C%p,
        'xi_mod_p2':Xi, 'xi_mod_p':Xi%p,
        'quotient_square_integral_mod_p2':integral,
        'rank_one_correction_12JC_mod_p2':12*J*C%M,
        'deformed_H1_mod_p2':Hd,
        'root_repair_mod_p2':root,
        'parameter_repair_mod_p2':repair,
        'joint_bridge_holds':True,
        'deformation_bridge_holds':True,
    }


def main():
    ps=[p for p in primes_up_to(3000) if p%24 in (13,19)]
    checked=[verify_prime(p) for p in ps]
    controls=[verify_prime(p) for p in [7,31,43] if p not in ps]
    record={
        'schema':'D25_AUTHOR_EXACT_JOINT_QUOTIENT_BRIDGE_CHECK_V1',
        'status':'EXECUTED_AUTHOR_SIDE_ONLY_UNREVIEWED_NOT_ADMITTED',
        'frozen_scientific_input':'c47e13e4aba0e006366f989d6334d443f6333ae3',
        'target_prime_bound':3000,
        'target_prime_count':len(ps),
        'all_target_assertions_passed':len(ps)==107,
        'control_prime_count':len(controls),
        'p13_p19_p373':[next(v for v in checked if v['p']==p) for p in (13,19,373)],
        'controls':controls,
        'coverage':'every prime <=3000 in classes 13 or 19 mod 24; all modular equalities at p^2',
        'equations':['Xi = I((5+t)Q^2)-12 J C EXACT',
                     'Hcal1_deformed = Xi+12JC+2epsilon(C+6Ctheta)+p*Tdef mod p^2'],
        'native_H0_B0_executed':False,
        'universal_D25_proved':False,
    }
    print(json.dumps(record,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
