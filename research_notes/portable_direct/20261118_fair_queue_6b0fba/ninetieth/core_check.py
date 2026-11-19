"""Finite checks of protected exponent locations using known-position erasures. Python 3."""
import json
from collections import Counter
from itertools import combinations
from math import comb, gcd, isqrt


def ceiling_double_sqrt(value):
    return 0 if not value else 1 + isqrt(4 * value - 1)


def first_bad_order(survivors, span):
    differences = [d for d in range(1, span + 1) if survivors & (survivors >> d)]
    for order in range(1, span + 1):
        divisor = 0
        for difference in differences:
            if difference % order == 0:
                divisor = gcd(divisor, difference)
        if divisor != order:
            return order
    return span + 1


def bad_core_table(span, budget, horizon, deletions):
    """Superset Boolean zeta transform of the unsafe retained masks."""
    size = 1 << (span + 1)
    bad = bytearray(size)
    for retained, loss, first_bad in deletions:
        if loss <= budget and first_bad <= horizon:
            bad[retained] = 1
    width = 1
    while width < size:
        for base in range(0, size, 2 * width):
            for index in range(base, base + width):
                if bad[index + width]:
                    bad[index] = 1
        width *= 2
    return bad


def end_masks(span, budget):
    strip = (1 << budget) - 1
    result = []
    for lower in range(1 << budget):
        for upper in range(1 << budget):
            upper_reverse = int(format(upper, "0%db" % budget)[::-1], 2)
            core = lower | (upper_reverse << (span - budget + 1))
            sums = 0
            for i in range(budget):
                if (lower >> i) & 1:
                    sums |= upper << i
            result.append((core, sums & strip))
    return result


def construction(span, budget, slack):
    length = max(0, budget - slack)
    if length:
        left_size = ceiling_double_sqrt(length) // 2
        right_size = (length + left_size - 1) // left_size
        result = set(range(left_size))
        result.update(span - slack - j * left_size for j in range(right_size))
    else:
        result = set()
    if span == 3 * budget - 1:
        result.add(budget)
    return sum(1 << x for x in result)


def check_all_cores(max_span):
    total_masks = 0
    parameters = 0
    selected = []
    for span in range(2, max_span + 1):
        full = (1 << (span + 1)) - 1
        max_budget = (span + 1) // 3
        deletions = []
        for loss in range(max_budget + 1):
            for removed in combinations(range(span + 1), loss):
                survivors = full ^ sum(1 << i for i in removed)
                deletions.append((survivors, loss, first_bad_order(survivors, span)))
        for budget in range(1, max_budget + 1):
            endpoints = end_masks(span, budget)
            middle = full ^ (((1 << budget) - 1) * (1 + (1 << (span - budget + 1))))
            special = span == 3 * budget - 1
            # Include the no-protection transition at s=e in the regular region.
            for slack in range(budget if special else budget + 1):
                length = budget - slack
                horizon = span - slack
                bad = bad_core_table(span, budget, horizon, deletions)
                need = ((1 << length) - 1) << slack
                accepted = {core for core, sums in endpoints if sums & need == need}
                count = Counter()
                for mask in range(full + 1):
                    predicted = (mask & ~middle) in accepted and (not special or bool(mask & middle))
                    assert bool(bad[mask]) != predicted, (span, budget, slack, mask)
                    if predicted:
                        count[mask.bit_count()] += 1
                optimum = ceiling_double_sqrt(length) + special
                assert min(count) == optimum
                core = construction(span, budget, slack)
                assert not bad[core] and core.bit_count() == optimum
                if length == 4 or (special and slack == 0):
                    selected.append([span, budget, slack, optimum, count[optimum]])
                parameters += 1
                total_masks += full + 1
    return {"max_span": max_span, "parameter_triples": parameters,
            "labeled_core_checks": total_masks,
            "selected_A_e_s_minimum_number": selected}


def exact_interval_tilings(size, left_size, right_size):
    """Search for the first missing integer, with exact collision/excess rejection."""
    full = (1 << size) - 1

    def visit(left, right, covered):
        if covered == full:
            return int(left.bit_count() == left_size and right.bit_count() == right_size)
        missing = full ^ covered
        point = (missing & -missing).bit_length() - 1
        answer = 0
        for add_left in (True, False):
            chosen, other = (left, right) if add_left else (right, left)
            room = left_size if add_left else right_size
            if chosen.bit_count() == room:
                continue
            extra = other << point
            if extra & covered or extra & ~full:
                continue
            grown = chosen | (1 << point)
            if add_left:
                answer += visit(grown, right, covered | extra)
            else:
                answer += visit(left, grown, covered | extra)
        return answer

    return visit(1, 1, 1)


def check_tilings():
    prime_power = []
    for prime, exponent in [(2, i) for i in range(1, 6)] + [(3, 1), (3, 2), (5, 1), (7, 1)]:
        side = prime ** exponent
        count = exact_interval_tilings(side ** 2, side, side)
        assert count == comb(2 * exponent, exponent)
        prime_power.append([prime, exponent, side ** 2, count])
    composites = []
    for side in (2, 3, 4, 5, 6, 7, 8):
        size = side * (side + 1)
        count = exact_interval_tilings(size, side, side + 1)
        composites.append([size, side, side + 1, count])
    return {"prime_exponent_window_labeled_count": prime_power,
            "other_tight_window_left_right_ordered_count": composites}


def minimum_sampling(span, budget, slack):
    """For the displayed fixed core, exact deletion-distance recurrence on all supports."""
    core = construction(span, budget, slack)
    size = 1 << (span + 1)
    distance = bytearray(size)
    counts = Counter()
    best = None
    for support in range(size):
        if support & core != core or first_bad_order(support, span) <= span - slack:
            continue
        removable = support ^ core
        remaining = budget + 1
        while removable:
            bit = removable & -removable
            remaining = min(remaining, 1 + distance[support ^ bit])
            removable ^= bit
        distance[support] = remaining
        if remaining > budget:
            counts[support.bit_count()] += 1
            if best is None or support.bit_count() < best.bit_count():
                best = support
    def coordinates(mask):
        return [i for i in range(span + 1) if mask >> i & 1]
    assert best is not None
    return {"A_e_s": [span, budget, slack], "preset_core": coordinates(core),
            "minimum_samples": best.bit_count(), "number_of_minimum_supports": counts[best.bit_count()],
            "one_minimum_support": coordinates(best)}


def frozen_witnesses():
    def mask(points):
        return sum(1 << p for p in points)
    assert first_bad_order(mask([0, 1, 2, 3, 8, 9, 10, 11]), 11) == 4
    assert first_bad_order(mask([0, 3, 6]), 6) == 1
    return {"A11_remove_4_through_7_first_bad_order": 4,
            "A6_remove_1_first_bad_order": 1}


if __name__ == "__main__":
    print(json.dumps({"all_cores": check_all_cores(15), "tilings": check_tilings(),
                      "fixed_core_sparse_supports": [minimum_sampling(*args) for args in [(12, 4, 0), (15, 5, 1), (16, 4, 0)]],
                      "frozen_witnesses": frozen_witnesses()}, ensure_ascii=False, indent=2))
