import itertools
import unittest

from enterprise_math.action_language_precision import (
    action_grain,
    boundary_orbit_equivalent,
    cyclic_gcd_subgroup,
    cyclic_reachable_residues,
    future_observation_signature,
    group_completed_window_class_count,
    group_completion_overrefinement_defect,
    numerical_semigroup_profile,
    one_sided_threshold_rank,
    one_sided_window_class_count,
    positive_semigroup_below,
    reachable_boundary_cuts,
    reachable_translations,
    relevant_semigroup_holes,
    signed_group_completion_grain,
    threshold_group_coordinate,
    translate_group_coordinate,
)


class ActionLanguagePrecisionTests(unittest.TestCase):
    def test_boundary_orbit_matches_future_signatures(self):
        boundary_sets = ((0,), (-2, 1), (-3, 0, 4))
        action_sets = ((1,), (1, 2), (-1, 2), (-2, 3))
        for boundaries in boundary_sets:
            for actions in action_sets:
                for horizon in range(4):
                    cuts = reachable_boundary_cuts(boundaries, actions, horizon)
                    self.assertTrue(set(boundaries).issubset(set(cuts)))
                    for left in range(-8, 8):
                        for right in range(-8, 8):
                            direct = (
                                future_observation_signature(
                                    left, boundaries, actions, horizon
                                )
                                == future_observation_signature(
                                    right, boundaries, actions, horizon
                                )
                            )
                            self.assertEqual(
                                boundary_orbit_equivalent(
                                    left, right, boundaries, actions, horizon
                                ),
                                direct,
                            )

    def test_one_sided_window_count_matches_direct_signatures(self):
        action_sets = (
            (1,),
            (2,),
            (2, 3),
            (4, 6),
            (4, 7),
            (6, 9, 20),
        )
        threshold = 0
        for actions in action_sets:
            for horizon in range(5):
                translations = reachable_translations(actions, horizon)
                for width in range(1, 18):
                    signatures = {
                        tuple(int(value + total < threshold) for total in translations)
                        for value in range(threshold - width, threshold)
                    }
                    self.assertEqual(
                        len(signatures),
                        one_sided_window_class_count(width, actions, horizon),
                    )

    def test_stable_one_sided_count_and_rank(self):
        for actions in ((2,), (2, 3), (4, 6), (5, 7, 9)):
            for width in range(1, 25):
                reached = positive_semigroup_below(actions, width)
                self.assertEqual(
                    one_sided_window_class_count(width, actions),
                    1 + len([value for value in reached if value > 0]),
                )
                for distance in range(1, width + 1):
                    expected = len(
                        [value for value in reached if 0 < value < distance]
                    )
                    self.assertEqual(
                        one_sided_threshold_rank(distance, actions),
                        expected,
                    )

    def test_gcd_overrefinement_defect_is_exact_hole_count(self):
        for actions in ((4, 6), (6, 10), (6, 9, 20), (5, 7)):
            grain = action_grain(actions)
            for width in range(1, 30):
                minimal = one_sided_window_class_count(width, actions)
                uniform = group_completed_window_class_count(width, actions)
                holes = relevant_semigroup_holes(width, actions)
                self.assertEqual(uniform - minimal, len(holes))
                self.assertEqual(
                    group_completion_overrefinement_defect(width, actions),
                    len(holes),
                )
                self.assertTrue(all(hole % grain == 0 for hole in holes))

    def test_minimal_semigroup_hole_counterexample(self):
        actions = (4, 6)
        width = 7
        self.assertEqual(action_grain(actions), 2)
        self.assertEqual(positive_semigroup_below(actions, width), (0, 4, 6))
        self.assertEqual(one_sided_window_class_count(width, actions), 3)
        self.assertEqual(group_completed_window_class_count(width, actions), 4)
        self.assertEqual(relevant_semigroup_holes(width, actions), (2,))
        self.assertEqual(group_completion_overrefinement_defect(width, actions), 1)

    def test_conductor_localizes_all_semigroup_holes(self):
        for actions in ((4, 6), (6, 10), (6, 9, 20), (5, 7), (7, 9, 11)):
            profile = numerical_semigroup_profile(actions)
            normalized = profile.normalized_generators
            self.assertEqual(action_grain(normalized), 1)
            cutoff = profile.physical_irregular_depth + 10 * profile.grain + 1
            reached = set(positive_semigroup_below(actions, cutoff))
            for value in range(
                profile.physical_irregular_depth,
                cutoff,
                profile.grain,
            ):
                self.assertIn(value, reached)
            self.assertTrue(
                all(
                    hole < profile.physical_irregular_depth
                    for hole in relevant_semigroup_holes(cutoff, actions)
                )
            )
        profile = numerical_semigroup_profile((4, 6))
        self.assertEqual(profile.grain, 2)
        self.assertEqual(profile.normalized_generators, (2, 3))
        self.assertEqual(profile.conductor, 2)
        self.assertEqual(profile.physical_irregular_depth, 4)

    def test_two_sided_group_coordinate_transport(self):
        for actions in ((6, -10), (9, -15), (4, -6, 10)):
            grain = signed_group_completion_grain(actions)
            for threshold in (-3, 0, 7):
                for value in range(-20, 21):
                    coordinate = threshold_group_coordinate(
                        value, threshold, grain
                    )
                    self.assertEqual(value < threshold, coordinate >= 1)
                    for action in actions:
                        self.assertEqual(
                            threshold_group_coordinate(
                                value + action, threshold, grain
                            ),
                            translate_group_coordinate(
                                coordinate, action, grain
                            ),
                        )

    def test_cyclic_one_sided_monoid_is_gcd_subgroup(self):
        action_sets = (
            (),
            (6,),
            (4, 6),
            (-4,),
            (6, 10, 15),
        )
        for width in range(1, 21):
            for actions in action_sets:
                self.assertEqual(
                    cyclic_reachable_residues(width, actions),
                    cyclic_gcd_subgroup(width, actions),
                )

    def test_exhaustive_small_cyclic_families(self):
        for width in range(1, 13):
            pool = range(-4, 5)
            for size in (1, 2):
                for actions in itertools.combinations_with_replacement(pool, size):
                    self.assertEqual(
                        cyclic_reachable_residues(width, actions),
                        cyclic_gcd_subgroup(width, actions),
                    )

    def test_chain_cycle_dichotomy_example(self):
        actions = (6,)
        self.assertEqual(one_sided_window_class_count(15, actions), 3)
        self.assertEqual(cyclic_reachable_residues(15, actions), (0, 3, 6, 9, 12))
        self.assertEqual(len(cyclic_gcd_subgroup(15, actions)), 5)


if __name__ == "__main__":
    unittest.main()
