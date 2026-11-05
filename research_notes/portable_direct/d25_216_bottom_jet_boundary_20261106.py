#!/usr/bin/env python3
"""Exact 0/1/2-jet finite boundary identities in original 216 bottom band.
Portable author check; this is not the native p=373 H0/B0 divided-power experiment.
"""
import json
from fractions import Fraction as F


def primes(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    for k in range(2, int(n**0.5)+1):
        if a[k]:
            for t in range(k*k,n+1,k):
                a[t]=False
    return [p for p in range(7,n+1) if a[p] and p%6==1]


def polys(n,m,inv2,inv3,inv9):
    M0 = (n-3*m)*(n-2*m)*(n-4*m)-2*n**3
    M1 = 3*n*n*inv2 - 26*m*n*inv3 +12*m*m
    M2 = 13*n*inv9-4*m
    return M0,M1,M2


def exact_rational(p):
    m=(p-1)//6; c=F(1); L=S=F(0); lhs=[F(0),F(0),F(0)]
    for n in range(2*m+1):
        M0,M1,M2=polys(n,m,F(1,2),F(1,3),F(1,9))
        lhs[0] += c*M0
        lhs[1] += c*(M1-M0*L)
        lhs[2] += c*(M2-2*M1*L+M0*(L*L-S))
        if n==2*m:
            rhs=[F(0), F(2*m*m,3)*c, c*(-F(10*m,9)-F(4*m*m,3)*L)]
            break
        a=F(1,2*(3*m-n));b=F(1,3*(2*m-n));d=F(2,3*(4*m-n))
        L+=a+b+d; S+=a*a+b*b+d*d
        c*=F((n-3*m)*(n-2*m)*(n-4*m),2*(n+1)**3)
    assert lhs==rhs, (p,lhs,rhs)
    return {'p':p,'first_boundary_num':rhs[1].numerator,'first_boundary_den':rhs[1].denominator,
            'second_boundary_num':rhs[2].numerator,'second_boundary_den':rhs[2].denominator}


def modular(p):
    m=(p-1)//6; mod=p**3; inv=lambda d:pow(d%mod,-1,mod)
    inv2,inv3,inv9=inv(2),inv(3),inv(9)
    c=1;L=S=0;sums=[0,0,0]
    for n in range(2*m+1):
        M0,M1,M2=polys(n,m,inv2,inv3,inv9)
        sums[0]=(sums[0]+M0*c)%mod
        sums[1]=(sums[1]+c*(M1-M0*L))%mod
        sums[2]=(sums[2]+c*(M2-2*M1*L+M0*(L*L-S)))%mod
        if n==2*m:
            end=[0,2*m*m*inv3*c%mod,(-10*m*inv9-4*m*m*inv3*L)*c%mod]
            break
        a=inv(2*(3*m-n));b=inv(3*(2*m-n));d=2*inv(3*(4*m-n))%mod
        L=(L+a+b+d)%mod;S=(S+a*a+b*b+d*d)%mod
        c=c*(n-3*m)*(n-2*m)*(n-4*m)*inv(2*(n+1)**3)%mod
    assert sums==end, (p,sums,end)
    return {'p':p,'m':m,'modulus':mod,'zeroth_moment':sums[0],
            'first_boundary':sums[1],'second_boundary':sums[2],
            'last_seed_c_mod_p3':c,'last_L_mod_p3':L}


def main():
    checked=[modular(p) for p in primes(997)]
    exact=[exact_rational(p) for p in (13,19)]
    assert len(checked)==80
    output={'schema':'ENTERPRISE_MATH_D25_BOTTOM_JET_ENDPOINT_V1',
     'classification':'AUTHOR_EXACT_PROOF_FINITE_CHECK_UNREVIEWED_NOT_ADMITTED',
     'scientific_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
     'p_1_mod6_count':80,'prime_ceiling':997,'assertions':'ALL_PASSED',
     'full_exact_rational_primes':exact,
     'selected_modular':[x for x in checked if x['p'] in (13,19,67,139,373)]}
    with open('20261106_onhour_d25_bottom_216_jet_endpoint_results.json','w') as f:
        json.dump(output,f,indent=2)
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
