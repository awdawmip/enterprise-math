#!/usr/bin/env python3
"""Reproduce six current certificates, preserving all predecessor calculations."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile

PREDECESSOR = 'riemann_directed_dyadic_integer_return_20261128'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root = Path(__file__).resolve().parent
    bundled = root/'previous'/PREDECESSOR
    default_previous = bundled if bundled.is_dir() else root.parent/'deliverables'/PREDECESSOR
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, default=default_previous)
    args = parser.parse_args()
    previous = args.previous.resolve()
    required = json.loads((root/'DEPENDENCIES.json').read_text())['required_files']
    for row in required:
        if digest(previous/row['path']) != row['sha256']:
            raise SystemExit('Predecessor identity mismatch: '+row['path'])
    print(f'PASS predecessor identities: {len(required)} exact files; no predecessor program executed.', flush=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')

    def run(command):
        result = subprocess.run(command, cwd=root, env=env, text=True, capture_output=True)
        if result.returncode:
            sys.stderr.write(result.stdout+result.stderr)
            raise SystemExit(result.returncode)
        return result

    with tempfile.TemporaryDirectory(prefix='em-block-green-r9-') as temp:
        temp = Path(temp)
        jobs = [
            ('block_means/certify_block_mean_statistics.py',
             'block_means/block_mean_certificate.json', ['--previous', str(previous)]),
            ('block_means/certify_quarter_block_aggregation.py',
             'block_means/quarter_block_certificate.json',
             ['--previous', str(previous), '--block-certificate', str(temp/'block_means/block_mean_certificate.json')]),
            ('bounded_source_anchors/certify_bounded_source_anchors.py',
             'bounded_source_anchors/bounded_source_anchors_certificate.json', ['--previous', str(previous)]),
            ('moving_shift_return/verify_uniform_moving_return.py',
             'moving_shift_return/uniform_moving_return_certificate.json', ['--previous', str(previous)]),
            ('moving_shift_return/crosscheck_block_mean_interval_cancellation.py',
             'moving_shift_return/block_mean_author_crosscheck_certificate.json',
             ['--block-means', str(root/'block_means')]),
        ]
        for script, certificate, extra in jobs:
            output = temp/certificate
            output.parent.mkdir(parents=True, exist_ok=True)
            run([sys.executable, str(root/script), *extra, '--output', str(output)])
            expected = root/certificate
            if output.read_bytes() != expected.read_bytes():
                raise SystemExit('Certificate byte mismatch: '+certificate+
                                 '\nExpected: '+digest(expected)+'\nActual: '+digest(output))
            print('PASS '+script+' (exact certificate bytes)', flush=True)
        run([sys.executable, str(root/'green_cutoff/certify_coarse_green.py'), '--check'])
        print('PASS green_cutoff/certify_coarse_green.py (exact certificate bytes)', flush=True)
    print('PASS: six current certificates reproduced; all predecessor programs and certificates remained read-only.', flush=True)


if __name__ == '__main__':
    main()
