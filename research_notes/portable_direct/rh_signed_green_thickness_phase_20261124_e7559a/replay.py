#!/usr/bin/env python3
"""Reproduce this round's four strict certificates without overwriting them."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,default=root/'prior/riemann_native_residual_growth_20261124')
    args=parser.parse_args();previous=args.previous.resolve()
    for row in json.loads((root/'MANIFEST.json').read_text())['files']:
        assert digest(root/row['path'])==row['sha256'],f'Artifact mismatch: {row["path"]}'
    for row in json.loads((root/'DEPENDENCIES.json').read_text())['required_files']:
        assert digest(previous/row['path'])==row['sha256'],f'Predecessor mismatch: {row["path"]}'
    jobs=[
        ('residual_strength/verify_road_convex_strength.py','residual_strength/road_convex_strength_certificate.json',None),
        ('coherent_matching/verify_uniform_thickness_identities.py','coherent_matching/uniform_thickness_identity_certificate.json',None),
        ('signed_green/certify_signed_green_grouping.py','signed_green/signed_green_grouping_certificate.json',previous/'prior/riemann_matching_isotonic_anchors_20261124'),
        ('fixed_family/certify_fixed_family_density.py','fixed_family/fixed_family_density_certificate.json',previous),
    ]
    with tempfile.TemporaryDirectory(prefix='em-signed-green-replay-') as temp:
        for script,certificate,input_root in jobs:
            output=Path(temp)/Path(certificate).name
            command=[sys.executable,str(root/script),'--output',str(output)]
            if input_root is not None:command+=['--previous',str(input_root)]
            result=subprocess.run(command,capture_output=True,text=True)
            if result.returncode:
                sys.stderr.write(result.stdout+result.stderr);raise SystemExit(result.returncode)
            assert json.loads(output.read_text())==json.loads((root/certificate).read_text()),f'Certificate mismatch: {certificate}'
            print('PASS',script,flush=True)
    print('PASS: four strict certificates reproduced; separately labeled exploration was not promoted to a strict certificate.')


if __name__=='__main__':main()
