#!/usr/bin/env python3
"""Executable loader for deterministic R063 Stage 1 checker parts."""
from pathlib import Path
_PART_DIR = Path(__file__).with_name("r063_stage1_checker_parts")
_PARTS = sorted(_PART_DIR.glob("part*.inc"))
if not _PARTS:
    raise RuntimeError("R063 Stage 1 checker parts are missing")
_SOURCE = "".join(p.read_text(encoding="utf-8") for p in _PARTS)
exec(compile(_SOURCE, str(_PARTS[0]), "exec"), globals(), globals())
