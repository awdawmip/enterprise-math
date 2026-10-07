#!/usr/bin/env python3
"""Run one deterministic shard of the repository Python test suite.

The repository historically contains both ``unittest.TestCase`` tests and
pytest-style top-level ``def test_*`` functions.  The old shard runner used only
``unittest`` discovery, which meant top-level functions could appear in shard
listings while never executing.  Silent skips are forbidden.

This runner classifies files before importing them. Ordinary unittest cases and
zero-argument functions retain their unittest adapter. Files requiring pytest
semantics run together, once per shard, in an isolated pytest worker which also
installs the canonical bootstrap before collection. Collection errors and empty
test files fail closed; explicit skips remain visible in the test report.

Control-plane tests exercise the same fault-isolated operational view used by
live dispatch. Strict/raw validators remain separately callable from the
reference-integrity workflow.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import inspect
import os
import subprocess
import sys
import tokenize
import unittest
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = ROOT / "tests"
SOURCE_ROOT = ROOT / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(TEST_ROOT) not in sys.path:
    sys.path.insert(0, str(TEST_ROOT))
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from control_plane import research_control_bootstrap  # noqa: E402


class TestDiscoveryContractError(RuntimeError):
    pass


def requires_pytest(path: Path) -> bool:
    """Classify without importing, so a mixed module is never executed twice."""
    try:
        with tokenize.open(path) as handle:
            tree = ast.parse(handle.read(), filename=str(path))
    except (OSError, SyntaxError, UnicodeError) as exc:
        raise TestDiscoveryContractError(f"cannot inspect {path}: {exc}") from exc
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) and any(alias.name.split('.')[0] == 'pytest' for alias in node.names):
            return True
        if isinstance(node, ast.ImportFrom) and (node.module or '').split('.')[0] == 'pytest':
            return True
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id in {'pytestmark', 'pytest_plugins'} for target in targets):
                return True
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in {'setup_module', 'teardown_module', 'setup_function', 'teardown_function'}:
                return True
            if node.name.startswith('test_'):
                args = node.args
                required = (len(args.posonlyargs) + len(args.args) > len(args.defaults)
                            or any(default is None for default in args.kw_defaults))
                if required or node.decorator_list or isinstance(node, ast.AsyncFunctionDef):
                    return True
        if isinstance(node, ast.ClassDef) and node.name.startswith('Test'):
            # An unbased test class uses pytest collection, unlike TestCase.
            if not node.bases and any(isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                                      and item.name.startswith('test_') for item in node.body):
                return True
    return False


def partition_files(files: list[Path]) -> tuple[list[Path], list[Path]]:
    ordinary, pytest_files = [], []
    for path in files:
        (pytest_files if requires_pytest(path) else ordinary).append(path)
    return ordinary, pytest_files


def run_pytest_worker(files: list[Path]) -> int:
    """Use real fixture/parametrize/skip semantics after the live-view bootstrap."""
    research_control_bootstrap.install(ROOT)
    try:
        import pytest
    except ImportError as exc:
        raise TestDiscoveryContractError('pytest is required; install the pinned CI test dependencies') from exc

    class DiscoveryReport:
        def __init__(self):
            self.counts = {path.resolve(): 0 for path in files}
            self.skipped = set()
            self.deselected = 0

        def pytest_collectreport(self, report):
            if report.skipped:
                location = report.nodeid.split('::')[0]
                if not location and isinstance(report.longrepr, tuple):
                    location = report.longrepr[0]
                if location:
                    self.skipped.add((ROOT / location).resolve())

        def pytest_deselected(self, items):
            self.deselected += len(items)

        def pytest_collection_finish(self, session):
            for item in session.items:
                path = Path(item.path).resolve()
                if path in self.counts:
                    self.counts[path] += 1
            for path, count in self.counts.items():
                rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
                print(f'PYTEST_DISCOVERY {rel} cases={count} collection_skipped={int(path in self.skipped)}', flush=True)

    report = DiscoveryReport()
    code = int(pytest.main(['--rootdir', str(ROOT), '--import-mode=importlib', '-v', '-ra',
                           *[str(path.resolve()) for path in files]], plugins=[report]))
    empty = [str(path) for path, count in report.counts.items() if not count and path not in report.skipped]
    if empty or report.deselected:
        print(f'ERROR: pytest discovery contract: zero-case files={empty}; deselected={report.deselected}',
              file=sys.stderr, flush=True)
        return 2
    # Pytest uses NO_TESTS_COLLECTED for a module-level explicit import skip.
    if code == int(pytest.ExitCode.NO_TESTS_COLLECTED) and len(report.skipped) == len(files):
        return 0
    return code


def run_pytest_files(files: list[Path]) -> int:
    if not files:
        return 0
    env = dict(os.environ)
    env['PYTEST_DISABLE_PLUGIN_AUTOLOAD'] = '1'
    # A developer's implicit -k/-m/--deselect options must not shrink a CI shard.
    env.pop('PYTEST_ADDOPTS', None)
    return subprocess.run([sys.executable, str(Path(__file__).resolve()), '--pytest-files',
                           *[str(path.resolve()) for path in files]], env=env, cwd=ROOT).returncode


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


def build_suite(index: int, count: int, *, files: list[Path] | None = None) -> tuple[unittest.TestSuite, dict[str, int]]:
    # Install once before importing any test module. This is deliberately the
    # operational view, not an audit waiver: exact quarantines are validated by
    # the bootstrap and strict/raw integrity checks run in their own CI gates.
    research_control_bootstrap.install(ROOT)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    counts: dict[str, int] = {}
    zero_case_files: list[str] = []

    for path in shard_files(index, count) if files is None else files:
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
    parser.add_argument("--index", type=int)
    parser.add_argument("--count", type=int)
    parser.add_argument("--pytest-files", type=Path, nargs='+', help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.pytest_files:
        try:
            return run_pytest_worker(args.pytest_files)
        except TestDiscoveryContractError as exc:
            print(f'ERROR: {exc}', file=sys.stderr, flush=True)
            return 2
    if args.index is None or args.count is None:
        parser.error('--index and --count are required')

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
        ordinary_files, pytest_files = partition_files(files)
        suite, counts = build_suite(args.index, args.count, files=ordinary_files)
    except TestDiscoveryContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        return 2

    for path, case_count in counts.items():
        print(f"UNITTEST_DISCOVERY {path} cases={case_count}", flush=True)

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    pytest_code = run_pytest_files(pytest_files)
    return 0 if result.wasSuccessful() and pytest_code == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
