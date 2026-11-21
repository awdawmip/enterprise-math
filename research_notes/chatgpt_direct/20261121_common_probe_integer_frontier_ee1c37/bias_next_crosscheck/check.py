#!/usr/bin/env python3
"""Same-team small exact audit; no geometry/packing search is rerun.

The forward loss generating function below is separate from the author's
backward signed-sum recursion.  Native catalogue and geometry completeness
remain inherited, explicitly identified inputs.
"""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import argparse
import ast
import json
import struct


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', type=Path, required=True)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--prior-audit', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base, checkpoint = args.base.resolve(), args.checkpoint.resolve()
    consulted = {}

    def read(root, name):
        path = root / name
        label = ('base/' if root == base else 'checkpoint/') + name
        consulted[label] = digest(path)
        return path.read_text()

    def data(root, name):
        return json.loads(read(root, name))

    old_audit = json.loads(args.prior_audit.read_text())
    assert old_audit['formal_independent_review'] is False
    assert old_audit['radius'] == '525/1049'
    bindings = data(checkpoint, 'BASE_BINDINGS.json')
    for name, expected in bindings['sha256'].items():
        assert digest(base / name) == expected
        consulted['base/' + name] = expected
    for name, expected in bindings['base_input_bindings'].items():
        assert digest(base / 'inputs' / name) == expected
        consulted['base/inputs/' + name] = expected

    receipt = data(checkpoint, 'verification/receipt.json')
    assert receipt['complete'] and receipt['review_status'] == 'NOT_REVIEWED'
    for name in ('README.md', 'replay.py', 'exact_boundary.py'):
        read(checkpoint, name)
    commands = {row['name']: row for row in receipt['commands']}
    assert len(commands) == len(receipt['commands'])
    for name, row in commands.items():
        assert row['returncode'] == 0
        for suffix in ('stdout', 'stderr'):
            path = checkpoint / 'verification' / (name + '.' + suffix)
            assert digest(path) == row[suffix + '_sha256']
            consulted['checkpoint/verification/' + path.name] = digest(path)

    actual, typed = {}, {}
    typed_count = abs_count = 0
    for line in read(base, 'signed_catalog.txt').splitlines():
        size, embedded, cost, *values = map(int, line.split())
        assert values == sorted(set(values)) and values
        assert all(0 <= v <= cost and (cost - v) % 2 == 0 for v in values)
        actual.setdefault((size, cost), set()).update(values)
        typed.setdefault((size, embedded), set()).add(cost)
        typed_count += 1
        abs_count += len(values)
    maximum = {key: max(values) for key, values in actual.items()}
    original = read(base, 'inputs/catalog.txt').splitlines()
    assert int(original[0]) == len(original) - 1
    assert maximum == {(s, c): d for s, c, d in
                       (map(int, line.split()) for line in original[1:])}
    all_min = {s: min(c for ss, c in actual if s == ss) for s in range(1, 14)}
    all_max = {s: max(c for ss, c in actual if s == ss) for s in range(1, 14)}
    embedded_min = {s: min(cs) for (s, e), cs in typed.items() if e == 1}
    embedded_max = {s: max(cs) for (s, e), cs in typed.items() if e == 1}
    # The only unrestricted-small sizes actually used by the new kernels.
    exc_min = [0, 0, 12, 36, 72, 120, 201, 292, 419, 557, 744, 1008, 1244, 99999]
    assert all(exc_min[s] == all_min[s] for s in (1, 8, 9, 10))

    families = data(checkpoint, 'cover_families.json')
    assert len(families) == 24 and len({f['id'] for f in families}) == 24
    extra = {'id': 'hl5_k1_s10_e12_12_12_13', 'small': [10], 'H_or_L': 5,
             'K': 1, 'E': [12, 12, 12, 13], 'source': 'cover_hlk.cpp',
             'receipt': 'hl5_k1_s10_e12_12_12_13_result.json', 'nodes': 1136063}
    completed = data(checkpoint, 'verification/completion_receipts.json')
    assert len(completed) == 50
    completed_index = {(r['family'], r['sign']): r for r in completed}
    assert len(completed_index) == 50
    family_audit = []
    for family in families + [extra]:
        q, small, embedded = family['H_or_L'], family['small'], family['E']
        count_k = family.get('K', 0)
        p_sizes = sorted(small + [11] * (q + count_k))
        assert len(p_sizes) + len(embedded) == 11
        assert sum(p_sizes) + sum(embedded) == 125
        assert min(embedded) >= 11
        deficiency = 13 * len(embedded) - sum(embedded)
        assert deficiency < min(p_sizes)
        # union.cpp returns early upon reaching target: this strict bound
        # ensures that cannot happen before exactly len(E) mothers are chosen.
        assert sum(embedded) > 13 * (len(embedded) - 1)
        upper = q * 1059 + count_k * 1126
        upper += sum(all_max[s] for s in small)
        upper += sum(embedded_max[s] for s in embedded)
        if 'total_cost_upper_bound' in family:
            assert upper == family['total_cost_upper_bound']
        source = read(checkpoint, family['source'])
        assert 'if(biasQ)' in source
        rows = data(checkpoint, family['receipt'])
        assert {row['sign'] for row in rows} == {-1, 1} and len(rows) == 2
        used_budget, frame_count = None, None
        for index, row in enumerate(rows):
            cmd = row['command']
            assert sorted(map(int, cmd[5].split(','))) == p_sizes
            assert list(map(int, cmd[6].split(','))) == embedded
            assert int(cmd[7]) <= sum(embedded_min[s] for s in embedded)
            assert int(cmd[8]) >= upper
            assert int(cmd[9]) == 0 and int(cmd[11]) == 0
            assert int(cmd[14]) == row['sign']
            frame_name = Path(cmd[4]).name
            frame_text = read(checkpoint, 'verification/' + frame_name)
            frames = {tuple(map(int, line.split())) for line in frame_text.splitlines()}
            assert len(frames) == len(frame_text.splitlines()) == int(cmd[10])
            assert all(len(set(frame)) == len(embedded) for frame in frames)
            assert row['complete'] and not row['stdout']
            assert row['counts'][0] == len(frames) and row['counts'][-1] == 0
            assert completed_index[family['id'], row['sign']]['counts'] == row['counts']
            stem = 'hl5_k1' if count_k else family['id']
            live = commands[stem + '_' + str(index)]
            assert live['command'][5:] == cmd[5:]
            assert not read(checkpoint, 'verification/' + stem + '_' + str(index) + '.stdout')
            assert list(map(int, read(checkpoint, 'verification/' + stem + '_' + str(index) + '.stderr').split())) == row['counts']
            used_budget, frame_count = int(cmd[8]), len(frames)
        assert sum(row['counts'][1] for row in rows) == family['nodes']
        family_audit.append({'id': family['id'], 'full_cost_upper_bound': upper,
                             'budget': used_budget, 'mother_deficiency': deficiency,
                             'smallest_remaining_class': min(p_sizes),
                             'canonical_frames': frame_count, 'signs': [-1, 1],
                             'completed_nodes': family['nodes']})
    assert sum(x['completed_nodes'] for x in family_audit) == receipt['completion_nodes'] == 6462523

    parents = [int(lo) + (int(hi) << 64) for lo, hi in
               (line.split() for line in read(base, 'inputs/parent').splitlines()[:250])]
    frames = {2: [(0, j) for j, mother in enumerate(parents) if not mother & parents[0]]}
    for f in (3, 4):
        frames[f] = [tuple(map(int, line.split())) for line in
                     read(base, f'inputs/f{f}_{13*f}').splitlines()]
    assert [len(frames[f]) for f in (2, 3, 4)] == [100, 15, 35]
    expected = {2: [6, 4, 4, 3, 2, 1, 0], 3: [4, 4, 2, 2, 0], 4: [2, 2, 1, 0]}
    joint = data(checkpoint, 'verification/joint_table.json')
    assert {(r['full_mothers'], r['H_count']) for r in joint} == {
        (f, h) for f, values in expected.items() for h in range(len(values))}
    new_nodes = 0
    template_functions = None
    table_audit = []
    for entry in joint:
        f, h = entry['full_mothers'], entry['H_count']
        if (f, h) == (2, 5):
            root, name = base, 'verification/mixed_two_result.json'
        elif (f, h) == (3, 4):
            root, name = base, 'verification/mixed_packing_result.json'
        else:
            root = checkpoint
            stem = f'mixed_{ {2:"two",3:"three",4:"four"}[f]}_h{h}'
            name = 'verification/' + stem + '_result.json'
            tree = ast.parse(read(checkpoint, stem + '.py'))
            functions = {node.name: ast.dump(node, include_attributes=False)
                         for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
            assert set(functions) == {'cd', 'shift', 'low_best', 'high_search'}
            if template_functions is None:
                template_functions = functions
            else:
                assert functions == template_functions
            start_calls = [node for node in ast.walk(tree)
                           if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                           and node.func.id == 'high_search' and len(node.args) == 4
                           and isinstance(node.args[1], ast.Constant)]
            assert len(start_calls) == 1 and start_calls[0].args[1].value == h
        assert digest(root / name) == entry['source_sha256']
        result = data(root, name)
        assert result['complete'] and result['max_additional_142'] == expected[f][h]
        assert entry['maximum_L'] == expected[f][h]
        assert {(r['sign'], r['frame']) for r in result['cases']} == {
            (sign, i) for sign in (-1, 1) for i in range(len(frames[f]))}
        assert len(result['cases']) == 2 * len(frames[f])
        assert result['nodes'] == sum(r['nodes'] for r in result['cases'])
        assert max(r['maximum_additional_142'] for r in result['cases']) == expected[f][h]
        if root == checkpoint:
            new_nodes += result['nodes']
        table_audit.append({'full_mothers': f, 'H_count': h, 'maximum_L': expected[f][h],
                            'both_sign_frame_cases': len(result['cases']),
                            'inherited': root == base})
    assert new_nodes == receipt['new_joint_packing_nodes'] == 19274334
    witnesses = data(checkpoint, 'verification/local_witnesses.json')
    assert len(witnesses) == 16
    for witness, entry in zip(witnesses, joint):
        f, h = entry['full_mothers'], entry['H_count']
        assert len(witness['full_mothers']) == f and len(witness['H']) == h
        assert len(witness['L']) == expected[f][h]
        assert witness['sign'] in (-1, 1)
        used = 0
        for mother in witness['full_mothers']:
            assert not used & parents[mother]
            used |= parents[mother]
        for mask in map(int, witness['H'] + witness['L']):
            assert mask.bit_count() == 11 and not mask & used
            used |= mask

    def possible(spec, target):
        """Coefficient support of a forward product in loss, H, L, K.

        Actual signed delta v contributes z^(maximum-v) H^flag L^flag K^flag.
        Every exponent is nonnegative; discard loss > the required budget.
        We use the explicit joint table, not the author's boolean predicates.
        """
        full = sum(s == 13 for s, c, d in spec)
        if full >= 5:
            return False
        cost = sum(c for s, c, d in spec)
        loss_budget = sum(d for s, c, d in spec) - target
        if loss_budget < 0:
            return False
        cap_h = min((11, 7, 6, 4, 3)[full], 6 if cost < 11925 else 11)
        embedded = sorted(s for s, c, d in spec
                          if s == 13 or (s == 12 and c in (1104, 1116))
                          or (s == 11 and c in (936, 944, 960)))
        small = sorted(s for s, c, d in spec if s < 11)
        limits = [family['H_or_L'] for family in families
                  if family['E'] == embedded and family['small'] == small]
        if limits:
            assert set(limits) == {11 - len(embedded) - len(small)}
        k_shape = embedded == [12, 12, 12, 13] and small == [10]

        def allowed(h, low, k):
            if h > cap_h:
                return False
            if full >= 2 and (h >= len(expected[full]) or low > expected[full][h]):
                return False
            if any(h + low >= limit for limit in limits):
                return False
            if k_shape and k >= 1 and h + low >= 5:
                return False
            return True

        states = {(0, 0, 0, 0)}
        for size, price, largest in spec:
            assert largest == maximum[size, price]
            choices = {(largest - sign * delta,
                        int((size, price, sign * delta) == (11, 1059, 179)),
                        int((size, price, sign * delta) == (11, 1042, 142)),
                        int((size, price, sign * delta) == (11, 1126, 114)))
                       for delta in actual[size, price] for sign in (-1, 1)}
            choices = {choice for choice in choices if choice[0] <= loss_budget}
            nxt = set()
            for loss, h, low, k in states:
                for dl, dh, db, dk in choices:
                    if loss + dl <= loss_budget and allowed(h + dh, low + db, k + dk):
                        nxt.add((loss + dl, h + dh, low + db, k + dk))
            states = nxt
        return any(loss == loss_budget for loss, h, low, k in states)

    # Restore exactly the previously certified envelope before the new 24 rows.
    bounds = {}
    for line in read(base, 'packing_layer_bounds.txt').splitlines():
        cost, delta = map(int, line.split())
        if cost < 11301:
            continue
        value = min(delta, 108 + 2 * (cost - 11292) - 1)
        value -= (value - cost) % 2
        bounds[cost] = min(value, {11825: 1171, 11823: 1167, 11821: 1163}.get(cost, value))
    inherited = data(base, 'verification/exact_boundary_result.json')
    for row in inherited['records']:
        if row['all_excluded']:
            bounds[row['cost']] = min(bounds[row['cost']], row['difference'] - 2)
    boundary = data(checkpoint, 'verification/exact_boundary_result.json')
    checked = 0
    boundary_audit = []
    for row in boundary['records']:
        minimum = min((Fraction(c - 11292, d - 108), c, d)
                      for c, d in bounds.items() if d > 108)
        assert minimum == (Fraction(row['radius']), row['cost'], row['difference'])
        trace_name = f"verification/exact_traces/{row['cost']}_{row['difference']}.txt"
        trace = read(checkpoint, trace_name)
        assert sha256(trace.encode()).hexdigest() == row['trace_sha256']
        specs = [[tuple(map(int, word.split(':'))) for word in line.split()[1:]]
                 for line in trace.splitlines()]
        assert len(specs) == row['spectrum_count'] == len(row['cases'])
        assert len({tuple(sorted(spec)) for spec in specs}) == len(specs)
        surviving = []
        for spec, case in zip(specs, row['cases']):
            assert spec == [tuple(v) for v in case['spectrum']]
            assert len(spec) == 11 and sum(s for s, c, d in spec) == 125
            assert sum(c for s, c, d in spec) == row['cost']
            assert sum(d for s, c, d in spec) >= row['difference']
            hit = possible(spec, row['difference'])
            assert hit == case['possible_in_signed_relaxation']
            if hit:
                surviving.append(spec)
            checked += 1
        assert row['all_excluded'] == (not surviving)
        boundary_audit.append({'cost': row['cost'], 'difference': row['difference'],
                               'radius': row['radius'], 'spectra': len(specs),
                               'survivors': surviving})
        if row['all_excluded']:
            bounds[row['cost']] = row['difference'] - 2
    assert len(boundary_audit) == 24 and checked == 2184
    assert sum(row['spectra'] for row in boundary_audit[:-1]) == 1943
    assert boundary_audit[-1]['spectra'] == 241 and len(boundary_audit[-1]['survivors']) == 3
    radius = Fraction(boundary['certified_radius'])
    assert radius == Fraction(479, 957)
    assert Fraction(12501 - 11292, 1611 - 108) > radius
    endpoint_pairs = [(11292 + t, 108 + d) for d in range(1, 1611 - 108 + 1)
                      for t in [(479 * d) // 957] if 957 * t == 479 * d and t >= 9]
    assert endpoint_pairs == [(11771, 1065)]
    assert radius - Fraction(1, 2) == Fraction(1, 1914)

    b11 = list(struct.iter_unpack('<QQQ', (base / 'inputs/B11').read_bytes()))
    assert len(b11) == 18920 and min(row[2] for row in b11) == 1008
    assert max(row[2] for row in b11) == 1376
    result = {
        'kind': 'SAME_TEAM_MATHEMATICAL_CROSSCHECK',
        'formal_independent_review': False, 'review_status_unchanged': 'NOT_REVIEWED',
        'large_geometry_or_packing_search_rerun': False,
        'native_catalog_completeness_and_frame_exhaustiveness': 'INHERITED_AND_SOURCE_AUDITED',
        'trace_enumeration_completeness': 'INHERITED_TRACE_SOURCE_AND_COMPLETED_RECEIPTS',
        'status': 'PASS_WITH_OUTER_ENDPOINT_EQUALITY_EXPLICITLY_OPEN',
        'catalog_typed_entries': typed_count, 'catalog_absolute_delta_entries': abs_count,
        'B11_total_origin_anchored_rows': len(b11),
        'B11_cost_1126_rows': sum(row[2] == 1126 for row in b11),
        'completed_command_receipts_hash_checked': len(commands),
        'all_full_cost_cover_families_checked': family_audit,
        'joint_table_checked': table_audit,
        'new_joint_packing_nodes_reconciled_not_rerun': new_nodes,
        'boundary_spectra_checked_by_independent_loss_generating_function': checked,
        'boundary_records': boundary_audit,
        'new_excluded_pairs': 23, 'new_excluded_spectra': 1943,
        'endpoint_spectra': 241, 'endpoint_necessary_survivors': 3,
        'radius': str(radius),
        'p_interval': [str((1 - radius) / 2), str((1 + radius) / 2)],
        'outer_endpoint_extra_ties': 'UNRESOLVED',
        'prior_audit_sha256': digest(args.prior_audit),
        'inputs_sha256': dict(sorted(consulted.items())),
        'checker_sha256': digest(Path(__file__)),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in (
        'kind', 'status', 'completed_command_receipts_hash_checked',
        'boundary_spectra_checked_by_independent_loss_generating_function',
        'new_excluded_pairs', 'new_excluded_spectra', 'endpoint_spectra',
        'endpoint_necessary_survivors', 'radius', 'p_interval')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
