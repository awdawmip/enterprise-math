import unittest

from enterprise_math.euler_o2_chirality_globalization import (
    EDGES,
    TRIANGLES,
    all_edge_cochains,
    all_triangle_holonomies,
    coboundary,
    exhaustive_certificate,
    gauge_orbit,
    gauge_transform,
    global_trivializations,
    independent_holonomies,
    inversion_fixed_phases,
    is_half_turn_central,
    is_trivial_chirality_class,
    o2_inverse,
    o2_multiply,
    permutation_parity,
    transport_phase,
)


class EulerO2ChiralityGlobalizationTests(unittest.TestCase):
    def test_k4_inventory(self) -> None:
        self.assertEqual(len(EDGES), 6)
        self.assertEqual(len(TRIANGLES), 4)
        self.assertEqual(len(tuple(all_edge_cochains())), 64)

    def test_triangle_holonomy_is_gauge_invariant(self) -> None:
        for epsilon in all_edge_cochains():
            before = independent_holonomies(epsilon)
            for mask in range(16):
                sigma = tuple((mask >> index) & 1 for index in range(4))
                self.assertEqual(
                    independent_holonomies(gauge_transform(epsilon, sigma)),
                    before,
                )

    def test_fourth_triangle_is_dependent(self) -> None:
        for epsilon in all_edge_cochains():
            h0, h1, h2, h3 = all_triangle_holonomies(epsilon)
            self.assertEqual(h3, h0 ^ h1 ^ h2)

    def test_holonomies_classify_gauge_orbits(self) -> None:
        cochains = tuple(all_edge_cochains())
        for left in cochains:
            orbit = gauge_orbit(left)
            self.assertEqual(len(orbit), 8)
            for right in cochains:
                self.assertEqual(
                    right in orbit,
                    independent_holonomies(right) == independent_holonomies(left),
                )

    def test_global_signed_chirality_is_a_two_element_torsor(self) -> None:
        for epsilon in all_edge_cochains():
            solutions = global_trivializations(epsilon)
            if is_trivial_chirality_class(epsilon):
                self.assertEqual(len(solutions), 2)
                first, second = solutions
                self.assertEqual(tuple(bit ^ 1 for bit in first), second)
                self.assertEqual(coboundary(first), epsilon)
                self.assertEqual(coboundary(second), epsilon)
            else:
                self.assertEqual(solutions, ())

    def test_tetrahedral_orientation_has_no_full_s4_fixed_choice(self) -> None:
        even = odd = 0
        from itertools import permutations

        for permutation in permutations(range(4)):
            if permutation_parity(permutation):
                odd += 1
            else:
                even += 1
        self.assertEqual((even, odd), (12, 12))

    def test_only_identity_and_half_turn_forget_chirality(self) -> None:
        for modulus in (6, 12, 24, 48, 96):
            self.assertEqual(inversion_fixed_phases(modulus), (0, modulus // 2))
            for flip in (0, 1):
                self.assertEqual(transport_phase(0, modulus, flip), 0)
                self.assertEqual(
                    transport_phase(modulus // 2, modulus, flip),
                    modulus // 2,
                )
            quarter = modulus // 4 if modulus % 4 == 0 else None
            if quarter is not None:
                self.assertNotEqual(
                    transport_phase(quarter, modulus, 1),
                    quarter,
                )

    def test_finite_o2_group_and_central_half_turn(self) -> None:
        for modulus in (6, 12, 24):
            identity = (0, 0)
            states = [(angle, flip) for angle in range(modulus) for flip in (0, 1)]
            self.assertTrue(is_half_turn_central(modulus))
            for state in states:
                inverse = o2_inverse(state, modulus)
                self.assertEqual(o2_multiply(state, inverse, modulus), identity)
                self.assertEqual(o2_multiply(inverse, state, modulus), identity)
                self.assertEqual(o2_multiply(identity, state, modulus), state)
                self.assertEqual(o2_multiply(state, identity, modulus), state)

    def test_exhaustive_certificate(self) -> None:
        certificate = exhaustive_certificate()
        self.assertEqual(certificate["edge_cochains"], 64)
        self.assertEqual(certificate["gauge_classes"], 8)
        self.assertEqual(certificate["trivial_holonomy_cochains"], 8)
        self.assertEqual(certificate["global_orientation_torsor_size"], 2)
        self.assertEqual(certificate["global_euler_fixed_phases"], "identity and half-turn")


if __name__ == "__main__":
    unittest.main()
