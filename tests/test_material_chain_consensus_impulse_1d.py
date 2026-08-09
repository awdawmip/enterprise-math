import itertools
import unittest

from enterprise_math.material_chain_consensus_impulse_1d import (
    balanced_integer_consensus,
    chain_candidate_is_nonclosing,
    chain_minimum_impulse_from_momenta,
    solve_equal_mass_chain_consensus_impulse,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_uniform_chain_impulse_1d import (
    uniform_chain_minimum_impulse_vector,
)


def chain_state(momenta, mass=1):
    values = tuple(momenta)
    return ContactNetworkMomentum1D(
        masses=(mass,) * len(values),
        momenta=values,
        contacts=tuple(
            ContactChannel1D(index, index + 1, 1)
            for index in range(len(values) - 1)
        ),
    )


class MaterialChainConsensusImpulse1DTests(unittest.TestCase):
    def test_balanced_integer_consensus_preserves_sum_and_has_range_at_most_one(self):
        for body_count in range(1, 9):
            for total in range(-30, 31):
                target = balanced_integer_consensus(total, body_count)
                self.assertEqual(sum(target), total)
                self.assertEqual(tuple(sorted(target)), target)
                self.assertLessEqual(max(target) - min(target), 1)

    def test_general_profile_specializes_to_uniform_closed_form(self):
        for contact_count in range(1, 11):
            for closing_score in range(1, 6):
                for offset in (-17, 0, 23):
                    momenta = tuple(
                        offset - closing_score * index
                        for index in range(contact_count + 1)
                    )
                    self.assertEqual(
                        chain_minimum_impulse_from_momenta(momenta),
                        uniform_chain_minimum_impulse_vector(
                            contact_count, closing_score
                        ),
                    )

    def test_nonuniform_closing_profile_reaches_balanced_consensus(self):
        solution = solve_equal_mass_chain_consensus_impulse(
            chain_state((5, 3, 2, 0))
        )
        self.assertEqual(solution.impulse_vector, (3, 4, 3))
        self.assertEqual(solution.minimum_total_impulse, 10)
        self.assertEqual(solution.balanced_final_momenta, (2, 2, 3, 3))
        self.assertEqual(solution.final_scores, (0, 1, 0))
        self.assertEqual(solution.surplus_contact, 1)
        self.assertFalse(solution.exact_comoving_consensus)
        self.assertEqual(
            sum(solution.balanced_final_momenta),
            sum(solution.before.momenta),
        )

    def test_nonuniform_profile_can_reach_exact_integer_consensus(self):
        solution = solve_equal_mass_chain_consensus_impulse(
            chain_state((6, 5, 2, -1))
        )
        self.assertEqual(solution.balanced_final_momenta, (3, 3, 3, 3))
        self.assertEqual(solution.final_scores, (0, 0, 0))
        self.assertIsNone(solution.surplus_contact)
        self.assertTrue(solution.exact_comoving_consensus)

    def test_negative_total_momentum_uses_euclidean_balanced_remainder_correctly(self):
        solution = solve_equal_mass_chain_consensus_impulse(
            chain_state((-1, -3, -7))
        )
        self.assertEqual(solution.impulse_vector, (3, 4))
        self.assertEqual(solution.balanced_final_momenta, (-4, -4, -3))
        self.assertEqual(solution.final_scores, (0, 1))
        self.assertEqual(solution.surplus_contact, 1)

    def test_already_comoving_chain_needs_zero_impulse(self):
        solution = solve_equal_mass_chain_consensus_impulse(
            chain_state((4, 4, 4, 4))
        )
        self.assertEqual(solution.impulse_vector, (0, 0, 0))
        self.assertEqual(solution.minimum_total_impulse, 0)
        self.assertEqual(solution.balanced_final_momenta, (4, 4, 4, 4))
        self.assertTrue(solution.exact_comoving_consensus)

    def test_componentwise_minimum_matches_independent_small_domain_oracle(self):
        values = range(-2, 3)
        for body_count in range(2, 6):
            for nondecreasing in itertools.combinations_with_replacement(values, body_count):
                momenta = tuple(reversed(nondecreasing))
                minimum = chain_minimum_impulse_from_momenta(momenta)
                ranges = tuple(range(value + 3) for value in minimum)
                feasible_count = 0
                for candidate in itertools.product(*ranges):
                    if not chain_candidate_is_nonclosing(momenta, candidate):
                        continue
                    feasible_count += 1
                    self.assertTrue(
                        all(
                            candidate[index] >= minimum[index]
                            for index in range(len(minimum))
                        )
                    )
                self.assertGreater(feasible_count, 0)

    def test_prefix_transfer_identity_recovers_every_minimum_contact_impulse(self):
        profiles = (
            (9, 8, 3, 3, -2),
            (5, 3, 2, 0),
            (4, 4, 2),
            (-1, -3, -7),
        )
        for momenta in profiles:
            target = balanced_integer_consensus(sum(momenta), len(momenta))
            impulses = chain_minimum_impulse_from_momenta(momenta)
            for prefix, impulse in enumerate(impulses, start=1):
                self.assertEqual(
                    impulse,
                    sum(momenta[:prefix]) - sum(target[:prefix]),
                )

    def test_common_equal_mass_value_does_not_change_normalized_solution(self):
        unit = solve_equal_mass_chain_consensus_impulse(
            chain_state((5, 3, 2, 0), mass=1)
        )
        seven = solve_equal_mass_chain_consensus_impulse(
            chain_state((5, 3, 2, 0), mass=7)
        )
        self.assertEqual(unit.impulse_vector, seven.impulse_vector)
        self.assertEqual(unit.balanced_final_momenta, seven.balanced_final_momenta)

    def test_invalid_hypotheses_are_rejected(self):
        with self.assertRaises(ValueError):
            balanced_integer_consensus(0, 0)
        with self.assertRaises(ValueError):
            chain_minimum_impulse_from_momenta((1,))
        with self.assertRaises(ValueError):
            chain_minimum_impulse_from_momenta((0, 1))
        with self.assertRaises(ValueError):
            chain_candidate_is_nonclosing((2, 1), ())
        with self.assertRaises(ValueError):
            chain_candidate_is_nonclosing((2, 1), (-1,))

        unequal = ContactNetworkMomentum1D(
            masses=(1, 2, 1),
            momenta=(3, 2, 0),
            contacts=(ContactChannel1D(0, 1, 1), ContactChannel1D(1, 2, 1)),
        )
        with self.assertRaises(ValueError):
            solve_equal_mass_chain_consensus_impulse(unequal)

        separating = chain_state((2, 3, 0))
        with self.assertRaises(ValueError):
            solve_equal_mass_chain_consensus_impulse(separating)

        noncanonical = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(3, 2, 0),
            contacts=(ContactChannel1D(1, 0, -1), ContactChannel1D(1, 2, 1)),
        )
        with self.assertRaises(ValueError):
            solve_equal_mass_chain_consensus_impulse(noncanonical)


if __name__ == "__main__":
    unittest.main()
