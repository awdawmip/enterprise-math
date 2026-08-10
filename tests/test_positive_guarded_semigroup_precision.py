import unittest

from enterprise_math.action_language_precision import (
    numerical_semigroup_profile,
    reachable_translations,
)
from enterprise_math.guarded_translation_precision import (
    guarded_reachable_boundary_cuts,
)
from enterprise_math.positive_guarded_semigroup_precision import (
    positive_guarded_base_cuts,
    positive_guarded_boundary_cuts_closed_form,
    positive_guarded_closed_form_agrees_with_profile_compiler,
    positive_guarded_infinite_cut_membership,
    positive_guarded_semigroup_tail,
    positive_semigroup_contains,
)


class PositiveGuardedSemigroupPrecisionTests(unittest.TestCase):
    def test_closed_form_matches_general_profile_compiler_exhaustively_small(self):
        action_sets = ((1,), (1, 2), (2, 3), (1, 3, 5))
        boundary_sets = ((), (0,), (-2, 1), (0, 4))
        checked = 0
        for actions in action_sets:
            for boundaries in boundary_sets:
                for guard in (-2, 0, 3):
                    for horizon in range(6):
                        self.assertTrue(
                            positive_guarded_closed_form_agrees_with_profile_compiler(
                                boundaries, actions, guard, horizon
                            )
                        )
                        self.assertEqual(
                            positive_guarded_boundary_cuts_closed_form(
                                boundaries, actions, guard, horizon
                            ),
                            guarded_reachable_boundary_cuts(
                                boundaries, actions, guard, horizon
                            ),
                        )
                        checked += 1
        self.assertGreater(checked, 200)

    def test_one_step_compiled_base_formula(self):
        boundaries = (0, 5)
        actions = (1, 3)
        guard = 2
        # g plus b-a that remain below g:
        # 0-1=-1, 0-3=-3, 5-3=2 is masked at the guard, 5-1=4 is above it.
        self.assertEqual(
            positive_guarded_base_cuts(boundaries, actions, guard),
            (-3, -1, 2),
        )
        self.assertEqual(
            positive_guarded_boundary_cuts_closed_form(
                boundaries, actions, guard, 1
            ),
            (-3, -1, 0, 2, 5),
        )

    def test_horizon_is_canonical_prefix_semigroup_orbit_after_compilation(self):
        boundaries = (-1, 4)
        actions = (2, 5)
        guard = 3
        bases = positive_guarded_base_cuts(boundaries, actions, guard)
        for horizon in range(1, 7):
            prefixes = reachable_translations(actions, horizon - 1)
            expected = set(boundaries)
            expected.update(
                base - prefix
                for base in bases
                for prefix in prefixes
            )
            self.assertEqual(
                positive_guarded_boundary_cuts_closed_form(
                    boundaries, actions, guard, horizon
                ),
                tuple(sorted(expected)),
            )

    def test_semigroup_membership_matches_bounded_reachability_when_bound_is_sufficient(self):
        for actions in ((2, 3), (4, 6), (3, 5), (6, 10, 14)):
            reached = set(reachable_translations(actions, 30))
            for total in range(80):
                self.assertEqual(
                    positive_semigroup_contains(total, actions),
                    total in reached,
                )

    def test_infinite_guarded_membership_matches_large_finite_orbit_on_bounded_window(self):
        cases = (
            ((2, 3), (0,), 1),
            ((4, 6), (-1, 5), 2),
            ((3, 5), (), -2),
        )
        for actions, boundaries, guard in cases:
            large = set(
                positive_guarded_boundary_cuts_closed_form(
                    boundaries, actions, guard, 40
                )
            )
            for cut in range(-60, 15):
                self.assertEqual(
                    positive_guarded_infinite_cut_membership(
                        cut, boundaries, actions, guard
                    ),
                    cut in large,
                )

    def test_conductor_controls_complete_tail_in_each_compiled_residue(self):
        cases = (
            ((4, 6), (-1, 5), 2),
            ((6, 10, 14), (0, 9), 4),
            ((3, 5), (), -2),
        )
        for actions, boundaries, guard in cases:
            tail = positive_guarded_semigroup_tail(
                boundaries, actions, guard
            )
            canonical = numerical_semigroup_profile(actions)
            self.assertEqual(tail.grain, canonical.grain)
            self.assertEqual(
                tail.normalized_conductor,
                canonical.conductor,
            )
            self.assertEqual(
                tail.physical_irregular_depth,
                canonical.physical_irregular_depth,
            )
            for residue in tail.residues:
                self.assertEqual(
                    residue.complete_below,
                    residue.anchor - tail.physical_irregular_depth,
                )
                for cut in range(
                    residue.complete_below - 8 * tail.grain,
                    residue.complete_below + 1,
                    tail.grain,
                ):
                    self.assertEqual(cut % tail.grain, residue.residue)
                    self.assertTrue(
                        positive_guarded_infinite_cut_membership(
                            cut, boundaries, actions, guard
                        )
                    )

    def test_compiled_generated_tail_has_no_new_residue_classes(self):
        actions = (6, 10)
        boundaries = (1, 8)
        guard = 4
        tail = positive_guarded_semigroup_tail(boundaries, actions, guard)
        represented = {entry.residue for entry in tail.residues}
        bases = tail.compiled_base_cuts
        for base in bases:
            for prefix in reachable_translations(actions, 20):
                self.assertIn((base - prefix) % tail.grain, represented)

    def test_empty_terminal_observation_still_has_guard_semigroup_tail(self):
        actions = (4, 6)
        guard = 3
        self.assertEqual(
            positive_guarded_base_cuts((), actions, guard),
            (guard,),
        )
        for horizon in range(1, 6):
            expected = tuple(
                sorted(
                    guard - prefix
                    for prefix in reachable_translations(
                        actions, horizon - 1
                    )
                )
            )
            self.assertEqual(
                positive_guarded_boundary_cuts_closed_form(
                    (), actions, guard, horizon
                ),
                expected,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            positive_guarded_base_cuts((), (), 0)
        with self.assertRaises(ValueError):
            positive_guarded_base_cuts((), (0, 1), 0)
        with self.assertRaises(ValueError):
            positive_guarded_base_cuts((), (-1, 2), 0)
        with self.assertRaises(TypeError):
            positive_guarded_base_cuts((), (1,), False)
        with self.assertRaises(ValueError):
            positive_guarded_boundary_cuts_closed_form(
                (), (1,), 0, -1
            )
        with self.assertRaises(TypeError):
            positive_semigroup_contains(True, (1, 2))


if __name__ == "__main__":
    unittest.main()
