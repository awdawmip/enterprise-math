"""Fixed second-order Hahn transfer at the P022 q=18m-1 boundary.

This module consumes the accepted reduction

    q | F_(2n)  iff  Q_n(n; -3n, n-1, 3n) == 0 (mod q),
    q = 6n - 1,

and removes the moving Hahn parameters from the *x*-difference equation.

Put Y_s = Q_n(n+s; -3n, n-1, 3n).  Since n == 1/6 (mod q),
the standard Hahn difference equation reduces modulo q to

    A_s Y_(s+1) + B_s Y_s + C_s Y_(s-1) = 0,

with the universal coefficients

    A_s = (s-1/3)(s+2/3),
    B_s = 1/3 - 2s^2,
    C_s = (s-1/2)(s+1/6).

Thus the remaining obstruction is a fixed 2x2 transfer problem.  Moreover
Q_n(0)=1 and Q_n(1)=10/9 (mod q), so if

    T_n = M_(-1) ... M_(1-n),

then

    T_n (10,9)^T = 9 (Q_n(n), Q_n(n-1))^T.

This is an exact equivalence, not a finite-data fit.
"""

from __future__ import annotations


def _is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _require_boundary(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    prime = 6 * n - 1
    if not _is_prime(prime):
        raise ValueError("6*n-1 must be prime")
    return prime


def _inv(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        raise ZeroDivisionError("nonunit denominator in boundary field")
    return pow(value, -1, prime)


def hahn_diagonal_residue(n: int) -> int:
    """Return Q_n(n;-3n,n-1,3n) modulo p=6n-1."""
    prime = _require_boundary(n)
    term = 1
    total = 1
    for j in range(n):
        numerator = pow((j - n) % prime, 3, prime)
        denominator = (
            (1 - 3 * n + j) * (-3 * n + j) * (j + 1)
        ) % prime
        term = term * numerator * _inv(denominator, prime) % prime
        total = (total + term) % prime
    return total


def centered_transfer_matrix(step: int, prime: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return the universal matrix M_s over F_p.

    V_s=(Y_s,Y_(s-1))^T and V_(s+1)=M_s V_s.
    """
    if isinstance(step, bool) or not isinstance(step, int):
        raise ValueError("step must be an integer")
    if not _is_prime(prime) or prime <= 3:
        raise ValueError("prime must be an odd prime greater than 3")

    inv9 = _inv(9, prime)
    inv12 = _inv(12, prime)
    inv3 = _inv(3, prime)
    A = (3 * step - 1) * (3 * step + 2) * inv9 % prime
    C = (2 * step - 1) * (6 * step + 1) * inv12 % prime
    minus_B = (6 * step * step - 1) * inv3 % prime
    inv_A = _inv(A, prime)
    return (
        (minus_B * inv_A % prime, -C * inv_A % prime),
        (1, 0),
    )


def centered_transfer_determinant(step: int, prime: int) -> int:
    """Return det(M_s)=C_s/A_s modulo p."""
    matrix = centered_transfer_matrix(step, prime)
    return (-matrix[0][1]) % prime


def _matvec(
    matrix: tuple[tuple[int, int], tuple[int, int]],
    vector: tuple[int, int],
    prime: int,
) -> tuple[int, int]:
    return (
        (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % prime,
        (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % prime,
    )


def centered_terminal_vector(n: int) -> tuple[int, int]:
    """Return T_n(10,9)^T = 9(Q_n(n),Q_n(n-1))^T modulo p."""
    prime = _require_boundary(n)
    vector = (10 % prime, 9 % prime)
    for step in range(1 - n, 0):
        vector = _matvec(centered_transfer_matrix(step, prime), vector, prime)
    return vector


def centered_transfer_matches_hahn(n: int) -> bool:
    """Certify the first transfer coordinate equals 9 times the Hahn diagonal."""
    prime = _require_boundary(n)
    transfer = centered_terminal_vector(n)[0]
    diagonal = hahn_diagonal_residue(n)
    if transfer != 9 * diagonal % prime:
        raise AssertionError("fixed transfer and Hahn diagonal disagree")
    return True


def transfer_product_determinant(n: int) -> int:
    """Return det(T_n); it is nonzero for every prime boundary."""
    prime = _require_boundary(n)
    determinant = 1
    for step in range(1 - n, 0):
        determinant = (
            determinant * centered_transfer_determinant(step, prime)
        ) % prime
    if determinant == 0:
        raise AssertionError("boundary transfer product must be invertible")
    return determinant


def zero_forced_local_ratios(n: int) -> tuple[int, int, int]:
    """Return universal neighboring ratios forced by Q_n(n)=0.

    The tuple is
      (Q(n-2)/Q(n-1), Q(n+1)/Q(n-1), Q(n+2)/Q(n+1))
    and equals (4/3, -3/8, 3/2) in F_p.
    """
    prime = _require_boundary(n)
    return (
        4 * _inv(3, prime) % prime,
        -3 * _inv(8, prime) % prime,
        3 * _inv(2, prime) % prime,
    )


def admissible_p022_boundary(n: int) -> bool:
    """Return the accepted P022 twin-boundary primality gate."""
    return (
        isinstance(n, int)
        and not isinstance(n, bool)
        and n >= 3
        and n % 3 == 0
        and _is_prime(6 * n - 1)
        and _is_prime(4 * n - 1)
        and _is_prime(4 * n + 1)
    )
