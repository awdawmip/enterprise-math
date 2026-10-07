# Reproduce the bounded U2 result

No network access or external Python package is needed during scientific execution. Python 3.10 or later suffices. This is a conditional positive-response circuit check, not native material dynamics.

1. Download this Result's sixteen files into one directory. Check their bytes against `MANIFEST.json`. The manifest lists every other file, not itself; the canonical checkpoint/readback supplies its own immutable blob.
2. Retrieve the seven original frozen files from the exact immutable URLs in `FETCH_MANIFEST.json`, using authenticated repository access. Put each in `source/<path>` as listed; in particular, the pinned kernel belongs at `source/sources/brc_weighted.py`. Copy `FETCH_MANIFEST.json` to `source/FETCH_MANIFEST.json` if using the original source-audit local layout. Git blob SHA1 is `sha1(b"blob "+ascii(len(bytes))+b"\0"+bytes)`; compare every file to its manifest value. No current-main substitution is allowed.
3. Preserve the published evidence directory. In a separate copy containing `incidence_check.py` and the `source/` tree, run `python incidence_check.py --full-evidence full.json`. It runs the actual pinned BRC packet/edge operations and emits compact `incidence_check.json`, lossless `incidence_trace.json.gz.b64`, and the optional uncompressed file. The expected result is 97 passed assertions, rows +1=4/3 and -1=1, and source-separated returns 1/144 and 5/768. A fresh measured wall time changes its artifact hash; it is not a change to the mathematical evidence.
4. Optional source regression: inside `source/`, run `python -B replay.py`. The unmodified original script gives 3329 assertions and the original four-layout diagnostics. This is old-source validation only, not a new four-material research result. Do not add 3329 and 97 and present their sum as a theorem count or independent reviews.

The packaged final checker was actually run once more in an isolated copy after adding lossless evidence export. The **entire** decompressed original and reproduced JSON objects were equal after removing only `resources.elapsed_seconds`. See `REPRODUCTION_CHECK.json`. This is same-context reproducibility verification, not independent replication. The published first-run bytes remain unchanged.

## Restore all original branch evidence

Run in the evidence directory:

```python
import base64, gzip, hashlib, json
from pathlib import Path
summary = json.loads(Path('incidence_check.json').read_text())
raw = gzip.decompress(base64.b64decode(Path('incidence_trace.json.gz.b64').read_bytes()))
assert len(raw) == summary['full_evidence_storage']['uncompressed_bytes']
assert hashlib.sha256(raw).hexdigest() == summary['full_evidence_storage']['uncompressed_sha256']
Path('incidence_original_full.json').write_bytes(raw)
```

The original uncompressed trace is 424947 bytes, SHA256 `741b47960228e7d997458abbe6622ee1f88fbd36a9f061aba7ad92fa136639fe`. It preserves all 24/90/1008 records at depths 0/1/2, including source identity, original input, packet labels, signed path and target Cell. Compression is a reversible storage encoding, not an observer quotient.

## Evidence roles

`INCIDENCE_REGULARITY.md` proves the finite all-hypergraph statement under its stated assumptions. The 97 assertions check one exact coherent hypergraph and its two-step execution, not every hypergraph. `SOURCE_AUDIT.md` and `INTERFACE_CERTIFICATE.md` preserve old quantifiers and identify missing native inputs. `REGULARITY_REVIEW.md` is explicitly a shared-context proof check. Native signed-triad admission, indivisible action realization, physical time and material occupancy successors remain unestablished.

The complete original 25074-check conversation attachment is not in this Result and was not obtained or rerun. The seven pinned source files and self-contained 3329-check replay are independently accessible at their recorded immutable repository URLs.
