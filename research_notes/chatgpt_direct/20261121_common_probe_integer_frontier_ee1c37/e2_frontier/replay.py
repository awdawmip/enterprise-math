"""Verify consecutive exact E=2 cost layers; optionally rerun native covers.

The frozen package records discovery computations. Audit regenerates the finite
typed price families and checks complete receipts. Full additionally recompiles
the unchanged native solver and reproduces every selected cover computation.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mother', type=Path, default=HERE.parent/'integer_cuts/mother12')
    p.add_argument('--defect', type=Path, default=HERE.parent/'mother_sublevels_D')
    p.add_argument('--marginal', type=Path, default=HERE.parent/'marginal_bound')
    p.add_argument('--lower', type=Path, default=HERE.parent/'lower')
    p.add_argument('--previous', type=Path, default=HERE.parent/'previous')
    p.add_argument('--native-inputs', type=Path)
    p.add_argument('--mode', choices=['audit', 'full'], default='audit')
    p.add_argument('--first', type=int)
    p.add_argument('--last', type=int)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    args.output = args.output.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    roots = {name: getattr(args, name).resolve() for name in ('mother', 'defect', 'marginal', 'lower', 'previous')}
    bindings = json.loads((HERE/'bindings.json').read_text())
    expected = json.loads((HERE/'expected.json').read_text())
    for item in bindings['dependencies']:
        assert digest(roots[item['root']]/item['path']) == item['sha256'], item
    baseline = json.loads((roots['marginal']/'verification.json').read_text())
    assert baseline['all_checks_passed']
    assert baseline['exact_two_embedded_global_lower_bound'] == 9867
    first = args.first if args.first is not None else 9867
    last = args.last if args.last is not None else expected['excluded_through']
    assert 9867 <= first <= last <= expected['excluded_through']
    receipts = [json.loads(line) for line in (HERE/'receipts.jsonl').read_text().splitlines()]
    assert len(receipts) == len({r['tag'] for r in receipts}) == expected['native_profiles']
    by_tag = {r['tag']: r for r in receipts}
    selected, layers = [], []
    for cost in range(first, last+1):
        target = args.output/f'cost{cost}.json'
        subprocess.run([sys.executable, '-B', HERE/'exact_price_frontier.py', '--cost', str(cost),
                        '--only-embedded-count', '2', '--mother-proof', roots['mother'],
                        '--defect-catalog', roots['defect']/'cost_defect_catalog.json',
                        '--output', target], check=True, stdout=subprocess.DEVNULL)
        result = json.loads(target.read_text())
        tags = sorted({r['tag'] for r in result['survivors']})
        assert set(tags) == {r['tag'] for r in receipts if r['cost'] == cost}, cost
        for tag in tags:
            r = by_tag[tag]
            assert r['found'] == 0 and r['cost'] == cost
            for key in ('source_sha256', 'bank_sha256', 'binary_sha256'):
                assert r[key] == bindings[key]
            selected.append(r)
        layer = {'cost': cost, 'size_profiles': result['size_profiles'],
                 'exact_price_patterns': result['total_exact_price_patterns'],
                 'surviving_typed_patterns': result['surviving_typed_patterns'],
                 'native_profiles': len(tags),
                 'search_nodes': sum(by_tag[tag]['search_nodes'] for tag in tags),
                 'geometric_nodes': sum(by_tag[tag]['geometric_nodes'] for tag in tags),
                 'leaf_nodes': sum(by_tag[tag]['leaf_nodes'] for tag in tags)}
        assert layer == expected['layers'][str(cost)], (cost, layer)
        layers.append(layer)
    answer = {'complete_selected_interval': True, 'first': first, 'last': last,
              'general_E2_lower_bound': last+1 if first == 9867 else None,
              'native_profiles': len(selected), 'solutions': 0,
              'search_nodes': sum(r['search_nodes'] for r in selected),
              'geometric_nodes': sum(r['geometric_nodes'] for r in selected),
              'leaf_nodes': sum(r['leaf_nodes'] for r in selected),
              'price_patterns': sum(r['exact_price_patterns'] for r in layers),
              'layers': layers, 'search_rerun': args.mode == 'full',
              'review_status': 'NOT_REVIEWED'}
    if args.mode == 'full':
        work = args.native_inputs.resolve() if args.native_inputs else args.output/'native_inputs'
        if args.native_inputs is None:
            subprocess.run([sys.executable, '-B', roots['lower']/'replay.py',
                            '--previous', roots['previous'], '--work', work,
                            '--first', '9861', '--last', '9870', '--cost', '9866',
                            '--cores', '0,1,2', '--engine', 'orbit-min', '--prepare-only'], check=True)
        for item in bindings['native_inputs']:
            assert digest(work/item['path']) == item['sha256'], item['path']
        types = list(map(tuple, json.loads((work/'manifest.json').read_text())['types']))
        execution = args.output/'execution_inputs'
        execution.mkdir(exist_ok=True)
        for item in bindings['native_inputs']:
            target = execution/item['path']
            if not target.exists():
                target.symlink_to(work/item['path'])
        exe = args.output/'native_search'
        subprocess.run(['c++', '-std=c++20', '-O3', '-mpopcnt',
                        roots['lower']/'front_orbit_min_witness.cpp', '-o', exe], check=True)
        query = ''
        for r in selected:
            counts = {(s,c):n for s,c,n in (map(int, item.split('-')) for item in r['tag'].split('_'))}
            assert set(counts) <= set(types), 'Necessary native types are missing'
            query += ' '.join(map(str, [r['cost'], *[counts.get(t,0) for t in types]]))+'\n'
        native = subprocess.run([exe, work/'bank', work, execution], input=query,
                                text=True, capture_output=True, check=True)
        words = [list(map(int, line.split())) for line in native.stdout.splitlines()]
        assert len(words) == len(selected)
        for r, actual in zip(selected, words):
            assert actual == [r[k] for k in ('cost','geometric_nodes','leaf_nodes','search_nodes','found')]
        answer['execution_binary_sha256'] = digest(exe)
    (args.output/'result.json').write_text(json.dumps(answer, indent=2)+'\n')
    print(json.dumps({k:v for k,v in answer.items() if k != 'layers'}, sort_keys=True))


if __name__ == '__main__':
    main()
