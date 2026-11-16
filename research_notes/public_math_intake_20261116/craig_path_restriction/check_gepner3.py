"""Check the finite Gepner normalization and its fourth moment using exact counts."""
from functools import lru_cache
from collections import Counter
from fractions import Fraction
from itertools import combinations

from check_x6_projection3 import paths
from check_weighted import load_signed_brc


def statistics(word):
    seen = [0, 0, 0]
    cyclic_pairs = 0
    for color in word:
        cyclic_pairs += seen[(color - 1) % 3]
        seen[color] += 1
    return cyclic_pairs


def cyclic_histogram(counts):
    """Distribution by cyclic pair count, adding the last colored step."""
    @lru_cache(maxsize=None)
    def build(state):
        if not any(state):
            return {0: 1}
        out = Counter()
        for color, amount in enumerate(state):
            if amount == 0:
                continue
            previous = list(state)
            previous[color] -= 1
            increment = previous[(color - 1) % 3]
            for value, freq in build(tuple(previous)).items():
                out[value + increment] += freq
        return out
    return build(counts)


if __name__ == "__main__":
    brc = load_signed_brc()
    for n in range(1, 5):
        count = fourth_numerator = 0
        endpoint = (n, n, n, 0, 0, 0)
        for word in paths(endpoint):
            cyclic_pairs = statistics(word)
            centered = 2 * cyclic_pairs - 3 * n * n
            if n <= 3:
                odd = sum((a, b, c) in {(0, 2, 1), (1, 0, 2), (2, 1, 0)}
                          for a, b, c in combinations(word, 3))
                assert 2 * odd - n**3 == -n * centered
            fourth_numerator += centered**4
            count += 1
        assert count == brc.shortest_path_multiplicity(endpoint)
        moment = Fraction(fourth_numerator, count * (2*n*n)**4)
        assert moment == Fraction(21, 80*n**4) - Fraction(1, 5*n**5)
        print(n, count, moment)

    for n in range(1, 7):
        hist = cyclic_histogram((n, n, n))
        total = brc.shortest_path_multiplicity((n, n, n, 0, 0, 0))
        assert total == sum(hist.values())
        def central(power):
            raw = sum((2*v-3*n*n)**power * weight for v, weight in hist.items())
            return Fraction(raw, total * (2*n*n)**power)
        assert central(4) == Fraction(21,80*n**4)-Fraction(1,5*n**5)
        assert central(6) == (Fraction(279,448*n**6)-Fraction(41,28*n**7)
                              +Fraction(8,7*n**8)-Fraction(2,7*n**9))
    print("Exact last-step recursion and fourth/sixth moments through N=6.")
