"""CRT independence of local negative-square phases.

The square-root diagonal uses forbidden classes

    a_p = -k^2 (mod p).

It is tempting to regard the fact that all classes arise from one square as a
cross-prime compatibility constraint.  At the purely modular level that is
false.  For a prime p define

    A_p = {-u^2 (mod p) : u (mod p)}.

Choose *arbitrarily and independently* one a_p in A_p for each prime in a
finite set.  Choose a local root u_p with u_p^2=-a_p (mod p).  The Chinese
remainder theorem glues the u_p to a global class x modulo the product P, and
then every chosen phase is simultaneously

    a_p = -x^2 (mod p).

Thus local negative-square admissibility is the complete modular compatibility
condition.  There is no additional conductor-to-conductor obstruction before
one asks which integer lift of x modulo P is distinguished.

For the Legendre square diagonal, the surviving datum is therefore
Archimedean rather than merely modular: the distinguished lift is the literal
small integer x=k that also sets the cutoff and interval scale.  This module
does **not** claim that k is the minimal CRT root, nor that covering CRT classes
cannot have smaller representatives.
"""

from __future__ import annotations

from math import prod
from typing import Iterable

from .legendre import is_prime


def negative_square_residues(p: int) -> tuple[int, ...]:
    """Return {-u^2 mod p}; for odd p this has (p+1)/2 elements."""
    if isinstance(p, bool) or not isinstance(p, int) or not is_prime(p):
        raise ValueError("p must be prime")
    return tuple(sorted({(-u * u) % p for u in range(p)}))


def _crt_pair(x: int, modulus: int, residue: int, p: int) -> tuple[int, int]:
    """Glue x mod modulus and residue mod prime p, assuming coprimality."""
    if modulus == 1:
        return residue % p, p
    correction = ((residue - x) * pow(modulus, -1, p)) % p
    new_modulus = modulus * p
    return (x + modulus * correction) % new_modulus, new_modulus


def glue_negative_square_phases(
    assignments: Iterable[tuple[int, int]],
) -> dict[str, object]:
    """Glue arbitrary locally admissible negative-square residues by CRT.

    ``assignments`` is an iterable of distinct ``(prime, phase_residue)`` pairs.
    A deterministic smallest nonnegative local square root is selected at each
    prime only to produce one canonical global witness.  Other independent sign
    choices give the remaining CRT root classes.
    """
    normalized = tuple((int(p), int(a)) for p, a in assignments)
    if not normalized:
        raise ValueError("at least one prime phase is required")

    seen: set[int] = set()
    local_data: list[tuple[int, int, tuple[int, ...], int]] = []
    for p, phase in normalized:
        if p in seen:
            raise ValueError("prime moduli must be distinct")
        seen.add(p)
        if not is_prime(p):
            raise ValueError("all moduli must be prime")
        phase %= p
        roots = tuple(u for u in range(p) if (u * u + phase) % p == 0)
        if not roots:
            raise ValueError("phase is not a negative-square residue modulo p")
        local_data.append((p, phase, roots, roots[0]))

    root = 0
    modulus = 1
    for p, _phase, _roots, chosen_root in local_data:
        root, modulus = _crt_pair(root, modulus, chosen_root, p)

    for p, phase, _roots, _chosen in local_data:
        if (-root * root) % p != phase:
            raise AssertionError("CRT root failed to realize a local square phase")

    expected_modulus = prod(p for p, _phase, _roots, _chosen in local_data)
    if modulus != expected_modulus:
        raise AssertionError("CRT modulus product mismatch")

    root_class_multiplicity = prod(
        len(roots) for _p, _phase, roots, _chosen in local_data
    )

    return {
        "assignments": tuple((p, phase) for p, phase, _roots, _chosen in local_data),
        "local_roots": tuple(
            (p, phase, roots) for p, phase, roots, _chosen in local_data
        ),
        "chosen_local_roots": tuple(
            (p, chosen) for p, _phase, _roots, chosen in local_data
        ),
        "crt_root": root,
        "crt_modulus": modulus,
        "root_class_multiplicity": root_class_multiplicity,
        "all_local_negative_square_choices_glue": True,
    }


def verify_phase_covering_lift(
    assignments: Iterable[tuple[int, int]],
    horizon: int,
) -> dict[str, object]:
    """If local phase classes cover [1,horizon], verify the glued root does too."""
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be a positive integer")

    glued = glue_negative_square_phases(assignments)
    phase_map = dict(glued["assignments"])
    root = int(glued["crt_root"])

    local_cover: list[tuple[int, int]] = []
    for offset in range(1, horizon + 1):
        covering_prime = next(
            (p for p, phase in phase_map.items() if offset % p == phase),
            None,
        )
        if covering_prime is None:
            return {
                **glued,
                "horizon": horizon,
                "locally_covers_horizon": False,
                "first_uncovered_offset": offset,
                "covering_witnesses": tuple(local_cover),
            }
        if (root * root + offset) % covering_prime != 0:
            raise AssertionError("local phase cover did not survive CRT gluing")
        local_cover.append((offset, covering_prime))

    return {
        **glued,
        "horizon": horizon,
        "locally_covers_horizon": True,
        "first_uncovered_offset": None,
        "covering_witnesses": tuple(local_cover),
        "glued_root_covers_horizon": True,
    }
