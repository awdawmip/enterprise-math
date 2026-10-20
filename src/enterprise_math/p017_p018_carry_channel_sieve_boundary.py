"""Exact sieve boundary of the P017/P018 quotient-channel carry network.

This module pushes the quotient-channel refinement monoid to its natural
negative boundary.

Fix K=k-1 and an odd parent modulus E.  If the nonempty parent fiber is
encoded by

    y_t = y_0 - 2t,              0 <= t < N,

then for every positive odd d

    F_(Ed)(K) = #{t < N : d | y_t}.

Consequently, for every positive odd squarefree Q,

    sum_(d|Q) mu(d) F_(Ed)(K)
      = #{t < N : gcd(y_0-2t,Q)=1}.

Thus an entire descendant Mobius subcube is exactly a finite rough/coprime
count on the parent quotient channel.  No approximation or density model is
involved.

Writing A=floor(K/E) and F_(Ed)=floor(K/(Ed))+eta_(Ed), the floor terms also
collapse exactly:

    sum_(d|Q) mu(d) eta_(Ed)(K)
      = #{t < N : gcd(y_0-2t,Q)=1}
        - #{1 <= m <= A : gcd(m,Q)=1}.

So the Mobius carry block is precisely the discrepancy between two finite
sifted sets.  For E=1 and Q equal to the odd prime wheel through K, the first
term is the odd candidate set in the consecutive-square interval and the
second term is the dyadic reference axis (1 and powers of two <=K).  This is
an exact segmented-sieve representation of the boundary-carry observable.

The same rough count has the standard Ramanujan-conductor expansion.  For
squarefree odd Q, with c_q the Ramanujan sum,

    Q*S_Q(N,y)
      = N*phi(Q)
        + sum_(q|Q,q>1) mu(q) phi(Q/q)
            sum_(t<N) c_q(y-2t),

where S_Q(N,y)=#{t<N:gcd(y-2t,Q)=1}.  Therefore moving Fourier from the
original modulus variable to quotient-channel index space does not create a
new observable: after Mobius recombination it is exactly the Ramanujan/Fourier
expansion of coprimality.  In an N-point transform of the occupancy sequence,
the desired count is its zero mode.

There is also a sharp independence boundary.  Let d_1,...,d_r>1 be pairwise
coprime odd moduli.  For either fixed parity of K and every bit vector
b_i in {0,1}, CRT gives arbitrarily large K with

    eta_(d_i)(K)=b_i  for all i.

Indeed the following local witnesses hold for every odd d>1:

    eta_d(0)=0,       eta_d(2d-2)=1,      (even K),
    eta_d(d)=0,       eta_d(2d-1)=1.      (odd K).

Hence pairwise-coprime carry coordinates can vary independently even for the
actual centered square phase M=(K+1)(K+2).  Composite-descendant correlations
remain, but they are exactly the divisor/CRT refinement correlations already
encoded by the monoid.  Any Legendre-relevant gain must therefore use a
moving-horizon property coupling K to the changing conductor family; it cannot
follow from a universal fixed-wheel carry-correlation law alone.

Status: bridge-local proved algebraic boundary.  It does not prove Legendre's
conjecture and does not claim that every possible moving-horizon argument is
parity-limited.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd

from .p017_p018_carry_refinement_channel import signed_fiber_channel_state


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


def _require_positive_odd(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1 or value % 2 == 0:
        raise ValueError(f"{name} must be a positive odd integer")


def _squarefree_prime_factors(value: int) -> tuple[int, ...]:
    """Return prime factors, rejecting non-squarefree inputs."""
    _require_positive_odd("value", value)
    if value == 1:
        return ()
    factors: list[int] = []
    remainder = value
    prime = 3
    while prime * prime <= remainder:
        if remainder % prime == 0:
            remainder //= prime
            if remainder % prime == 0:
                raise ValueError("value must be squarefree")
            factors.append(prime)
        prime += 2
    if remainder > 1:
        factors.append(remainder)
    return tuple(factors)


def _squarefree_divisors_with_mobius(value: int) -> tuple[tuple[int, int], ...]:
    factors = _squarefree_prime_factors(value)
    terms: list[tuple[int, int]] = [(1, 1)]
    for size in range(1, len(factors) + 1):
        sign = -1 if size % 2 else 1
        for subset in combinations(factors, size):
            divisor = 1
            for prime in subset:
                divisor *= prime
            terms.append((divisor, sign))
    return tuple(terms)


def _phi_squarefree(value: int) -> int:
    result = 1
    for prime in _squarefree_prime_factors(value):
        result *= prime - 1
    return result


def _mobius_squarefree(value: int) -> int:
    return -1 if len(_squarefree_prime_factors(value)) % 2 else 1


def channel_rough_count(fiber_size: int, first_quotient: int | None, wheel: int) -> int:
    """Count quotient-channel indices whose transported quotient is Q-rough."""
    _require_nonnegative("fiber_size", fiber_size)
    _squarefree_prime_factors(wheel)
    if fiber_size == 0:
        if first_quotient is not None:
            raise ValueError("empty channel must use first_quotient=None")
        return 0
    if isinstance(first_quotient, bool) or not isinstance(first_quotient, int):
        raise ValueError("nonempty channel requires an integer first_quotient")
    if first_quotient % 2 == 0:
        raise ValueError("first_quotient must be odd")
    return sum(gcd(first_quotient - 2 * index, wheel) == 1 for index in range(fiber_size))


def initial_rough_count(length: int, wheel: int) -> int:
    """Count 1<=m<=length with gcd(m,Q)=1."""
    _require_nonnegative("length", length)
    _squarefree_prime_factors(wheel)
    return sum(gcd(value, wheel) == 1 for value in range(1, length + 1))


def mobius_descendant_sieve_identity(K: int, parent_modulus: int, wheel: int) -> dict[str, object]:
    """Verify sum mu(d)F_(Ed) equals one exact channel rough count."""
    _require_nonnegative("K", K)
    _require_positive_odd("parent_modulus", parent_modulus)
    terms = _squarefree_divisors_with_mobius(wheel)
    parent = signed_fiber_channel_state(K, parent_modulus)
    fiber_size = int(parent["fiber_size"])
    first_quotient = parent["first_quotient"]
    rough_count = channel_rough_count(
        fiber_size,
        None if first_quotient is None else int(first_quotient),
        wheel,
    )

    descendants: list[dict[str, int]] = []
    mobius_sum = 0
    carry_sum = 0
    for divisor, mu in terms:
        child = signed_fiber_channel_state(K, parent_modulus * divisor)
        child_size = int(child["fiber_size"])
        child_carry = int(child["centered_carry"])
        mobius_sum += mu * child_size
        carry_sum += mu * child_carry
        descendants.append(
            {
                "divisor": divisor,
                "mobius": mu,
                "child_modulus": parent_modulus * divisor,
                "fiber_size": child_size,
                "centered_carry": child_carry,
            }
        )

    if mobius_sum != rough_count:
        raise AssertionError("descendant Mobius sum did not collapse to channel rough count")

    reference_length = K // parent_modulus
    reference_rough = initial_rough_count(reference_length, wheel)
    discrepancy = rough_count - reference_rough
    if carry_sum != discrepancy:
        raise AssertionError("Mobius carry block did not equal exact rough-count discrepancy")

    return {
        "K": K,
        "parent_modulus": parent_modulus,
        "wheel": wheel,
        "parent": parent,
        "descendants": tuple(descendants),
        "mobius_fiber_sum": mobius_sum,
        "channel_rough_count": rough_count,
        "reference_length": reference_length,
        "reference_rough_count": reference_rough,
        "mobius_carry_sum": carry_sum,
        "rough_count_discrepancy": discrepancy,
        "exact_sieve_collapse": True,
    }


def ramanujan_sum_squarefree(modulus: int, value: int) -> int:
    """Return c_q(value) for squarefree odd q using the exact gcd formula."""
    factors = _squarefree_prime_factors(modulus)
    if not factors:
        return 1
    common = gcd(modulus, value)
    quotient = modulus // common
    mu = _mobius_squarefree(quotient)
    return mu * (_phi_squarefree(modulus) // _phi_squarefree(quotient))


def ramanujan_channel_rough_count(
    fiber_size: int,
    first_quotient: int | None,
    wheel: int,
) -> dict[str, int | bool]:
    """Evaluate the exact conductor/Ramanujan expansion of channel roughness."""
    _require_nonnegative("fiber_size", fiber_size)
    terms = _squarefree_divisors_with_mobius(wheel)
    if fiber_size == 0:
        if first_quotient is not None:
            raise ValueError("empty channel must use first_quotient=None")
        first = 1
    else:
        if isinstance(first_quotient, bool) or not isinstance(first_quotient, int):
            raise ValueError("nonempty channel requires an integer first_quotient")
        if first_quotient % 2 == 0:
            raise ValueError("first_quotient must be odd")
        first = first_quotient

    numerator = fiber_size * _phi_squarefree(wheel)
    conductor_correction = 0
    for conductor, mu in terms:
        if conductor == 1:
            continue
        channel_ramanujan_sum = sum(
            ramanujan_sum_squarefree(conductor, first - 2 * index)
            for index in range(fiber_size)
        )
        conductor_correction += (
            mu * _phi_squarefree(wheel // conductor) * channel_ramanujan_sum
        )
    numerator += conductor_correction
    if numerator % wheel:
        raise AssertionError("Ramanujan conductor numerator lost integrality")
    reconstructed = numerator // wheel
    direct = channel_rough_count(
        fiber_size,
        None if fiber_size == 0 else first,
        wheel,
    )
    if reconstructed != direct:
        raise AssertionError("Ramanujan conductor expansion disagrees with direct rough count")
    return {
        "wheel": wheel,
        "fiber_size": fiber_size,
        "main_numerator": fiber_size * _phi_squarefree(wheel),
        "conductor_correction_numerator": conductor_correction,
        "total_numerator": numerator,
        "rough_count": reconstructed,
        "direct_rough_count": direct,
        "exact_ramanujan_reconstruction": True,
    }


def realize_pairwise_coprime_carry_bits(
    moduli: tuple[int, ...],
    bits: tuple[int, ...],
    parity: int,
    minimum_K: int = 0,
) -> dict[str, object]:
    """CRT-realize arbitrary centered-carry bits on pairwise-coprime odd moduli."""
    if len(moduli) != len(bits):
        raise ValueError("moduli and bits must have the same length")
    if parity not in (0, 1):
        raise ValueError("parity must be 0 or 1")
    _require_nonnegative("minimum_K", minimum_K)
    for modulus in moduli:
        _require_positive_odd("modulus", modulus)
        if modulus == 1:
            raise ValueError("carry-independence moduli must exceed 1")
    for bit in bits:
        if bit not in (0, 1):
            raise ValueError("bits must be 0 or 1")
    for left, right in combinations(moduli, 2):
        if gcd(left, right) != 1:
            raise ValueError("moduli must be pairwise coprime")

    # Solve K=parity (mod 2) together with one residue modulo each odd modulus.
    value = parity
    period = 2
    local_residues: list[int] = []
    for modulus, bit in zip(moduli, bits, strict=True):
        if bit == 0:
            residue = 0
        elif parity == 0:
            residue = (-2) % modulus
        else:
            residue = (-1) % modulus
        local_residues.append(residue)
        step = ((residue - value) * pow(period, -1, modulus)) % modulus
        value += period * step
        period *= modulus
        value %= period

    target_floor = max((minimum_K, *moduli), default=minimum_K)
    if value < target_floor:
        value += ((target_floor - value + period - 1) // period) * period

    realized = tuple(
        int(signed_fiber_channel_state(value, modulus)["centered_carry"])
        for modulus in moduli
    )
    if realized != bits:
        raise AssertionError("CRT carry witness did not realize the requested bit vector")
    if value % 2 != parity:
        raise AssertionError("CRT carry witness lost the requested parity")

    return {
        "K": value,
        "period": period,
        "parity": parity,
        "moduli": moduli,
        "requested_bits": bits,
        "realized_bits": realized,
        "local_residues": tuple(local_residues),
        "arbitrarily_large_by_period_shift": True,
    }
