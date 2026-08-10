import itertools
import unittest

from enterprise_math.contact_cycle_memory_policy import (
    apply_capacity_guarded_witness_profile,
    capped_repetition_lifetime,
    combined_witnessed_repetition_capacity,
    componentwise_modulo_witness_period,
    cycle_memory_policy_report,
    exact_additive_witness_period,
    lifetime_separating_exponent,
    modulo_witness_after_repetitions,
    repeated_definedness_signature,
    repeated_definedness_signature_from_lifetime,
    witness_capacity_repetition_capacity,
)
from enterprise_math.contact_guarded_witness_normal_form import (
    contact_guarded_witness_profile,
)


CYCLE_K = (
    (2, -1, -1),
    (-1, 2, -1),
    (-1, -1, 2),
)
PATH_K = (
    (2, -1),
    (-1, 2),
)


def direct_capacity_lifetime(state, capacity, increment):
    current = list(state)
    count = 0
    if all(value == 0 for value in increment):
        return None
    while all(
        current[i] + increment[i] <= capacity[i]
        for i in range(len(current))
    ):
        current = [
            current[i] + increment[i]
            for i in range(len(current))
        ]
        count += 1
    return count


def direct_combined_lifetime(score, witness, capacity, profile, limit=80):
    current_score = tuple(score)
    current_witness = tuple(witness)
    count = 0
    while count < limit:
        outcome = apply_capacity_guarded_witness_profile(
            current_score,
            current_witness,
            capacity,
            profile,
        )
        if not outcome.defined:
            return count
        assert outcome.score_state is not None
        assert outcome.witness_state is not None
        current_score = outcome.score_state
        current_witness = outcome.witness_state
        count += 1
    return None


class ContactCycleMemoryPolicyTests(unittest.TestCase):
    def test_capacity_lifetime_matches_direct_increment_exhaustively(self):
        checked = 0
        for dimension in range(1, 4):
            for capacity in itertools.product(range(4), repeat=dimension):
                state_ranges = [range(limit + 1) for limit in capacity]
                for state in itertools.product(*state_ranges):
                    for increment in itertools.product(range(3), repeat=dimension):
                        predicted = witness_capacity_repetition_capacity(
                            state,
                            capacity,
                            increment,
                        )
                        direct = direct_capacity_lifetime(
                            state,
                            capacity,
                            increment,
                        )
                        self.assertEqual(predicted, direct)
                        checked += 1
        self.assertGreater(checked, 1000)

    def test_combined_lifetime_is_minimum_of_coarse_and_witness_guards(self):
        profiles = (
            contact_guarded_witness_profile(
                CYCLE_K,
                (
                    (1, 0, 0),
                    (0, 1, 0),
                    (0, 0, 1),
                ),
                (0, 1, 2),
            ),
            contact_guarded_witness_profile(
                PATH_K,
                ((1, 1),),
                (0,),
            ),
        )
        cases = (
            ((-1, 0, 1), (0, 0, 0), (5, 5, 5), profiles[0]),
            ((-1, -1), (0,), (10,), profiles[1]),
            ((-4, -2), (3,), (4,), profiles[1]),
        )
        for score, witness, capacity, profile in cases:
            predicted = combined_witnessed_repetition_capacity(
                score,
                witness,
                capacity,
                profile,
            )
            direct = direct_combined_lifetime(
                score,
                witness,
                capacity,
                profile,
            )
            self.assertEqual(predicted, direct)

    def test_every_legal_step_decrements_finite_remaining_lifetime_by_one(self):
        profile = contact_guarded_witness_profile(
            PATH_K,
            ((1, 1),),
            (0,),
        )
        for score in itertools.product(range(-6, 1), repeat=2):
            for capacity in range(1, 9):
                for witness in range(capacity + 1):
                    before = combined_witnessed_repetition_capacity(
                        score,
                        (witness,),
                        (capacity,),
                        profile,
                    )
                    if before in (None, 0):
                        continue
                    outcome = apply_capacity_guarded_witness_profile(
                        score,
                        (witness,),
                        (capacity,),
                        profile,
                    )
                    self.assertTrue(outcome.defined)
                    assert outcome.score_state is not None
                    assert outcome.witness_state is not None
                    after = combined_witnessed_repetition_capacity(
                        outcome.score_state,
                        outcome.witness_state,
                        (capacity,),
                        profile,
                    )
                    self.assertEqual(after, before - 1)

    def test_capped_lifetime_is_exact_bounded_definedness_quotient(self):
        for horizon in range(8):
            lifetimes = (None,) + tuple(range(10))
            for left in lifetimes:
                for right in lifetimes:
                    same_signature = (
                        repeated_definedness_signature_from_lifetime(
                            left,
                            horizon,
                        )
                        == repeated_definedness_signature_from_lifetime(
                            right,
                            horizon,
                        )
                    )
                    same_capped = (
                        capped_repetition_lifetime(left, horizon)
                        == capped_repetition_lifetime(right, horizon)
                    )
                    self.assertEqual(same_signature, same_capped)
                    if not same_capped:
                        exponent = lifetime_separating_exponent(
                            left,
                            right,
                            horizon,
                        )
                        left_sig = repeated_definedness_signature_from_lifetime(
                            left,
                            horizon,
                        )
                        right_sig = repeated_definedness_signature_from_lifetime(
                            right,
                            horizon,
                        )
                        self.assertNotEqual(
                            left_sig[exponent],
                            right_sig[exponent],
                        )

    def test_triangle_cycle_full_witness_becomes_finite_countdown(self):
        profile = contact_guarded_witness_profile(
            CYCLE_K,
            (
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
            ),
            (0, 1, 2),
        )
        score = (-1, 0, 1)
        self.assertEqual(
            combined_witnessed_repetition_capacity(
                score,
                (0, 0, 0),
                (5, 5, 5),
                profile,
            ),
            5,
        )
        self.assertEqual(
            repeated_definedness_signature(
                score,
                (0, 0, 0),
                (5, 5, 5),
                profile,
                7,
            ),
            (True, True, True, True, True, True, False, False),
        )

    def test_cycle_witness_killed_by_readout_remains_unbounded(self):
        profile = contact_guarded_witness_profile(
            CYCLE_K,
            ((1, -1, 0),),
            (0, 1, 2),
        )
        self.assertEqual(profile.witness_shift, (0,))
        self.assertIsNone(
            combined_witnessed_repetition_capacity(
                (-1, 0, 1),
                (0,),
                (0,),
                profile,
            )
        )

    def test_total_cycle_witness_capacity_stops_after_floor_slack_over_three(self):
        profile = contact_guarded_witness_profile(
            CYCLE_K,
            ((1, 1, 1),),
            (0, 1, 2),
        )
        self.assertEqual(profile.witness_shift, (3,))
        self.assertEqual(
            combined_witnessed_repetition_capacity(
                (-1, 0, 1),
                (0,),
                (10,),
                profile,
            ),
            3,
        )

    def test_exact_additive_vs_capacity_vs_modulo_are_distinct_policies(self):
        increment = (3,)
        self.assertIsNone(exact_additive_witness_period(increment))
        self.assertEqual(
            witness_capacity_repetition_capacity((0,), (9,), increment),
            3,
        )
        self.assertEqual(
            componentwise_modulo_witness_period(increment, (9,)),
            3,
        )
        self.assertEqual(
            modulo_witness_after_repetitions(
                (0,),
                increment,
                (9,),
                3,
            ),
            (0,),
        )
        report = cycle_memory_policy_report(
            (0,),
            (9,),
            increment,
            (9,),
        )
        self.assertIsNone(report.exact_additive_period)
        self.assertEqual(report.finite_capacity_lifetime, 3)
        self.assertEqual(report.modulo_period, 3)

    def test_componentwise_modulo_period_formula_exhaustively(self):
        checked = 0
        for dimension in range(1, 4):
            for moduli in itertools.product(range(1, 6), repeat=dimension):
                for increment in itertools.product(range(-3, 4), repeat=dimension):
                    period = componentwise_modulo_witness_period(
                        increment,
                        moduli,
                    )
                    state = (0,) * dimension
                    for repetitions in range(1, period):
                        self.assertNotEqual(
                            modulo_witness_after_repetitions(
                                state,
                                increment,
                                moduli,
                                repetitions,
                            ),
                            state,
                        )
                    self.assertEqual(
                        modulo_witness_after_repetitions(
                            state,
                            increment,
                            moduli,
                            period,
                        ),
                        state,
                    )
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_vector_modulo_example_has_lcm_period(self):
        self.assertEqual(
            componentwise_modulo_witness_period(
                (1, 1, 1),
                (4, 6, 5),
            ),
            60,
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            witness_capacity_repetition_capacity(
                (2,),
                (1,),
                (0,),
            )
        with self.assertRaises(ValueError):
            witness_capacity_repetition_capacity(
                (0,),
                (1,),
                (-1,),
            )
        with self.assertRaises(ValueError):
            componentwise_modulo_witness_period((1,), (0,))
        with self.assertRaises(ValueError):
            capped_repetition_lifetime(1, -1)


if __name__ == "__main__":
    unittest.main()
