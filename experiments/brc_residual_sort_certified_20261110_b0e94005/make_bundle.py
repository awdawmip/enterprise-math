#!/usr/bin/env python3
"""Package the certified-selection phase and all frozen measured dependencies."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    previous = next((p for p in (
        root.parent / "brc_residual_sort_selection_20261110_b0e94005",
        root.parent / "brc_selection_sort") if (p / "make_bundle.py").is_file()), None)
    if previous is None:
        raise SystemExit("Missing exact phase-three bundle maker and source dependencies")
    with tempfile.TemporaryDirectory(prefix="brc-certified-bundle-") as tmp:
        prior_zip = Path(tmp) / "prior.zip"
        subprocess.run([sys.executable, str(previous / "make_bundle.py"),
                        "--output", str(prior_zip)], check=True, capture_output=True)
        with zipfile.ZipFile(prior_zip) as archive:
            files = {name: archive.read(name) for name in archive.namelist()
                     if name not in {"BUNDLE_MANIFEST.json", "README_BUNDLE.md"}}
    canonical = "brc_residual_sort_certified_20261110_b0e94005"
    names = [
        "README.md", "REVIEW.md", "THEORY.md", "DESIGN.md",
        "certified_bench.cpp", "certified_kernels.hpp", "prepare_frozen_include.py",
        "run_experiment.py", "analyze_results.py", "make_bundle.py", "write_report.py",
        "frozen_manifest.json", "execution_optimized_verify_v1.json",
        "execution_sanitized_verify.json", "execution_all_frozen.json",
        "analysis_summary.json", "analysis_table.md",
        "analysis_heldout_speedup.png", "analysis_heldout_speedup.svg",
        "results_all.csv", "results_all.csv.certified_nodes.csv",
        "results_all.csv.certified_attempts.csv", "results_all.csv.selection_attempts.csv",
    ]
    for name in names:
        files[f"{canonical}/{name}"] = (root / name).read_bytes()
    files["README_BUNDLE.md"] = f"""# Residual integer sorting reproduction bundle

This bundle contains four measured repair phases and all exact source dependencies.
Historical reports retain their original host/compiler provenance. Phases three
and four rebuild every earlier control in the same current AMD EPYC9V74/GCC14.2.0
binary for each experiment; old Intel-host absolute times are not pooled.
No prebuilt executables or credentials are included; source licenses are retained.

From the extracted bundle:

```bash
cd {canonical}
python run_experiment.py --verify-only --cpu 0
python run_experiment.py --sanitize --verify-only --cpu 1
python run_experiment.py --skip-build --skip-verify --cpu 0 --subset all --output results_local.csv --receipt execution_local.json
python analyze_results.py results_local.csv --prefix local
```

Choose available CPU identifiers. Builds require Linux taskset, GCC/C++20 and
Python's standard library; plotting additionally uses NumPy and Matplotlib.
Runners verify frozen dependency bytes and generate disposable include adapters.
The supplied files retain the original observed run; the commands above write
fresh timing evidence under different names.

The newest phase adds best-singleton, exact fractional rejection and conditional
mass-index DP after a failed greedy sample-half proposal. Its completeness theorem
concerns only whole-bin half-sample feasibility on a fixed learned grid. It does
not guarantee maximum actual population coverage or minimum runtime; only the DP
branch guarantees maximum feasible sample mass. The actual residual half gate and
full ascending multiset output remain separately verified.

See {canonical}/README.md for all measured gains/losses and controls, THEORY.md
for proofs, and REVIEW.md for the author-side review. The prior density/gap/fused
phase is in brc_residual_sort_selection_20261110_b0e94005/README.md.
The manifest contains bytes/SHA256 for every packaged file except itself.
""".encode()
    manifest = {"format": "BRC_RESIDUAL_SORT_REPRODUCTION_BUNDLE_V3",
                "files": {name: {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
                          for name, data in sorted(files.items())}}
    files["BUNDLE_MANIFEST.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    out = args.output or root / "brc_sort_reproducibility.zip"
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 11, 10, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        for name, data in files.items():
            assert archive.read(name) == data
    print(json.dumps({"archive": str(out), "files": len(files), "bytes": out.stat().st_size,
                      "sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
                      "crc_and_content_check": "PASS"}, indent=2))


if __name__ == "__main__":
    main()
