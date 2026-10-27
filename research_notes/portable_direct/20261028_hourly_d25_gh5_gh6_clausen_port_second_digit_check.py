#!/usr/bin/env python3
"""GH-5/GH-6 author-side exact modular checks; no native experiment or review."""
from fractions import Fraction
from math import isqrt


def primes_below(bound):
    sieve = bytearray(b"\x01") * bound
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(bound - 1) + 1):
        if sieve[p]:
            sieve[p*p:bound:p] = b"\x00" * ((bound - 1 - p*p)//p + 1)
    return [p for p in range(5, bound) if sieve[p]]


def t_scalar(p, modulus):
    d = (p-1)//4
    coeff = total = 1
    for r in range(d):
        coeff = (coeff * 9 * (4*r+1)**3
                 * pow(4*(4*r+2)*(4*r+3)*(r+1), -1, modulus)) % modulus
        total = (total + (8*r+9)*coeff) % modulus
    return total


def gh5_port(p):
    """Original labelled middle source; independent first-order deformation check."""
    assert p % 24 == 19
    a, b, h, d = (p-3)//8, (3*p-1)//8, (p-1)//2, (p-3)//4
    modulus = p*p
    normalized, beta = 1, []
    for k in range(b):
        numerator = (8*k+1)*(8*k+3)
        if k == a:
            assert numerator % p == 0
            numerator //= p
        else:
            assert numerator % p != 0
        normalized = (normalized * numerator
                      * pow(576*(k+1)**2, -1, modulus)) % modulus
        if k+1 > a:
            beta.append(normalized)
    assert len(beta) == d+1 and beta[-1] % p
    tail_inv = pow(beta[-1], -1, modulus)
    reversed_original = [value*tail_inv % modulus for value in beta[::-1]]

    g, harmonic, c = [1], [0], [1]
    for r in range(d):
        g.append(g[-1]*9*(8*r+1)**2
                 * pow(16*(r+1)*(4*r+3), -1, modulus) % modulus)
        harmonic.append((harmonic[-1] + pow(8*r+8, -1, p)
                         + pow(8*r+6, -1, p)
                         - 2*pow(8*r+1, -1, p)) % p)
        c.append(c[-1]*9*(4*r+1)**3
                 * pow(4*(4*r+2)*(4*r+3)*(r+1), -1, modulus) % modulus)
    for r in range(d+1):
        assert reversed_original[r] == g[r]*(1+3*p*harmonic[r]) % modulus

    t = sum((8*r+1)*c[r] for r in range(d+1)) % modulus
    assert t == t_scalar(p, modulus)
    c_sum = sum(c) % p
    k_sum = sum((8*(r+s)+1)*g[r]*g[s]*(harmonic[r]+harmonic[s])
                for r in range(d+1) for s in range(d+1-r)) % p
    original_port = sum((8*(i+j)+1)*beta[i-a-1]*beta[j-a-1]
                        for i in range(a+1,b+1) for j in range(a+1,b+1)
                        if i+j > h) % modulus
    predicted = beta[-1]**2*(-t+p*(6*c_sum-3*k_sum)) % modulus
    assert original_port == predicted, (p, original_port, predicted)
    return {
        "p":p, "T_over_p": t//p if t % p == 0 else None,
        "C":c_sum, "K":k_sum,
        "port_mod_p2":original_port,
        "normalized_port_mod_p2":original_port*pow(beta[-1], -2, modulus)%modulus,
        "lift_digit":((predicted*pow(beta[-1], -2, modulus))%modulus)//p
            if predicted % p == 0 else None,
    }


def exact_rational_port_check(p):
    a, b, h = (p-3)//8, (3*p-1)//8, (p-1)//2
    u = Fraction(1)
    beta = {}
    for k in range(b):
        u *= Fraction((8*k+1)*(8*k+3), 576*(k+1)**2)
        if k+1 > a:
            beta[k+1] = u/p
    true_port = sum(((8*(i+j)+1)*beta[i]*beta[j]
                     for i in beta for j in beta if i+j > h), Fraction(0))
    assert true_port.denominator % p != 0
    port_mod = true_port.numerator * pow(true_port.denominator, -1, p*p) % (p*p)
    assert port_mod == gh5_port(p)["port_mod_p2"]
    numerator = true_port.numerator
    valuation = 0
    while numerator and numerator % p == 0:
        numerator //= p
        valuation += 1
    return valuation, numerator * pow(true_port.denominator, -1, p) % p


def main():
    primes = primes_below(10000)
    double_zero = []
    for p in primes:
        residue = t_scalar(p, p*p)
        assert residue % p == 0, ("T_mod_p", p, residue)
        if residue == 0:
            double_zero.append(p)
    assert not double_zero, ("T_mod_p2_exception", double_zero)
    print("OBSERVATION T_p has exact p-valuation 1 for primes 5<=p<10000:", len(primes))

    q19 = [p for p in primes if p % 24 == 19 and p < 2000]
    elevated = []
    for p in q19:
        packet = gh5_port(p)
        assert packet["T_over_p"] is not None
        if packet["port_mod_p2"] == 0:
            elevated.append(p)
    assert elevated == [43], elevated
    assert exact_rational_port_check(19)[0] == 1
    assert exact_rational_port_check(43) == (2, 22)
    assert gh5_port(19)["normalized_port_mod_p2"] == 76
    assert gh5_port(43)["port_mod_p2"] == 0
    print("PASS GH5 exact original source/p-adic lift, p≡19 mod24 <2000:", len(q19))
    print("GH6 enhanced port valuation in scanned 19-class:", elevated)
    for p in (19,43,67,139,181,211,283,373):
        if p % 24 == 19:
            print("CERT", gh5_port(p))
    print("PASS GH5_GH6_AUTHOR_SIDE")


if __name__ == "__main__":
    main()
