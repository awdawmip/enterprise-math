#!/usr/bin/env python3
"""Package the selection phase and all frozen measured source dependencies."""
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
        root.parent / "brc_residual_sort_adaptive_20261110_b0e94005",
        root.parent / "brc_adaptive_sort") if (p / "make_bundle.py").is_file()), None)
    if previous is None:
        raise SystemExit("Missing exact phase-two bundle maker and source dependencies")
    with tempfile.TemporaryDirectory(prefix="brc-selection-bundle-") as tmp:
        prior_zip = Path(tmp) / "prior.zip"
        subprocess.run([sys.executable, str(previous / "make_bundle.py"),
                        "--output", str(prior_zip)], check=True, capture_output=True)
        with zipfile.ZipFile(prior_zip) as archive:
            files = {name: archive.read(name) for name in archive.namelist()
                     if name not in {"BUNDLE_MANIFEST.json", "README_BUNDLE.md"}}
    canonical = "brc_residual_sort_selection_20261110_b0e94005"
    names = [
        "README.md", "REVIEW.md", "THEORY.md", "DESIGN.md",
        "selection_bench.cpp", "selection_kernels.hpp", "prepare_frozen_include.py",
        "run_experiment.py", "analyze_results.py", "make_bundle.py", "write_report.py",
        "frozen_manifest.json", "execution_harness_verify_v2.json",
        "execution_sanitized_verify.json", "execution_calibration.json",
        "execution_all_frozen.json", "analysis_summary.json", "analysis_table.md",
        "analysis_heldout_speedup.png", "analysis_heldout_speedup.svg",
        "results_all.csv", "results_all.csv.selection_nodes.csv",
        "results_all.csv.selection_attempts.csv", "results_calibration.csv",
        "results_calibration.csv.selection_nodes.csv", "results_calibration.csv.selection_attempts.csv",
        "selection_certificate.py", "selection_certificate_results.json",
    ]
    for name in names:
        files[f"{canonical}/{name}"] = (root / name).read_bytes()
    files["README_BUNDLE.md"] = f"""# Residual integer sorting reproduction bundle

This bundle contains the three measured repair phases and every exact C++
dependency needed for the newest phase. Earlier reports retain their original
hardware/timing provenance. New phase-three comparisons rebuild all controls on
the same AMD EPYC9V74/GCC14.2.0 host; historical absolute timings are not pooled.
No prebuilt executables or credentials are included. pdqsort's license is retained.

From the extracted bundle:

```bash
cd {canonical}
python run_experiment.py --verify-only --cpu 0
python run_experiment.py --sanitize --verify-only --cpu 1
python run_experiment.py --skip-build --skip-verify --cpu 0 --subset all
python analyze_results.py results_all.csv
```

Use CPU identifiers allowed by your local affinity. Builds require Linux taskset,
GCC with C++20 and Python's standard library. Plotting additionally uses NumPy and
Matplotlib. The runners check frozen dependency hashes and make disposable include
adapters. Timings must be rerun on the target host; supplied data are actual run
records, not expected portable timings. Every accepted counting node of the fused
output candidates writes exactly n final values; this excludes recursive/fallback
internals and does not claim n total operations.

Read {canonical}/README.md for measured successes, failures and comparisons,
THEORY.md for definitions/proofs and REVIEW.md for author-side validation scope.
The manifest gives bytes and SHA256 for every file except itself.
""".encode()
    manifest = {"format": "BRC_RESIDUAL_SORT_REPRODUCTION_BUNDLE_V2",
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
