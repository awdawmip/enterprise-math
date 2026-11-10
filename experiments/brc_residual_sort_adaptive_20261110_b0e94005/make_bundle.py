#!/usr/bin/env python3
"""Package both measured phases and the exact source dependencies for reproduction."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile


def add_tree(files, source, destination, names):
    for name in names:
        path = source / name
        if not path.is_file():
            raise SystemExit(f"Missing bundle input: {path}")
        files[f"{destination}/{name}"] = path.read_bytes()


def locate(parent, short, canonical):
    for path in (parent / canonical, parent / short):
        if path.is_dir():
            return path
    raise SystemExit(f"Cannot find {canonical}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    root = Path(__file__).resolve().parent
    parent = root.parent
    out = args.output or root / "brc_sort_reproducibility.zip"
    names = {
        "adaptive": "brc_residual_sort_adaptive_20261110_b0e94005",
        "robust": "brc_residual_sort_robust_20261110_b0e94005",
        "sampled": "brc_residual_sort_sampled_20261108_b0e94005",
        "expanded": "brc_residual_sort_expanded_20261107_b0e94005",
        "local": "brc_residual_sort_local_20261107_b0e94005",
    }
    robust = locate(parent, "brc_robust_sort", names["robust"])
    files = {}
    shared = ["README.md", "THEORY.md", "REVIEW.md", "run_experiment.py", "analyze_results.py",
              "prepare_frozen_include.py", "frozen_implementation.json", "analysis_summary.json",
              "analysis_table.md", "analysis_heldout_speedup.svg", "analysis_heldout_speedup.png",
              "execution_sanitized_verify.json", "execution_all_frozen.json", "harness_integration_receipt.json"]
    add_tree(files, root, names["adaptive"], shared + [
        "adaptive_bench.cpp", "adaptive_kernels.hpp", "make_bundle.py",
        "execution_optimized_verify_v2.json", "execution_calibration.json", "adaptive_validation_optimized.json",
        "results_all.csv", "results_all.csv.adaptive_nodes.csv", "results_all.csv.adaptive_attempts.csv",
        "results_calibration.csv", "results_calibration.csv.adaptive_nodes.csv",
        "results_calibration.csv.adaptive_attempts.csv"])
    add_tree(files, robust, names["robust"], shared + [
        "robust_bench.cpp", "robust_kernels.hpp", "sample_tail_probability.py", "sampling_probabilities.json",
        "execution_optimized_verify_v1.json", "execution_calibration_final.json", "execution_calibration_precompact.json",
        "robust_validation_optimized.json", "results_all.csv", "results_all.csv.robust_nodes.csv",
        "results_calibration_final.csv", "results_calibration_final.csv.robust_nodes.csv",
        "results_calibration_precompact.csv", "results_calibration_precompact.csv.robust_nodes.csv",
        "calibration_precompact/PROVENANCE.md", "calibration_precompact/robust_bench.cpp",
        "calibration_precompact/robust_kernels.hpp", "robust_compile_optimized_precompact_v2.json",
        "robust_verify_execution_precompact_v2.json", "vendor/SOURCE.json", "vendor/pdqsort.h", "vendor/license.txt"])
    add_tree(files, locate(parent, "brc_sampled_sort", names["sampled"]), names["sampled"],
             ["sampled_bench.cpp", "sampled_kernels.hpp", "flat_frequency.hpp"])
    add_tree(files, locate(parent, "brc_expanded_sort", names["expanded"]), names["expanded"], ["pure_bench.cpp"])
    add_tree(files, locate(parent, "brc_local_sort", names["local"]), names["local"], ["local_kernels.hpp"])
    readme = f"""# Residual integer sorting reproduction bundle

The two measured phases and all required C++ source dependencies are included.
No prebuilt executables or credentials are included. The per-phase reports retain
successful and failed conditions and explain the scope of each comparison.

For phase two, from the extracted bundle:

```bash
cd {names['adaptive']}
python run_experiment.py --verify-only --cpu 0
python run_experiment.py --sanitize --verify-only --cpu 1
python run_experiment.py --skip-build --skip-verify --cpu 0 --subset all
python analyze_results.py results_all.csv
```

Choose available CPU identifiers on your machine. The measured environment used
Linux, GCC13.3.0 and C++20. Verification and benchmark orchestration use Python's
standard library; analysis plots additionally need NumPy and Matplotlib.
The runners check pinned dependency bytes and generate disposable include files.
All timings must be rerun locally; the supplied CSVs are the actual recorded run.

Phase-one report: {names['robust']}/README.md
Phase-two report: {names['adaptive']}/README.md
Mathematical conditions and counterexamples are in their THEORY.md files.

The manifest lists SHA256 for every packaged file except itself. Source licenses
are retained, including upstream pdqsort's Zlib license.
"""
    files["README_BUNDLE.md"] = readme.encode()
    manifest = {"format": "BRC_RESIDUAL_SORT_REPRODUCTION_BUNDLE_V1",
                "files": {k: {"bytes": len(v), "sha256": hashlib.sha256(v).hexdigest()}
                          for k, v in sorted(files.items())}}
    files["BUNDLE_MANIFEST.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 11, 10, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(out) as z:
        assert z.testzip() is None
        for name, data in files.items():
            assert hashlib.sha256(z.read(name)).digest() == hashlib.sha256(data).digest()
    print(json.dumps({"archive": str(out), "files": len(files), "bytes": out.stat().st_size,
                      "sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
                      "crc_and_content_check": "PASS"}, indent=2))


if __name__ == "__main__":
    main()
