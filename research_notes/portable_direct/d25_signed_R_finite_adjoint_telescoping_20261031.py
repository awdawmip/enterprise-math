"""Exact rational/finite-field signed R adjoint certificate; external D25 arithmetic.
This program validates an exact finite telescope, not the original p^3 target.
"""
from fractions import Fraction
from math import comb


def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for q in range(2, int(limit ** .5) + 1):
        if sieve[q]:
            sieve[q*q::q] = b'\x00' * (((limit - q*q) // q) + 1)
    return [p for p in range(7, limit + 1) if sieve[p] and p % 6 == 1]


def calc(ell, p=None, arbitrary=False):
    # Every rational division is reduced modulo p only after checking units.
    def v(x):
        if p is None:
            return Fraction(x)
        if isinstance(x, Fraction):
            assert x.denominator % p != 0
            return x.numerator * pow(x.denominator, -1, p) % p
        return x % p

    def div(a, b):
        if p is None:
            return a / b
        assert b % p
        return a * pow(b, -1, p) % p

    def eq(a, b):
        return a == b if p is None else (a - b) % p == 0

    zero = v(0)
    g = [v(Fraction(comb(ell, i) * comb(2*ell, i), 2**i)) for i in range(ell+1)]
    c = [zero] * (ell+1)
    c[1] = v(Fraction(1, 10))
    for a in range(1, ell):
        c[a+1] = div(c[a] * 36 * a * a, (6*a + 5) * (3*a + 2))

    # Original signed double sum, independent of the adjoint solver.
    q = [zero]*(ell+1)
    for i in range(1, ell+1):
        q[i] = v(sum((1+6*(i-a))*c[a] for a in range(1, i+1)))
    R_original = v(2 * sum(g[i] * q[i] for i in range(1, ell+1)))

    # Reverse Gauss tail moments and exact adjoint test weight.
    tail0 = [zero] * (ell+2)
    tail1 = [zero] * (ell+2)
    for i in range(ell, -1, -1):
        tail0[i] = v(tail0[i+1] + g[i])
        tail1[i] = v(tail1[i+1] + i*g[i])
    w = [zero] * (ell+2)
    for k in range(ell):
        w[k] = div(6*tail1[k+1] - (6*k+5)*tail0[k+1], 5)
        direct = div(sum((1+6*(i-k-1))*g[i] for i in range(k+1, ell+1)), 5)
        assert eq(w[k], direct)
    # Reverse discrete Green identity: (1-shift)^2 w=(g_(k+1)+5g_(k+2))/5.
    for k in range(ell):
        actual = v(w[k]-2*w[k+1]+w[k+2])
        target = div(g[k+1]+5*g[k+2] if k+2<=ell else g[k+1], 5)
        assert eq(actual, target), (ell, p, k)

    d = [zero] * (ell+1)
    for n in range(1, ell+1):
        d[n] = v(Fraction(n*(6*n+5)*(3*n+2), 18))
    lam = [zero]*(ell+1)
    for k in range(ell):
        lam[k+1] = div(d[k]*lam[k]-w[k], 2*(k+1)**3)
        assert eq(d[k]*lam[k]-2*(k+1)**3*lam[k+1], w[k])

    # Independent expanded-kernel check on rational cases and short modular cases;
    # production recurrence has linear arithmetic cost (expanded form is quadratic).
    if p is None or ell <= 65:
        expanded = zero
        for k in range(ell):
            product = v(1)
            for j in range(k+1, ell):
                product = v(product * div(d[j], 2*(j+1)**3))
            expanded = v(expanded - div(w[k] * product, 2*(k+1)**3))
        assert eq(expanded, lam[ell])

    source = [zero]*(ell+1)
    if arbitrary:
        for n in range(1, ell+1):
            source[n]=v((-1)**n*(7*n+3)+n*n)
    else:
        source[ell] = v(-20 * ell**3 * c[ell])

    f=[zero]*(ell+1)  # f_ell=0 fixed
    for n in range(ell, 0, -1):
        f[n-1] = div(d[n]*f[n]-source[n], 2*n**3)
    assert eq(f[ell], zero)

    # Verify each coefficient, each telescope and the global adjoint pairing.
    past = zero
    for n in range(1, ell+1):
        y_actual = v(d[n]*f[n]-2*n**3*f[n-1])
        assert eq(y_actual, source[n])
        now = v(d[n]*lam[n]*f[n])
        diff = v(lam[n]*source[n]-w[n-1]*f[n-1])
        assert eq(diff, now-past), (ell, p, n)
        past = now
    assert eq(past, zero)
    LHS = v(sum(w[k]*f[k] for k in range(ell)))
    RHS = v(sum(lam[n]*source[n] for n in range(1, ell+1)))
    assert eq(LHS, RHS)

    if not arbitrary:
        for k in range(ell):
            assert eq(f[k], 10*c[k+1]), (ell,p,k)
        assert eq(LHS, R_original)
        assert eq(R_original, source[ell]*lam[ell])
        return (R_original, v(source[ell]), lam[ell])
    return (LHS, RHS)


def main():
    for ell in range(1, 10):
        calc(ell)
        calc(ell, arbitrary=True)
    anchor = {}
    selected = primes(5000)
    assert len(selected) == 330
    for p in selected:
        ell=(p-1)//6
        r,src,dual=calc(ell,p)
        calc(ell,p,arbitrary=True)
        if p in (7,13,19,37,67,373):
            anchor[p] = (r,src,dual)
    expected={13:0, 19:12, 37:11, 67:21, 373:196}
    for p,r in expected.items():
        assert anchor[p][0] == r
    for p,(r,src,dual) in anchor.items():
        print(f'ANCHOR p={p} ell={(p-1)//6} R={r} source={src} adjoint_terminal={dual}')
    print(f'PASS_D25_SIGNED_R_EXACT_FINITE_ADJOINT_TELESCOPE rational_ell=1..9 primes={len(selected)} two_source_families=True')

if __name__ == '__main__':
    main()
