#!/usr/bin/env python3
"""Replay this research batch without modifying the published certificates."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value):
    if isinstance(value, list):
        return [canonical(x) for x in value]
    if isinstance(value, dict):
        result = {}
        for k, v in value.items():
            if k == 'path' and isinstance(v, str) and 'riemann_directed_local_20261124/' in v:
                v = v.split('riemann_directed_local_20261124/', 1)[1]
            result[k] = canonical(v)
        return result
    return value


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--prior', type=Path, default=root/'prior/riemann_directed_local_20261124')
    args = parser.parse_args()
    prior = args.prior.resolve()
    manifest = json.loads((root/'MANIFEST.json').read_text())
    for item in manifest['files']:
        path = root/item['path']
        assert digest(path) == item['sha256'], f'Current artifact hash mismatch: {item["path"]}'
    dependencies = json.loads((root/'DEPENDENCIES.json').read_text())
    for item in dependencies['required_files']:
        assert digest(prior/item['path']) == item['sha256'], f'Predecessor hash mismatch: {item["path"]}'
    jobs = [
        ('matching/verify_actual_matching.py', 'matching/actual_matching_certificate.json', True),
        ('anchors/verify_anchor_green.py', 'anchors/anchor_green_certificate.json', False),
        ('deficit/certify_isotonic_deficit.py', 'deficit/isotonic_certificate.json', True),
        ('deficit/verify_pool_refinement.py', 'deficit/pool_refinement_certificate.json', False),
        ('seams/certify_saved_anchors.py', 'seams/saved_anchor_certificate.json', True),
        ('radius/certify_product_radius.py', 'radius/product_radius_certificate.json', True),
    ]
    with tempfile.TemporaryDirectory(prefix='em-replay-') as temp:
        for script, certificate, needs_prior in jobs:
            output = Path(temp)/Path(certificate).name
            command = [sys.executable, str(root/script), '--output', str(output)]
            if needs_prior:
                command += ['--prior', str(prior)]
            result = subprocess.run(command, text=True, capture_output=True)
            if result.returncode:
                sys.stderr.write(result.stdout+result.stderr)
                raise SystemExit(result.returncode)
            expected = canonical(json.loads((root/certificate).read_text()))
            actual = canonical(json.loads(output.read_text()))
            assert actual == expected, f'Certificate mismatch: {certificate}'
            print('PASS', script, flush=True)
    print('PASS: all six strict certificates reproduced; exploratory floating data excluded.')


if __name__ == '__main__':
    main()
