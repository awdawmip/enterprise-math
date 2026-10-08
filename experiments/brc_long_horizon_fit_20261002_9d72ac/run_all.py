#!/usr/bin/env python3
"""Reproduce both complete scans, independent audit, figures and manifest."""
import argparse
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reuse-data', action='store_true', help='Use already generated trajectories; still run independent audit and refresh plots/manifest.')
    args = parser.parse_args()
    programs = ([] if args.reuse_data else ['weighted_sweep.py', 'markov_sweep.py'])
    programs += ['audit_check.py', 'summarize.py']
    for name in programs:
        subprocess.run([sys.executable, str(HERE/name)], check=True)
    from make_bundle import write_manifest, verify
    write_manifest()
    print({'verified_experiment_files': verify()})
