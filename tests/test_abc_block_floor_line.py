import unittest

from enterprise_math.abc_absorption_access import absorption_optimal_radius
from enterprise_math.abc_block_floor_line import (
    block_value_floor_line,
    block_value_lattice_basis,
    exact_absorption_floor_access,
)


class AbcBlockFloorLineTests(unittest.TestCase):
    def test_235_hnf_basis_and_floor_line(self) -> None:
        self.assertEqual(block_value_lattice_basis(2, 3, 5), ((1, 0), (0, 1)))
        line = block_value_floor_line(2, 3, 5)
        self.assertEqual(line.basis_wronskians, (-3, 2))
        self.assertEqual(line.wronskian_generator, 1)
        self.assertEqual(line.particular_floor_point, (1, 2))
        self.assertEqual(line.kernel_direction, (2, 3))

        solution = exact_absorption_floor_access(2, 3, 5)
        self.assertEqual(solution.nu, 2)
        self.assertEqual(solution.absorption_floor, 1)
        self.assertEqual(solution.nu, absorption_optimal_radius(2, 3, 5))

    def test_279_floor_line_recovers_nu_five(self) -> None:
        self.assertEqual(block_value_lattice_basis(2, 7, 9), ((6, 0), (5, 1)))
        line = block_value_floor_line(2, 7, 9)
        self.assertEqual(line.basis_wronskians, (-42, -33))
        self.assertEqual(line.wronskian_generator, 3)
        self.assertEqual(line.particular_floor_point, (1, 5))
        self.assertEqual(line.kernel_direction, (4, 14))

        solution = exact_absorption_floor_access(2, 7, 9)
        self.assertEqual(solution.derivative_values, (1, 5, 6))
        self.assertEqual(solution.nu, 5)
        self.assertEqual(solution.absorption_floor, 1)
        self.assertEqual(solution.nu, absorption_optimal_radius(2, 7, 9, max_bound=6))

    def test_irreducible_overhead_floor_line(self) -> None:
        line = block_value_floor_line(5, 7, 12)
        self.assertEqual(line.basis, ((4, 0), (3, 1)))
        self.assertEqual(line.wronskian_generator, 4)
        self.assertEqual(line.particular_floor_point, (-2, -2))
        self.assertEqual(line.kernel_direction, (5, 7))

        solution = exact_absorption_floor_access(5, 7, 12)
        self.assertEqual(solution.nu, 2)
        self.assertEqual(solution.absorption_floor, 2)

    def test_unit_relations_are_rank_one_floor_points(self) -> None:
        first = block_value_floor_line(1, 8, 9)
        self.assertEqual(first.basis, ((0, 12),))
        self.assertIsNone(first.kernel_direction)
        self.assertEqual(first.particular_floor_point, (0, 12))
        self.assertEqual(exact_absorption_floor_access(1, 8, 9).nu, 2)

        second = exact_absorption_floor_access(1, 242, 243)
        self.assertEqual(second.derivative_values, (0, 4455, 4455))
        self.assertEqual(second.block_radii, (0, 27, 11))
        self.assertEqual(second.nu, 27)
        self.assertEqual(second.absorption_floor, 5)

        third = exact_absorption_floor_access(1, 512, 513)
        self.assertEqual(third.nu, 13)
        self.assertEqual(third.absorption_floor, 3)

    def test_arbitrary_support_solver_avoids_fine_cube_enumeration(self) -> None:
        # Four prime coordinates across the three blocks; the exact solver searches
        # only the one-dimensional compressed floor line.
        solution = exact_absorption_floor_access(25, 704, 729)
        self.assertEqual(solution.derivative_values, (-20, 8768, 8748))
        self.assertEqual(solution.nu, 6)
        self.assertEqual(solution.absorption_floor, 6)
        self.assertIsNotNone(solution.searched_parameter_interval)

    def test_more_small_floor_access_values(self) -> None:
        self.assertEqual(exact_absorption_floor_access(4, 5, 9).nu, 2)
        self.assertEqual(exact_absorption_floor_access(5, 27, 32).nu, 3)
        self.assertEqual(exact_absorption_floor_access(14, 15, 29).nu, 3)


if __name__ == "__main__":
    unittest.main()
