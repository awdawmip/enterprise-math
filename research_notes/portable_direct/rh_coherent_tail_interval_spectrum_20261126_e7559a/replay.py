#!/usr/bin/env python3
"""Reproduce three current certificates, preserving all fixed older evidence."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path,
                        default=root/'prior/riemann_three_thickness_green_macro_20261126')
    args = parser.parse_args()
    previous = args.previous.resolve()
    for row in json.loads((root/'MANIFEST.json').read_text())['files']:
        assert digest(root/row['path']) == row['sha256'], 'Artifact mismatch: '+row['path']
    for row in json.loads((root/'DEPENDENCIES.json').read_text())['required_files']:
        assert digest(previous/row['path']) == row['sha256'], 'Predecessor mismatch: '+row['path']
    round4 = previous/'prior/riemann_calibrated_green_sparse_20261126'
    jobs = [
        ('third_order_source/certify_third_order_source.py',
         'third_order_source/third_order_source_certificate.json',
         ['--previous', str(round4), '--round5', str(previous/'three_thickness')]),
        ('green_arithmetic/verify_interval_transfer.py',
         'green_arithmetic/interval_transfer_results.json',
         ['--previous', str(previous)]),
        ('geometric_sampling/construct_atomic_moment_counterexample.py',
         'geometric_sampling/atomic_moment_prefix.json',
         ['--last-order', '64']),
    ]
    task_env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='em-coherent-interval-replay-') as temporary:
        for script, certificate, extra in jobs:
            output = Path(temporary)/Path(certificate).name
            result = subprocess.run(
                [sys.executable, str(root/script), *extra, '--output', str(output)],
                capture_output=True, text=True, env=task_env,
            )
            if result.returncode:
                sys.stderr.write(result.stdout+result.stderr)
                raise SystemExit(result.returncode)
            actual = json.loads(output.read_text())
            expected = json.loads((root/certificate).read_text())
            assert actual == expected, 'Certificate mismatch: '+certificate
            print('PASS', script, flush=True)
    print('PASS: three current certificates reproduced exactly; prior calculations were not rerun.')


if __name__ == '__main__':
    main()
