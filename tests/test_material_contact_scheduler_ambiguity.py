import unittest

from enterprise_math.material_contact_causal_history_state import (
    history_aware_causal_material_tick,
    history_state_from_exact_applied_history,
)
from enterprise_math.material_contact_causal_tick_state import (
    CausalMaterialContactState1D,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_incidence_matrix,
)
from enterprise_math.material_contact_network_tick_1d import (
    ContactMaterialImpulseState,
)
from enterprise_math.material_contact_scheduler_ambiguity import (
    exact_queue_is_scheduler_deterministic,
    history_scheduler_determinism_report,
    linear_terminal_output_relation,
    observable_is_scheduler_deterministic,
    repeated_scalar_modular_ambiguity_phase_count,
    scalar_modular_scheduler_deterministic,
    scalar_modular_terminal_outputs,
    scalar_scheduler_ambiguity_grain,
    scheduler_difference_generators,
)
from enterprise_math.material_contact_tick_causal_queue import (
    guarded_terminal_prefix_relation,
)


def reservoirs(count):
    return tuple(ContactMaterialImpulseState(1, 1, 0) for _ in range(count))


class MaterialContactSchedulerAmbiguityTests(unittest.TestCase):
    def test_v_terminal_difference_lattice_controls_linear_observables(self):
        relation = guarded_terminal_prefix_relation(
            (-1, -2),
            ((2, 1), (1, 2)),
            (1, 1),
        )
        self.assertEqual(
            {terminal.applied_counts for terminal in relation.terminals},
            {(0, 1), (1, 1)},
        )
        generators = scheduler_difference_generators(relation)
        self.assertEqual(len(generators), 1)
        self.assertIn(generators[0], ((1, 0), (-1, 0)))

        self.assertFalse(
            observable_is_scheduler_deterministic(
                relation,
                ((1, 1),),
            )
        )
        self.assertEqual(
            linear_terminal_output_relation(relation, ((1, 1),)),
            ((1,), (2,)),
        )
        self.assertFalse(exact_queue_is_scheduler_deterministic(relation))

    def test_q1_star_body_branches_but_total_applied_contact_count_is_exact(self):
        relation = guarded_terminal_prefix_relation(
            (-1, -1, -1),
            (
                (2, 1, 1),
                (1, 2, 1),
                (1, 1, 2),
            ),
            (1, 1, 1),
        )
        # Total applied count is one on every branch.
        total = ((1, 1, 1),)
        self.assertTrue(observable_is_scheduler_deterministic(relation, total))
        self.assertEqual(linear_terminal_output_relation(relation, total), ((1,),))
        self.assertEqual(scalar_scheduler_ambiguity_grain(relation, total[0]), 0)

        # Full labeled applied-contact history distinguishes all three branches.
        identity = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
        )
        self.assertFalse(
            observable_is_scheduler_deterministic(relation, identity)
        )
        self.assertEqual(len(linear_terminal_output_relation(relation, identity)), 3)
        self.assertFalse(exact_queue_is_scheduler_deterministic(relation))

        # The actual body incidence also distinguishes the unit branches.
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
                ContactChannel1D(0, 3, 1),
            ),
        )
        incidence = contact_incidence_matrix(network)
        self.assertFalse(observable_is_scheduler_deterministic(relation, incidence))

    def test_exact_branch_can_disappear_modulo_declared_history_precision(self):
        relation = guarded_terminal_prefix_relation(
            (-1, -2),
            ((2, 1), (1, 2)),
            (1, 1),
        )
        # c=(2,0) gives outputs 0 and 2: exact branch remains, mod 2 it vanishes.
        row = (2, 0)
        self.assertEqual(scalar_scheduler_ambiguity_grain(relation, row), 2)
        self.assertFalse(
            observable_is_scheduler_deterministic(relation, (row,))
        )
        self.assertTrue(
            scalar_modular_scheduler_deterministic(relation, row, 2)
        )
        self.assertEqual(
            scalar_modular_terminal_outputs(relation, row, 2),
            (0,),
        )
        self.assertFalse(
            scalar_modular_scheduler_deterministic(relation, row, 4)
        )
        self.assertEqual(
            scalar_modular_terminal_outputs(relation, row, 4),
            (0, 2),
        )

    def test_repeated_modular_ambiguity_closure_has_gcd_phase_count(self):
        expected = {
            (0, 7): 1,
            (1, 7): 7,
            (2, 6): 3,
            (4, 6): 3,
            (6, 6): 1,
            (8, 12): 3,
        }
        for (grain, modulus), phases in expected.items():
            self.assertEqual(
                repeated_scalar_modular_ambiguity_phase_count(grain, modulus),
                phases,
            )

    def test_history_aware_v_has_applied_branch_but_committed_singleton(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(2),
            whole_queue=(0, 0),
        )
        witness = ((1, 1),)
        state = history_state_from_exact_applied_history(
            causal,
            (0, 0),
            witness,
            (0, 1),
        )
        tick = history_aware_causal_material_tick(
            state,
            ((1,), (1,)),
            witness,
            (0, 1),
        )
        report = history_scheduler_determinism_report(tick)
        self.assertEqual(report.terminal_count, 2)
        self.assertFalse(report.applied_history_scheduler_independent)
        self.assertTrue(report.committed_history_scheduler_independent)
        self.assertFalse(report.exact_queue_scheduler_independent)
        self.assertEqual(set(report.applied_history_values), {(1,), (2,)})
        self.assertEqual(set(report.committed_history_values), {(2,)})

    def test_history_aware_star_total_damage_is_applied_deterministic_even_though_queue_branches(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
                ContactChannel1D(0, 3, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(3),
            whole_queue=(0, 0, 0),
        )
        witness = ((1, 1, 1),)
        # The graph is a tree (star), so all history repair is body-derived.
        state = history_state_from_exact_applied_history(
            causal,
            (0, 0, 0),
            witness,
            (0, 1, 2),
        )
        tick = history_aware_causal_material_tick(
            state,
            ((1,), (1,), (1,)),
            witness,
            (0, 1, 2),
        )
        report = history_scheduler_determinism_report(tick)
        self.assertEqual(report.terminal_count, 3)
        self.assertTrue(report.applied_history_scheduler_independent)
        self.assertTrue(report.committed_history_scheduler_independent)
        self.assertFalse(report.exact_queue_scheduler_independent)
        self.assertEqual(report.applied_history_values, ((1,),))
        self.assertEqual(report.committed_history_values, ((3,),))

    def test_kernel_test_matches_direct_output_cardinality_over_small_relations(self):
        relations = (
            guarded_terminal_prefix_relation(
                (-1, -2),
                ((2, 1), (1, 2)),
                (1, 1),
            ),
            guarded_terminal_prefix_relation(
                (-1, -1),
                ((2, -1), (-1, 2)),
                (1, 1),
            ),
            guarded_terminal_prefix_relation(
                (-1, -1, -1),
                (
                    (2, 1, 1),
                    (1, 2, 1),
                    (1, 1, 2),
                ),
                (1, 1, 1),
            ),
        )
        for relation in relations:
            width = len(relation.target_counts)
            rows = tuple(
                row
                for row in __import__("itertools").product(range(-1, 2), repeat=width)
                if any(row)
            )
            for row in rows[: min(30, len(rows))]:
                direct = len(linear_terminal_output_relation(relation, (row,))) == 1
                self.assertEqual(
                    observable_is_scheduler_deterministic(relation, (row,)),
                    direct,
                )

    def test_validation(self):
        relation = guarded_terminal_prefix_relation(
            (-1, -2),
            ((2, 1), (1, 2)),
            (1, 1),
        )
        with self.assertRaises(ValueError):
            linear_terminal_output_relation(relation, ())
        with self.assertRaises(ValueError):
            scalar_scheduler_ambiguity_grain(relation, (1, 2, 3))
        with self.assertRaises(ValueError):
            scalar_modular_terminal_outputs(relation, (1, 1), 0)
        with self.assertRaises(ValueError):
            repeated_scalar_modular_ambiguity_phase_count(-1, 5)
        with self.assertRaises(TypeError):
            history_scheduler_determinism_report(object())


if __name__ == "__main__":
    unittest.main()
