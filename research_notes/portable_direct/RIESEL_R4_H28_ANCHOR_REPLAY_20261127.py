"""Replay both renormalized Riesel anchors and the named 12/13 switch."""

import json
from math import gcd, lcm, prod
from pathlib import Path
from runpy import run_path


HERE = Path(__file__).parent
SHARED = run_path(str(HERE / "RIESEL_R4_H20_ANCHOR_REPLAY_20261127.py"))
INPUTS = HERE / "RIESEL_R4_H20_ANCHOR_INPUTS_20261127.json"
RECIPES = ((1009, 0, 56), (21169, 24, 276))
FAMILY = (112, 336, 1008)
NEW = ((449, 224, 0), (2689, 224, 1), (494968321, 1344, 0), (663239809, 1344, 2))


def main():
    phase, tail, hits = (SHARED[name] for name in ("phase", "tail", "hits"))
    prime, exact_order, carrier = (SHARED[name] for name in ("prime", "exact_order", "primitive_carrier"))
    source = json.loads(INPUTS.read_text())
    a4, s4 = int(source["A4"]), int(source["S4"])
    fixed = set(map(int, source["fixed_primes"]))
    low = {q for q, _, _ in source["free_anchors"]}
    old = fixed | low
    assert len(fixed) == 74 and 6 * prod(fixed) == s4 and a4 % 6 == 3
    assert not fixed & low
    pool = set(source["dictionary"] + source["prefix"] + source["fixed_tails"])
    assert pool <= fixed
    assert all(a4 % q == 0 for q in fixed - pool)
    named = pool | low | {q for q, _, _ in NEW}
    assert all(prime(q) for q in named)

    dictionary = [phase(q, a4) for q in source["dictionary"]]
    prefix = [phase(q, a4) for q in source["prefix"]]
    fixed_phases = [phase(q, a4) for q in source["fixed_tails"]]
    free_phases = [tail(q, d, w) for q, w, d in source["free_anchors"]]
    assert all(exact_order(q, d) for q, d, _ in free_phases)
    auxiliary = 246241
    all_anchors = prefix + fixed_phases + free_phases
    common_hole = carrier(5040, s4 * prod(low))
    assert common_hole > 1 and exact_order(common_hole, 5040)
    assert gcd(common_hole, s4 * prod(low)) == 1
    hole = common_hole, 5040, 3488
    period = lcm(112, 5040, *(d for _, d, _ in dictionary + all_anchors))
    assert period == 60480 and lcm(*(d for _, d, _ in dictionary)) == 6720

    for descriptor, (h, w) in zip(fixed_phases, ((2, 1), (3, 1), (4, 2))):
        assert descriptor[1] // gcd(descriptor[1], 36) == h and hits(descriptor, 32 + 36 * w)
    assert all(d // gcd(d, 36) == 28 for d in FAMILY)
    phase_period = lcm(35, 140, 28, *(d // gcd(d, 36) for _, d, _ in fixed_phases + free_phases))
    assert phase_period == 420 and phase_period // 28 == 15
    cutoff_holes = set(source["holes_mod35"])
    for n in range(1, period + 1):
        residual = n % 36 == 32 and ((n - 32) // 36) % 35 in cutoff_holes
        assert residual == (not any(hits(row, n) for row in dictionary + prefix))

    anchor_order = source["prefix"] + [source["fixed_tails"][0], source["fixed_tails"][2]]
    anchor_order += [q for q, _, _ in source["free_anchors"]]
    private = dict(zip(anchor_order, map(int, source["private_indices"])))
    assert all(n % 560 != 3488 % 560 for n in private.values())

    inventory_compares = {}
    for base in FAMILY:
        checks = 0
        for q in old:
            d = base
            while (q - 1) % d == 0:
                assert not exact_order(q, d)
                checks += 1
                d *= 2
        inventory_compares[base] = checks
    assert len({q for q, _, _ in NEW}) == 4
    assert all(q not in old and exact_order(q, d) for q, d, _ in NEW)
    for depth in range(1, 9):
        for j in range(1, depth + 1):
            SHARED["check_tree"](depth, j)

    old_without_aux = [row for row in all_anchors if row[0] != auxiliary]
    reports = []
    for old_label, new_w, witness_w in RECIPES:
        assert private[old_label] == 32 + 36 * witness_w
        assert witness_w % 28 == new_w
        inherited = [row for row in all_anchors if row[0] != old_label]
        geometric_anchor = tail(old_label, 112, new_w)
        new_without_aux = [row for row in inherited if row[0] != auxiliary] + [geometric_anchor]
        for n in range(1, period + 1):
            old_hole = not any(hits(row, n) for row in dictionary + old_without_aux)
            new_hole = not any(hits(row, n) for row in dictionary + new_without_aux)
            assert old_hole == new_hole == hits(hole, n)
        for q, n in private.items():
            assert [row[0] for row in dictionary + inherited + [geometric_anchor, hole]
                    if hits(row, n)] == [q]
        assert not hits(geometric_anchor, 3488) and 560 % 112 == 0
        assert [row[0] for row in dictionary + inherited + [geometric_anchor, hole]
                if hits(row, 3488)] == [common_hole]

        before = [row for row in inherited if row[0] not in prefix]
        assert [row[0] for row in before if hits(row, 32 + 36 * witness_w)] == []
        assert all(phase_period % (d // gcd(d, 36)) == 0 for _, d, _ in before + [hole])
        assert witness_w % 35 in cutoff_holes
        added = [tail(q, d, new_w + 28 * u) for q, d, u in NEW]
        active = inherited + [hole] + added
        assert all(period % d == 0 for _, d, _ in active)
        opened = SHARED["minimum_cover"](dictionary, active, period)
        closed = SHARED["minimum_cover"](dictionary, [row for row in active if row[0] != 449], period)
        assert (opened["cost"], closed["cost"]) == (12, 13)
        reports.append({"replaced_anchor": old_label, "w_phase_mod28": new_w,
                        "n_phase_mod112": geometric_anchor[2],
                        "private_w_progression": [witness_w, phase_period],
                        "new_label_phases": added, "opened": opened, "closed": closed})

    print(json.dumps({"verified_named_primes": len(named),
                      "fixed_labels": len(fixed), "phase_replay_period": period,
                      "carrier_bits": common_hole.bit_length(), "old_slot_comparisons": inventory_compares,
                      "tree_depths_replayed": 8, "switch_prime": 449, "switch_order": 224,
                      "effective_period": 56, "recipes": reports}, indent=2))


if __name__ == "__main__":
    main()
