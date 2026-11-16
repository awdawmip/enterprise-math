"""Exact minimax depths for the 729 R762CA policies and the declared probe menus.

Run with Python 3.10+. Port 2 is the minority sign in either mixed representative.
Each rooted probe returns exclusion separately from a disabled but closed root.
All readouts are exact unit-source counts, without sampling or measurement noise.
"""

from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, product


POLICIES = tuple(product((-1, 0, 7), (-1, 0, 7), range(-1, 8), range(-1, 8)))
POLICY_IDS = tuple(range(len(POLICIES)))
# -1 means excluded, 0 means closed with empty gate, 1 through 7 are Port masks.
ROOTS = tuple((o, p) for o in range(4) for p in range(1 if o < 2 else 3))


def global_readout(policy):
    counts = [0] * 4
    for mask, orbit_size in zip(policy, (1, 1, 3, 3)):
        if mask >= 0:
            counts[mask.bit_count()] += orbit_size
    n0 = sum(counts)
    n4 = sum(n * weight for n, weight in zip(counts, (0, 21, 138, 369)))
    return n0, n4


def rooted_readout(policy, root, mode):
    orbit, p = root
    mask = policy[orbit]
    if mask < 0:
        return "excluded"
    if not (mask & (1 << p)):
        return "disabled"
    if mode == "gate":
        return "enabled"
    if mode == "named":
        return mask
    k = mask.bit_count()
    if mode == "total":
        return k + 1
    same_sign_mask = 7 if orbit < 2 else (4 if p == 2 else 3)
    return k + 1, (mask & same_sign_mask).bit_count() + 1


def partition(ids, readout):
    cells = defaultdict(list)
    for idx in ids:
        cells[readout[idx]].append(idx)
    return tuple(tuple(members) for members in cells.values())


def minimax(readouts):
    @cache
    def depth(ids):
        if len(ids) == 1:
            return 0
        best = len(readouts) + 1
        for readout in readouts:
            children = partition(ids, readout)
            if len(children) > 1:
                best = min(best, 1 + max(depth(child) for child in children))
        # An unresolved family receives a sentinel larger than the whole menu.
        return best

    return depth


def smallest_fixed_designs(globals_by_id, rooted_readouts):
    for size in range(len(ROOTS) + 1):
        valid = []
        for probes in combinations(range(len(ROOTS)), size):
            signatures = {
                (globals_by_id[i], *(rooted_readouts[q][i] for q in probes))
                for i in POLICY_IDS
            }
            if len(signatures) == len(POLICIES):
                valid.append(probes)
        if valid:
            return valid
    raise AssertionError("All rooted probes and both global counts must separate.")


def main():
    globals_by_id = tuple(map(global_readout, POLICIES))
    global_columns = tuple(zip(*globals_by_id))
    fibers = partition(POLICY_IDS, globals_by_id)
    assert len(POLICIES) == 729 and len(fibers) == 90
    expected = {
        "gate": (9, 18, 9, 12, 18, 15, 9),
        "total": (9, 18, 9, 15, 24, 12, 3),
        "signed": (9, 18, 18, 18, 15, 9, 3),
        "named": (9, 18, 18, 18, 15, 9, 3),
    }
    for mode, expected_histogram in expected.items():
        columns = tuple(tuple(rooted_readout(x, r, mode) for x in POLICIES) for r in ROOTS)
        solve = minimax(columns)
        hist = Counter(solve(fiber) for fiber in fibers)
        depths = tuple(hist[i] for i in range(max(hist) + 1))
        hardest = sorted(globals_by_id[f[0]] for f in fibers if solve(f) == max(hist))
        designs = smallest_fixed_designs(globals_by_id, columns)
        free_depth = minimax(global_columns + columns)(POLICY_IDS)
        assert depths == expected_histogram and free_depth == 8
        assert len(designs) == 12 and all(len(v) == 6 for v in designs)
        for probes in designs:
            by_orbit = Counter(ROOTS[j][0] for j in probes)
            assert by_orbit[0] + by_orbit[1] == 1
            assert {by_orbit[2], by_orbit[3]} == {2, 3}
        if mode != "gate":
            assert hardest == [(7, 63), (7, 432), (8, 432)]
        print(f"{mode}: depth histogram {depths}; 12 fixed six-root designs; free-menu depth {free_depth}")

    hard = next(f for f in fibers if globals_by_id[f[0]] == (7, 63))
    assert len(hard) == 12
    print("729 policies; 90 return spectra; (7,63) has 12 policies, worst residual depth 6.")


if __name__ == "__main__":
    main()
