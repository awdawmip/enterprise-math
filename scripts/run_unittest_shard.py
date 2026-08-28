#!/usr/bin/env python3
"""Run one deterministic shard of the repository unittest suite.

This preserves the exact ``tests/test*.py`` discovery universe while splitting
wall-clock work across multiple GitHub-hosted runners. Files are sorted and
assigned round-robin by index, so every discovered test file belongs to exactly
one shard and no test semantics are weakened.

A file named ``tests/test*.py`` is a test contract. Silently discovering zero
``unittest`` cases from such a file is forbidden: it previously allowed
pytest-style top-level functions to appear in shard listings while never running.
The runner therefore fails closed when any assigned test file contributes zero
cases.

Control-plane tests exercise the same fault-isolated operational view used by
live dispatch. Strict/raw validators remain separately callable from the
reference-integrity workflow; forgetting an import-side bootstrap in an
individual test module must not resurrect a task-local fault into a global test
process denial of service.
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

from control_plane import research_control_bootstrap  # noqa: E402


def test_files() -> list[Path]:
    return sorted(path for path in TEST_ROOT.glob("test*.py") if path.is_file())


def shard_files(index: int, count: int) -> list[Path]:
    if count < 1:
        raise ValueError("count must be >= 1")
    if index < 0 or index >= count:
        raise ValueError("index must satisfy 0 <= index < count")
    return [path for offset, path in enumerate(test_files()) if offset % count == index]


def build_suite(index: int, count: int) -> tuple[unittest.TestSuite, dict[str, int]]:
    # Install once before importing any test module. This is deliberately the
    # operational view, not an audit waiver: exact quarantines are validated by
    # the bootstrap and strict/raw integrity checks run in their own CI gates.
    research_control_bootstrap.install(ROOT)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    counts: dict[str, int] = {}
    zero_case_files: list[str] = []

    for path in shard_files(index, count):
        discovered = loader.discover(str(TEST_ROOT), pattern=path.name)
        case_count = discovered.countTestCases()
        rel = path.relative_to(ROOT).as_posix()
        counts[rel] = case_count
        if case_count == 0:
            zero_case_files.append(rel)
            continue
        suite.addTests(discovered)

    if zero_case_files:
        joined = ", ".join(zero_case_files)
        raise RuntimeError(
            "test discovery contract violation: tests/test*.py file(s) produced zero unittest cases: "
            + joined
            + "; convert them to unittest.TestCase or remove/rename them if they are not tests"
        )

    return suite, counts


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

    try:
        suite, counts = build_suite(args.index, args.count)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        return 2

    for path, case_count in counts.items():
        print(f"UNITTEST_DISCOVERY {path} cases={case_count}", flush=True)

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
