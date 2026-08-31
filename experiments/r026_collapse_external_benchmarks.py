"""R026 external benchmark runner.

The researched implementation is stored as deterministic gzip+base64 text chunks
under ``experiments/r026_payload`` for connector-only publication.  The loader
reconstructs the exact frozen source bytes and executes them as this module.
"""
from pathlib import Path as _Path
import base64 as _base64
import gzip as _gzip
_payload_dir = _Path(__file__).with_name("r026_payload")
_b64 = "".join(p.read_text(encoding="ascii") for p in sorted(_payload_dir.glob("source.py.gz.b64part*")))
_source = _gzip.decompress(_base64.b64decode(_b64)).decode("utf-8")
exec(compile(_source, str(_Path(__file__).resolve()), "exec"), globals(), globals())
