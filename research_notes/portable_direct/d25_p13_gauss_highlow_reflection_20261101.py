"""Exact certificate for the p=8t+5 clipped beta high/low p^2 port.

Author-side arithmetic only; NOT an H0/B0 native experiment or an accepted Result.
"""
from math import factorial


def primes(limit):
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            yield n


def beta_terms(p):
    mod = p**3
    inv576 = pow(576, -1, mod)
    terms = [1]
    for k in range(p - 1):
        terms.append(terms[-1] * (8*k+1) * (8*k+3) * inv576
                     * pow(k+1, -2, mod) % mod)
    return terms


def low_binomial_coefficients(p, a, b):
    inv9 = pow(9, -1, p)
    u = v = w = 1
    low = []
    for i in range(a + 1):
        low.append(u*v*w % p)
        if i < a:
            inv = pow(i + 1, -1, p)
            u = u*(a-i)*inv % p
            v = v*(b-i)*inv % p
            w = w*inv9 % p
    return low


def reflection_and_highlow(p, terms):
    assert p > 5 and p % 8 == 5
    t, a, b = (p-5)//8, (5*p-1)//8, (7*p-3)//8
    assert 0 < a < b < p-1 and p-b-1 == t
    mod = p**3
    low = low_binomial_coefficients(p, a, b)
    assert [x % p for x in terms[:a+1]] == low
    assert all(x % p == 0 for x in terms[a+1:b+1])
    assert all(x % (p*p) == 0 for x in terms[b+1:])
    q = 1
    prediction = direct_highlow = 0
    for j in range(t):
        high = p - 1 - j
        assert high >= b + 1
        actual_q = terms[high] // (p*p)
        assert actual_q % p == q, (p, j, actual_q, q)
        c = sum((8*(i-j)-7)*low[i] for i in range(j+1, a+1)) % p
        prediction = (prediction + 2*q*c) % p
        for i in range(j+1, a+1):
            direct_highlow = (direct_highlow + 2*(8*(i+high)+1)*terms[i]*terms[high]) % mod
        if j + 1 < t:
            q = q*576*(j+1)**2 * pow((8*j+13)*(8*j+15), -1, p) % p
    assert direct_highlow % (p*p) == 0
    assert direct_highlow // (p*p) == prediction, (p, prediction, direct_highlow)
    return prediction


def full_signed_tail(p, terms):
    mod = p**3
    s0 = [0]*(p+1); s1 = [0]*(p+1)
    for j in range(p-1, -1, -1):
        s0[j] = (s0[j+1]+terms[j]) % mod
        s1[j] = (s1[j+1]+j*terms[j]) % mod
    return sum(terms[i]*((8*i+1)*s0[p-i]+8*s1[p-i])
               for i in range(1, p)) % mod


def independent_terminal(p):
    mod = p**3
    numerator = 1
    for k in range(p-1):
        numerator = numerator*(8*k+1)*(8*k+3) % mod
    denominator = pow(576,p-1,mod)*pow(factorial(p-1),2,mod) % mod
    return numerator*pow(denominator,-1,mod) % mod


def main():
    tested = 0
    p13_class = 0
    cases = {}
    for p in primes(3000):
        if p <= 5 or p % 8 != 5:
            continue
        terms = beta_terms(p)
        actual_seed = terms[-1] // (p*p)
        assert terms[-1] % (p*p) == 0 and actual_seed == 1, (p,actual_seed)
        highlow = reflection_and_highlow(p,terms)
        if p in (13, 29, 37, 53, 61, 109, 373):
            assert independent_terminal(p) == terms[-1]
            tail = full_signed_tail(p,terms)
            cases[p] = (highlow, tail % (p*p), tail % p**3)
        tested += 1
        p13_class += (p % 24 == 13)
    assert (tested,p13_class) == (109,53), (tested,p13_class)
    assert cases[13][0] == 8
    assert cases[373][0] == 111
    print(f"PASS: {tested} primes p<=3000, p≡5 mod8; {p13_class} p≡13 mod24")
    print("p | (high-low clipped beta port)/p^2 mod p | full tail mod p^2 | full tail mod p^3")
    for p,vals in cases.items():
        print(p,*vals,sep=" | ")


if __name__ == "__main__":
    main()
