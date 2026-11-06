#!/usr/bin/env python3
"""Author-side exact 216 Clausen triangular boundary check. Python stdlib only.
No Source-native H0/B0 operation or mathematical review is performed.
"""
from fractions import Fraction
from math import factorial, isqrt
import json


def primes_up_to(N):
    for p in range(5, N + 1):
        if all(p % q for q in range(2, isqrt(p) + 1)):
            yield p


def a_rational(n):
    return Fraction(factorial(2*n)*factorial(3*n), 216**n*factorial(n)**5)


def d_rational(n):
    return Fraction(
        __import__('math').prod((6*k+1)*(3*k+1) for k in range(n)),
        36**n * factorial(n)**2)


def check_small_clausen(n_max=8):
    ds=[d_rational(n) for n in range(n_max+1)]
    for n in range(n_max+1):
        assert sum(ds[i]*ds[n-i] for i in range(n+1)) == a_rational(n), n


def run_prime(p):
    assert p % 6 == 1
    m=(p-1)//6
    M=p**3
    d=[1]
    for n in range(1,p):
        d.append((d[-1]*(6*n-5)*(3*n-2)*pow(36*n*n,-1,M)) % M)
    a=1; W=1
    for n in range(1,p):
        a=(a*(2*n-1)*(3*n-2)*(3*n-1)*pow(36*n**3,-1,M))%M
        W=(W+(6*n+1)*a)%M
    S=sum(d)%M; T=sum(k*d[k] for k in range(p))%M
    full=(S*S+12*S*T)%M
    def e(r):
        den=1
        for s in range(1,r+1):
            den=(den*(1-6*s)*(1-3*s))%p
        return pow(36,r-1,p)*factorial(r-1)**2*pow(den,-1,p)%p
    J=0
    for i in range(1,m+1):
        for r in range(1,i+1):
            assert (d[p-r]//(p*p))%p == e(r), ('reflection',p,i,r)
            J=(J+(1+6*(i-r))*d[i]*e(r))%p
    corrected=(full-2*p*p*J)%M
    assert corrected==W, ('triangle-correction',p,corrected,W)
    if p in (7,13,19):
        cp=[sum(d[i]*d[n-i] for i in range(n+1))%M for n in range(p)]
        direct=sum((6*n+1)*cp[n] for n in range(p))%M
        assert direct==W, ('convolution',p,direct,W)
    chi=1 if p%3==1 else -1
    assert W==p*chi%M,('old-congruence-regression',p,W)
    return {
        'p':p,'m':m,'class_mod_24':p%24,
        'W_mod_p3':W,'S_mod_p':S%p,
        'S_plus_12T_mod_p':(S+12*T)%p,
        'S2_plus_12ST_mod_p3':full,
        'J_mod_p':J,'boundary_2J_mod_p':(2*J)%p,
        'boundary_nonzero':(2*J)%p!=0,
        'corrected_mod_p3':corrected,
        'S_divisible_by_p':S%p==0,
    }


def main():
    check_small_clausen(8)
    rows=[run_prime(p) for p in primes_up_to(997) if p%6==1]
    targets=[r for r in rows if r['class_mod_24'] in (13,19)]
    other=[r for r in rows if r['class_mod_24'] not in (13,19)]
    assert len(rows)==80 and len(targets)==45,(len(rows),len(targets))
    assert all(r['S_divisible_by_p'] for r in targets)
    assert all(r['S_plus_12T_mod_p']==0 for r in other)
    summary={
        'status':'EXACT_FINITE_EXECUTED; UNIVERSAL_CLAUSEN_TRIANGLE_IDENTITY_HAND_PROVED; UNREVIEWED_NOT_ADMITTED',
        'source':'original_216_coefficients; finite_p_adic_clausen; no_native_CM',
        'prime_range':'p prime, 7<=p<=997 and p mod6=1',
        'prime_count':len(rows), 'frozen_target_count':len(targets),
        'clausen_exact_rational_coefficients_tested':list(range(9)),
        'correction_assertion_failures':0,'reflection_assertion_failures':0,
        'direct_convolution_primes':[7,13,19],
        'target_S_mod_p_zero_observed_count':sum(r['S_divisible_by_p'] for r in targets),
        'other_S_plus_12T_mod_p_zero_observed_count':sum(r['S_plus_12T_mod_p']==0 for r in other),
        'nonzero_boundary_target_count':sum(r['boundary_nonzero'] for r in targets),
        'examples':[r for r in rows if r['p'] in (7,13,19,31,37,43,67,139,373,997)],
        'all_rows':rows,
        'limits':'The p mod 24 first-factor split is a finite observation, NOT a uniform theorem. The 216 supercongruence was numerically checked here, not proved. Native H0/B0 is NOT_RUN.'
    }
    with open('20261106_d25_clausen_triangle_results.json','w',encoding='utf-8') as f:
        json.dump(summary,f,ensure_ascii=False,indent=2)
    print(json.dumps({k:v for k,v in summary.items() if k!='all_rows'},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
