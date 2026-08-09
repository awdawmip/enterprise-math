import unittest

from enterprise_math.causal_contextual_join import (
    compile_contextual_type_operation,
    composition_is_associative,
    induced_type_composition,
    stable_contextual_types,
    type_composition_is_associative,
)


class CausalContextualJoinTests(unittest.TestCase):
    def test_mod_four_addition_with_parity_observation_compiles_to_two_types(self):
        states = (0, 1, 2, 3)
        composition = {
            (left, right): (left + right) % 4
            for left in states
            for right in states
        }
        observations = {state: state % 2 for state in states}
        self.assertTrue(composition_is_associative(states, composition))
        classes, induced, _ = compile_contextual_type_operation(
            states, observations, composition
        )
        self.assertEqual(len(set(classes.values())), 2)
        self.assertEqual(classes[0], classes[2])
        self.assertEqual(classes[1], classes[3])
        self.assertNotEqual(classes[0], classes[1])
        self.assertTrue(type_composition_is_associative(induced))
        even = classes[0]
        odd = classes[1]
        self.assertEqual(induced[(even, even)], even)
        self.assertEqual(induced[(even, odd)], odd)
        self.assertEqual(induced[(odd, even)], odd)
        self.assertEqual(induced[(odd, odd)], even)

    def test_contextual_refinement_repairs_a_noncongruent_current_observation(self):
        states = (0, 1, 2, 3)
        composition = {
            (left, right): (left + right) % 4
            for left in states
            for right in states
        }
        # Current observation groups 0~1 and 2~3, but that partition is not
        # stable under adding the same partner.
        observations = {0: 0, 1: 0, 2: 1, 3: 1}
        classes, _ = stable_contextual_types(states, observations, composition)
        self.assertGreater(len(set(classes.values())), 2)
        induced = induced_type_composition(states, composition, classes)
        self.assertTrue(type_composition_is_associative(induced))

    def test_parity_constraint_is_not_absolute_three_body_primitive(self):
        # Binary XOR is a two-type associative continuation law.  A final
        # observation accepting only type 0 recognizes even parity for any
        # number of binary slots, including the classic three-bit set
        # 000,011,101,110.
        states = (0, 1)
        composition = {
            (left, right): left ^ right
            for left in states
            for right in states
        }
        observations = {0: "accept", 1: "reject"}
        classes, induced, _ = compile_contextual_type_operation(
            states, observations, composition
        )
        self.assertEqual(len(set(classes.values())), 2)
        self.assertTrue(type_composition_is_associative(induced))

        zero = classes[0]
        one = classes[1]
        accepted = []
        for a in states:
            for b in states:
                for c in states:
                    t_ab = induced[(classes[a], classes[b])]
                    t_abc = induced[(t_ab, classes[c])]
                    if t_abc == zero:
                        accepted.append((a, b, c))
        self.assertEqual(
            tuple(accepted),
            ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)),
        )

    def test_contextual_type_is_coarser_than_raw_identity_when_future_allows_it(self):
        states = (0, 1, 2, 3)
        composition = {
            (left, right): (left + right) % 4
            for left in states
            for right in states
        }
        observations = {state: state % 2 for state in states}
        classes, _, _ = compile_contextual_type_operation(states, observations, composition)
        self.assertEqual(len(set(classes.values())), 2)
        self.assertLess(len(set(classes.values())), len(states))


if __name__ == "__main__":
    unittest.main()
