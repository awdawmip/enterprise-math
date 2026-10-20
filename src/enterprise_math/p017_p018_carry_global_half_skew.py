"""Exact global half-period skew of the Mobius carry field.

For every odd squarefree E>1, p017_p018_carry_phase_mean proves

    sum_(K=E)^(2E-1) eta_E(K)
      - sum_(K=0)^(E-1) eta_E(K) = 2.

The modulus E=1 is the parity carry `eta_1(K)=K mod 2` and has half-period skew
1 on its own period 2.

Let P>1 be odd squarefree and embed every eta_E, E|P, in the common period 2P:

    C_P(K)=sum_(E|P) mu(E) eta_E(K).

Because P/E is odd, shifting K by P induces exactly a half-period shift by E in
every period-2E component.  Over a global half of length P, the E>1 component
therefore contributes its same two-unit skew, while E=1 contributes one unit.
Since

    sum_(E|P) mu(E)=0,

the full Mobius field has the universal skew

    sum_(K=P)^(2P-1) C_P(K)
      - sum_(K=0)^(P-1) C_P(K)
      = 1 + 2 sum_(E|P,E>1) mu(E)
      = -1.

Thus the attractive +2 directional bias of every nontrivial individual modulus
does **not** accumulate into a positive global advantage.  Mobius recombination
cancels it exactly and reverses the residual sign to -1.  Period mean and
half-period skew are therefore insufficient statistics for a pointwise Legendre
bound; finer conductor/channel phase information is mandatory.
"""

from __future__ import annotations

from .legendre import squarefree_divisors_with_mu
from .p017_p018_carry_phase_mean import (
    _odd_squarefree_prime_factors,
    unified_centered_carry_bit,
)


def global_mobius_carry_half_skew(primorial: int) -> dict[str, object]:
    """Verify the universal -1 half-period skew on the common period 2P."""
    factors = _odd_squarefree_prime_factors(primorial)
    if not factors:
        raise ValueError("primorial must be an odd squarefree integer >1")
    P = primorial
    rows = squarefree_divisors_with_mu(list(factors))
    field = tuple(
        sum(mu * unified_centered_carry_bit(K, E) for E, mu in rows)
        for K in range(2 * P)
    )
    first = sum(field[:P])
    second = sum(field[P:])
    skew = second - first
    if skew != -1:
        raise AssertionError("global Mobius carry half-period skew is not -1")
    return {
        "primorial": P,
        "prime_factors": factors,
        "global_period": 2 * P,
        "first_half_mass": first,
        "second_half_mass": second,
        "second_minus_first_half": skew,
        "universal_global_half_skew": -1,
        "field": field,
    }
