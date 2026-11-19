"""Exact CRT root minima for Table 6 and its even exponent translations.

Run: python research_notes/portable_direct/riesel_mixed_20261119/minimize.py

The search uses only certificate.json's original rows. The supplied original
root and optimized certificate are compared after the search, not assumed by
it. Primality, exact orders, and the mixed Riesel certificate are checked by
the companion verifier. This file computes static CRT minima with integers;
it does not introduce another dynamical propagator.

For a fixed left subset sum u, the first right sum at or cyclically after
(-base-u) mod R gives the least (base+u+v) mod R. Taking this minimum over
every left sum examines all sign choices exactly. All even translations are
examined; Gray-code enumeration independently checks the original and the
winning translation. No minimum over other covering shapes is claimed.
"""
from __future__ import annotations

import argparse
from bisect import bisect_left
import json
from math import lcm, prod
from pathlib import Path


def crt_parameters(roots: list[int], basis: list[int], product: int,
                   modulus: int) -> tuple[int, list[int]]:
    base = (product + sum(c * e for c, e in zip(roots, basis))) % modulus
    deltas = [(-2 * c * e) % modulus for c, e in zip(roots, basis)]
    return base, deltas


def gray_minimum(base: int, deltas: list[int], modulus: int) -> tuple[int, int]:
    """Visit every subset once in binary-reflected Gray-code order."""
    best, best_mask, current = base, 0, base
    for j in range(1, 1 << len(deltas)):
        mask = j ^ (j >> 1)
        changed = (j & -j).bit_length() - 1
        delta = deltas[changed] if (mask >> changed) & 1 else -deltas[changed]
        current = (current + delta) % modulus
        if current < best:
            best, best_mask = current, mask
    return best, best_mask


def subset_sums(deltas: list[int], modulus: int) -> list[tuple[int, int]]:
    sums = [(0, 0)]
    for i, delta in enumerate(deltas):
        sums += [((s + delta) % modulus, mask | (1 << i)) for s, mask in sums]
    return sums


def mitm_minimum(base: int, deltas: list[int], modulus: int) -> tuple[int, int]:
    """Exact minimum over all subsets using two complete half-subset lists."""
    half = len(deltas) // 2
    left = subset_sums(deltas[:half], modulus)
    right = sorted(subset_sums(deltas[half:], modulus))
    right_values = [value for value, _ in right]
    best, best_mask = modulus, 0
    for u, mask in left:
        target = (-base - u) % modulus
        index = bisect_left(right_values, target) % len(right_values)
        v, right_mask = right[index]
        candidate = (base + u + v) % modulus
        if candidate < best:
            best, best_mask = candidate, mask | (right_mask << half)
    return best, best_mask


def certificate_rows(rows: list[dict], roots: list[int], exponent_shift: int,
                     mask: int, minimum: int) -> list[dict]:
    result = []
    for i, (row, root) in enumerate(zip(rows, roots)):
        p = row["p"]
        sign = -1 if (mask >> i) & 1 else 1
        residue = sign * root % p
        phase = (row["exponent_phase"] + exponent_shift) % row["order"]
        assert minimum % p == residue
        assert residue * residue * pow(2, phase, p) % p == 1
        result.append({"p": p, "order": row["order"], "exponent_phase": phase,
                       "a_residue": residue, "root_sign": sign})
    return result


def minimize(data: dict) -> dict:
    original = data["original"]
    rows = original["rows"]
    primes = [row["p"] for row in rows]
    product = prod(primes)
    modulus = 2 * product
    period = lcm(*(row["order"] for row in rows))
    assert period % 2 == 0
    basis = [(modulus // p) * pow(modulus // p, -1, p) % modulus for p in primes]
    inverse_two = [pow(2, -1, p) for p in primes]
    roots = [row["a_residue"] for row in rows]
    base, deltas = crt_parameters(roots, basis, product, modulus)
    original_mitm = mitm_minimum(base, deltas, modulus)
    original_gray = gray_minimum(base, deltas, modulus)
    assert original_mitm == original_gray
    fixed_minimum, fixed_mask = original_mitm
    fixed_rows = certificate_rows(rows, roots, 0, fixed_mask, fixed_minimum)

    best = modulus
    minima = []
    for t in range(period // 2):
        base, deltas = crt_parameters(roots, basis, product, modulus)
        value, mask = original_mitm if t == 0 else mitm_minimum(base, deltas, modulus)
        minima.append([2 * t, str(value), mask])
        if value < best:
            best, best_t, best_mask = value, t, mask
            best_roots, best_base, best_deltas = list(roots), base, deltas
        roots = [c * inverse % p for c, inverse, p in zip(roots, inverse_two, primes)]

    assert gray_minimum(best_base, best_deltas, modulus) == (best, best_mask)
    winning_rows = certificate_rows(rows, best_roots, 2 * best_t, best_mask, best)
    assert best > 0 and best % 2 == 1
    assert 2 * best * best - 1 > max(primes)

    # These comparisons occur only after the entire search has finished.
    optimized = data["optimized"]
    actual_rows = [{k: v for k, v in row.items() if k != "root_sign"} for row in winning_rows]
    optimized_match = (best == int(optimized["a"])
                       and 2 * best_t == optimized["exponent_shift"]
                       and actual_rows == optimized["rows"])
    assert optimized_match
    return {
        "schema": "RIESEL_MIXED_CRT_MINIMA_V1",
        "researcher_id": data["researcher_id"],
        "research_activity_id": data["research_activity_id"],
        "exact_scope": "Minimum positive odd root over the independent signs of the original Table 6 roots and all even global translations of its exponent phases. Not all 20-prime phase assignments, all covers, or all square Riesel numbers.",
        "arithmetic": "Exact Python integers; no floating-point search or random sampling.",
        "source_url": original["source_url"],
        "period": period,
        "prime_product": str(product),
        "odd_crt_modulus": str(modulus),
        "counts": {
            "primes": len(rows),
            "signs_per_translation": 1 << len(rows),
            "even_translation_classes": period // 2,
            "distinct_odd_root_classes": (period // 2) * (1 << len(rows)),
        },
        "fixed_original_phases": {
            "minimum_positive_odd_root": str(fixed_minimum),
            "minimum_square_k": str(fixed_minimum * fixed_minimum),
            "sign_bitmask": fixed_mask,
            "gray_enumeration_agrees_with_mitm": True,
            "supplied_original_root": original["a"],
            "minimum_equals_supplied_original_root": fixed_minimum == int(original["a"]),
            "rows": fixed_rows,
        },
        "minimum": {
            "positive_odd_root": str(best),
            "square_k": str(best * best),
            "half_shift": best_t,
            "exponent_shift": 2 * best_t,
            "sign_bitmask": best_mask,
            "gray_enumeration_agrees_with_mitm": True,
            "matches_supplied_optimized_certificate": optimized_match,
            "root_decimal_digits": len(str(best)),
            "square_decimal_digits": len(str(best * best)),
            "N1_true_factor_lower_bound": str(2 * best * best - 1),
            "maximum_fixed_prime": max(primes),
            "rows": winning_rows,
        },
        "method": "For each left subset sum, the cyclic successor to (-base-left) modulo R in sorted right sums attains its least residue. Compare all left sums and all even translations. Exhaustive Gray-code checks independently confirm the fixed original and winning minima.",
        "per_shift_columns": ["exponent_shift", "minimum_positive_odd_root", "sign_bitmask"],
        "per_shift_minima": minima,
    }


def main() -> None:
    directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=directory / "certificate.json")
    parser.add_argument("--output", type=Path, default=directory / "minima.json")
    args = parser.parse_args()
    result = minimize(json.loads(args.input.read_text()))
    # Keep each of the 3360 exhaustive per-shift records on one compact line.
    minima = result.pop("per_shift_minima")
    header = json.dumps(result, ensure_ascii=False, indent=2)
    body = ",\n".join("    " + json.dumps(row, separators=(",", ":")) for row in minima)
    args.output.write_text(header[:-2] + ',\n  "per_shift_minima": [\n' + body + "\n  ]\n}\n")
    print(json.dumps({"output": str(args.output), "counts": result["counts"],
                      "fixed_original_minimum": result["fixed_original_phases"]["minimum_positive_odd_root"],
                      "minimum": {k: v for k, v in result["minimum"].items() if k != "rows"}},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
