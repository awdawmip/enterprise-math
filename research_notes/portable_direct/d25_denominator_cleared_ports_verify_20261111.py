#!/usr/bin/env python3
"""D25 exact integer-lift port checker. Author side, not Source-native admission."""
from math import comb, factorial, isqrt
from fractions import Fraction
import json

SPEC = {
  0: dict(c=5, rho=1,
          d=lambda n:40*(n+1)*(2*n+1),
          a=lambda n:371*n*n+331*n+80,
          b=lambda n:-81*n*n+137*n-60,
          g=lambda n:2*n*n-5*n+3,
          s=lambda n:24*n+5,
          t=lambda n:36*n-25),
  1: dict(c=8, rho=5,
          d=lambda n:64*(n+1)*(2*n+3),
          a=lambda n:648*n*n+1096*n+480,
          b=lambda n:-371*n*n+331*n-80,
          g=lambda n:10*n*n-15*n+5,
          s=lambda n:-40,
          t=lambda n:204*n-35),
}

def integer_lift(m,e,mod=None):
    f=SPEC[e]; c=f['c']
    # U_n=P_n*A_n, T_n=c**n*P_n*B_n, Q_n=c**n*P_n, q_n=c*d_n
    old2,old1,U = 0,0,1
    T,Q,c_power=1-6*e,1,1
    q_old2=q_old1=0
    for n in range(m):
        q=c*f['d'](n)
        N=c*(f['a'](n)*U
             +(f['b'](n)*q_old1*old1 if n>=1 else 0)
             +(f['g'](n)*q_old1*q_old2*old2 if n>=2 else 0))
        if mod: N%=mod
        V=c_power*(f['s'](n+1)*N+f['t'](n+1)*q*U)+f['rho']*q*T
        if mod: V%=mod
        Q*=c*q
        c_power*=c
        if mod: Q%=mod; c_power%=mod
        old2,old1,U=old1,U,N
        T=V
        q_old2,q_old1=q_old1,q
    if mod: return U%mod,T%mod,Q%mod,c_power%mod
    return U,T,Q,c_power

def direct(m,e,mod):
    A=B=0
    for k in range(m+1):
        v=comb(m,k)*comb(2*m+e,k)*pow(pow(2,k,mod),-1,mod)
        A+=v
        B+=(1-6*e+12*k)*v
    return A%mod,B%mod

def primes(N):
    prime=bytearray(b'\x01')*(N+1);prime[:2]=b'\x00\x00'
    for d in range(2,isqrt(N)+1):
        if prime[d]:
            prime[d*d::d]=b'\x00'*((N-d*d)//d+1)
    return [p for p in range(5,N+1) if prime[p]]

def check():
    rational=0
    for e in (0,1):
        for m in range(14):
            A=sum((Fraction(comb(m,k)*comb(2*m+e,k),2**k) for k in range(m+1)),Fraction(0))
            B=sum((Fraction((1-6*e+12*k)*comb(m,k)*comb(2*m+e,k),2**k)
                   for k in range(m+1)),Fraction(0))
            U,T,Q,cp=integer_lift(m,e)
            assert cp*U==Q*A and T==Q*B
            assert Q==(500**m*factorial(2*m) if e==0 else 2048**m*factorial(2*m+1))
            rational+=2
    num=direct_count=zero_A=zero_B=0
    examples={}
    for p in primes(50000):
        e=0 if p%6==1 else 1
        m=(p-1-4*e)//6
        assert p==6*m+1+4*e
        U,T,Q,cp=integer_lift(m,e,p)
        assert Q!=0
        # No inversion is needed for the two Boolean zero-port observations.
        zu=(U==0);zt=(T==0)
        assert zu != zt
        # Exactly ONE modular inversion to recover both numerical ports.
        invQ=pow(Q,-1,p)
        A,B=(U*cp*invQ)%p,(T*invQ)%p
        assert zu==(A==0) and zt==(B==0)
        if p<=2000:
            assert (A,B)==direct(m,e,p)
            direct_count+=1
        chi=1 if pow((-6)%p,(p-1)//2,p)==1 else -1
        assert (chi==-1 and zu) or (chi==1 and zt)
        if p in [5,7,11,13,17,19,29,157,373]:
            examples[str(p)]={'A':A,'B':B,'U':U,'T':T,'Q':Q,'epsilon':e,'m':m}
        zero_A+=zu;zero_B+=zt;num+=1
    return {'status':'PASS','rational_port_checks':rational,
            'direct_binomial_prime_checks':direct_count,'prime_sweep':num,
            'max_prime':50000,'A_zero':zero_A,'B_zero':zero_B,
            'step_inversions':0,'final_inversions_to_recover_two_ports':1,
            'examples':examples,'admission':'UNREVIEWED_NOT_ADMITTED_AUTHOR_ONLY'}

if __name__=='__main__':
    print(json.dumps(check(),ensure_ascii=False,indent=2))
