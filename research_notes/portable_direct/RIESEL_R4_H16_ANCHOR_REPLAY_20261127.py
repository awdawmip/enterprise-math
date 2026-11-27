"""Check the four-slot h16 template and the named 12/13 switch at order 2304."""

from collections import Counter
from itertools import combinations
import json
from math import gcd, lcm, prod
from pathlib import Path
from runpy import run_path


HERE = Path(__file__).parent
SHARED = run_path(str(HERE / "RIESEL_R4_H20_ANCHOR_REPLAY_20261127.py"))
INPUTS = HERE / "RIESEL_R4_H20_ANCHOR_INPUTS_20261127.json"
FAMILY = (64, 192, 576)
SMALL_STABLE = (3457, 816769)
GOLDILOCKS = 18446744069414584321
STABLE = ((3457, 576, 4), (816769, 576, 8), (GOLDILOCKS, 192, 12))


def main():
    phase, tail, hits, prime, exact_order, carrier = (
        SHARED[name] for name in ("phase", "tail", "hits", "prime", "exact_order", "primitive_carrier")
    )
    source = json.loads(INPUTS.read_text())
    a4, s4 = int(source["A4"]), int(source["S4"])
    fixed = set(map(int, source["fixed_primes"]))
    dictionaries = source["dictionary"]
    prefix = source["prefix"]
    fixed_tails = source["fixed_tails"]
    expected_active = set(dictionaries + prefix + fixed_tails)
    assert len(fixed) == 74 and 6 * prod(fixed) == s4 and a4 % 6 == 3
    assert expected_active <= fixed and all(a4 % q == 0 for q in fixed - expected_active)
    trial_proven = expected_active | set(SMALL_STABLE) | {274177, 18433, 101377}
    assert all(prime(q) for q in trial_proven)

    # A full q-1 order certificate also proves primality of this named anchor.
    gold_factors = (2, 3, 5, 17, 257, 65537)
    assert all(prime(q) for q in gold_factors)
    assert GOLDILOCKS - 1 == 2**32 * prod(gold_factors[1:])
    assert pow(7, GOLDILOCKS - 1, GOLDILOCKS) == 1
    assert all(gcd(pow(7, (GOLDILOCKS - 1) // q, GOLDILOCKS) - 1, GOLDILOCKS) == 1
               for q in gold_factors)
    assert all(q not in fixed and exact_order(q, d) and d // gcd(d, 36) == 16
               for q, d, _ in STABLE)

    dict_rows = [phase(q, a4) for q in dictionaries]
    prefix_rows = [phase(q, a4) for q in prefix]
    tails = [phase(q, a4) for q in fixed_tails]
    for descriptor, (h, w) in zip(tails, ((2, 1), (3, 1), (4, 2))):
        assert descriptor[1] // gcd(descriptor[1], 36) == h and hits(descriptor, 32 + 36 * w)
    common_fixed = prefix_rows + [tails[0], tails[2]]
    optional = tails[1]
    old = fixed | {q for q, _, _ in STABLE}
    period = lcm(36 * 35, *(d for _, d, _ in dict_rows + prefix_rows + tails))
    assert lcm(*(d for _, d, _ in dict_rows)) == 6720
    holes = set(source["holes_mod35"])
    for n in range(1, period + 1):
        in_third = n % 36 == 32 and ((n - 32) // 36) % 35 in holes
        assert in_third == (not any(hits(row, n) for row in dict_rows + prefix_rows))
        in_slots = in_third and ((n - 32) // 36) % 4 == 0
        assert in_slots == (not any(hits(row, n) for row in dict_rows + common_fixed))

    fixed_witnesses = [int(n) for n in source["private_indices"][:6]]
    for (label, _, _), n in zip(common_fixed, fixed_witnesses):
        assert n % 16 != 0
        assert [row[0] for row in dict_rows + common_fixed + [optional] if hits(row, n)] == [label]
    assert 0 in holes and lcm(16, 35, 3) == 1680
    for a in (0, 4, 8, 12):
        sample = 105 * a
        assert sample % 16 == a and sample % 3 == 0 and sample % 35 == 0
        assert not any(hits(row, 32 + 36 * sample) for row in dict_rows + common_fixed + [optional])

    # The primitive order-64 number is exhausted by two dictionary primes.
    assert carrier(64, 1) == 641 * 6700417 and {641, 6700417} <= set(dictionaries)
    comparisons = {}
    for base in FAMILY:
        checks = 0
        for q in old:
            d = base * 2
            while (q - 1) % d == 0:
                assert not exact_order(q, d)
                checks += 1
                d *= 2
        comparisons[base] = checks
    for d in (192, 576):
        assert all(not exact_order(q, d) for q in fixed if (q - 1) % d == 0)

    # One named factor plus a nontrivial coprime residual supplies two primes.
    duplicate_residuals = {}
    excluded = s4 * prod(q for q, _, _ in STABLE)
    for d, named in ((128, 274177), (2304, 18433)):
        assert named not in old and exact_order(named, d)
        assert carrier(d, excluded) % named == 0
        residual = carrier(d, excluded * named)
        assert residual > 1 and gcd(residual, named) == 1
        duplicate_residuals[d] = residual.bit_length()
    for depth in range(1, 9):
        for j in range(1, depth + 1):
            SHARED["check_tree"](depth, j)
        zero_counts = Counter(j for j, _ in SHARED["comb"](depth))
        zero_counts[1] += 2
        assert all(used <= (4 if j == 1 else 3) for j, used in zero_counts.items())

    sibling = carrier(256, excluded)
    repair = carrier(512, excluded)
    assert sibling > 1 and repair > 1 and exact_order(sibling, 256) and exact_order(repair, 512)
    assert exact_order(101377, 4608) and 101377 not in old
    q_star = 18433
    slots = [(274177, 128, 1), (sibling, 256, 2), (q_star, 2304, 0),
             (repair, 512, 0), (101377, 4608, 4)]
    raw_slots = [tail(q, d, 16 * u) for q, d, u in slots]
    stable_rows = [tail(q, d, a) for q, d, a in STABLE]
    assert all(r % 16 == 0 and d % 64 == 0 for _, d, r in stable_rows + raw_slots)
    new_moduli = [q for q, _, _ in raw_slots]
    assert all(gcd(x, y) == 1 for x, y in combinations(new_moduli, 2))
    assert all(gcd(q, excluded) == 1 for q in new_moduli)
    extras = common_fixed + [optional] + stable_rows + raw_slots
    replay_period = lcm(period, *(d for _, d, _ in extras))
    opened = SHARED["minimum_cover"](dict_rows, extras, replay_period)
    closed = SHARED["minimum_cover"](dict_rows, [row for row in extras if row[0] != q_star], replay_period)
    assert (opened["cost"], closed["cost"]) == (12, 13)
    print(json.dumps({
        "fixed_labels": len(fixed),
        "trial_proven_names": len(trial_proven),
        "order192_certificate_base": 7,
        "fixed_private_indices": fixed_witnesses,
        "private_w_progressions": [[105 * a, 1680] for a in (0, 4, 8, 12)],
        "positive_depth_old_slot_comparisons": comparisons,
        "duplicate_order_coprime_residual_bits": duplicate_residuals,
        "verified_tree_depths": 8,
        "named_switch_prime": q_star,
        "named_switch_order": 2304,
        "effective_period": 64,
        "finite_replay_period": replay_period,
        "named_switch_phases": [[str(q), d, r] for q, d, r in raw_slots],
        "opened": opened,
        "closed": closed,
    }, indent=2))


if __name__ == "__main__":
    main()
