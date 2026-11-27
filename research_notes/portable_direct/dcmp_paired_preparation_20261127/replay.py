"""Exact finite checks for globally flipped pair preparations."""

from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from math import lcm
from pathlib import Path
import argparse
import json


def partition(size, count):
    base, extra = divmod(size, count)
    return tuple(base + (i < extra) for i in range(count))


def binary_rows(blocks):
    size = sum(blocks)
    length = 0
    for width in blocks:
        row = (0,) * length + tuple(1 << i for i in range(width)) + (0,) * (size - length - width)
        yield row, (1 << width) - 1
        length += width


def direction_margin(rows, size):
    common = lcm(*(denominator for _, denominator in rows))
    scaled = [tuple(a * (common // denominator) for a in row) for row, denominator in rows]
    margin = 2 * common + 1
    checked = 0
    for d in product((-1, 0, 1), repeat=size):
        if not any(d):
            continue
        observed = max(abs(sum(a * b for a, b in zip(row, d))) for row in scaled)
        margin = min(margin, 2 * observed)
        checked += 1
    return Q(margin, common), checked


def table_pairs(frozen):
    raw = json.loads(frozen)["extremal_model"]
    signs = {tuple(map(tuple, row["outcomes_setting_order_00_01_10_11"])): row for row in raw}
    pairs = []
    for table in sorted(signs):
        flip = tuple((-a, -b) for a, b in table)
        if table > flip:
            continue
        original = signs[table]
        other = signs[flip]
        direction = tuple(original["marginal_differences_A0_A1_B0_B1"])
        assert direction == tuple(-d for d in other["marginal_differences_A0_A1_B0_B1"])
        weight = tuple(map(Q, original["affine_weight_in_c"]))
        assert weight == tuple(map(Q, other["affine_weight_in_c"]))
        pairs.append((table, direction, tuple(2 * w for w in weight)))
    assert 2 * len(pairs) == len(raw)
    assert sorted(direction.count(0) for _, direction, _ in pairs) == [3] * 4 + [4] * 4
    assert sorted(next(i for i,d in enumerate(direction) if d) for _, direction, _ in pairs if any(direction)) == list(range(4))
    return pairs


def positive_inside_c_interval(affine):
    constant, slope = affine
    # 2/5 < sqrt(2)-1 < 5/12, proven by squaring 7/5 and 17/12.
    assert Q(7, 5)**2 < 2 < Q(17, 12)**2
    return min(constant + slope*Q(2,5), constant + slope*Q(5,12)) > 0


def run(frozen):
    assert sha256(frozen).hexdigest() == "2a7456dff338ef83f6616e542e3dcaa5af370fdea5b4812cd50bdcd8b8ce790f"
    paired = table_pairs(frozen)
    budgets = []
    check_count = 0
    for size in range(1, 9):
        for count in range(1, size+1):
            blocks = partition(size, count)
            margin, checked = direction_margin(tuple(binary_rows(blocks)), size)
            assert margin == Q(2, (1 << max(blocks)) - 1)
            check_count += checked
            budgets.append({"pairs": size, "preparations": count, "tested_directions": checked,
                            "block_sizes": blocks, "margin_over_tv_radius": str(margin)})

    eps = Q(1, 1024)
    (row, denominator), = binary_rows((len(paired),))
    signals = []
    for component in range(4):
        val = 2 * eps * Q(sum(row[j] * directions[component]
                             for j, (_, directions, _) in enumerate(paired)), denominator)
        signals.append(str(val))
    assert all(Q(x) != 0 for x in signals)

    for weight, (_, _, mass) in zip(row, paired):
        delta = eps * Q(weight, denominator)
        assert positive_inside_c_interval((mass[0]/2 - delta, mass[1]/2))

    masses = [q for _, _, q in paired]
    ordered = sorted(masses, key=lambda w: w[0] + w[1]*Q(49,120), reverse=True)
    assert all(positive_inside_c_interval((a-c,b-d)) for (a,b),(c,d) in zip(ordered,ordered[1:]) if (a,b)!=(c,d))
    leftovers = []
    for count in range(len(ordered)+1):
        untested = tuple(sum(w[i] for w in ordered[count:]) for i in range(2))
        below = positive_inside_c_interval((-untested[0], 1-untested[1]))
        leftovers.append({"tests": count, "remaining_affine_mass_in_c": tuple(map(str, untested)),
                          "strictly_below_c": below})
    assert next(x["tests"] for x in leftovers if x["strictly_below_c"]) == 5
    assert leftovers[4]["remaining_affine_mass_in_c"] == ("0", "1")
    return {
        "frozen_support_sha256": sha256(frozen).hexdigest(),
        "paired_tables": [{"first_output_table": q, "directions": d, "pair_affine_mass_in_c": tuple(map(str,w))}
                          for q,d,w in paired],
        "binary_design_counts": budgets,
        "total_exact_direction_checks": check_count,
        "dense_epsilon": str(eps),
        "actual_frozen_four_signed_marginal_changes": signals,
        "scalar_chsh_maximum_by_number_of_largest_mass_pairs_tested": leftovers,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("frozen", type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.frozen.read_bytes()), indent=2, sort_keys=True))
