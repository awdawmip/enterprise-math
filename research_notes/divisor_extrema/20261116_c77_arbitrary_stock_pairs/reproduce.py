"""Verify the archive and replay the exact and numerical controls."""
from hashlib import sha256
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CHECKS = (
    ("check_mixed", "mixed_controls.json"),
    ("check_proportional_edge", "proportional_edge.json"),
    ("check_spectral_rigidity", "spectral_rigidity.json"),
    ("check_spectral_derivative", "spectral_derivative.json"),
    ("check_three_precision", "three_precision.json"),
    ("check_rounded_pairs", "rounded_pairs.json"),
    ("check_decoder_bounds", "decoder_bounds.json"),
    ("check_reconstruct_independent", "reconstruction_independent.json"),
    ("verify_decoder_physical", "decoder_physical.json"),
    ("check_far_decoder", "far_decoder_checks.json"),
    ("check_lattice_decoder", "lattice_checks.json"),
    ("check_critical_three", "critical_three.json"),
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
