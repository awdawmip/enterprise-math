#!/usr/bin/env python3
"""Single mandatory dispatch gate for Enterprise Math research taskbooks."""
from __future__ import annotations

import argparse
from pathlib import Path

import tools.research_execution_state as execution
import tools.research_taskbook as taskbook

ROOT = Path(__file__).resolve().parents[1]


def machine_findings() -> list[dict[str, str]]:
    return [
        {"severity": "ERROR", "code": "EX-MACHINE", "message": message}
        for message in execution.validate_machine(execution.load_machine(ROOT))
    ]


def audit_one(path: Path) -> list[dict[str, str]]:
    # research_taskbook.audit_taskbook(..., dispatch=True) already composes the
    # taskbook-policy audit with the execution-gate/taskbook audit. Keep this
    # wrapper as the single user-facing dispatch command and add a structural
    # validation of the machine itself without duplicating findings.
    findings = machine_findings()
    findings.extend(taskbook.audit_taskbook(path, root=ROOT, dispatch=True))
    return findings


def command_audit(args: argparse.Namespace) -> int:
    if args.all:
        paths = sorted((ROOT / "research_tasks").glob("*.md"))
    else:
        paths = [Path(item) if Path(item).is_absolute() else ROOT / item for item in args.paths]
    if not paths:
        raise SystemExit("no taskbooks selected")

    errors = 0
    for path in paths:
        findings = audit_one(path)
        display = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        if not findings:
            print(f"{display}: PASS")
            continue
        for item in findings:
            print(f"{display}: {item['severity']} {item['code']}: {item['message']}")
            errors += item["severity"] == "ERROR"
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    audit = sub.add_parser("audit")
    audit.add_argument("paths", nargs="*")
    audit.add_argument("--all", action="store_true")
    audit.set_defaults(func=command_audit)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
