#!/usr/bin/env python3
"""Author-side exact V2304 half-tail fourth-digit source-band certificate.
Only original binomial arithmetic; no native H0/B0 experiment.
"""
from math import isqrt


def primes_through(N):
    s = bytearray(b'\x01') * (N + 1)
    s[:2] = b'\x00\x00'
    for q in range(2, isqrt(N) + 1):
        if s[q]:
            s[q*q:N+1:q] = b'\x00' * (((N-q*q)//q)+1)
    return [p for p in range(5,N+1) if s[p]]


def direct_tail(p):
    M=p**4
    t=1; tail=0; half=0; full=0
    d=pow(2304,-1,M)
    for n in range(p):
        x=(8*n+1)*t % M
        full=(full+x)%M
        if n<=(p-1)//2: half=(half+x)%M
        else: tail=(tail+x)%M
        if n+1<p:
            t=t*(4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)*pow(n+1,-4,M)*d%M
    return tail,full,half


def transported_tail(p):
    Q=p*p
    f=[1]*p
    for j in range(1,p): f[j]=f[j-1]*j%Q
    omega=((f[p-1]+1)%Q)//p
    h=[0]*p
    for j in range(1,p): h[j]=(h[j-1]+pow(j,-1,p))%p
    C=L=T3=0
    for n in range((p+1)//2,p):
        if 4*n<3*p:
            r=4*n-2*p
            b=2*(8*n+1)*f[r]*pow(f[n],-4,Q)*pow(2304,-n,Q)%Q
            C=(C+b)%Q
            L=(L+2*b*(h[r]-omega))%p
        else:
            r=4*n-3*p
            b=-6*(8*n+1)*f[r]*pow(f[n],-4,p)*pow(2304,-n,p)%p
            T3=(T3+b)%p
    return C,L,T3,omega


def main():
    tested=primes_through(2000)
    for p in tested:
        tail,_,_=direct_tail(p)
        C,L,T3,omega=transported_tail(p)
        assert C%p==0,('Guo-Zudilin tail grade-2 boundary',p,C)
        assert tail%p**3==0,('Guo-Zudilin dual truncation',p,tail)
        q=(C//p+L+T3)%p
        assert tail//p**3==q,('fourth digit source-port mismatch',p,q,tail//p**3)
    print('PASS:',len(tested),'primes 5..2000; exact original tail and independent p-adic band formula match')
    for p in (5,7,11,13,19,373):
        tail,full,half=direct_tail(p)
        C,L,T3,omega=transported_tail(p)
        print(f'p={p}: V_full={full}, V_half={half}, tail={tail} mod {p**4}, '
              f'C/p={C//p %p}, L={L}, T3={T3}, fourth digit={tail//p**3}')
    print('Author-side proof is finite factorial/Wilson expansion; native benchmark NOT_EXECUTED.')


if __name__=='__main__':
    main()
