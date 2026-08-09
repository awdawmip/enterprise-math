import unittest
from math import isqrt

from enterprise_math.incidence_repair import (
    incidence_repair_alphabet_size,
    joint_monotonicity,
    label_decoder_exists,
    observation_coarsening_monotone,
    relation_enlargement_monotone,
)
from enterprise_math.p017_actual_root_separation import lower_band_primes
from enterprise_math.p017_cofactor_window import is_p_rough
from enterprise_math.quotient_window import square_basin_window
from enterprise_math.task_precision_refinement import minimal_repair_alphabet_size


class IncidenceRepairTests(unittest.TestCase):
    def test_incidence_formula_matches_generic_p023_minimal_repair(self) -> None:
        relation = frozenset(
            {
                ("A", 0),
                ("A", 1),
                ("B", 2),
                ("C", 3),
            }
        )
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        burden = incidence_repair_alphabet_size(relation, observation)

        tagged = tuple(sorted(relation))
        coarse = {state: observation[state[1]] for state in tagged}
        target = {state: (observation[state[1]], state[0]) for state in tagged}
        self.assertEqual(
            burden,
            minimal_repair_alphabet_size(tagged, target, coarse),
        )
        self.assertEqual(burden, 2)

    def test_relation_enlargement_can_strictly_increase_burden(self) -> None:
        actual = frozenset({("A", 0)})
        envelope = frozenset({("A", 0), ("B", 1)})
        observation = {0: "z", 1: "z"}
        self.assertTrue(relation_enlargement_monotone(actual, envelope, observation))
        self.assertEqual(incidence_repair_alphabet_size(actual, observation), 1)
        self.assertEqual(incidence_repair_alphabet_size(envelope, observation), 2)

    def test_observation_coarsening_can_strictly_increase_burden(self) -> None:
        relation = frozenset({("A", 0), ("B", 1)})
        fine = {0: "left", 1: "right"}
        coarse = {0: "same", 1: "same"}
        self.assertTrue(observation_coarsening_monotone(relation, fine, coarse))
        self.assertEqual(incidence_repair_alphabet_size(relation, fine), 1)
        self.assertEqual(incidence_repair_alphabet_size(relation, coarse), 2)

    def test_combined_monotonicity_square(self) -> None:
        actual = frozenset({("A", 0), ("B", 1)})
        envelope = frozenset({("A", 0), ("B", 1), ("C", 2)})
        fine = {0: 0, 1: 1, 2: 2}
        coarse = {0: 0, 1: 0, 2: 0}
        self.assertTrue(joint_monotonicity(actual, envelope, fine, coarse))
        self.assertEqual(incidence_repair_alphabet_size(actual, fine), 1)
        self.assertEqual(incidence_repair_alphabet_size(envelope, coarse), 3)

    def test_image_separation_is_exactly_the_alphabet_one_case(self) -> None:
        separated = frozenset({("A", 0), ("B", 1)})
        collided = frozenset({("A", 0), ("B", 1)})
        self.assertTrue(label_decoder_exists(separated, {0: 0, 1: 1}))
        self.assertFalse(label_decoder_exists(collided, {0: 0, 1: 0}))

    def test_p017_k6_raw_window_collision_disappears_after_rough_filter(self) -> None:
        k = 6
        raw_pairs = []
        actual_pairs = []
        states = set()
        for p in lower_band_primes(k):
            window = square_basin_window(k, p)
            self.assertIsNotNone(window)
            assert window is not None
            for q in range(window.lo, window.hi + 1):
                raw_pairs.append((p, q))
                states.add(q)
                if is_p_rough(q, p):
                    actual_pairs.append((p, q))
        observation = {q: isqrt(q) for q in states}
        self.assertEqual(
            incidence_repair_alphabet_size(raw_pairs, observation), 2
        )
        self.assertEqual(
            incidence_repair_alphabet_size(actual_pairs, observation), 1
        )
        self.assertTrue(
            relation_enlargement_monotone(actual_pairs, raw_pairs, observation)
        )


if __name__ == "__main__":
    unittest.main()
