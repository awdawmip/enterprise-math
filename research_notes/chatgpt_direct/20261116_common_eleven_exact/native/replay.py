"""Recheck both tables on the original fifteen-slot components."""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("--original", type=Path, default=HERE.parent / "original")
parser.add_argument("--record", action="store_true")
args = parser.parse_args()
sys.path.insert(0, str(args.original.resolve()))
from frontier9.native.replay_joint import run

for name, filename in (("eleven","best11.txt"), ("twelve","twelve.txt")):
    table = list(map(int, (HERE.parent / "common" / filename).read_text().split()))
    evidence = run(table, 1)
    reference = HERE / (name + ".json")
    if args.record:
        reference.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n")
    else:
        assert json.loads(reference.read_text()) == json.loads(json.dumps(evidence))
    print(name, evidence["joint"]["by_queries"], evidence["joint"]["full_raw_sample"], flush=True)
