#!/usr/bin/env python3
"""Universal p^2 harmonic two-port identity: exact independent finite crosschecks."""
from math import isqrt

def prime_list(limit):
    mark=bytearray(b'\x01')*(limit+1);mark[:2]=b'\x00\x00'
    for q in range(2,isqrt(limit)+1):
        if mark[q]:mark[q*q:limit+1:q]=b'\x00'*((limit-q*q)//q+1)
    return [p for p in range(5,limit+1) if mark[p]]

def harmonic_two_ports(p):
    e=0 if p%6==1 else 1
    m=(p-1-4*e)//6;M=p*p
    t=1;H=0;inv36=pow(36,-1,M)
    S_A=S_B=E_A=E_B=0
    for k in range(m+1):
        w=1-6*e+12*k
        S_A=(S_A+t)%M;S_B=(S_B+w*t)%M
        E_A=(E_A+(t%p)*H)%p;E_B=(E_B+w*(t%p)*H)%p
        if k<m:
            H=(H+pow(6*k+1+4*e,-1,p)+pow(3*k+1+e,-1,p))%p
            t=t*(6*k+1+4*e)*(3*k+1+e)*inv36*pow(k+1,-2,M)%M
    return (S_A-p*E_A)%M,(S_B-p*E_B)%M,S_A,S_B,E_A,E_B

def direct_binom_ports(p):
    e=0 if p%6==1 else 1
    m=(p-1-4*e)//6;M=p*p;h=pow(2,-1,M)
    lim=2*m+e; f=[1]*(lim+1)
    for j in range(1,lim+1):f[j]=f[j-1]*j%M
    iv=[0]*(lim+1);iv[lim]=pow(f[lim],-1,M)
    for j in range(lim,0,-1):iv[j-1]=iv[j]*j%M
    C=lambda n,k:f[n]*iv[k]*iv[n-k]%M
    z=1;A=B=0
    for k in range(m+1):
        term=C(m,k)*C(2*m+e,k)*z%M
        A=(A+term)%M;B=(B+(1-6*e+12*k)*term)%M
        z=z*h%M
    return A,B

if __name__=='__main__':
    ps=prime_list(10000)
    for p in ps:
        A,B,*_=harmonic_two_ports(p)
        assert (A,B)==direct_binom_ports(p),(p,A,B)
    assert len(ps)==1227
    for p,label in [(149,'B'),(211,'A'),(101419,'A')]:
        A,B,SA,SB,EA,EB=harmonic_two_ports(p)
        s,h=(SA,EA) if label=='A' else (SB,EB)
        assert s%p==0 and s//p==h
        assert (A if label=='A' else B)==0
        print('EXACT SECOND-DIGIT CANCELLATION p',p,'port',label,'base quotient',s//p,'harmonic',h)
    print('PASS all',len(ps),'primes 5<=p<=10000, independent factorial comparison of both ports mod p²')
