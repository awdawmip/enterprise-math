"""P017/P018 Generation 3: signed parity-refined short-interval remainder.

For an odd divisor D, an odd state divisible by D lies in the single residue
class

    n == D (mod 2D).

This is the arithmetic form of the P017 signed-capacity rule "parity +
divisibility = one class modulo 2D".  In the square shell

    I_k = (k^2, k^2+2k],

its exact incidence count is

    g_odd(k,D)
      = floor((U_k+D)/(2D)) - floor((k^2+D)/(2D)).

Equivalently it counts odd quotients j with k^2 < D*j <= U_k.

For root-certified P3 pairs D=ab one has D>k, hence the shell width 2k is
strictly smaller than the period 2D and g_odd is a 0/1 gate.  It is exactly the
gate for the unique possible odd third factor in
`p017_p018_root_p3_pair_collapse`.

Centering by the uniform residue density gives

    rho_odd(k,D) = g_odd(k,D) - 2k/(2D)
                 = g_odd(k,D) - k/D.

Thus the root-P3 pair obstruction is naturally a bilinear sum of **signed
residue-class remainders modulo 2ab**, not merely ordinary multiple-count
remainders modulo ab.  The factor 2 does not by itself create analytic saving,
but it makes the P017 signed-capacity and Chen/Iwaniec remainder languages the
same exact finite object.
"""

from __future__ import annotations

from fractions import Fraction

from .p017_p018_buchstab_cutoff_ladder import square_interval_upper


def signed_odd_divisor_gate(k: int, divisor: int) -> dict[str, object]:
    """Count odd-quotient D-multiples in the consecutive-square shell."""
    for name, value in (("k", k), ("divisor", divisor)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if k < 1:
        raise ValueError("k must be positive")
    if divisor < 1 or divisor % 2 == 0:
        raise ValueError("divisor must be positive and odd")

    lower = k * k
    upper = square_interval_upper(k)
    modulus = 2 * divisor
    count = (upper + divisor) // modulus - (lower + divisor) // modulus

    direct = tuple(
        n for n in range(lower + 1, upper + 1) if n % modulus == divisor
    )
    if count != len(direct):
        raise AssertionError("mod-2D floor count disagreed with direct residue count")

    odd_quotients = tuple(n // divisor for n in direct)
    if any(q % 2 != 1 for q in odd_quotients):
        raise AssertionError("signed residue class lost odd quotient parity")

    density = Fraction(2 * k, modulus)
    centered = Fraction(count * modulus - 2 * k, modulus)
    if density + centered != count:
        raise AssertionError("signed remainder failed exact reconstruction")

    if divisor > k and count not in (0, 1):
        raise AssertionError("D>k should make the signed shell gate 0/1")

    return {
        "k": k,
        "lower": lower,
        "upper": upper,
        "divisor": divisor,
        "signed_modulus": modulus,
        "signed_residue": divisor,
        "count": count,
        "states": direct,
        "odd_quotients": odd_quotients,
        "density_main_term": density,
        "centered_signed_remainder": centered,
        "single_use_in_shell": divisor > k,
        "status": "P017_SIGNED_CLASS_EQUALS_BILINEAR_RESIDUE_GATE",
    }
