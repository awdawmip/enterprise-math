"""Replay the exact C74 controls; --full also rebuilds every large certificate."""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
CASES = (
    (("check_finite.py",), "finite_controls.txt"),
    (("check_same.py", "100"), "through100.json"),
    (("recover_interval.py",), "interval_checks.json"),
    (("gamma_lattice.py",), "gamma_lattice.json"),
    (("check_rare.py",), "rare_rows.json"),
    (("check_outer.py",), "outer_checks.json"),
    (("check_rounding.py",), "rounding_controls_final.json"),
    (("check_precision_pair.py",), "precision_pair.json"),
)


def run(args):
    return subprocess.check_output(args, cwd=ROOT)


def verify(data, name):
    if data != (ROOT / name).read_bytes():
        raise SystemExit(f"Different reference output: {name}")
    print(f"Verified {name}", flush=True)


def large_certificates(directory):
    stock_program = directory / "two_blocks"
    order_program = directory / "same_landing"
    subprocess.run(["c++", "-O3", "-std=c++17", "c74_two_blocks.cpp", "-o",
                    str(stock_program)], cwd=ROOT, check=True)
    runs = [(2501,3000),(4096,4096),(8192,8192),(10000,10000)]
    data = b"".join(run([stock_program, str(lo), str(hi)]) for lo, hi in runs)
    verify(data, "single_h_2501_3000_and_large.txt")
    subprocess.run(["c++", "-O2", "-std=c++17", "order_certificate.cpp", "-lgmpxx",
                    "-lgmp", "-o", str(order_program)], cwd=ROOT, check=True)
    all_outputs = []
    for lo, hi in [(2,250),(251,512),(513,768)]:
        data = run([order_program, str(hi), "3001", str(lo)])
        verify(data, f"cut{hi}.txt")
        all_outputs.append(data)
    verify(b"".join(all_outputs), "same_all_stocks.txt")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true",
                        help="Recompute all 503 stock certificates and 75,202,816 pair tests.")
    opts = parser.parse_args()
    for cmd, reference in CASES:
        verify(run([sys.executable, *cmd]), reference)
    if opts.full:
        with tempfile.TemporaryDirectory() as directory:
            large_certificates(Path(directory))
