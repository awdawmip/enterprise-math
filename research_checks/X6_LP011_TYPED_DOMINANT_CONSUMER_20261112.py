"""LP011 bounded raw signed X6 dominant/observer and BRC interface regression.

Standalone exact-integer regression, distinct from prior signed-shell 72/111 checks.
When executed inside enterprise-math, optionally uses the existing Source
experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py module.
Provenance: LP011 HIRR REQUEST_REVISION; current TASK_RESEARCH, NONBLIND.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
from math import factorial
from pathlib import Path

SELECTED_AXES = (0, 2, 5)  # zero-based, noncontiguous selected native axes
REPO_ROOT = Path(__file__).resolve().parents[1]
BRC_SOURCE = REPO_ROOT / "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"


def dominant_signed(vector):
    v = tuple(vector)
    if len(v) not in (3, 6) or any(type(x) is not int for x in v):
        raise ValueError("raw signed integer 3-slice or 6-X6 required")
    m = max(map(abs, v))
    if not m:
        return frozenset()
    return frozenset((i, 1 if x > 0 else -1) for i, x in enumerate(v) if abs(x) == m)


def embed3(v):
    assert len(v) == 3
    out = [0] * 6
    for k, x in zip(SELECTED_AXES, v):
        out[k] = x
    return tuple(out)


def minzero(v):
    h = min(v)
    return tuple(x-h for x in v), h


def signed_from_observer(a, h):
    assert min(a) == 0 and all(type(x) is int and x >= 0 for x in a)
    M = max(a)
    if M == 0:
        if h == 0:
            return frozenset()
        return frozenset((i, 1 if h > 0 else -1) for i in range(3))
    theta = 2*h + M
    positive = {(i, 1) for i, x in enumerate(a) if x == M}
    negative = {(i, -1) for i, x in enumerate(a) if x == 0}
    if theta > 0:
        return frozenset(positive)
    if theta < 0:
        return frozenset(negative)
    return frozenset(positive | negative)


def legacy_positive_selector(a):
    M = max(a)
    return frozenset((i, 1) for i, x in enumerate(a) if x == M) if M else frozenset()


def brc_shortest(v):
    v = tuple(v)
    n = sum(map(abs, v))
    out = factorial(n)
    for x in v:
        out //= factorial(abs(x))
    return out


def main():
    signed_points = 0
    positive_guard_matches = 0
    zero_cases = 0
    signed_ties = 0
    brc_samples = 0
    imported_module_calls = 0
    module = None
    if BRC_SOURCE.is_file():
        spec = importlib.util.spec_from_file_location("x6_signed_brc_source_lp011", BRC_SOURCE)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    for d in itertools.product(range(-7, 8), repeat=3):
        signed_points += 1
        a, h = minzero(d)
        D3 = dominant_signed(d)
        D6 = dominant_signed(embed3(d))
        assert D3 == signed_from_observer(a, h)
        assert D6 == frozenset((SELECTED_AXES[i], sign) for i, sign in D3)
        assert dominant_signed(tuple(-x for x in d)) == frozenset((i, -s) for i, s in D3)
        assert D3 == legacy_positive_selector(a) if ((max(a) > 0 and 2*h+max(a) > 0) or (max(a) == 0 and h == 0)) else D3 != legacy_positive_selector(a)
        positive_guard_matches += (D3 == legacy_positive_selector(a))
        zero_cases += (d == (0, 0, 0))
        signed_ties += (len(D3) > 1)
        c3 = brc_shortest(d)
        c6 = brc_shortest(embed3(d))
        assert c3 == c6 == brc_shortest(tuple(-x for x in d))
        brc_samples += 1
        if module is not None:
            assert module.shortest_path_multiplicity(embed3(d)) == c6
            imported_module_calls += 1
    assert dominant_signed((0, 0, 0)) == frozenset()
    assert dominant_signed((0, 0, 0, 0, 0, 0)) == frozenset()
    assert signed_from_observer((0, 2, 4), -2) == frozenset({(0, -1), (2, 1)})
    a = (0, 1, 4)
    assert brc_shortest(tuple(x - 2 for x in a)) == 30
    assert brc_shortest(a) == 5
    assert minzero(tuple(x - 2 for x in a))[0] == minzero(a)[0]
    print(json.dumps({
        "status": "PASS", "signed_points": signed_points,
        "signed_ties": signed_ties, "zero_cases": zero_cases,
        "legacy_selector_agreement": positive_guard_matches,
        "three_axis_embedding": list(SELECTED_AXES),
        "brc_shortest_formula_checks": brc_samples,
        "existing_native_brc_imported": module is not None,
        "existing_native_brc_calls": imported_module_calls,
        "LP011_status": "bounded proposed typed consumer; historical original caller not located",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
