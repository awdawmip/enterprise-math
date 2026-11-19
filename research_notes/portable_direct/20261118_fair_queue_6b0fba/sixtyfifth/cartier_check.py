"""Finite-field point counts and exact integral recurrences for both genus-two forms."""
import json
from math import isqrt


def primes(limit):
    return [n for n in range(2, limit + 1) if all(n % d for d in range(2, isqrt(n) + 1))]


def field_counts(p, A=2, b=2):
    # F_{p²}=F_p[s]/(s²-b) and b is a quadratic nonresidue.
    assert pow(b, (p - 1) // 2, p) == p - 1

    def product(x, y):
        return ((x[0] * y[0] + b * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)

    def count(points):
        squares = {product(z, z) for z in points}
        total = 2 * ((b**3 % p, 0) in squares)  # both points above infinity or neither
        for z in points:
            u = product(z, product(z, z))
            v = product(u, u)
            f = ((1 - 2*A*u[0] + b**3*v[0]) % p, (-2*A*u[1] + b**3*v[1]) % p)
            total += 1 if f == (0, 0) else 2 * (f in squares)
        return total

    prime = count([(i, 0) for i in range(p)])
    square = count([(i, j) for i in range(p) for j in range(p)])
    return [prime, square]


def hasse(p, A=2, b=2):
    # Write F(x)=f(x³). Ordinary integer polynomial multiplication modulo p.
    terms = [1]
    for _ in range((p - 1) // 2):
        out = [0] * (len(terms) + 2)
        for i, t in enumerate(terms):
            out[i] += t
            out[i+1] -= 2*A*t
            out[i+2] += b**3*t
        terms = [c % p for c in out]
    return [[terms[(i*p-j)//3] if (i*p-j) % 3 == 0 else 0
             for j in (1, 2)] for i in (1, 2)]


def exact_coefficients(indices):
    # (1−4z+8z²)B'=(2−8z)B. Integer division is checked on every step.
    answer = {}
    previous, current = 0, 1
    for k in range(max(indices) + 1):
        if k in indices:
            answer[k] = current
        following, remainder = divmod((4*k+2)*current - 8*k*previous, k+1)
        assert remainder == 0
        previous, current = current, following
    # A second local check uses the equation f B²=1.
    initial = [answer[i] for i in range(65)]
    sq = [sum(initial[j]*initial[i-j] for j in range(i+1)) for i in range(65)]
    assert all(sq[i] - (4*sq[i-1] if i >= 1 else 0)
                      + (8*sq[i-2] if i >= 2 else 0) == (i == 0) for i in range(65))
    return answer


def power_order(n, p):
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def main():
    scoped = [p for p in primes(700) if p % 24 in (13, 19)]
    tall = {13: 4, 19: 3, 37: 3, 43: 2, 61: 2, 67: 2, 109: 2, 139: 2}
    lower = {p: 1 for p in scoped}
    depths = lower | tall
    chosen = set(range(65))
    for p, end in depths.items():
        chosen.add((p-1)//3-1)
        for r in range(end+1):
            chosen.update([(p**r-1)//3, 2*((p**r-1)//3)])
    general = [(p, n, i) for p in (13, 19, 37, 43) for n in range(p, 5001, p)
               for i in (1, 2) if n % 3 == i % 3]
    for p, n, i in general:
        chosen.add((n-i)//3)
        if n % (p*p) == 0:
            chosen.add((n//(p*p)-i)//3)
    vals = exact_coefficients(chosen)
    field_rows = {p: field_counts(p) for p in (13,19,37,43,61,67)}
    assert all(row == [p+1, p*p+1-4*p] for p, row in field_rows.items())
    generic = {}
    for p in (7, 13, 19, 31, 37):
        b = next(i for i in range(2,p) if pow(i,(p-1)//2,p) == p-1)
        sqrt_minus3 = next(i for i in range(p) if i*i % p == (-3) % p)
        cases = []
        for A in range(p):
            assert (A*A-b**3) % p != 0  # b nonsquare
            matrix = hasse(p,A,b)
            u = matrix[0][0]
            assert matrix == [[u,0],[0,-u % p]]
            n = u * pow(sqrt_minus3,-1,p) % p
            n = min(n,p-n)
            assert 3*n*n <= 4*p
            observed = field_counts(p,A,b)
            assert observed == [p+1,p*p+1-4*p+6*n*n]
            cases.append(n)
        generic[p] = dict(b=b, counts_by_abs_n={j:cases.count(j) for j in sorted(set(cases))})
    totals = {}
    for p, end in depths.items():
        assert hasse(p) == [[0,0],[0,0]]
        mod = p**(end+3)
        rows = []
        first_old = None
        for r in range(end+1):
            degree = (p**r-1)//3
            current = [vals[k] * pow(pow(2,3*k//2,mod),-1,mod) % mod
                       for k in (degree,2*degree)]
            mixed = (current[1] + 2*current[0]) % mod
            scale = (r+1)//2
            assert all(x % p**scale == 0 for x in current)
            assert mixed % p**scale == 0 and mixed//p**scale % p != 0
            diff = None
            if r == 1:
                first_old = mixed//p % p
                # Base derivative, P_n'(t)/t=2n(P_(n−1)(t)/t−P_n(t)).
                # (2 sqrt2)^(n−1)*t=2^(3n/2−2) for n even.
                k = degree
                pnm1_over_t = vals[k-1] * pow(pow(2,3*k//2-2,p),-1,p) % p
                slope_over_t = 2*k*(pnm1_over_t-current[0]) % p
                assert first_old*slope_over_t % p == p-1
            assert mixed//p**scale % p == (3 if r % 2 == 0 else first_old)
            if r >= 2:
                prior = rows[r-2]['raw']
                diff = [((current[i]-p*prior[i]) % p**(r+1)) for i in range(2)]
                assert all(x % p**r == 0 for x in diff)
                diff = [x//p**r for x in diff]
            rows.append(dict(r=r,raw=current,mixed_first=mixed//p**scale%p,
                             next_digits_two_step=diff))
        totals[p] = [dict(r=h['r'],scaled_first=[a//p**((h['r']+1)//2)%p for a in h['raw']],
                           mixed_first=h['mixed_first'],next_digits_two_step=h['next_digits_two_step'])
                     for h in rows] if p in tall else rows[1]['mixed_first']
    for p, n, i in general:
        r = power_order(n,p)
        prev = vals[(n//(p*p)-i)//3] if n % (p*p) == 0 else 0
        assert (vals[(n-i)//3] - p*prev) % p**r == 0
    print(json.dumps(dict(scoped_primes=scoped,cartier_zero_matrices=len(scoped),
          raw_polynomial_top_index=max(chosen),point_counts_prime_and_square=field_rows,
          generic_family_by_prime=generic,both_forms_general_indices=len(general),raw_legendre_towers=totals),
          ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
