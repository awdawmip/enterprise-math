#!/usr/bin/env python3
"""Author-side independent check of frozen first-jet reduction; not native D25."""
from math import comb
from d25_finite_rational_green_eval_20261031 import primes, jets, evaluation, exact_mod_check


def jet_coefficients(p, power=3):
    mod=p**power; l=(p-1)//6; inv6=pow(6,-1,mod); inv3=pow(3,-1,mod)
    u,v,w=[1],[0],[0]; x,y,z=1,0,0
    for k in range(1,p):
        a,b=k-1-l,k-1-2*l
        a0=x*a%mod; a1=(y*a+x*inv6)%mod; a2=(z*a+y*inv6)%mod
        inv=pow(k*k,-1,mod)
        x=a0*b*inv%mod; y=(a1*b+a0*inv3)*inv%mod
        z=(a2*b+a1*inv3)*inv%mod
        u.append(x);v.append(y);w.append(z)
    return u,v,w


def original_A(p):
    mod=p**3
    return sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod) for n in range(p)) %mod


def check(p):
    l=(p-1)//6; mod=p**3
    u,v,w=jet_coefficients(p)
    z=pow(2,-1,mod)
    j0=evaluation(u,z,mod);j1=evaluation(v,z,mod)
    j2=evaluation(w,z,mod)
    theta0=evaluation([i*u[i] for i in range(p)],z,mod)
    theta1=evaluation([i*v[i] for i in range(p)],z,mod)
    assert j0%p==0,('target J0 mod p',p,j0%p)
    L0=(j0//p+j1)%(p*p)
    N0=(j0+12*theta0)%(p*p)
    N1=(j1+12*theta1)%p
    assert (L0*N0-1)%p==0,('prior first-digit theorem',p)
    carry=((L0*N0-1)%(p*p))//p
    Phi=exact_mod_check(p)[3]
    signedR=exact_mod_check(p)[5]
    j2N0=j2*N0%p
    transf=-12*pow(2,-3*l,p)*Phi%p
    assert j2N0==transf,('target Green bridge',p,j2N0,transf)
    four=(carry+L0*N1+j2N0-signedR)%p
    replaced=(carry+L0*N1+transf-signedR)%p
    assert four==replaced
    a=original_A(p)
    assert (a-p)%(p*p)==0,('original first digit',p)
    actual=((a-p)%(p**3))//(p*p)
    assert actual==replaced,('orig source congruence',p,actual,replaced)
    return (p,carry,L0*N1%p,j2N0,transf,signedR,replaced)


def main():
    results=[check(p) for p in primes(500) if p%24 in (13,19)]
    assert all(x[-1]==0 for x in results)
    print('target primes 13,19 mod24 <=500:',len(results))
    print('anchors (p,carry,firstjet,secondjet,finiteGreen,signedR,fullresidual):',
          [x for x in results if x[0] in (13,19,37,67,373)])
    print('PASS_D25_FIRST_JET_REDUCTION_ORIGINAL_216_EXACT')

if __name__=='__main__':main()
