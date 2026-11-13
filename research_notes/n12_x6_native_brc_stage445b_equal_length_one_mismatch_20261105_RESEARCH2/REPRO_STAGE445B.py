#!/usr/bin/env python3
"""Run the complete preserved Stage445-B Python3 reproduction with no dependencies."""
import gzip
from pathlib import Path
p = Path(__file__).with_name("STAGE445B_FULL_REPRO.py.gz")
exec(compile(gzip.decompress(p.read_bytes()), "STAGE445B_FULL_REPRO.py", "exec"), {"__name__":"__main__"})
