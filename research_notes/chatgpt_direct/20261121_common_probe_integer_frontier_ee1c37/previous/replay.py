"""Replay exact certificates. Default: short checks; --full includes long searches."""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def commands(jobs):
    previous = ROOT / "previous"
    common = ["--previous", str(previous)]
    return {
        "audit": ["new_lower/audit_completed.py", *common, "--receipts", "new_lower/cost_9859_completed.jsonl", "new_lower/cost_9860_completed.jsonl", "--first", "9859", "--last", "9860", "--output", "replay_results/audit"],
        "weighted": ["bias/check_weighted.py"],
        "star": ["fractional/proof/verify.py", "--output", "replay_results/full_star.json"],
        "parity": ["fractional/next_cuts/verify.py", "--output", "replay_results/full_star_parity.json"],
        "upgrade": ["upgrade23/replay.py", "--output", "replay_results/upgrade23.json"],
        "lower": ["lower/replay.py", *common, "--first", "9855", "--last", "9860", "--cores", "0,1,2", "--jobs", str(jobs)],
        "four": ["lower/replay.py", *common, "--first", "9861", "--last", "9870", "--cores", "4", "--jobs", str(jobs)],
        "cores": ["cores/verify_core_three.py", *common, "--jobs", str(jobs)],
        "bias": ["bias/weighted_replay.py", "--denominator", "4", "--jobs", str(jobs)],
        "moments": ["new_lower/replay_moments.py", "--lower-source", "lower", "--output", "replay_results/moments.json"],
        "migration": ["migration20/replay.py", *common],
        "native21_22": ["migration20/native_replay.py", "--budgets", "21,22"],
        "upgrade_native": ["upgrade23/replay.py", "--previous", str(ROOT), "--rebuild-bank", "--native", "--output", "replay_results/upgrade23_rebuilt_native.json"],
        "fractions_old": ["lower/verify_fractional.py", *common],
        "cuts_old": ["cuts/verify.py", *common],
        "bias_q5": ["bias/weighted_replay.py", "--denominator", "5", "--jobs", str(jobs)],
        "endpoint_q5": ["bias/check_endpoint.py"],
    }


QUICK = ["audit", "weighted", "star", "parity", "upgrade"]
FULL = QUICK + ["lower", "four", "cores", "bias", "moments", "migration", "native21_22", "upgrade_native"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", nargs="+", choices=list(commands(2)))
    parser.add_argument("--full", action="store_true", help="Include all current long finite-search certificates")
    parser.add_argument("--jobs", type=int, default=2)
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be positive")
    if args.full and args.only:
        parser.error("Choose --full or --only")
    if not (ROOT / "previous/README.md").is_file():
        parser.error("The complete previous/ dependency archive is required")
    (ROOT / "replay_results").mkdir(exist_ok=True)
    selected = args.only or (FULL if args.full else QUICK)
    for name in selected:
        print(f"Replaying {name}", flush=True)
        subprocess.run([sys.executable, "-B", *commands(args.jobs)[name]], cwd=ROOT, check=True)
        print(f"PASS {name}", flush=True)
