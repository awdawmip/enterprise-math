#!/usr/bin/env python3
"""Lossless launcher for the validated event-17 checker source."""
from pathlib import Path
import hashlib

HERE = Path(__file__).resolve().parent
PARTS = [HERE / f"check_reference.part{i}.pyfrag" for i in (1, 2, 3)]
EXPECTED = "5f7beef516f4d4d40b2d5f73322bc8737d726c72a266b5960460275daf412d5f"
source = "".join(p.read_text(encoding="utf-8") for p in PARTS)
if hashlib.sha256(source.encode("utf-8")).hexdigest() != EXPECTED:
    raise RuntimeError("Event-17 checker fragments do not reconstruct the validated source.")
exec(compile(source, str(HERE / "assembled_check_reference.py"), "exec"),
     {"__name__": "__main__", "__file__": str(HERE / "check_reference.py")})
