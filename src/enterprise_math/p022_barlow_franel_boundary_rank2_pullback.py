"""Rank-two Franel pullback and cusp-transfer structure for the P022 boundary.

Prior-art interface (Caruso--Fuernsinn--Vargas-Montoya--Zudilin, 2026):

    h(x) = 1/(1-2x) * 2F1(1/3,2/3;1; 27x^2/(1-2x)^3)

for the Franel generating series h(x)=sum F_n x^n, and, modulo primes
p=5 (mod 6), the p-Lucas truncation H_p obeys three projective involution
relations.  This module freezes the P022-specific exact consequences:

* coefficient extraction from the rank-two pullback gives

      F_(2M) = 4^M * 3F2(-M,1/2-M,2M+1;1,1;1),

  so at p=6M-1 it specializes termwise to the already-frozen fixed
  one-third Franel obstruction with parameters (-1/6,1/3,4/3);

* the finite mod-p rank-two Hasse pullback reconstructs the complete Franel
  truncation H_p;

* the three cusp involutions give exact 2x2 first-jet transfer matrices.
  In particular the transfer from x=1/8 to x=0 has determinant -9/8, whose
  quadratic character is (-2/p), exactly the Jarvis--Verrill half-index
  residue discriminator.

The last coincidence is a structural bridge, not a proof that a one-third
Franel zero forces (-2/p)=-1.  That implication remains open.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

from .p022_barlow_franel_half_index import minus_two_legendre_from_residue
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_inert_cubic_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 5
        or not _is_prime(prime)
        or prime % 6 != 5
    ):
        raise ValueError("prime must be an odd prime congruent to 5 modulo 6")
    return (prime + 1) // 6


def multinomial_three(index: int) -> int:
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    return factorial(3 * index) // factorial(index) ** 3


def franel_rank2_pullback_coefficient(index: int) -> int:
    """Extract [x^index] from the exact rank-two Franel pullback."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    total = 0
    for k in range(index // 2 + 1):
        total += (
            multinomial_three(k)
            * 2 ** (index - 2 * k)
            * comb(index + k, index - 2 * k)
        )
    return total


def even_franel_rank2_hypergeometric(index: int) -> Fraction:
    """Return the terminating 3F2 factor S_M with F_(2M)=4^M S_M."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    M = index
    term = Fraction(1)
    total = term
    for k in range(M):
        term *= (
            Fraction(-M + k, k + 1)
            * Fraction(1 - 2 * M + 2 * k, 2 * (k + 1))
            * Fraction(2 * M + 1 + k, k + 1)
        )
        total += term
    return total


def exact_even_franel_rank2_identity(index: int) -> bool:
    """Certify F_(2M)=4^M*3F2(-M,1/2-M,2M+1;1,1;1)."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    left = franel_rank2_pullback_coefficient(2 * index)
    right = Fraction(4**index) * even_franel_rank2_hypergeometric(index)
    if right.denominator != 1 or left != right.numerator:
        raise AssertionError("rank-two coefficient extraction identity failed")
    if left != triple_moment_factor(2 * index):
        raise AssertionError("rank-two pullback coefficient disagrees with Franel number")
    return True


def rank2_hasse_multinomial_coefficients(prime: int) -> tuple[int, ...]:
    """Return 27^k*(1/3)_k(2/3)_k/(k!)^2 mod p through its live degree."""
    M = _require_inert_cubic_prime(prime)
    degree = 2 * M - 1
    return tuple(multinomial_three(k) % prime for k in range(degree + 1))


def rank2_pullback_franel_hasse_coefficients(prime: int) -> tuple[int, ...]:
    """Reconstruct H_p=sum_(n<p)F_n x^n from the finite rank-two pullback.

    For p=6M-1 and N=2M-1,

        H_p(x)=sum_(k=0)^N (3k)!/(k!)^3 * x^(2k)
                 * (1-2x)^(p-1-3k)              (mod p).
    """
    M = _require_inert_cubic_prime(prime)
    degree = 2 * M - 1
    output = [0] * prime
    for k, coefficient in enumerate(rank2_hasse_multinomial_coefficients(prime)):
        exponent = prime - 1 - 3 * k
        if exponent < 0:
            raise AssertionError("rank-two live truncation exceeded polynomial range")
        for j in range(exponent + 1):
            target = 2 * k + j
            if target >= prime:
                raise AssertionError("finite pullback must have degree at most p-1")
            output[target] = (
                output[target]
                + coefficient * comb(exponent, j) * pow(-2, j, prime)
            ) % prime
    for n, coefficient in enumerate(output):
        if coefficient != triple_moment_factor(n) % prime:
            raise AssertionError("rank-two finite pullback failed to reconstruct H_p")
    return tuple(output)


def rank2_boundary_coefficient_identity(prime: int) -> tuple[int, int]:
    """Return (M,F_(2M) mod p) and certify the fixed-parameter specialization."""
    M = _require_inert_cubic_prime(prime)
    exact_even_franel_rank2_identity(M)
    reconstructed = rank2_pullback_franel_hasse_coefficients(prime)[2 * M]
    direct = triple_moment_factor(2 * M) % prime
    if reconstructed != direct:
        raise AssertionError("rank-two boundary coefficient changed")

    # Termwise parameter specialization at p=6M-1:
    # -M=-1/6, 1/2-M=1/3, 2M+1=4/3 modulo p.
    inv6 = pow(6, -1, prime)
    if (-M - (-inv6)) % prime:
        raise AssertionError("-M did not specialize to -1/6")
    if (Fraction(1, 2) - M).numerator * pow((Fraction(1, 2) - M).denominator, -1, prime) % prime != pow(3, -1, prime):
        raise AssertionError("1/2-M did not specialize to 1/3")
    if (2 * M + 1) % prime != 4 * pow(3, -1, prime) % prime:
        raise AssertionError("2M+1 did not specialize to 4/3")
    return M, direct


def franel_cusp_states(prime: int) -> dict[str, tuple[int, int]]:
    """Return the exact first-jet states at 0, -1, and 1/8 modulo p.

    For p=5 mod 6, prior-art involution relations give H(-1)=H(1/8)=-1.
    The rank-two Franel differential equation then forces

        H'(0)=2,
        H'(-1)=-2/3,
        H'(1/8)=8/3.
    """
    _require_inert_cubic_prime(prime)
    inv3 = pow(3, -1, prime)
    return {
        "0": (1, 2 % prime),
        "minus_one": ((-1) % prime, (-2 * inv3) % prime),
        "one_eighth": ((-1) % prime, (8 * inv3) % prime),
    }


def cusp_transfer_matrices(prime: int) -> dict[str, tuple[tuple[int, int], tuple[int, int]]]:
    """Return exact 2x2 first-jet transfer matrices into the x=0 cusp.

    A maps the state at x=1/8 to x=0 using
      sigma_A=(1-8x)/(8+8x), H=-(1+x)^(p-1) H(sigma_A).

    D maps the state at x=-1 to x=0 using
      sigma_D=(1+x)/(8x-1), H=-(8x-1)^(p-1) H(sigma_D).
    """
    _require_inert_cubic_prime(prime)
    inv8 = pow(8, -1, prime)
    A = (((-1) % prime, 0), (1, 9 * inv8 % prime))
    D = (((-1) % prime, 0), ((-8) % prime, 9 % prime))

    states = franel_cusp_states(prime)
    for name, matrix, source in (
        ("A", A, states["one_eighth"]),
        ("D", D, states["minus_one"]),
    ):
        image = (
            (matrix[0][0] * source[0] + matrix[0][1] * source[1]) % prime,
            (matrix[1][0] * source[0] + matrix[1][1] * source[1]) % prime,
        )
        if image != states["0"]:
            raise AssertionError(f"{name} cusp-transfer matrix failed")
    return {"A": A, "D": D}


def one_eighth_to_minus_one_transfer(prime: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return the constant cusp transfer v_(1/8)=[[1,0],[-8,8]] v_(-1)."""
    _require_inert_cubic_prime(prime)
    matrix = ((1, 0), ((-8) % prime, 8 % prime))
    source = franel_cusp_states(prime)["minus_one"]
    target = (
        (matrix[0][0] * source[0] + matrix[0][1] * source[1]) % prime,
        (matrix[1][0] * source[0] + matrix[1][1] * source[1]) % prime,
    )
    if target != franel_cusp_states(prime)["one_eighth"]:
        raise AssertionError("inter-cusp rank-two transfer failed")
    return matrix


def cusp_transfer_determinant_characters(prime: int) -> tuple[int, int, int]:
    """Return characters of det(A), det(D), and the inter-cusp determinant.

    det(A)=-9/8 has Legendre character (-2/p); this exactly matches the
    Jarvis--Verrill half-index discriminator.  No implication from a one-third
    Franel zero to this character is asserted.
    """
    _require_inert_cubic_prime(prime)
    matrices = cusp_transfer_matrices(prime)
    A = matrices["A"]
    D = matrices["D"]
    det_a = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % prime
    det_d = (D[0][0] * D[1][1] - D[0][1] * D[1][0]) % prime
    inter = one_eighth_to_minus_one_transfer(prime)
    det_i = (inter[0][0] * inter[1][1] - inter[0][1] * inter[1][0]) % prime

    def char(value: int) -> int:
        residue = pow(value % prime, (prime - 1) // 2, prime)
        if residue == 1:
            return 1
        if residue == prime - 1:
            return -1
        raise AssertionError("transfer determinant must be a p-unit")

    chars = (char(det_a), char(det_d), char(det_i))
    if chars[0] != minus_two_legendre_from_residue(prime):
        raise AssertionError("det(A) character must equal (-2/p)")
    return chars
