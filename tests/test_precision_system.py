import unittest

from enterprise_math.factor_precision import factor_witness_state, square_basin
from enterprise_math.precision_system import (
    FALSE,
    TRUE,
    UNRESOLVED,
    ambiguity_gain_profile,
    ambiguity_multiplicity,
    ambiguity_profile,
    deterministic_time_partition_coarsens,
    fiber_nesting,
    first_decision_shells,
    observation_fiber,
    observation_partition,
    predicate_certificate_profile,
    predicate_fiber_certificate,
    product_fiber_identity,
    product_observation,
    refinement_projection,
    strict_refinement_witness,
)


def scale_observation(terminal_scale, scale):
    ratio = terminal_scale // scale
    return lambda state: state // ratio


class PrecisionSystemTests(unittest.TestCase):
    def test_scale_observations_form_refinement_chain(self):
        terminal_scale = 24
        states = list(range(0, 96))
        scales = [1, 2, 4, 8, 24]
        observations = [scale_observation(terminal_scale, scale) for scale in scales]
        for coarse, fine in zip(observations, observations[1:]):
            projection = refinement_projection(states, coarse, fine)
            self.assertTrue(projection)
            for state in states:
                data = fiber_nesting(states, coarse, fine, state)
                self.assertTrue(set(data["fine"]).issubset(data["coarse"]))

    def test_ambiguity_decreases_and_gains_telescope(self):
        terminal_scale = 24
        states = list(range(0, 96))
        scales = [1, 2, 4, 8, 24]
        observations = [scale_observation(terminal_scale, scale) for scale in scales]
        for state in states:
            profile = ambiguity_profile(states, observations, state)
            self.assertEqual(profile, sorted(profile, reverse=True))
            gains = ambiguity_gain_profile(states, observations, state)
            self.assertEqual(sum(gains), profile[0] - profile[-1])
            self.assertEqual(profile[-1], 1)

    def test_strict_decrease_iff_fiber_is_split(self):
        states = list(range(0, 48))
        coarse = scale_observation(12, 1)
        fine = scale_observation(12, 3)
        for state in states:
            before = ambiguity_multiplicity(states, coarse, state)
            after = ambiguity_multiplicity(states, fine, state)
            witness = strict_refinement_witness(states, coarse, fine, state)
            self.assertEqual(before > after, witness is not None)
            if witness is not None:
                self.assertEqual(coarse(witness), coarse(state))
                self.assertNotEqual(fine(witness), fine(state))

    def test_predicate_certificate_persists(self):
        terminal_scale = 24
        states = list(range(0, 72))
        scales = [1, 2, 4, 8, 24]
        observations = [scale_observation(terminal_scale, scale) for scale in scales]
        predicate = lambda x: x < 37
        for state in states:
            profile = predicate_certificate_profile(
                states, observations, predicate, state
            )
            decided = None
            for status in profile:
                if decided is not None:
                    self.assertEqual(status, decided)
                elif status != UNRESOLVED:
                    decided = status
            self.assertEqual(profile[-1], TRUE if predicate(state) else FALSE)

    def test_first_decision_shells_partition_terminal_states(self):
        states = list(range(0, 48))
        observations = [
            scale_observation(12, scale) for scale in [1, 2, 3, 6, 12]
        ]
        predicate = lambda x: x < 23
        shells = first_decision_shells(states, observations, predicate)
        flattened = [state for block in shells.values() for state in block]
        self.assertEqual(sorted(flattened), states)
        self.assertNotIn(None, shells)

    def test_factor_precision_is_an_abstract_precision_system(self):
        k = 11
        states = list(square_basin(k))
        cutoffs = [0, 2, 3, 5, 7, 11]
        observations = [
            (lambda cutoff: (lambda n: factor_witness_state(n, cutoff)))(cutoff)
            for cutoff in cutoffs
        ]
        for coarse, fine in zip(observations, observations[1:]):
            refinement_projection(states, coarse, fine)
        # A composite with a visible factor becomes a constant-composite fiber.
        predicate = lambda n: any(n % p == 0 for p in range(2, k + 1))
        for state in states:
            profile = predicate_certificate_profile(
                states, observations, predicate, state
            )
            # Terminal factor observation may still group several primes together,
            # so only require persistence, not terminal singleton fibers.
            decided = None
            for status in profile:
                if decided is not None:
                    self.assertEqual(status, decided)
                elif status != UNRESOLVED:
                    decided = status

    def test_time_kernel_partition_moves_opposite_to_precision(self):
        states = list(range(0, 32))
        earlier = lambda x: x // 2
        transition = lambda y: y // 2
        self.assertTrue(
            deterministic_time_partition_coarsens(states, earlier, transition)
        )
        later = lambda x: transition(earlier(x))
        for state in states:
            early_fiber = observation_fiber(states, earlier, state)
            later_fiber = observation_fiber(states, later, state)
            self.assertTrue(set(early_fiber).issubset(later_fiber))
            self.assertLessEqual(len(early_fiber), len(later_fiber))

        # Precision moves the other way on the same terminal set.
        coarse = scale_observation(8, 1)
        fine = scale_observation(8, 2)
        for state in states:
            coarse_fiber = observation_fiber(states, coarse, state)
            fine_fiber = observation_fiber(states, fine, state)
            self.assertTrue(set(fine_fiber).issubset(coarse_fiber))
            self.assertLessEqual(len(fine_fiber), len(coarse_fiber))

    def test_product_precision_fiber_is_intersection(self):
        k = 7
        states = list(square_basin(k))
        terminal_scale = 12
        scale_obs = lambda n: n // (terminal_scale // 3)
        factor_obs = lambda n: factor_witness_state(n, 3)
        product = product_observation(scale_obs, factor_obs)
        for state in states:
            data = product_fiber_identity(
                states, scale_obs, factor_obs, state
            )
            self.assertLessEqual(
                data["product_ambiguity"], data["first_ambiguity"]
            )
            self.assertLessEqual(
                data["product_ambiguity"], data["second_ambiguity"]
            )
            self.assertEqual(
                set(observation_fiber(states, product, state)),
                set(data["product_fiber"]),
            )

    def test_observation_partition_is_disjoint_cover(self):
        states = list(range(0, 50))
        observation = lambda x: (x // 5, x % 2)
        partition = observation_partition(states, observation)
        flattened = [state for block in partition.values() for state in block]
        self.assertEqual(sorted(flattened), states)
        self.assertEqual(len(flattened), len(set(flattened)))


if __name__ == "__main__":
    unittest.main()
