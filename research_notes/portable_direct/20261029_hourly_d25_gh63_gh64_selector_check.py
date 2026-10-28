#!/usr/bin/env python3
"""Independent exact F_p checks for GH-63/64 syzygy and selector blind charts.
Pure integer modular arithmetic, no numerical integration or native X6 test.
"""
from math import comb


def primes_below(limit):
    sieve = bytearray(b'\1') * limit
    sieve[:2] = b'\0\0'
    for k in range(2, int((limit - 1) ** .5) + 1):
        if sieve[k]:
            sieve[k * k:limit:k] = b'\0' * len(sieve[k * k:limit:k])
    return [p for p in range(11, limit) if sieve[p] and p % 8 == 3]


def coeffs(p):
    m = (p - 3) // 8
    f = [1]
    for r in range(m):
        den = (2 * m + 2 + r) * (r + 1) % p
        f.append(f[-1] * (m-r) ** 2 * pow(den, -1, p) % p)
    return m, f


def eval_poly(c, x, p):
    result = 0
    for b in reversed(c):
        result = (result * x + b) % p
    return result


def h_coefficients(f, p):
    # H=4z(1-z)F'+(1+z)F, with leading-degree m+1 retained.
    h = [0] * (len(f) + 1)
    for r, val in enumerate(f):
        h[r] = (h[r] + val) % p
        h[r + 1] = (h[r + 1] + val) % p
        if r:
            h[r] = (h[r] + 4 * r * val) % p
            h[r + 1] = (h[r + 1] - 4 * r * val) % p
    return h


def jets(p, a, u, v):
    a %= p
    A = a * (1 - a) % p
    B = (5 - 7 * a) * pow(4, -1, p) % p
    inv8 = pow(8, -1, p)
    jet = [u % p, v % p]
    for n in range(p - 2):
        num = (n + 3 * inv8) ** 2 * jet[n] - (n + 1) * (n * (1 - 2*a) + B) * jet[n + 1]
        den = A * (n+1) * (n+2) % p
        jet.append(num * pow(den, -1, p) % p)
    C = ((9*a-3) * pow(4, -1, p) * jet[p-1] + 169 * pow(64, -1, p) * jet[p-2]) % p
    D = 25 * pow(64, -1, p) * jet[p-1] % p
    return C, D


def chart(p, m, f, h, a):
    a %= p
    F = eval_poly(f, a, p)
    Fp = eval_poly([r * f[r] % p for r in range(1, len(f))], a, p)
    H = eval_poly(h, a, p)
    A = a*(1-a) % p
    P = comb(3*m+1, m) % p
    q = pow(a, -(2*m+2), p) * pow(1-a, 4*m+1, p) % p
    assert q and P and A
    assert H == (4*A*Fp + (1+a)*F) % p
    for u,v in ((1,0),(0,1),(3,5)):
        C,D = jets(p,a,u,v)
        assert (4*A*F*D + H*C) % p == 0, (p,a,u,v,C,D)
        W=(F*v-Fp*u)%p
        assert C == (1-a)*P*P*F*W*pow(q,-1,p)%p, (p,a,u,v)
        if F == 0:
            assert C==0 and D==(1-a)*P*P*Fp*Fp*u*pow(q,-1,p)%p
        else:
            assert D == -C * H * pow(4*A*F,-1,p) % p
    return F,H


def main():
    samples = primes_below(2000)
    charts=blind=0
    for p in samples:
        m,f=coeffs(p)
        h=h_coefficients(f,p)
        assert len(h)==m+2 and h[-1]==(1-4*m)*f[-1]%p and h[-1]
        assert h[0]==1 and eval_poly(h,1,p)==2*eval_poly(f,1,p)%p
        assert all((r*h[r] - 25*pow(16,-1,p)*f[r-1])%p==0 for r in range(1,m+2))
        for a in (2,9,p-1,6):
            a%=p
            if a in (0,1): continue
            chart(p,m,f,h,a)
            charts+=1
        if p < 1000:
            for a in range(2,p):
                if not eval_poly(h,a,p):
                    assert eval_poly(f,a,p)
                    # At this chart D vanishes on the entire initial-data plane.
                    assert jets(p,a,1,0)[1] == jets(p,a,0,1)[1] == 0
                    blind+=1
    m,f=coeffs(43);h=h_coefficients(f,43)
    assert eval_poly(f,6,43)==20 and eval_poly(h,6,43)==0
    assert jets(43,6,1,0)==(3,0) and jets(43,6,0,1)==(10,0)
    for p in (11,19,43,59,67,83):
        m,f=coeffs(p);h=h_coefficients(f,p)
        F=eval_poly(f,9,p); G=(144*eval_poly([r*f[r] for r in range(1,len(f))],9,p)+5*F)%p
        H=eval_poly(h,9,p)
        assert H == 2*(10*F-G)%p
        print('TARGET_CHART',p,'F',F,'G',G,'H',H)
    print('PASS_GH63_GH64',len(samples),'primes',charts,'three-initial-data charts',blind,'field-rational blind roots p<1000')
    print('PASS_GH63_TERMINAL_BLIND_COUNTEREXAMPLE p=43 a=6')


if __name__ == '__main__':
    main()
