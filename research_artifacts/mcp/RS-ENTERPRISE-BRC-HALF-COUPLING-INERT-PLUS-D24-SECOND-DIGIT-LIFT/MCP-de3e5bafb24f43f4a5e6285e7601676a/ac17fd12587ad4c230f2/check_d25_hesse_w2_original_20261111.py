#!/usr/bin/env python3
"""Exact R_2 Hesse-model and p^2 coefficient checker, D25 original-class input.
No floating point and no native H0/B0 crystalline or [X]U computation.
Authors' finite regression only. Scientific Source pin:
c47e13e4aba0e006366f989d6334d443f6333ae3.
"""
from math import factorial

def check(p):
    assert p >= 13 and p % 24 in (13, 19)
    mod = p * p
    def mul(x, y, m=mod):
        return ((x[0]*y[0]+2*x[1]*y[1]) % m,
                (x[0]*y[1]+x[1]*y[0]) % m)
    def exp(x, n, m=mod):
        z = (1, 0)
        while n:
            if n & 1: z = mul(z, x, m)
            x = mul(x, x, m)
            n >>= 1
        return z
    def add(x, y, m=mod):
        return ((x[0]+y[0]) % m, (x[1]+y[1]) % m)
    def sub(x, y, m=mod):
        return ((x[0]-y[0]) % m, (x[1]-y[1]) % m)
    def inv(x, m=mod):
        d = (x[0]*x[0]-2*x[1]*x[1]) % m
        return mul((x[0], -x[1] % m), (pow(d, -1, m), 0), m)
    t = (4, 2)
    q = p * p
    assert exp(t, (q-1)//3, p) == (1, 0)
    lam1 = next((a, b) for a in range(p) for b in range(p)
                if exp((a,b),3,p) == (4 % p, 2 % p))
    # Hensel Newton step modulo p^2.
    lam = sub(lam1, mul(sub(exp(lam1,3), t),
                        inv(mul((3,0),exp(lam1,2)))))
    assert exp(lam,3) == (4,2)
    inv4 = pow(4,-1,mod)
    u = (2*inv4 % mod, -inv4 % mod)
    assert mul(u,t) == (1,0)
    jt = mul(mul((27,0), t),exp(add(t,(8,0)),3))
    jt = mul(jt,inv(exp(sub(t,(1,0)),3)))
    assert jt == (2417472 % mod, -1707264 % mod)
    n = (p-1)//3
    f = [1]
    for j in range(1,p): f.append(f[-1]*j % mod)
    C = (0,0)
    neg3lam = mul((-3 % mod, 0),lam)
    for k in range(n+1):
        r=p-1-3*k
        w=f[p-1]*pow(f[k]**3*f[r] % mod,-1,mod) % mod
        C=add(C,mul((w,0),exp(neg3lam,r)))
    A=D=(0,0)
    c=1
    up=(1,0)
    h=0
    for k in range(n+1):
        A=add(A,mul((c,0),up))
        if k:
            for j in range(3*k-2,3*k+1):
                h=(h+pow(j,-1,mod)) % mod
        D=add(D,mul((c*h % mod,0),up))
        if k<n:
            c=c*(3*k+1)*(3*k+2)*(3*k+3)*pow(27*(k+1)**3,-1,mod) % mod
            up=mul(up,u)
    s=exp(neg3lam,p-1)
    assert C == mul(s,sub(A,mul((p,0),D)))
    assert C[0]%p == C[1]%p == 0
    assert A[0]%p == A[1]%p == 0
    finite = dict(p=p, lambda2=lam, C=C, A=A,
        C_over_p=(C[0]//p,C[1]//p),
        D_modp=(D[0]%p,D[1]%p),
        s_modp=(s[0]%p,s[1]%p))
    return finite

for p in (13,19,37,43,373):
    print(check(p))
v=check(373)
assert v == {
    "p":373,"lambda2":(91441,93269),
    "C":(24618,132788),"A":(112646,57442),
    "C_over_p":(66,356),"D_modp":(326,250),"s_modp":(272,327)
}
print("EXACT_AUTHOR_REGRESSION_PASS: 5 target primes, W2, same original Hesse class")
