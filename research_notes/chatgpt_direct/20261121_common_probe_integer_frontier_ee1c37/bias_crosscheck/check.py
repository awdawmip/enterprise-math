"""Small same-team cross-check; does not rerun native or cover enumeration."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import argparse
import json


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bias', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    root = args.bias.resolve()
    consulted = set()

    def read(name):
        candidates = [root / 'verification' / name, root / name]
        if name.startswith('exact_traces/'):
            pair = Path(name).stem
            candidates.append(root / 'verification' / f'intake_{pair}.stdout')
        path = next((candidate for candidate in candidates if candidate.exists()), None)
        assert path is not None, name
        consulted.add(str(path.relative_to(root)))
        return path.read_text()

    actual = {}
    typed_count = absolute_count = 0
    for line in read('signed_catalog.txt').splitlines():
        size, embedded, cost, *values = map(int, line.split())
        assert values == sorted(set(values)) and values
        assert all(0 <= v <= cost and (cost - v) % 2 == 0 for v in values)
        actual.setdefault((size, cost), set()).update(values)
        typed_count += 1
        absolute_count += len(values)
    projected = {key: max(values) for key, values in actual.items()}
    catalog_path = 'proof/inputs/catalog.txt' if (root / 'proof/inputs/catalog.txt').exists() else 'inputs/catalog.txt'
    catalog = read(catalog_path).splitlines()
    assert int(catalog[0]) == len(catalog) - 1
    reference = {(s, c): d for s, c, d in map(lambda line: map(int, line.split()), catalog[1:])}
    assert projected == reference

    def possible(spec, target):
        """Generating function in the loss from each class's maximum delta."""
        full = sum(s == 13 for s, c, d in spec)
        if full >= 5:
            return False
        budget = sum(d for s, c, d in spec) - target
        if budget < 0:
            return False
        cap = min((11, 7, 6, 4, 3)[full], 6 if sum(c for s, c, d in spec) < 11925 else 11)
        states = {(0, 0, 0)}
        for size, cost, maximum in spec:
            assert maximum == projected[size, cost]
            choices = {(maximum - sign * value,
                        int(size == 11 and cost == 1059 and sign * value == 179),
                        int(size == 11 and cost == 1042 and sign * value == 142))
                       for value in actual[size, cost] for sign in (-1, 1)}
            nxt = set()
            for loss, high, middle in states:
                for dl, dh, dm in choices:
                    l, h, m = loss + dl, high + dh, middle + dm
                    if l > budget or h > cap:
                        continue
                    if full >= 3 and h >= 4 and m >= 1:
                        continue
                    if full >= 2 and h >= 5 and m >= 2:
                        continue
                    nxt.add((l, h, m))
            states = nxt
        return any(loss == budget for loss, h, m in states)

    bounds = {}
    initial = {}
    for line in read('packing_layer_bounds.txt').splitlines():
        cost, maximum = map(int, line.split())
        if cost < 11301:
            continue
        value = min(maximum, 108 + 2 * (cost - 11292) - 1)
        value -= (value - cost) % 2
        initial[cost] = value
        bounds[cost] = min(value, {11825: 1171, 11823: 1167, 11821: 1163}.get(cost, value))

    geometric = []
    for cost, value, expected_survivors in [(11825, 1173, 1), (11823, 1169, 1), (11821, 1165, 2)]:
        assert initial[cost] == value
        name = f'exact_traces/{cost}_{value}.txt'
        spectra = [[tuple(map(int, word.split(':'))) for word in line.split()[1:]]
                   for line in read(name).splitlines()]
        survivors = [spec for spec in spectra if possible(spec, value)]
        assert len(survivors) == expected_survivors
        receipts = json.loads(read(f'endpoint_{cost}_result.json'))
        assert len(receipts) == 2 * expected_survivors
        for row in receipts:
            assert row['completed'] and row['counts'][-1] == 0 and not row['stdout']
            assert row['sign'] in (-1, 1)
        geometric.append({'cost': cost, 'difference': value, 'spectra': len(spectra),
                          'remaining_before_geometry': survivors,
                          'finished_geometric_receipts': len(receipts)})

    boundary = json.loads(read('exact_boundary_result.json'))
    checked = 0
    for row in boundary['records']:
        minimum = min((Fraction(c - 11292, d - 108), c, d)
                      for c, d in bounds.items() if d > 108)
        assert minimum == (Fraction(row['radius']), row['cost'], row['difference'])
        name = f"exact_traces/{row['cost']}_{row['difference']}.txt"
        trace = read(name)
        assert sha256(trace.encode()).hexdigest() == row['trace_sha256']
        specs = [[tuple(map(int, word.split(':'))) for word in line.split()[1:]]
                 for line in trace.splitlines()]
        assert len(specs) == row['spectrum_count'] == len(row['cases'])
        for spec, case in zip(specs, row['cases']):
            assert spec == [tuple(v) for v in case['spectrum']]
            assert len(spec) == 11 and sum(s for s, c, d in spec) == 125
            assert sum(c for s, c, d in spec) == row['cost']
            assert possible(spec, row['difference']) == case['possible_in_signed_relaxation']
            checked += 1
        assert row['all_excluded'] == all(not c['possible_in_signed_relaxation'] for c in row['cases'])
        if row['all_excluded']:
            bounds[row['cost']] = row['difference'] - 2
    radius = Fraction(boundary['certified_radius'])
    assert radius == Fraction(525, 1049)
    assert Fraction(12501 - 11292, 1611 - 108) > radius
    result = {
        'kind': 'SAME_TEAM_MATHEMATICAL_CROSSCHECK',
        'formal_independent_review': False,
        'review_status_unchanged': 'NOT_REVIEWED',
        'large_search_rerun': False,
        'status': 'PASS_WITH_ENDPOINT_EQUALITY_EXPLICITLY_OPEN',
        'catalog_typed_entries': typed_count,
        'catalog_absolute_delta_entries': absolute_count,
        'catalog_size_cost_projection': len(projected),
        'boundary_spectra_checked_by_independent_loss_generating_function': checked,
        'geometric_pairs': geometric,
        'radius': str(radius),
        'p_interval': [str((1 - radius) / 2), str((1 + radius) / 2)],
        'outer_endpoint_extra_ties': 'UNRESOLVED',
        'remaining_pair': boundary['remaining_pair'],
        'inputs_sha256': {name: digest(root / name) for name in sorted(consulted)},
        'checker_sha256': digest(Path(__file__)),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('inputs_sha256', 'geometric_pairs')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
