"""Audit or freshly rerun the complete173-batch cost9865 profile exclusion."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def file_hash(path):
    return sha256(path.read_bytes()).hexdigest()


def audit_ranges(directory):
    plan = json.loads((directory/'plan.json').read_text())
    ranges = plan['ranges']
    assert ranges and ranges[0][0] == 0 and ranges[-1][1] == plan['total_frames']
    assert all(0 <= begin < end <= plan['total_frames'] for begin, end in ranges)
    assert all(a[1] == b[0] for a, b in zip(ranges, ranges[1:]))
    assert len(list((directory/'completed').glob('*.json'))) == len(ranges)
    metrics = {'geometric_nodes': 0, 'leaf_nodes': 0, 'search_nodes': 0}
    for index, (begin, end) in enumerate(ranges):
        row = json.loads((directory/'completed'/f'{index:06d}.json').read_text())
        for key in ('cost', 'tag', 'total_frames', 'source_sha256', 'bank_sha256', 'profile_manifest_sha256'):
            assert row[key] == plan[key]
        assert (row['begin_frame'], row['end_frame']) == (begin, end)
        assert row['found'] == 0 and row['engine'] == 'orbit-min-sharded'
        for key in metrics:
            assert type(row[key]) is int and row[key] >= 0
            metrics[key] += row[key]
    return {**plan, **metrics, 'found': 0, 'completed_batches': len(ranges), 'complete': True}


def check_inputs(work, bindings):
    for row in bindings['native_input_bindings']:
        assert file_hash(work/row['path']) == row['sha256'], row['path']
    assert file_hash(work/'manifest.json') == bindings['profile_manifest_sha256']


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--lower', type=Path, required=True, help='The unchanged B/C lower/ source directory')
    p.add_argument('--previous', type=Path, help='The complete predecessor package; required for --mode full')
    p.add_argument('--work', type=Path, help='Optional existing native input directory for all18 hash checks in audit mode')
    p.add_argument('--binary', type=Path, help='Optional retained original execution binary, to check its archived SHA256 in audit mode')
    p.add_argument('--mode', choices=['audit', 'full'], default='audit')
    p.add_argument('--output', type=Path, default=HERE/'verification.json')
    args = p.parse_args()
    args.lower = args.lower.resolve()
    bindings = json.loads((HERE/'input_bindings.json').read_text())
    generation = json.loads((HERE/'generation.json').read_text())
    expected = json.loads((HERE/'expected_receipt.json').read_text())
    original = args.lower/'front_orbit_min_witness.cpp'
    assert file_hash(original) == bindings['original_engine_source_sha256'] == generation['original_source_sha256']
    source = original.read_text()
    for old, new in generation['replacements'].items():
        assert source.count(old) == 1
        source = source.replace(old, new)
    assert source == (HERE/'front_sharded.cpp').read_text()
    assert file_hash(HERE/'front_sharded.cpp') == bindings['derived_source_sha256'] == generation['derived_source_sha256']
    for row in bindings['included_headers']:
        assert file_hash(args.lower/row['path']) == row['sha256']
    if args.work:
        check_inputs(args.work.resolve(), bindings)
    if args.binary:
        assert file_hash(args.binary) == bindings['actual_binary_sha256']
    actual = audit_ranges(HERE/'receipts')
    for key in ('cost', 'tag', 'total_frames', 'source_sha256', 'bank_sha256', 'profile_manifest_sha256',
                'geometric_nodes', 'leaf_nodes', 'search_nodes', 'found', 'completed_batches', 'complete'):
        assert actual[key] == expected[key]
    assert file_hash(HERE/'receipts/plan.json') == expected['prefix_plan_sha256']
    assert actual['cost'] == 9865 and actual['total_frames'] == 5528 and actual['completed_batches'] == 173
    for name, comparison in [('control', 'control_comparison.json'), ('control_punct', 'control_punct_comparison.json')]:
        fixture = audit_ranges(HERE/'controls'/name)
        old = json.loads((HERE/comparison).read_text())['original_receipt']
        for key in ('cost', 'tag', 'geometric_nodes', 'leaf_nodes', 'search_nodes', 'found'):
            assert fixture[key] == old[key]
    resumed = audit_ranges(HERE/'controls/control_resume')
    assert resumed['search_nodes'] == 23136
    resume_report = json.loads((HERE/'resume_validation.json').read_text())
    assert resume_report['partial_result_was_not_exclusion'] and resume_report['partial_missing_batches'] == [3, 4, 5]
    execution_binding = {'archived_actual_binary_sha256': bindings['actual_binary_sha256'],
                         'retained_original_binary_hash_checked': bool(args.binary)}
    if args.mode == 'full':
        assert args.previous is not None
        args.previous = args.previous.resolve()
        with tempfile.TemporaryDirectory(prefix='prefix_sharded9865_') as temporary:
            temp = Path(temporary)
            work = temp/'native_inputs'
            subprocess.run([sys.executable, args.lower/'replay.py', '--previous', args.previous, '--work', work,
                            '--first', '9861', '--last', '9870', '--cost', '9865', '--cores', '0,1,2',
                            '--engine', 'orbit-min', '--jobs', '1', '--prepare-only'], check=True)
            check_inputs(work, bindings)
            engine = temp/'engine'
            engine.mkdir()
            for name in ('front_sharded.cpp', 'run.py'):
                shutil.copyfile(HERE/name, engine/name)
            command = ['c++', '-std=c++20', '-O3', '-mpopcnt', '-I', args.lower,
                       engine/'front_sharded.cpp', '-o', engine/'front_sharded']
            assert file_hash(engine/'front_sharded.cpp') == bindings['derived_source_sha256']
            subprocess.run(command, check=True)
            binary_sha = file_hash(engine/'front_sharded')
            execution_binding.update(recompiled_source_sha256=file_hash(engine/'front_sharded.cpp'),
                                     included_headers=bindings['included_headers'],
                                     compilation_command=list(map(str, command)),
                                     compiler_version=subprocess.check_output(['c++', '--version'], text=True).splitlines()[0],
                                     executed_binary_sha256=binary_sha,
                                     executed_driver_sha256=file_hash(engine/'run.py'))
            receipts = temp/'receipts'
            subprocess.run([sys.executable, engine/'run.py', '--work', work, '--tag', expected['tag'],
                            '--batch-size', '32', '--output', receipts], check=True)
            assert file_hash(engine/'front_sharded') == binary_sha
            assert file_hash(engine/'front_sharded.cpp') == bindings['derived_source_sha256']
            rerun = audit_ranges(receipts)
            for key in ('cost', 'tag', 'total_frames', 'geometric_nodes', 'leaf_nodes', 'search_nodes', 'found'):
                assert rerun[key] == expected[key]
    result = {'all_checks_passed': True, 'complete_profile_exclusion': True, 'cost': 9865,
              'tag': expected['tag'], 'total_frames': 5528, 'completed_batches': 173,
              'geometric_nodes': actual['geometric_nodes'], 'leaf_nodes': actual['leaf_nodes'],
              'search_nodes': actual['search_nodes'], 'source_regenerated_identically': True,
              'native_input_hashes_checked': bool(args.work) or args.mode == 'full',
              'execution_binding': execution_binding,
              'search_rerun': args.mode == 'full', 'whole_cost_layer_claimed': False,
              'review_status': 'NOT_REVIEWED'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
