"""Compare true positive three-state path probabilities with the integer centers."""
from fractions import Fraction as Q
import json

from blind_center_decoder import endpoint_odds, simulate, truth, blind


def native_observations(gaps):
    rates = (Q(1, 4), Q(1), Q(4))
    blocks = len(gaps) - 1
    stock = [blocks, blocks, sum(gaps) + 2, 1]
    symbols = "2357"

    def consume(vector, inventory, symbol):
        idx = symbols.index(symbol)
        weights = []
        for mass, rate in zip(vector, rates):
            total = inventory[0] + inventory[1] + rate * inventory[2] + inventory[3]
            factor = rate if symbol == "5" else 1
            weights.append(mass * inventory[idx] * factor / total)
        inventory[idx] -= 1
        if symbol == "2":
            return [Q(0), weights[0], weights[1] + weights[2]]
        if symbol == "3":
            return [(7 * sum(weights) + weights[0]) / 8, weights[1] / 8, weights[2] / 8]
        return weights

    tails = ("557", "575", "755")
    word = "".join("5" * gap + "23" for gap in gaps[:-1]) + "5" * gaps[-1]
    rows = []
    for t in (0, 1):
        # The common starting mass factor of 1/8 cancels in all ratios.
        state = [Q(7), Q(t), Q(1 - t)]
        inventory = stock.copy()
        for symbol in word:
            state = consume(state, inventory, symbol)
        assert inventory == [0, 0, 2, 1]
        row = []
        for tail in tails:
            tail_inventory = inventory.copy()
            tail_state = state.copy()
            for symbol in tail:
                tail_state = consume(tail_state, tail_inventory, symbol)
            row.append(sum(tail_state))
        assert sum(row) == sum(state)
        rows.append(row)
    z = [end / start for start, end in zip(*rows)]
    lo, hi = min(z), max(z)
    return hi / lo, (1 + hi) / (1 + lo), z


def order(value):
    assert value
    def v2(n):
        return (n & -n).bit_length() - 1
    return v2(value.numerator) - v2(value.denominator)


def check(gaps, decode=False):
    g, h, z = native_observations(gaps)
    assert z == endpoint_odds(gaps)
    assert (g, h) == simulate(gaps)
    if not decode:
        return
    c = 2 + sum(gaps)
    r = len(gaps) - 1
    centers, bits = blind(r, c, g, h)
    assert centers == truth(gaps)
    paired = sorted(max(order(1 / v - center) for center in centers)
                    for v in (min(z), max(z)))
    return {"r": r, "c": c, "gaps": gaps, "two_center_bits": bits,
            "matched_dyadic_orders": paired}


if __name__ == "__main__":
    from itertools import product
    controls = [gaps for r in range(1, 4) for gaps in product(range(4), repeat=r + 1)]
    for gaps in controls:
        check(gaps)
    examples = [check(gaps, True) for gaps in [(200, 250), (450, 505, 470)]]
    print(json.dumps({"small_schedules": len(controls), "decoded_long_schedules": examples}, indent=2))
