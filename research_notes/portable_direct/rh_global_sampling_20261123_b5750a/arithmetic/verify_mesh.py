"""Exact finite checks of the globally allocated integer mesh.

Only block geometry and the smooth Green error are checked here. No road values
or prime asymptotics are inferred from these finite examples.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
import json


def floor_root(n, degree):
    lo, hi = 0, 1 << ((n.bit_length() + degree - 1) // degree)
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if m**degree <= n:
            lo = m
        else:
            hi = m
    return hi if hi**degree <= n else lo


def decimal(x):
    with localcontext() as context:
        context.prec = 35
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def check(A, B, r):
    assert 4 <= A < B and 0 < r <= 1 and B * r**40 >= 1
    X = A
    cells, smooth, blocks = 0, Fraction(0), []
    while X < B:
        Y, b = min(2 * X, B), min(2 * X, B) - X
        numerator = r.numerator**20 * X**16
        denominator = r.denominator**20 * B
        floor_H = floor_root(numerator // denominator, 20)
        assert denominator * floor_H**20 <= numerator
        assert denominator * (floor_H + 1)**20 > numerator
        step = max(1, floor_H)
        full, tail = divmod(b, step)
        count = full + bool(tail)
        assert 2**20 * denominator * step**20 >= numerator
        if step >= 2:
            assert denominator * step**20 <= numerator
        mass = Fraction(full * (step**5 - step) + tail**5 - tail, 120 * X**4)
        if step == 1:
            assert mass == 0
        cells += count
        smooth += mass
        blocks.append({"X": X, "Y": Y, "floor_H": floor_H,
                       "step": step, "full_cells": full, "tail_length": tail,
                       "cells": count, "smooth_cost": str(mass)})
        X = Y
    # G_(1/5)<8, because (8/7)^5<2. This rational slack avoids
    # using floating roots in the mathematical checks.
    assert 8**5 < 2 * 7**5
    assert smooth <= r**4 / 15
    excess = max(0, cells - len(blocks))
    assert (excess * r)**4 <= 16**4 * B
    return {"A": A, "B": B, "r": str(r), "blocks": len(blocks),
            "samples": cells + 1,
            "fully_sampled_blocks": sum(b["step"] == 1 for b in blocks),
            "smooth_cost_exact": str(smooth), "smooth_cost_decimal": decimal(smooth),
            "smooth_over_r4": decimal(smooth / r**4),
            "rational_upper_smooth": str(r**4 / 15),
            "all_exact_checks_passed": True, "block_details": blocks}


examples = [(4, 1027, Fraction(1)), (1024, 32768, Fraction(1)),
            (2**10, 2**20, Fraction(1)),
            (2**10, 2**80, Fraction(1, 2)),
            (2**10, 2**320, Fraction(1, 8))]
records = [check(*e) for e in examples]
result = {"scope": "Exact grid construction, finite smooth-source bounds, node-count bound and integer saturation",
          "no_full_road_or_prime_values_read": True,
          "examples": records}
path = Path(__file__).with_name("mesh_checks.json")
path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
for r in records:
    print({k: v for k, v in r.items() if k != "block_details"})
