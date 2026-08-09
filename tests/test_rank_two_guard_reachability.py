import itertools
import unittest

from enterprise_math.rank_two_guard_reachability import (
    rank_two_basis_coordinates,
    rank_two_lattice_basis,
    rank_two_threshold_pattern_face_bound,
    rank_two_threshold_pattern_reachable,
    rank_two_threshold_pattern_witness,
)


class RankTwoGuardReachabilityTests(unittest.TestCase):
    def test_rank_two_basis_exactly_spans_redundant_generator_family(self):
        generators = (
            (4, 6, 2),
            (6, 9, 3),
            (2, 3, 1),
            (1, 1, 0),
        )
        basis = rank_two_lattice_basis(generators)
        self.assertEqual(basis, ((1, 0, -1), (0, 1, 1)))
        for generator in generators:
            coordinates = rank_two_basis_coordinates(generator, basis)
            self.assertIsNotNone(coordinates)
            first, second = coordinates
            self.assertEqual(
                tuple(
                    first * basis[0][index] + second * basis[1][index]
                    for index in range(3)
                ),
                generator,
            )

    def test_rank_two_basis_accepts_arbitrary_original_integer_combinations(self):
        generators = (
            (2, 0, 1, -1),
            (0, 2, 1, 1),
            (2, 2, 2, 0),
            (-2, 2, 0, 2),
        )
        basis = rank_two_lattice_basis(generators)
        for coefficients in itertools.product(range(-3, 4), repeat=len(generators)):
            vector = tuple(
                sum(
                    coefficient * generator[index]
                    for coefficient, generator in zip(coefficients, generators)
                )
                for index in range(4)
            )
            self.assertIsNotNone(
                rank_two_basis_coordinates(vector, basis),
                msg=(coefficients, vector, basis),
            )

    def test_strict_recession_certificate_returns_pattern_witness(self):
        generators = ((-2, -2, -2), (-2, -2, -1))
        base = (-2, -2, -2)
        pattern = (False, False, False)
        witness = rank_two_threshold_pattern_witness(base, generators, pattern)
        self.assertIsNotNone(witness)
        self.assertEqual(witness.certificate_mode, "strict_recession")
        self.assertTrue(all(score < 0 for score in witness.scores))

    def test_one_dimensional_recession_certificate_handles_reachable_case(self):
        generators = ((-2, -2, -2), (-2, -2, -1))
        base = (-2, 0, -2)
        pattern = (False, True, False)
        witness = rank_two_threshold_pattern_witness(base, generators, pattern)
        self.assertIsNotNone(witness)
        self.assertEqual(witness.certificate_mode, "recession_ray_or_line")
        self.assertTrue(witness.scores[1] >= 0)
        self.assertTrue(witness.scores[0] < 0 and witness.scores[2] < 0)

    def test_one_dimensional_recession_can_prove_unreachable_pattern(self):
        generators = ((-2, -2, -2), (-2, -2, -1))
        base = (-2, -2, -2)
        pattern = (False, True, False)
        self.assertFalse(
            rank_two_threshold_pattern_reachable(base, generators, pattern)
        )

    def test_bounded_polygon_certificate_returns_finite_scan_width(self):
        generators = ((-2, -2, -2), (-2, -1, 0))
        base = (-2, -2, 0)
        pattern = (True, False, True)
        witness = rank_two_threshold_pattern_witness(base, generators, pattern)
        self.assertIsNotNone(witness)
        self.assertEqual(witness.certificate_mode, "bounded_scan")
        self.assertIsNotNone(witness.bounded_scan_width)
        self.assertGreaterEqual(witness.bounded_scan_width, 1)
        self.assertTrue(witness.scores[0] >= 0)
        self.assertTrue(witness.scores[1] < 0)
        self.assertTrue(witness.scores[2] >= 0)

    def test_bounded_real_region_can_have_no_integer_lattice_witness(self):
        generators = ((-2, -2, -2), (-2, -1, 0))
        base = (-2, -1, -2)
        pattern = (False, True, False)
        self.assertFalse(
            rank_two_threshold_pattern_reachable(base, generators, pattern)
        )

    def test_face_bound_is_quadratic_in_nonconstant_guard_count(self):
        generators = (
            (1, 0, 1, -1, 2, 0),
            (0, 1, 1, 1, -1, 0),
        )
        # Five nonconstant threshold lines and one constant guard.
        self.assertEqual(rank_two_threshold_pattern_face_bound(generators), 51)
        self.assertLess(51, 2 ** 6)

    def test_actual_reachable_pattern_count_respects_face_bound(self):
        generators = (
            (1, 0, 1, -1, 2),
            (0, 1, 1, 1, -1),
        )
        base = (0, 0, 0, 0, 0)
        reachable = {
            pattern
            for pattern in itertools.product((False, True), repeat=5)
            if rank_two_threshold_pattern_reachable(base, generators, pattern)
        }
        self.assertLessEqual(
            len(reachable),
            rank_two_threshold_pattern_face_bound(generators),
        )

    def test_closed_solver_matches_bounded_parameter_enumeration_on_small_cases(self):
        generator_families = (
            ((1, 0, 1), (0, 1, 1)),
            ((2, 0, -2), (0, 1, 2)),
            ((2, 2, 0), (0, 0, 1)),
            ((1, -1, 0, 1), (0, 1, -1, 1)),
        )
        for generators in generator_families:
            dimension = len(generators[0])
            basis = rank_two_lattice_basis(generators)
            for base in itertools.product(range(-2, 3), repeat=dimension):
                for pattern in itertools.product((False, True), repeat=dimension):
                    exact = rank_two_threshold_pattern_reachable(
                        base, generators, pattern
                    )
                    brute = False
                    for first in range(-18, 19):
                        for second in range(-18, 19):
                            scores = tuple(
                                base[index]
                                + first * basis[0][index]
                                + second * basis[1][index]
                                for index in range(dimension)
                            )
                            if all(
                                (score >= 0) if wants_true else (score < 0)
                                for score, wants_true in zip(scores, pattern)
                            ):
                                brute = True
                                break
                        if brute:
                            break
                    if brute:
                        self.assertTrue(exact, msg=(generators, base, pattern))
                    if not exact:
                        self.assertFalse(brute, msg=(generators, base, pattern))


if __name__ == "__main__":
    unittest.main()
