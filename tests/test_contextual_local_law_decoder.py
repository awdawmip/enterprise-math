import unittest

from enterprise_math.bounded_local_law_reflection import (
    exact_weighted_quotient_matrices,
    modulus_is_injective_on_values,
    weighted_local_aggregate_alphabet,
    weighted_refinement_sequence,
)
from enterprise_math.contextual_local_law_decoder import (
    contextual_local_aggregate_codebooks,
    contextual_reflection_reproduces_exact_sequence,
    minimal_contextual_reflective_modulus,
    modularize_weighted_family,
    modulus_is_contextually_reflective,
    reconstruct_exact_quotient_from_modular_only,
)
from enterprise_math.relation_support_stable_refinement import (
    partition_from_observation,
)


class ContextualLocalLawDecoderTests(unittest.TestCase):
    def test_cross_action_residue_collision_is_harmless(self):
        states = ("x", "y", "z")
        family = {
            "a": {("x", "z"): 1},
            "b": {("y", "z"): 4},
        }
        observation = lambda _state: "visible"

        global_alphabet = weighted_local_aggregate_alphabet(states, family)
        self.assertEqual(global_alphabet, frozenset({0, 1, 4}))
        self.assertFalse(modulus_is_injective_on_values(global_alphabet, 3))

        codebooks = contextual_local_aggregate_codebooks(states, family, observation)
        self.assertTrue(modulus_is_contextually_reflective(codebooks, 3))
        self.assertEqual(minimal_contextual_reflective_modulus(codebooks), 3)
        self.assertTrue(
            contextual_reflection_reproduces_exact_sequence(
                states,
                family,
                observation,
                3,
            )
        )

    def test_source_observation_context_can_reuse_one_residue(self):
        states = ("x", "y", "z")
        family = {
            "a": {
                ("x", "z"): 1,
                ("y", "z"): 4,
            }
        }
        labels = {"x": "source-1", "y": "source-2", "z": "target"}
        observation = lambda state: labels[state]

        global_alphabet = weighted_local_aggregate_alphabet(states, family)
        self.assertFalse(modulus_is_injective_on_values(global_alphabet, 3))
        codebooks = contextual_local_aggregate_codebooks(states, family, observation)
        self.assertTrue(modulus_is_contextually_reflective(codebooks, 3))
        self.assertTrue(
            contextual_reflection_reproduces_exact_sequence(
                states,
                family,
                observation,
                3,
            )
        )

    def test_target_observation_context_can_reuse_one_residue(self):
        states = ("x", "y", "t1", "t2")
        family = {
            "a": {
                ("x", "t1"): 1,
                ("y", "t2"): 4,
            }
        }
        labels = {
            "x": "source",
            "y": "source",
            "t1": "target-1",
            "t2": "target-2",
        }
        observation = lambda state: labels[state]

        global_alphabet = weighted_local_aggregate_alphabet(states, family)
        self.assertFalse(modulus_is_injective_on_values(global_alphabet, 3))
        codebooks = contextual_local_aggregate_codebooks(states, family, observation)
        self.assertTrue(modulus_is_contextually_reflective(codebooks, 3))
        self.assertTrue(
            contextual_reflection_reproduces_exact_sequence(
                states,
                family,
                observation,
                3,
            )
        )

    def test_modular_only_decoder_recovers_exact_weight_four_from_residue_one(self):
        states = ("x", "y", "t1", "t2")
        family = {
            "a": {
                ("x", "t1"): 1,
                ("y", "t2"): 4,
            }
        }
        labels = {
            "x": "source",
            "y": "source",
            "t1": "target-1",
            "t2": "target-2",
        }
        observation = lambda state: labels[state]
        codebooks = contextual_local_aggregate_codebooks(states, family, observation)
        modular_family = modularize_weighted_family(states, family, 3)

        # The modular data has forgotten whether the two primitive values were
        # 1 or 4: both are residue 1.  Context identifies the correct codebook.
        self.assertEqual(modular_family["a"][("x", "t1")], 1)
        self.assertEqual(modular_family["a"][("y", "t2")], 1)

        initial = partition_from_observation(states, observation)
        exact_steps = weighted_refinement_sequence(initial, family)
        modular_steps = weighted_refinement_sequence(initial, family, modulus=3)
        self.assertEqual(exact_steps, modular_steps)
        final_partition = exact_steps[-1]

        decoded = reconstruct_exact_quotient_from_modular_only(
            states,
            final_partition,
            modular_family,
            observation,
            3,
            codebooks,
        )
        exact = exact_weighted_quotient_matrices(final_partition, family)
        self.assertEqual(decoded, exact)
        self.assertIn(4, {value for row in decoded["a"] for value in row})

    def test_contextual_reflection_still_rejects_collision_inside_one_coordinate(self):
        states = ("x", "y", "z")
        family = {
            "a": {
                ("x", "z"): 1,
                ("y", "z"): 4,
            }
        }
        observation = lambda _state: "visible"
        codebooks = contextual_local_aggregate_codebooks(states, family, observation)
        self.assertFalse(modulus_is_contextually_reflective(codebooks, 3))
        with self.assertRaises(ValueError):
            contextual_reflection_reproduces_exact_sequence(
                states,
                family,
                observation,
                3,
            )


if __name__ == "__main__":
    unittest.main()
