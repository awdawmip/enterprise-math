"""Exact boundary-cancellation checks for the original weighted-216 scalar observer.

This is portable author-side mathematics, not a native H0/B0 evaluation.
No dependencies outside the Python standard library.
"""

from math import comb

PRIMES = (5, 7, 11, 13, 19, 31, 37, 43, 61, 67, 73, 211, 373)


def check_prime(p: int) -> dict[str, int]:
    modulus = p**4

    def coefficient(n: int) -> int:
        # 216 is a p-adic unit for the selected primes.
        return (comb(2*n, n)**2 * comb(3*n, n) * pow(216, -n, modulus)) % modulus

    # Independent original integer-binomial and forward-recurrence sequences.
    direct = [coefficient(n) for n in range(p+1)]
    forward = [1]
    for n in range(p-2):
        a = (2*n+1)*(3*n+1)*(3*n+2)
        b = 36*(n+1)**3
        forward.append(forward[-1]*a*pow(b, -1, modulus) % modulus)
    assert forward == direct[:p-1], (p, "recurrence differs")

    weighted = sum((6*n+1)*direct[n] for n in range(p)) % modulus
    interior = sum(
        (66*n*n+113*n+49)*forward[n]*pow(9*(n+1)**3, -1, modulus)
        for n in range(p-1)
    ) % modulus
    boundary = (11-6*p)*direct[p-1] % modulus

    # Exact rational identity, independently reduced modulo p^4.
    assert (weighted-(interior-4+boundary)) % modulus == 0
    # Coefficient valuation, matching t_{p-1}/p^3 = -1 (mod p).
    assert direct[p-1] % p**3 == 0
    assert direct[p-1]//p**3 % p == p-1
    # Two-source upper boundary cancels in the p^3 readout.
    assert boundary % p**3 == 0
    assert boundary == (-11*p**3) % modulus
    # Original recurrence across the non-unit denominator requires cross multiplication.
    upper_denominator = (2*p-1)*(3*p-2)*(3*p-1)
    assert (upper_denominator*direct[p-1]-36*p**3*direct[p]) % modulus == 0
    assert (weighted-(interior-4-11*p**3)) % modulus == 0
    return {
        "p": p,
        "weighted_mod_p3": weighted % p**3,
        "interior_mod_p3": interior % p**3,
        "weighted_mod_p4": weighted,
        "interior_mod_p4": interior,
        "boundary_mod_p4": boundary,
    }


if __name__ == "__main__":
    answers = [check_prime(p) for p in PRIMES]
    fixed = answers[-1]
    assert fixed == {
        "p": 373,
        "weighted_mod_p3": 373,
        "interior_mod_p3": 377,
        "weighted_mod_p4": 11832087049,
        "interior_mod_p4": 12402933340,
        "boundary_mod_p4": 18786032354,
    }
    print("PASS_D25_ORIGINAL216_ENDPOINT_P4_EXACT_BOUNDARY", len(answers), "primes")
    print("p373", fixed)
