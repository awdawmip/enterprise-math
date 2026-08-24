#!/usr/bin/env python3
"""Compatibility entrypoint for the canonical Scheduler V2 implementation."""

try:
    from .research_scheduler_v2 import *  # noqa: F401,F403
    from .research_scheduler_v2 import main
except ImportError:  # direct `python tools/research_scheduler.py ...`
    from research_scheduler_v2 import *  # type: ignore # noqa: F401,F403
    from research_scheduler_v2 import main  # type: ignore


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SchedulerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
