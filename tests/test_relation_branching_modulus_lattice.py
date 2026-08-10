import unittest
from math import lcm

from enterprise_math.relation_branching_modulus_lattice import (
    modular_branching_lattice_report,
    modular_divisibility_branching_refinement,
    modular_gcd_is_common_coefficient_coarsening,
    modular_lcm_branching_equals_product,
    modular_lcm_pair_morphism,
    modular_lcm_pair_morphism_is_injective,
    modular_reduction_morphism,
    modular_terminal_trace_lcm_is_independent_join,
)
from enterprise_math.relation_branching_semiring import verify_semiring_morphism


def crt_correlation_fixture():
    states = (
        "p",
        "q",
        "A",
        "B",
        "C",
        "D",
        "z1",
        "z2",
        "z3",
        "z4",
    )
    relations = {
        "a": frozenset(
            {
                ("p", "A"),
                ("p", "D"),
                ("q", "B"),
                ("q", "C"),
            }
        ),
        "b": frozenset(
            {
                # B has count4 -> (mod2,mod3)=(0,1).
                ("B", "z1"),
                ("B", "z2"),
                ("B", "z3"),
                ("B", "z4"),
                # C has count3 -> (1,0).
                ("C", "z1"),
                ("C", "z2"),
                ("C", "z3"),
                # D has count1 -> (1,1).
                ("D", "z1"),
                # A has count0 -> (0,0).
            }
        ),
    }
    return states, relations, lambda _state: "visible"


def small_fixture():
    states = (0, 1, 2)
    relations = {
        "a": frozenset({(0, 0), (0, 1), (1, 2), (2, 2)}),
        "b": frozenset({(0, 2), (1, 0), (2, 1)}),
    }
    return states, relations, lambda state: int(state == 2)


class RelationBranchingModulusLatticeTests(unittest.TestCase):
    def test_modular_reductions_are_semiring_morphisms(self):
        for coarse, fine in ((2, 4), (2, 6), (3, 6), (4, 12), (6, 12)):
            morphism = modular_reduction_morphism(fine, coarse)
            self.assertTrue(
                verify_semiring_morphism(
                    morphism,
                    tuple(range(2 * fine + 3)),
                )
            )

    def test_lcm_pair_maps_are_injective_semiring_morphisms(self):
        for left, right in ((2, 3), (2, 4), (4, 6), (6, 9), (8, 12)):
            morphism = modular_lcm_pair_morphism(left, right)
            self.assertTrue(modular_lcm_pair_morphism_is_injective(left, right))
            self.assertTrue(
                verify_semiring_morphism(
                    morphism,
                    tuple(range(2 * lcm(left, right) + 3)),
                )
            )

    def test_divisibility_orders_branching_precision(self):
        states, relations, observation = small_fixture()
        for coarse, fine in ((2, 4), (2, 6), (3, 6), (4, 12)):
            for horizon in range(4):
                self.assertTrue(
                    modular_divisibility_branching_refinement(
                        states,
                        relations,
                        observation,
                        horizon,
                        coarse,
                        fine,
                    )
                )

    def test_lcm_branching_equals_product_branching_at_every_checked_horizon(self):
        states, relations, observation = crt_correlation_fixture()
        for left, right in ((2, 3), (2, 4), (3, 6), (4, 6)):
            for horizon in range(4):
                self.assertTrue(
                    modular_lcm_branching_equals_product(
                        states,
                        relations,
                        observation,
                        horizon,
                        left,
                        right,
                    )
                )

    def test_crt_fixture_has_mod2_mod3_readout_join_but_mod6_compositional_split(self):
        states, relations, observation = crt_correlation_fixture()
        report = modular_branching_lattice_report(
            states,
            relations,
            observation,
            2,
            3,
        )
        self.assertEqual(report.gcd_modulus, 1)
        self.assertEqual(report.lcm_modulus, 6)
        self.assertIn(frozenset({"p", "q"}), report.independent_branching_join)
        self.assertIn(frozenset({"p"}), report.coupled_branching_join)
        self.assertIn(frozenset({"q"}), report.coupled_branching_join)
        self.assertEqual(report.coupled_branching_join, report.lcm_branching_partition)
        self.assertGreater(report.compositional_debt_blocks, 0)
        self.assertGreater(report.compositional_repair_steps, 0)

    def test_terminal_modular_count_traces_have_exact_lcm_readout_join(self):
        fixtures = (small_fixture(), crt_correlation_fixture())
        for states, relations, observation in fixtures:
            for left, right in ((2, 3), (2, 4), (3, 6), (4, 6)):
                for horizon in range(4):
                    self.assertTrue(
                        modular_terminal_trace_lcm_is_independent_join(
                            states,
                            relations,
                            observation,
                            horizon,
                            left,
                            right,
                        )
                    )

    def test_gcd_is_common_modular_coarsening(self):
        states, relations, observation = small_fixture()
        for left, right in ((4, 6), (6, 9), (8, 12), (2, 3)):
            for horizon in range(4):
                self.assertTrue(
                    modular_gcd_is_common_coefficient_coarsening(
                        states,
                        relations,
                        observation,
                        horizon,
                        left,
                        right,
                    )
                )

    def test_coprime_terminal_join_is_crt_product_without_branch_debt_requirement(self):
        states, relations, observation = crt_correlation_fixture()
        # Every terminal count entry modulo2 and modulo3 jointly determines its
        # residue modulo6, even though the branching-state join needs extra
        # compositional closure on this same fixture.
        for horizon in range(5):
            self.assertTrue(
                modular_terminal_trace_lcm_is_independent_join(
                    states,
                    relations,
                    observation,
                    horizon,
                    2,
                    3,
                )
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            modular_reduction_morphism(6, 4)
        with self.assertRaises(ValueError):
            modular_reduction_morphism(1, 1)
        with self.assertRaises(TypeError):
            modular_lcm_pair_morphism(False, 3)


if __name__ == "__main__":
    unittest.main()
