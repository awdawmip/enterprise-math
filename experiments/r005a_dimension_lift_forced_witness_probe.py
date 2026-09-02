#!/usr/bin/env python3
"""Exact probe for the R005 dimension-lift forced-witness theorem.

If p = m*r with r >= 2 and q is prime in the m-power basin
    k^m < q < (k+1)^m,
then
    k^(m*r) < q^r < (k+1)^(m*r).
The composite q^r has exactly one prime divisor q, so q is an exclusive
divisor-witness collision in the p-power basin and must lie in its forced core.

This script checks the transport against the exact forced cores computed by
r005a_basin_witness_core_probe.py inside the same explicit bound.
"""

from __future__ import annotations

import importlib.util
import json
from functools import lru_cache
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_CORE_PATH = _HERE / "r005a_basin_witness_core_probe.py"
_spec = importlib.util.spec_from_file_location("r005a_basin_witness_core_probe", _CORE_PATH)
if _spec is None or _spec.loader is None:
    raise RuntimeError(f"cannot load {_CORE_PATH}")
core = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(core)

MAX_POWER = 8


@lru_cache(maxsize=None)
def basin_record(power: int, k: int) -> dict:
    return core.basin_record(power, k)


def primes_in_basin(power: int, k: int) -> tuple[int, ...]:
    lo = k ** power
    hi = (k + 1) ** power
    return tuple(q for q in range(lo + 1, hi) if core.is_prime(q))


def check_pair(m: int, r: int) -> dict:
    p = m * r
    if r < 2 or p > MAX_POWER:
        raise ValueError("invalid lift pair")

    checked_basins = 0
    lifted_prime_count = 0
    first_nonempty = None

    k = 2
    while (k + 1) ** p - 1 <= core.MAX_U:
        high = basin_record(p, k)
        forced = set(high["forced_core"])
        lower_primes = primes_in_basin(m, k)

        for q in lower_primes:
            n = q ** r
            assert k ** p < n < (k + 1) ** p
            assert n <= core.MAX_U
            assert core.factorization(n) == ((q, r),)
            assert q <= high["horizon"]
            assert q in forced

        if lower_primes and first_nonempty is None:
            first_nonempty = {
                "k": k,
                "lower_primes": lower_primes,
                "lifted_collisions": tuple((q, q ** r) for q in lower_primes),
            }

        checked_basins += 1
        lifted_prime_count += len(lower_primes)
        k += 1

    return {
        "m": m,
        "r": r,
        "p": p,
        "checked_high_basins": checked_basins,
        "lifted_prime_instances": lifted_prime_count,
        "first_nonempty_example": first_nonempty,
    }


def main() -> dict:
    rows = []
    for p in range(2, MAX_POWER + 1):
        for r in range(2, p + 1):
            if p % r == 0:
                m = p // r
                rows.append(check_pair(m, r))

    p2 = next(row for row in rows if row["p"] == 2)
    assert p2["lifted_prime_instances"] == 0

    p4 = next(row for row in rows if row["m"] == 2 and row["r"] == 2)
    assert p4["lifted_prime_instances"] > 0

    p6_from3 = next(row for row in rows if row["m"] == 3 and row["r"] == 2)
    assert p6_from3["lifted_prime_instances"] > 0

    saturation = {}
    for p in range(2, MAX_POWER + 1):
        k = 2
        first_nonfull = None
        all_full = True
        checked = 0
        while (k + 1) ** p - 1 <= core.MAX_U:
            record = basin_record(p, k)
            missing = tuple(sorted(set(record["witnesses"]) - set(record["forced_core"])))
            if missing:
                all_full = False
                if first_nonfull is None:
                    first_nonfull = {
                        "k": k,
                        "missing_witnesses": missing,
                    }
            checked += 1
            k += 1
        saturation[str(p)] = {
            "checked_basins": checked,
            "all_candidate_witnesses_forced": all_full,
            "first_nonfull": first_nonfull,
        }

    assert saturation["2"]["first_nonfull"]["k"] == 6
    assert saturation["3"]["first_nonfull"] == {
        "k": 23,
        "missing_witnesses": (109,),
    }
    assert all(saturation[str(p)]["all_candidate_witnesses_forced"] for p in range(4, 9))

    return {
        "status": "EXACT_BOUNDED_DIMENSION_LIFT_CHECK / GENERIC_THEOREM_IS_ELEMENTARY",
        "max_upper_endpoint": core.MAX_U,
        "transport_rows": rows,
        "forcing_saturation_scan": saturation,
        "interpretation": {
            "pure_power_lift": "Prime_m(k) injects into ForcedCore_(m*r)(k) via q -> q^r",
            "cardinality_bound": "|ForcedCore_(m*r,k)| >= P_m(k)",
            "square_case": "m=1 source basin is empty, so p=2 receives no nontrivial pure-power lift from a lower positive integer exponent",
            "boundary": "forced cores may contain additional witnesses arising from non-pure exclusive collisions; the lift is an injection, not an equality",
        },
    }


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2))
