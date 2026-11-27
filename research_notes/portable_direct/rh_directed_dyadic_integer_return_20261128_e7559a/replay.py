#!/usr/bin/env python3
"""Reproduce the four current certificates in temporary files, byte for byte."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile


PREDECESSOR = 'riemann_sparse_lengths_canonical_return_20261126'
JOBS = (
    ('directed_dyadic/verify_directed_dyadic.py',
     'directed_dyadic/directed_dyadic_certificate.json', False),
    ('arithmetic_sampling/certify_dyadic_windows.py',
     'arithmetic_sampling/dyadic_windows_certificate.json', True),
    ('arithmetic_rigidity/certify_first_cell_and_repair.py',
     'arithmetic_rigidity/first_cell_and_repair_certificate.json', True),
    ('return_energy/certify_log_energy_constants.py',
     'return_energy/log_energy_constants_certificate.json', True),
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_predecessor(root, previous):
    manifest = root / 'DEPENDENCIES.json'
    if not manifest.exists():
        print('SKIP predecessor manifest: DEPENDENCIES.json is absent.', flush=True)
        return
    rows = json.loads(manifest.read_text(encoding='utf-8'))['required_files']
    for row in rows:
        actual = digest(previous / row['path'])
        if actual != row['sha256']:
            raise SystemExit('Predecessor SHA256 mismatch: ' + row['path'])
    print(f'PASS predecessor identities: {len(rows)} files; no predecessor calculation run.',
          flush=True)


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--previous', type=Path,
        default=root.parent / 'deliverables' / PREDECESSOR,
        help='round7 package; for a delivered bundle use previous/' + PREDECESSOR,
    )
    args = parser.parse_args()
    previous = args.previous.resolve()
    verify_predecessor(root, previous)
    task_env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='em-directed-arithmetic-r8-') as temporary:
        temporary = Path(temporary)
        for script, certificate, accepts_output in JOBS:
            output = temporary / certificate
            output.parent.mkdir(parents=True, exist_ok=True)
            if accepts_output:
                command = [sys.executable, str(root / script),
                           '--previous', str(previous), '--output', str(output)]
            else:
                # This existing script writes beside __file__.  Run unchanged
                # bytes from the temporary directory to preserve its saved output.
                temporary_script = temporary / script
                shutil.copyfile(root / script, temporary_script)
                command = [sys.executable, str(temporary_script)]
            result = subprocess.run(command, cwd=root, capture_output=True,
                                    text=True, env=task_env)
            if result.returncode:
                sys.stderr.write(result.stdout + result.stderr)
                raise SystemExit(result.returncode)
            expected = root / certificate
            if output.read_bytes() != expected.read_bytes():
                raise SystemExit(
                    'Certificate byte mismatch: ' + certificate
                    + '\nexpected SHA256: ' + digest(expected)
                    + '\nactual SHA256:   ' + digest(output)
                )
            print('PASS ' + script + ' (exact bytes)', flush=True)
    print('PASS: all four current certificates reproduced byte for byte; '
          'no prior calculation rerun.')


if __name__ == '__main__':
    main()
