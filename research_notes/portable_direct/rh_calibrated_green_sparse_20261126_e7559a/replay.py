#!/usr/bin/env python3
"""Replay the four current strict certificates against pinned predecessor data."""
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
    root=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,default=root/'prior/riemann_signed_green_thickness_phase_20261124')
    args=parser.parse_args()
    previous=args.previous.resolve()
    for row in json.loads((root/'MANIFEST.json').read_text())['files']:
        assert digest(root/row['path'])==row['sha256'],f'Artifact mismatch: {row["path"]}'
    for row in json.loads((root/'DEPENDENCIES.json').read_text())['required_files']:
        assert digest(previous/row['path'])==row['sha256'],f'Predecessor mismatch: {row["path"]}'
    jobs=[
        ('calibrated_family/certify_calibrated_family.py','calibrated_family/calibrated_family_certificate.json'),
        ('group_arithmetic/certify_grouped_dirichlet.py','group_arithmetic/grouped_dirichlet_certificate.json'),
        ('sampling/certify_sparse_skeleton.py','sampling/sparse_skeleton_certificate.json'),
        ('exact_tree/certify_depth_four_energy.py','exact_tree/depth_four_energy_certificate.json'),
    ]
    with tempfile.TemporaryDirectory(prefix='em-calibrated-green-replay-') as temp:
        for script,certificate in jobs:
            output=Path(temp)/Path(certificate).name
            command=[sys.executable,str(root/script),'--previous',str(previous),'--output',str(output)]
            result=subprocess.run(command,capture_output=True,text=True)
            if result.returncode:
                sys.stderr.write(result.stdout+result.stderr)
                raise SystemExit(result.returncode)
            assert json.loads(output.read_text())==json.loads((root/certificate).read_text()),f'Certificate mismatch: {certificate}'
            print('PASS',script,flush=True)
    print('PASS: four strict certificates reproduced. Exploratory output is not used for certificate decisions.')


if __name__=='__main__':
    main()
