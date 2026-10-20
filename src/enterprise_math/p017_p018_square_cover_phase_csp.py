"""Finite CSP for square-compatible covering phases.

Fix y>=2.  A fixed-y square covering root x covers every offset 1<=r<=2y by
some prime p<=y with

    r = -x^2 (mod p).

For each prime p define the locally admissible phase set

    A_p = {-u^2 (mod p) : u mod p}.

Because arbitrary choices a_p in A_p glue by CRT to a simultaneous square root,
the existence of *some* fixed-y square covering root is exactly the finite
partitioned set-cover problem:

- choose at most one phase a_p in A_p for each p<=y;
- require every r in {1,...,2y} to lie in at least one chosen class r=a_p mod p.

Unchosen primes can be assigned arbitrary local phases afterwards.  Thus phase
feasibility is purely finite combinatorics; root height is a second, separate
question obtained by minimizing the positive CRT square roots of a feasible
phase vector.

This file contains validators and one explicit y=73 feasible certificate.  It
does not claim that 73 is the first feasible y, nor that the displayed CRT root
is the global covering height h(73).
"""

from __future__ import annotations

from itertools import product

from .legendre import is_prime, primes_up_to
from .p017_p018_square_covering_height import is_fixed_y_square_covering_root
from .p017_p018_square_phase_crt import negative_square_residues
from .p017_p018_square_sign_orbit import primorial


Y73_PHASE_CERTIFICATE: tuple[tuple[int, int], ...] = (
    (2, 0),
    (3, 2),
    (5, 0),
    (7, 0),
    (11, 2),
    (13, 9),
    (17, 1),
    (19, 3),
    (23, 19),
    (29, 22),
    (31, 6),
    (37, 30),
    (41, 39),
    (43, 0),
    (47, 33),
    (53, 28),
    (59, 14),
    (61, 27),
    (67, 31),
    (71, 22),
    (73, 24),
)

Y73_PHASE_MINIMUM_SIGN_LIFT = 627431388493620297650


def verify_square_cover_phase(
    y: int, assignments: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    """Verify a finite negative-square phase vector covers 1,...,2y."""
    if isinstance(y, bool) or not isinstance(y, int) or y < 2:
        raise ValueError("y must be an integer >=2")

    phase_map: dict[int, int] = {}
    for p, phase in assignments:
        if not is_prime(p) or p > y:
            raise ValueError("phase moduli must be distinct primes <=y")
        if p in phase_map:
            raise ValueError("each prime may receive at most one phase")
        phase %= p
        if phase not in negative_square_residues(p):
            raise ValueError("phase must be a negative-square residue")
        phase_map[p] = phase

    covering_witnesses: list[tuple[int, int]] = []
    for r in range(1, 2 * y + 1):
        p = next(
            (p for p, phase in phase_map.items() if r % p == phase),
            None,
        )
        if p is None:
            return {
                "y": y,
                "assignments": tuple(sorted(phase_map.items())),
                "covers_full_horizon": False,
                "first_uncovered_offset": r,
                "covering_witnesses": tuple(covering_witnesses),
            }
        covering_witnesses.append((r, p))

    return {
        "y": y,
        "assignments": tuple(sorted(phase_map.items())),
        "covers_full_horizon": True,
        "first_uncovered_offset": None,
        "covering_witnesses": tuple(covering_witnesses),
    }


def minimum_positive_square_root_of_phase(
    assignments: tuple[tuple[int, int], ...]
) -> dict[str, object]:
    """Enumerate all sign roots of one bounded phase vector and return the least.

    Intended for finite certificates such as y=73.  The number of root classes
    is the product of the local root multiplicities and may grow exponentially.
    """
    local: list[tuple[int, int, tuple[int, ...]]] = []
    for p, phase in assignments:
        phase %= p
        roots = tuple(u for u in range(p) if (-u * u) % p == phase)
        if not roots:
            raise ValueError("phase is not a negative-square residue")
        local.append((p, phase, roots))

    classes: list[int] = []
    wheel = 1
    for p, _phase, _roots in local:
        wheel *= p

    for root_tuple in product(*(roots for _p, _phase, roots in local)):
        x = 0
        modulus = 1
        for (p, _phase, _roots), residue in zip(local, root_tuple):
            if modulus == 1:
                x = residue % p
                modulus = p
                continue
            correction = ((residue - x) * pow(modulus, -1, p)) % p
            x = (x + modulus * correction) % (modulus * p)
            modulus *= p
        if modulus != wheel:
            raise AssertionError("phase-root CRT modulus mismatch")
        classes.append(x)

    positive = tuple(sorted(x for x in set(classes) if x > 0))
    if not positive:
        raise AssertionError("phase vector has no positive CRT root class")
    minimum = positive[0]

    return {
        "assignments": tuple(assignments),
        "wheel": wheel,
        "root_class_count": len(set(classes)),
        "minimum_positive_root": minimum,
        "positive_roots": positive,
    }


def y73_square_cover_phase_certificate() -> dict[str, object]:
    """Verify one explicit y=73 feasible phase and its finite sign-orbit minimum."""
    phase = verify_square_cover_phase(73, Y73_PHASE_CERTIFICATE)
    if not phase["covers_full_horizon"]:
        raise AssertionError("y=73 phase certificate no longer covers all offsets")

    root_data = minimum_positive_square_root_of_phase(Y73_PHASE_CERTIFICATE)
    minimum = int(root_data["minimum_positive_root"])
    if minimum != Y73_PHASE_MINIMUM_SIGN_LIFT:
        raise AssertionError("y=73 phase minimum sign lift changed")
    if root_data["wheel"] != primorial(73):
        raise AssertionError("y=73 phase root wheel mismatch")
    if not is_fixed_y_square_covering_root(minimum, 73):
        raise AssertionError("minimum phase root lost its fixed-y full cover")

    return {
        **phase,
        "root_class_count": root_data["root_class_count"],
        "minimum_positive_sign_lift": minimum,
        "covering_height_upper_bound": minimum,
        "minimum_over_diagonal_ratio": minimum / 73,
        "phase_feasibility_verified": True,
        "not_first_feasible_y_claim": True,
        "not_global_h73_minimality_claim": True,
    }


def exhaustive_phase_feasibility_small_y(y: int) -> dict[str, object]:
    """Exhaust all phase vectors for very small y; use only in bounded regressions."""
    if isinstance(y, bool) or not isinstance(y, int) or not (2 <= y <= 13):
        raise ValueError("small exhaustive phase search is restricted to 2<=y<=13")
    primes = tuple(primes_up_to(y))
    option_sets = tuple(negative_square_residues(p) for p in primes)
    for phases in product(*option_sets):
        assignments = tuple(zip(primes, phases))
        data = verify_square_cover_phase(y, assignments)
        if data["covers_full_horizon"]:
            return {
                "y": y,
                "feasible": True,
                "witness": assignments,
            }
    return {
        "y": y,
        "feasible": False,
        "witness": None,
    }
