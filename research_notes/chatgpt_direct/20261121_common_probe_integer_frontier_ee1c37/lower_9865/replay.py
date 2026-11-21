"""Audit a completed cost9865 layer, or rerun all190 original native searches.

This becomes a portable entry point only after the builder has verified complete
coverage and copied it into proof_bundle_9865/.  It makes no claim from an
unfinished working directory.
"""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def check_files(root, records):
    for record in records:
        assert digest(root/record['path']) == record['sha256'], record['path']


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--previous', type=Path, required=True)
    p.add_argument('--lower', type=Path, default=HERE.parent/'lower')
    p.add_argument('--prior-layer', type=Path, default=HERE.parent/'lower_9864')
    p.add_argument('--prior9863', type=Path, default=HERE.parent/'lower_9863')
    p.add_argument('--prior9862', type=Path, default=HERE.parent/'lower_9862')
    p.add_argument('--mode', choices=['audit', 'full'], default='audit')
    p.add_argument('--jobs', type=int, default=2)
    p.add_argument('--output', type=Path, default=HERE/'verification')
    args = p.parse_args()
    for key in ('previous', 'lower', 'prior_layer', 'prior9863', 'prior9862', 'output'):
        setattr(args, key, getattr(args, key).resolve())
    assert args.jobs >= 1
    args.output.mkdir(parents=True, exist_ok=True)
    bindings = json.loads((HERE/'bindings.json').read_text())
    expected = json.loads((HERE/'result.json').read_text())['layer']
    assert expected['complete'] and expected['cost'] == 9865
    check_files(args.lower, bindings['source_bindings'])
    check_files(args.prior_layer, bindings['prior_incremental_bindings'])
    check_files(HERE, bindings['driver_bindings'])
    check_files(HERE/'sharded', bindings['sharded_package_bindings'])
    subprocess.run([sys.executable, args.prior_layer/'replay.py',
                    '--previous', args.previous, '--lower', args.lower,
                    '--prior-layer', args.prior9863, '--earlier-layer', args.prior9862,
                    '--mode', 'audit', '--output', args.output/'prior9864'], check=True)
    subprocess.run([sys.executable, HERE/'sharded/replay.py', '--lower', args.lower,
                    '--mode', 'audit', '--output', args.output/'sharded.json'], check=True)
    sharded = json.loads((HERE/'sharded/expected_receipt.json').read_text())
    rows = [json.loads(line) for line in (HERE/'cost_9865_completed.jsonl').read_text().splitlines()]
    assert len(rows) == len({row['tag'] for row in rows}) == 190
    assert dict(Counter(row['engine'] for row in rows)) == bindings['raw_receipt_engine_counts']
    original_sha = next(row['sha256'] for row in bindings['source_bindings']
                        if row['path'] == 'front_orbit_min_witness.cpp')
    bank_sha = next(row['sha256'] for row in bindings['input_bindings'] if row['path'] == 'bank')
    driver_shas = {row['sha256'] for row in bindings['driver_bindings']}
    sharded_rows = 0
    for row in rows:
        assert row['cost'] == 9865 and row['found'] == 0 and row['bank_sha256'] == bank_sha
        if row['engine'] == 'orbit-min-sharded':
            sharded_rows += 1
            for key in ('cost', 'tag', 'source_sha256', 'bank_sha256', 'geometric_nodes',
                        'leaf_nodes', 'search_nodes', 'found'):
                assert row[key] == sharded[key], key
        else:
            assert row['engine'] in ('orbit-min', 'orbits-min-witness')
            assert row['source_sha256'] == original_sha
            # The older reverse scheduler recorded the native source and bank
            # hashes, but did not put its Python-driver hash into every row.
            # Its preserved source is checked above; do not invent a row field.
            if row['engine'] == 'orbit-min' or 'driver_sha256' in row:
                assert row['driver_sha256'] in driver_shas
    assert sharded_rows == 1

    def audit(path, seeds=None):
        command = [sys.executable, args.lower/'audit_completed.py', '--previous', args.previous,
                   '--receipts', path, '--first', '9865', '--last', '9865', '--output', args.output]
        command += ['--seeds', seeds] if seeds else ['--spectrum', args.lower/'class_cost_spectrum.json']
        subprocess.run(command, check=True)
        actual = json.loads((args.output/'coverage.json').read_text())['layers'][0]
        assert actual == expected
        return actual

    execution = {'search_rerun': False,
                 'archived_native_compilation': json.loads((HERE/'native_binary_binding.json').read_text())}
    actual = audit(HERE/'cost_9865_completed.jsonl')
    if args.mode == 'full':
        with tempfile.TemporaryDirectory(prefix='twelve9865_full_') as temporary:
            temp = Path(temporary)
            work = temp/'native_inputs'
            subprocess.run([sys.executable, args.lower/'replay.py', '--previous', args.previous,
                            '--work', work, '--first', '9861', '--last', '9870', '--cost', '9865',
                            '--cores', '0,1,2', '--engine', 'orbit-min', '--jobs', '1',
                            '--prepare-only'], check=True)
            check_files(work, bindings['input_bindings'])
            for name in ('front_orbit_min_witness.cpp', 'marginals.hpp', 'exact_margins.hpp'):
                shutil.copyfile(args.lower/name, temp/name)
            drivers = temp/'drivers'
            drivers.mkdir()
            shutil.copyfile(HERE/'drivers/main.py', drivers/'main.py')
            command = ['c++', '-std=c++20', '-O3', '-mpopcnt', temp/'front_orbit_min_witness.cpp',
                       '-o', work/'front_orbit_min_witness']
            subprocess.run(command, check=True)
            binary_sha = digest(work/'front_orbit_min_witness')
            source_sha = digest(temp/'front_orbit_min_witness.cpp')
            assert source_sha == original_sha
            execution = {'search_rerun': True, 'source_sha256': source_sha,
                         'compilation_command': list(map(str, command)),
                         'compiler_version': subprocess.check_output(['c++', '--version'], text=True).splitlines()[0],
                         'executed_binary_sha256': binary_sha,
                         'executed_driver_sha256': digest(drivers/'main.py'),
                         'all_profiles_use_original_unsharded_native': True}
            subprocess.run([sys.executable, drivers/'main.py', '--work', work, '--cost', '9865',
                            '--jobs', str(args.jobs), '--profiles', HERE/'cost_9865_profiles.txt'], check=True)
            assert digest(work/'front_orbit_min_witness') == binary_sha
            assert digest(temp/'front_orbit_min_witness.cpp') == source_sha
            actual = audit(work/'completed.jsonl', work/'seeds')
    result = {'complete': True, 'cost': 9865, 'profiles': 190,
              'prior_cost9864_audit_passed': True, 'sharded_profile_audit_passed': True,
              'layer': actual, 'execution_binding': execution,
              'new_global_lower_bound': 9866, 'upper_bound': 9996,
              'review_status': 'NOT_REVIEWED'}
    (args.output/'result.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
