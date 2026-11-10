#!/usr/bin/env python3
"""Original signed W216 grade-0/1 fourth-digit harmonic certificate.
AUTHOR_SIDE exact finite checker, not native H0/B0; no external deps.
"""
from math import comb

def original_bands(p):
    M = p**4
    inv216 = pow(216, -1, M)
    arr = [comb(2*k, k)**2*comb(3*k, k)*pow(inv216, k, M) % M for k in range(4*p)]
    val = [0]*(12*p + 1)
    units = [1]*(12*p + 1)
    for n in range(1, 12*p + 1):
        z, v = n, 0
        while z % p == 0:
            z //= p
            v += 1
        val[n] = val[n-1] + v
        units[n] = units[n-1]*z % M
    independent = []
    for k in range(4*p):
        v = val[2*k] + val[3*k] - 5*val[k]
        assert v >= 0
        independent.append(0 if v >= 4 else p**v * units[2*k] * units[3*k]
                           * pow(units[k], -5, M) * pow(inv216, k, M) % M)
    assert arr == independent
    C = [[0]*4 for _ in range(4)]
    for b in range(p):
        g = (2*b//p)+(3*b//p)
        for a in range(4):
            k = a*p+b
            C[g][a] = (C[g][a] + (6*k+1)*arr[k]*pow(arr[a], -1, M))%M
    L = [((v[3]-5*v[2]+7*v[1]-3*v[0]) % M) for v in C]
    return arr, L

def certificate(p):
    assert p >= 13 and p % 6 == 1
    M, P2, P3 = p**4, p*p, p**3
    A, L = original_bands(p)
    H1=[0]*p; H2=[0]*p; H3=[0]*p
    for n in range(1, p):
        inv = pow(n, -1, P2)
        H1[n] = (H1[n-1] + inv)%P2
        H2[n] = (H2[n-1] + inv*inv)%P2
        H3[n] = (H3[n-1] + pow(n,-3,p))%p
    Q = ((pow(216,p-1,p**3)-1)//p)%P2
    inv2,inv3,inv6=pow(2,-1,P2),pow(3,-1,P2),pow(6,-1,P2)
    assert H2[p-1]%p == 0
    h2 = H2[p-1]//p
    zero = 0
    one = 0
    m=(p-1)//6
    for b in range(3*m+1):
        weight=6*b+1
        Ab=A[b]
        if b<=2*m:
            lam=(2*H1[2*b]+3*H1[3*b]-5*H1[b]-Q)%P2
            mu=(-4*H2[2*b]-9*H2[3*b]+5*H2[b])%P2
            nu=(8*H3[2*b]+27*H3[3*b]-5*H3[b])%p
            S=(mu+lam*lam)%P2
            N=(nu*inv3-5*h2+lam*mu*inv2+lam**3*inv6)%p
            zero=(zero + Ab*(P2*(-2*weight*S-24*lam)
                   +P3*(-2*weight*lam*Q**2-6*weight*N-12*Q**2-18*S)))%M
        else:
            s=3*b-p
            shifted=sum(pow(p+j, -1, P2) for j in range(1,s+1))%P2
            lam=(2*H1[2*b]+3*shifted-5*H1[b]-Q)%P2
            mu=(-4*H2[2*b]-9*H2[s]+5*H2[b])%p
            one=(one + Ab*(-12*p*(6+weight*lam)
                          -12*P2*(weight*Q**2*inv2)
                          -22*P2*(6*lam+weight*(mu+lam*lam)*inv2)))%M
    assert zero == L[0], (p, zero, L[0])
    assert one == L[1], (p, one, L[1])
    assert sum(L)%M == 0, (p, L)
    return (p,L[0],L[1],L[2],L[3],h2)

if __name__ == '__main__':
    for p in (13,19,31,37,43,61,67,73,109,373):
        print(*certificate(p))
