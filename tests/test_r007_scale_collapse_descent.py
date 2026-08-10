from __future__ import annotations

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_scale_collapse_descent.py"
spec = importlib.util.spec_from_file_location("r007_scale_collapse_descent", MODULE_PATH)
assert spec is not None and spec.loader is not None
r007 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r007)


def test_universal_witness_grid_and_exact_defect() -> None:
    for p in range(2, 7):
        for r in range(2, 20):
            for t in range(1, 20):
                x, y = r007.unsafe_witness(p, r, t)
                assert r007.q(x, r) == r007.q(y, r)
                assert r007.q(r007.collapse(x, p), r) != r007.q(r007.collapse(y, p), r)
                assert r007.coarse_future_defect(p, r, t) == r007.defect_polynomial(p, r, t)


def test_minimal_repair_has_at_most_two_classes_and_one_bit_decodes() -> None:
    for p in range(2, 6):
        for r in range(2, 25):
            for a in range(0, 250):
                values = r007.fiber_repair_values(a, p, r)
                assert len(values) <= 2
                assert (len(values) == 2) == r007.fiber_needs_repair(a, p, r)
                for n in range(a * r, (a + 1) * r):
                    beta = r007.repair_bit(n, p, r)
                    assert r007.repair_future_from_bit(a, beta, p, r) == r007.q(
                        r007.collapse(n, p), r
                    )


def test_infinitely_parameterized_full_erasure_fibers() -> None:
    for p in range(2, 6):
        for r in range(2, 15):
            for t in range(1, 10):
                z = (t * r) ** p
                a = z // r
                repaired = {
                    (r007.q(n, r), r007.q(r007.collapse(n, p), r))
                    for n in range(z, z + r)
                }
                assert repaired == {(a, a)}


def test_scale_relative_collapse_is_natural_downward_and_idempotent() -> None:
    for p in range(2, 6):
        for d in range(1, 8):
            for ratio in range(1, 8):
                e = d * ratio
                for m in range(0, 1000, 23):
                    lhs = r007.projection(r007.relative_lift(m, e, p), e, d)
                    rhs = r007.relative_lift(r007.projection(m, e, d), d, p)
                    assert lhs == rhs
                    assert r007.relative_lift(m, d, p) <= m
                    assert r007.relative_lift(r007.relative_lift(m, d, p), d, p) == r007.relative_lift(
                        m, d, p
                    )


def test_integer_root_itself_descends_through_floor_quotient() -> None:
    for p in range(1, 6):
        for r in range(2, 20):
            for n in range(0, 2000, 19):
                lhs = r007.q(r007.floor_root(n, p), r)
                rhs = r007.root_induced_on_q(r007.q(n, r), p, r)
                assert lhs == rhs
