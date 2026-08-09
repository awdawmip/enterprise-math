"""Half-index Franel divisibility forced by the Jarvis--Verrill mirror congruence.

For every odd prime p and 0<=k<=p-1, Jarvis--Verrill proved

    F_k == (-8)^k F_(p-1-k)  (mod p),

where F_n=sum_j C(n,j)^3 is the Franel sequence.  At the fixed midpoint
n=(p-1)/2, Euler's criterion turns the multiplier into the Legendre symbol
(-8/p)=(-2/p).  Therefore p divides F_n whenever p==5 or 7 (mod 8).

Combining this with p==2 (mod 3) gives an infinite P022 composite-boundary
subfamily: for primes p==5 or 23 (mod 24), p>5, n=(p-1)/2 has
2n-1=p-2 divisible by three while p divides F_n.

The stronger empirical statement v_p(D_n)=1 for the corresponding pure Franel
defect is intentionally *not* asserted here.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def jarvis_verrill_mirror_residues(prime: int, index: int) -> tuple[int, int]:
    """Return both sides of F_k == (-8)^k F_(p-1-k) mod p."""
    _require_odd_prime(prime)
    if (
        isinstance(index, bool)
        or not isinstance(index, int)
        or not 0 <= index <= prime - 1
    ):
        raise ValueError("index must lie in 0..p-1")
    left = triple_moment_factor(index) % prime
    reflected = prime - 1 - index
    right = (
        pow(-8, index, prime) * (triple_moment_factor(reflected) % prime)
    ) % prime
    return left, right


def mirror_congruence_holds(prime: int, index: int) -> bool:
    left, right = jarvis_verrill_mirror_residues(prime, index)
    return left == right


def minus_two_legendre_from_residue(prime: int) -> int:
    """Return (-2/p) from the residue class modulo eight."""
    _require_odd_prime(prime)
    residue = prime % 8
    if residue in (1, 3):
        return 1
    if residue in (5, 7):
        return -1
    raise AssertionError("odd prime must lie in 1,3,5,7 modulo eight")


def half_index(prime: int) -> int:
    _require_odd_prime(prime)
    return (prime - 1) // 2


def half_index_is_forced_zero(prime: int) -> bool:
    """Whether the mirror congruence forces F_((p-1)/2)=0 mod p."""
    return minus_two_legendre_from_residue(prime) == -1


def verify_forced_half_index_divisibility(prime: int) -> bool:
    """Certify the exact forced-zero implication for one prime."""
    _require_odd_prime(prime)
    if not half_index_is_forced_zero(prime):
        raise ValueError("this residue class is not forced to vanish by the mirror theorem")
    index = half_index(prime)
    left, right = jarvis_verrill_mirror_residues(prime, index)
    if left != right:
        raise AssertionError("Jarvis--Verrill mirror congruence failed")
    multiplier = pow(-8, index, prime)
    # Euler criterion gives multiplier=(-2/p)=-1 in this branch.
    if multiplier != prime - 1:
        raise AssertionError("half-index multiplier must be -1 modulo p")
    if left != 0:
        raise AssertionError("2*F_half=0 modulo an odd prime must force F_half=0")
    return True


def composite_boundary_half_witness(prime: int) -> tuple[int, int]:
    """Return (n,p) for the infinite residue family p=5 or 23 mod 24.

    For p>5 in these classes, n=(p-1)/2 satisfies:
      * p divides F_n;
      * 2n-1=p-2 is divisible by three and exceeds three, hence composite.
    Infinitude of the prime residue classes is Dirichlet prior art and is not
    computationally asserted by this finite helper.
    """
    _require_odd_prime(prime)
    if prime <= 5 or prime % 24 not in (5, 23):
        raise ValueError("prime must exceed five and lie in 5 or 23 modulo 24")
    segment = half_index(prime)
    odd_boundary = 2 * segment - 1
    if odd_boundary != prime - 2 or odd_boundary % 3:
        raise AssertionError("residue arithmetic for the composite boundary failed")
    if _is_prime(odd_boundary):
        raise AssertionError("p-2 must be composite in the declared residue family")
    if not verify_forced_half_index_divisibility(prime):
        raise AssertionError("half-index Franel divisibility failed")
    return segment, prime


def mirror_zero_set_is_symmetric(prime: int, index: int) -> bool:
    """A Jarvis--Verrill zero at k is equivalent to a zero at p-1-k."""
    _require_odd_prime(prime)
    if (
        isinstance(index, bool)
        or not isinstance(index, int)
        or not 0 <= index <= prime - 1
    ):
        raise ValueError("index must lie in 0..p-1")
    reflected = prime - 1 - index
    left_zero = triple_moment_factor(index) % prime == 0
    right_zero = triple_moment_factor(reflected) % prime == 0
    if left_zero != right_zero:
        raise AssertionError("nonzero mirror multiplier must preserve the zero set")
    return True
