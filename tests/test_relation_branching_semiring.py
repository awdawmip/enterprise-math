import itertools
import unittest

from enterprise_math.relation_branching_future_signature import (
    branching_signature_partition,
)
from enterprise_math.relation_branching_semiring import (
    boolean_semiring,
    map_branching_signature,
    modular_semiring,
    morphism_commutes_with_branching_construction,
    morphism_commutes_with_trace_fold,
    morphism_source_partition_refines_target,
    natural_semiring,
    natural_to_boolean_morphism,
    natural_to_modular_morphism,
    product_projection_left,
    product_projection_right,
    product_semiring,
    raw_semiring_word_trace,
    semiring_branching_partition,
    semiring_branching_signature_map,
    semiring_trace_from_branching_signature,
    trace_projection_matches_raw_semiring_execution,
    verify_semiring_morphism,
    words_through_horizon,
)
from enterprise_math.relation_count_branching_signature import (
    count_branching_signature_partition,
)
from enterprise_math.relation_support_stable_refinement import partition_refines


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


def count_0123_fixture():
    states = ("x0", "x1", "x2", "x3", "u", "v", "w")
    relations = {
        "a": frozenset(
            {
                ("x1", "u"),
                ("x2", "u"),
                ("x2", "v"),
                ("x3", "u"),
                ("x3", "v"),
                ("x3", "w"),
            }
        )
    }
    return states, relations, lambda _state: "visible"


class RelationBranchingSemiringTests(unittest.TestCase):
    def test_standard_coefficient_maps_are_semiring_morphisms_on_bounded_samples(self):
        self.assertTrue(
            verify_semiring_morphism(
                natural_to_boolean_morphism(),
                tuple(range(8)),
            )
        )
        for modulus in range(2, 8):
            self.assertTrue(
                verify_semiring_morphism(
                    natural_to_modular_morphism(modulus),
                    tuple(range(12)),
                )
            )

    def test_generic_N_and_B_branching_match_concrete_compilers(self):
        states = (0, 1)
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        N = natural_semiring()
        B = boolean_semiring()
        for relation in all_two_state_relations():
            relations = {"a": relation}
            for observation in observations:
                for horizon in range(4):
                    self.assertEqual(
                        semiring_branching_partition(
                            states, relations, observation, horizon, N
                        ),
                        count_branching_signature_partition(
                            states, relations, observation, horizon
                        ),
                    )
                    self.assertEqual(
                        semiring_branching_partition(
                            states, relations, observation, horizon, B
                        ),
                        branching_signature_partition(
                            states, relations, observation, horizon
                        ),
                    )

    def test_N_to_B_and_N_to_modular_maps_commute_with_branching_construction(self):
        states = (0, 1)
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        morphisms = (
            natural_to_boolean_morphism(),
            natural_to_modular_morphism(2),
            natural_to_modular_morphism(3),
        )
        for relation in all_two_state_relations():
            relations = {"a": relation}
            for observation in observations:
                for horizon in range(4):
                    for morphism in morphisms:
                        self.assertTrue(
                            morphism_commutes_with_branching_construction(
                                states,
                                relations,
                                observation,
                                horizon,
                                morphism,
                            )
                        )
                        self.assertTrue(
                            morphism_source_partition_refines_target(
                                states,
                                relations,
                                observation,
                                horizon,
                                morphism,
                            )
                        )

    def test_semiring_branching_trace_projection_matches_raw_execution(self):
        states = (0, 1)
        relations = {
            "a": frozenset({(0, 0), (0, 1), (1, 1)}),
            "b": frozenset({(0, 1), (1, 0)}),
        }
        observation = lambda state: state
        semirings = (
            natural_semiring(),
            boolean_semiring(),
            modular_semiring(2),
            modular_semiring(3),
        )
        words = words_through_horizon(tuple(relations), 4)
        for semiring in semirings:
            for source in states:
                for word in words:
                    self.assertTrue(
                        trace_projection_matches_raw_semiring_execution(
                            states,
                            relations,
                            observation,
                            source,
                            word,
                            semiring,
                        )
                    )

    def test_coefficient_morphism_commutes_with_trace_fold(self):
        states = (0, 1)
        relations = {
            "a": frozenset({(0, 0), (0, 1), (1, 1)}),
            "b": frozenset({(0, 1), (1, 0)}),
        }
        observation = lambda state: state
        horizon = 4
        N_signatures = semiring_branching_signature_map(
            states,
            relations,
            observation,
            horizon,
            natural_semiring(),
        )
        words = words_through_horizon(tuple(relations), horizon)
        for morphism in (
            natural_to_boolean_morphism(),
            natural_to_modular_morphism(2),
            natural_to_modular_morphism(3),
        ):
            for signature in N_signatures.values():
                for word in words:
                    self.assertTrue(
                        morphism_commutes_with_trace_fold(
                            signature,
                            word,
                            morphism,
                        )
                    )

    def test_boolean_support_and_mod2_count_are_incomparable_coefficient_views(self):
        B = boolean_semiring()
        Z2 = modular_semiring(2)

        # 0 versus 2: support distinguishes absent/present, parity does not.
        self.assertNotEqual(B.natural(0), B.natural(2))
        self.assertEqual(Z2.natural(0), Z2.natural(2))

        # 1 versus 2: parity distinguishes, support only sees nonzero.
        self.assertEqual(B.natural(1), B.natural(2))
        self.assertNotEqual(Z2.natural(1), Z2.natural(2))

        # Hence no factor map compatible with the natural-count embeddings can
        # exist in either direction.

    def test_product_semiring_is_a_common_branching_refinement_of_support_and_parity(self):
        states, relations, observation = count_0123_fixture()
        B = boolean_semiring()
        Z2 = modular_semiring(2)
        product_spec = product_semiring(B, Z2)
        product_partition = semiring_branching_partition(
            states,
            relations,
            observation,
            1,
            product_spec,
        )
        B_partition = semiring_branching_partition(
            states,
            relations,
            observation,
            1,
            B,
        )
        Z2_partition = semiring_branching_partition(
            states,
            relations,
            observation,
            1,
            Z2,
        )
        self.assertTrue(partition_refines(product_partition, B_partition))
        self.assertTrue(partition_refines(product_partition, Z2_partition))

        left_projection = product_projection_left(B, Z2)
        right_projection = product_projection_right(B, Z2)
        self.assertTrue(
            verify_semiring_morphism(
                left_projection,
                ((0, 0), (1, 0), (0, 1), (1, 1)),
            )
        )
        self.assertTrue(
            verify_semiring_morphism(
                right_projection,
                ((0, 0), (1, 0), (0, 1), (1, 1)),
            )
        )

    def test_product_support_parity_is_still_coarser_than_exact_N_counts(self):
        states, relations, observation = count_0123_fixture()
        product_spec = product_semiring(boolean_semiring(), modular_semiring(2))
        product_partition = semiring_branching_partition(
            states,
            relations,
            observation,
            1,
            product_spec,
        )
        natural_partition = semiring_branching_partition(
            states,
            relations,
            observation,
            1,
            natural_semiring(),
        )
        self.assertTrue(partition_refines(natural_partition, product_partition))
        self.assertIn(frozenset({"x1", "x3"}), product_partition)
        self.assertIn(frozenset({"x1"}), natural_partition)
        self.assertIn(frozenset({"x3"}), natural_partition)

    def test_modular_branching_can_annihilate_nonempty_successor_multiplicity(self):
        states, relations, observation = count_0123_fixture()
        Z2 = modular_semiring(2)
        partition = semiring_branching_partition(
            states,
            relations,
            observation,
            1,
            Z2,
        )
        # x0 has zero successors and x2 has two equivalent successors; both have
        # coefficient zero modulo two.
        self.assertIn(frozenset({"x0", "x2"}), partition)

    def test_validation(self):
        with self.assertRaises(ValueError):
            modular_semiring(1)
        with self.assertRaises(TypeError):
            modular_semiring(False)
        with self.assertRaises(ValueError):
            natural_semiring().natural(-1)
        with self.assertRaises(ValueError):
            words_through_horizon(("a",), -1)


if __name__ == "__main__":
    unittest.main()
