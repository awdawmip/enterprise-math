"""Exact checks for the C63 fixed-inversion likelihood extrema.

Run with Python 3.10+; prints a JSON result. No third-party dependencies.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import prod
import json


def words(fives, sevens):
    length = fives + sevens
    for positions in combinations(range(length), fives):
        symbols = ["7"] * length
        for index in positions:
            symbols[index] = "5"
        yield "".join(symbols)


def inversion_count(word):
    """Number of ordered pairs consisting of a 5 followed by a 7."""
    fives = pairs = 0
    for prime in word:
        if prime == "5":
            fives += 1
        else:
            pairs += fives
    return pairs


def marked_word(gaps, sevens):
    symbols = ["7"] * (len(gaps) + sevens)
    for index, gap in enumerate(gaps):
        symbols[index + gap] = "5"
    return "".join(symbols)


def endpoints(fives, sevens, inversions):
    if fives == 0 or sevens == 0:
        word = "5" * fives + "7" * sevens
        return word, word
    total = fives * sevens - inversions
    level, excess = divmod(total, fives)
    balanced = [level] * (fives - excess) + [level + 1] * excess
    full, part = divmod(total, sevens)
    packed = [0] * (fives - full - int(part > 0))
    if part:
        packed.append(part)
    packed.extend([sevens] * full)
    return marked_word(balanced, sevens), marked_word(packed, sevens)


def likelihood_of_block_and_pair(word, r, c, d, five_rate):
    """Direct sampling probabilities for the hidden word followed by 2 then 3."""
    next_rate = 1 if five_rate == Fraction(1, 4) else 4
    probability = Fraction(1)
    for prime in word:
        total = 2 * r + c * five_rate + d
        if prime == "5":
            probability *= Fraction(c * five_rate, total)
            c -= 1
        else:
            probability *= Fraction(d, total)
            d -= 1
    probability *= Fraction(r, 2 * r + c * five_rate + d)
    probability *= Fraction(r, 2 * r - 1 + next_rate * c + d)
    return probability


def direct_ratio(word, r, c, d):
    return (likelihood_of_block_and_pair(word, r, c, d, 1)
            / likelihood_of_block_and_pair(word, r, c, d, 4))


def prefix_numerator(word, budget):
    factors = [budget]
    for symbol in word:
        factors.append(factors[-1] - (4 if symbol == "5" else 1))
    return prod(factors)


def check_transfers(word, budget, weights):
    """Check the two changed factors against independently computed products."""
    positions = [t for t, symbol in enumerate(word) if symbol == "5"]
    checked = 0
    for i, t in enumerate(positions):
        if t == 0 or word[t - 1] == "5":
            continue
        for h in range(i + 1, len(positions)):
            u = positions[h]
            if u + 1 == len(word) or word[u + 1] == "5":
                continue
            updated = list(word)
            updated[t - 1:t + 1] = "57"
            updated[u:u + 2] = "75"
            updated = "".join(updated)
            old_first = budget - t - 3 * i
            old_second = budget - (u + 1) - 3 * (h + 1)
            ratio = Fraction((old_first - 3) * (old_second + 3),
                             old_first * old_second)
            assert ratio == Fraction(prefix_numerator(updated, budget),
                                     prefix_numerator(word, budget))
            assert (ratio - 1 == Fraction(3 * (u - t + 3 * (h - i) + 1),
                                          old_first * old_second))
            assert inversion_count(updated) == inversion_count(word)
            assert ratio > 1
            old_q0, old_q1, old_q2 = weights[word]
            new_q0, new_q1, new_q2 = weights[updated]
            assert new_q0 > old_q0 and new_q1 == old_q1 and new_q2 < old_q2
            checked += 1
    return checked


def verify():
    counts = Counter()
    for a in range(7):
        for b in range(7):
            candidates = list(words(a, b))
            for r, c, d in [(1, max(1, a), b), (2, a + 3, b + 1),
                            (5, a + 1, b + 7)]:
                initial_total = 2 * r + d + 4 * c
                common_den = 4**a * prod(2 * r + d + c - j
                                          for j in range(a + b + 1))
                fibers = defaultdict(dict)
                weights = {word: tuple(likelihood_of_block_and_pair(word, r, c, d, z)
                                       for z in (Fraction(1, 4), 1, 4))
                           for word in candidates}
                for word, (q0, q1, q2) in weights.items():
                    ratio = q1 / q2
                    assert ratio == Fraction(prefix_numerator(word, initial_total),
                                             common_den)
                    fibers[inversion_count(word)][word] = ratio
                    counts["word_inventory_checks"] += 1
                    counts["legal_outward_transfer_checks"] += check_transfers(
                        word, initial_total, weights)
                for x, ratios in fibers.items():
                    lower, upper = endpoints(a, b, x)
                    minimum, maximum = min(ratios.values()), max(ratios.values())
                    assert [w for w, val in ratios.items() if val == minimum] == [lower]
                    assert [w for w, val in ratios.items() if val == maximum] == [upper]
                    # For every input, the reciprocal map is affine in the two
                    # posterior odds q2/q0 and q1/q0. Test both sufficient endpoints.
                    for endpoint in (1, 2):
                        odds = {word: weights[word][endpoint] / weights[word][0]
                                for word in ratios}
                        assert [w for w, val in odds.items() if val == max(odds.values())] == [lower]
                        assert [w for w, val in odds.items() if val == min(odds.values())] == [upper]
                        counts["posterior_odds_endpoint_checks"] += 1
                    counts["fiber_inventory_checks"] += 1
                    if len(ratios) > 1:
                        counts["nonsingleton_fiber_inventory_checks"] += 1

    cases = []
    for r, c, d, expected in [
            (1, 4, 8, ("85/88", "1")),
            (1, 5, 11, ("253/255", "22011/21760"))]:
        lower, upper = endpoints(2, 2, 2)
        values = [str(direct_ratio(word, r, c, d)) for word in (lower, upper)]
        assert tuple(values) == expected
        assert [w for w in words(2, 2) if inversion_count(w) == 2] == [upper, lower]
        cases.append({"r": r, "c": c, "d": d, "X57": 2,
                      "lower": [lower, values[0]], "upper": [upper, values[1]]})
    first, second = "57777557", "75757775"
    assert inversion_count(first) == inversion_count(second) == 7
    reversals = []
    for r, expected in [(29, Fraction(4260864, 4260865)), (30, Fraction(132275, 132273))]:
        ratio = direct_ratio(first, r, 4, 6) / direct_ratio(second, r, 4, 6)
        assert ratio == expected
        reversals.append({"r": r, "c": 4, "d": 6, "ratio_of_rhos": str(ratio)})
    reversal_case = {"first": first, "second": second, "inventories": reversals}

    ties = []
    for word, expected in [("57577557557", Fraction(2130128, 83251703)),
                           ("75755575775", Fraction(254562, 10049503))]:
        assert inversion_count(word) == 15
        assert direct_ratio(word, 2, 7, 7) == Fraction(68875, 147456)
        q0 = likelihood_of_block_and_pair(word, 2, 7, 7, Fraction(1, 4))
        q2 = likelihood_of_block_and_pair(word, 2, 7, 7, 4)
        value = 7 * q0 / (7 * q0 + q2)
        assert value == expected
        ties.append({"word": word, "F(0)": str(value)})
    tie_case = {"r": 2, "c": 7, "d": 7, "X57": 15, "rho": "68875/147456",
                "maps": ties}
    interior_syncs = []
    for r, c, d, a, b, x, witness, expected, expected_size in [
        (1, 2, 6, 2, 5, 4, "7757757", ("13/16", "1", "11/8"), 3),
        (2, 10, 8, 7, 5, 23, "555577775557",
         ("8486179/10813440", "1", "6003/5632"), 35),
    ]:
        lower, upper = endpoints(a, b, x)
        fiber = [word for word in words(a, b) if inversion_count(word) == x]
        assert witness in fiber and witness not in (lower, upper)
        assert len(fiber) == expected_size
        ratios = {word: direct_ratio(word, r, c, d) for word in fiber}
        values = [str(ratios[word]) for word in (lower, witness, upper)]
        assert values == list(expected)
        assert ratios[lower] == min(ratios.values()) and ratios[upper] == max(ratios.values())
        interior_syncs.append({"r": r, "c": c, "d": d, "X57": x, "size": len(fiber),
                               "words": [lower, witness, upper], "rhos": values})
    return {"checks": dict(counts), "cases": cases, "order_reversal": reversal_case,
            "tied_rho_distinct_update": tie_case, "interior_sync": interior_syncs,
            "success": True}


if __name__ == "__main__":
    print(json.dumps(verify(), ensure_ascii=False, indent=2, sort_keys=True))
