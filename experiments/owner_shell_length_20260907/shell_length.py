"""Typed Meng--Sun Lemma 2.4 consumer for the signed X6 quadratic shell.

The all-N theorem is proved in OWNER_SHELL_LENGTH_FRONTIER_20260907.md.
This helper constructs and verifies individual exact endpoints, with explicit
budgets; exhaustion never means that an endpoint does not exist.
"""
from __future__ import annotations

import argparse
import hashlib
from itertools import combinations
import json
from math import isqrt
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
NATIVE = ROOT / "experiments/x6_signed_native_spatial_v16_20260905"
sys.path.insert(0, str(NATIVE))
import signed_brc
import x6_signed


class ResourceLimit(RuntimeError):
    """A finite implementation budget, never a mathematical infeasibility result."""


def _natural(value, name):
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be an exact nonnegative integer")
    return value


def upper_length(N):
    """Largest k with k*k <= 6*N and k == N mod 2, using integer arithmetic."""
    _natural(N, "N")
    k = isqrt(6 * N)
    return k - ((k - N) % 2)


def reduction_parameters(N):
    _natural(N, "N")
    k = upper_length(N)
    b, r = divmod(k, 6)
    base = 6 * b * b + 2 * b * r + r
    if (N - base) % 2:
        raise ArithmeticError("parity reduction failed")
    t = (N - base) // 2
    if not 0 <= t <= 2 * b + (r == 5):
        raise ArithmeticError("proved remainder range failed")
    result = {"N": N, "k": k, "auxiliary_center_b": b, "r": r, "t": t}
    if r == 0 and t == 0:
        return {**result, "case": "BALANCED", "magnitudes": (b,) * 6}
    offsets = {0: (0, 1), 1: (0, 0), 2: (0, 1),
               3: (0, 0), 4: (0, 1), 5: (1, 1)}
    da, dc = offsets[r]
    p, q = b + da, b + dc
    B = k - p - q
    A = N - p * p - q * q
    D = 4 * A - B * B
    if not (p >= 0 and q >= 0 and A > 0 and B > 0 and A % 2 == B % 2 == 1):
        raise ArithmeticError("Meng--Sun odd positive input contract failed")
    if not (D > 0 and D % 8 == 3 and 3 * A < B * B + 2 * B + 4):
        raise ArithmeticError("Meng--Sun strict inequalities failed")
    return {**result, "case": "MENG_SUN_LEMMA_2_4_ODD_BRANCH",
            "fixed_last_two": (p, q), "A": A, "B": B, "D": D,
            "nonnegativity_margin": (B + 4) ** 2 - 3 * D}


def _three_odd_squares(D, budget):
    """Complete finite search for sorted positive odd x<=y<=z, not shell scan.

    D == 3 mod 8 guarantees existence by the three-square theorem.  Every
    representation is odd, and sorting loses no possibilities.
    """
    _natural(budget, "search_budget")
    checked = 0
    for x in range(1, isqrt(D // 3) + 1, 2):
        remaining = D - x * x
        for y in range(x, isqrt(remaining // 2) + 1, 2):
            if checked >= budget:
                raise ResourceLimit(f"three-square candidate budget exhausted after {checked} candidates")
            checked += 1
            z2 = remaining - y * y
            z = isqrt(z2)
            if z >= y and z % 2 == 1 and z * z == z2:
                return (x, y, z), checked
    raise ArithmeticError("complete bounded search contradicted the three-square theorem contract")


def construct_endpoint(N, *, signs=(1,) * 6, search_budget=1_000_000):
    """Return one raw signed endpoint and the exact four-square construction."""
    _natural(search_budget, "search_budget")
    if type(signs) not in (tuple, list) or len(signs) != 6:
        raise ValueError("six explicit signs required")
    if any(type(s) is not int or s not in (-1, 1) for s in signs):
        raise ValueError("each sign must be exact +1 or -1")
    params = reduction_parameters(N)
    if params["case"] == "BALANCED":
        magnitudes = params["magnitudes"]
        detail = {"candidates_checked": 0}
    else:
        B, D = params["B"], params["D"]
        positive_triple, checked = _three_odd_squares(D, search_budget)
        # Each signed odd square root can be chosen congruent to B modulo 4.
        x, y, z = tuple(v if (v - B) % 4 == 0 else -v for v in positive_triple)
        numerators = (B + x + y + z, B + x - y - z,
                      B - x + y - z, B - x - y + z)
        if any(v % 4 for v in numerators):
            raise ArithmeticError("Hadamard divisibility failed")
        four = tuple(v // 4 for v in numerators)
        if min(four) < 0 or sum(four) != B or sum(v * v for v in four) != params["A"]:
            raise ArithmeticError("four-square output verification failed")
        magnitudes = four + params["fixed_last_two"]
        detail = {"three_odd_squares_positive": positive_triple,
                  "three_odd_squares_signed": (x, y, z),
                  "hadamard_first_four": four, "candidates_checked": checked}
    endpoint = tuple(s * a for s, a in zip(signs, magnitudes))
    verdict = verify_endpoint(N, endpoint)
    if not verdict["valid"]:
        raise ArithmeticError("native signed endpoint failed independent verification")
    return endpoint, {**params, **detail, "signs": tuple(signs), "magnitudes": magnitudes}


def verify_endpoint(N, endpoint):
    """Check this raw witness via original signed BRC; not an all-N proof checker."""
    try:
        _natural(N, "N")
        if type(endpoint) not in (tuple, list) or len(endpoint) != 6:
            raise ValueError("endpoint must be an explicit six-item tuple/list")
        z = tuple(endpoint)
        norm = signed_brc.spatial_norm_squared(z)
        length = signed_brc.shortest_event_count(z)
        k = upper_length(N)
        return {"valid": norm == N and length == k, "N": N,
                "actual_norm_squared": norm, "actual_shortest_length": length,
                "upper_length": k, "scope": "THIS_RAW_SIGNED_ENDPOINT_ONLY"}
    except (ValueError, TypeError) as exc:
        return {"valid": False, "reason": str(exc), "scope": "THIS_RAW_SIGNED_ENDPOINT_ONLY"}


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def certificate(N, *, signs=(1,) * 6, search_budget=1_000_000, brc_event_budget=4000):
    """Native readouts retain actual common depth and all twenty joint slices.

    The separate BRC budget avoids computing/printing arbitrarily huge factorial
    integers.  Skipping that readout does not invalidate an already checked endpoint.
    """
    _natural(brc_event_budget, "brc_event_budget")
    endpoint, construction = construct_endpoint(N, signs=signs, search_budget=search_budget)
    state = x6_signed.Spatial6(endpoint)
    residual, depth = state.relative_residual_depth()
    if x6_signed.from_residual_depth(residual, depth) != state:
        raise ArithmeticError("native residual/depth reconstruction failed")
    if 6 * depth * depth + 2 * depth * sum(residual) + sum(v * v for v in residual) != N:
        raise ArithmeticError("native norm/depth identity failed")
    slices = []
    for axes in combinations(range(6), 3):
        visible, common, hidden = x6_signed.hidden_slice_coordinates(state, axes)
        if x6_signed.from_hidden_slice_coordinates(axes, visible, common, hidden) != state:
            raise ArithmeticError("joint native slice reconstruction failed")
        slices.append({"axes": axes, "can3": visible, "visible_common_offset": common,
                       "omitted_signed_coordinates": hidden})
    k = construction["k"]
    factorial_ratio = {"numerator_factorial": k,
                       "denominator_factorials": tuple(abs(v) for v in endpoint)}
    if k <= brc_event_budget:
        count = signed_brc.shortest_path_multiplicity(endpoint)
        if signed_brc.endpoint_multiplicity(k, endpoint) != count:
            raise ArithmeticError("native shortest/general endpoint BRC counts disagree")
        try:
            count_decimal = str(count)
        except ValueError as exc:
            # A caller may explicitly raise the event budget above the runtime's
            # integer-to-decimal limit. Keep the verified endpoint and exact
            # count expression; do not change the interpreter-wide limit.
            multiplicity = {"status": "RESOURCE_LIMIT", "reason": "DECIMAL_CONVERSION_LIMIT",
                            "detail": str(exc), "computed_count_bit_length": count.bit_length(),
                            "exact_factorial_ratio": factorial_ratio}
        else:
            multiplicity = {"status": "COMPUTED_EXACT", "count_decimal": count_decimal}
    else:
        multiplicity = {"status": "RESOURCE_LIMIT", "reason": "EVENT_BUDGET",
                        "event_budget": brc_event_budget, "exact_factorial_ratio": factorial_ratio}
    return {"schema": "owner_shell_length_endpoint_v1", "status": "ENDPOINT_VERIFIED",
            "N": N, "raw_signed_endpoint": endpoint, "origin_anchor": (0,) * 6,
            "construction": construction, "verification": verify_endpoint(N, endpoint),
            "native_common_depth": depth, "native_can6": residual,
            "native_signed_coordinate_sum": sum(endpoint),
            "native_shortest_length": k, "joint_twenty_slices": slices,
            "shortest_path_multiplicity": multiplicity,
            "coordinate_boundary": "auxiliary_center_b is not common-depth; signs on nonzero magnitudes distinguish raw Cells; changing a zero-coordinate sign does not; no P000 change",
            "provenance": {"helper_sha256": _sha(Path(__file__)),
                           "signed_brc_sha256": _sha(NATIVE / "signed_brc.py"),
                           "x6_signed_sha256": _sha(NATIVE / "x6_signed.py"),
                           "primary_source": "https://www.impan.pl/shop/en/publication/transaction/download/product/92360",
                           "primary_lemma": "Meng--Sun, Acta Arith. 180 (2017), Lemma 2.4, odd-input branch",
                           "global_knowledge_canonical": "4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563"}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", type=int)
    parser.add_argument("--signs", nargs=6, type=int, default=(1,) * 6)
    parser.add_argument("--search-budget", type=int, default=1_000_000)
    parser.add_argument("--brc-event-budget", type=int, default=4000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = certificate(args.N, signs=args.signs, search_budget=args.search_budget,
                              brc_event_budget=args.brc_event_budget)
    except ResourceLimit as exc:
        payload = {"schema": "owner_shell_length_endpoint_v1", "status": "RESOURCE_LIMIT",
                   "N": args.N, "reason": str(exc),
                   "scope": "NO_NONEXISTENCE_CONCLUSION; mathematical all-N construction theorem is separate"}
    encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8", newline="\n")
        print(json.dumps({"status": payload["status"], "output_sha256": _sha(args.output)}))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
