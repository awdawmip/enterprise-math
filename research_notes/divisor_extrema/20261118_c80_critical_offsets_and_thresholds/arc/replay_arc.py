"""Replay one or more saved rank certificates using their precise input values."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

folder=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('degrees',nargs='*',type=int,default=[2])
for degree in parser.parse_args().degrees:
    expected=json.loads((folder/f'd{degree}.json').read_text())
    digits=int(re.fullmatch(r'1e-(\d+)',expected['root_box_radius']).group(1))
    child_env={**os.environ,'ARC_BITS':str(expected['binary_precision'])}
    output=subprocess.check_output([sys.executable,str(folder/'arc_rank.py'),str(degree),str(digits)],env=child_env)
    actual=json.loads(output)
    if actual!=expected:
        raise ValueError(f'Certificate mismatch at degree {degree}: {actual!r}')
    print(f'Degree {degree}: all {actual["columns"]} columns verified, d >= {actual["projective_degree_lower_bound"]}.')
