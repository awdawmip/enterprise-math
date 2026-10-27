#!/usr/bin/env python3
"""Exact finite-field D25 216/Cauchy moment to even Legendre bridge.
External scalar diagnostic only; not original H0/B0 divided-power execution.
"""
from math import comb


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] = (c[i+j] + ai*bj) % p
    return c


def even_composition(c, p):
    """Polynomial c(z) at z=2(1-x²), ascending powers of x."""
    ans = [0] * (2*(len(c)-1) + 1)
    for j, cj in enumerate(c):
        for r in range(j+1):
            ans[2*r] = (ans[2*r] + cj*2**j*(-1)**r*comb(j, r)) % p
    return ans


def legendre(n, p):
    p0, p1 = [1], [0, 1]
    if n == 0: return p0
    for j in range(1, n):
        z = [0] * (j+2)
        inv = pow(j+1, -1, p)
        for k, v in enumerate(p1): z[k+1] += (2*j+1)*v
        for k, v in enumerate(p0): z[k] -= j*v
        z = [v*inv % p for v in z]
        p0, p1 = p1, z
    return p1


def check(p):
    assert p > 3 and (p-1) % 6 == 0
    m, n = (p-1)//6, (p-1)//3
    inv = lambda a: pow(a % p, -1, p)
    a = [comb(m, j)*comb(2*m, j)*inv(2**j) % p for j in range(m+1)]
    P = legendre(n, p)
    assert even_composition(a, p) == P, 'quadratic Jacobi/Legendre transform'
    y = mul(P, P, p)
    t = [sum(a[j]*a[k-j] for j in range(max(0,k-m),min(m,k)+1))%p
         for k in range(n+1)]
    for k in range(n+1):
        assert t[k] == comb(2*k,k)**2 * comb(3*k,k)*inv(216**k) % p
    f = [(6*k+1)*t[k]%p for k in range(n+1)]
    q = [sum(f[s+1:])%p for s in range(n)]
    Q = even_composition(q, p)
    # F(2(1-x²)) = P² -3(1-x²)/x * (P²)'. All coefficients are integral.
    v = [0]*len(y)
    for j in range(2, len(y), 2): v[j-2] = j*y[j]%p
    Fcomp = [0]*len(y)
    for j in range(len(y)):
        Fcomp[j] = (y[j] -3*(v[j] if j<len(v) else 0)
                    +3*(v[j-2] if j>=2 else 0))%p
    rhs = [0]*(len(Q)+2)
    for j, x in enumerate(Q):
        rhs[j] = (rhs[j]-x)%p
        rhs[j+2] = (rhs[j+2]+2*x)%p
    left = [(-x)%p for x in Fcomp]
    left[0] = (left[0]+sum(f))%p
    assert rhs == left, 'original signed q quotient'
    assert sum(f)%p == 0, 'known mod-p original W vanishing (finite test)'
    # Genuine u_s = 8^s/((2s+1)*binom(2s,s)), NOT 4^s*(s!)²/(2s+1)!.
    u = [8**s*inv((2*s+1)*comb(2*s,s))%p for s in range(n)]
    for s in range(n):
        integ = sum((-1)**j*comb(s,j)*inv(2*j+1) for j in range(s+1))
        assert u[s] == pow(2,s,p)*integ%p
    nested = sum(f[k]*sum(u[:k]) for k in range(n+1))%p
    moment = sum(q[s]*u[s] for s in range(n))%p
    legendre_integral = sum(Q[2*r]*inv(2*r+1) for r in range(2*m))%p
    assert nested == moment == legendre_integral
    chi = 1 if pow(2,(p-1)//2,p)==1 else -1
    # Only finite check of conjecture; not a proof.
    conjectural = 3*(1-chi)%p
    assert nested == conjectural, 'finite observation of Cauchy/LIFT auxiliary conjecture'
    result = {'p':p,'m':m,'P_even_degree':n,'F1':sum(f)%p,'A1':sum(a)%p,
              'T':nested,'chi2':chi,'P0':P[0]}
    if chi == -1:
        # Separately observed for selected primes; not asserted from chi alone as theorem.
        xpoly = [P[2*j] for j in range(m+1)]
        h = [0]*m
        h[-1] = xpoly[-1]*inv(2)%p
        for j in range(m-1,0,-1): h[j-1] = (xpoly[j]+h[j])*inv(2)%p
        rem = (xpoly[0]+h[0])%p
        result['P_mod_(2x²-1)_remainder'] = rem
        assert rem == 0
    return result


if __name__ == '__main__':
    for p in (7,13,19,31,37,43,61,67,73,211,373):
        print(check(p))
    print('PASS_AUTHOR_SIDE_D25_LEGENDRE_MOMENT_EXACT_11_PRIMES')
