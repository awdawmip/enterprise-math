"""Exact certificate operators for the admitted native tri-sector coupled-closure theorem.

This module is a domain operator, not a new global tool family.  It exposes finite
prime-field certificates for the support mechanisms and for the exact
longitudinal/transverse closure admitted as
``NATIVE_TRISECTOR_COUPLED_CLOSURE_THEOREM``.

Hard boundaries:
- only ``s=3`` is current native Enterprise geometry; other odd ``s`` values are
  controlled comparator parameters;
- the returned ``9`` is breaker-coprime capacity, not an unrestricted prime-run
  theorem;
- ``105`` is exact arithmetic equality only;
- ``53`` is a local finite-window terminal odd factor, not a global breaker;
- split-hyperbola/Joukowski machinery is classical support, not a novelty claim.
"""

from __future__ import annotations

from typing import Any

from .legendre import is_prime


THEOREM_NODE = "NATIVE_TRISECTOR_COUPLED_CLOSURE_THEOREM"
THEOREM_CLASS = "AUDITED_RESEARCH_THEOREM / MODEL_SPECIFIC_SELECTION_THEOREM"


def _require_odd_prime(q: int) -> None:
    if q <= 2 or q % 2 == 0 or not is_prime(q):
        raise ValueError("q must be an odd prime")


def _legendre_symbol(value: int, q: int) -> int:
    value %= q
    if value == 0:
        return 0
    residue = pow(value, (q - 1) // 2, q)
    if residue == 1:
        return 1
    if residue == q - 1:
        return -1
    raise AssertionError("Euler criterion returned a non-Legendre residue")


def _largest_odd_prime_factor(value: int) -> int | None:
    value = abs(value)
    while value and value % 2 == 0:
        value //= 2
    if value <= 1:
        return None
    largest = 1
    divisor = 3
    while divisor * divisor <= value:
        while value % divisor == 0:
            largest = divisor
            value //= divisor
        divisor += 2
    if value > 1:
        largest = value
    return largest


def split_hyperbola_orbit_certificate(B: int, C: int, q: int) -> dict[str, Any]:
    """Return the exact prime-field sign-orbit certificate for ``B(y^2-x^2)=C``.

    The implementation uses the admitted linear split-hyperbola parametrization.
    ``q`` is intentionally restricted to an odd prime so the public certificate
    does not silently generalize the prime-field Legendre notation to arbitrary
    finite fields.
    """

    _require_odd_prime(q)
    Bq = B % q
    Cq = C % q
    if Bq == 0 or Cq == 0:
        raise ValueError("B and C must both be nonzero modulo q")

    inv_two = pow(2, -1, q)
    points: set[tuple[int, int]] = set()
    for a in range(1, q):
        b = Cq * pow(Bq * a % q, -1, q) % q
        x = (b - a) * inv_two % q
        y = (a + b) * inv_two % q
        points.add((x, y))

    unseen = set(points)
    orbits: list[tuple[tuple[int, int], ...]] = []
    while unseen:
        x, y = min(unseen)
        orbit = {
            (sx * x % q, sy * y % q)
            for sx in (1, -1)
            for sy in (1, -1)
        }
        orbit &= points
        frozen = tuple(sorted(orbit))
        orbits.append(frozen)
        unseen.difference_update(orbit)

    chi_bc = _legendre_symbol(Bq * Cq, q)
    chi_minus_bc = _legendre_symbol(-Bq * Cq, q)
    burnside_count = (q + 1 + chi_bc + chi_minus_bc) // 4
    if len(points) != q - 1:
        raise AssertionError("split-hyperbola point count disagreed with q-1")
    if len(orbits) != burnside_count:
        raise AssertionError("enumerated sign orbits disagreed with Burnside formula")

    return {
        "operator": "split_hyperbola_orbit_certificate",
        "field": f"F_{q}",
        "B_mod_q": Bq,
        "C_mod_q": Cq,
        "point_count": len(points),
        "expected_point_count": q - 1,
        "orbit_count": len(orbits),
        "burnside_orbit_count": burnside_count,
        "orbit_sizes": sorted(len(orbit) for orbit in orbits),
        "legendre_BC": chi_bc,
        "legendre_minus_BC": chi_minus_bc,
        "one_orbit": len(orbits) == 1,
        "breaker_capacity_implication_q_le_5": len(orbits) != 1 or q <= 5,
        "support_status": "KNOWN_IMMEDIATE_COROLLARY",
        "hard_boundary": (
            "One sign orbit is a support-level breaker certificate only after the "
            "declared dual-value/breaker semantics are supplied; this operator does "
            "not invent those semantics."
        ),
    }


def odd_sector_lane_certificate(s: int, q: int) -> dict[str, Any]:
    """Return the exact centered-lane Joukowski image/saturation certificate.

    The controlled family requires odd ``s>=3``.  Only ``s=3`` has current native
    Enterprise geometry; all other accepted inputs are comparator parameters.
    """

    if s < 3 or s % 2 == 0:
        raise ValueError("s must be an odd integer >= 3")
    _require_odd_prime(q)
    if (2 * s) % q == 0:
        raise ValueError("q must not divide 2s for the admitted Joukowski quotient")

    c = pow((2 * s) % q, -1, q)
    fibers: dict[int, list[int]] = {}
    for a in range(1, q):
        lane = (-s * a - pow(2 * a % q, -1, q)) % q
        fibers.setdefault(lane, []).append(a)

    image = set(fibers)
    half = (s - 1) // 2
    target = {lane % q for lane in range(-half, half + 1)}
    legendre_c = _legendre_symbol(c, q)
    image_size_formula = (q + legendre_c) // 2
    if len(image) != image_size_formula:
        raise AssertionError("enumerated Joukowski image disagreed with orbit formula")

    if q == 2 * s - 1:
        extremal_kind = "LOWER"
    elif q == 2 * s + 1:
        extremal_kind = "UPPER"
    else:
        extremal_kind = None

    saturated = image <= target
    if extremal_kind == "LOWER" and saturated:
        admitted_uniqueness_consistent = (s, q) == (3, 5)
    elif extremal_kind == "UPPER" and saturated:
        admitted_uniqueness_consistent = (s, q) == (3, 7)
    else:
        admitted_uniqueness_consistent = True

    return {
        "operator": "odd_sector_lane_certificate",
        "s": s,
        "native_geometry": s == 3,
        "q": q,
        "c_mod_q": c,
        "legendre_c": legendre_c,
        "image": sorted(image),
        "image_size": len(image),
        "image_size_formula": image_size_formula,
        "target_centered_lanes_mod_q": sorted(target),
        "target_size": len(target),
        "fiber_sizes": sorted(len(values) for values in fibers.values()),
        "saturated": saturated,
        "image_equals_target": image == target,
        "extremal_kind": extremal_kind,
        "admitted_extremal_uniqueness_consistent": admitted_uniqueness_consistent,
        "theorem_status": (
            "NO_DIRECT_MATCH_FOUND for extremal centered-lane uniqueness; "
            "Joukowski quotient/image-size layer is KNOWN_IMMEDIATE_COROLLARY"
        ),
        "hard_boundary": (
            "For s!=3 this is a controlled comparator calculation, not a canonical "
            "higher-sector Enterprise geometry."
        ),
    }


def coupled_closure_certificate(s: int, q_b: int) -> dict[str, Any]:
    """Check the exact longitudinal/transverse boundary-closure equations.

    ``q_b`` is treated as the caller-declared odd universal breaker.  The operator
    verifies the theorem's arithmetic consequences but does not infer breaker
    semantics from primality alone.
    """

    if s < 3 or s % 2 == 0:
        raise ValueError("s must be an odd integer >= 3")
    _require_odd_prime(q_b)

    k_star = 2 * q_b - 1
    q_minus = 2 * s - 1
    q_plus = 2 * s + 1
    lower_match = k_star - 4 == q_minus
    upper_match = k_star - 2 == q_plus
    closure_matched = lower_match and upper_match
    within_breaker_bound = q_b <= 5
    admitted_unique = closure_matched and within_breaker_bound
    if admitted_unique and (s, q_b, k_star) != (3, 5, 9):
        raise AssertionError("admitted q_b<=5 uniqueness was violated")

    mixed_product = (k_star - 4) * (k_star - 2)
    scaled_product = s * mixed_product
    local_obstruction = scaled_product + 1
    terminal_odd_factor = _largest_odd_prime_factor(local_obstruction)
    native_closure = (s, q_b, k_star) == (3, 5, 9) and closure_matched

    typed_chain = None
    if native_closure:
        typed_chain = {
            "3": "native sector count / curvature coefficient",
            "5": "odd universal-breaker terminal channel in the admitted native phase",
            "7": "upper extremal transverse saturation boundary, not a longitudinal breaker",
            "9": "breaker-coprime capacity, not an unrestricted prime-run theorem",
            "35": "M_9=(9-4)(9-2)",
            "105": "exact equality 3*35; no automatic shared genealogy",
            "53": "terminal odd factor of local obstruction 106, not a global breaker",
        }

    return {
        "operator": "coupled_closure_certificate",
        "theorem_node": THEOREM_NODE,
        "theorem_class": THEOREM_CLASS,
        "s": s,
        "native_geometry": s == 3,
        "declared_breaker_q_b": q_b,
        "within_admitted_breaker_bound_q_b_le_5": within_breaker_bound,
        "k_star": k_star,
        "transverse_lower": q_minus,
        "transverse_upper": q_plus,
        "lower_boundary_match": lower_match,
        "upper_boundary_match": upper_match,
        "closure_matched": closure_matched,
        "admitted_unique_solution": admitted_unique,
        "native_admitted_closure": native_closure,
        "M_k": mixed_product,
        "s_times_M_k": scaled_product,
        "local_obstruction": local_obstruction,
        "terminal_odd_prime_factor": terminal_odd_factor,
        "typed_native_chain": typed_chain,
        "hard_boundaries": [
            "q_b must already carry the caller's universal-breaker semantics.",
            "k_star is breaker-coprime capacity, not an unrestricted prime-run length.",
            "53, when present in the native certificate, is local finite-window data.",
            "Foundation status is not inferred by this operator.",
        ],
    }


def native_trisector_coupled_certificate() -> dict[str, Any]:
    """Return one complete exact certificate for the admitted native ``s=3`` node."""

    lower = odd_sector_lane_certificate(3, 5)
    upper = odd_sector_lane_certificate(3, 7)
    closure = coupled_closure_certificate(3, 5)
    q5_orbit = split_hyperbola_orbit_certificate(3, 1, 5)
    q7_control = split_hyperbola_orbit_certificate(3, 1, 7)

    if not lower["saturated"] or not upper["saturated"]:
        raise AssertionError("native extremal lane saturations failed")
    if not closure["native_admitted_closure"]:
        raise AssertionError("native coupled closure failed")
    if not q5_orbit["one_orbit"] or q7_control["one_orbit"]:
        raise AssertionError("native q=5 breaker / q=7 control split failed")

    return {
        "operator": "native_trisector_coupled_certificate",
        "theorem_node": THEOREM_NODE,
        "theorem_status": "AUDITED_RESEARCH_THEOREM / DRIVER_ADMITTED",
        "foundation_status": "REVIEW_COMPLETED_NOT_ADMITTED",
        "lower_extremal": lower,
        "upper_extremal": upper,
        "closure": closure,
        "q5_sign_orbit_support": q5_orbit,
        "q7_nonbreaker_control": q7_control,
        "exact_chain": [3, [5, 7], 9, 35, 105, 53],
        "external_literature_boundary": (
            "NO DIRECT THEOREM-STATEMENT MATCH FOUND IN THE AUDITED LITERATURE SET"
        ),
        "novelty_claim": False,
    }


__all__ = [
    "THEOREM_NODE",
    "THEOREM_CLASS",
    "split_hyperbola_orbit_certificate",
    "odd_sector_lane_certificate",
    "coupled_closure_certificate",
    "native_trisector_coupled_certificate",
]
