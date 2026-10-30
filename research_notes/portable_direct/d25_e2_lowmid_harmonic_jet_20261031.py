#!/usr/bin/env python3
"""Author-side exact modular regression: original 216 / Van Hamme E.2 low-mid p^3 harmonic jet.
Pure stdlib, no native H0/B0 computation, no assertion of all-prime LIFT proof.
"""


def primes(limit):
    s = [True] * (limit + 1)
    s[0] = s[1] = False
    for k in range(2, int(limit ** .5) + 1):
        if s[k]:
            s[k * k::k] = [False] * len(s[k * k::k])
    return [p for p in range(13, limit + 1) if s[p] and p % 24 in (13, 19)]


def check(p):
    assert p % 24 in (13, 19)
    l = (p - 1) // 6
    m, h, q = 2 * l, 3 * l, 4 * l
    mod, mod2 = p ** 3, p ** 2
    inv = [0] + [pow(k, -1, mod) for k in range(1, p)]
    d = {N: [0] * (h + 1) for N in (m, h, q)}
    d2 = {N: [0] * (h + 1) for N in (m, h, q)}
    for N in (m, h, q):
        for n in range(1, min(h, N) + 1):
            r = inv[N - n + 1]
            d[N][n] = (d[N][n - 1] + r) % mod
            d2[N][n] = (d2[N][n - 1] + r * r) % mod
    harmonic = [0] * (h + 1)
    for n in range(1, h + 1):
        harmonic[n] = (harmonic[n - 1] + inv[n]) % mod

    def frac(a, den):
        return a * pow(den, -1, mod) % mod

    fact = [1] * p
    invfact = [1] * p
    for k in range(1,p):
        fact[k] = fact[k-1] * k % mod
    invfact[p-1] = pow(fact[p-1],-1,mod)
    for k in range(p-1,0,-1):
        invfact[k-1] = invfact[k] * k % mod
    def bc(N,K):
        return fact[N]*invfact[K]*invfact[N-K] % mod
    inv2 = inv[2]
    one_over_two_pow = 1
    original, e2 = 1, 1
    E0 = E1 = E2 = 0
    D0 = D1 = 0
    witnesses = []
    for n in range(h + 1):
        if n <= m:
            t = ((-1)**n * bc(h, n) * bc(m, n) * bc(q, n)
                 * one_over_two_pow) % mod
            v = bc(m, n) ** 3 % mod
            L = (-frac(d[h][n], 2) - frac(d[m][n], 3)
                 - frac(2 * d[q][n], 3)) % mod
            J = (frac(d2[h][n], 4) + frac(d2[m][n], 9)
                 + frac(4 * d2[q][n], 9)) % mod
            dm = d[m][n]
            bmJ = frac(d2[m][n], 3)
            a_pred = t * (1 + p*L + p*p*frac(L*L-J, 2)) % mod
            b_pred = v * (1 - p*dm + p*p*frac(dm*dm-bmJ, 2)) % mod
            assert a_pred == original and b_pred == e2, ('LOW_TERM', p, n)
            w = 6*n + 1
            E0 = (E0 + w * (t - v)) % mod
            E1 = (E1 + w * (t*L + v*dm)) % mod
            E2 = (E2 + w * frac(t*(L*L-J) - v*(dm*dm-bmJ), 2)) % mod
            D0 = (D0 + w * (original - e2)) % mod
        else:
            j = n - m
            u = (fact[m] * fact[j-1] * bc(h, n) * bc(q, n)
                 * inv[3] * invfact[n] * one_over_two_pow) % mod
            Z = (frac(harmonic[j-1] - harmonic[m], 3)
                 - frac(d[h][n], 2) - frac(2*d[q][n], 3)) % mod
            assert original % p == 0
            assert (original // p) % mod2 == (u * (1 + p * Z)) % mod2, ('MID_TERM', p, n)
            w = 6*n + 1
            E1 = (E1 + w*u) % mod
            E2 = (E2 + w*u*Z) % mod
            D1 = (D1 + w*original) % mod
        if n < h:
            original = original*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3, -1, mod)%mod
            e2 = -e2*(3*n+1)**3*pow(27*(n+1)**3,-1,mod)%mod
            one_over_two_pow = one_over_two_pow*inv2%mod

    predicted = (E0 + p*E1 + p*p*E2) % mod
    assert predicted == (D0 + D1) % mod, ('SUM',p)
    assert E0 % p == 0
    assert (E0 + p * E1) % (p*p) == 0
    assert (D0 + D1) % (p*p) == 0
    carry_01 = ((E0 + p*E1) % mod)//(p*p)
    second_jet = E2 % p
    actual = ((D0 + D1) % mod)//(p*p)
    assert (carry_01 + second_jet) % p == actual
    # Separate high strip, independently calculated via the original coefficient recurrence.
    high = 0
    a = 1
    for n in range(2*m+1):
        if h < n <= 2*m:
            high = (high + (6*n+1)*a) % mod
        if n < 2*m:
            a = a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod)%mod
    assert high % mod2 == 0
    high_digit = high//mod2
    if p in (13, 19, 37, 43, 67, 373):
        from math import comb
        inv216 = pow(216, -1, mod)
        scale = 1
        from_bin = 0
        recur = 1
        from_recur = 0
        for n in range(p):
            from_bin = (from_bin + (6*n+1)*comb(2*n,n)**2*comb(3*n,n)*scale) % mod
            from_recur = (from_recur+(6*n+1)*recur) % mod
            if n < p-1:
                scale = scale*inv216%mod
                recur = recur*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod)%mod
        assert from_bin == from_recur, ('BINOM',p)
    if (carry_01 + second_jet + high_digit) % p:
        raise AssertionError(('BRIDGE_FAIL',p,carry_01,second_jet,high_digit))
    return p, carry_01, second_jet, actual, high_digit


def main():
    selected = primes(5000)
    for p in selected:
        witness = check(p)
        if p in (13,19,37,43,67,373):
            print('p,c_01,second_jet,low_mid,high:',*witness,sep=' ')
    print('PASS_D25_E2_LOWMID_HARMONIC_JET', 'target_primes',len(selected))


if __name__ == '__main__':
    main()
