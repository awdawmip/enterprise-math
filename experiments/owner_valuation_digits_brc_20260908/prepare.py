"""Capture the fixed source and prepare one TEMP-only digits migration."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import subprocess
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-ref", required=True)
    args = parser.parse_args()
    out = Path(__file__).resolve().parent
    if out.joinpath("inputs.json").exists():
        raise SystemExit("refusing to overwrite an existing captured package")

    def git(*argv: str) -> bytes:
        return subprocess.check_output(["git", "-C", str(args.repo), *argv])

    target = "research_notes/owner_arithmetic_20260907.py"
    runtime = [f"src/enterprise_math/{name}.py" for name in ("exact_arithmetic", "division", "core")]
    paths = [target, *runtime, "exact_arithmetic_runtime_policy.json",
             "research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json",
             "src/enterprise_math/brc_histogram.py", "src/enterprise_math/legendre.py"]
    captured = {}
    worktree_before = {}
    for path in paths:
        data = git("show", f"{args.source_ref}:{path}")
        destination = out.joinpath("frozen", path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        captured[path] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                          "blob": git("rev-parse", f"{args.source_ref}:{path}").decode().strip()}
        local = args.repo.joinpath(path)
        worktree_before[path] = hashlib.sha256(local.read_bytes()).hexdigest() if local.is_file() else None

    original = out.joinpath("frozen", target).read_bytes()
    assert hashlib.sha256(original).hexdigest() == "71f0214cc414c9d1291facd3ec8a727989fafe1bc21e0db5001b7d5e5655a79d"
    old = b"""def digits_lsd(n: int, p: int) -> tuple[int, ...]:
    digits = []
    while n:
        n, digit = divmod(n, p)
        digits.append(digit)
    return tuple(digits or [0])
"""
    new = b"""def digits_lsd(
    n: int,
    p: int,
    *,
    arithmetic_trace: list[BRCDivisionTrace] | None = None,
) -> tuple[int, ...]:
    \"\"\"Return low-first digits; optionally retain each local BRC DIV trace.\"\"\"
    n = _integer(\"n\", n, 0)
    p = _integer(\"p\", p, 2)
    digits = []
    while n:
        trace = brc_evaluate_division(division(n, p))
        if arithmetic_trace is not None:
            arithmetic_trace.append(trace)
        n, digit = trace.quotient, trace.remainder
        digits.append(digit)
    return tuple(digits or [0])
"""
    import_line = b"from enterprise_math.legendre import is_prime\n"
    addition = b"from enterprise_math.exact_arithmetic import (\n    BRCDivisionTrace,\n    brc_evaluate_division,\n    division,\n)\n"
    assert original.count(old) == original.count(import_line) == 1
    candidate = original.replace(import_line, addition + import_line).replace(old, new)
    out.joinpath("owner_arithmetic_20260907.candidate.py").write_bytes(candidate)
    patch = "".join(difflib.unified_diff(original.decode().splitlines(keepends=True),
                                      candidate.decode().splitlines(keepends=True),
                                      fromfile="a/" + target, tofile="b/" + target))
    out.joinpath("digits_lsd_brc.patch").write_text(patch, encoding="utf-8", newline="\n")
    metadata = {
        "scope": "TEMP_ONLY_INTERNAL_DIGITS_MIGRATION_NOT_WHOLE_TOOL_COMPLIANCE",
        "published_source": "909ed4c3c81adca8d5d653994a83df316faf1365",
        "actual_local_source": args.source_ref,
        "actual_local_tree": git("rev-parse", f"{args.source_ref}^{{tree}}").decode().strip(),
        "published_local_tree_equivalence": "Parent exact publication receipt; this script reads the recorded local immutable object.",
        "captured": captured,
        "candidate_sha256": hashlib.sha256(candidate).hexdigest(),
        "patch_sha256": hashlib.sha256(patch.encode()).hexdigest(),
        "candidate_bytes": len(candidate),
        "source_worktree": str(args.repo.resolve()),
        "source_worktree_before": worktree_before,
    }
    out.joinpath("inputs.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"prepared": str(out), "candidate_sha256": metadata["candidate_sha256"],
                      "patch_sha256": metadata["patch_sha256"], "captured_files": len(captured)}))


if __name__ == "__main__":
    main()
