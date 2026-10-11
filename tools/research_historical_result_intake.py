#!/usr/bin/env python3
"""Canonical candidate writer; authority context is supplied by native guard."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from control_plane import research_historical_result_intake as impl


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("intake", "review", "audit", "state"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--spec")
    parser.add_argument("--authority-context")
    parser.add_argument("--source-commit")
    parser.add_argument("--task-id")
    parser.add_argument("--publication-id")
    args = parser.parse_args()
    try:
        if args.operation == "audit":
            value = impl.audit(args.root)
        elif args.operation == "state":
            value = impl.task_state(args.task_id, args.publication_id, root=args.root)
        else:
            context = json.loads(Path(args.authority_context).read_text())
            impl._require(context["source_commit"] == args.source_commit, "CLI Source snapshot binding mismatch")
            value = (impl.freeze_intake if args.operation == "intake" else impl.freeze_review)(
                json.loads(Path(args.spec).read_text()), context, root=args.root)
        print(json.dumps(value, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
