#!/usr/bin/env python3
"""Make a disposable include of the pinned preceding harness.

The preceding file locally defines and undefines main while including its own
base, so an enclosing main macro cannot rename its final entry point. Exactly
one entry-point signature is replaced; every algorithm/generator/timer byte is
otherwise preserved. The generated file belongs in build/, not in source control.
"""
import argparse
import hashlib
import json
from pathlib import Path

SOURCE_COMMIT = "8bf6a677359b62d406eaa7258f5541431466315b"
SOURCE_SHA256 = "596cf4add967669ec1feb02344f49ec448bd4c0b927ed9b791cc03d802b86468"
SIGNATURE = b"int main(int argc, char** argv)"
REPLACEMENT = b"int sampled_frozen_entry(int argc, char** argv)"


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path,
                        default=here.parent / "brc_sampled_sort" / "sampled_bench.cpp")
    parser.add_argument("--output", type=Path,
                        default=here / "build" / "sampled_frozen_include.hpp")
    args = parser.parse_args()
    content = args.source.read_bytes()
    actual_hash = hashlib.sha256(content).hexdigest()
    if actual_hash != SOURCE_SHA256:
        raise SystemExit(f"Frozen sampled harness SHA256 mismatch: {actual_hash}")
    if content.count(SIGNATURE) != 1:
        raise SystemExit("Expected exactly one final entry-point signature")
    generated = content.replace(SIGNATURE, REPLACEMENT, 1)
    if generated.replace(REPLACEMENT, SIGNATURE, 1) != content:
        raise SystemExit("Adapter changed bytes beyond the entry-point signature")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(generated)
    print(json.dumps({"result": "PASS", "source_commit": SOURCE_COMMIT,
                      "source": str(args.source.resolve()), "source_sha256": actual_hash,
                      "output": str(args.output.resolve()), "replacements": 1,
                      "generated_sha256": hashlib.sha256(generated).hexdigest()}))


if __name__ == "__main__":
    main()
