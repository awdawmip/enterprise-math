#!/usr/bin/env python3
"""Exact source-factor and sixth-digit Frobenius seam check; author-side only."""
from math import comb, isqrt

def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))

def check(p):
    assert p >= 13 and p % 6 == 1 and prime(p)
    m, n, M = (p - 1)//6, (p - 1)//3, p**6
    def f(a, b=1):
        return a * pow(b % M, -1, M) % M
    def h(k, r=1):
        return sum(f(1, j**r) for j in range(1, k+1)) % M
    q = (pow(108, p-1, p**7)-1)//p
    qa = (pow(2, p-1, p**7)-1)//p
    qb = (pow(3, p-1, p**7)-1)//p
    C = f((p+1)*(2*p-1)**2*(30*p*p+77*p+40),
          2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5))
    B, carry = 0, 1
    for j in range(1, 5):
        B = (B+(6*p+6*j+7)*carry) % M
        if j < 4:
            carry = carry*f((2*p+2*j+3)*(2*p+3*j-1)*(2*p+3*j),
                   4*(2*p+3*j+1)*(p+j+2)*(4*p+3*j+11)) % M
    T = comb(2*p-1,p-1) % M
    R = f((1-p)**2, 1-2*p)
    K = pow(1+p*q,-1,M)*pow(1-p,-2,M) % M
    for k in range(2,n+1):
        K = K*f((k-p)**2,k*k) % M
    for j in range(1,n):
        K = K*f(j,j+p) % M
    A = 2*m*C*K % M
    P = 1
    for c,e in [(-1,2),(2,2),(5,2),(8,1),(11,1)]:
        P = P*pow(1+p*f(1,c),-e,M) % M
    P = P*pow(1+p*qa,-2,M)*pow(1+p*qb,-3,M) % M
    for j in range(1,n):
        P = P*f((j-p)**2,j*j) % M
    for j in range(1,6):
        P = P*f(j+p,j) % M
    for j in range(1,5):
        P = P*f(j+2*p,j) % M
    P = P*(1+2*p) % M
    for j in range(1,3):
        P = P*pow(f(j+p,j),-2,M) % M
    for j in range(1,n+5):
        P = P*pow(f(j+p,j),-1,M) % M
    L = p*f(3,220)*B*P % M
    F_U = pow(1+p*q,-1,M)
    for k in range(2,n+1):
        F_U = F_U*f((k-p)**2,k*k) % M
    for j in range(1,p-1):
        F_U = F_U*f((j+p)**2,j*j) % M
    for j in range(1,n):
        F_U = F_U*f(j,j+p) % M
    assert F_U == T*T*R*R*K % M
    Q = (2*m*C*F_U+T*T*L) % M
    actual = (Q-A-L) % M
    assert h(p-1,2)%p == 0 and h(p-1,4)%p == 0
    theta,omega = h(p-1,2)//p,h(p-1,4)//p
    assert T*T%M == (1-2*p**3*theta-p**5*omega)%M
    k1 = 4-q-2*h(n)-h(n-1)
    k2 = 2+f(q*q,2)-h(n,2)+f(h(n-1,2),2)
    k3 = f(4,3)-f(q**3,3)-f(2*h(n,3),3)-f(h(n-1,3),3)
    K2 = k2+f(k1*k1,2)
    K3 = k3+k1*k2+f(k1**3,6)
    a0 = -4*m
    a1 = 2*m*(f(3,4)-2*k1)
    a2 = 2*m*(f(-393,40)+f(3*k1,4)-2*K2)
    a3 = 2*m*(f(-10051,400)-f(393*k1,40)+f(3*K2,4)-2*K3)
    g = (f(169,440)-2*qa-3*qb-2*h(n-1)+h(5)+
         2*h(4)+2-2*h(2)-h(n+4))
    ell1 = f(752427,3942400)
    ell2 = f(466056841,4691456000)+ell1*g
    assert (A-a0-a1*p-a2*p*p-a3*p**3)%p**4 == 0
    assert (L-ell1*p-ell2*p*p)%p**3 == 0
    pred = (2*a0*p**2+
        (2*a1+(4-2*theta)*a0)*p**3+
        (2*a2+(4-2*theta)*a1+9*a0-2*theta*ell1)*p**4+
        (2*a3+(4-2*theta)*a2+9*a1+
         (20-4*theta-omega)*a0-2*theta*ell2)*p**5) % M
    assert pred == actual, (p,pred,actual)
    return actual, ((T*T-1)*L)%M

if __name__ == "__main__":
    checked = [p for p in range(13,3000) if p%6==1 and prime(p)]
    assert len(checked)==206
    for p in checked:
        check(p)
    for p, expected in [(13,10),(109,42)]:
        tail = check(p)[1]
        assert tail % p**5 == 0
        assert tail//p**5 == expected
    print("206/206 PASS; p13=",check(13),
          "p19=",check(19),"p109=",check(109))
