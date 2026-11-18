"""Reflection of the Franel companion and modular endpoint jets. Standard library."""
from fractions import Fraction
from math import comb, isqrt
import json


def primes_through(bound):
    flags = bytearray(b'\1') * (bound + 1)
    flags[:2] = b'\0\0'
    for p in range(2, isqrt(bound) + 1):
        if flags[p]:
            flags[p*p::p] = b'\0' * ((bound - p*p)//p + 1)
    return [i for i in range(2, bound+1) if flags[i]]


def bernoulli(bound):
    values = [Fraction(1)]
    for n in range(1, bound+1):
        values.append(-sum(comb(n+1, j)*values[j] for j in range(n)) / (n+1))
    return values


def residue(a, modulus):
    return a.numerator * pow(a.denominator, -1, modulus) % modulus


def solutions(p, modulus):
    f, g = [1, 2 % modulus], [0, 1]
    for j in range(1, p-1):
        inv = pow((j+1)**2, -1, modulus)
        for values in (f, g):
            values.append(((7*j*(j+1)+2)*values[-1]+8*j*j*values[-2])*inv % modulus)
    return f, g


def multiply(a, b, modulus):
    return [sum(a[k]*b[j-k] for k in range(j+1)) % modulus for j in range(len(a))]


def direct_deformation(n, r, modulus, degree):
    """Expand both rising-factorial denominators independently for each k."""
    one = [1] + [0]*degree
    rising, falling = [one], [one]
    for j in range(1, n+1):
        inv = pow(j, -1, modulus)
        for previous, sign in ((rising, -1), (falling, 1)):
            step = [comb(r+i-1, i)*pow(sign*inv, i, modulus) % modulus
                    for i in range(degree+1)]
            previous.append(multiply(previous[-1], step, modulus))
    result = [0] * (degree+1)
    for k in range(n+1):
        terms = multiply(rising[k], falling[n-k], modulus)
        scale = pow(comb(n,k), r, modulus)
        result = [(a+scale*b) % modulus for a,b in zip(result, terms)]
    return result


def main():
    b = bernoulli(246)
    primes = [p for p in primes_through(2000) if p >= 5]
    endpoint_tests = derivative_tests = even_tests = 0
    for p in primes:
        f, g = solutions(p, p*p)
        factor = 1
        for n in range(p):
            assert (factor*f[p-1-n]-f[n]) % p == 0
            assert (factor*g[p-1-n]+g[n]) % p == 0
            factor = -8*factor % p
        m = (p-1)//2
        if pow(-8, m, p) == 1:
            assert g[m] % p == 0 and 2*f[m]*g[m-1] % p == 1
        else:
            assert f[m] % p == 0 and 2*g[m]*f[m-1] % p == 1
        assert f[-1] == (1+3*(pow(2, p-1, p*p)-1)) % (p*p)
        if p <= 241:
            expected = p*residue(Fraction(7,48)*b[p-3],p)
            assert g[-1] == expected
            endpoint_tests += 1
        if p <= 67:
            for r in (2, 4, 6):
                degree = min(12, p-2)
                values = direct_deformation(p-1, r, p*p, degree)
                assert values == [p*(1-r) % (p*p)] + [0]*degree
                even_tests += 1
            for r in (1, 3, 5, 7):
                degree = min(12,p-3)
                direct = direct_deformation(p-1, r, p*p, degree)
                for d in range(2, degree+1, 2):
                    coefficient = r*Fraction(2*2**d-1,2**d*(d+1))*b[p-1-d]
                    assert direct[d] == p*residue(coefficient,p)
                    derivative_tests += 1
    # Verify both exact deformation initial data and row recurrence at small n.
    p = 1009
    f, g = solutions(p,p*p)
    for n in range(40):
        coeff = direct_deformation(n,3,p*p,2)
        assert coeff == [f[n], 0, 12*g[n] % (p*p)]
    samples = []
    for p in (5, 7, 11, 269, 16843):
        mod = p**3
        f, g = solutions(p,mod)
        assert g[-1] % p == 0
        samples.append({"p":p, "G_last_mod_p3":g[-1], "G_last_div_p_mod_p":g[-1]//p%p,
                        "F_last_mod_p2":f[-1]%(p*p)})
        if p in (7,16843):
            assert g[-1] % (p*p) == 0
    print(json.dumps({"reflection_primes":len(primes),"largest_reflection_prime":primes[-1],
                      "direct_Bernoulli_companion_comparisons":endpoint_tests,
                      "independent_deformed_even_jet_comparisons":derivative_tests,
                      "even_power_row_comparisons":even_tests,
                      "direct_early_row_comparisons":40,"endpoints":samples},indent=2))


if __name__ == "__main__":
    main()
