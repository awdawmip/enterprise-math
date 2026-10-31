#!/usr/bin/env python3
"""D25 portable regression: p^2 lifted reciprocal p^3 Clausen tail, all p>=5."""
from fractions import Fraction
from math import comb


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, int(n ** 0.5) + 1):
        if sieve[q]:
            sieve[q * q:n + 1:q] = b'\x00' * ((n - q * q) // q + 1)
    return [q for q in range(5, n + 1) if sieve[q]]


def mod_rational(num, den, mod):
    return num % mod * pow(den % mod, -1, mod) % mod


def test_prime(p):
    h = (p - 1) // 3
    N = p - h
    mod2, mod5 = p * p, p ** 5
    coeff = [1]
    for n in range(p - 1):
        mult = (2 * n + 1) * (3 * n + 1) * (3 * n + 2)
        denom = 36 * (n + 1) ** 3
        coeff.append(coeff[-1] * mult * pow(denom, -1, mod5) % mod5)
    assert all(coeff[p-k] % p**3 == 0 for k in range(1, h+1))
    assert all(coeff[k] % p != 0 for k in range(1, h+1))
    endpoint = (-coeff[p-1] // p**3) % mod2
    assert endpoint % p == 1, (p, 'endpoint', endpoint)
    q = ((endpoint - 1) % mod2) // p
    H = 0
    Qraw = 0
    B = 0
    D = 0
    b_first = None
    pairs = 0
    for k in range(1, h+1):
        if k >= 2:
            H = (H + mod_rational(2,2*k-1,p)
                    + mod_rational(3,3*k-1,p)
                    + mod_rational(3,3*k-2,p)
                    - mod_rational(3,k-1,p)) % p
        lo_inv = pow(coeff[k] % mod2, -1, mod2)
        low_denom_inv = pow(18*k**3 % mod2, -1, mod2) * lo_inv % mod2
        expected = -(1 + p*(q+H)) * low_denom_inv % mod2
        actual = coeff[p-k]//p**3
        assert expected == actual, (p,k,expected,actual)
        M = (-18*k**3*(coeff[k]%mod2)*actual) % mod2
        assert M == (1+p*(q+H))%mod2, (p,k,'transport')
        B = (B+(6*k-1)*low_denom_inv)%mod2
        D = (D + ((6*k-1)*H-6)*low_denom_inv) % p
        Qraw = (Qraw+(6*(p-k)+1)*actual) % mod2
        if k == h:
            b_first = (N**3*actual)%mod2
        pairs += 1
    predicted = (B+p*(q*(B%p)+D))%mod2
    assert Qraw == predicted, (p, 'weighted tail', Qraw,predicted)
    first_pred = (pow(18*(coeff[h]%mod2),-1,mod2)*(1+p*(q+H-3*pow(h,-1,p))))%mod2
    assert b_first == first_pred, (p,'first wall',b_first,first_pred)
    terminal = (-mod_rational((2*p-1)*(3*p-2)*(3*p-1),36,mod2)* (coeff[p-1]//p**3))%mod2
    terminal_pred = (mod_rational(-1,18,mod2)+p*(mod_rational(13,36,p)-mod_rational(q,18,p)))%mod2
    assert terminal == terminal_pred, (p,'terminal wall',terminal,terminal_pred)
    # Anchor against the unmodified integer binomial coefficients (no recurrence).
    if p in (5,11,17,23,29,41,73,373,1327):
        for n in (0,1,h,N,p-1):
            a_direct=comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod5)%mod5
            assert a_direct == coeff[n], (p,n,'binomial')
    return {'p':p,'h':h,'q':q,'B':B,'D':D,'Q2':Qraw,'first':b_first,'terminal':terminal,'pairs':pairs}


def test_exact_rational_ode():
    # L=theta^3 - X*(theta+1/2)(theta+1/3)(theta+2/3)/2.
    # The stated two-boundary equation is exact over the rationals.
    for p in (5,7,11,13,17,19,23,29):
        h=(p-1)//3
        N=p-h
        a=[Fraction(1)]
        for n in range(p-1):
            a.append(a[-1]*Fraction((2*n+1)*(3*n+1)*(3*n+2),36*(n+1)**3))
        scaled={n:a[n]/p**3 for n in range(N,p)}
        for n in range(N,p+1):
            lhs=n**3*scaled.get(n,0)-Fraction((2*n-1)*(3*n-2)*(3*n-1),36)*scaled.get(n-1,0)
            exp=(N**3*scaled[N] if n==N else -Fraction((2*p-1)*(3*p-2)*(3*p-1),36)*scaled[p-1] if n==p else 0)
            assert lhs==exp, (p,n,'exact rational source')
    return 8


def main():
    result = [test_prime(p) for p in primes_upto(3000)]
    print('PRIMES',len(result),'P5_BRANCH',sum(x['p']%6==5 for x in result),'P1_BRANCH',sum(x['p']%6==1 for x in result))
    print('MIRROR_COEFFICIENTS',sum(x['pairs'] for x in result))
    print('EXACT_RATIONAL_ODE_PRIMES',test_exact_rational_ode())
    for x in result:
        if x['p'] in (5,11,17,23,29,41,373,1327):
            print('ANCHOR',x)
    print('PASS_D25_ALL_PRIME_P2_LIFTED_CLAUSEN_TAIL_TWO_BOUNDARIES_EXACT')


if __name__=='__main__':
    main()
