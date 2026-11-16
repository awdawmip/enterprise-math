"""Independent exact integer test of an inverse-orbit positive BRC mass carrier.

Scoped finite test: U(7), multiplier 3, six named residue states and 16
nonnegative direction-weight pairs. No P000 native spatial step semantics.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from math import gcd


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def orbit(u: int, modulus: int) -> tuple[int, int]:
    return tuple(sorted((u, pow(u, -1, modulus))))


def row(u: int, modulus: int, multiplier: int, positive_weight: int, negative_weight: int):
    inverse_multiplier = pow(multiplier, -1, modulus)
    destinations = ((u, 2), (u * multiplier % modulus, positive_weight),
                    (u * inverse_multiplier % modulus, negative_weight))
    counts = defaultdict(int)
    for v, weight in destinations:
        require(weight >= 0, "mass must remain nonnegative")
        counts[orbit(v, modulus)] += weight
    return dict(sorted(counts.items()))


def main():
    modulus, multiplier = 7, 3
    units = tuple(u for u in range(1, modulus) if gcd(u, modulus) == 1)
    classes = tuple(sorted({orbit(u, modulus) for u in units}))
    require(classes == ((1, 1), (2, 4), (3, 5), (6, 6)), "orbit census")
    all_pairs = 0
    safe_pairs = 0
    source_pairs_checked = 0
    delta_checks = 0
    unsafe_example = None
    for wp in range(4):
        for wm in range(4):
            all_pairs += 1
            safe = True
            for u in units:
                inverse_u = pow(u, -1, modulus)
                left = row(u, modulus, multiplier, wp, wm)
                right = row(inverse_u, modulus, multiplier, wp, wm)
                require(sum(left.values()) == 2 + wp + wm, "positive mass conservation")
                require(sum(right.values()) == 2 + wp + wm, "inverse source mass conservation")
                source_pairs_checked += 1
                for target in classes:
                    lhs = left.get(target, 0) - right.get(target, 0)
                    plus = orbit(u * multiplier % modulus, modulus)
                    minus = orbit(u * pow(multiplier, -1, modulus) % modulus, modulus)
                    rhs = (wp - wm) * (int(target == plus) - int(target == minus))
                    require(lhs == rhs, "inverse-orbit exact row-difference formula")
                    delta_checks += 1
                if left != right:
                    safe = False
                    if unsafe_example is None:
                        unsafe_example = {"positive_weight": wp, "negative_weight": wm,
                                          "source_u": u, "inverse_u": inverse_u,
                                          "row_u": {str(k): v for k,v in left.items()},
                                          "row_inverse_u": {str(k): v for k,v in right.items()}}
            require(safe == (wp == wm), "sharp U(7), g=3 safe-weight criterion")
            if safe:
                safe_pairs += 1
    require(all_pairs == 16 and safe_pairs == 4, "weight census")
    u, inverse_u = 3, 5
    symmetric = {str(x): {str(k):v for k,v in row(x, modulus, multiplier, 1, 1).items()}
                 for x in (u,inverse_u)}
    asymmetric = {str(x): {str(k):v for k,v in row(x, modulus, multiplier, 2, 1).items()}
                  for x in (u,inverse_u)}
    require(symmetric[str(u)] == symmetric[str(inverse_u)], "symmetric 3/5 fiber")
    require(asymmetric[str(u)] != asymmetric[str(inverse_u)], "asymmetric 3/5 fiber")
    result = {
        "schema": "EM_X6_UNIT75_SCOPED_INTEGER_CERTIFICATE_V1",
        "modulus": modulus, "multiplier": multiplier,
        "source_domain": "U(7), finite inversion orbits; nonspatial BRC mass",
        "classes": [list(v) for v in classes],
        "weight_pairs_checked": all_pairs, "safe_weight_pairs": safe_pairs,
        "unsafe_weight_pairs": all_pairs - safe_pairs,
        "source_pair_comparisons": source_pairs_checked,
        "target_class_delta_checks": delta_checks,
        "symmetric_3_5": symmetric, "asymmetric_3_5": asymmetric,
        "first_unsafe_example": unsafe_example,
        "result": "PASS",
        "scope": "Exact finite exhaustive 16 weight pairs (0..3)^2 and all 6 source units; mathematical general equivalence is separately proved in report"
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
