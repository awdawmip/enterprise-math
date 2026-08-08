import itertools
import math
import unittest

from enterprise_math.core import collapse


def collapse_word(n: int, exponents: tuple[int, ...]) -> int:
    state = n
    for p in exponents:
        state = collapse(state, p)
    return state


def exponent_lcm(exponents: tuple[int, ...]) -> int:
    result = 1
    for p in exponents:
        result = math.lcm(result, p)
    return result


class CollapseWordFixedPointTests(unittest.TestCase):
    def test_fixed_points_equal_lcm_perfect_powers(self) -> None:
        words = [
            (),
            (2,),
            (2, 3),
            (3, 2),
            (2, 4),
            (2, 3, 4),
            (6, 2, 3, 6),
        ]
        for word in words:
            L = exponent_lcm(word)
            for n in range(0, 5001):
                self.assertEqual(
                    collapse_word(n, word) == n,
                    collapse(n, L) == n,
                    msg=f"word={word}, L={L}, n={n}",
                )

    def test_all_short_words_match_lcm_fixed_profile(self) -> None:
        alphabet = (1, 2, 3, 4)
        for length in range(0, 5):
            for word in itertools.product(alphabet, repeat=length):
                L = exponent_lcm(word)
                for n in range(0, 401):
                    self.assertEqual(
                        collapse_word(n, word) == n,
                        collapse(n, L) == n,
                        msg=f"word={word}, L={L}, n={n}",
                    )

    def test_reordering_preserves_fixed_points_but_not_single_pass_action(self) -> None:
        left = (3, 2)
        right = (2, 3)
        for n in range(0, 2001):
            self.assertEqual(
                collapse_word(n, left) == n,
                collapse_word(n, right) == n,
            )

        self.assertNotEqual(collapse_word(8, left), collapse_word(8, right))

    def test_repetition_preserves_fixed_point_set(self) -> None:
        a = (2, 3)
        b = (2, 3, 2, 3, 3)
        for n in range(0, 2001):
            self.assertEqual(collapse_word(n, a) == n, collapse_word(n, b) == n)


if __name__ == "__main__":
    unittest.main()
