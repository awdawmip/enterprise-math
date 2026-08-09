import itertools
import unittest

from enterprise_math.causal_future_module import (
    causal_future_closure,
    future_indistinguishable,
)
from enterprise_math.causal_probe_basis import (
    causal_probe_basis,
    probe_signature,
    same_future_signature,
)


class CausalProbeBasisTests(unittest.TestCase):
    def test_shift_system_basis_is_three_concrete_future_probes(self):
        shift = (
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0),
        )
        basis = causal_probe_basis((shift,), ((1, 0, 0),))
        self.assertEqual(basis.causal_dimension, 3)
        self.assertEqual(basis.stable_depth, 2)
        self.assertEqual(
            tuple(probe.row for probe in basis.probes),
            ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        )
        self.assertEqual(
            tuple(probe.pullback_word for probe in basis.probes),
            ((), (0,), (0, 0)),
        )

    def test_redundant_current_observations_do_not_inflate_causal_basis(self):
        identity = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
        )
        observations = (
            (1, 1, 0),
            (2, 2, 0),
            (0, 0, 0),
        )
        basis = causal_probe_basis((identity,), observations)
        self.assertEqual(basis.causal_dimension, 1)
        self.assertEqual(tuple(probe.row for probe in basis.probes), ((1, 1, 0),))

    def test_probe_basis_signature_matches_full_future_equivalence(self):
        operations = (
            (
                (0, 1, 0),
                (0, 0, 1),
                (0, 0, 0),
            ),
        )
        observations = ((1, 0, 0),)
        closure = causal_future_closure(operations, observations)
        basis = causal_probe_basis(operations, observations)

        states = tuple(itertools.product(range(-1, 2), repeat=3))
        for left in states:
            for right in states:
                self.assertEqual(
                    same_future_signature(left, right, basis),
                    future_indistinguishable(left, right, closure),
                    msg=(left, right),
                )

    def test_causal_basis_size_equals_future_visible_rank(self):
        operations = (
            (
                (0, 1, 0, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 1),
                (0, 0, 0, 0),
            ),
        )
        observations = ((1, 0, 0, 0),)
        closure = causal_future_closure(operations, observations)
        basis = causal_probe_basis(operations, observations)
        self.assertEqual(basis.causal_dimension, closure.causal_visible_rank)
        self.assertEqual(basis.stable_depth, closure.stable_depth)

    def test_probe_signature_is_an_integer_state_not_a_precision_annotation(self):
        operation = (
            (0, 1),
            (0, 0),
        )
        basis = causal_probe_basis((operation,), ((1, 0),))
        self.assertEqual(probe_signature((7, -3), basis), (7, -3))
        self.assertEqual(probe_signature((7, 5), basis), (7, 5))


if __name__ == "__main__":
    unittest.main()
