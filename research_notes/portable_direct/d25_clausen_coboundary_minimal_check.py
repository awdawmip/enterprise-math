#!/usr/bin/env python3
"""D25 portable exact F_p certificate; neither native H0/B0 nor Source Result."""
from math import comb

# Literal ascending coefficients of the p=373 coboundary witness.
R373 = tuple(map(int, (
    "95,142,166,143,316,157,86,181,354,126,307,115,159,350,197,76,"
    "330,135,53,5,280,211,92,320,201,163,272,314,327,112,248,160,"
    "143,34,310,334,114,158,232,245,313,230,210,225,231,180,131,269,"
    "329,154,47,286,109,27,38,130,200,359,60,33,67,27,176,116,240,"
    "231,161,173,356,4,25,77,33,304,126,211,106,179,131,347,258,315,"
    "127,286,197,43,93,262,71,182,195,219,144,215,341,321,259,72,18,"
    "280,123,14,141,195,114,98,83,225,299,196,43,141,250,285,186,"
    "292,356,361,247,356,319,162,176").split(',')))


def check(p):
    m = (p-1)//6
    assert p > 3 and p % 6 == 1
    inv = lambda a: pow(a % p, -1, p)
    a = [comb(m,j)*comb(2*m,j)*inv(2**j)%p for j in range(m+1)]
    t = [sum(a[j]*a[k-j] for j in range(max(0,k-m),min(k,m)+1))%p
         for k in range(2*m+1)]
    for k in range(2*m+1):
        assert t[k] == comb(2*k,k)**2*comb(3*k,k)*inv(216**k)%p
    f = [(6*k+1)*t[k]%p for k in range(2*m+1)]
    q = [sum(f[s+1:])%p for s in range(2*m)]
    assert sum(f)%p == 0  # finite check, not a new general theorem
    d = len(q)-1
    r = [0]*d
    for n in range(d,0,-1):
        r[n-1] = (q[n]+(4*n+4)*(r[n] if n<d else 0))*inv(2*n+1)%p
    C = (q[0]+4*r[0])%p
    assert all(q[n] == ((C if n==0 else 0)
                        +(2*n+1)*(r[n-1] if n else 0)
                        -(4*n+4)*(r[n] if n<d else 0))%p
               for n in range(d+1))
    if p == 373:
        assert C == 6 and len(R373)==123
        assert all(q[n] == ((6 if n==0 else 0)
                            +(2*n+1)*(R373[n-1] if n else 0)
                            -(4*n+4)*(R373[n] if n<123 else 0))%p
                   for n in range(len(q)))
        assert tuple(r)==R373
    u=[1]
    for n in range(2*m-1):
        u.append(u[-1]*4*(n+1)*inv(2*n+3)%p)
    assert sum(q[s]*u[s] for s in range(2*m))%p==C
    tail=direct=0
    for k in range(2*m+1):
        direct=(direct+f[k]*tail)%p
        if k<2*m: tail=(tail+u[k])%p
    assert direct==C
    chi=1 if pow(2,(p-1)//2,p)==1 else -1
    assert C==3*(1-chi)%p  # finite observations ONLY
    return p, m, C, r[0], chi


if __name__=='__main__':
    for p in (7,13,19,31,37,43,73,211,373): print(check(p))
    print('PASS_D25_CLAUSEN_COB_EXACT_P373_LITERAL_AUTHOR_SIDE')
