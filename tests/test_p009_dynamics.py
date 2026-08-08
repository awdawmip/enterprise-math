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


def iterate_until_fixed(n: int, exponents: tuple[int, ...]) -> tuple[int, int]:
    steps = 0
    state = n
    while True:
        nxt = collapse_word(state, exponents)
        if nxt == state:
            return state, steps
        if not nxt < state:
            raise AssertionError((state, nxt, exponents))
        state = nxt
        steps += 1


class CollapseWordDynamicsTests(unittest.TestCase):
    def test_every_word_converges_to_lcm_collapse(self) -> None:
        words = [
            (),
            (2,),
            (2, 3),
            (3, 2),
            (2, 4),
            (2, 3, 5),
            (6, 2, 3, 6),
        ]
        for word in words:
            L = exponent_lcm(word)
            for n in range(0, 3001):
                limit, steps = iterate_until_fixed(n, word)
                expected = collapse(n, L)
                self.assertEqual(limit, expected, msg=f"word={word}, n={n}")
                self.assertLessEqual(steps, n - expected)

    def test_order_can_change_transient_but_not_limit(self) -> None:
        n = 8
        a = (3, 2)
        b = (2, 3)
        self.assertNotEqual(collapse_word(n, a), collapse_word(n, b))
        self.assertEqual(iterate_until_fixed(n, a)[0], iterate_until_fixed(n, b)[0])
        self.assertEqual(iterate_until_fixed(n, a)[0], collapse(n, 6))

    def test_no_nontrivial_cycle_on_small_domains(self) -> None:
        words = [(2, 3), (3, 2), (2, 5, 3), (4, 6)]
        for word in words:
            for n in range(0, 2001):
                seen: set[int] = set()
                state = n
                while state not in seen:
                    seen.add(state)
                    nxt = collapse_word(state, word)
                    if nxt == state:
                        break
                    self.assertLess(nxt, state)
                    state = nxt
                else:
                    self.fail(f"nontrivial cycle detected: word={word}, n={n}")


if __name__ == "__main__":
    unittest.main()
