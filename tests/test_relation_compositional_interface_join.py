import unittest

from enterprise_math.relation_branching_semiring import (
    boolean_semiring,
    modular_semiring,
    natural_semiring,
    natural_to_boolean_morphism,
    natural_to_modular_morphism,
)
from enterprise_math.relation_compositional_interface_join import (
    compositional_interface_join_report,
    joint_partitions,
    morphism_ordered_pair_has_zero_compositional_debt,
)
from enterprise_math.relation_support_stable_refinement import (
    partition_from_observation,
    partition_refines,
)


def product_correlation_fixture():
    states = (
        "p",
        "q",
        "a1",
        "a2",
        "c",
        "d",
        "z1",
        "z2",
    )
    relations = {
        "a": frozenset(
            {
                ("p", "a1"),
                ("p", "d"),
                ("q", "a1"),
                ("q", "a2"),
                ("q", "c"),
                ("q", "d"),
            }
        ),
        "b": frozenset(
            {
                ("c", "z1"),
                ("c", "z2"),
                ("d", "z1"),
            }
        ),
    }
    return states, relations, lambda _state: "visible"


def mixed_fixture():
    states = (0, 1, 2, 3, 4)
    relations = {
        "a": frozenset(
            {
                (0, 2),
                (0, 3),
                (1, 2),
                (2, 4),
                (3, 4),
            }
        ),
        "b": frozenset({(2, 2), (3, 4), (4, 4)}),
    }
    observation = lambda state: int(state == 4)
    return states, relations, observation


class RelationCompositionalInterfaceJoinTests(unittest.TestCase):
    def test_product_correlation_fixture_has_positive_compositional_debt(self):
        states, relations, observation = product_correlation_fixture()
        initial = partition_from_observation(states, observation)
        report = compositional_interface_join_report(
            initial,
            relations,
            (boolean_semiring(), modular_semiring(2)),
        )

        self.assertIn(frozenset({"p", "q"}), report.independent_readout_join)
        self.assertIn(frozenset({"p"}), report.coupled_final_partition)
        self.assertIn(frozenset({"q"}), report.coupled_final_partition)
        self.assertTrue(report.has_compositional_debt)
        self.assertEqual(report.extra_compositional_blocks, 1)
        self.assertEqual(report.strict_compositional_repair_steps, 1)
        self.assertTrue(
            partition_refines(
                report.coupled_final_partition,
                report.independent_readout_join,
            )
        )

    def test_N_to_B_factor_pair_has_zero_debt(self):
        states, relations, observation = mixed_fixture()
        initial = partition_from_observation(states, observation)
        self.assertTrue(
            morphism_ordered_pair_has_zero_compositional_debt(
                initial,
                relations,
                natural_to_boolean_morphism(),
            )
        )

    def test_N_to_modular_factor_pair_has_zero_debt(self):
        states, relations, observation = mixed_fixture()
        initial = partition_from_observation(states, observation)
        for modulus in (2, 3, 5):
            self.assertTrue(
                morphism_ordered_pair_has_zero_compositional_debt(
                    initial,
                    relations,
                    natural_to_modular_morphism(modulus),
                )
            )

    def test_one_dominating_N_interface_removes_debt_for_support_and_parity_together(self):
        states, relations, observation = product_correlation_fixture()
        initial = partition_from_observation(states, observation)
        report = compositional_interface_join_report(
            initial,
            relations,
            (natural_semiring(), boolean_semiring(), modular_semiring(2)),
        )
        natural_final = report.individual_final_partitions[0]
        self.assertEqual(report.independent_readout_join, natural_final)
        self.assertEqual(report.coupled_final_partition, natural_final)
        self.assertFalse(report.has_compositional_debt)

    def test_joint_partitions_is_order_independent_at_equivalence_level(self):
        states, relations, observation = mixed_fixture()
        initial = partition_from_observation(states, observation)
        B_Z2 = compositional_interface_join_report(
            initial,
            relations,
            (boolean_semiring(), modular_semiring(2)),
        )
        left = joint_partitions(B_Z2.individual_final_partitions)
        right = joint_partitions(tuple(reversed(B_Z2.individual_final_partitions)))
        self.assertEqual(left, right)

    def test_single_interface_has_no_join_debt_by_definition(self):
        states, relations, observation = mixed_fixture()
        initial = partition_from_observation(states, observation)
        report = compositional_interface_join_report(
            initial,
            relations,
            (boolean_semiring(),),
        )
        self.assertEqual(
            report.independent_readout_join,
            report.coupled_final_partition,
        )
        self.assertFalse(report.has_compositional_debt)

    def test_validation(self):
        states, relations, observation = mixed_fixture()
        initial = partition_from_observation(states, observation)
        with self.assertRaises(ValueError):
            compositional_interface_join_report(initial, relations, ())
        with self.assertRaises(ValueError):
            joint_partitions(())


if __name__ == "__main__":
    unittest.main()
