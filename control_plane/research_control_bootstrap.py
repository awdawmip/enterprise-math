#!/usr/bin/env python3
"""Canonical control-plane bootstrap for resilient task-view construction.

Order is intentional:
1. isolate unresolved immutable publication forks without selecting a head;
2. isolate exact pinned current task-integrity faults;
3. leave every unrelated task under the original strict publication/dispatch rules.

This bootstrap grants no research or publication authority.
"""
from __future__ import annotations

from pathlib import Path

from control_plane import research_publication_fault_isolation
from control_plane import research_task_integrity_fault_isolation

ROOT = Path(__file__).resolve().parents[1]


def install(root: Path = ROOT) -> None:
    research_publication_fault_isolation.install(root)
    research_task_integrity_fault_isolation.install(root)


if __name__ == "__main__":
    install()
    print("PASS: canonical control-plane task-view bootstrap installed.")
