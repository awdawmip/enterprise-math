#!/usr/bin/env python3
"""Reproduce the bounded X6 study from a repo checkout or the Drive bundle."""
import argparse
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--reuse-data",action="store_true",help="Verify archived data and rebuild figures without regenerating trajectories")
    args=parser.parse_args()
    scripts=["restore_data.py"] if args.reuse_data else ["transfer_sweep.py","restore_data.py","joint_transfer.py","parity_probe.py"]
    scripts += ["root_parity_review.py","audit_check.py","make_figure.py"]
    for script in scripts:
        subprocess.run([sys.executable,str(HERE/script)],check=True,cwd=HERE.parents[1])


if __name__=="__main__":
    main()
