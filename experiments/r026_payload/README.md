# R026 Source Payload Transport

The exact researched R026 Python source is stored as deterministic gzip bytes, base64-encoded into ordered text chunks `source.py.gz.b64part00` ... `source.py.gz.b64part05`.

The public entrypoint `experiments/r026_collapse_external_benchmarks.py` reconstructs and executes the source automatically.

Frozen uncompressed source SHA-256: `4e65d8fef280928ee4c608301af417785d5060979e689afe71ea294acffed1e0`.

This split transport exists only for connector-only publication and does not alter benchmark semantics.
