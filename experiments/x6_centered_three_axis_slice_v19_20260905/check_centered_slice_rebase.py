from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
X6_DIR = REPO_ROOT / "experiments" / "x6_signed_native_spatial_v16_20260905"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


x6 = load("x6_signed_centered_slice_reuse", X6_DIR / "x6_signed.py")
brc = load("signed_brc_centered_slice_reuse", X6_DIR / "signed_brc.py")
S = (0, 1, 2)


def embed3(x):
    z = [0] * 6
    for i, v in zip(S, x):
        z[i] = v
    return x6.Spatial6(tuple(z))


def can3(x):
    x = tuple(x)
    h = min(x)
    return tuple(v - h for v in x), h


def carrier_axial(x):
    a, b, c = x
    return (a - c, b - c)


def carrier_q2(x):
    a, b, c = x
    return a * a + b * b + c * c - a * b - b * c - c * a


def mult3(x):
    return brc.shortest_path_multiplicity(tuple(x) + (0, 0, 0))


origin = embed3((0, 0, 0))
for axis in range(3):
    p = [0, 0, 0]
    n = [0, 0, 0]
    p[axis] = 1
    n[axis] = -1
    assert x6.full_distance_squared(origin, embed3(p)) == 1
    assert x6.full_distance_squared(origin, embed3(n)) == 1

triples = list(itertools.product(range(-4, 5), repeat=3))
for x in triples:
    r, h = can3(x)
    assert tuple(v + h for v in r) == x
    assert carrier_axial(r) == carrier_axial(x)

pairs = list(itertools.product(range(-2, 3), repeat=3))
pair_checks = 0
for a in pairs:
    for b in pairs:
        d2 = x6.full_distance_squared(embed3(a), embed3(b))
        assert d2 == sum((bi - ai) ** 2 for ai, bi in zip(a, b))
        assert d2 == x6.full_distance_squared(embed3(b), embed3(a))
        ra, ha = can3(a)
        rb, hb = can3(b)
        dh = hb - ha
        assert d2 == sum((rb[i] - ra[i] + dh) ** 2 for i in range(3))
        pair_checks += 1

kernel_vals = list(itertools.product(range(-2, 3), repeat=3))
kernel_pair_checks = 0
for a in kernel_vals:
    for b in kernel_vals:
        same = carrier_axial(a) == carrier_axial(b)
        diagonal = len(set(bi - ai for ai, bi in zip(a, b))) == 1
        assert same == diagonal
        kernel_pair_checks += 1

assert carrier_q2((3, 4, 0)) == 13
assert carrier_axial((3, 4, 0)) == carrier_axial((4, 5, 1))
assert x6.full_distance_squared(origin, embed3((3, 4, 0))) == 25
assert x6.full_distance_squared(origin, embed3((4, 5, 1))) == 42
assert x6.full_distance_squared(origin, embed3((-3, -4, 0))) == 25
rrev, hrev = can3((-3, -4, 0))
assert rrev == (1, 0, 4) and hrev == -4
assert sum(v * v for v in rrev) == 17

assert mult3((3, 4, 0)) == 35
assert mult3((-3, -4, 0)) == 35
assert mult3((1, 0, 4)) == 5
assert mult3((1, 1, 1)) == 6
assert carrier_axial((1, 1, 1)) == (0, 0)
assert x6.full_distance_squared(origin, embed3((1, 1, 1))) == 3

shell25 = [
    x
    for x in itertools.product(range(-5, 6), repeat=3)
    if sum(v * v for v in x) == 25
]
assert len(shell25) == 30
support = Counter(sum(v != 0 for v in x) for x in shell25)
assert support == Counter({2: 24, 1: 6})
total25 = sum(mult3(x) for x in shell25)
assert total25 == 846
old_subset = [(0, 5, 0), (3, 4, 0), (4, 3, 0), (5, 0, 0)]
assert sum(mult3(x) for x in old_subset) == 72

# Carrier circle-footprint calculations, exact in squared form.
# Unit nearest-center spacing and R^2=1/3.
assert Fraction(1, 1) < Fraction(4, 3)  # neighbor overlap: d^2 < (2R)^2
assert Fraction(1, 3) - Fraction(1, 4) == Fraction(1, 12)
assert Fraction(3, 1) > Fraction(4, 3)  # next shell does not intersect

result = {
    "raw_triplet_rebase_cases": len(triples),
    "native_distance_pair_cases": pair_checks,
    "carrier_kernel_pair_cases": kernel_pair_checks,
    "raw_3_4_0": {
        "native_norm_squared": 25,
        "carrier_q": 13,
        "shortest_brc": 35,
    },
    "diagonal_shift_4_5_1": {
        "same_carrier": True,
        "native_norm_squared": 42,
    },
    "native_reverse_3_4_0": {
        "native_norm_squared": 25,
        "shortest_brc": 35,
    },
    "legacy_minzero_reverse": {
        "residual": [1, 0, 4],
        "observer_square_sum": 17,
        "positive_shortest_words": 5,
    },
    "carrier_triangle_holonomy": {
        "raw_endpoint": [1, 1, 1],
        "carrier_endpoint": [0, 0],
        "native_norm_squared": 3,
        "shortest_brc": 6,
    },
    "signed_n25_shell": {
        "endpoint_count": 30,
        "support1": 6,
        "support2": 24,
        "shortest_brc_total": 846,
        "legacy_positive_sector_subtotal": 72,
    },
    "carrier_circle": {
        "nearest_center_squared": 1,
        "radius_squared": "1/3",
        "pair_intersection_offset_squared": "1/12",
        "next_shell_squared": 3,
        "gap_free_covering_radius_squared": "1/3",
    },
    "status": "PASS",
}
print(json.dumps(result, indent=2, sort_keys=True))
