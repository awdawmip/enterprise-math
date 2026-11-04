#!/usr/bin/env python3
"""Exact modular checks for the short-Jacobi/harmonic D25 port.
Independent baselines: Gauss rational recurrence; terminating binomial coefficients;
Jacobi polynomial at 5/4. Only prime-to-p modular divisions are performed.
This is a finite exact checker, not a universal proof or native experiment.
"""
from math import comb, isqrt

def primes(n):
    for p in range(5,n+1):
        if all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def check(p):
    assert p%8==5
    q=(p-5)//8; m=p*p
    inv9=pow(9,-1,m); inv8=pow(8,-1,m)
    inv576=pow(576,-1,m)
    orig=jac=1
    s_orig=d_orig=s_j=d_j=k_sum=k_der=0
    h1=h2=0
    jac_coeff=[]; harm_coeff=[]
    for j in range(q+1):
        if j:
            orig=orig*(8*j-3)*(8*j-1)*inv576*pow(j*j,-1,m)%m
            jac=jac*(q-j+1)*(3*q+2-j)*inv9*pow(j*j,-1,m)%m
            h1=(h1+pow(q-j+1,-1,p))%p
            h2=(h2+pow(3*q+2-j,-1,p))%p
        hj=(h1+3*h2)*pow(8,-1,p)%p
        kin=(jac%p)*hj%p
        jac_coeff.append(jac%p); harm_coeff.append(kin)
        assert orig==(jac*(1-p*hj))%m,(p,q,j,orig,jac,hj)
        s_orig=(s_orig+orig)%m
        d_orig=(d_orig+j*orig)%m
        s_j=(s_j+jac)%m
        d_j=(d_j+j*jac)%m
        k_sum=(k_sum+kin)%p
        k_der=(k_der+j*kin)%p
    assert s_orig==(s_j-p*k_sum)%m and d_orig==(d_j-p*k_der)%m
    # Inhomogeneous reduced Picard-Fuchs equation for K at every coefficient.
    # D0 = theta^2 - z/9 (theta-q)(theta-(3q+1));
    # D0 K + z/72 (4theta-6q-1)J = c_q*z^(q+1)/288 mod p.
    inv9p=pow(9,-1,p); inv72=pow(72,-1,p); inv288=pow(288,-1,p)
    for n in range(q+2):
        value=(n*n*harm_coeff[n])%p if n<=q else 0
        if n>=1:
            term=((n-1-q)*(n-3*q-2))%p
            value=(value-inv9p*term*harm_coeff[n-1])%p
            value=(value+inv72*(4*(n-1)-6*q-1)*jac_coeff[n-1])%p
        expected=(jac_coeff[q]*inv288)%p if n==q+1 else 0
        assert value==expected,(p,q,n,value,expected)
    # At 5/4, each Jacobi monomial is binom(q,m)*binom(3q+1,q-m)*(1/8)^(q-m)*(9/8)^m.
    pj=dpj=0
    for a in range(q+1):
        term=comb(q,a)*comb(3*q+1,q-a)*pow(9,a,m)*pow(inv8,q,m)%m
        pj=(pj+term)%m
        dpj=(dpj+term*(4*(q-a)+4*a*pow(9,-1,m)))%m
    u=pow(8*inv9%m,q,m)
    assert s_j==u*pj%m
    assert d_j==u*(9*pow(32,-1,m)*dpj-q*pow(8,-1,m)*pj)%m
    # A prime-field second-jet relation for J(z) at z=1 from terminating Gauss ODE.
    # J(z) = sum binomial coefficients (z/9)^j ; J''(1) computed using j(j-1).
    b=1; d2=0
    for j in range(1,q+1):
        b=b*(q-j+1)*(3*q+2-j)*inv9*pow(j*j,-1,m)%m
        d2=(d2+j*(j-1)*b)%m
    # At z=1, 8 J'' + (9+4q) J' - q(3q+1) J = 0
    assert (8*d2+(9+4*q)*d_j-q*(3*q+1)*s_j)%m==0
    # Exact p-adic short-C endpoint forcing, evaluated at z=1:
    # 8C'' + (13/2)C' - (35/64)C = -p(p+2)c_q/64.
    # Reduce rational coefficients after multiplying by 64.
    orig=1; cd2=0
    for j in range(1,q+1):
        orig=orig*(8*j-3)*(8*j-1)*inv576*pow(j*j,-1,m)%m
        cd2=(cd2+j*(j-1)*orig)%m
    lhs=(512*cd2+416*d_orig-35*s_orig)%m
    rhs=(-p*(p+2)*orig)%m
    assert lhs==rhs,(p,lhs,rhs)
    if q%3==0: assert d_j%p==0,(p,q,d_j%p)
    if q%3==1: assert s_j%p==0,(p,q,s_j%p)
    return (p,q,s_j%p,d_j%p,k_sum,k_der,s_orig%p**2,d_orig%p**2,pj%p,dpj%p)

if __name__=='__main__':
    seen=[]; checks=0
    for p in primes(5000):
        if p%8==5:
            rec=check(p); seen.append(rec); checks+=(p-5)//8+1
            if p in (5,13,29,37,53,61,373):print('WITNESS',rec)
    print(f'PASS short Jacobi/harmonic primes={len(seen)} unit_coefficients={checks} Jacobi_and_endpoint_checks={len(seen)}')
