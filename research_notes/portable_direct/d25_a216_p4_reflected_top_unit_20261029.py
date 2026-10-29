"""Exact p^4 A216 reflected top-tier checker (standard library only).
Author-side evidence, not native H0/B0 or an accepted Result.
"""
from math import comb, factorial, isqrt


def run(p):
    q = p**4
    a = [1]
    for n in range(p-1):
        a.append(a[-1]*(2*n+1)*(3*n+1)*(3*n+2)
                 * pow(36*(n+1)**3, -1, q) % q)
    top = (p-3)//3
    reflected = 0
    for r in range(top+1):
        n = p-1-r
        w = (6*n+1)*a[n] % q
        assert w % p**3 == 0
        v = w//p**3
        d = (2*r+1)*(3*r+1)*(3*r+2)
        assert v*a[r]*d % p == 2*(6*r+5) % p
        t = (2*(6*r+5)*pow(216,r,p)*factorial(r)**5
             * pow(factorial(2*r+1)*factorial(3*r+2), -1, p)) % p
        assert v == t
        reflected = (reflected+t) % p
    full = sum((6*n+1)*a[n] for n in range(p)) % q
    chi = 1 if p % 3 == 1 else -1
    assert (full-p*chi) % p**3 == 0  # finite test, NOT a proof
    if p in (13,19,373):
        inv = pow(216,-1,q)
        literal = sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(inv,n,q)
                      for n in range(p)) % q
        assert literal == full
    return top+1, reflected, ((full-p*chi)//p**3) % p


def main():
    counts = pairs = 0
    zero_tail, zero_defect, samples = [], [], {}
    for p in range(5,1500):
        if any(p % d == 0 for d in range(2,isqrt(p)+1)):
            continue
        t, tail, defect = run(p)
        counts += 1
        pairs += t
        if tail == 0: zero_tail.append(p)
        if defect == 0: zero_defect.append(p)
        if p in (5,7,11,13,19,37,43,73,373):
            samples[p] = (t,tail,defect)
    print('PASS_A216_P4_REFLECTED_TOP',counts,'primes',pairs,'pairs')
    print('zero_tail',zero_tail,'zero_total_p4_defect',zero_defect)
    print('samples (top_terms,tail/p^3,total_defect)',samples)


if __name__ == '__main__':
    main()
