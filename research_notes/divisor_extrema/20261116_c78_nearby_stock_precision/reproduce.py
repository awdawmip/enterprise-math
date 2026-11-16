"""Verify the archive and replay the exact and numerical controls."""
from hashlib import sha256
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CHECKS = (
    ("check_local", "local_checks.json"),
    ("check_euler_packing", "euler_packing.json"),
    ("check_endpoint", "endpoint_checks.json"),
    ("check_cross_curvature", "cross_curvature.json"),
    ("check_confluent_singleton", "confluent_singleton.json"),
    ("check_alias_curvature", "alias_curvature.json"),
    ("check_alias_torsion", "alias_torsion.json"),
    ("check_alias_quadratic", "alias_quadratic.json"),
    ("check_alias_degree", "alias_degree.json"),
    ("check_three_face", "three_face.json"),
    ("critical_bins", "critical_bins.json"),
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
