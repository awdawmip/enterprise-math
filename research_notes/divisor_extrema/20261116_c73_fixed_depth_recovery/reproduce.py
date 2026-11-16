"""Run each published exact control and check its reference output."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASES = (
    ("check_prefix.py", "center_checks.json"),
    ("check_three_state.py", "native_checks.json"),
    ("check_linear_landing.py", "linear_checks.txt"),
    ("verify_fixed_h.py", "fixed_h_checks.txt"),
    ("check_fixed_h_gap.py", "fixed_h_gaps.txt"),
    ("check_four_five.py", "four_five_checks.json"),
    ("four_five_independent.py", "four_five_rank.txt"),
    ("audit_four_five.py", "four_five_derivatives.txt"),
    ("check_single.py", "single_checks.txt"),
    ("check_single_stock.py", "calibration_checks.txt"),
    ("radical_decoder.py", "radical_controls.json"),
    ("certify_two_single.py", "physical_two_single.json"),
    ("decode_two_blocks.py", "two_decode.json"),
    ("decode_one_preparation.py", "one_preparation.json"),
    ("blind_center_decoder.py --full", "blind_center_check.json"),
)

if __name__ == "__main__":
    for command, output in CASES:
        result = subprocess.check_output([sys.executable, *command.split()], cwd=HERE)
        if result != (HERE / output).read_bytes():
            raise SystemExit(f"Output mismatch for {command}: {output}")
        print(f"Verified {output}", flush=True)
