from __future__ import annotations

import random
import unittest
from dataclasses import dataclass
from math import isqrt

from enterprise_math.brc_table_free_tail import (
    binomial_half_coefficients,
    transport_certified_tail,
    two_correction_certificate,
)


@dataclass(frozen=True)
class Source:
    n: int
    multiplier: int
    root: int
    remainder: int


def source_state(n: int, multiplier: int) -> Source:
    root = isqrt(multiplier * n)
    return Source(n, multiplier, root, multiplier * n - root * root)


class BRCTableFreeTailTests(unittest.TestCase):
    def test_reference_coefficients(self) -> None:
        coeffs = binomial_half_coefficients(5)
        self.assertEqual(
            tuple(str(value) for value in coeffs),
            ("1/2", "-1/8", "1/16", "-5/128", "7/256"),
        )

    def test_exhaustive_certified_small(self) -> None:
        for degree in (2, 4, 6, 8, 16):
            for n in range(1, 500):
                for multiplier in range(2, 120):
                    source = source_state(n, multiplier)
                    for step in (1, 2):
                        if not two_correction_certificate(
                            source.root, multiplier, step, degree
                        ):
                            continue
                        got = transport_certified_tail(
                            source, multiplier + step, degree=degree
                        )
                        want = source_state(n, multiplier + step)
                        self.assertEqual(
                            (got.root, got.remainder),
                            (want.root, want.remainder),
                        )
                        self.assertLessEqual(got.correction_steps, 2)

    def test_random_big_certified_thresholds(self) -> None:
        rng = random.Random(20260907)
        for bits, degree in (
            (128, 32),
            (256, 32),
            (512, 64),
            (1024, 128),
            (2048, 256),
            (4096, 256),
        ):
            for _ in range(12):
                n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
                multiplier = 2
                while True:
                    source = source_state(n, multiplier)
                    if two_correction_certificate(
                        source.root, multiplier, 2, degree
                    ):
                        break
                    multiplier *= 2
                got = transport_certified_tail(
                    source, multiplier + 2, degree=degree
                )
                want = source_state(n, multiplier + 2)
                self.assertEqual(
                    (got.root, got.remainder),
                    (want.root, want.remainder),
                )

    def test_uncertified_state_is_rejected(self) -> None:
        n = (1 << 1024) + 643
        source = source_state(n, 2)
        self.assertFalse(two_correction_certificate(source.root, 2, 2, 4))
        with self.assertRaises(ValueError):
            transport_certified_tail(source, 4, degree=4)


if __name__ == "__main__":
    unittest.main()
