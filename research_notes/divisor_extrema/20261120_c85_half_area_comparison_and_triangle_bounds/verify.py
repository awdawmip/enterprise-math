#!/usr/bin/env python3
"""Recompute C85's six exact check groups; integral meshes are opt-in.

This is an integration/reproduction driver, not a formal proof checker.
The final integral generator was executed when the saved certificate was made.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
GROUPS = [
    ('half_area', 'position/certify_half_area.py', 'position/half_area_certificate.json'),
    ('square', 'position/verify_square_lattice.py', 'position/square_lattice_certificate.json'),
    ('cusp', 'lattice/verify_cusp.py', 'lattice/cusp_checks.json'),
    ('compact', 'lattice/verify_compact_reduction.py', 'lattice/compact_reduction_checks.json'),
    ('endpoint', 'endpoint/verify_endpoint.py', 'endpoint/endpoint_checks.json'),
    ('triangle', 'triangle/verify_triangle85.py', 'triangle/triangle85_checks.json'),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_script(path):
    proc = subprocess.run([sys.executable, str(ROOT / path)], cwd=ROOT,
                          capture_output=True, text=True)
    if proc.returncode:
        raise RuntimeError(f'{path} failed:\n{proc.stdout}\n{proc.stderr}')


def check_manifest():
    lines = (ROOT / 'SHA256SUMS').read_text().splitlines()
    for line in lines:
        expected, name = line.split('  ', 1)
        assert digest(ROOT / name) == expected, name
    return len(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recompute-integrals', action='store_true',
                        help='also regenerate the final 112-bit integral certificate')
    parser.add_argument('--check-manifest', action='store_true',
                        help='check delivered bytes only; do not rewrite results')
    args = parser.parse_args()
    if args.check_manifest:
        print(json.dumps({'status': 'PASS', 'manifest_files': check_manifest()}))
        return
    if args.recompute_integrals:
        run_script('triangle/certify_farey_parallelogram.py')
    rows = []
    for name, script, result in GROUPS:
        run_script(script)
        data = json.loads((ROOT / result).read_text())
        assert data.get('status') not in ('failed', 'FAIL')
        assert data.get('all_passed', True)
        if isinstance(data.get('checks'), dict):
            assert all(data['checks'].values())
        rows.append({'group': name, 'status': 'PASS', 'script': script,
                     'script_sha256': digest(ROOT / script), 'result': result,
                     'result_sha256': digest(ROOT / result)})
        print(name + ': PASS', flush=True)
    import sympy
    output = {
        'schema': 'C85_REPRODUCTION_CHECKS_V1', 'status': 'PASS',
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'python': sys.version.split()[0], 'sympy': sympy.__version__,
        'groups_recomputed': len(rows), 'groups': rows,
        'integral_mesh_regenerated_by_this_driver': args.recompute_integrals,
        'saved_final_integral_certificate': 'triangle/parallelogram_certificate.json',
        'saved_final_integral_certificate_sha256': digest(ROOT / 'triangle/parallelogram_certificate.json'),
        'scope': 'Exact algebra, finite cases, certificate sums and code-byte bindings. General proofs are separate Markdown files; not a formal proof checker or external peer review.'
    }
    (ROOT / 'CHECKS.json').write_text(json.dumps(output, indent=2) + '\n')
    print('C85: all six groups passed')


if __name__ == '__main__':
    main()
