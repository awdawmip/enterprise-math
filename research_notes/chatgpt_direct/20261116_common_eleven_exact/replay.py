"""Replay from this package, or pass the preceding package with --original."""
import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil

ROOT = Path(__file__).resolve().parent

def execute(task):
    folder, script, reference, flags = task
    cmd = [sys.executable, "-B", str(folder / script), *flags]
    output = subprocess.check_output(cmd, cwd=folder, text=True)
    if reference:
        assert json.loads(output) == json.loads((folder / reference).read_text()), script
    print("PASS", script, flush=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--original", type=Path, default=ROOT / "original")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as scratch:
        common = Path(scratch) / "common"
        shutil.copytree(ROOT / "common", common)
        # These two inventory generators serialize their output next to the generator.
        subprocess.run([sys.executable, "-B", "cyclic11.py"], cwd=common, check=True, stdout=subprocess.DEVNULL)
        subprocess.run([sys.executable, "-B", "residual11.py"], cwd=common, check=True, stdout=subprocess.DEVNULL)
        for f in ("cyclic11.json","residual11.json","best11.txt"):
            assert (common/f).read_bytes() == (ROOT/"common"/f).read_bytes(), f
        print("PASS cyclic and unrestricted residual inventories", flush=True)
        tasks = [
            (common,"check_tables.py","endpoints.json",[]),
            (common,"six_form.py",None,[]),
            (ROOT/"independent","check.py","result.json",[]),
            (ROOT/"native","replay.py",None,["--original",str(args.original.resolve())]),
            (common,"six13.py","six13.json",[]),
            (common,"eleven_orbits.py","eleven_orbits.json",[]),
            (ROOT/"lower","replay.py","result.json",[]),
            (common,"five13_stratum.py","five13_stratum.json",[]),
        ]
        with ThreadPoolExecutor(max_workers=3) as pool:
            list(pool.map(execute,tasks))

if __name__ == "__main__":
    main()
