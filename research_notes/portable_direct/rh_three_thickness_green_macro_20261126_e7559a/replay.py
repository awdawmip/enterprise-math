#!/usr/bin/env python3
"""Reproduce the two current certificates; reuse all earlier fixed evidence."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path,
                        default=root/'prior/riemann_calibrated_green_sparse_20261126')
    args = parser.parse_args()
    previous = args.previous.resolve()
    for row in json.loads((root/'MANIFEST.json').read_text())['files']:
        assert digest(root/row['path']) == row['sha256'], f'Artifact mismatch: {row["path"]}'
    for row in json.loads((root/'DEPENDENCIES.json').read_text())['required_files']:
        assert digest(previous/row['path']) == row['sha256'], f'Predecessor mismatch: {row["path"]}'
    jobs = [
        ('three_thickness/certify_three_thickness.py', 'three_thickness/three_thickness_certificate.json'),
        ('positive_green/compute_positive_green.py', 'positive_green/positive_green_results.json'),
    ]
    with tempfile.TemporaryDirectory(prefix='em-three-green-macro-replay-') as temp:
        for script, certificate in jobs:
            output = Path(temp)/Path(certificate).name
            result = subprocess.run(
                [sys.executable, str(root/script), '--previous', str(previous), '--output', str(output)],
                capture_output=True, text=True,
            )
            if result.returncode:
                sys.stderr.write(result.stdout+result.stderr)
                raise SystemExit(result.returncode)
            assert json.loads(output.read_text()) == json.loads((root/certificate).read_text()), \
                f'Certificate mismatch: {certificate}'
            print('PASS', script, flush=True)
    print('PASS: both current certificates reproduced; predecessor calculations were not rerun.')


if __name__ == '__main__':
    main()
