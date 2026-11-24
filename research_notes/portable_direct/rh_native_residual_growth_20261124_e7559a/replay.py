#!/usr/bin/env python3
"""Replay the current scientific certificates without mutating them."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,default=root/'prior/riemann_matching_isotonic_anchors_20261124')
    args=parser.parse_args()
    previous=args.previous.resolve()
    manifest=json.loads((root/'MANIFEST.json').read_text())
    for row in manifest['files']:
        assert sha(root/row['path'])==row['sha256'],f'Artifact mismatch: {row["path"]}'
    dependencies=json.loads((root/'DEPENDENCIES.json').read_text())
    for row in dependencies['required_files']:
        assert sha(previous/row['path'])==row['sha256'],f'Predecessor mismatch: {row["path"]}'
    jobs=[
        ('parametric/verify_parametric_envelope.py','parametric/parametric_envelope_certificate.json',None),
        ('compensation/certify_native_compensation.py','compensation/native_compensation_certificate.json','--previous'),
        ('matching/certify_single_thickness_bias.py','matching/single_thickness_bias_certificate.json','--previous'),
        ('anchors/verify_macro_constants.py','anchors/macro_constant_certificate.json',None),
        ('anchors/verify_green_l2.py','anchors/green_l2_certificate.json',None),
        ('parametric/compare_saved_drift.py','parametric/saved_paid_drift_comparison.json','--prior'),
    ]
    with tempfile.TemporaryDirectory(prefix='em-residual-replay-') as temp:
        for script,certificate,option in jobs:
            out=Path(temp)/Path(certificate).name
            command=[sys.executable,str(root/script),'--output',str(out)]
            if option:command.extend([option,str(previous)])
            run=subprocess.run(command,capture_output=True,text=True)
            if run.returncode:
                sys.stderr.write(run.stdout+run.stderr)
                raise SystemExit(run.returncode)
            actual=json.loads(out.read_text())
            expected=json.loads((root/certificate).read_text())
            assert actual==expected,f'Certificate mismatch: {certificate}'
            print('PASS',script,flush=True)
    print('PASS: five strict certificates and one separately labeled saved-data comparison reproduced.')


if __name__=='__main__':main()
