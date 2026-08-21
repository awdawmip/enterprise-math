"""Prime-BRC midpoint ladder and absorbing-defect research kernel.

This owner-local module extends ``prime_brc_phase`` with the exact mirror ladder
and the two center-lock/absorbing laws.  It is L3 research support and makes no
Legendre proof claim.
"""

from __future__ import annotations

from fractions import Fraction

from .prime_brc_phase import (
    defect,
    mirror_pair,
    quotient_triple,
    square_basin_frame,
    square_midpoint_defect,
    square_quotient_phase,
)


def midpoint_absorption_plus(
    lower: int, middle: int, upper: int, divisor: int
) -> dict[str, object]:
    """If Delta=+1 and d|M, quotienting preserves Delta=+1 exactly."""
    if defect(lower, middle, upper) != 1:
        raise ValueError("input triple must have midpoint defect +1")
    if divisor < 2 or middle % divisor:
        raise ValueError("divisor must be >=2 and divide the integer midpoint")
    out = quotient_triple(lower, middle, upper, divisor)
    if defect(*out) != 1:
        raise AssertionError("+1 midpoint defect failed its absorbing law")
    return {"input": (lower, middle, upper), "divisor": divisor, "output": out, "defect": 1}


def midpoint_absorption_minus(
    lower: int, middle: int, upper: int, divisor: int
) -> dict[str, object]:
    """If Delta=-1 and d|(M+1), quotienting preserves Delta=-1 exactly."""
    if defect(lower, middle, upper) != -1:
        raise ValueError("input triple must have midpoint defect -1")
    if divisor < 2 or (middle + 1) % divisor:
        raise ValueError("divisor must be >=2 and divide the upper adjacent midpoint M+1")
    out = quotient_triple(lower, middle, upper, divisor)
    if defect(*out) != -1:
        raise AssertionError("-1 adjacent-midpoint defect failed its absorbing law")
    return {"input": (lower, middle, upper), "divisor": divisor, "output": out, "defect": -1}


def mirror_phase_ladder(k: int, radius: int, divisor: int, side: str) -> dict[str, object]:
    """Return the exact step-2 half-window ladder for one mirror divisor hit.

    Lower hit ``d|(M-r)``:

        h^- = 2m-w = chi_d - 2 floor(r/d).

    Upper hit ``d|(M+r)``:

        h^+ = 2m-w = chi_d + 2 ceil(r/d).

    Hence ``Theta=1/2+h/(2w)``.  The center term is the ternary midpoint
    defect chi_d; subsequent same-channel hits move by steps of two.
    """
    frame = square_basin_frame(k)
    lower_state, upper_state = mirror_pair(k, radius)
    if divisor < 2:
        raise ValueError("divisor must be at least 2")
    if frame["center"] % divisor == 0:
        raise ValueError("divisor must be transverse to the mirror center")
    chi = square_midpoint_defect(k, divisor)

    if side == "lower":
        if lower_state % divisor:
            raise ValueError("divisor must divide M-r on the lower side")
        state = lower_state
        ladder_index = radius // divisor
        expected_bias = chi - 2 * ladder_index
    elif side == "upper":
        if upper_state % divisor:
            raise ValueError("divisor must divide M+r on the upper side")
        state = upper_state
        ladder_index = (radius + divisor - 1) // divisor
        expected_bias = chi + 2 * ladder_index
    else:
        raise ValueError("side must be 'lower' or 'upper'")

    phase = square_quotient_phase(k, state, divisor)
    width = int(phase["width"])
    index = int(phase["index"])
    actual_bias = 2 * index - width
    if actual_bias != expected_bias:
        raise AssertionError("mirror phase ladder identity failed")
    expected_phase = Fraction(1, 2) + Fraction(expected_bias, 2 * width)
    if phase["phase"] != expected_phase:
        raise AssertionError("mirror phase did not match its half-window ladder")
    return {
        "k": k,
        "radius": radius,
        "divisor": divisor,
        "side": side,
        "chi": chi,
        "width": width,
        "index": index,
        "ladder_index": ladder_index,
        "half_window_bias": actual_bias,
        "phase": phase["phase"],
    }


def mirror_critical_bilinear_carry(
    k: int, radius: int, lower_divisor: int, upper_divisor: int
) -> dict[str, object]:
    """Return the exact integer form of mirror phase crossing.

    For transverse divisor hits on both sides, let ``h_-`` and ``h_+`` be the
    ladder half-window biases and ``w_-``, ``w_+`` their quotient widths.  Then

        w_+ h_- + w_- h_+ = 2(m_-m_+ - u_-u_+) >= 2.

    This is an exact rewrite of the mirror-divisibility crossing, not an
    independent new source of arithmetic information.
    """
    lo = mirror_phase_ladder(k, radius, lower_divisor, "lower")
    hi = mirror_phase_ladder(k, radius, upper_divisor, "upper")
    w_lo = int(lo["width"])
    w_hi = int(hi["width"])
    h_lo = int(lo["half_window_bias"])
    h_hi = int(hi["half_window_bias"])
    margin = w_hi * h_lo + w_lo * h_hi
    if margin < 2 or margin % 2:
        raise AssertionError("critical bilinear carry margin must be a positive even integer")
    phase_margin = lo["phase"] + hi["phase"] - 1
    if phase_margin != Fraction(margin, 2 * w_lo * w_hi):
        raise AssertionError("integer carry margin disagrees with phase crossing")
    return {
        "k": k,
        "radius": radius,
        "lower_divisor": lower_divisor,
        "upper_divisor": upper_divisor,
        "lower": lo,
        "upper": hi,
        "integer_margin": margin,
        "product_margin": margin // 2,
        "phase_margin": phase_margin,
    }


def positive_entry_factor_lock(k: int, radius: int, first_divisor: int, suffix_factors: tuple[int, ...]) -> dict[str, object]:
    """Verify the +1 center-lock after a positive lower critical entry.

    Preconditions encode the theorem-critical geometry directly:

    * ``first_divisor | M-r``;
    * its lower ladder bias is exactly +1, so the quotient state lands at
      ``floor(M/p)`` and the quotient triple has defect +1;
    * every later supplied factor divides the current midpoint state.

    All suffix quotient defects must then remain +1 by the absorbing law.
    """
    entry = mirror_phase_ladder(k, radius, first_divisor, "lower")
    if entry["half_window_bias"] != 1:
        raise ValueError("first divisor must be a positive one-bit lower entry")
    frame = square_basin_frame(k)
    lower_state, _ = mirror_pair(k, radius)
    if lower_state % first_divisor:
        raise AssertionError("entry divisor left the lower state")
    current = quotient_triple(frame["lower"], frame["center"], frame["upper"], first_divisor)
    state = lower_state // first_divisor
    if state != current[1] or defect(*current) != 1:
        raise AssertionError("positive entry did not recoalesce exactly at the +1 midpoint")

    trace = [current]
    states = [state]
    for factor in suffix_factors:
        if factor < 2 or state % factor:
            raise ValueError("each suffix factor must divide the current midpoint state")
        step = midpoint_absorption_plus(*current, factor)
        current = step["output"]
        state //= factor
        if state != current[1]:
            raise AssertionError("suffix factor path left the exact midpoint")
        trace.append(current)
        states.append(state)
    return {
        "entry": entry,
        "suffix_factors": suffix_factors,
        "quotient_triples": tuple(trace),
        "midpoint_states": tuple(states),
        "defect_trace": tuple(defect(*triple) for triple in trace),
    }
