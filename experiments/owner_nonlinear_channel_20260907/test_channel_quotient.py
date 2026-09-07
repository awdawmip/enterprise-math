"""Exact finite witnesses and adversarial certificate/input boundary tests."""

from dataclasses import replace
from fractions import Fraction as F
from itertools import product
import unittest

from channel_quotient import (
    GateStep, GateWitness, brc_gate_observation, channel_vector,
    finite_gate_descent_check, gate_image, make_gate_witness, verify_gate_witness,
)


class GateWitnessTests(unittest.TestCase):
    def valid(self, x, y, positive=False):
        w = make_gate_witness(x, y, strictly_positive=positive)
        result = verify_gate_witness(x, y, w, strictly_positive=positive)
        self.assertEqual(result.status, "VALID", result.reason)
        self.assertLessEqual(len(w.steps), 5)
        return w

    def test_equal_and_zero_mass(self):
        self.assertEqual(self.valid((0,) * 6, (0,) * 6).steps, ())
        x = (F(1, 7), 2, 0, 0, 3, 0)
        self.assertEqual(self.valid(x, x).steps, ())

    def test_five_step_boundary_witness(self):
        x, y = (5, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1)
        w = self.valid(x, y)
        self.assertEqual(len(w.steps), 5)
        self.assertEqual([s.gate for s in w.steps], [2, 1, 1, 1, 1])

    def test_strict_positive_rationals_and_coordinate_bounds(self):
        x = (F(1, 11), F(3, 7), F(5, 13), 2, F(8, 17), 3)
        y = tuple(reversed(x))
        w = self.valid(x, y, True)
        for s in w.steps:
            self.assertTrue(all(v > 0 for v in s.after))
            self.assertTrue(all(min(a, b) <= v <= max(a, b)
                                for a, b, v in zip(x, y, s.after)))

    def test_all_small_cone_pairs(self):
        by_mass = {}
        for v in product(range(3), repeat=6):
            if sum(v) <= 3:
                by_mass.setdefault(sum(v), []).append(v)
        pairs = 0
        for vectors in by_mass.values():
            for x in vectors:
                for y in vectors:
                    self.valid(x, y)
                    pairs += 1
        self.assertEqual(pairs, 2978)

    def test_gate_formula_and_idempotence_on_rationals(self):
        for i in range(6):
            x = (F(1, 3), 0, F(4, 7), 2, 0, F(1, 11))
            expected = tuple(x[i] if j == i else (sum(x) - x[i]) / 5 for j in range(6))
            actual = gate_image(x, i)
            self.assertEqual(actual, expected)
            self.assertEqual(gate_image(actual, i), actual)

    def test_wrong_mass_and_invalid_inputs(self):
        with self.assertRaises(ValueError):
            make_gate_witness((1, 0, 0, 0, 0, 0), (0,) * 6)
        for v in [(1,) * 5, (1,) * 7, (True, 0, 0, 0, 0, 0),
                  (0.5, 0, 0, 0, 0, 0), (-1, 0, 0, 0, 0, 0)]:
            with self.assertRaises((ValueError, TypeError)):
                channel_vector(v)
        with self.assertRaises(ValueError):
            channel_vector((0,) * 6, strictly_positive=True)
        class FractionSubclass(F):
            pass
        with self.assertRaises(TypeError):
            channel_vector((FractionSubclass(1), 0, 0, 0, 0, 0))

    def test_witness_is_frozen_from_mutable_inputs(self):
        x, y = [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]
        w = self.valid(x, y)
        x[0] = 99
        y[1] = 88
        self.assertEqual(w.source, (1, 0, 0, 0, 0, 0))
        self.assertEqual(w.target, (0, 1, 0, 0, 0, 0))

    def test_tampered_steps_and_deleted_suffix(self):
        x, y = (5, 0, 0, 0, 0, 0), (0, 1, 1, 1, 1, 1)
        w = make_gate_witness(x, y)
        bad_first = [replace(w.steps[0], amount=True), replace(w.steps[0], amount=F(2)),
                     replace(w.steps[0], gate=0), replace(w.steps[0], donor=True),
                     replace(w.steps[0], after=(4, 0, 1, 0, 0, 0))]
        for first in bad_first:
            bad = replace(w, steps=(first,) + w.steps[1:])
            self.assertEqual(verify_gate_witness(x, y, bad).status, "INVALID")
        self.assertEqual(verify_gate_witness(x, y, replace(w, steps=w.steps[:-1])).status, "INVALID")
        self.assertEqual(verify_gate_witness(x, y, replace(w, steps=w.steps[::-1])).status, "INVALID")

    def test_changed_endpoint_and_malformed_certificate(self):
        x, y = (1, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0)
        w = make_gate_witness(x, y)
        self.assertEqual(verify_gate_witness(y, x, w).status, "INVALID")
        self.assertEqual(verify_gate_witness(x, y, replace(w, steps=())).status, "INVALID")
        self.assertEqual(verify_gate_witness(x, y, replace(w, steps=list(w.steps))).status, "INVALID")
        self.assertEqual(verify_gate_witness(x, y, object()).status, "INVALID")
        class WitnessSubclass(GateWitness):
            pass
        self.assertEqual(verify_gate_witness(x, y, WitnessSubclass(w.source, w.target, w.steps)).status, "INVALID")

    def test_brc_histograms_remain_distinct_after_common_gate(self):
        x = (1, 0, 0, 0, 0, 0)
        y = (F(1, 2), F(1, 2), 0, 0, 0, 0)
        w = self.valid(x, y)
        self.assertEqual(w.steps[0].gate, 2)
        vx, cx, hx = brc_gate_observation(x, 2)
        vy, cy, hy = brc_gate_observation(y, 2)
        self.assertEqual(tuple(vx), gate_image(x, 2))
        self.assertEqual(vx, vy)
        self.assertEqual((cx.count, cy.count), (5, 10))
        self.assertEqual(hx.entries, ((F(1, 5), 5),))
        self.assertEqual(hy.entries, ((F(1, 10), 10),))
        self.assertNotEqual(hx, hy)
        v, c, h = brc_gate_observation((0,) * 6, 2)
        self.assertEqual(tuple(v), (0,) * 6)
        self.assertEqual((c.count, h.count), (0, 0))

    def test_actual_t6_finite_closed_domain_nonlinear_observer(self):
        inputs = [(0,) * 6, (1, 0, 0, 0, 0, 0), (F(1, 2), F(1, 2), 0, 0, 0, 0),
                  (2, 3, 0, 0, 0, 0)]
        for gate in range(6):
            self.assertTrue(finite_gate_descent_check(inputs, gate, lambda v: sum(v) ** 2))
            self.assertTrue(finite_gate_descent_check(inputs, gate, lambda v: sum(v) > 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
