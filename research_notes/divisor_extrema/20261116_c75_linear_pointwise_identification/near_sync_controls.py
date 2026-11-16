"""Reproduce the fixed-odd-K quadratic-window controls using integer arithmetic."""
import argparse
import json
from fractions import Fraction as Q
from math import comb


def centered_coefficients(k):
    # Independently substitute G(n)=n^d*(1+t1/n+t2/n²+...) into its recurrence.
    d = 3*k
    left = Q(k+4, 4)
    right = k+1
    terms = [Q(1)]
    for j in (1, 2):
        residual = Q(0)
        for i, t in enumerate(terms):
            m = j+1-i
            for u in range(min(4, m)+1):
                if m-u <= d-i:
                    residual += t*comb(4, u)*left**u*comb(d-i, m-u)
            if m <= 4:
                residual -= t*comb(4, m)*right**m
        terms.append(residual/j)
    mu = terms[1]/d
    correction = terms[2]/d-(d-1)*terms[1]**2/(2*d*d)
    assert mu == Q(5*k+4, 8)
    assert correction == (1-Q(3*k, 4)**2)/24
    return dict(K=k, mu=str(mu), correction=str(correction))


def scan(k, limit):
    # rho increases in s, decreases in n. Follow the first s at/above 1.
    s = 2
    upper = Q(4*s+k, s+k)
    exponents = (2, 3, 8)
    hits = {e: [] for e in exponents}
    boundary_data = []
    for n in range(2, limit+1):
        if n > 2:
            upper *= Q(4*n+k, 4*(n+k))
        while upper < 1:
            upper *= Q(4*(s+k), 4*s+k)
            s += 1
        assert s <= n
        un, ud = upper.as_integer_ratio()
        candidates = [(s, un-ud, ud)]
        if s > 2:
            ln, ld = un*(4*(s-1)+k), ud*4*(s-1+k)
            assert 0 < ln < ld
            candidates.append((s-1, ld-ln, ld))
        for w, numer, denom in candidates:
            if numer*n*n <= denom:
                boundary_data.append(dict(n=n, s=w, above_one=(w==s),
                                          floor_1e8_times_n2_error=numer*n*n*10**8//denom))
            for e in exponents:
                if numer * n**e <= denom:
                    hits[e].append([n,w])
        if n <= 48:
            exact = Q(4)
            direct = {e: [] for e in exponents}
            for w in range(n, 1, -1):
                exact *= Q(4*w+k, 4*(w+k))
                for e in exponents:
                    if abs(1-exact)*n**e <= 1:
                        direct[e].append([n,w])
            for e in exponents:
                assert sorted(direct[e]) == sorted(pair for pair in hits[e] if pair[0] == n)
        # For K=3, no other s can enter even the widest scan window 1/n².
        # Adjacent likelihood ratio is >=1+9/(4*n+3); this exceeds
        # (1+n^-2)/(1-n^-2) for n>=3. n=2 is in the direct control.
        if n >= 3:
            assert 3*k*(n*n-1) > 2*(4*n+k)
    return {str(e): hits[e] for e in exponents}, boundary_data


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=65536)
    args=parser.parse_args()
    hits, boundary_data = scan(3,args.limit)
    result = dict(coefficients=[centered_coefficients(k) for k in (1,3,5,7,9,11)],
                  K=3, max_n=args.limit, inclusive_hits_by_exponent=hits, quadratic_hits_details=boundary_data)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
