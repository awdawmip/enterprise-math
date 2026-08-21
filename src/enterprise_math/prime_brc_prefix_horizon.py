"""Prime-BRC mirror factor-prefix horizon and post-lock monotonicity.

For a mirror state M-r or M+r, a cumulative true divisor D retains a simple
integer offset from the quotient midpoint until D exceeds the original radius.
At D>r the quotient state lands exactly on one of the two adjacent integer
centers.  Subsequent factor divisions therefore enter a monotone ternary-defect
regime.

L3 owner-local research support; no prime-existence theorem is claimed.
"""

from __future__ import annotations

from .prime_brc_phase import defect, quotient_triple, square_basin_frame


def lower_cumulative_divisor_state(k: int, radius: int, divisor: int) -> dict[str, int | bool]:
    """Exact state/midpoint offset for D | (M-r).

        (M-r)/D = floor(M/D) - floor(r/D).

    Hence D>r is exactly the center-lock threshold.
    """
    frame = square_basin_frame(k)
    if not 1 <= radius < k:
        raise ValueError("require 1 <= radius < k")
    state = frame["center"] - radius
    if divisor < 2 or state % divisor:
        raise ValueError("divisor must be >=2 and divide M-r")
    qstate = state // divisor
    qmid = frame["center"] // divisor
    offset = qstate - qmid
    expected = -(radius // divisor)
    if offset != expected:
        raise AssertionError("lower cumulative-divisor offset identity failed")
    return {
        "k": k,
        "radius": radius,
        "divisor": divisor,
        "quotient_state": qstate,
        "quotient_midpoint": qmid,
        "midpoint_offset": offset,
        "center_locked": divisor > radius,
    }


def upper_cumulative_divisor_state(k: int, radius: int, divisor: int) -> dict[str, int | bool]:
    """Exact state/adjacent-midpoint offset for D | (M+r).

    Put c=ceil(r/D). Then

        (M+r)/D = floor(M/D) + c.

    Hence D>r gives exactly the upper adjacent integer center floor(M/D)+1.
    """
    frame = square_basin_frame(k)
    if not 1 <= radius < k:
        raise ValueError("require 1 <= radius < k")
    state = frame["center"] + radius
    if divisor < 2 or state % divisor:
        raise ValueError("divisor must be >=2 and divide M+r")
    qstate = state // divisor
    qmid = frame["center"] // divisor
    ceil_radius = (radius + divisor - 1) // divisor
    offset = qstate - qmid
    if offset != ceil_radius:
        raise AssertionError("upper cumulative-divisor offset identity failed")
    return {
        "k": k,
        "radius": radius,
        "divisor": divisor,
        "quotient_state": qstate,
        "quotient_midpoint": qmid,
        "midpoint_offset": offset,
        "center_locked": divisor > radius,
    }


def midpoint_divisor_defect_transition(
    lower: int, middle: int, upper: int, divisor: int
) -> dict[str, object]:
    """Quotient a ternary triple by a divisor of its integer midpoint.

    The ternary defect is monotone nondecreasing in the order -1<0<+1.
    """
    before = defect(lower, middle, upper)
    if before not in (-1, 0, 1):
        raise ValueError("input defect must be ternary")
    if divisor < 2 or middle % divisor:
        raise ValueError("divisor must divide the integer midpoint")
    out = quotient_triple(lower, middle, upper, divisor)
    after = defect(*out)
    if after not in (-1, 0, 1) or after < before:
        raise AssertionError("midpoint-divisor defect failed monotone nondecrease")
    return {"input_defect": before, "output_defect": after, "output": out}


def adjacent_midpoint_divisor_defect_transition(
    lower: int, middle: int, upper: int, divisor: int
) -> dict[str, object]:
    """Quotient by a divisor of the upper adjacent integer midpoint M+1.

    The ternary defect is monotone nonincreasing in the order -1<0<+1.
    """
    before = defect(lower, middle, upper)
    if before not in (-1, 0, 1):
        raise ValueError("input defect must be ternary")
    if divisor < 2 or (middle + 1) % divisor:
        raise ValueError("divisor must divide M+1")
    out = quotient_triple(lower, middle, upper, divisor)
    after = defect(*out)
    if after not in (-1, 0, 1) or after > before:
        raise AssertionError("adjacent-midpoint defect failed monotone nonincrease")
    return {"input_defect": before, "output_defect": after, "output": out}


def lower_factor_prefix_horizon(k: int, radius: int, factors: tuple[int, ...]) -> dict[str, object]:
    """Replay an ordered factor prefix of M-r and locate the first D>r lock.

    ``factors`` must be a genuine sequential factorization prefix of M-r.  Once
    the cumulative divisor exceeds r, the quotient state equals the quotient
    midpoint.  Every remaining supplied factor then divides that midpoint and
    the defect trace is monotone nondecreasing.
    """
    frame = square_basin_frame(k)
    state = frame["center"] - radius
    if not 1 <= radius < k:
        raise ValueError("require 1 <= radius < k")
    current_triple = (frame["lower"], frame["center"], frame["upper"])
    cumulative = 1
    lock_index = None
    records = []
    locked = False
    previous_defect = defect(*current_triple)
    for index, factor in enumerate(factors, start=1):
        if factor < 2 or state % factor:
            raise ValueError("factors must divide the current quotient state sequentially")
        cumulative *= factor
        state //= factor
        current_triple = quotient_triple(*current_triple, factor)
        current_defect = defect(*current_triple)
        offset = state - current_triple[1]
        expected_offset = -(radius // cumulative)
        if offset != expected_offset:
            raise AssertionError("factor-prefix midpoint offset disagrees with cumulative formula")
        if cumulative > radius and not locked:
            locked = True
            lock_index = index
        if locked:
            if offset != 0:
                raise AssertionError("post-horizon lower state left the exact midpoint")
            if current_defect < previous_defect and index > lock_index:
                raise AssertionError("post-lock lower defect decreased")
        records.append(
            {
                "index": index,
                "factor": factor,
                "cumulative_divisor": cumulative,
                "state": state,
                "midpoint_offset": offset,
                "defect": current_defect,
                "locked": locked,
            }
        )
        previous_defect = current_defect
    return {
        "k": k,
        "radius": radius,
        "lock_index": lock_index,
        "locked": locked,
        "records": tuple(records),
    }


def upper_factor_prefix_horizon(k: int, radius: int, factors: tuple[int, ...]) -> dict[str, object]:
    """Dual prefix-horizon replay for M+r.

    After cumulative D>r, the quotient state is exactly M_D+1 and the subsequent
    defect trace is monotone nonincreasing.
    """
    frame = square_basin_frame(k)
    state = frame["center"] + radius
    if not 1 <= radius < k:
        raise ValueError("require 1 <= radius < k")
    current_triple = (frame["lower"], frame["center"], frame["upper"])
    cumulative = 1
    lock_index = None
    records = []
    locked = False
    previous_defect = defect(*current_triple)
    for index, factor in enumerate(factors, start=1):
        if factor < 2 or state % factor:
            raise ValueError("factors must divide the current quotient state sequentially")
        cumulative *= factor
        state //= factor
        current_triple = quotient_triple(*current_triple, factor)
        current_defect = defect(*current_triple)
        expected_offset = (radius + cumulative - 1) // cumulative
        offset = state - current_triple[1]
        if offset != expected_offset:
            raise AssertionError("upper factor-prefix offset disagrees with cumulative formula")
        if cumulative > radius and not locked:
            locked = True
            lock_index = index
        if locked:
            if offset != 1:
                raise AssertionError("post-horizon upper state left the adjacent midpoint")
            if current_defect > previous_defect and index > lock_index:
                raise AssertionError("post-lock upper defect increased")
        records.append(
            {
                "index": index,
                "factor": factor,
                "cumulative_divisor": cumulative,
                "state": state,
                "midpoint_offset": offset,
                "defect": current_defect,
                "locked": locked,
            }
        )
        previous_defect = current_defect
    return {
        "k": k,
        "radius": radius,
        "lock_index": lock_index,
        "locked": locked,
        "records": tuple(records),
    }
