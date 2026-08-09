"""Integer coupling defect for exact witness-count composition.

For non-negative predecessor/successor profiles ``l_i`` and ``r_i`` over one
middle witness class of size ``m``, define

    Delta = m*sum_i l_i*r_i - (sum_i l_i)*(sum_i r_i).

Then Delta is equivalently the sum of pairwise profile-difference products.
Given ``m,L,R``, Delta is information-equivalent to the exact current matched
count ``N``.  This is a one-step count repair; it does not restore witness
identity for later joins.
"""

from __future__ import annotations

Profile = tuple[int, ...]
IntMatrix = tuple[tuple[int, ...], ...]


def _require_profile(profile: Profile, name: str) -> None:
    if not isinstance(profile, tuple) or not profile:
        raise ValueError(f"{name} must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in profile):
        raise ValueError(f"{name} entries must be non-negative integers")


def exact_matched_count(left: Profile, right: Profile) -> int:
    """Return N=sum_i l_i*r_i."""
    _require_profile(left, "left")
    _require_profile(right, "right")
    if len(left) != len(right):
        raise ValueError("profiles must have the same length")
    return sum(a * b for a, b in zip(left, right, strict=True))


def coupling_defect(left: Profile, right: Profile) -> int:
    """Return Delta=m*N-L*R as a signed integer."""
    _require_profile(left, "left")
    _require_profile(right, "right")
    if len(left) != len(right):
        raise ValueError("profiles must have the same length")
    m = len(left)
    return m * exact_matched_count(left, right) - sum(left) * sum(right)


def pair_difference_coupling_defect(left: Profile, right: Profile) -> int:
    """Return sum_{i<j}(l_i-l_j)(r_i-r_j), equal to coupling_defect."""
    _require_profile(left, "left")
    _require_profile(right, "right")
    if len(left) != len(right):
        raise ValueError("profiles must have the same length")
    return sum(
        (left[i] - left[j]) * (right[i] - right[j])
        for i in range(len(left))
        for j in range(i + 1, len(left))
    )


def recover_matched_count_from_marginals(
    middle_size: int, left_total: int, right_total: int, defect: int
) -> int:
    """Recover N=(L*R+Delta)/m with exact divisibility validation."""
    if isinstance(middle_size, bool) or not isinstance(middle_size, int) or middle_size <= 0:
        raise ValueError("middle_size must be a positive integer")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in (left_total, right_total)
    ):
        raise ValueError("marginal totals must be non-negative integers")
    if isinstance(defect, bool) or not isinstance(defect, int):
        raise ValueError("defect must be an integer")
    numerator = left_total * right_total + defect
    if numerator < 0 or numerator % middle_size != 0:
        raise ValueError("marginals and defect do not encode a realizable matched count")
    return numerator // middle_size


def cardinality_shadow_is_exact(left: Profile, right: Profile) -> bool:
    """Exact iff Delta=0, equivalently m*N=L*R."""
    return coupling_defect(left, right) == 0


def _require_matrix(matrix: IntMatrix, name: str) -> None:
    if not isinstance(matrix, tuple) or not matrix or not matrix[0]:
        raise ValueError(f"{name} must be a non-empty rectangular tuple")
    width = len(matrix[0])
    if any(not isinstance(row, tuple) or len(row) != width for row in matrix):
        raise ValueError(f"{name} must be rectangular")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for row in matrix
        for value in row
    ):
        raise ValueError(f"{name} entries must be non-negative integers")


def exact_composite_count_matrix(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    """Return ordinary non-negative-integer matrix product A*B."""
    _require_matrix(left, "left")
    _require_matrix(right, "right")
    middle = len(left[0])
    if len(right) != middle:
        raise ValueError("inner matrix dimensions must match")
    target_count = len(right[0])
    return tuple(
        tuple(
            sum(left[source][i] * right[i][target] for i in range(middle))
            for target in range(target_count)
        )
        for source in range(len(left))
    )


def coupling_defect_matrix(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    """Return D_ab=m*C_ab-L_a*R_b for every source/target class pair."""
    _require_matrix(left, "left")
    _require_matrix(right, "right")
    middle = len(left[0])
    if len(right) != middle:
        raise ValueError("inner matrix dimensions must match")
    composite = exact_composite_count_matrix(left, right)
    left_marginals = tuple(sum(row) for row in left)
    right_marginals = tuple(
        sum(right[i][target] for i in range(middle))
        for target in range(len(right[0]))
    )
    return tuple(
        tuple(
            middle * composite[source][target]
            - left_marginals[source] * right_marginals[target]
            for target in range(len(right[0]))
        )
        for source in range(len(left))
    )


def recover_composite_from_marginals_and_defect(
    middle_size: int,
    left_marginals: tuple[int, ...],
    right_marginals: tuple[int, ...],
    defect: IntMatrix,
) -> IntMatrix:
    """Recover the exact current composite count matrix from marginals + D."""
    if isinstance(middle_size, bool) or not isinstance(middle_size, int) or middle_size <= 0:
        raise ValueError("middle_size must be a positive integer")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in left_marginals):
        raise ValueError("left marginals must be non-negative integers")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in right_marginals):
        raise ValueError("right marginals must be non-negative integers")
    if not left_marginals or not right_marginals:
        raise ValueError("marginals must be non-empty")
    if len(defect) != len(left_marginals) or any(len(row) != len(right_marginals) for row in defect):
        raise ValueError("defect shape must match marginal dimensions")
    return tuple(
        tuple(
            recover_matched_count_from_marginals(
                middle_size,
                left_marginals[source],
                right_marginals[target],
                defect[source][target],
            )
            for target in range(len(right_marginals))
        )
        for source in range(len(left_marginals))
    )
