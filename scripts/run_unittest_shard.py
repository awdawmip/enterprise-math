#!/usr/bin/env python3
"""Run one deterministic shard of the repository unittest suite.

This preserves the exact ``tests/test*.py`` discovery universe while splitting
wall-clock work across multiple GitHub-hosted runners. Files are sorted and
assigned round-robin by index, so every discovered test file belongs to exactly
one shard and no test semantics are weakened.
"""
from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = ROOT / "tests"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_files() -> list[Path]:
    return sorted(path for path in TEST_ROOT.glob("test*.py") if path.is_file())


def shard_files(index: int, count: int) -> list[Path]:
    if count < 1:
        raise ValueError("count must be >= 1")
    if index < 0 or index >= count:
        raise ValueError("index must satisfy 0 <= index < count")
    return [path for offset, path in enumerate(test_files()) if offset % count == index]


def build_suite(index: int, count: int) -> unittest.TestSuite:
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for path in shard_files(index, count):
        suite.addTests(loader.discover(str(TEST_ROOT), pattern=path.name))
    return suite


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one deterministic unittest file shard")
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--count", type=int, required=True)
    args = parser.parse_args()

    files = shard_files(args.index, args.count)
    if not files:
        print(f"ERROR: shard {args.index}/{args.count} has no test files", file=sys.stderr)
        return 2
    print(
        f"UNITTEST_SHARD index={args.index} count={args.count} files={len(files)} total={len(test_files())}",
        flush=True,
    )
    for path in files:
        print(path.relative_to(ROOT).as_posix(), flush=True)

    result = unittest.TextTestRunner(verbosity=2).run(build_suite(args.index, args.count))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
