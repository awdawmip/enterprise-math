"""Replay the unchanged archived review in a new, isolated output directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    package = Path(__file__).resolve().parent
    manifest = json.loads(package.joinpath("package_manifest.json").read_text(encoding="utf-8"))
    for relative, pin in manifest["archived_files"].items():
        assert digest(package.joinpath(relative).read_bytes()) == pin["sha256"], relative
    if args.output_dir:
        output = args.output_dir.resolve()
        assert not output.is_relative_to(package), "replay output must be outside the source package"
        output.mkdir(parents=True, exist_ok=False)
    else:
        output = Path(tempfile.mkdtemp(prefix="owner-valuation-digits-brc-replay-"))
    assert not output.is_relative_to(package), "replay output must be outside the source package"
    for relative in ("review.py", "owner_arithmetic_20260907.candidate.py"):
        shutil.copyfile(package.joinpath(relative), output.joinpath(relative))
    shutil.copytree(package.joinpath("frozen"), output.joinpath("frozen"))
    original_inputs = package.joinpath("inputs.json").read_bytes()
    inputs = json.loads(original_inputs)
    old_location = inputs["source_worktree"]
    inputs["source_worktree"] = str(output.joinpath("frozen"))
    # In the original run these eight worktree hashes equal the captured source.
    assert inputs["source_worktree_before"] == {
        path: pin["sha256"] for path, pin in inputs["captured"].items()
    }, "the archived run did not use the same fixed source bytes"
    execution_inputs = (json.dumps(inputs, indent=2) + "\n").encode()
    output.joinpath("inputs.json").write_bytes(execution_inputs)
    argv = [sys.executable, "-B", "-X", "utf8", str(output.joinpath("review.py"))]
    process = subprocess.run(argv, cwd=output, capture_output=True, check=False)
    output.joinpath("stdout.log").write_bytes(process.stdout)
    output.joinpath("stderr.log").write_bytes(process.stderr)
    receipt = {
        "schema": "OWNER_VALUATION_DIGITS_ARCHIVED_REPLAY_V1",
        "status": "PASS" if process.returncode == 0 else "FAIL",
        "argv": argv, "exit_code": process.returncode,
        "executed_replay_entry_sha256": digest(Path(__file__).read_bytes()),
        "archived_review_script_sha256": digest(package.joinpath("review.py").read_bytes()),
        "executed_review_script_sha256": digest(output.joinpath("review.py").read_bytes()),
        "archived_review_receipt_sha256": digest(package.joinpath("review.json").read_bytes()),
        "archived_inputs_sha256": digest(original_inputs),
        "execution_inputs_sha256": digest(execution_inputs),
        "execution_manifest_changed_fields": ["source_worktree"],
        "old_source_worktree": old_location,
        "new_source_worktree": inputs["source_worktree"],
        "boundary": "Only the original preservation-check location is rebound to its exact frozen eight-file snapshot. Mathematical cases, native dependencies, candidate, and review script are unchanged. This is a new run, not the historical receipt.",
        "stdout_sha256": digest(process.stdout), "stderr_sha256": digest(process.stderr),
    }
    if output.joinpath("review.json").is_file():
        receipt["new_review_receipt_sha256"] = digest(output.joinpath("review.json").read_bytes())
    output.joinpath("replay_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": receipt["status"], "output_dir": str(output),
                      "receipt_sha256": digest(output.joinpath("replay_receipt.json").read_bytes())}))
    return process.returncode


if __name__ == "__main__":
    raise SystemExit(main())
