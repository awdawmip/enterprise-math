import itertools
import unittest

from enterprise_math.contact_cycle_witness_repair import (
    apply_integer_matrix,
    contact_cycle_witness_repair_report,
    decompose_incidence_cycle,
    edge_coboundary_from_vertex_potential,
    fundamental_cycle_lattice,
    same_body_delta,
    same_witness_readout,
    scalar_witness_descends_by_telescoping,
    scalar_witness_vertex_potential,
)
from enterprise_math.contact_guarded_word_normal_form import (
    contact_guarded_profile_power,
    contact_guarded_word_profile,
)


TRIANGLE_B = (
    (-1, 0, 1),
    (1, -1, 0),
    (0, 1, -1),
)

TRIANGLE_K = (
    (2, -1, -1),
    (-1, 2, -1),
    (-1, -1, 2),
)

PATH_B = (
    (-1, 0),
    (1, -1),
    (0, 1),
)

SQUARE_DIAGONAL_B = (
    (-1, 0, 0, 1, -1),
    (1, -1, 0, 0, 0),
    (0, 1, -1, 0, 1),
    (0, 0, 1, -1, 0),
)


class ContactCycleWitnessRepairTests(unittest.TestCase):
    def test_triangle_fundamental_cycle_is_integer_kernel_basis(self):
        lattice = fundamental_cycle_lattice(TRIANGLE_B)
        self.assertEqual(lattice.component_count, 1)
        self.assertEqual(lattice.cycle_rank, 1)
        self.assertEqual(lattice.cycle_basis, ((1, 1, 1),))
        self.assertEqual(
            decompose_incidence_cycle(TRIANGLE_B, (4, 4, 4)),
            (4,),
        )

    def test_square_diagonal_has_two_exact_cycle_coordinates(self):
        lattice = fundamental_cycle_lattice(SQUARE_DIAGONAL_B)
        self.assertEqual(lattice.cycle_rank, 2)
        for coefficients in itertools.product(range(-3, 4), repeat=2):
            cycle = tuple(
                sum(
                    coefficient * basis[index]
                    for coefficient, basis in zip(
                        coefficients,
                        lattice.cycle_basis,
                        strict=True,
                    )
                )
                for index in range(5)
            )
            self.assertEqual(
                decompose_incidence_cycle(
                    SQUARE_DIAGONAL_B,
                    cycle,
                ),
                coefficients,
            )

    def test_tree_has_no_hidden_cycle_history_for_any_linear_readout(self):
        witness = (
            (1, 0),
            (0, 1),
            (3, -5),
        )
        report = contact_cycle_witness_repair_report(
            PATH_B,
            witness,
        )
        self.assertEqual(report.cycle_rank, 0)
        self.assertEqual(report.hidden_witness_rank, 0)
        self.assertTrue(report.witness_descends_through_body_state)
        self.assertFalse(report.hidden_witness_present)
        self.assertEqual(report.hidden_witness_generators, ())

    def test_triangle_full_contact_history_has_one_hidden_cycle_direction(self):
        identity_witness = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
        )
        report = contact_cycle_witness_repair_report(
            TRIANGLE_B,
            identity_witness,
        )
        self.assertEqual(report.cycle_rank, 1)
        self.assertEqual(report.hidden_witness_rank, 1)
        self.assertFalse(report.witness_descends_through_body_state)
        self.assertEqual(
            report.hidden_witness_generators,
            ((1, 1, 1),),
        )
        self.assertIsNone(report.scalar_hidden_grain)

    def test_scalar_witness_can_either_see_or_kill_the_cycle(self):
        total = contact_cycle_witness_repair_report(
            TRIANGLE_B,
            ((1, 1, 1),),
        )
        self.assertFalse(total.witness_descends_through_body_state)
        self.assertEqual(total.hidden_witness_generators, ((3,),))
        self.assertEqual(total.scalar_hidden_grain, 3)

        difference = contact_cycle_witness_repair_report(
            TRIANGLE_B,
            ((1, -1, 0),),
        )
        self.assertTrue(difference.witness_descends_through_body_state)
        self.assertEqual(difference.hidden_witness_rank, 0)
        self.assertEqual(difference.hidden_witness_generators, ((0,),))
        self.assertEqual(difference.scalar_hidden_grain, 0)

    def test_same_body_state_can_split_under_future_witness(self):
        left = (1, 0, 0)
        right = (2, 1, 1)
        self.assertTrue(same_body_delta(TRIANGLE_B, left, right))

        self.assertFalse(
            same_witness_readout(
                (
                    (1, 0, 0),
                    (0, 1, 0),
                    (0, 0, 1),
                ),
                left,
                right,
            )
        )
        self.assertFalse(
            same_witness_readout(
                ((1, 1, 1),),
                left,
                right,
            )
        )
        self.assertTrue(
            same_witness_readout(
                ((1, -1, 0),),
                left,
                right,
            )
        )

    def test_cycle_basis_criterion_matches_bounded_kernel_search(self):
        witness_families = (
            ((1, 0, 0),),
            ((1, 1, 1),),
            ((1, -1, 0),),
            (
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
            ),
        )
        for witness in witness_families:
            report = contact_cycle_witness_repair_report(
                TRIANGLE_B,
                witness,
            )
            bounded_hidden = False
            for cycle in itertools.product(range(-2, 3), repeat=3):
                if any(apply_integer_matrix(TRIANGLE_B, cycle)):
                    continue
                if any(apply_integer_matrix(witness, cycle)):
                    bounded_hidden = True
                    break
            self.assertEqual(
                report.witness_descends_through_body_state,
                not bounded_hidden,
            )

    def test_guarded_cycle_coarse_operation_is_idempotent_while_witness_accumulates(self):
        profile = contact_guarded_word_profile(
            TRIANGLE_K,
            (0, 1, 2),
        )
        self.assertTrue(profile.is_partial_identity)

        cycle_count = (1, 1, 1)
        full_witness = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
        )
        difference_witness = ((1, -1, 0),)

        for repetitions in range(1, 7):
            self.assertEqual(
                contact_guarded_profile_power(
                    profile,
                    repetitions,
                ),
                profile,
            )
            repeated_count = tuple(
                repetitions * value
                for value in cycle_count
            )
            self.assertEqual(
                apply_integer_matrix(
                    full_witness,
                    repeated_count,
                ),
                repeated_count,
            )
            self.assertEqual(
                apply_integer_matrix(
                    difference_witness,
                    repeated_count,
                ),
                (0,),
            )

    def test_cycle_invisible_scalar_witness_is_exact_integer_coboundary(self):
        potential = scalar_witness_vertex_potential(
            TRIANGLE_B,
            (1, -1, 0),
        )
        self.assertEqual(potential, (0, 1, 0))
        self.assertEqual(
            edge_coboundary_from_vertex_potential(
                TRIANGLE_B,
                potential,
            ),
            (1, -1, 0),
        )

    def test_cycle_visible_scalar_witness_has_nontrivial_cohomology(self):
        self.assertIsNone(
            scalar_witness_vertex_potential(
                TRIANGLE_B,
                (1, 1, 1),
            )
        )

    def test_coboundary_witness_telescopes_exactly_to_body_state(self):
        witness = (1, -1, 0)
        for history in itertools.product(range(-2, 3), repeat=3):
            direct = sum(
                coefficient * impulse
                for coefficient, impulse in zip(
                    witness,
                    history,
                    strict=True,
                )
            )
            self.assertEqual(
                scalar_witness_descends_by_telescoping(
                    TRIANGLE_B,
                    witness,
                    history,
                ),
                direct,
            )

    def test_tree_every_scalar_edge_readout_is_a_coboundary(self):
        for witness in itertools.product(range(-2, 3), repeat=2):
            potential = scalar_witness_vertex_potential(
                PATH_B,
                witness,
            )
            self.assertIsNotNone(potential)
            self.assertEqual(
                edge_coboundary_from_vertex_potential(
                    PATH_B,
                    potential,
                ),
                witness,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            fundamental_cycle_lattice(((1,), (-1,), (1,)))
        with self.assertRaises(ValueError):
            fundamental_cycle_lattice(((0,), (0,)))
        with self.assertRaises(ValueError):
            decompose_incidence_cycle(TRIANGLE_B, (1, 0, 0))
        with self.assertRaises(ValueError):
            contact_cycle_witness_repair_report(
                TRIANGLE_B,
                ((1, 0),),
            )
        with self.assertRaises(TypeError):
            contact_cycle_witness_repair_report(
                TRIANGLE_B,
                ((1, True, 0),),
            )


if __name__ == "__main__":
    unittest.main()
