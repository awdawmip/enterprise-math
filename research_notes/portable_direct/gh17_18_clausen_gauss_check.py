"""Exact finite-field checks for D25 GH-17/GH-18 (author-side, not native Source)."""
from math import isqrt


def primes(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for q in range(2, isqrt(limit - 1) + 1):
        if sieve[q]:
            sieve[q * q:limit:q] = b'\x00' * ((limit - 1 - q*q)//q + 1)
    return [q for q in range(11, limit) if sieve[q] and q % 8 == 3]


def value(coeff, z, p):
    # Horner evaluation is exact in F_p.
    ans = 0
    for a in reversed(coeff):
        ans = (ans*z + a) % p
    return ans


def derivative(coeff, p):
    return [(r*a) % p for r, a in enumerate(coeff)][1:]


def F_coeff(p):
    m = (p - 3)//8
    coeff = [1]
    for r in range(m):
        q = coeff[-1] * (r-m)**2
        q *= pow((2*m+2+r)*(r+1), -1, p)
        coeff.append(q % p)
    return coeff


def H_coeff(p):
    d = (p - 3)//4
    h, out = 1, [5]
    for r in range(d):
        h = (h * (4*r+3)**3
             * pow((4*r+4)*(4*r+5)*(4*r+6), -1, p)) % p
        out.append((8*(r+1)+5)*h % p)
    return out


def multiply(a, b, p):
    res = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            res[i+j] = (res[i+j] + u*v) % p
    return res


def polynomial_gcd(a, b, p):
    def trim(seq):
        while seq and seq[-1] == 0:
            seq.pop()
        return seq
    a, b = trim(a[:]), trim(b[:])
    while b:
        inv = pow(b[-1], -1, p)
        while len(a) >= len(b):
            k = len(a)-len(b)
            q = a[-1]*inv % p
            for i, v in enumerate(b):
                a[i+k] = (a[i+k]-q*v) % p
            trim(a)
        a, b = b, a
    return [(v*pow(a[-1], -1, p)) % p for v in a] if a else []


def verify(limit=10000):
    qs = primes(limit)
    branch_F = branch_G = other = 0
    for p in qs:
        f = F_coeff(p)
        df = derivative(f, p)
        g = [(5*a + (16*r*f[r] if r else 0)) % p
             for r, a in enumerate(f)]
        fv = value(f, 9, p)
        gv = value(g, 9, p)
        hv = fv*gv % p
        hprime = (value(df, 9, p)*gv + fv*value(derivative(g, p), 9, p)) % p
        assert value(f, 0, p) == 1
        assert value(f, 1, p) != 0
        # Differential first-order transport at z=9.
        assert (16*9*(1-9)*value(derivative(g, p), 9, p)
                - (7*9+1)*gv - (9-5)*fv) % p == 0
        assert not(fv == 0 and gv == 0)
        if hv == 0:
            assert hprime != 0  # unconditional GH-18 transversality
        if p % 24 == 19 and fv == 0 and gv != 0:
            branch_F += 1
        elif p % 24 == 11 and gv == 0 and fv != 0:
            branch_G += 1
        else:
            other += 1
        if p < 1000:
            assert polynomial_gcd(f, df, p) == [1]
            assert polynomial_gcd(f, g, p) == [1]
            gg = polynomial_gcd(g, derivative(g, p), p)
            # If a multiple root exists, it can only occur at z=5.
            assert gg == [1] or gg == [(-5) % p, 1]
            h = H_coeff(p)
            sq = multiply(f, f, p)
            expected = [(8*r+5)*v % p for r, v in enumerate(sq)]
            assert h == expected  # GH-17 all coefficients, not only z=9
            for z in (0, 1, 5, 9):
                assert value(h, z, p) == value(f, z, p)*value(g, z, p)%p
            for z in range(p):
                # Directly verify the coupled F/G differential system.
                lhs = 16*z*(1-z)*value(derivative(g, p), z, p)
                rhs = (7*z+1)*value(g, z, p)+(z-5)*value(f, z, p)
                assert (lhs-rhs) % p == 0
    print('PASS_GH17_EXACT_CLAUSEN_FACTOR_AND_COUPLED_ODE')
    print('PASS_GH18_COPRIME_ROOT_AND_Z9_TRANSVERSALITY')
    print('range: primes 11 <= p < %d, p %% 8 = 3: %d' % (limit, len(qs)))
    print('finite observed split: F9=0 on p%%24=19: %d; '
          'G9=0 on p%%24=11: %d; exceptions: %d' % (branch_F, branch_G, other))
    print('exact full coefficient and every z in F_p: p < 1000')


if __name__ == '__main__':
    verify()
