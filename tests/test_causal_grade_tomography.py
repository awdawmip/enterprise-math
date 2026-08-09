import unittest

from enterprise_math.causal_conservation_tomography import (
    exact_total_law,
    modular_total_law,
    unit_amplitude_events,
)
from enterprise_math.causal_grade_tomography import (
    first_grade_difference,
    graded_shell_histogram,
    primitive_grade,
    primitive_shell,
    visible_events,
)


def support_grade(event):
    return sum(value != 0 for value in event)


class CausalGradeTomographyTests(unittest.TestCase):
    def test_exact_and_mod_m_share_a_primitive_shell_then_split_at_grade_m(self):
        for modulus in range(3, 7):
            slots = modulus + 1
            universe = unit_amplitude_events(slots)
            exact_shell = primitive_shell(universe, exact_total_law, support_grade)
            modular_shell = primitive_shell(universe, modular_total_law(modulus), support_grade)
            self.assertEqual(primitive_grade(universe, exact_total_law, support_grade), 2)
            self.assertEqual(primitive_grade(universe, modular_total_law(modulus), support_grade), 2)
            self.assertEqual(exact_shell, modular_shell)
            self.assertEqual(
                first_grade_difference(
                    universe,
                    exact_total_law,
                    support_grade,
                    modular_total_law(modulus),
                    support_grade,
                    maximum_budget=slots,
                ),
                modulus,
            )

    def test_grade_budget_is_nested_and_primitive_geometry_is_first_nonempty_cut(self):
        slots = 5
        universe = unit_amplitude_events(slots)
        law = modular_total_law(4)
        previous = frozenset()
        for budget in range(0, slots + 1):
            current = visible_events(universe, law, support_grade, budget)
            self.assertTrue(previous <= current)
            previous = current
        self.assertEqual(
            visible_events(universe, law, support_grade, 2),
            primitive_shell(universe, law, support_grade),
        )

    def test_shell_histogram_retains_higher_causal_channels_beyond_geometry(self):
        slots = 5
        universe = unit_amplitude_events(slots)
        exact = graded_shell_histogram(universe, exact_total_law, support_grade)
        mod4 = graded_shell_histogram(universe, modular_total_law(4), support_grade)
        self.assertEqual(exact[2], mod4[2])
        self.assertNotEqual(exact.get(4, 0), mod4.get(4, 0))


if __name__ == "__main__":
    unittest.main()
