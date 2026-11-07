#!/usr/bin/env python3
"""Run the existing Python validation contract locally; never publish GitHub status.

Python 3.12 and the repository's existing test/validation dependencies are required.
The JSON contract is intentionally pinned to exact workflow bytes. Workflow edits
require reviewing/regenerating it; a stale contract must not silently skip checks.
This runner does not replace Lean, deployment, research, or other specialized gates.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time

QUALITY_COMMAND = "python scripts/run_unittest_shard.py --index 0 --count 1"
STAGES = ("quality", "reference-integrity", "bilingual")
EXCLUDED_DIRS = {".git", ".local", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".lake"}


class ContractError(ValueError):
    """A missing or stale source contract blocks execution."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_source(root: Path, relative: str) -> bytes:
    path = root / relative
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ContractError(f"source path must be repository-relative: {relative}")
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ContractError(f"source path escapes repository or is a symlink: {relative}")
    try:
        return path.read_bytes()
    except OSError as exc:
        raise ContractError(f"missing/unreadable source: {relative}: {exc}") from exc


def workflow_commands(source: str) -> list[str]:
    """Read this pinned workflow's simple run scalars without a YAML dependency.

    Exact workflow hashing makes this a deliberately narrow reader, not a general
    YAML parser. Independent development validation compares it with a YAML parser.
    """
    lines = source.splitlines()
    commands: list[str] = []
    i = 0
    while i < len(lines):
        match = re.match(r"^(\s+)(?:- )?run: (.*)$", lines[i])
        if not match:
            i += 1
            continue
        indent, value = len(match[1]), match[2]
        if value in {"|", "|-", ">", ">-"}:
            block: list[str] = []
            i += 1
            while i < len(lines):
                line = lines[i]
                if line.strip() and len(line) - len(line.lstrip()) <= indent:
                    break
                block.append(line)
                i += 1
            nonempty = [line for line in block if line.strip()]
            if not nonempty:
                raise ContractError("empty workflow run block")
            width = min(len(line) - len(line.lstrip()) for line in nonempty)
            block = [line[width:] if line.strip() else "" for line in block]
            while block and not block[-1]:
                block.pop()
            command = " ".join(block) if value.startswith(">") else "\n".join(block)
        else:
            if not value or value.startswith(("'", '"', "&", "*", "${{")):
                raise ContractError("unsupported run scalar in pinned workflow")
            command = value
            i += 1
        commands.append(command.strip())
    return commands


def load_contract(root: Path, manifest: Path) -> dict:
    try:
        contract = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ContractError(f"missing/malformed validation manifest: {exc}") from exc
    if not isinstance(contract, dict) or contract.get("schema_version") != 1:
        raise ContractError("unsupported validation manifest schema")
    try:
        workflows = contract["workflows"]
        expected_paths = {
            ".github/workflows/quality.yml",
            ".github/workflows/reference-integrity.yml",
            ".github/workflows/bilingual-sync.yml",
        }
        if set(workflows) != expected_paths:
            raise ContractError("workflow contract must cover all three source workflows")
        for relative, expected in workflows.items():
            data = read_source(root, relative)
            if digest(data) != expected["sha256"]:
                raise ContractError(f"workflow contract changed: {relative}")
            actual = workflow_commands(data.decode("utf-8"))
            if actual != expected["run_commands"]:
                raise ContractError(f"workflow command parity failed: {relative}")
        quality = workflows[".github/workflows/quality.yml"]["run_commands"]
        if "python scripts/run_unittest_shard.py --index ${{ matrix.shard }} --count 8" not in quality:
            raise ContractError("quality no longer uses the mixed test runner")
        if "python tests/test_p017_mirror_cross.py" not in quality:
            raise ContractError("quality's isolated P017 coverage changed")
        reference = workflows[".github/workflows/reference-integrity.yml"]["run_commands"]
        if not reference or any(shlex.split(command)[0] != "python" for command in reference):
            raise ContractError("reference contract contains unsupported non-Python commands")
        bilingual = workflows[".github/workflows/bilingual-sync.yml"]["run_commands"]
        if bilingual[-1] != 'python tools/check_bilingual_pairs.py --base "$BASE_SHA"':
            raise ContractError("bilingual command contract changed")
    except (KeyError, TypeError, IndexError, UnicodeError, ValueError) as exc:
        if isinstance(exc, ContractError):
            raise
        raise ContractError(f"malformed workflow command contract: {exc}") from exc
    return contract


def git_output(root: Path, *args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=root, text=True, stderr=subprocess.PIPE).strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ContractError(f"local git provenance unavailable: {' '.join(args)}") from exc


def bilingual_provenance(root: Path, mode: str | None, base: str | None) -> dict:
    if mode == "full-snapshot":
        if base is not None:
            raise ContractError("full-snapshot cannot also provide a comparison base")
        return {"mode": mode, "same_change_pairing_verified": False, "base": None}
    if mode != "base" or not base:
        raise ContractError("bilingual requires --base or explicit --full-snapshot")
    if not re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", base) or set(base) == {"0"}:
        raise ContractError("bilingual base must be a nonzero full commit SHA")
    if Path(git_output(root, "rev-parse", "--show-toplevel")).resolve() != root.resolve():
        raise ContractError("bilingual comparison requires the exact repository root")
    resolved = git_output(root, "rev-parse", "--verify", f"{base}^{{commit}}")
    head = git_output(root, "rev-parse", "--verify", "HEAD^{commit}")
    if git_output(root, "status", "--porcelain", "--untracked-files=all"):
        raise ContractError("same-change bilingual validation requires a clean committed candidate; use explicit full-snapshot for an uncommitted tree")
    merge_base = git_output(root, "merge-base", resolved, head)
    return {"mode": mode, "base": resolved, "head": head, "merge_base": merge_base, "same_change_pairing_verified": False}


def quality_source_provenance(root: Path) -> dict:
    """Reject sparse connector materializations and missing tracked source files.

    This establishes completeness relative to a local Git HEAD tree, not remote
    authenticity. The receipt separately records the exact local working bytes.
    """
    if Path(git_output(root, "rev-parse", "--show-toplevel")).resolve() != root.resolve():
        raise ContractError("quality requires a complete checkout at the exact repository root")
    head = git_output(root, "rev-parse", "--verify", "HEAD^{commit}")
    try:
        sparse = git_output(root, "config", "--bool", "core.sparseCheckout")
    except ContractError:
        sparse = "false"
    index = git_output(root, "ls-files", "-t", "-z").split("\0")
    if sparse == "true" or any(row and row[0].upper() == "S" for row in index):
        raise ContractError("quality cannot claim full coverage from a sparse/skip-worktree checkout")
    files = sorted(filter(None, git_output(root, "ls-tree", "-r", "--name-only", "-z", "HEAD").split("\0")))
    if not {"scripts/run_unittest_shard.py", "tests/test_p017_mirror_cross.py"}.issubset(files):
        raise ContractError("quality HEAD inventory lacks the existing mixed runner or P017 tests")
    for relative in files:
        read_source(root, relative)
    inventory = digest(json.dumps(files, separators=(",", ":")).encode())
    return {"local_head": head, "tracked_file_count": len(files), "tracked_path_inventory_sha256": inventory, "all_head_files_materialized": True, "remote_commit_verified": False, "quality_execution": "same supported test-file coverage in one process; not identical eight-shard process isolation or ordering"}


def source_snapshot(root: Path) -> dict:
    files: dict[str, str] = {}
    for directory, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_DIRS and not (Path(directory) / d).is_symlink())
        for name in sorted(names):
            path = Path(directory) / name
            if path.suffix in {".pyc", ".pyo"} or path.is_symlink():
                continue
            relative = path.relative_to(root).as_posix()
            files[relative] = digest(read_source(root, relative))
    encoded = json.dumps(files, sort_keys=True, separators=(",", ":")).encode()
    return {"sha256": digest(encoded), "files": files, "excluded_directory_names": sorted(EXCLUDED_DIRS), "scope": "local regular files; excludes runtime/cache directories and symlinks; not a verified remote commit"}


def plan_commands(contract: dict, stages: list[str], bilingual: dict | None) -> list[dict]:
    commands = []
    if "quality" in stages:
        commands.append({"stage": "quality", "command": QUALITY_COMMAND, "env": {"PYTHONPATH": "src"}})
    if "reference-integrity" in stages:
        for command in contract["workflows"][".github/workflows/reference-integrity.yml"]["run_commands"]:
            commands.append({"stage": "reference-integrity", "command": command, "env": {}})
    if "bilingual" in stages:
        base = bilingual["base"] if bilingual else None
        commands.append({"stage": "bilingual", "command": "python tools/check_bilingual_pairs.py --base " + shlex.quote(base or ""), "env": {}})
    for row in commands:
        tokens = shlex.split(row["command"])
        if not tokens or tokens[0] != "python":
            raise ContractError("only pinned Python commands can execute")
        row["argv"] = [sys.executable, *tokens[1:]]
    return commands


def execute_plan(root: Path, output: Path, plan: list[dict], timeout: int, execute=None) -> list[dict]:
    execute = execute or subprocess.run
    results = []
    failed_stages: set[str] = set()
    for index, command in enumerate(plan):
        row = dict(command)
        row["log"] = f"{index + 1:03d}-{row['stage']}.log"
        if row["stage"] in failed_stages:
            row.update(status="NOT_RUN_DEPENDENCY_FAILED", exit_code=None, duration_seconds=0)
            results.append(row)
            continue
        started = time.monotonic()
        env = os.environ.copy()
        env.update(row["env"])
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        with (output / row["log"]).open("wb") as log:
            try:
                result = execute(row["argv"], cwd=root, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=timeout, check=False)
                row.update(status="PASS" if result.returncode == 0 else "FAIL", exit_code=result.returncode)
            except subprocess.TimeoutExpired:
                row.update(status="TIMEOUT", exit_code=None)
                log.write(b"\nConversation runner: command timeout; validation did not pass.\n")
            except OSError as exc:
                row.update(status="EXECUTION_ERROR", exit_code=None)
                log.write(f"\nConversation runner: {exc}\n".encode())
        row["duration_seconds"] = round(time.monotonic() - started, 3)
        row["log_sha256"] = digest((output / row["log"]).read_bytes())
        results.append(row)
        if row["status"] != "PASS":
            failed_stages.add(row["stage"])
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="New evidence directory OUTSIDE the source repository")
    parser.add_argument("--stages", nargs="+", choices=STAGES, default=list(STAGES))
    parser.add_argument("--reference-step", type=int, action="append", help="Run only specified 1-based reference command(s); explicitly records partial coverage")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--base", help="Full existing commit SHA; requires a clean committed candidate")
    mode.add_argument("--full-snapshot", action="store_true", help="Explicitly omit bilingual same-change pairing, retaining full structural validation")
    parser.add_argument("--timeout-seconds", type=int, default=3600, help="Per-command ceiling; timeout is a failure, never a pass")
    args = parser.parse_args(argv)
    root, output = args.repo.resolve(), args.output.resolve()
    if output == root or output.is_relative_to(root):
        parser.error("evidence output must be outside the source repository")
    if output.exists():
        parser.error("evidence directory already exists; use a fresh path")
    output.mkdir(parents=True)
    receipt = {"schema_version": 1, "started_at": datetime.now(timezone.utc).isoformat(), "python": sys.version, "python_executable": sys.executable, "source_root": str(root), "stages": args.stages, "github_checks_updated": False, "coverage": "selected Python gates only; does not establish Lean, specialized workflows, mathematical review, merge or deployment approval", "results": []}
    code = 2
    try:
        if sys.version_info[:2] != (3, 12):
            raise ContractError("Python 3.12 is required to match the existing workflows")
        if not root.is_dir() or args.timeout_seconds < 1:
            raise ContractError("repository must exist and timeout must be positive")
        manifest = args.manifest or root / "scripts/conversation_validation_contract.json"
        contract = load_contract(root, manifest)
        receipt["manifest_sha256"] = digest(manifest.read_bytes())
        receipt["workflow_sha256"] = {path: row["sha256"] for path, row in contract["workflows"].items()}
        if "quality" in args.stages:
            receipt["quality_source_inventory"] = quality_source_provenance(root)
        bilingual = None
        if "bilingual" in args.stages:
            selected_mode = "base" if args.base is not None else "full-snapshot" if args.full_snapshot else None
            bilingual = bilingual_provenance(root, selected_mode, args.base)
            receipt["bilingual"] = bilingual
        plan = plan_commands(contract, args.stages, bilingual)
        if args.reference_step:
            if args.stages != ["reference-integrity"]:
                raise ContractError("--reference-step requires --stages reference-integrity only")
            reference_count = len(plan)
            if any(index < 1 or index > reference_count for index in args.reference_step):
                raise ContractError(f"reference step must be between 1 and {reference_count}")
            selected = set(args.reference_step)
            plan = [dict(row, reference_step=index) for index, row in enumerate(plan, 1) if index in selected]
            receipt["reference_subset"] = sorted(selected)
            receipt["coverage"] = "explicit reference-command subset only; does not establish complete reference integrity, quality, bilingual or any GitHub check"
        receipt["planned_commands"] = plan
        required = {row["argv"][1] for row in plan if row["argv"][1] != "-c"}
        if "quality" in args.stages:
            required.add("tests/test_p017_mirror_cross.py")
        for relative in required:
            read_source(root, relative)
        receipt["source_before"] = source_snapshot(root)
        try:
            if Path(git_output(root, "rev-parse", "--show-toplevel")).resolve() != root:
                raise ContractError("ancestor Git repository is not the selected source root")
            receipt["local_git_head"] = git_output(root, "rev-parse", "HEAD")
        except ContractError:
            receipt["local_git_head"] = None
        receipt["results"] = execute_plan(root, output, plan, args.timeout_seconds)
        receipt["source_after"] = source_snapshot(root)
        receipt["source_unchanged"] = receipt["source_before"]["sha256"] == receipt["source_after"]["sha256"]
        passed = all(row["status"] == "PASS" for row in receipt["results"]) and receipt["source_unchanged"]
        if bilingual and bilingual["mode"] == "base":
            bilingual["same_change_pairing_verified"] = any(row["stage"] == "bilingual" and row["status"] == "PASS" for row in receipt["results"]) and receipt["source_unchanged"]
        receipt["status"] = "LOCAL_SELECTED_SCOPE_PASS" if passed else "FAIL"
        code = 0 if passed else 1
    except (ContractError, OSError) as exc:
        receipt.update(status="BLOCKED", error=str(exc))
    except KeyboardInterrupt:
        receipt.update(status="INTERRUPTED", error="User interrupted local validation; no pass established")
        code = 130
    finally:
        receipt["completed_at"] = datetime.now(timezone.utc).isoformat()
        (output / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "receipt": str(output / "receipt.json"), "github_checks_updated": False}))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
