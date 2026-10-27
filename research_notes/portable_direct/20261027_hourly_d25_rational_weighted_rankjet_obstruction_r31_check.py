"""Author exact finite-field audit for D25/R31 (not native H0/B0 execution).

Runs without network or dependencies.  Every assertion is a finite check;
the all-prime conclusion is proved separately by a polynomial degree argument.
"""
from fractions import Fraction

def primes_below(limit):
    out = []
    for n in range(2, limit):
        if all(n % q for q in out if q * q <= n):
            out.append(n)
    return out

def weighted_ports(p):
    """W and S after exact R25 Hadamard transport, strictly 0<=r<m."""
    m = (p - 1) // 6
    inv = lambda x: pow(x % p, -1, p)
    h = [1]
    for r in range(1, m):
        # (r-1/12)(r+5/12)h[r] = r(r+1/3)h[r-1].
        h.append(h[-1] * 48 * r * (3 * r + 1)
                 * inv((12 * r - 1) * (12 * r + 5)) % p)
    W = [(2*r + 1) * pow(2, r, p) % p for r in range(m)]
    S = [((24*r + 13) * inv(3)) * pow(9, r, p) * h[r] % p
         for r in range(m)]
    return W, S, h

def rank_mod(rows, p):
    a = [row.copy() for row in rows]
    pos = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pos, len(a)) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[pos], a[pivot] = a[pivot], a[pos]
        scale = pow(a[pos][col], -1, p)
        a[pos][col:] = [x * scale % p for x in a[pos][col:]]
        for i in range(pos+1, len(a)):
            if factor := a[i][col]:
                a[i][col:] = [(x-factor*y) % p for x,y in
                             zip(a[i][col:],a[pos][col:])]
        pos += 1
        if pos == len(a):
            break
    return pos

def degree_pair_obstructed(p, n, d, W, S):
    # S_r N(r) - W_r D(r) = 0; full column rank rules out any
    # nonzero fraction of numerator degree <=n, denominator degree <=d.
    rows = [
        [(S[r] * pow(r, i, p)) % p for i in range(n+1)] +
        [(-W[r] * pow(r, j, p)) % p for j in range(d+1)]
        for r in range(len(W))
    ]
    return rank_mod(rows, p) == n + d + 2

def main():
    sample_count = 0
    term_count = 0
    for p in primes_below(2000):
        if p % 24 != 19:
            continue
        m = (p - 1) // 6
        W,S,h = weighted_ports(p)
        assert all(S), (p, 'unexpected S zero')
        assert all(W), (p, 'unexpected W zero')
        A = lambda t: 216*t*(2*t-1)*(3*t+1)*(24*t+13)
        B = lambda t: (2*t+1)*(24*t-11)*(12*t-1)*(12*t+5)
        assert (31104-6912) % p != 0
        for r in range(1,m):
            assert A(r) % p and B(r) % p
            assert (W[r] * S[r-1] * A(r) -
                    W[r-1] * S[r] * B(r)) % p == 0, (p,r)
            term_count += 1
        sample_count += 1

    checked_pairs = 0
    results = []
    for p in [19,43,67,139]:
        m = (p - 1)//6
        W,S,_ = weighted_ports(p)
        for total_degree in range(m-1):
            for n in range(total_degree+1):
                d = total_degree-n
                assert degree_pair_obstructed(p,n,d,W,S), (p,n,d)
                checked_pairs += 1
        results.append((p,m,'minimum numerator+denominator degree',m-1))

    hole_cases = 0
    for p in primes_below(2000):
        if p % 24 != 13:
            continue
        m = (p-1)//6
        W,S,_ = weighted_ports(p)
        r0 = (p-13)//24
        assert 0 <= r0 < m and S[r0] == 0 and W[r0] != 0
        assert sum(s == 0 for s in S) == 1
        hole_cases += 1

    rat = [Fraction(1)]
    for r in [1,2]:
        rat.append(rat[-1] * Fraction(48*r*(3*r+1),
                                       (12*r-1)*(12*r+5)))
    assert rat == [Fraction(1), Fraction(192,187),
                   Fraction(129024,124729)]
    print('D25_R31_RATIONAL_WEIGHTED_OBSERVER_PASS',
          'p19_classes',sample_count,
          'ratio_indices',term_count,
          'pair_rank_tests',checked_pairs,
          'p13_weight_holes',hole_cases,
          'small_exact_minima',results)

if __name__ == '__main__':
    main()
