#!/usr/bin/env python3
"""GH44-46 reproducible exact author checks; NOT native Source admission."""
from fractions import Fraction as Q
from math import gcd


def square(a, mod=None):
    c = [0] * (2 * len(a) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            c[i+j] += x*y
            if mod: c[i+j] %= mod
    return c


def coefficients(d, mod=None):
    p = 4*d + 3
    a, b, c, g = [[1] for _ in range(4)]
    ratios = lambda r: (
        ((8*r+1)**2, 16*(4*r+3)*(r+1)),
        (16*(r+1)*(4*r+3), (8*r+13)**2),
        ((4*r+1)**3, (4*r+2)*(4*r+3)*(4*r+4)),
        ((8*r+8-2*p)*(8*r+6-2*p), (8*r+13-2*p)**2))
    for r in range(d):
        for seq, (num, den) in zip((a, b, c, g), ratios(r)):
            if mod:
                assert gcd(den, p) == 1
                seq.append(seq[-1]*num*pow(den, -1, mod) % mod)
            else:
                seq.append(seq[-1]*Q(num, den))
    return a, b, c, g


def check_prime(p):
    d = (p-3)//4
    mod = p*p
    a, b, c, g = coefficients(d, mod)
    v, z = square(b, mod), square(g, mod)
    for n in range(2*d+2):
        prev_v = v[n-1] if n else 0
        cur_v = v[n] if n <= 2*d else 0
        bn = b[n] if n <= d else 0
        assert (8*(n+1)*(2*n+1)*(4*n+3)*prev_v - (4*n+5)**3*cur_v + 25*(6*n+5)*bn) % p == 0
        prev_z = z[n-1] if n else 0
        cur_z = z[n] if n <= 2*d else 0
        gn = g[n] if n <= d else 0
        assert (4*(2*n+2-p)*(2*n+1-p)*(4*n+3-2*p)*prev_z
                - (4*n+5-2*p)**3*cur_z + (5-2*p)**2*(6*n+5-2*p)*gn) % mod == 0
    assert v[d] % p == 25*pow(16, -1, p)*b[d] % p
    assert z[d] == (25*pow(16,-1,mod)*g[d]
                    + p*(pow(8,-1,mod)*z[d-1] -15*pow(32,-1,mod)*g[d])) % mod
    W_fast, v_fast, u_power, u = 11 % p, 1, 1, pow(9,-1,p)
    for n in range(1,d):
        v_fast = ((8*(n+1)*(2*n+1)*(4*n+3)*v_fast +25*(6*n+5)*b[n])
                  *pow((4*n+5)**3,-1,p))%p
        assert v_fast == v[n]%p
        u_power = u_power*u%p
        W_fast = (W_fast+(8*n+11)*v_fast*u_power)%p
    assert W_fast == sum((8*n+11)*v[n]*pow(u,n,p) for n in range(d))%p
    tail = v[d]%p
    for s in range(1,d+1):
        n = d+s
        tail = tail*8*(n+1)*(2*n+1)*(4*n+3)*pow((4*n+5)**3,-1,p)%p
        assert tail == v[n]%p
    assert z[d] == c[d]*pow(a[d]**2,-1,mod)%mod
    b_next = sum(a[i]*a[d+1-i] for i in range(1,d+1))%mod
    assert ((2-p)**3*c[d] -p*(1-p*p)*b_next
            -(5-2*p)**2*(1-p)*pow(2,-1,mod)*a[d])%mod == 0
    assert g[d] == pow(a[d], -1, mod)
    H = [0]
    for r in range(d):
        H.append((H[-1]+4*pow(8*r+13,-1,p)-pow(4*r+4,-1,p)-pow(4*r+3,-1,p))%p)
    assert all(g[i]==b[i]*(1+p*H[i])%mod for i in range(d+1))
    j = sum(b[i]*b[d-i]*(H[i]+H[d-i]) for i in range(d+1))%p
    assert (z[d]-v[d]-p*j)%mod==0
    numerator=(v[d]-25*pow(16,-1,mod)*b[d])%mod
    assert numerator%p==0
    assert (numerator//p+j)%p == (25*pow(16,-1,p)*b[d]*H[d]
                               +pow(8,-1,p)*v[d-1]-15*pow(32,-1,p)*b[d])%p
    return p, d, W_fast


def check_rational(d):
    p = 4*d+3
    a, b, c, g = coefficients(d)
    g = [a[d-i]/a[d] for i in range(d+1)]
    v, z = square(b), square(g)
    E = Q(p*(d+1), 4)*b[d]
    h = Q(p,4)
    for n in range(2*d+2):
        pv = v[n-1] if n else 0
        cv = v[n] if n <= 2*d else 0
        bn = b[n] if n <= d else 0
        rhs = -Q(25,64)*(6*n+5)*bn
        if 0 <= n-d-1 <= d: rhs += E*(6*(n-d-1)+2*d+7)*b[n-d-1]
        assert Q(n+1)*(n+Q(1,2))*(n+Q(3,4))*pv - (n+Q(5,4))**3*cv == rhs
        pz = z[n-1] if n else 0
        cz = z[n] if n <= 2*d else 0
        gn = g[n] if n <= d else 0
        assert ((n+1-2*h)*(n+Q(1,2)-2*h)*(n+Q(3,4)-2*h)*pz
                -(n+Q(5,4)-2*h)**3*cz
                == -(Q(5,8)-h)**2*(6*n+5-8*h)*gn)
    b_next = sum(a[i]*a[d+1-i] for i in range(1,d+1))
    assert (2-p)**3*c[d] == p*(1-p*p)*b_next + Q((5-2*p)**2*(1-p),2)*a[d]


def main():
    ps = [p for p in range(7,2000,4) if all(p%q for q in range(2,int(p**.5)+1))]
    vals = [check_prime(p) for p in ps]
    for d in range(1,13): check_rational(d)
    print('PASS_GH44_GH45_GH46_MOD_P_AND_P2',len(vals),'primes')
    print('PASS_GH44_GH45_GH46_RATIONAL',12,'integer d values')
    print('SAMPLES', [x for x in vals if x[0] in (19,43,67)])


if __name__ == '__main__': main()
