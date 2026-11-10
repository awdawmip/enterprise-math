#!/usr/bin/env python3
"""Generate disposable entry-point adapters for the three frozen harnesses."""
import argparse
import hashlib
import json
from pathlib import Path

PINS = {
    "adaptive": "c98662a7ed38858c186dfd238c4b6b1d1bacdd51cff891ba7f5591c583d831a9",
    "robust": "d1f9d696ad8f02efad7d79adfca55087dac0a060e4ec4977cb3bc1c597256d26",
    "sampled": "596cf4add967669ec1feb02344f49ec448bd4c0b927ed9b791cc03d802b86468",
}


def main():
    here = Path(__file__).resolve().parent
    p = argparse.ArgumentParser(description=__doc__)
    for name in PINS:
        p.add_argument(f"--{name}-source", type=Path,
                       default=here.parent / f"brc_{name}_sort/{name}_bench.cpp")
    p.add_argument("--output-dir", type=Path, default=here / "build")
    args = p.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for name, expected in PINS.items():
        path = getattr(args, f"{name}_source")
        source = path.read_bytes()
        actual = hashlib.sha256(source).hexdigest()
        if actual != expected:
            raise SystemExit(f"Frozen {name} source mismatch: {actual}")
        signature = (b"int main(int argc, char** argv)" if name == "sampled"
                     else b"int main(int argc,char** argv)")
        replacement = (f"int {name}_frozen_entry(int argc, char** argv)" if name == "sampled"
                       else f"int {name}_frozen_entry(int argc,char** argv)").encode()
        if source.count(signature) != 1:
            raise SystemExit(f"Expected one entry-point signature: {path}")
        generated = source.replace(signature, replacement, 1)
        destination = args.output_dir / f"{name}_frozen_include.hpp"
        destination.write_bytes(generated)
        records.append({"source": str(path.resolve()), "source_sha256": actual,
                        "output": str(destination.resolve()), "replacements": 1,
                        "generated_sha256": hashlib.sha256(generated).hexdigest()})
    print(json.dumps({"result": "PASS", "files": records}))


if __name__ == "__main__":
    main()
