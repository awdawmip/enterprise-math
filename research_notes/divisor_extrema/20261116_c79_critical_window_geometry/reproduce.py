"""Verify the archive and replay the exact and numerical controls."""
from hashlib import sha256
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CHECKS = (
    ("check_capacity", "capacity.json"),
    ("check_stock_capacity", "stock_capacity.json"),
    ("check_turning_minors", "turning_minors.json"),
    ("check_three_global", "three_global.json"),
    ("check_phase_carries", "phase_carries.json"),
    ("check_offset_profile", "offset_profile.json"),
    ("check_finite", "finite_control.txt"),
)


def main():
    for line in (HERE / "SHA256SUMS").read_text().splitlines():
        digest, name = line.split("  ", 1)
        if sha256((HERE / name).read_bytes()).hexdigest() != digest:
            raise ValueError("Manifest mismatch in " + name)
    for program, record in CHECKS:
        actual = subprocess.check_output([sys.executable, HERE / (program + ".py")], cwd=HERE)
        if actual != (HERE / record).read_bytes():
            raise ValueError("Replay differs from " + record)
        print("Verified", record, flush=True)


if __name__ == "__main__":
    main()
