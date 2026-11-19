"""Exact residue windows and one independently reconstructed N1 operation."""
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from tempfile import TemporaryDirectory


SOURCE = {
    'test_native_pointer.py': '09eae3e08308e3041416daaca5a951b7c632104bbe7fa21200b11d57b6b568e9',
    'parent/test_mod7_only.py': 'b0fa9b4f9b96480d5cf409f15d5f7f07afc993b6ca57b74bce7811e93adb93c7',
    'parent/parent_M5/wave_compare.py': 'fd2f6f73d3d0af1df9b4a2bf771b8574c06d03e9df5bd33310394967f5d2cfd2',
    'parent/parent_M5/vendor/brc_division_excerpt.py': 'db9a41d7087e6e042f5330d39815dedd504a49fcb2db30048f0e3f55b8472bb4',
    'parent/parent_M5/vendor/brc_weighted_recurrent.py': '7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26',
    'parent/parent_M5/vendor/division.py': '4421c6dc9acfaa61492137951e543973c010c6a127655126152cc18763cc35e9',
}
CELLS = list(itertools.product(range(3), repeat=6))
SLOTS = {v: i for i, v in enumerate(CELLS)}


def route(x, z, contact):
    """One edge along each changed coordinate in the source contact's order."""
    edges = []
    for offset in range(6):
        axis = (contact + offset) % 6
        start = list(CELLS[x])
        target = CELLS[z][axis]
        change = (target - start[axis]) % 3
        if not change:
            continue
        direction = axis if change == 1 else axis + 6
        start[axis] = target
        end = SLOTS[tuple(start)]
        edges.append([x, direction, end])
        x = end
    assert x == z
    return edges


def direct_prefix():
    modulus = 77
    actors = [1, 1]
    budget = 21 * modulus
    summaries, plans = [], []
    for tick in range(1, 6):
        steps = []
        for actor, stride in enumerate((1, 2)):
            for sub in range(stride):
                y = actors[actor]
                q, z = divmod(2 * y, modulus)
                path = route(y, z, (tick - 1) % 3)
                steps.append(dict(actor=actor, subaction=sub, old=y, quotient=q,
                                  new=z, path=path, transfer_cost=1 + len(path)))
                actors[actor] = z
        hops = sum(len(s['path']) for s in steps)
        budget -= 3 + hops
        summaries.append([tick, *actors, hops, budget])
        plans.append(steps)
    return summaries, plans


def window(y, m, k):
    reads = [y % 7]
    for _ in range(k):
        y = 2 * y % m
        reads.append(y % 7)
    return tuple(reads)


def decode(reads, m):
    r = reads[0]
    bin_index = 0
    for previous, following in zip(reads, reads[1:]):
        delta = (2 * previous - following) % 7
        assert delta in (0, m % 7)
        bin_index = 2 * bin_index + int(delta != 0)
    return r, bin_index


def validate_windows():
    count = 0
    for m in range(1, 258):
        for k in range(9):
            words = Counter()
            for y in range(m):
                reads = window(y, m, k)
                words[reads] += 1
                count += 1
                if m % 7:
                    assert decode(reads, m) == (y % 7, (2**k * y) // m)
                else:
                    assert reads == tuple((2**j * y) % 7 for j in range(k + 1))
            if m % 7:
                cells = 7 * (2**k)
                q, r = divmod(m, cells)
                hist = Counter(words.values())
                hist[0] += cells - len(words)
                assert hist == Counter({q: cells-r, q+1: r})
            else:
                assert set(words.values()) == {m // 7}
    return count


def case_orbits():
    result = []
    for m in (15, 21, 35, 77, 143):
        orbit = [1]
        while (z := 2 * orbit[-1] % m) != 1:
            assert z not in orbit
            orbit.append(z)
        counts = [len({window(y, m, k) for y in orbit}) for k in range(8)]
        if m % 7 == 0:
            assert counts == [3] * 8
        else:
            assert len(orbit) in counts
        result.append({'M': m, 'period': len(orbit), 'counts_for_k_0_through_7': counts})
    return result


def separation():
    m, y = 77, 16
    units = [b for b in range(m) if math.gcd(m, b) == 1 and b % 7 == 2]
    pairs = {}
    true_axes = [d % 6 for _, d, _ in route(y, 32, 1)]
    for b in units:
        z = b * y % m
        path = route(y, z, 1)
        if [d % 6 for _, d, _ in path] == true_axes:
            pairs[b] = {'target': z, 'path': path, 'cost': 1+len(path)}
        for x in range(m):
            assert (b*x % m) % 7 == (2*x % m) % 7
    assert set(pairs) == {2, 72}
    assert set([32, 74]) <= {pow(2, j, m) for j in range(30)}
    signs = [j for j in range(4) if pairs[2]['path'][j][1] != pairs[72]['path'][j][1]]
    assert signs == [0, 1, 2]
    return {'units': units, 'same_unsigned_axes': pairs, 'distinguishing_indices_zero_based': signs}


def replay_original(file, rows, plans):
    file = file.resolve()
    for relative, digest in SOURCE.items():
        assert hashlib.sha256((file.parent / relative).read_bytes()).hexdigest() == digest
    spec = importlib.util.spec_from_file_location('brc_n1_doubling_reference', file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert list(module.CELLS) == CELLS
    with TemporaryDirectory() as tmp:
        atlas, codes = module.schema_codes(Path(tmp))
        arithmetic = module.TraceArithmetic()
        arena = module.Arena(atlas, codes, arithmetic, 'pointer')
        world = module.NativeCandidate(77, 2, arena, arithmetic)
        for tick, actors_left, actors_right, hops, remaining in rows:
            assert world.step() is False
            expected = plans[tick-1]
            for event, record in zip(world.events[-3:], expected, strict=True):
                assert all(event[key] == value for key, value in record.items())
                assert event['product'] == 2 * record['old']
                assert event['source_slot'] == record['old'] and event['target_slot'] == record['new']
            row = world.summary[-1]
            assert [row[k] for k in ('heartbeat','left','right','native_hops','energy')] == [
                tick, actors_left, actors_right, hops, remaining]
            assert row['internal'] == 21 * 77 - remaining
        assert len(world.events) == 15 and len(world.frames) == 6


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--native', type=Path, help='pinned original test_native_pointer.py with its parent modules')
    args = parser.parse_args()
    rows, plans = direct_prefix()
    if args.native:
        replay_original(args.native, rows, plans)
    values = {'native_reference_sha256': SOURCE, 'independent_prefix': {
        'columns': ['tick', 'left', 'right', 'edge_hops_all_three_actions', 'shared_remaining'],
        'rows': rows, 'selected_action': plans[4][0]},
        'single_operation_ambiguity': separation(), 'native_orbit_observation_counts': case_orbits(),
        'finite_window_sweep': {'moduli': [1,257], 'transition_counts': [0,8],
                                'state_windows_checked': validate_windows()}}
    print(json.dumps(values, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
