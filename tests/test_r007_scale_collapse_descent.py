from __future__ import annotations

import importlib.util
from math import gcd
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


def test_safe_affine_classification_grid() -> None:
    for r in range(2, 15):
        for u in range(5):
            for v in range(0, 3 * r + 1):
                predicted = r007.affine_predicted_safe(u, v, r)
                observed = r007.is_safe_on_prefix(lambda n, u=u, v=v: u * n + v, r, 50)
                assert predicted == observed


def test_translation_safe_iff_divisible() -> None:
    for r in range(2, 25):
        for t in range(0, 4 * r + 1):
            assert r007.translation_predicted_safe(t, r) == r007.is_safe_on_prefix(
                lambda n, t=t: n + t, r, 50
            )


def test_power_reembedding_is_uniformly_unsafe() -> None:
    for p in range(2, 7):
        for r in range(2, 20):
            for t in range(1, 20):
                x, y = r007.power_unsafe_witness(p, r, t)
                assert r007.q(x, r) == r007.q(y, r)
                assert r007.q(r007.power_map(x, p), r) != r007.q(r007.power_map(y, p), r)


def test_residue_tower_policies_are_coherent() -> None:
    policies = [
        r007.residue_zero,
        r007.residue_identity,
        r007.residue_reflect,
        r007.residue_divide(2),
        r007.residue_divide(3),
        r007.residue_upper_divide(2),
        r007.residue_upper_divide(3),
    ]
    for rho in policies:
        for d in range(1, 10):
            for ratio in range(1, 8):
                for u in range(d * ratio):
                    assert r007.residue_policy_coherent(rho, d, ratio, u)


def test_general_residue_lifts_are_natural() -> None:
    policies = [
        r007.residue_zero,
        r007.residue_identity,
        r007.residue_reflect,
        r007.residue_divide(2),
        r007.residue_upper_divide(2),
    ]
    coarse_maps = [lambda a: a, lambda a: a // 2, lambda a: r007.floor_root(a, 2)]
    for rho in policies:
        for coarse_map in coarse_maps:
            for d in range(1, 8):
                for ratio in range(1, 7):
                    for m in range(0, 500, 19):
                        assert r007.check_natural_lift_square(m, d, ratio, coarse_map, rho)


def test_translation_language_scale_spectrum_is_divisor_lattice_of_gcd() -> None:
    for steps in ([6, 10], [12, 18, 30], [7], [0, 24, 36], [18, 42, 66]):
        g = 0
        for t in steps:
            g = gcd(g, t)
        spectrum = r007.translation_scale_spectrum(list(steps))
        assert spectrum == [r for r in range(1, g + 1) if g % r == 0]
        for r in range(1, g + 3):
            assert (r in spectrum) == all(t % r == 0 for t in steps)
