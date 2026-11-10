#!/usr/bin/env python3
"""Create a disposable include of the frozen phase-one robust harness."""
import argparse
import hashlib
import json
from pathlib import Path

ROBUST_SHA256 = "d1f9d696ad8f02efad7d79adfca55087dac0a060e4ec4977cb3bc1c597256d26"
SAMPLED_SHA256 = "596cf4add967669ec1feb02344f49ec448bd4c0b927ed9b791cc03d802b86468"


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--robust-source", type=Path, default=here.parent / "brc_robust_sort/robust_bench.cpp")
    parser.add_argument("--sampled-source", type=Path, default=here.parent / "brc_sampled_sort/sampled_bench.cpp")
    parser.add_argument("--output-dir", type=Path, default=here / "build")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for path, expected, signature, replacement, output in [
        (args.robust_source, ROBUST_SHA256, b"int main(int argc,char** argv)",
         b"int robust_frozen_entry(int argc,char** argv)", "robust_frozen_include.hpp"),
        (args.sampled_source, SAMPLED_SHA256, b"int main(int argc, char** argv)",
         b"int sampled_frozen_entry(int argc, char** argv)", "sampled_frozen_include.hpp"),
    ]:
        source = path.read_bytes()
        digest = hashlib.sha256(source).hexdigest()
        if digest != expected:
            raise SystemExit(f"Frozen source SHA256 mismatch for {path.name}: {digest}")
        if source.count(signature) != 1:
            raise SystemExit(f"Expected exactly one final entry-point signature in {path.name}")
        generated = source.replace(signature, replacement, 1)
        if generated.replace(replacement, signature, 1) != source:
            raise SystemExit("Unexpected adapter transformation")
        destination = args.output_dir / output
        destination.write_bytes(generated)
        records.append({"source": str(path.resolve()), "source_sha256": digest,
                        "output": str(destination.resolve()), "replacements": 1,
                        "generated_sha256": hashlib.sha256(generated).hexdigest()})
    print(json.dumps({"result": "PASS", "files": records}))


if __name__ == "__main__":
    main()
