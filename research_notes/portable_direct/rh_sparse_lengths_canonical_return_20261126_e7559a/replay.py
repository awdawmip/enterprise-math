#!/usr/bin/env python3
"""Replay this round's three new certificates; preserve all old calculations."""
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
                        default=root/'prior/riemann_coherent_tail_interval_spectrum_20261126')
    args = parser.parse_args()
    previous = args.previous.resolve()
    for row in json.loads((root/'MANIFEST.json').read_text())['files']:
        assert digest(root/row['path']) == row['sha256'], 'Artifact mismatch: '+row['path']
    for row in json.loads((root/'DEPENDENCIES.json').read_text())['required_files']:
        assert digest(previous/row['path']) == row['sha256'], 'Predecessor mismatch: '+row['path']
    jobs = [
        ('sparse_lengths/verify_sparse_lengths.py',
         'sparse_lengths/sparse_length_results.json', []),
        ('canonical_sampling/certify_exact_alias_packet.py',
         'canonical_sampling/exact_alias_packet_certificate.json', ['--steps','24']),
        ('shifted_roads/certify_shifted_roads.py',
         'shifted_roads/shifted_roads_certificate.json', ['--previous',str(previous)]),
    ]
    task_env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='em-sparse-canonical-return-') as temporary:
        for script, certificate, extra in jobs:
            output = Path(temporary)/Path(certificate).name
            result = subprocess.run(
                [sys.executable,str(root/script),*extra,'--output',str(output)],
                capture_output=True,text=True,env=task_env,
            )
            if result.returncode:
                sys.stderr.write(result.stdout+result.stderr)
                raise SystemExit(result.returncode)
            actual = json.loads(output.read_text())
            expected = json.loads((root/certificate).read_text())
            assert actual == expected, 'Certificate mismatch: '+certificate
            print('PASS',script,flush=True)
    print('PASS: all three current certificates reproduced exactly; no prior calculation rerun.')


if __name__ == '__main__':
    main()
