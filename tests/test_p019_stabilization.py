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


def iterate_until_fixed(n: int, exponents: tuple[int, ...]) -> tuple[int, int]:
    state = n
    steps = 0
    while True:
        nxt = collapse_word(state, exponents)
        if nxt == state:
            return state, steps
        if not nxt < state:
            raise AssertionError((state, nxt, exponents))
        state = nxt
        steps += 1


def iterate_map_until_fixed(start: int, values: tuple[int, ...]) -> int:
    state = start
    while True:
        nxt = values[state]
        if nxt == state:
            return state
        if not nxt < state:
            raise AssertionError((values, state, nxt))
        state = nxt


class WellFoundedMotherTheoremTests(unittest.TestCase):
    def test_all_monotone_reductive_maps_on_small_chains(self) -> None:
        # Enumerate every reductive self-map on {0,...,5}, then retain the monotone ones.
        # For each initial state, iteration must reach the greatest fixed point below it.
        size = 6
        choices = [range(i + 1) for i in range(size)]
        for values in itertools.product(*choices):
            if any(values[i] > values[i + 1] for i in range(size - 1)):
                continue
            fixed = [i for i, value in enumerate(values) if i == value]
            for start in range(size):
                expected = max(i for i in fixed if i <= start)
                self.assertEqual(iterate_map_until_fixed(start, values), expected)


class CollapseWordStabilizationTests(unittest.TestCase):
    def test_all_short_words_stabilize_to_lcm_collapse(self) -> None:
        alphabet = (1, 2, 3, 4, 5)
        for length in range(0, 4):
            for word in itertools.product(alphabet, repeat=length):
                L = exponent_lcm(word)
                for n in range(0, 601):
                    limit, steps = iterate_until_fixed(n, word)
                    expected = collapse(n, L)
                    self.assertEqual(limit, expected, msg=f"word={word}, L={L}, n={n}")
                    self.assertLessEqual(steps, n - expected)

    def test_order_changes_transient_but_not_stable_map(self) -> None:
        n = 8
        left = (3, 2)
        right = (2, 3)
        self.assertNotEqual(collapse_word(n, left), collapse_word(n, right))
        self.assertEqual(iterate_until_fixed(n, left)[0], collapse(n, 6))
        self.assertEqual(iterate_until_fixed(n, right)[0], collapse(n, 6))

    def test_distinct_lcm_exponents_give_distinct_stable_maps(self) -> None:
        for a in range(1, 13):
            for b in range(a + 1, 13):
                witness = 2**a
                self.assertEqual(collapse(witness, a), witness)
                self.assertEqual(collapse(witness, b), 1)

    def test_concatenation_stable_normal_form_uses_lcm(self) -> None:
        words = [(), (2,), (3,), (2, 4), (3, 5), (2, 3, 4)]
        for left in words:
            for right in words:
                joined = left + right
                L = math.lcm(exponent_lcm(left), exponent_lcm(right))
                self.assertEqual(exponent_lcm(joined), L)
                for n in range(0, 801):
                    self.assertEqual(iterate_until_fixed(n, joined)[0], collapse(n, L))

    def test_no_nontrivial_cycle_on_representative_words(self) -> None:
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
