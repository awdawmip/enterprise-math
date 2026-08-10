"""A nonlinear profinite ghost: locally solvable at every modulus, no integer root.

Consider

    F(x) = (x^2-13)(x^2-17)(x^2-221).

No factor has an integer zero because 13, 17 and 221 are nonsquares.  Yet F has
a zero modulo every positive integer.

Prime-power proof:

* p=2: 17 == 1 (mod 8), hence 17 is a square in Z_2;
* p=13: 17 == 4 (mod 13), with simple root 2, so Hensel lifting gives a
  root of x^2-17 at every 13-adic depth;
* p=17: 13 is a quadratic residue mod 17 (8^2 == 13), again with a simple
  root and Hensel lifts;
* any other odd p: if 13 or 17 is a quadratic residue, use it.  If both are
  nonresidues, then 221=13*17 is a residue because the two Legendre symbols
  multiply to +1.

For a general modulus, choose one factor root independently at every prime-power
component and combine the residues by CRT.  The resulting x makes the product F
zero modulo the whole modulus.

Thus finite modular solvability at every precision does **not** imply an integer
solution for a general nonlinear Diophantine predicate.  The positive local-global
theorem for ``A x=b`` depends on the extra fact that an integer lattice image is
profinite-closed; it is not a consequence of precision refinement alone.

Prime-by-prime one may choose compatible p-adic roots, producing a point of the
profinite completion ``Z_hat`` on which F vanishes, although no point of Z does.
This is a sharp "profinite ghost state" boundary between finite-precision
coherence and exact integer realization.

Quadratic residues, Hensel lifting, CRT and intersective polynomials are standard
prior mathematics.  This module provides an executable pressure-test witness for
the A2/P023 local-global architecture; it claims no novelty for the polynomial.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


CONSTANTS = (13, 17, 221)


def intersective_polynomial(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    square = value * value
    result = 1
    for constant in CONSTANTS:
        result *= square - constant
    return result


def _prime(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("prime must be an integer")
    if value < 2:
        raise ValueError("prime must be at least two")
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            raise ValueError("prime must be prime")
        divisor += 1
    return value


def legendre_symbol(value: int, prime: int) -> int:
    """Legendre symbol for an odd prime."""
    p = _prime(prime)
    if p == 2:
        raise ValueError("Legendre symbol requires an odd prime")
    residue = value % p
    if residue == 0:
        return 0
    power = pow(residue, (p - 1) // 2, p)
    if power == 1:
        return 1
    if power == p - 1:
        return -1
    raise AssertionError("Euler criterion returned an invalid Legendre value")


def chosen_square_factor_for_prime(prime: int) -> int:
    """Choose d in {13,17,221} that is a square in Z_p."""
    p = _prime(prime)
    if p == 2:
        return 17
    if p == 13:
        return 17
    if p == 17:
        return 13
    if legendre_symbol(13, p) == 1:
        return 13
    if legendre_symbol(17, p) == 1:
        return 17
    if legendre_symbol(221, p) != 1:
        raise AssertionError("quadratic-character product failed to supply a square factor")
    return 221


def _root_mod_prime(constant: int, prime: int) -> int:
    p = _prime(prime)
    if p == 2:
        return constant & 1
    root = next(
        (candidate for candidate in range(p) if candidate * candidate % p == constant % p),
        None,
    )
    if root is None:
        raise AssertionError("declared quadratic residue had no prime-field root")
    return root


def _hensel_lift_simple_square_root(
    constant: int,
    prime: int,
    exponent: int,
    root_mod_prime: int,
) -> int:
    p = _prime(prime)
    if p == 2:
        raise ValueError("simple odd-prime Hensel lift requires an odd prime")
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    root = root_mod_prime % p
    if (root * root - constant) % p:
        raise ValueError("initial root does not solve the equation modulo p")
    if (2 * root) % p == 0:
        raise ValueError("initial root is not simple modulo p")
    modulus = p
    for _level in range(1, exponent):
        candidate = next(
            (
                root + digit * modulus
                for digit in range(p)
                if (root + digit * modulus) ** 2 % (modulus * p)
                == constant % (modulus * p)
            ),
            None,
        )
        if candidate is None:
            raise AssertionError("simple Hensel square-root lift failed")
        root = candidate
        modulus *= p
    return root % modulus


def two_adic_root_17(exponent: int) -> int:
    """Return one root of x^2=17 modulo 2^exponent."""
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    modulus = 1 << exponent
    if exponent <= 3:
        root = next(
            candidate for candidate in range(modulus)
            if (candidate * candidate - 17) % modulus == 0
        )
        return root

    roots = {
        candidate
        for candidate in range(8)
        if (candidate * candidate - 17) % 8 == 0
    }
    current_modulus = 8
    for _level in range(3, exponent):
        next_modulus = current_modulus * 2
        roots = {
            candidate
            for root in roots
            for candidate in (root, root + current_modulus)
            if (candidate * candidate - 17) % next_modulus == 0
        }
        if not roots:
            raise AssertionError("2-adic square-root lift for 17 died")
        current_modulus = next_modulus
    return min(roots) % modulus


def factor_root_mod_prime_power(prime: int, exponent: int) -> tuple[int, int]:
    """Return ``(root,d)`` with root^2=d mod p^exponent and d a factor constant."""
    p = _prime(prime)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    constant = chosen_square_factor_for_prime(p)
    if p == 2:
        root = two_adic_root_17(exponent)
    else:
        initial = _root_mod_prime(constant, p)
        if (2 * initial) % p == 0:
            raise AssertionError("chosen odd-prime factor root was unexpectedly singular")
        root = _hensel_lift_simple_square_root(
            constant,
            p,
            exponent,
            initial,
        )
    modulus = p ** exponent
    if (root * root - constant) % modulus:
        raise AssertionError("prime-power factor root failed final verification")
    if intersective_polynomial(root) % modulus:
        raise AssertionError("factor root did not annihilate product polynomial")
    return root, constant


def _factor_prime_powers(modulus: int) -> tuple[tuple[int, int], ...]:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if modulus == 1:
        return ()
    remaining = modulus
    prime = 2
    result = []
    while prime * prime <= remaining:
        if remaining % prime:
            prime = 3 if prime == 2 else prime + 2
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        result.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        result.append((remaining, 1))
    return tuple(result)


def _crt_pair(left: int, left_modulus: int, right: int, right_modulus: int) -> tuple[int, int]:
    if left_modulus <= 0 or right_modulus <= 0:
        raise ValueError("CRT moduli must be positive")
    inverse = pow(left_modulus, -1, right_modulus)
    step = ((right - left) * inverse) % right_modulus
    combined_modulus = left_modulus * right_modulus
    combined = (left + left_modulus * step) % combined_modulus
    return combined, combined_modulus


def polynomial_root_modulus(modulus: int) -> int:
    """Construct a root of F modulo every positive modulus by prime-power CRT."""
    factors = _factor_prime_powers(modulus)
    if not factors:
        return 0
    residue = 0
    current_modulus = 1
    for prime, exponent in factors:
        component_modulus = prime ** exponent
        root, _constant = factor_root_mod_prime_power(prime, exponent)
        residue, current_modulus = _crt_pair(
            residue,
            current_modulus,
            root,
            component_modulus,
        )
    if current_modulus != modulus:
        raise AssertionError("CRT reconstruction lost original modulus")
    if intersective_polynomial(residue) % modulus:
        raise AssertionError("CRT polynomial root failed final modulus check")
    return residue


def polynomial_has_integer_root() -> bool:
    """False because an integer zero would force x^2 in {13,17,221}."""
    return any(isqrt(constant) ** 2 == constant for constant in CONSTANTS)


@dataclass(frozen=True)
class ProfiniteGhostReport:
    constants: tuple[int, ...]
    has_integer_root: bool
    checked_modulus_max: int
    all_checked_moduli_have_roots: bool


def profinite_ghost_report(checked_modulus_max: int) -> ProfiniteGhostReport:
    if isinstance(checked_modulus_max, bool) or not isinstance(checked_modulus_max, int):
        raise TypeError("checked_modulus_max must be an integer")
    if checked_modulus_max <= 0:
        raise ValueError("checked_modulus_max must be positive")
    all_local = all(
        intersective_polynomial(polynomial_root_modulus(modulus)) % modulus == 0
        for modulus in range(1, checked_modulus_max + 1)
    )
    global_root = polynomial_has_integer_root()
    if global_root:
        raise AssertionError("intersective polynomial unexpectedly gained an integer root")
    if not all_local:
        raise AssertionError("bounded profinite ghost regression lost local solvability")
    return ProfiniteGhostReport(
        constants=CONSTANTS,
        has_integer_root=global_root,
        checked_modulus_max=checked_modulus_max,
        all_checked_moduli_have_roots=all_local,
    )
