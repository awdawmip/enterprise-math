import unittest

from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_p023_adapter import (
    compile_peak_material_p023_system,
    states_future_equivalent,
)
from enterprise_math.material_peak_memory import peak_conditioned_material_family
from enterprise_math.material_response import explicit_material_curve_profile


def profile(loading, returning, amplitude=100):
    return explicit_material_curve_profile(loading, returning, amplitude)


class MaterialP023AdapterTests(unittest.TestCase):
    def test_future_command_can_require_peak_even_when_current_response_matches(self):
        # At index 1 both peak classes currently return 20.  Command 2 keeps peak2
        # on profile2 but peak4 on profile4, revealing the hidden history.
        family = peak_conditioned_material_family(
            {
                2: profile(
                    (0, 20, 60, 80, 100),
                    (0, 20, 40, 60, 80),
                ),
                4: profile(
                    (0, 20, 30, 50, 70),
                    (0, 20, 25, 40, 60),
                ),
            }
        )
        system = compile_peak_material_p023_system(family, (0, 1, 2, 4))
        left = (1, RETURNING, 2)
        right = (1, RETURNING, 4)
        self.assertEqual(system.initial_partition[left], system.initial_partition[right])
        self.assertFalse(states_future_equivalent(system, left, right))
        self.assertGreaterEqual(system.stable_class_count, system.initial_class_count)

    def test_common_higher_peak_command_can_make_old_peak_future_irrelevant(self):
        family = peak_conditioned_material_family(
            {
                2: profile(
                    (0, 20, 60, 80, 100),
                    (0, 20, 40, 60, 80),
                ),
                4: profile(
                    (0, 20, 30, 50, 70),
                    (0, 20, 25, 40, 60),
                ),
            }
        )
        # With only command 4, both histories jump into the same peak4 LOADING state.
        system = compile_peak_material_p023_system(family, (4,))
        left = (1, RETURNING, 2)
        right = (1, RETURNING, 4)
        self.assertEqual(system.initial_partition[left], system.initial_partition[right])
        self.assertTrue(states_future_equivalent(system, left, right))

    def test_declaring_peak_observable_prevents_merge_by_definition(self):
        common = profile(
            (0, 20, 40, 60, 80),
            (0, 10, 20, 30, 40),
        )
        family = peak_conditioned_material_family({2: common, 4: common})
        response_only = compile_peak_material_p023_system(family, (4,))
        peak_visible = compile_peak_material_p023_system(
            family,
            (4,),
            include_peak_observation=True,
        )
        left = (1, LOADING, 2)
        right = (1, LOADING, 4)
        self.assertTrue(states_future_equivalent(response_only, left, right))
        self.assertFalse(states_future_equivalent(peak_visible, left, right))

    def test_branch_observable_can_be_stricter_than_response_only(self):
        common = profile(
            (0, 20, 40, 60, 80),
            (0, 20, 40, 60, 80),
        )
        family = peak_conditioned_material_family({2: common, 4: common})
        # Command 4 overwrites both branch and peak, so response-only can merge
        # current LOADING/RETURNING states at one geometry index.
        response_only = compile_peak_material_p023_system(family, (4,))
        branch_visible = compile_peak_material_p023_system(
            family,
            (4,),
            include_branch_observation=True,
        )
        left = (1, LOADING, 2)
        right = (1, RETURNING, 2)
        self.assertTrue(states_future_equivalent(response_only, left, right))
        self.assertFalse(states_future_equivalent(branch_visible, left, right))

    def test_missing_intermediate_peak_class_makes_command_non_total_instead_of_interpolating(self):
        common = profile(
            (0, 20, 40, 60, 80),
            (0, 10, 20, 30, 40),
        )
        family = peak_conditioned_material_family({2: common, 4: common})
        with self.assertRaises(ValueError):
            compile_peak_material_p023_system(family, (3,))

    def test_full_peak_family_supports_all_absolute_deformation_commands(self):
        profiles = {
            peak: profile(
                tuple(10 * index for index in range(5)),
                tuple(5 * index for index in range(5)),
            )
            for peak in range(5)
        }
        family = peak_conditioned_material_family(profiles)
        system = compile_peak_material_p023_system(family, tuple(range(5)))
        self.assertEqual(system.command_indices, (0, 1, 2, 3, 4))
        self.assertTrue(system.stable_class_count >= 1)


if __name__ == "__main__":
    unittest.main()
