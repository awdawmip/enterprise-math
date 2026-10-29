#!/usr/bin/env python3
"""Author-side exact F_p polynomial and F_{p^2} tests for GH-131.

The GH-129 coefficient implementation is reused for moment evaluation.  The
polynomial involution and differential-equation checks below use separate
integer coefficient construction and no character-sum sampling.
"""

from d25_gh129_blind_band_check import (
    add, div, fact_tables, coefficient_prediction, conj, mul,
)


def choose(n, k, p, fact, ifact):
    return 0 if k < 0 or k > n else fact[n] * ifact[k] * ifact[n-k] % p


def pad(coeffs, n):
    return coeffs + [0] * (n - len(coeffs))


def reflect(coeffs, p):
    """Compute f(1/4 - X) by plain polynomial Horner arithmetic."""
    quarter = pow(4, -1, p)
    result = []
    for c in reversed(coeffs):
        nxt = [0] * (len(result) + 1)
        for i, v in enumerate(result):
            nxt[i] = (nxt[i] + quarter*v) % p
            nxt[i+1] = (nxt[i+1] - v) % p
        nxt[0] = (nxt[0] + c) % p
        result = nxt
    return result


def checked_polynomial_involutions(p):
    assert p >= 11 and p % 8 == 3
    m = (p - 3) // 8
    n = 4*m + 1
    d = 2*m
    fact, ifact = fact_tables(p)
    # H(B) = [X^N](X²+X+B)^N.
    H = [fact[n] * ifact[j]**2 * ifact[n-2*j] % p for j in range(d+1)]
    # P_t(B) = [X^t] 1/(1+X+B X²).
    def P(t):
        return [(-1 if (t-j)%2 else 1) * choose(t-j, j, p, fact, ifact) % p
                for j in range(t//2+1)]
    E = P(n-1)
    A = [0]*n + P(n)
    assert len(H) == d+1 and len(E) == d+1 and len(A) == n+d+1

    # Hypergeometric equations proved by their coefficient recurrences.
    def check_h(coeffs):
        c = coeffs + [0]
        for j in range(len(coeffs)):
            assert (4*(j+1)**2*c[j+1] - (4*j+1)*(4*j+3)*c[j]) % p == 0, (p,'H',j)
    def check_ae(coeffs, label):
        c = coeffs + [0]
        for j in range(len(coeffs)):
            assert (2*(j+1)*(2*j+3)*c[j+1] - (4*j+3)*(4*j+5)*c[j]) % p == 0, (p,label,j)
    check_h(H)
    check_ae(E, 'E')
    check_ae(A, 'A')

    assert reflect(H,p) == H, (p,'H_reflection')
    assert reflect(E,p) == E, (p,'E_reflection')
    rA = reflect(A,p)
    rhs = [(pad(E,len(A))[i]*pow(2,-1,p)-A[i])%p for i in range(len(A))]
    assert rA == rhs, (p,'A_reflection')
    return fact, ifact, n, (len(H),len(E),len(A))


def test_marked_moments(p, fact, ifact, n, indices):
    B = div(add((1,0), div((0,2),(3,0),p),p),(8,0),p)
    Bstar = ((pow(4,-1,p)-B[0])%p,(-B[1])%p)
    assert Bstar == conj(B,p)
    out = {}
    for s in indices:
        value,_ = coefficient_prediction(p,B,s,fact,ifact)
        conjugate,_ = coefficient_prediction(p,Bstar,s,fact,ifact)
        expected = tuple(((-1)**(s+1)*v)%p for v in value)
        assert conjugate == expected, (p,s,value,conjugate)
        assert value == ((value[0],0) if s%2 else (0,value[1])), (p,s,value)
        out[s]=value
    return B,out


def run():
    total=0
    for p in (11,19,43,59,83,107,3347):
        fact, ifact, n, degrees = checked_polynomial_involutions(p)
        indices = list(range(1,n+1)) if p <= 107 else [1,2,3,4,5,10,n]
        B, values = test_marked_moments(p,fact,ifact,n,indices)
        total += len(indices)
        print('polynomial involution + marked moments', p, 'poly lengths H/E/A', degrees,
              'moments', len(indices), 'B', B,
              'first', values[1], 'second', values[2],
              'third', values[3])
        if p==3347:
            assert values[1] == (3179,0)
            assert values[2] == (0,2701)
            norm = mul(values[2],conj(values[2],p),p)
            assert norm == (2118,0), norm
            print('p3347 exact trace-only loss: S_1675=(0,2701), trace=0, norm=',norm)
    print('PASS_GH131_ALL_PRIMES_PROOF_CONSISTENCY_EXACT_INVARIANCE',
          'polynomial_prime_instances=7', 'marked_moment_instances='+str(total))


if __name__ == '__main__':
    run()
