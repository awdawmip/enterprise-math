"""Full three-state mass recursion for an internal 11 -> 02 or 20 exchange.

Runs with the Python standard library. With --c64, independently compares
both TV and H against the inherited scalar model for every complete schedule.
"""
import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


FIVE_RATE = (Q(1, 4), Q(1), Q(4))
TAILS = ("557", "575", "755")


def read_word(raw_masses, inventory, word):
    masses = list(raw_masses)
    stock = list(inventory)
    for letter in word:
        position = "2357".index(letter)
        assert stock[position] > 0
        next_masses = [Q(0)] * 3
        for s, mass in enumerate(masses):
            total_rate = stock[0] + stock[1] + FIVE_RATE[s] * stock[2] + stock[3]
            selected = stock[position] * (FIVE_RATE[s] if letter == "5" else 1)
            contribution = mass * selected / total_rate
            if letter == "3":
                next_masses[0] += contribution * Q(7, 8)
                next_masses[s] += contribution / 8
            elif letter == "2":
                next_masses[min(s + 1, 2)] += contribution
            else:
                next_masses[s] += contribution
        stock[position] -= 1
        masses = next_masses
    return tuple(masses), tuple(stock)


def indicators(k, gaps):
    assert len(gaps) == k + 1 and sum(gaps) == k - 1
    word = '23'.join('5' * m for m in gaps)
    priors = [(Q(1), Q(0), Q(0)), (Q(0), Q(1), Q(0))]
    states, tails = [], []
    for prior in priors:
        masses, remain = read_word(prior, (k, k, k + 1, 1), word)
        total = sum(masses)
        states.append([mass / total for mass in masses])
        assert remain == (0, 0, 2, 1)
        tail_masses = []
        for ending in TAILS:
            full, consumed = read_word(masses, remain, ending)
            assert consumed == (0, 0, 0, 0)
            tail_masses.append(sum(full))
        assert sum(tail_masses) == total
        tails.append(tail_masses)
    delta = sum(abs(x - y) for x, y in zip(*states)) / 2
    ratios = [x / y for x, y in zip(*tails)]
    return delta, max(ratios) / min(ratios)


def enclose(lower, upper, digits=14):
    scale = 10**digits
    lowscaled = (lower.numerator * scale) // lower.denominator
    highscaled = -((-upper.numerator * scale) // upper.denominator)
    def show(q):
        return f"{q//scale}.{q%scale:0{digits}d}"
    return [show(lowscaled), show(highscaled)]


def run(crosscheck=None):
    table = []
    for r in (8, 16, 32, 50, 51, 64, 128):
        k = r + 2  # One canonical internal update before the two changed gaps.
        canonical = [1] * (k - 1) + [0, 0]
        values = {}
        for label in ("11", "02", "20"):
            gaps = canonical.copy()
            gaps[k-r:k-r+2] = [int(symbol) for symbol in label]
            delta, H = indicators(k, gaps)
            if crosscheck is not None:
                compact, observable = crosscheck
                assert delta == compact.total_variation(k, gaps)
                assert H == observable.hilbert_ratio(k, gaps)
            values[label] = (delta, H)
        base, base_H = values["11"]
        row = dict(k=k, residual_pairs_at_exchange=r)
        for label in ("02", "20"):
            delta, H = values[label]
            tv = delta / (base * r**4)
            # x/(1+x) < log(1+x) < x for x>0, with no evaluation of a
            # transcendental function or floating subtraction of near-equals.
            first_order = (H-1) / ((base_H-1) * r**4)
            row[label] = dict(TV_ratio_div_r4=enclose(tv, tv),
                              log_H_ratio_div_r4=enclose(first_order/H, first_order*base_H))
        table.append(row)
    return dict(full_mass_model="exact state sums by selected symbol, separately for each prepared history and each complete tail", 
                cuts=table, scalar_crosscheck=bool(crosscheck),
                counts=dict(full_schedules=3*len(table), final_state_rows=6*len(table),
                            complete_tail_masses=18*len(table)),
                limit_02="217206405000/4149549889", limit_20="217206405000/4346633041")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--c64", type=Path, help="directory holding suffix_limits.py and observable_minimum.py")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    modules = None
    if args.c64:
        sys.path.insert(0, str(args.c64.resolve()))
        import suffix_limits, observable_minimum
        modules = (suffix_limits, observable_minimum)
    result = run(modules)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in result["cuts"]:
        print(row["residual_pairs_at_exchange"], row["02"]["TV_ratio_div_r4"], row["20"]["TV_ratio_div_r4"])
