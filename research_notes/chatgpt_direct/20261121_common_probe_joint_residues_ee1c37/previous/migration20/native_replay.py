"""Check the new 20, 21 and 22 label tables with the original program receipts."""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
previous = HERE.parent / "previous"
third = previous / "previous/previous/previous/previous"
sys.path.insert(0, str(third / "original"))
from frontier9.native.replay_joint import run

witness = json.loads((HERE / "twenty_transition.json").read_text())
q = json.loads((HERE / "two_step_extension.json").read_text())["branches"][0]["first_new_label"]
q = set(q)
tables = {20: witness["old"], 21: witness["new"], 22: [sorted(set(r) - q) for r in witness["new"]] + [sorted(q)]}
parser = argparse.ArgumentParser()
parser.add_argument("--budgets", default="20,21,22")
args = parser.parse_args()
results = {}
for k, rows in tables.items():
    if k not in set(map(int, args.budgets.split(","))):
        continue
    code = [0] * 125
    for label, row in enumerate(rows):
        for x in row:
            code[x] = label
    receipt = run(code, 1)
    assert receipt["joint"]["total_queries"] == {20: 4475, 21: 4140, 22: 3855}[k]
    results[k] = receipt
    (HERE / f"native_{k}.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(k, receipt["joint"]["total_queries"], receipt["joint"]["full_raw_sample"], flush=True)
(HERE / "native_result.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
