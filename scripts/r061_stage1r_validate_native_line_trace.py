#!/usr/bin/env python3
from pathlib import Path

_THIS = Path(__file__).resolve()
_PARTS = _THIS.with_name("r061_stage1r_checker_parts")
_SOURCE = "".join(
    (_PARTS / f"part{i:02d}.inc").read_text(encoding="utf-8")
    for i in range(4)
)
_NS = {"__name__": "__main__", "__file__": str(_THIS)}
exec(compile(_SOURCE, str(_THIS), "exec"), _NS, _NS)
