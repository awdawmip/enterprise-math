import unittest

from enterprise_math.partial_legality_scale import (
    action_gcd,
    one_sided_basin_boundaries,
    one_sided_complete_basin_widths,
    one_sided_legality_rank,
    reachable_decrement_sums,
    signed_gcd_probe_word,
    signed_legality_level,
    signed_word_is_legal,
    single_decrement_level,
)


class PartialLegalityScaleTests(unittest.TestCase):
    def test_single_decrement_generates_exact_block_quotient(self):
        for step in range(1, 9):
            for n in range(0, 129):
                expected = max(k for k in range(0, n // step + 1) if k * step <= n)
                self.assertEqual(single_decrement_level(n, step), expected)

    def test_one_sided_boundaries_are_additive_monoid_sums(self):
        steps = (4, 6)
        expected = (0, 4, 6, 8, 10, 12, 14, 16, 18, 20)
        self.assertEqual(reachable_decrement_sums(steps, 20), expected)
        self.assertEqual(one_sided_basin_boundaries(steps, 20), expected)
        self.assertEqual(
            one_sided_complete_basin_widths(steps, 20),
            (4, 2, 2, 2, 2, 2, 2, 2, 2),
        )
        for n in range(0, 4):
            self.assertEqual(one_sided_legality_rank(n, steps), 0)
        self.assertEqual(one_sided_legality_rank(4, steps), 1)
        self.assertEqual(one_sided_legality_rank(5, steps), 1)
        self.assertEqual(one_sided_legality_rank(6, steps), 2)

    def test_signed_probe_realizes_gcd_threshold(self):
        families = (
            (4, 6),
            (6, 12, 18),
            (6, 10, 15),
            (8, 12, 18),
            (5, 7),
        )
        for steps in families:
            grain = action_gcd(steps)
            probe = signed_gcd_probe_word(steps)
            self.assertEqual(sum(probe), -grain)

            displacement = 0
            minimum = 0
            for signed_step in probe:
                displacement += signed_step
                minimum = min(minimum, displacement)
            self.assertEqual(minimum, -grain)

            for copies in range(1, 6):
                word = probe * copies
                for n in range(0, 64):
                    self.assertEqual(
                        signed_word_is_legal(n, word),
                        n >= copies * grain,
                    )

    def test_signed_family_generates_exact_gcd_block_level(self):
        families = (
            (4, 6),
            (6, 12, 18),
            (6, 10, 15),
            (8, 12, 18),
            (5, 7),
        )
        for steps in families:
            grain = action_gcd(steps)
            for n in range(0, 129):
                self.assertEqual(signed_legality_level(n, steps), n // grain)

            for level in range(0, 20):
                fiber = range(level * grain, (level + 1) * grain)
                for step in steps:
                    delta = step // grain
                    enabled = level >= delta
                    for n in fiber:
                        self.assertEqual(n >= step, enabled)
                        self.assertEqual((n + step) // grain, level + delta)
                        if enabled:
                            self.assertEqual((n - step) // grain, level - delta)

    def test_total_increment_can_expose_a_missing_one_sided_cut(self):
        self.assertEqual(one_sided_legality_rank(0, (4, 6)), 0)
        self.assertEqual(one_sided_legality_rank(2, (4, 6)), 0)

        probe = signed_gcd_probe_word((4, 6))
        self.assertEqual(probe, (4, -6))
        self.assertFalse(signed_word_is_legal(0, probe))
        self.assertTrue(signed_word_is_legal(2, probe))
        self.assertNotEqual(
            signed_legality_level(0, (4, 6)),
            signed_legality_level(2, (4, 6)),
        )


if __name__ == "__main__":
    unittest.main()
