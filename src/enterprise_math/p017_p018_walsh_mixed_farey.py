"""Mixed orientation-Walsh roots as determinant-one/Farey phases.

For an even squarefree conductor q=ab with (a,b)=1, let a collect positive
orientation primes and b negative orientation primes.  The two pure splits
b=1 and a=1 are the global roots u=+1 and u=-1.  At even support degree both
carry coefficient +1, so their physical incidences are nonnegative resources in
a lower-bound argument.  The potentially harmful part is therefore the mixed
family a,b>1.

For one mixed split choose x=inv(a,b) with 1<=x<b and put

    t=(a*x-1)/b.

Then 0<=t<a and

    a*x-b*t=1.

Thus t/a and x/b are neighboring determinant-one/Farey fractions.  The signed
unity root

    u = 1-2a*x (mod ab)

obeys the exact normalized identity

    u/(ab) = -(x/b+t/a) (mod 1).

Consequently the P017 root phase is

    e(h M u/(ab)) = e(-h M (x/b+t/a)).

Equivalently, the reciprocity cosine from
p017_p018_walsh_root_kloosterman is a cosine of the sum of two determinant-one
fractions.  This removes the spurious large-discriminant formulation
r^2-M^2=0: after scaling by M^{-1}, the polynomial is the fixed u^2-1, while
the square-basin information sits in the moving high-frequency phase hM.

The classical reducible-quadratic Weyl-sum obstruction from the two linear
roots u=+/-1 is absent after restricting to this mixed family.  This does NOT
prove mixed-root equidistribution; it identifies the precise signed spectral
object for which a new estimate would be needed.
"""

from __future__ import annotations

from cmath import exp, pi
from math import gcd


def mixed_farey_coordinates(a: int, b: int) -> dict[str, object]:
    """Return determinant-one coordinates and the signed unity root for a,b>1."""
    for name, value in (("a", a), ("b", b)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 1 or value % 2 == 0:
            raise ValueError(f"{name} must be an odd integer >1")
    if gcd(a, b) != 1:
        raise ValueError("a,b must be coprime")
    q = a * b
    x = pow(a, -1, b)
    t = (a * x - 1) // b
    if a * x - b * t != 1:
        raise AssertionError("determinant-one identity failed")
    if not (1 <= x < b and 0 <= t < a):
        raise AssertionError("Farey coordinates left canonical ranges")

    root_u = (1 - 2 * a * x) % q
    if root_u % a != 1 % a or root_u % b != (-1) % b:
        raise AssertionError("mixed signed-unity root lost orientation residues")

    # Check u/q = -(x/b+t/a) modulo one without floating point:
    # u + a*x + b*t is divisible by q.
    numerator = root_u + a * x + b * t
    if numerator % q != 0:
        raise AssertionError("Farey phase identity failed modulo one")

    return {
        "a": a,
        "b": b,
        "conductor": q,
        "inverse_a_mod_b": x,
        "companion_t": t,
        "determinant_one": True,
        "signed_unity_root_u": root_u,
        "farey_phase_integer_multiple": numerator // q,
        "mixed_root": True,
    }


def mixed_farey_phase(k: int, a: int, b: int, frequency: int) -> dict[str, object]:
    """Verify e(hMu/q)=e(-hM(x/b+t/a)) exactly up to numerical evaluation."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(frequency, bool) or not isinstance(frequency, int):
        raise ValueError("frequency must be an integer")
    row = mixed_farey_coordinates(a, b)
    M = k * (k + 1)
    q = int(row["conductor"])
    u = int(row["signed_unity_root_u"])
    x = int(row["inverse_a_mod_b"])
    t = int(row["companion_t"])
    h = frequency

    root_phase = exp(2j * pi * h * M * u / q)
    farey_phase = exp(-2j * pi * h * M * (x / b + t / a))
    if abs(root_phase - farey_phase) > 1e-8:
        raise AssertionError("mixed root Fourier phase disagreed with Farey phase")
    return {
        **row,
        "k": k,
        "center": M,
        "frequency": h,
        "root_fourier_phase": root_phase,
        "farey_determinant_phase": farey_phase,
        "phase_identity": True,
    }


def pure_even_root_phases(k: int, conductor: int, frequency: int) -> dict[str, object]:
    """Return the two nonnegative-coefficient pure-root phases at even support degree.

    This routine only records the phase pair.  Physical boundary incidences of
    these pure roots are ordinary nonnegative same-orientation counts and may be
    discarded when seeking a lower bound for a signed even-conductor correction.
    """
    if conductor <= 1 or conductor % 2 == 0:
        raise ValueError("conductor must be odd and >1")
    M = k * (k + 1)
    q = conductor
    plus = exp(2j * pi * frequency * M / q)
    minus = exp(-2j * pi * frequency * M / q)
    return {
        "k": k,
        "conductor": q,
        "frequency": frequency,
        "plus_root_phase": plus,
        "minus_root_phase": minus,
        "pure_pair_phase_sum": plus + minus,
        "pure_even_coefficients_positive": True,
    }
