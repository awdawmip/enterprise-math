# Stage488-B exact evidence package

The full standard-library Python reproduction is `REPRO_STAGE488B.py`; it writes `STAGE488B_EXECUTED.json` alongside itself when run. Its source blob `78666e30bc25074d98b17d8eceff755962bfa6fc` matches the locally executed portable source.

The fully executed result JSON (26,069 UTF-8 bytes, SHA256 `0aab2019ec56ac6dc904bdf4a047ec27d2bc26022c1370cc84254e098716282a`) is stored losslessly in `STAGE488B_EXECUTED_JSON_GZIP_BASE64.txt`, which contains gzip-compressed, base64-encoded JSON with deterministic gzip mtime=0. The Git blob of this encoded text is `e7cea722d628d5f8e82477a261c321481768fb31`.

Decoding offline with Python standard library:

```python
import base64, gzip, hashlib
from pathlib import Path
encoded=Path("STAGE488B_EXECUTED_JSON_GZIP_BASE64.txt").read_text().strip()
raw=gzip.decompress(base64.b64decode(encoded))
assert len(raw)==26069
assert hashlib.sha256(raw).hexdigest()=="0aab2019ec56ac6dc904bdf4a047ec27d2bc26022c1370cc84254e098716282a"
Path("STAGE488B_EXECUTED_DECODED.json").write_bytes(raw)
```

The separate `REPRO_STAGE488B_EXECUTED_STDOUT.txt` captures actual PASS output for all 20 configurations and the edit witness. `STAGE488B_SUMMARY.json` includes exact integer results and measurement summary. The executed JSON contains per-case wall-clock and tracemalloc peak samples from one run; `STAGE488B_SUMMARY.json` also reports the seven-repeat medians for the growing case. These timing measurements are environment-specific.

Status: author-side mathematical result with independent review and native admission pending. The Stage486-B future-equivalence-key assumption remains distinct from the sparse/dense algorithmic equivalence proven here.
