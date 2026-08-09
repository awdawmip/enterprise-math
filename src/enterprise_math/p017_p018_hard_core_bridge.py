"""WIP P017/P018 bridge: recursive root-basin isolation of hard-core prime tails.

Sources consumed, not re-owned:
- P018 discovery PR #148: exact divisor quotient windows and odd small-product
  candidate-root separation.
- P017 discovery PR #150: residual hard-core mirror states with odd full cores
  and prime tails.
- canonical P018 APQ-T01: one quotient image meets at most two adjacent
  square-root basins.

Let ``3 <= d < e`` be odd, ``d*e < k``, ``M=k(k+1)``, ``1 <= r < k``,
and ``eps in {-1,+1}``. If

    q_d = (M + eps*r) // d,
    q_e = (M - eps*r) // e

are exact integer quotients, both exceed ``k``, and both are prime, then

    isqrt(q_d) - isqrt(q_e) >= 3.

The proof has an analytic finite-reduction step plus an exact finite audit. If
the actual root gap were at most two, APQ-T01 forces the base root gap
``j_d-j_e <= 3``, where ``j_s=isqrt(k^2//s)``. Put ``u=j_e``. Then

    e*u^2 <= k^2 < d*(u+4)^2,

so, because ``e-d>=2``, one gets ``2*u^2 < 8*d*u+16*d`` and therefore
``u<=4*d+1``. Combining ``d*e<k`` with ``k^2<e*(u+1)^2`` yields

    d^2*e < (4*d+2)^2.

Pure integer arithmetic then forces ``d<=15``, ``e<=21`` and ``k<=284``.
Exact enumeration inside that analytically complete box leaves only thirteen
mirror rows with actual root gap below three. Each row has the explicit proper
factor witness recorded below, so no row has two prime tails.

This is a bridge result, not a canonical P017 L-number or P018 theorem number.
"""

from __future__ import annotations

from math import isqrt

from .legendre import is_prime

RISK_K_MAX = 284

SMALL_ACTUAL_GAP_ROWS = (
    (16, 3, 5, 8, -1, 88, 56, 9, 7),
    (16, 3, 5, 7, 1, 93, 53, 9, 7),
    (17, 3, 5, 9, -1, 99, 63, 9, 7),
    (18, 3, 5, 3, -1, 113, 69, 10, 8),
    (18, 3, 5, 12, 1, 118, 66, 10, 8),
    (20, 3, 5, 15, -1, 135, 87, 11, 9),
    (22, 3, 5, 14, -1, 164, 104, 12, 10),
    (24, 3, 5, 15, -1, 195, 123, 13, 11),
    (37, 5, 7, 1, -1, 281, 201, 16, 14),
    (37, 5, 7, 36, -1, 274, 206, 16, 14),
    (37, 5, 7, 34, 1, 288, 196, 16, 14),
    (39, 5, 7, 15, -1, 309, 225, 17, 15),
    (42, 5, 7, 21, -1, 357, 261, 18, 16),
)

# (side, proper factor) for the corresponding row above.
SMALL_GAP_COMPOSITE_WITNESSES = (
    ("d", 2),
    ("d", 3),
    ("d", 3),
    ("e", 3),
    ("d", 2),
    ("d", 3),
    ("d", 2),
    ("d", 3),
    ("e", 3),
    ("d", 2),
    ("d", 2),
    ("d", 3),
    ("d", 3),
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def base_root_index(k: int, divisor: int) -> int:
    """Return the square-root index of ``floor(k^2/divisor)``."""
    _require_int("k", k)
    _require_int("divisor", divisor)
    if k < 2 or divisor < 2:
        raise ValueError("require k>=2 and divisor>=2")
    return isqrt((k * k) // divisor)


def finite_base_gap_reduction(k: int, d: int, e: int) -> dict[str, int]:
    """Certify the analytic finite box under ``j_d-j_e <= 3``."""
    for name, value in (("k", k), ("d", d), ("e", e)):
        _require_int(name, value)
    if not (3 <= d < e and d % 2 == 1 and e % 2 == 1 and d * e < k):
        raise ValueError("require odd 3<=d<e with d*e<k")

    j_d = base_root_index(k, d)
    u = base_root_index(k, e)
    if j_d - u > 3:
        raise ValueError("base root gap is already at least four")

    if not (e * u * u <= k * k < e * (u + 1) * (u + 1)):
        raise AssertionError("e-root index escaped its defining basin")
    if not (k * k < d * (u + 4) * (u + 4)):
        raise AssertionError("base-gap hypothesis failed to imply the d-bound")

    # (e-d)u^2 < 8du+16d and e-d>=2. At u=4d+2 the
    # left-minus-right lower bound is already 8 and increases thereafter.
    if u >= 4 * d + 2:
        if 2 * u * u <= 8 * d * u + 16 * d:
            raise AssertionError("quadratic cutoff arithmetic was miscomputed")
        raise AssertionError("base-gap hypothesis contradicts u>=4d+2")

    # de<k and k^2<e(u+1)^2 give d^2 e < (u+1)^2.
    if not (d * d * e < (4 * d + 2) * (4 * d + 2)):
        raise AssertionError("finite-reduction inequality failed")

    # For odd d>=17, d^2(d+2) >= (4d+2)^2; for e>=22 and d>=3,
    # 22d^2 >= (4d+2)^2. Both contradict the preceding strict inequality.
    if d > 15:
        raise AssertionError("finite reduction failed to force d<=15")
    if e > 21:
        raise AssertionError("finite reduction failed to force e<=21")

    # k^2 < e(u+1)^2 <= 21*62^2 = 80724 < 285^2.
    if k > RISK_K_MAX:
        raise AssertionError("finite reduction failed to force k<=284")

    return {
        "k": k,
        "d": d,
        "e": e,
        "j_d": j_d,
        "j_e": u,
        "base_root_gap": j_d - u,
        "u_bound": 4 * d + 1,
        "k_bound": RISK_K_MAX,
    }


def finite_base_risk_triples() -> tuple[tuple[int, int, int, int, int], ...]:
    """Enumerate the analytically complete ``j_d-j_e<=3`` parameter box."""
    rows: list[tuple[int, int, int, int, int]] = []
    for d in range(3, 16, 2):
        for e in range(d + 2, 22, 2):
            if d * d * e >= (4 * d + 2) ** 2:
                continue
            k_max = isqrt(e * (4 * d + 2) ** 2 - 1)
            for k in range(d * e + 1, min(k_max, RISK_K_MAX) + 1):
                j_d = base_root_index(k, d)
                j_e = base_root_index(k, e)
                if j_d - j_e <= 3:
                    finite_base_gap_reduction(k, d, e)
                    rows.append((k, d, e, j_d, j_e))
    return tuple(rows)


def enumerate_small_actual_gap_rows() -> tuple[tuple[int, ...], ...]:
    """Enumerate every mirror row in the finite box with actual root gap < 3."""
    rows: list[tuple[int, ...]] = []
    for k, d, e, _, _ in finite_base_risk_triples():
        center = k * (k + 1)
        for orientation in (-1, 1):
            for radius in range(1, k):
                d_num = center + orientation * radius
                e_num = center - orientation * radius
                if d_num % d or e_num % e:
                    continue
                q_d = d_num // d
                q_e = e_num // e
                if q_d <= k or q_e <= k:
                    continue
                root_d = isqrt(q_d)
                root_e = isqrt(q_e)
                if root_d < root_e:
                    raise AssertionError("same-parity quotient ordering was reversed")
                if root_d - root_e < 3:
                    rows.append(
                        (
                            k,
                            d,
                            e,
                            radius,
                            orientation,
                            q_d,
                            q_e,
                            root_d,
                            root_e,
                        )
                    )
    return tuple(rows)


def _small_gap_composite_witness(row: tuple[int, ...]) -> tuple[str, int]:
    try:
        index = SMALL_ACTUAL_GAP_ROWS.index(row)
    except ValueError as exc:
        raise AssertionError("small-gap row escaped the exact finite certificate") from exc
    side, factor = SMALL_GAP_COMPOSITE_WITNESSES[index]
    target = row[5] if side == "d" else row[6]
    if target == factor or target % factor:
        raise AssertionError("recorded composite witness is invalid")
    return side, factor


def prime_tail_root_gap_certificate(
    k: int,
    d: int,
    e: int,
    radius: int,
    orientation: int,
) -> dict[str, int]:
    """Certify root-gap >=3 for an odd small-product prime-tail mirror pair."""
    for name, value in (("k", k), ("d", d), ("e", e), ("radius", radius)):
        _require_int(name, value)
    if orientation not in (-1, 1):
        raise ValueError("orientation must be -1 or +1")
    if not (3 <= d < e and d % 2 == 1 and e % 2 == 1 and d * e < k):
        raise ValueError("require odd 3<=d<e with d*e<k")
    if not 1 <= radius < k:
        raise ValueError("require 1<=radius<k")

    center = k * (k + 1)
    d_num = center + orientation * radius
    e_num = center - orientation * radius
    if d_num % d or e_num % e:
        raise ValueError("mirror states must divide exactly by their declared cores")
    if not (k * k < d_num < (k + 1) ** 2 and k * k < e_num < (k + 1) ** 2):
        raise AssertionError("mirror state escaped the open square basin")

    q_d = d_num // d
    q_e = e_num // e
    if q_d <= k or q_e <= k:
        raise ValueError("both residual tails must exceed k")
    if not is_prime(q_d) or not is_prime(q_e):
        raise ValueError("both residual tails must be prime")

    root_d = isqrt(q_d)
    root_e = isqrt(q_e)
    if root_d < root_e:
        raise AssertionError("same-parity quotient ordering was reversed")
    gap = root_d - root_e

    if gap < 3:
        j_d = base_root_index(k, d)
        j_e = base_root_index(k, e)
        if root_d not in (j_d, j_d + 1) or root_e not in (j_e, j_e + 1):
            raise AssertionError("canonical APQ two-basin transport was violated")
        if j_d - j_e > 3:
            raise AssertionError("small actual gap failed to force small base gap")
        finite_base_gap_reduction(k, d, e)
        row = (k, d, e, radius, orientation, q_d, q_e, root_d, root_e)
        _small_gap_composite_witness(row)
        raise AssertionError("prime tails entered a finite row with a composite witness")

    return {
        "k": k,
        "d": d,
        "e": e,
        "radius": radius,
        "orientation": orientation,
        "q_d": q_d,
        "q_e": q_e,
        "root_d": root_d,
        "root_e": root_e,
        "root_gap": gap,
    }
