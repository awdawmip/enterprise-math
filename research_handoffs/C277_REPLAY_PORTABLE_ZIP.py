#!/usr/bin/env python3
"""C277 author exact replay launcher for the separately delivered portable ZIP.

This is a small GitHub-persisted launcher, NOT the 69KB standalone proof
program itself. Run it with the original ZIP from this conversation.
It validates the ZIP digest and each SHA256 manifest entry before execution.
Does not perform native Source claim or independent Driver review.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

EXPECTED_ZIP_SHA256 = "56966756a4a8ae0eacb57cfb8af9f94fbee98849e142ae3320cf1a76a5ad789a"
EXPECTED_CODE_SHA256 = "63f2745b2af840eb788ec94dfe658906dd57dd62bde5b64238b0111538b7c58e"
PAIRS = ((9, 23), (18, 19), (8, 29), (25, 29), (11, 28), (6, 18))

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def verify_package(path):
    raw = path.read_bytes()
    assert sha256(raw) == EXPECTED_ZIP_SHA256, "ZIP_SHA256_MISMATCH"
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, "ZIP_CRC_ERROR"
        names = archive.namelist()
        assert all(Path(name).name == name for name in names), "INVALID_ENTRY_NAME"
        assert len(names) == len(set(names)), "DUPLICATE_ENTRY"
        manifest = json.loads(archive.read("C277_FILE_HASH_MANIFEST.json"))
        for name, item in manifest["entries"].items():
            contents = archive.read(name)
            assert len(contents) == item["size"], ("SIZE_MISMATCH", name)
            assert sha256(contents) == item["sha256"], ("DIGEST_MISMATCH", name)
        code = archive.read("C277_STANDALONE_EXACT_REPLAY.py")
        assert sha256(code) == EXPECTED_CODE_SHA256, "PROOF_CODE_MISMATCH"
    return len(names)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", type=Path)
    parser.add_argument("--inventory-only", action="store_true")
    parser.add_argument("--pair", nargs=2, type=int)
    args = parser.parse_args()
    paths = [tuple(args.pair)] if args.pair else PAIRS
    assert all(p in PAIRS for p in paths), "UNKNOWN_PARENT_HULL"
    checked = verify_package(args.zip_path)
    with tempfile.TemporaryDirectory(prefix="em-c277-proof-") as name:
        with zipfile.ZipFile(args.zip_path) as archive:
            archive.extract("C277_STANDALONE_EXACT_REPLAY.py", path=name)
        checker = Path(name) / "C277_STANDALONE_EXACT_REPLAY.py"
        commands = [["--inventory"]]
        if not args.inventory_only:
            commands.extend([["--pair", str(i), str(j)] for i, j in paths])
        for cmd in commands:
            completed = subprocess.run(
                [sys.executable, str(checker), *cmd],
                check=True, capture_output=True, text=True,
            )
            output = completed.stdout
            assert "PASS" in output, ("MISSING_PASS", cmd)
            print(output.strip(), flush=True)
    print("C277_ZIP_REPLAY_PASS", checked, "zip entries", len(commands), "check commands")

if __name__ == "__main__":
    main()
