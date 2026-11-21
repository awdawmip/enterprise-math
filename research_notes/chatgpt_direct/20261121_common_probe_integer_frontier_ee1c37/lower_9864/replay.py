"""Verify the complete cost9864 certificate, or rerun its native integer search."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--previous', type=Path, required=True,
                    help='The unchanged complete 2026-11-20 predecessor package')
parser.add_argument('--lower', type=Path, default=HERE.parent/'lower',
                    help='The unchanged checkpoint-B lower/ proof directory')
parser.add_argument('--prior-layer', type=Path, default=HERE.parent/'lower_9863',
                    help='The unchanged completed cost9863 incremental certificate')
parser.add_argument('--earlier-layer', type=Path, default=HERE.parent/'lower_9862', help='The unchanged cost9862 certificate needed by the cost9863 verifier')
parser.add_argument('--mode', choices=['audit', 'full'], default='audit')
parser.add_argument('--jobs', type=int, default=2)
parser.add_argument('--output', type=Path, default=HERE/'verification')
args = parser.parse_args()
args.lower = args.lower.resolve()
args.previous = args.previous.resolve()
args.prior_layer = args.prior_layer.resolve()
args.earlier_layer = args.earlier_layer.resolve()
args.output.mkdir(parents=True, exist_ok=True)
bindings = json.loads((HERE/'bindings.json').read_text())
expected = json.loads((HERE/'result.json').read_text())['layer']
for row in bindings['source_bindings']:
    assert hashlib.sha256((args.lower/row['path']).read_bytes()).hexdigest() == row['sha256'], row['path']
for row in bindings['prior_incremental_bindings']:
    assert hashlib.sha256((args.prior_layer/row['path']).read_bytes()).hexdigest() == row['sha256'], row['path']
driver = bindings['auxiliary_driver']
assert hashlib.sha256((HERE/driver['path']).read_bytes()).hexdigest() == driver['sha256']
subprocess.run([sys.executable, args.prior_layer/'replay.py', '--previous', args.previous,
                '--lower', args.lower, '--prior-layer', args.earlier_layer, '--mode', 'audit', '--output', args.output/'prior9863'], check=True)
receipts = [json.loads(line) for line in (HERE/'cost_9864_completed.jsonl').read_text().splitlines()]
assert len(receipts) == len({row['tag'] for row in receipts}) == 153
assert all(row['cost'] == 9864 and row['found'] == 0 for row in receipts)
assert dict(Counter(row['engine'] for row in receipts)) == bindings['raw_receipt_engine_counts']
source_sha = next(row['sha256'] for row in bindings['source_bindings'] if row['path'] == 'front_orbit_min_witness.cpp')
bank_sha = next(row['sha256'] for row in bindings['input_bindings'] if row['path'] == 'bank')
for row in receipts:
    if row['engine'] == 'orbits-min-witness':
        assert row['source_sha256'] == source_sha and row['bank_sha256'] == bank_sha
    else:
        assert row['engine'] == 'orbit-min'


def audit(receipt_path, seeds=None):
    command = [sys.executable, args.lower/'audit_completed.py', '--previous', args.previous,
               '--receipts', receipt_path, '--first', '9864', '--last', '9864', '--output', args.output]
    command += ['--seeds', seeds] if seeds else ['--spectrum', args.lower/'class_cost_spectrum.json']
    subprocess.run(command, check=True)
    actual = json.loads((args.output/'coverage.json').read_text())['layers'][0]
    assert actual['complete'] and actual['expected_low_core_profiles'] == actual['completed_low_core_profiles'] == 153
    assert actual['profile_sha256'] == expected['profile_sha256']
    return actual


if args.mode == 'audit':
    actual = audit(HERE/'cost_9864_completed.jsonl')
    assert actual == expected
else:
    with tempfile.TemporaryDirectory(prefix='twelve_9864_') as temporary:
        work = Path(temporary)
        subprocess.run([sys.executable, args.lower/'replay.py', '--previous', args.previous, '--work', work,
                        '--first', '9861', '--last', '9870', '--cost', '9864', '--cores', '0,1,2',
                        '--engine', 'orbit-min', '--jobs', str(args.jobs)], check=True)
        for row in bindings['input_bindings']:
            assert hashlib.sha256((work/row['path']).read_bytes()).hexdigest() == row['sha256'], row['path']
        actual = audit(work/'completed.jsonl', work/'seeds')
result = {'complete': True, 'cost': 9864, 'profiles': 153, 'search_rerun': args.mode == 'full',
          'prior_cost9863_audit_passed': True, 'layer': actual,
          'new_global_lower_bound': 9865, 'upper_bound': 9996}
(args.output/'result.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
print(json.dumps(result, sort_keys=True))
