#!/usr/bin/env python3
"""Evidence-only CLI for the lineage-forward publication quarantine primitive."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_publication_quarantine_lineage as lineage

LineageForwardSafetyError = lineage.LineageForwardSafetyError
prove = lineage.prove


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--anchor", action="append", required=True)
    args = parser.parse_args()
    try:
        evidence = prove(args.task_id, args.anchor)
    except (LineageForwardSafetyError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    payload = {
        "status": "SAFE_LINEAR_DESCENDANT_FORWARD_EVIDENCE_ONLY",
        **evidence,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    print("PASS: anchored publication fork advances only through unique linear descendants.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
