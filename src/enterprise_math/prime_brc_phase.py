"""Exact integer Prime-BRC quotient-phase and midpoint-defect research kernel.

Status: L3 owner-local research support.  This module does **not** prove
Legendre's conjecture.  It packages exact arithmetic identities discovered on
``research/prime-brc-stage-a`` so that the claims can be replayed without
floating-point arithmetic or primality-oracle leakage into theorem statements.

The core square-basin coordinates are

    L = k^2,
    M = k(k+1),
    U = (k+1)^2,
    G = U-L = 2k+1.

The pure-algebra BRC midpoint defect is

    Delta(L,M,U) = 2M-L-U = -1.

Floor quotienting preserves the ternary defect class {-1,0,+1}.  For a
transverse prime p, the quotient midpoint defect is the signed companion of the
canonical P017 centered square carry: kappa records the unsigned total of the
two boundary carry bits, while chi records their orientation.

All phase values are returned as ``fractions.Fraction``.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt
from typing import Iterable

from .legendre import centered_square_carry, primes_up_to


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_k(k: int) -> None:
    _require_int("k", k)
    if k < 2:
        raise ValueError("k must be at least 2")


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def square_basin_frame(k: int) -> dict[str, int]:
    """Return the exact consecutive-square BRC frame."""
    _require_k(k)
    lower = k * k
    center = k * (k + 1)
    upper = (k + 1) * (k + 1)
    gap = upper - lower
    if 2 * center - lower - upper != -1:
        raise AssertionError("square-basin midpoint unit defect changed")
    return {
        "k": k,
        "lower": lower,
        "center": center,
        "upper": upper,
        "gap": gap,
        "midpoint_defect": -1,
    }


def mirror_pair(k: int, radius: int) -> tuple[int, int]:
    """Return M-r and M+r for 1<=r<k."""
    _require_k(k)
    _require_int("radius", radius)
    if not 1 <= radius < k:
        raise ValueError("radius must satisfy 1 <= radius < k")
    center = k * (k + 1)
    return center - radius, center + radius


def complementary_collapse_residuals(
    k: int, radius: int, lower_bit: int, upper_bit: int
) -> tuple[int, int]:
    """Return signed endpoint-collapse residuals for complementary BRC bits.

    ``bit=0`` means lower-square collapse and ``bit=1`` means upper-square
    collapse.  Complementary bits always give residual sum -1.
    """
    _require_k(k)
    _require_int("lower_bit", lower_bit)
    _require_int("upper_bit", upper_bit)
    if lower_bit not in (0, 1) or upper_bit not in (0, 1):
        raise ValueError("collapse bits must be 0 or 1")
    if lower_bit + upper_bit != 1:
        raise ValueError("this interface requires complementary collapse bits")
    lower_state, upper_state = mirror_pair(k, radius)
    lower = k * k
    gap = 2 * k + 1
    rho_lower = lower_state - (lower + gap * lower_bit)
    rho_upper = upper_state - (lower + gap * upper_bit)
    if rho_lower + rho_upper != -1:
        raise AssertionError("complementary unit-defect law failed")
    return rho_lower, rho_upper


def defect(lower: int, middle: int, upper: int) -> int:
    """Return the signed midpoint defect 2M-L-U."""
    for name, value in (("lower", lower), ("middle", middle), ("upper", upper)):
        _require_int(name, value)
    if not lower <= middle <= upper:
        raise ValueError("require lower <= middle <= upper")
    return 2 * middle - lower - upper


def quotient_triple(lower: int, middle: int, upper: int, divisor: int) -> tuple[int, int, int]:
    """Floor-quotient a typed boundary triple."""
    _require_int("divisor", divisor)
    if divisor < 2:
        raise ValueError("divisor must be at least 2")
    if not lower <= middle <= upper:
        raise ValueError("require lower <= middle <= upper")
    return lower // divisor, middle // divisor, upper // divisor


def ternary_defect_quotient(
    lower: int, middle: int, upper: int, divisor: int
) -> dict[str, object]:
    """Apply one quotient to a triple whose defect lies in {-1,0,+1}.

    Exact remainder expansion gives

        d*Delta' = Delta + a + c - 2b,

    with 0<=a,b,c<d.  The right side lies strictly between -2d and 2d,
    hence the divisible value ``d*Delta'`` can only be -d, 0, or +d.
    """
    current = defect(lower, middle, upper)
    if current not in (-1, 0, 1):
        raise ValueError("current defect must lie in {-1,0,+1}")
    q_lower, q_middle, q_upper = quotient_triple(lower, middle, upper, divisor)
    next_defect = defect(q_lower, q_middle, q_upper)
    if next_defect not in (-1, 0, 1):
        raise AssertionError("floor quotient escaped the ternary defect class")
    a = lower % divisor
    b = middle % divisor
    c = upper % divisor
    if divisor * next_defect != current + a + c - 2 * b:
        raise AssertionError("ternary defect remainder identity failed")
    return {
        "input": (lower, middle, upper),
        "divisor": divisor,
        "input_defect": current,
        "residues": (a, b, c),
        "output": (q_lower, q_middle, q_upper),
        "output_defect": next_defect,
    }


def defect_path_flattening(
    lower: int, middle: int, upper: int, divisors: Iterable[int]
) -> dict[str, object]:
    """Verify that the final quotient defect depends only on total divisor.

    Intermediate defect values need not be determined by the ternary value alone;
    this function records the exact quotient triples and checks only the lawful
    path-flattening statement inherited from floor-division associativity.
    """
    ds = tuple(divisors)
    if not ds:
        raise ValueError("at least one divisor is required")
    for d in ds:
        _require_int("divisor", d)
        if d < 2:
            raise ValueError("every divisor must be at least 2")
    if defect(lower, middle, upper) not in (-1, 0, 1):
        raise ValueError("initial defect must lie in {-1,0,+1}")

    current = (lower, middle, upper)
    trace: list[tuple[int, int, int]] = [current]
    defects: list[int] = [defect(*current)]
    product = 1
    for d in ds:
        current = quotient_triple(*current, d)
        product *= d
        trace.append(current)
        current_defect = defect(*current)
        if current_defect not in (-1, 0, 1):
            raise AssertionError("iterated quotient escaped ternary defect class")
        defects.append(current_defect)

    direct = quotient_triple(lower, middle, upper, product)
    if current != direct:
        raise AssertionError("floor quotient path flattening failed")
    return {
        "divisors": ds,
        "total_divisor": product,
        "quotient_trace": tuple(trace),
        "defect_trace": tuple(defects),
        "direct_final": direct,
        "final_defect": defects[-1],
    }


def square_midpoint_defect(k: int, divisor: int) -> int:
    """Return chi_d(k)=2 floor(M/d)-floor(L/d)-floor(U/d)."""
    _require_k(k)
    _require_int("divisor", divisor)
    if divisor < 2:
        raise ValueError("divisor must be at least 2")
    frame = square_basin_frame(k)
    value = (
        2 * (frame["center"] // divisor)
        - frame["lower"] // divisor
        - frame["upper"] // divisor
    )
    if value not in (-1, 0, 1):
        raise AssertionError("square midpoint quotient defect is not ternary")
    return value


def quotient_phase_data(lower: int, upper: int, state: int, divisor: int) -> dict[str, object]:
    """Return the exact normalized quotient phase of one divisible interior state.

    The phase is

        (state/d - floor(lower/d)) /
        (floor(upper/d)-floor(lower/d)).

    For a strict interior state the phase is strictly ahead of its continuous
    linear position whenever ``d>=2``.
    """
    for name, value in (("lower", lower), ("upper", upper), ("state", state), ("divisor", divisor)):
        _require_int(name, value)
    if not lower < state < upper:
        raise ValueError("state must be strictly inside the interval")
    if divisor < 2 or state % divisor:
        raise ValueError("divisor must be >=2 and divide the state")
    base = lower // divisor
    top = upper // divisor
    width = top - base
    if width <= 0:
        raise ValueError("quotient interval must have positive integer width")
    index = state // divisor - base
    phase = Fraction(index, width)
    position = Fraction(state - lower, upper - lower)
    r = lower % divisor
    s = upper % divisor
    lead_formula = Fraction(
        r * (upper - state) + s * (state - lower),
        (upper - lower) * (upper - lower + r - s),
    )
    if phase - position != lead_formula:
        raise AssertionError("quotient phase lead formula failed")
    if not phase > position:
        raise AssertionError("interior quotient phase failed strict discrete lead")
    return {
        "lower": lower,
        "upper": upper,
        "state": state,
        "divisor": divisor,
        "base_quotient": base,
        "top_quotient": top,
        "width": width,
        "index": index,
        "phase": phase,
        "continuous_position": position,
        "phase_lead": phase - position,
        "lower_remainder": r,
        "upper_remainder": s,
    }


def square_quotient_phase(k: int, state: int, divisor: int) -> dict[str, object]:
    """Square-basin specialization of :func:`quotient_phase_data`."""
    frame = square_basin_frame(k)
    return quotient_phase_data(frame["lower"], frame["upper"], state, divisor)


def phase_path_flattening(
    lower: int, upper: int, state: int, divisors: Iterable[int]
) -> dict[str, object]:
    """Verify exact quotient-phase flattening along a true divisor path."""
    ds = tuple(divisors)
    if not ds:
        raise ValueError("at least one divisor is required")
    current_lower, current_upper, current_state = lower, upper, state
    product = 1
    trace: list[dict[str, object]] = []
    for d in ds:
        if current_state % d:
            raise ValueError("each path divisor must divide the current state")
        data = quotient_phase_data(current_lower, current_upper, current_state, d)
        trace.append(data)
        current_lower //= d
        current_upper //= d
        current_state //= d
        product *= d
    direct = quotient_phase_data(lower, upper, state, product)
    if trace[-1]["phase"] != direct["phase"]:
        raise AssertionError("quotient phase did not flatten through total divisor")
    return {
        "divisors": ds,
        "total_divisor": product,
        "path_phase": trace[-1]["phase"],
        "direct_phase": direct["phase"],
        "trace": tuple(trace),
    }


def transverse_prime_carry_bridge(k: int, prime: int) -> dict[str, int]:
    """Relate canonical P017 carry kappa to signed midpoint defect chi.

    For a prime ``p<=k`` with ``p`` transverse to ``M=k(k+1)``, put

        t = k mod p,
        a = t(t+1) mod p.

    The two centered boundary carry bits are

        b_minus = 1[a<t],
        b_plus  = 1[a>=p-t].

    Canonical P017 has ``kappa=b_minus+b_plus``.  The Prime-BRC signed
    midpoint defect is exactly ``chi=b_minus-b_plus``.
    """
    _require_k(k)
    _require_int("prime", prime)
    if prime > k or not _is_prime(prime):
        raise ValueError("prime must be prime and <=k")
    center = k * (k + 1)
    if center % prime == 0:
        raise ValueError("prime must be transverse to k(k+1)")
    t = k % prime
    a = (t * (t + 1)) % prime
    b_minus = int(a < t)
    b_plus = int(a >= prime - t)
    kappa = centered_square_carry(k, prime)
    chi = square_midpoint_defect(k, prime)
    if kappa != b_minus + b_plus:
        raise AssertionError("canonical centered carry lost its two-bit split")
    if chi != b_minus - b_plus:
        raise AssertionError("signed midpoint defect lost directional carry orientation")
    if (kappa + chi) // 2 != b_minus or (kappa - chi) // 2 != b_plus:
        raise AssertionError("(kappa,chi) failed exact directional recovery")
    return {
        "k": k,
        "prime": prime,
        "t": t,
        "center_remainder": a,
        "lower_carry_bit": b_minus,
        "upper_carry_bit": b_plus,
        "kappa": kappa,
        "chi": chi,
    }


def lower_midpoint_carry_candidate(k: int, prime: int) -> dict[str, object]:
    """Return the unique lower midpoint hit selected by a positive chi prime.

    If ``chi_p(k)=+1`` then ``r=M mod p`` satisfies ``p>=2r+3`` and the
    midpoint-adjacent lower multiple is ``n=M-r=p*floor(M/p)``.  Its quotient
    phase is exactly ``1/2 + 1/(2w_p)``.
    """
    bridge = transverse_prime_carry_bridge(k, prime)
    if bridge["chi"] != 1:
        raise ValueError("prime must lie in the positive midpoint-carry channel")
    frame = square_basin_frame(k)
    center = frame["center"]
    radius = center % prime
    if not 1 <= radius < k:
        raise AssertionError("positive midpoint carry did not produce an interior lower radius")
    if prime < 2 * radius + 3:
        raise AssertionError("positive midpoint carry failed p>=2r+3")
    state = center - radius
    if state != prime * (center // prime):
        raise AssertionError("midpoint lower hit is not the floor quotient multiple")
    phase = square_quotient_phase(k, state, prime)
    half_bias = 2 * int(phase["index"]) - int(phase["width"])
    if half_bias != 1:
        raise AssertionError("positive midpoint carry is not one exact half-window bit")
    expected = Fraction(1, 2) + Fraction(1, 2 * int(phase["width"]))
    if phase["phase"] != expected:
        raise AssertionError("positive midpoint carry phase is not the nearest upper half-grid point")
    return {
        "k": k,
        "prime": prime,
        "radius": radius,
        "state": state,
        "cofactor": center // prime,
        "phase_width": phase["width"],
        "phase": phase["phase"],
        "half_bias": half_bias,
    }


def is_p_rough(value: int, threshold: int) -> bool:
    """Return whether ``value`` has no prime divisor below ``threshold``."""
    _require_int("value", value)
    _require_int("threshold", threshold)
    if value < 1 or threshold < 2:
        raise ValueError("require value>=1 and threshold>=2")
    return all(value % p for p in primes_up_to(threshold - 1))


def lower_midpoint_least_factor_event(k: int, prime: int) -> dict[str, object]:
    """Classify whether a positive midpoint carry survives least-factor gating.

    The event survives exactly when ``floor(M/p)`` is p-rough.  In that case p
    is the least prime factor of the lower midpoint hit and the event is a true
    Prime-BRC one-bit shell rather than an overcounted divisibility incidence.
    """
    candidate = lower_midpoint_carry_candidate(k, prime)
    cofactor = int(candidate["cofactor"])
    survives = is_p_rough(cofactor, prime)
    return {
        **candidate,
        "p_rough_cofactor": survives,
        "least_factor_event": survives,
    }


def mirror_phase_crossing(k: int, radius: int, lower_divisor: int, upper_divisor: int) -> dict[str, object]:
    """Prove the exact mirror quotient-phase crossing for transverse divisors.

    For ``n_-=M-r`` and ``n_+=M+r``, if ``d|n_-`` and ``e|n_+`` with both
    divisors coprime to M, then

        phase_d(n_-) + phase_e(n_+) > 1.

    The proof is checked through the integer counter inequalities

        d*m_d - e*u_e = (L mod d) + (U mod e) - 1 >= 1,
        e*m_e - d*u_d = (L mod e) + (U mod d) - 1 >= 1.
    """
    frame = square_basin_frame(k)
    lower_state, upper_state = mirror_pair(k, radius)
    center = frame["center"]
    for name, d, n in (
        ("lower_divisor", lower_divisor, lower_state),
        ("upper_divisor", upper_divisor, upper_state),
    ):
        _require_int(name, d)
        if d < 2 or n % d:
            raise ValueError(f"{name} must be >=2 and divide its mirror state")
        if center % d == 0:
            raise ValueError(f"{name} must be transverse to the mirror center")

    lo = square_quotient_phase(k, lower_state, lower_divisor)
    hi = square_quotient_phase(k, upper_state, upper_divisor)
    m_lo = int(lo["index"])
    m_hi = int(hi["index"])
    w_lo = int(lo["width"])
    w_hi = int(hi["width"])
    u_lo = w_lo - m_lo
    u_hi = w_hi - m_hi
    r_lo = frame["lower"] % lower_divisor
    s_lo = frame["upper"] % lower_divisor
    r_hi = frame["lower"] % upper_divisor
    s_hi = frame["upper"] % upper_divisor
    lhs1 = lower_divisor * m_lo - upper_divisor * u_hi
    lhs2 = upper_divisor * m_hi - lower_divisor * u_lo
    if lhs1 != r_lo + s_hi - 1 or lhs2 != r_hi + s_lo - 1:
        raise AssertionError("mirror counter transport identity failed")
    if lhs1 < 1 or lhs2 < 1:
        raise AssertionError("transverse mirror counter transport lost strict positivity")
    if m_lo * m_hi <= u_lo * u_hi:
        raise AssertionError("mirror quotient counters failed strict product crossing")
    phase_sum = lo["phase"] + hi["phase"]
    if not phase_sum > 1:
        raise AssertionError("mirror quotient phases failed to cross one")
    return {
        "k": k,
        "radius": radius,
        "lower_state": lower_state,
        "upper_state": upper_state,
        "lower_divisor": lower_divisor,
        "upper_divisor": upper_divisor,
        "lower_phase": lo["phase"],
        "upper_phase": hi["phase"],
        "phase_sum": phase_sum,
        "first_counter_margin": lhs1,
        "second_counter_margin": lhs2,
        "product_margin": m_lo * m_hi - u_lo * u_hi,
    }


def least_prime_factor(value: int) -> int:
    """Small exact least-prime-factor helper for bounded diagnostics."""
    _require_int("value", value)
    if value < 2:
        raise ValueError("value must be at least 2")
    for p in range(2, isqrt(value) + 1):
        if value % p == 0:
            return p
    return value


def global_least_factor_phase_sum(k: int) -> dict[str, object]:
    """Compute the owner-local Prime-BRC phase-capacity diagnostic F_k.

    ``F_k`` sums quotient phase over composite states, using each state's least
    prime factor.  If the square basin were prime-free, strict phase lead would
    force ``F_k>k``.  Therefore a theorem ``F_k<=k`` for every k would imply
    Legendre's conjecture.  This function is a finite diagnostic only and does
    not assert that conjectural inequality.
    """
    frame = square_basin_frame(k)
    total = Fraction(0, 1)
    composite_count = 0
    prime_count = 0
    for state in range(frame["lower"] + 1, frame["upper"]):
        p = least_prime_factor(state)
        if p == state:
            prime_count += 1
            continue
        composite_count += 1
        total += square_quotient_phase(k, state, p)["phase"]
    return {
        "k": k,
        "phase_sum": total,
        "capacity": Fraction(k, 1),
        "phase_capacity_holds": total <= k,
        "prime_count": prime_count,
        "composite_count": composite_count,
        "status": "COMPUTATIONAL_DIAGNOSTIC_NOT_THEOREM",
    }
