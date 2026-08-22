"""Prime-BRC quotient-phase credit cocycle.

Owner-local L3 research support on ``research/prime-brc-stage-a``.

For an integer interval A<n<B and a true cumulative divisor D|n, define

    theta_D(n) = (n/D-floor(A/D)) / (floor(B/D)-floor(A/D)).

If D|E|n, then theta_E(n) >= theta_D(n).  The increment is the ordinary
integer quotient-phase lead after passing to the D-quotient interval, hence is
nonnegative.  Because repeated floor quotienting flattens through the product,
these increments form an additive path-independent cocycle on the divisor
poset of n.

This is a process/readout theorem, not a prime-existence theorem.
"""

from __future__ import annotations

from fractions import Fraction


def divisor_phase(lower: int, upper: int, state: int, divisor: int) -> Fraction:
    if not lower < state < upper:
        raise ValueError("state must be strictly inside interval")
    if divisor < 1 or state % divisor:
        raise ValueError("divisor must be positive and divide state")
    lo = lower // divisor
    hi = upper // divisor
    width = hi - lo
    if width <= 0:
        raise ValueError("quotient width must be positive")
    return Fraction(state // divisor - lo, width)


def phase_refinement(lower: int, upper: int, state: int, coarse: int, fine: int) -> dict[str, object]:
    """Return one exact divisor refinement D|E|n and its nonnegative credit."""
    if coarse < 1 or fine < coarse or fine % coarse:
        raise ValueError("require positive coarse|fine")
    if state % fine:
        raise ValueError("fine divisor must divide state")

    theta_coarse = divisor_phase(lower, upper, state, coarse)
    theta_fine = divisor_phase(lower, upper, state, fine)
    credit = theta_fine - theta_coarse

    # Reduce the statement to one quotient step on the exact D-quotient frame.
    e = fine // coarse
    a = lower // coarse
    x = state // coarse
    b = upper // coarse
    if x % e:
        raise AssertionError("refinement factor failed to divide quotient state")
    r = a % e
    s = b % e
    lead = Fraction(
        r * (b - x) + s * (x - a),
        (b - a) * (b - a + r - s),
    )
    if credit != lead:
        raise AssertionError("phase credit disagrees with quotient-lead formula")
    if credit < 0:
        raise AssertionError("true divisor refinement decreased quotient phase")

    return {
        "lower": lower,
        "upper": upper,
        "state": state,
        "coarse_divisor": coarse,
        "fine_divisor": fine,
        "refinement_factor": e,
        "coarse_phase": theta_coarse,
        "fine_phase": theta_fine,
        "credit": credit,
        "quotient_lower_remainder": r,
        "quotient_upper_remainder": s,
    }


def phase_cocycle(lower: int, upper: int, state: int, divisors: tuple[int, ...]) -> dict[str, object]:
    """Verify monotone/additive/path-flat phase credit along a divisor chain.

    ``divisors`` is a strictly nondecreasing divisibility chain ending at any
    true divisor of ``state``.  The total credit telescopes and depends only on
    the first and last cumulative divisors.
    """
    if not divisors:
        raise ValueError("divisor chain must be nonempty")
    if any(d < 1 or state % d for d in divisors):
        raise ValueError("every chain element must be a positive divisor of state")
    for a, b in zip(divisors, divisors[1:]):
        if b % a:
            raise ValueError("divisors must form a divisibility chain")

    phases = tuple(divisor_phase(lower, upper, state, d) for d in divisors)
    credits = tuple(b - a for a, b in zip(phases, phases[1:]))
    if any(c < 0 for c in credits):
        raise AssertionError("phase cocycle contains negative credit")
    total = phases[-1] - phases[0]
    if sum(credits, Fraction(0, 1)) != total:
        raise AssertionError("phase cocycle failed additivity")

    return {
        "divisors": divisors,
        "phases": phases,
        "credits": credits,
        "total_credit": total,
        "endpoint_credit": divisor_phase(lower, upper, state, divisors[-1]) - divisor_phase(lower, upper, state, divisors[0]),
    }


def terminal_credit_decomposition(lower: int, upper: int, state: int, factor_chain: tuple[int, ...]) -> dict[str, object]:
    """Decompose the full continuous-to-terminal credit along a true factor path.

    ``factor_chain`` contains factor steps e_1,...,e_m whose product is state.
    Cumulative products give a divisor chain 1=D_0|...|D_m=state.  Terminal
    phase equals one, so the total credit is exactly

        1 - (state-lower)/(upper-lower).
    """
    if not factor_chain or any(e < 2 for e in factor_chain):
        raise ValueError("factor_chain must contain integers >=2")
    cumulative = [1]
    product = 1
    for e in factor_chain:
        product *= e
        if state % product:
            raise ValueError("factor chain must be a genuine cumulative factorization")
        cumulative.append(product)
    if product != state:
        raise ValueError("factor_chain must multiply exactly to state")

    data = phase_cocycle(lower, upper, state, tuple(cumulative))
    terminal = data["phases"][-1]
    if terminal != 1:
        raise AssertionError("terminal divisor phase is not one")
    expected = 1 - Fraction(state - lower, upper - lower)
    if data["total_credit"] != expected:
        raise AssertionError("terminal credit failed exact conservation")
    return {**data, "factor_chain": factor_chain, "continuous_position": Fraction(state-lower, upper-lower)}


def kappa_chi_not_phase_complete_witness() -> dict[str, object]:
    """Minimal small witness that boundary support does not recover phase credit.

    In the square basin (36,49), divisor 5 has the same basin-level (kappa,chi)
    state for both hits 40 and 45, but their quotient phases/leads differ.  Thus
    the minimal boundary-support state (kappa,chi) is exact for directional hit
    support but is not, by itself, a complete runtime state for quantitative
    phase credit.  A within-window position/index is additional information.
    """
    lower, upper, k, d = 36, 49, 6, 5
    # H_d = 2, bulk 2*floor(k/d)=2, hence kappa=0; midpoint defect chi=0.
    kappa = ((upper - 1) // d - lower // d) - 2 * (k // d)
    middle = k * (k + 1)
    chi = 2 * (middle // d) - lower // d - upper // d
    p40 = divisor_phase(lower, upper, 40, d)
    p45 = divisor_phase(lower, upper, 45, d)
    pos40 = Fraction(40 - lower, upper - lower)
    pos45 = Fraction(45 - lower, upper - lower)
    if (kappa, chi) != (0, 0) or p40 == p45 or p40-pos40 == p45-pos45:
        raise AssertionError("phase-completeness counterexample changed")
    return {
        "k": k,
        "divisor": d,
        "kappa": kappa,
        "chi": chi,
        "state_a": 40,
        "state_b": 45,
        "phase_a": p40,
        "phase_b": p45,
        "lead_a": p40-pos40,
        "lead_b": p45-pos45,
        "verdict": "KAPPA_CHI_NOT_COMPLETE_FOR_QUANTITATIVE_PHASE",
    }
