#!/usr/bin/env python3
"""R005-A external finite prime-gap transfer certificate.

External premise (Oliveira e Silva project data):
- all consecutive prime gaps below 4e18 were computed;
- results were double-checked through X = 4e17;
- the largest gap whose first occurrence lies below 4e17 is 1328.

This executable does NOT re-prove that external computation.  It verifies the
R005 arithmetic consequence of that premise.

Together with the Axler n=3 tail:
  x < prime <= x * (1 + c/log^3 x), c=0.0486680000822,
the external finite gap bound covers the lower cofactor band while Axler covers
the upper cofactor tail.

For p=3 and p=4, if all danger cofactor points x=A/q below xcrit lie inside the
double-checked prime-gap region, and the absolute gap bound G is smaller than
the basin-relative allowance u*x, then every danger witness is forced.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
import json

getcontext().prec = 80

AXLER_C = Decimal("0.0486680000822")
EXTERNAL_GAP_LIMIT = 400_000_000_000_000_000
EXTERNAL_MAX_GAP = 1328
START_AFTER_INTERNAL = {3: 500_001, 4: 2_102_192}


def basin_u(p: int, k: int) -> Decimal:
    K = Decimal(k)
    A = K**p
    U = Decimal((k + 1) ** p - 1)
    return U / A - 1


def L(p: int, k: int) -> Decimal:
    K = Decimal(k)
    U = Decimal((k + 1) ** p - 1)
    return Decimal(2).sqrt() * (K**p) / U.sqrt()


def xcrit(p: int, k: int) -> Decimal:
    u = basin_u(p, k)
    cube_root = ((AXLER_C / u).ln() / Decimal(3)).exp()
    return cube_root.exp()


def largest_k_with_xcrit_below(p: int, lo: int, hi: int, cap: Decimal) -> int:
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if xcrit(p, mid) + Decimal(EXTERNAL_MAX_GAP) <= cap:
            lo = mid
        else:
            hi = mid - 1
    return lo


def relative_gap_margin(p: int, k: int) -> Decimal:
    """Conservative margin u(k)*(L(k)-G)-G."""
    u = basin_u(p, k)
    return u * (L(p, k) - Decimal(EXTERNAL_MAX_GAP)) - Decimal(EXTERNAL_MAX_GAP)


def certify_power(p: int, search_hi: int) -> dict:
    start = START_AFTER_INTERNAL[p]
    end = largest_k_with_xcrit_below(
        p, start, search_hi, Decimal(EXTERNAL_GAP_LIMIT)
    )

    assert xcrit(p, end) + Decimal(EXTERNAL_MAX_GAP) <= Decimal(EXTERNAL_GAP_LIMIT)
    assert xcrit(p, end + 1) + Decimal(EXTERNAL_MAX_GAP) > Decimal(EXTERNAL_GAP_LIMIT)

    start_margin = relative_gap_margin(p, start)
    end_margin = relative_gap_margin(p, end)
    assert start_margin > 0
    assert end_margin >= start_margin

    return {
        "p": p,
        "external_transfer_start_k": start,
        "external_transfer_end_k": end,
        "xcrit_end": str(xcrit(p, end)),
        "xcrit_next": str(xcrit(p, end + 1)),
        "external_gap_limit": EXTERNAL_GAP_LIMIT,
        "external_max_gap_premise": EXTERNAL_MAX_GAP,
        "relative_gap_margin_start": str(start_margin),
        "relative_gap_margin_end": str(end_margin),
        "conclusion": (
            f"Assuming the stated external double-checked gap premise, "
            f"every p={p} danger witness is forced for every integer "
            f"{start}<=k<={end}."
        ),
    }


def main() -> None:
    p3 = certify_power(3, 6_000_000)
    p4 = certify_power(4, 8_000_000)

    assert p3["external_transfer_end_k"] == 4_104_076
    assert p4["external_transfer_end_k"] == 5_472_101

    result = {
        "status": (
            "R005-A EXTERNAL DOUBLE-CHECKED PRIME-GAP TRANSFER / "
            "ARITHMETIC CONSEQUENCE VERIFIED / EXTERNAL COMPUTATION PREMISE"
        ),
        "external_premise": {
            "double_checked_through": EXTERNAL_GAP_LIMIT,
            "max_gap_used": EXTERNAL_MAX_GAP,
            "source_status": (
                "author/project computational record; this file verifies only "
                "the downstream R005 inequalities"
            ),
        },
        "p3": p3,
        "p4": p4,
        "combined_ranges": {
            "p3_unique_least_basis_through_k": 4_104_076,
            "p4_unique_least_basis_through_k_from_gap_transfer": 5_472_101,
        },
        "boundary": (
            "The next k is not a counterexample. It is merely the first k for "
            "which the Axler-uncertified crossover extends beyond the chosen "
            "4e17 double-checked external gap region."
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
