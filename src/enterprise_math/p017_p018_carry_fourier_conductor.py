"""Fourier-conductor decomposition of the unified P017×P018 carry phase field.

Let E be a positive odd modulus, Q=2E, K=k-1, and eta_E(K) the unified binary
centered carry from p017_p018_carry_phase_mean.  Put

    beta_Q(n) = (n mod Q)/Q,
    s = K mod E.

The floor-carry identity has the exact sawtooth form

    eta_E(K)
      = (2s+1)/Q
        + beta_Q((K+1)^2+E)
        - beta_Q((K+2)^2+E-2).

Thus the carry phase is a deterministic period-E ramp plus the difference of
two quadratic finite sawtooths.

Use the normalized DFT on Z/QZ,

    hat f(r) = (1/Q) sum_(K mod Q) f(K) zeta^(-rK),
    zeta=exp(2*pi*i/Q).

For h!=0 the normalized Fourier coefficient of beta_Q is

    c_Q(h) = -1/[Q(1-zeta^(-h))].

Define the normalized quadratic Gauss sum

    G_E(h,r) = (1/Q) sum_(K mod Q)
                 zeta^[h(K+1)^2-rK].

Changing K to K+1 in the second quadratic sawtooth gives the exact carry DFT

    hat eta_E(r)
      = hat ramp_E(r)
        + sum_(h=1)^(Q-1)
            c_Q(h) (-1)^h [1-zeta^(r-2h)] G_E(h,r).

The ramp coefficients are explicit:

    hat ramp_E(0)=1/2,
    hat ramp_E(r)=0                         for odd r,
    hat ramp_E(r)=-1/[E(1-zeta^(-r))]      for nonzero even r.

Hence every odd carry frequency is purely quadratic.

The Gauss sums admit an elementary square-root bound requiring no deep analytic
number theory.  For the unnormalized sum S=Q G, expand |S|^2 and set d=K-L.
The inner L-sum vanishes unless Q|2hd; there are gcd(2h,Q) such d.  Therefore

    |G_E(h,r)|^2 <= gcd(2h,Q)/Q = gcd(h,E)/E.

For odd r and squarefree E this combines with
`|1-exp(-2*pi*i*h/Q)|=2|sin(pi*h/Q)|` and the harmonic divisor bound to give

    |hat eta_E(r)|
      <= (1+log E)/sqrt(E) * product_(p|E)(1+p^(-1/2)).

The useful point is structural: odd-frequency oscillation is a complete
quadratic-exponential object with square-root conductor control, while the even
ramp is an explicit deterministic term.

There is also an exact cross-modulus conductor triangle.  For odd squarefree P,
embed every eta_E, E|P, into the common period 2P and define

    C_P(K)=sum_(E|P) mu(E) eta_E(K).

If h is a global Fourier index, period lifting gives

    hat C_P(h)
      = sum_(d | gcd(P,h))
          mu(P/d) hat eta_(P/d)(h/d).

Indeed a period-2E function repeated P/E times contributes to global frequency
h iff P/E divides h.  Consequently:

* h=0 is exactly the previously factorized Mobius period mean;
* if gcd(P,h)=1, only the top modulus survives:

      hat C_P(h)=mu(P) hat eta_P(h).

Thus primitive global frequencies cannot be canceled by lower-modulus carry
fields.  Nonprimitive frequencies form a divisor-triangular lower-conductor
hierarchy.  This is the natural Fourier analogue of the quotient-channel
refinement monoid.

These identities expose cross-modulus phase structure but do not prove a
pointwise lower bound for the full Mobius carry sum.  Any Legendre application
must still control the coherent special phase K=k-1 rather than only individual
Fourier coefficients or period means.
"""

from __future__ import annotations

from cmath import exp, pi
from math import gcd, log, prod, sin, sqrt

from .legendre import squarefree_divisors_with_mu
from .p017_p018_carry_phase_mean import (
    _odd_squarefree_prime_factors,
    unified_centered_carry_bit,
)


def _normalized_dft(values: tuple[float, ...], frequency: int) -> complex:
    period = len(values)
    zeta = exp(2j * pi / period)
    return sum(
        value * zeta ** (-frequency * index)
        for index, value in enumerate(values)
    ) / period


def carry_sawtooth_value(K: int, modulus: int) -> float:
    """Evaluate the exact ramp+quadratic-sawtooth expression diagnostically."""
    if isinstance(K, bool) or not isinstance(K, int) or K < 0:
        raise ValueError("K must be a nonnegative integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError("modulus must be a positive odd integer")
    E = modulus
    Q = 2 * E
    s = K % E
    lower = ((K + 1) ** 2 + E) % Q
    upper = ((K + 2) ** 2 + E - 2) % Q
    return (2 * s + 1) / Q + lower / Q - upper / Q


def normalized_carry_fourier_coefficient(modulus: int, frequency: int) -> complex:
    """Return the normalized DFT coefficient of eta_E by direct finite sum."""
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError("modulus must be a positive odd integer")
    Q = 2 * modulus
    r = frequency % Q
    values = tuple(float(unified_centered_carry_bit(K, modulus)) for K in range(Q))
    return _normalized_dft(values, r)


def normalized_quadratic_gauss_sum(modulus: int, h: int, frequency: int) -> complex:
    """Return G_E(h,r) on the common period Q=2E."""
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError("modulus must be a positive odd integer")
    E = modulus
    Q = 2 * E
    zeta = exp(2j * pi / Q)
    r = frequency % Q
    return sum(
        zeta ** (h * (K + 1) ** 2 - r * K)
        for K in range(Q)
    ) / Q


def carry_fourier_gauss_reconstruction(modulus: int, frequency: int) -> dict[str, object]:
    """Reconstruct hat eta_E(r) from the ramp and quadratic Gauss sums."""
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError("modulus must be a positive odd integer")
    E = modulus
    Q = 2 * E
    r = frequency % Q
    zeta = exp(2j * pi / Q)

    if r == 0:
        ramp = 0.5 + 0j
    elif r % 2 == 1:
        ramp = 0j
    else:
        ramp = -1 / (E * (1 - zeta ** (-r)))

    quadratic = 0j
    gauss_rows: list[dict[str, object]] = []
    for h in range(1, Q):
        coefficient = -1 / (Q * (1 - zeta ** (-h)))
        gauss = normalized_quadratic_gauss_sum(E, h, r)
        gauss_bound = sqrt(gcd(h, E) / E)
        if abs(gauss) > gauss_bound + 1e-10:
            raise AssertionError("quadratic Gauss sum exceeded elementary gcd bound")
        term = coefficient * ((-1) ** h) * (1 - zeta ** (r - 2 * h)) * gauss
        quadratic += term
        gauss_rows.append(
            {
                "h": h,
                "sawtooth_coefficient": coefficient,
                "gauss_sum": gauss,
                "gauss_bound": gauss_bound,
                "term": term,
            }
        )

    reconstructed = ramp + quadratic
    direct = normalized_carry_fourier_coefficient(E, r)
    if abs(reconstructed - direct) > 1e-9:
        raise AssertionError("Gauss-sum carry Fourier reconstruction failed")

    return {
        "modulus": E,
        "period": Q,
        "frequency": r,
        "ramp_coefficient": ramp,
        "quadratic_coefficient": quadratic,
        "reconstructed_carry_coefficient": reconstructed,
        "direct_carry_coefficient": direct,
        "odd_frequency_is_purely_quadratic": r % 2 == 1,
        "gauss_rows": tuple(gauss_rows),
    }


def odd_frequency_squarefree_bound(modulus: int) -> float:
    """Return the simple square-root/harmonic bound for odd carry frequencies."""
    factors = _odd_squarefree_prime_factors(modulus)
    E = modulus
    if E == 1:
        return 1.0
    divisor_factor = prod(1.0 + prime ** -0.5 for prime in factors)
    return ((1.0 + log(E)) / sqrt(E)) * divisor_factor


def mobius_carry_field_fourier_coefficient(
    primorial: int,
    frequency: int,
) -> dict[str, object]:
    """Verify the exact divisor-triangular conductor formula on period 2P."""
    factors = _odd_squarefree_prime_factors(primorial)
    P = primorial
    Q = 2 * P
    h = frequency % Q
    divisor_rows = squarefree_divisors_with_mu(list(factors))

    field = tuple(
        float(sum(mu * unified_centered_carry_bit(K, E) for E, mu in divisor_rows))
        for K in range(Q)
    )
    direct = _normalized_dft(field, h)

    g = gcd(P, h)
    triangular = 0j
    rows: list[dict[str, object]] = []
    for d, _mu_d in squarefree_divisors_with_mu(list(_odd_squarefree_prime_factors(g))):
        E = P // d
        mu_E = next(mu for divisor, mu in divisor_rows if divisor == E)
        local_frequency = h // d
        local = normalized_carry_fourier_coefficient(E, local_frequency)
        triangular += mu_E * local
        rows.append(
            {
                "frequency_divisor": d,
                "source_modulus": E,
                "source_mu": mu_E,
                "local_frequency": local_frequency,
                "local_coefficient": local,
            }
        )

    if abs(triangular - direct) > 1e-9:
        raise AssertionError("global carry conductor triangle failed")
    primitive = gcd(P, h) == 1
    if primitive:
        top_mu = next(mu for divisor, mu in divisor_rows if divisor == P)
        top = top_mu * normalized_carry_fourier_coefficient(P, h)
        if abs(direct - top) > 1e-9:
            raise AssertionError("primitive global frequency received lower-modulus mass")

    return {
        "primorial": P,
        "prime_factors": factors,
        "global_period": Q,
        "frequency": h,
        "frequency_gcd_with_primorial": g,
        "primitive_frequency": primitive,
        "direct_global_coefficient": direct,
        "triangular_coefficient": triangular,
        "source_rows": tuple(rows),
    }
