#!/usr/bin/env python3
"""Canonical parallel-evidence CLI over the operational result/review view.

Importing ``tools.research_result_records`` first composes immutable-history
compatibility, control-only result replacement, review exact-set authority and the
parallel reducer in one process. The root ``research_parallel_evidence`` module
then executes unchanged semantics over that injected operational view.
"""
from __future__ import annotations

from tools import research_result_records as _result_view  # noqa: F401,E402
import research_parallel_evidence as _parallel  # noqa: E402


if __name__ == "__main__":
    try:
        raise SystemExit(_parallel.main())
    except _parallel.ParallelEvidenceError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
