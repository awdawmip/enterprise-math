import itertools
import unittest

from enterprise_math.relation_branching_semiring import (
    boolean_semiring,
    modular_semiring,
    natural_semiring,
    product_semiring,
)
from enterprise_math.relation_local_count_code_capacity import (
    boolean_code_capacity,
    boolean_modular_code_capacity,
    boolean_modular_family_code_capacity,
    boolean_modular_product_semiring,
    finite_code_capacity,
    first_natural_code_collision,
    local_code_collision_fixture,
    local_code_exact_branching_theorem,
    local_count_code_capacity_report,
    modular_code_capacity,
    modular_family_code_capacity,
    modular_family_lcm,
    modular_product_semiring,
    natural_code_injective_through,
    natural_code_values,
)
from enterprise_math.relation_semiring_stable_refinement import (
    coarsest_shared_semiring_refinement,
)
from enterprise_math.relation_support_stable_refinement import partition_from_observation


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


class RelationLocalCountCodeCapacityTests(unittest.TestCase):
    def test_basic_code_capacities(self):
        self.assertEqual(boolean_code_capacity(), 1)
        for modulus in range(2, 9):
            self.assertEqual(modular_code_capacity(modulus), modulus - 1)
            self.assertEqual(boolean_modular_code_capacity(modulus), modulus)

            self.assertTrue(
                natural_code_injective_through(
                    modular_semiring(modulus),
                    modulus - 1,
                )
            )
            self.assertFalse(
                natural_code_injective_through(
                    modular_semiring(modulus),
                    modulus,
                )
            )

            product_spec = product_semiring(
                boolean_semiring(),
                modular_semiring(modulus),
            )
            self.assertTrue(natural_code_injective_through(product_spec, modulus))
            self.assertFalse(natural_code_injective_through(product_spec, modulus + 1))

    def test_boolean_plus_parity_synergy_exactly_codes_zero_one_two(self):
        BxZ2 = product_semiring(boolean_semiring(), modular_semiring(2))
        self.assertEqual(
            natural_code_values(BxZ2, 3),
            ((0, 0), (1, 1), (1, 0), (1, 1)),
        )
        self.assertTrue(natural_code_injective_through(BxZ2, 2))
        self.assertEqual(first_natural_code_collision(BxZ2, 3), (1, 3))
        self.assertEqual(finite_code_capacity(BxZ2, 10), 2)

    def test_boolean_plus_parity_matches_exact_N_for_every_two_state_relation_pair(self):
        states = (0, 1)
        relations = all_two_state_relations()
        semiring = product_semiring(boolean_semiring(), modular_semiring(2))
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for first in relations:
            for second in relations:
                family = {"a": first, "b": second}
                for observation in observations:
                    self.assertTrue(
                        local_code_exact_branching_theorem(
                            states,
                            family,
                            observation,
                            semiring,
                            max_outdegree=2,
                        )
                    )

    def test_each_individual_boolean_or_parity_view_can_fail_at_degree_two(self):
        for semiring in (boolean_semiring(), modular_semiring(2)):
            states, relations, observation, collision = local_code_collision_fixture(
                semiring,
                2,
            )
            self.assertIsNotNone(collision)
            initial = partition_from_observation(states, observation)
            exact = coarsest_shared_semiring_refinement(
                initial,
                relations,
                (natural_semiring(),),
            )
            coded = coarsest_shared_semiring_refinement(
                initial,
                relations,
                (semiring,),
            )
            self.assertNotEqual(exact.final_partition, coded.final_partition)

    def test_modular_family_capacity_is_lcm_minus_one(self):
        families = (
            (2, 3),
            (4, 6),
            (6, 9),
            (4, 6, 9),
        )
        for moduli in families:
            common = modular_family_lcm(moduli)
            semiring = modular_product_semiring(moduli)
            self.assertEqual(modular_family_code_capacity(moduli), common - 1)
            self.assertTrue(natural_code_injective_through(semiring, common - 1))
            self.assertFalse(natural_code_injective_through(semiring, common))
            self.assertEqual(first_natural_code_collision(semiring, common), (0, common))

    def test_boolean_extends_modular_family_capacity_by_exactly_one(self):
        for moduli in ((2, 3), (4, 6), (4, 6, 9)):
            common = modular_family_lcm(moduli)
            semiring = boolean_modular_product_semiring(moduli)
            self.assertEqual(boolean_modular_family_code_capacity(moduli), common)
            self.assertTrue(natural_code_injective_through(semiring, common))
            self.assertFalse(natural_code_injective_through(semiring, common + 1))
            self.assertEqual(
                first_natural_code_collision(semiring, common + 1),
                (1, common + 1),
            )

    def test_collision_fixture_gives_worst_case_failure_for_generic_semiring(self):
        semirings_and_deltas = (
            (boolean_semiring(), 2),
            (modular_semiring(3), 3),
            (product_semiring(boolean_semiring(), modular_semiring(2)), 3),
            (modular_product_semiring((2, 3)), 6),
            (boolean_modular_product_semiring((2, 3)), 7),
        )
        for semiring, delta in semirings_and_deltas:
            states, relations, observation, collision = local_code_collision_fixture(
                semiring,
                delta,
            )
            self.assertIsNotNone(collision)
            initial = partition_from_observation(states, observation)
            exact = coarsest_shared_semiring_refinement(
                initial,
                relations,
                (natural_semiring(),),
            )
            coded = coarsest_shared_semiring_refinement(
                initial,
                relations,
                (semiring,),
            )
            self.assertNotEqual(exact.final_partition, coded.final_partition)

    def test_capacity_report_exposes_first_collision(self):
        report = local_count_code_capacity_report(
            product_semiring(boolean_semiring(), modular_semiring(2)),
            4,
        )
        self.assertFalse(report.injective)
        self.assertEqual(report.first_collision, (1, 3))
        self.assertEqual(report.code_values[:4], ((0, 0), (1, 1), (1, 0), (1, 1)))

    def test_validation(self):
        with self.assertRaises(ValueError):
            modular_family_lcm(())
        with self.assertRaises(ValueError):
            natural_code_values(boolean_semiring(), -1)
        with self.assertRaises(ValueError):
            local_code_collision_fixture(natural_semiring(), 5)
        with self.assertRaises(ValueError):
            local_code_exact_branching_theorem(
                (0, 1),
                {"a": frozenset({(0, 0), (0, 1)})},
                lambda _state: 0,
                modular_semiring(2),
                max_outdegree=2,
            )


if __name__ == "__main__":
    unittest.main()
