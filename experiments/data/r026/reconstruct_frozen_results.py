#!/usr/bin/env python3
"""Reconstruct exact frozen R026 machine results from base64 text parts."""
from pathlib import Path
import argparse
import base64
import gzip
import hashlib

ROOT = Path(__file__).resolve().parent
FROZEN = {
    "json": {
        "glob": "r026_collapse_external_benchmark_results.json.gz.b64part*",
        "output": "r026_collapse_external_benchmark_results.json",
        "gzip_sha256": "ebc643c30a02384510625d5997f8d0d497275969e3923b0769a2a341c7cf7e9e",
        "raw_sha256": "a7b69a96d31316b6ff78f03b31577e2ef27ae1f7f04a49ad486ab2db53b4d00b",
    },
    "csv": {
        "glob": "r026_collapse_external_benchmark_results.csv.gz.b64part*",
        "output": "r026_collapse_external_benchmark_results.csv",
        "gzip_sha256": "d16f6e0390f3b8f1d39927adcf01c05b8fd3e5ee806a635a3084ef7422d53cbf",
        "raw_sha256": None,
    },
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reconstruct(kind: str) -> Path:
    spec = FROZEN[kind]
    parts = sorted(ROOT.glob(spec["glob"]))
    if not parts:
        raise SystemExit(f"no frozen {kind} parts found")
    packed = "".join(p.read_text(encoding="ascii") for p in parts)
    gz = base64.b64decode(packed)
    gz_digest = sha256(gz)
    if gz_digest != spec["gzip_sha256"]:
        raise SystemExit(f"{kind} gzip sha256 mismatch: {gz_digest}")
    raw = gzip.decompress(gz)
    raw_digest = sha256(raw)
    if spec["raw_sha256"] and raw_digest != spec["raw_sha256"]:
        raise SystemExit(f"{kind} raw sha256 mismatch: {raw_digest}")
    out = ROOT / spec["output"]
    out.write_bytes(raw)
    print(f"{kind}: {out} gzip_sha256={gz_digest} raw_sha256={raw_digest}")
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=sorted(FROZEN))
    args = parser.parse_args()
    reconstruct(args.kind)
