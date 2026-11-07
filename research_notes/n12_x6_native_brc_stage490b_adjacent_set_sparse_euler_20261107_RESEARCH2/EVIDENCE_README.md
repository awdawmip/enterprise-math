# Stage490-B full source and evidence (lossless UTF-8 gzip/base64)

Both text files have metadata headers `filename`, `sha256-uncompressed`, `content-base64:` and one gzip+base64 payload line. Each can be decoded with Python standard library:

```python
import base64, gzip, hashlib, pathlib
for item in ('REPRO_STAGE490B_PY_GZIP_BASE64.txt','STAGE490B_EXECUTED_JSON_GZIP_BASE64.txt'):
    lines=pathlib.Path(item).read_text().splitlines()
    name=next(x.split(': ',1)[1] for x in lines if x.startswith('filename: '))
    expected=next(x.split(': ',1)[1] for x in lines if x.startswith('sha256-uncompressed: '))
    payload=lines[lines.index('content-base64:')+1]
    raw=gzip.decompress(base64.b64decode(payload))
    assert hashlib.sha256(raw).hexdigest()==expected
    pathlib.Path(name).write_bytes(raw)
```

Actual author-run source SHA256: `88887420a1633855c61ca022fb646419905b6359edc75c7712a799429664bd08`. Full executed JSON SHA256: `3a154681bcfc13a3dfe3dfed41b3017d9e19569686f80ae4fc324086d45f7bf8`. The human-readable `STAGE490B_EXECUTED_SUMMARY.json` preserves key output, and `REPRO_STAGE490B_PORTABLE.py` is an independent small runnable verifier. Do not treat remote storage as mathematical admission.
