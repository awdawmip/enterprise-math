"""Author exact-arithmetic checker: D25 all-order source moment closure.

This executes a classical rational/modular hypergeometric coefficient model,
not native CM, divided-power Frobenius or an admitted Source run.
"""
from fractions import Fraction
from math import comb


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


def direct_moments(p, order, modulus):
    r = 1
    result = [0] * (order + 1)
    for n in range(p):
        for j in range(order + 1):
            result[j] = (result[j] + pow(n, j, modulus) * r) % modulus
        if n < p - 1:
            numerator = (6*n + 1)*(3*n + 1)
            denominator = 36*(n + 1)*(n + 1)
            r = r*numerator*pow(denominator, -1, modulus) % modulus
    return result


def lifted_moments(p, order, modulus, M0, M1, exact_E=None):
    half = pow(2, -1, modulus)
    eighteenth = pow(18, -1, modulus)
    E = (-p*p if exact_E is None else exact_E) % modulus
    out = [M0 % modulus, M1 % modulus]
    for s in range(order-1):
        z = (half*out[s+1] + eighteenth*out[s] + E*eighteenth*pow(p, s, modulus)) % modulus
        for j in range(s):
            z += comb(s,j) * (out[j+2] + half*out[j+1] + eighteenth*out[j])
        out.append(z % modulus)
    return out


def rational_moments(p, order):
    b = Fraction(1)
    out = [Fraction(0) for _ in range(order + 1)]
    for n in range(p):
        r = b/Fraction(2**n)
        for s in range(order+1):
            out[s] += n**s * r
        if n < p-1:
            b *= Fraction((6*n+1)*(3*n+1), 18*(n+1)**2)
    return out


def check():
    total = 0
    selected = {}
    for p in list(range(7,1200))+[1327,19963]:
        if p % 6 != 1 or not is_prime(p):
            continue
        order = 9
        modulus = p**3
        actual = direct_moments(p, order, modulus)
        E = (18*actual[2] - 9*actual[1] - actual[0]) % modulus
        assert E == (-p*p) % modulus, (p,"boundary")
        predicted = lifted_moments(p, order, modulus, actual[0], actual[1])
        assert predicted == actual, (p,[(i,actual[i],predicted[i]) for i in range(order+1) if actual[i]!=predicted[i]])
        assert (36*actual[3] - 5*actual[0] -47*actual[1] + 3*p*p) % modulus == 0
        assert (648*actual[4] -335*actual[0]-3177*actual[1]+209*p*p) % modulus == 0
        total += 1
        if p in (7,13,19,373,1327,19963):
            selected[p]=(actual[:5],E)
    for p in (7,13,19):
        exact=rational_moments(p,7)
        E=18*exact[2]-9*exact[1]-exact[0]
        assert 36*exact[3]==5*exact[0]+47*exact[1]+(3+2*p)*E
        assert 648*exact[4]==335*exact[0]+3177*exact[1]+(209+90*p+36*p*p)*E
        for s in range(0,6):
            lhs=2*exact[s+2]
            rhs=sum(comb(s,j)*(exact[j+2]+exact[j+1]/2+exact[j]/18) for j in range(s+1)) + E*Fraction(p**s,18)
            assert lhs == rhs,(p,s)
    print(f"PASS {total} primes: exact mod-p^3 source moments M_0..M_9, all-order recurrence, boundary and M_3/M_4 corollaries")
    for p,(ms,e) in selected.items():
        print(f"p={p}: g={ms[0]}, d={ms[1]}, M2={ms[2]}, M3={ms[3]}, M4={ms[4]}, E={e}, modulus={p**3}")
    print("PASS Fraction polynomial identity and exact recurrence for p=7,13,19, moments M_0..M_7")


if __name__ == '__main__':
    check()
