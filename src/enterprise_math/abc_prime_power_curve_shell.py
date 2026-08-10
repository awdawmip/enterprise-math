"""Curve-type classification of low-capacity prime-power unit branches.

If one unit-relation side is a prime power ``p^e``, then its normalized block
capacity is exactly ``e``.  When the neighboring integer has a large
multiplicity residual, strip its largest square divisor:

    p^e +/- 1 = k*s^2,

where k is the squarefree kernel of the neighboring integer.  Multiplying by k
and setting Y=k*s gives

    Y^2 = k*(p^e +/- 1).

For e=2 this is a Pell conic (genus zero).  For e>=3 the polynomial on the
right is squarefree in characteristic zero and the hyperelliptic genus is
floor((e-1)/2): genus one for e=3,4 and genus >=2 for e>=5.

The module records this exact structural routing.  Finiteness theorems for
integral points on positive-genus curves are external prior mathematics, not
implemented or claimed here.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_projective_sparse_failure import largest_square_divisor_root
from .abc_support import prime_factorization


@dataclass(frozen=True)
class PrimePowerSquareKernelCurve:
    base_prime: int
    exponent: int
    sign: int
    prime_power: int
    neighboring_value: int
    square_divisor_root: int
    squarefree_kernel: int
    curve_genus: int
    curve_type: str
    curve_identity: tuple[int, int, int]


def _is_prime(n: int) -> bool:
    return n > 1 and prime_factorization(n) == ((n, 1),)


def is_squarefree(n: int) -> bool:
    """Return whether every prime exponent of n is at most one."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return all(exponent == 1 for _prime, exponent in prime_factorization(n))


def prime_power_square_kernel_curve(
    base_prime: int,
    exponent: int,
    sign: int,
) -> PrimePowerSquareKernelCurve:
    """Classify ``p^e + sign = k*s^2`` for sign +/-1.

    ``sign=+1`` is the successor shell; ``sign=-1`` is the predecessor shell.
    """
    if isinstance(base_prime, bool) or not isinstance(base_prime, int) or not _is_prime(base_prime):
        raise ValueError("base_prime must be prime")
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 2:
        raise ValueError("exponent must be an integer >=2")
    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    value = base_prime**exponent
    neighbor = value + sign
    if neighbor <= 0:
        raise ValueError("neighboring value must be positive")
    s = largest_square_divisor_root(neighbor)
    if neighbor % (s * s):
        raise AssertionError("largest square divisor failed exact decomposition")
    k = neighbor // (s * s)
    if not is_squarefree(k):
        raise AssertionError("residual after largest square divisor must be squarefree")
    genus = (exponent - 1) // 2
    if exponent == 2:
        curve_type = "pell_conic"
        genus = 0
    elif genus == 1:
        curve_type = "genus_one_hyperelliptic"
    else:
        curve_type = "higher_genus_hyperelliptic"
    Y = k * s
    # Y^2 = k*(p^e + sign).
    if Y * Y != k * neighbor:
        raise AssertionError("square-kernel hyperelliptic identity failed")
    return PrimePowerSquareKernelCurve(
        base_prime=base_prime,
        exponent=exponent,
        sign=sign,
        prime_power=value,
        neighboring_value=neighbor,
        square_divisor_root=s,
        squarefree_kernel=k,
        curve_genus=genus,
        curve_type=curve_type,
        curve_identity=(Y, k, neighbor),
    )
