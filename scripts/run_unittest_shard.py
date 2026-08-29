#!/usr/bin/env python3
"""Run one deterministic shard of the repository Python test suite.

The repository historically contains both ``unittest.TestCase`` tests and
pytest-style top-level ``def test_*`` functions.  The old shard runner used only
``unittest`` discovery, which meant top-level functions could appear in shard
listings while never executing.  Silent skips are forbidden.

This runner therefore loads each assigned test module exactly once, executes all
ordinary unittest cases, and adapts top-level synchronous ``test_*`` functions
with no required fixture arguments into ``unittest.FunctionTestCase``.  A
pytest-style test that requires fixture/parameter injection or is async fails
closed with an explicit discovery-contract error rather than being skipped or
called incorrectly.

Control-plane tests exercise the same fault-isolated operational view used by
live dispatch. Strict/raw validators remain separately callable from the
reference-integrity workflow.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import inspect
import sys
import unittest
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = ROOT / "tests"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))

from control_plane import research_control_bootstrap  # noqa: E402


class TestDiscoveryContractError(RuntimeError):
    pass


def test_files() -> list[Path]:
    return sorted(path for path in TEST_ROOT.glob("test*.py") if path.is_file())


def shard_files(index: int, count: int) -> list[Path]:
    if count < 1:
        raise ValueError("count must be >= 1")
    if index < 0 or index >= count:
        raise ValueError("index must satisfy 0 <= index < count")
    return [path for offset, path in enumerate(test_files()) if offset % count == index]


def _module_name(path: Path) -> str:
    digest = hashlib.sha256(path.resolve().as_posix().encode("utf-8")).hexdigest()[:12]
    return f"_enterprise_math_test_{path.stem}_{digest}"


def load_test_module(path: Path) -> ModuleType:
    name = _module_name(path)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise TestDiscoveryContractError(f"cannot create import spec for {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except Exception as exc:
        sys.modules.pop(name, None)
        raise TestDiscoveryContractError(
            f"test module import failed for {path}: {type(exc).__name__}: {exc}"
        ) from exc
    return module


def top_level_function_tests(module: ModuleType, rel: str) -> list[unittest.FunctionTestCase]:
    out: list[unittest.FunctionTestCase] = []
    unsupported: list[str] = []
    for name, value in sorted(vars(module).items()):
        if not name.startswith("test_") or not inspect.isfunction(value):
            continue
        if value.__module__ != module.__name__:
            continue
        if inspect.iscoroutinefunction(value):
            unsupported.append(f"{name}(async)")
            continue
        signature = inspect.signature(value)
        required = [
            parameter.name
            for parameter in signature.parameters.values()
            if parameter.default is inspect.Parameter.empty
            and parameter.kind
            in {
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
                inspect.Parameter.KEYWORD_ONLY,
            }
        ]
        if required:
            unsupported.append(f"{name}(requires={required})")
            continue
        out.append(
            unittest.FunctionTestCase(
                value,
                description=f"{rel}::{name}",
            )
        )
    if unsupported:
        raise TestDiscoveryContractError(
            f"{rel}: pytest-style test(s) require unsupported fixture/async semantics: "
            + ", ".join(unsupported)
            + "; convert those tests to unittest.TestCase or provide an explicit supported adapter"
        )
    return out


def load_file_suite(path: Path, loader: unittest.TestLoader | None = None) -> unittest.TestSuite:
    loader = loader or unittest.TestLoader()
    module = load_test_module(path)
    rel = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(module))
    suite.addTests(top_level_function_tests(module, rel))
    return suite


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
        rel = path.relative_to(ROOT).as_posix()
        discovered = load_file_suite(path, loader)
        case_count = discovered.countTestCases()
        counts[rel] = case_count
        if case_count == 0:
            zero_case_files.append(rel)
            continue
        suite.addTests(discovered)

    if zero_case_files:
        joined = ", ".join(zero_case_files)
        raise TestDiscoveryContractError(
            "test discovery contract violation: tests/test*.py file(s) produced zero executable "
            "unittest or zero-argument top-level test cases: "
            + joined
            + "; add executable tests or remove/rename the file if it is not a test contract"
        )

    return suite, counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one deterministic Python test file shard")
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
    except TestDiscoveryContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        return 2

    for path, case_count in counts.items():
        print(f"UNITTEST_DISCOVERY {path} cases={case_count}", flush=True)

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
