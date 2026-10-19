import unittest
from itertools import product

from enterprise_math.euler_atlas_orientation import (
    EDGES,
    IDENTITY4,
    ODD_GAUGE4,
    all_permutations4,
    apply_vertex_relabeling,
    atlas_orientation_certificate,
    fourth_triangle_holonomy,
    gauges_clearing,
    orientation_class_count,
    parity_bit,
    reduce_transitions_to_a4,
    reduction_gauge,
    transition_parity_bits,
    triangle_holonomies,
    vertex_gauge,
)


class EulerAtlasOrientationTests(unittest.TestCase):
    def test_h1_has_eight_classes_of_eight_patterns(self) -> None:
        self.assertEqual(orientation_class_count(), 8)
        classes = {}
        for bits in product((0, 1), repeat=6):
            classes.setdefault(triangle_holonomies(bits), []).append(bits)
        self.assertEqual(len(classes), 8)
        self.assertTrue(all(len(items) == 8 for items in classes.values()))

    def test_triangle_holonomies_are_gauge_invariant(self) -> None:
        for bits in product((0, 1), repeat=6):
            invariant = triangle_holonomies(bits)
            for gauge in product((0, 1), repeat=4):
                self.assertEqual(
                    triangle_holonomies(vertex_gauge(bits, gauge)),
                    invariant,
                )

    def test_constructive_flattening_criterion(self) -> None:
        flat = 0
        nonflat = 0
        for bits in product((0, 1), repeat=6):
            gauge = reduction_gauge(bits)
            if triangle_holonomies(bits) == (0, 0, 0):
                flat += 1
                self.assertIsNotNone(gauge)
                assert gauge is not None
                self.assertEqual(vertex_gauge(bits, gauge), (0, 0, 0, 0, 0, 0))
            else:
                nonflat += 1
                self.assertIsNone(gauge)
        self.assertEqual((flat, nonflat), (8, 56))

    def test_flat_gauge_unique_up_to_global_reversal(self) -> None:
        for bits in product((0, 1), repeat=6):
            if triangle_holonomies(bits) != (0, 0, 0):
                continue
            clearers = gauges_clearing(bits)
            self.assertEqual(len(clearers), 2)
            self.assertEqual(clearers[1], tuple(bit ^ 1 for bit in clearers[0]))

    def test_fourth_triangle_is_dependent(self) -> None:
        for bits in product((0, 1), repeat=6):
            first, second, third = triangle_holonomies(bits)
            self.assertEqual(
                fourth_triangle_holonomy(bits),
                first ^ second ^ third,
            )

    def test_s4_transition_reduction_to_a4(self) -> None:
        for bits in product((0, 1), repeat=6):
            transitions = {
                edge: (ODD_GAUGE4 if bit else IDENTITY4)
                for edge, bit in zip(EDGES, bits)
            }
            self.assertEqual(transition_parity_bits(transitions), bits)
            reduced = reduce_transitions_to_a4(transitions)
            if triangle_holonomies(bits) == (0, 0, 0):
                self.assertIsNotNone(reduced)
                assert reduced is not None
                adjusted, gauge = reduced
                self.assertEqual(transition_parity_bits(adjusted), (0, 0, 0, 0, 0, 0))
                self.assertEqual(
                    transition_parity_bits(apply_vertex_relabeling(transitions, gauge)),
                    (0, 0, 0, 0, 0, 0),
                )
            else:
                self.assertIsNone(reduced)

    def test_s4_parity_split(self) -> None:
        permutations = all_permutations4()
        self.assertEqual(len(permutations), 24)
        self.assertEqual(sum(parity_bit(item) == 0 for item in permutations), 12)
        self.assertEqual(sum(parity_bit(item) == 1 for item in permutations), 12)

    def test_complete_certificate(self) -> None:
        certificate = atlas_orientation_certificate()
        self.assertEqual(certificate["status"], "PASS")
        self.assertEqual(certificate["orientation_classes"], 8)
        self.assertEqual(certificate["flat_patterns"], 8)
        self.assertEqual(certificate["nonflat_patterns"], 56)
        self.assertEqual(certificate["flat_clearing_gauges_per_pattern"], 2)
        self.assertEqual(certificate["coherent_J_ambiguity"], "one global reversal")


if __name__ == "__main__":
    unittest.main()
