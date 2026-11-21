"""Audit the complete E=3 and E=4 exact9866 proofs, or rerun their native profiles."""
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, default=HERE.parent/'previous')
    parser.add_argument('--embedded-count', type=int, choices=[3,4])
    parser.add_argument('--mother', type=Path, default=HERE.parent/'integer_cuts/mother12')
    parser.add_argument('--defect', type=Path, default=HERE.parent/'mother_sublevels_D')
    parser.add_argument('--lower', type=Path, default=HERE.parent/'lower')
    parser.add_argument('--native-inputs', type=Path)
    parser.add_argument('--mode', choices=['audit', 'full'], default='audit')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output = args.output.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    roots = {name: getattr(args, name).resolve() for name in ('mother', 'defect', 'lower', 'previous')}
    bindings = json.loads((HERE/'bindings.json').read_text())
    for dep in bindings['dependencies']:
        assert digest(roots[dep['root']]/dep['path']) == dep['sha256'], dep
    assert digest(HERE/'original_driver.py') == bindings['driver_sha256']
    subprocess.run([sys.executable, '-B', HERE/'exact_price_frontier.py', '--cost', '9866',
                    '--mother-proof', roots['mother'], '--defect-catalog', roots['defect']/'cost_defect_catalog.json',
                    '--output', args.output/'typed_frontier.json'], check=True)
    arithmetic = json.loads((args.output/'typed_frontier.json').read_text())
    scopes = [args.embedded_count] if args.embedded_count else [3, 4]
    expected = json.loads((HERE/'expected.json').read_text())
    size_statistics = {}
    target = set()
    for e in scopes:
        sizes = [r for r in arithmetic['size_summary'] if r['embedded_count'] == e]
        totals = {key: sum(r['counts'].get(key, 0) for r in sizes)
                  for key in ('all', 'centre_defect', 'inherited_core_bound')}
        assert len(sizes) == expected[str(e)]['size_profiles']
        assert totals == expected[str(e)]['price_profile_statistics']
        tags = {r['tag'] for r in arithmetic['survivors'] if r['embedded_count'] == e}
        assert len(tags) == expected[str(e)]['remaining_profiles']
        target.update(tags)
        size_statistics[str(e)] = {'size_profiles': len(sizes), 'price_combinations': totals, 'native_profiles': len(tags)}
    all_rows = [json.loads(line) for line in (HERE/'receipts.jsonl').read_text().splitlines()]
    assert len(all_rows) == len({r['tag'] for r in all_rows}) == 40
    assert set((HERE/'profiles.txt').read_text().splitlines()) == {r['tag'] for r in all_rows}
    rows = [r for r in all_rows if r['tag'] in target]
    assert {r['tag'] for r in rows} == target
    for row in rows:
        assert row['cost'] == 9866 and row['found'] == 0
        assert row['source_sha256'] == bindings['source_sha256']
        assert row['bank_sha256'] == bindings['bank_sha256']
        assert row['driver_sha256'] == bindings['driver_sha256']
    inherited = json.loads((roots['defect']/'e3/core_three_dependency_result.json').read_text())
    assert inherited['scope'] == 'exactly 3 cores' and inherited['excluded_through'] == 9880
    assert len(inherited['cases']) == 134 and all(row['solutions'] == 0 for row in inherited['cases'])
    assert sum(row['nodes'] for row in inherited['cases']) == 96050105
    four = json.loads((roots['previous']/'lower/four_result.json').read_text())
    assert four['all_excluded'] and 9866 in four['fully_excluded_costs']
    assert four['completed_by_cost']['9866'] == 525
    result = {'cost': 9866, 'embedded_counts': scopes, 'complete': True,
              'size_statistics': size_statistics, 'native_profiles': len(rows), 'solutions': 0,
              'cover_nodes': sum(r['search_nodes'] for r in rows),
              'geometric_nodes': sum(r['geometric_nodes'] for r in rows),
              'leaf_nodes': sum(r['leaf_nodes'] for r in rows),
              'search_rerun': args.mode == 'full', 'review_status': 'NOT_REVIEWED'}
    for key, expected_key in [('cover_nodes','search_nodes'),('geometric_nodes','geometric_nodes'),('leaf_nodes','leaf_nodes')]:
        assert result[key] == sum(expected[str(e)][expected_key] for e in scopes)
    if args.mode == 'full':
        work = args.native_inputs.resolve() if args.native_inputs else args.output/'native_inputs'
        if args.native_inputs is None:
            assert args.previous is not None, '--previous is needed to regenerate native inputs'
            subprocess.run([sys.executable, '-B', roots['lower']/'replay.py',
                            '--previous', args.previous.resolve(), '--work', work,
                            '--first', '9861', '--last', '9870', '--cost', '9866',
                            '--cores', '0,1,2', '--engine', 'orbit-min', '--prepare-only'], check=True)
        for dep in bindings['native_inputs']:
            assert digest(work/dep['path']) == dep['sha256'], dep['path']
        executable = args.output/'native_search'
        compile_command = ['c++', '-std=c++20', '-O3', '-mpopcnt',
                           roots['lower']/'front_orbit_min_witness.cpp', '-o', executable]
        subprocess.run(compile_command, check=True)
        types = list(map(tuple, json.loads((work/'manifest.json').read_text())['types']))
        query = ''
        for row in rows:
            counts = {(s, c): n for s, c, n in (map(int, part.split('-')) for part in row['tag'].split('_'))}
            query += ' '.join(map(str, [9866, *[counts.get(t, 0) for t in types]]))+'\n'
        execution_inputs = args.output/'execution_inputs'
        execution_inputs.mkdir(exist_ok=True)
        for dep in bindings['native_inputs']:
            target = execution_inputs/dep['path']
            if not target.exists():
                target.symlink_to(work/dep['path'])
        answer = subprocess.run([executable, work/'bank', work, execution_inputs], input=query,
                                text=True, capture_output=True, check=True)
        # Fresh output paths preserve the original input files even if a
        # counterexample is found during future reproduction.
        if answer.stderr:
            (args.output/'native.stderr').write_text(answer.stderr)
        words = [list(map(int, line.split())) for line in answer.stdout.splitlines()]
        assert len(words) == len(rows)
        for row, actual in zip(rows, words):
            assert actual == [row[k] for k in ('cost', 'geometric_nodes', 'leaf_nodes', 'search_nodes', 'found')]
        result['execution'] = {'binary_sha256': digest(executable),
                               'source_sha256': bindings['source_sha256'],
                               'compile_command': list(map(str, compile_command))}
    (args.output/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
