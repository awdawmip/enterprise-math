import unittest
from itertools import product

from enterprise_math.causal_modular_generation import (
    apply_event_program,
    fixed_m_body_event,
    modular_displacement_allowed,
    modular_generation_is_exact,
    modular_generation_program,
)


class CausalModularGenerationTests(unittest.TestCase):
    def test_fixed_bridge_event_changes_total_by_exact_modulus(self):
        self.assertEqual(sum(fixed_m_body_event(6, 4, 1)), 4)
        self.assertEqual(sum(fixed_m_body_event(6, 4, -1)), -4)

    def test_constructive_program_generates_many_small_modular_displacements(self):
        modulus = 3
        for displacement in product(range(-2, 3), repeat=4):
            if not modular_displacement_allowed(displacement, modulus):
                continue
            self.assertTrue(modular_generation_is_exact(displacement, modulus))
            program = modular_generation_program(displacement, modulus)
            self.assertEqual(apply_event_program(4, program), displacement)

    def test_support_two_transfer_world_cannot_cross_exact_total_but_m_body_event_can(self):
        displacement = (1, 1, 1, 0)
        self.assertEqual(sum(displacement), 3)
        self.assertTrue(modular_generation_is_exact(displacement, 3))
        program = modular_generation_program(displacement, 3)
        self.assertEqual(len(program), 1)
        self.assertEqual(program[0], displacement)

    def test_illegal_total_change_is_rejected(self):
        with self.assertRaises(ValueError):
            modular_generation_program((1, 1, 0, 0), 3)


if __name__ == "__main__":
    unittest.main()
