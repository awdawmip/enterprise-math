# R026 machine artifacts

The full 245-row result tables are frozen as deterministic gzip streams. Because the connector-only owner checkpoint cannot send local binary files directly, each `.gz` is transported as ordered base64 text parts (`*.b64partNN`).

Reconstruct the raw machine-readable files with:

```bash
python experiments/data/r026/reconstruct_frozen_results.py json
python experiments/data/r026/reconstruct_frozen_results.py csv
```

The script concatenates the ordered parts, base64-decodes them, verifies the frozen gzip SHA-256, gzip-decompresses the bytes, and writes the raw `.json` / `.csv`. The JSON path also verifies the frozen raw JSON SHA-256.

The benchmark runner itself is packaged the same way under `experiments/r026_payload/`; `experiments/r026_collapse_external_benchmarks.py` reconstructs and executes the exact frozen source automatically.

Frozen hashes:

- runner source SHA-256: `4e65d8fef280928ee4c608301af417785d5060979e689afe71ea294acffed1e0`
- full JSON SHA-256: `a7b69a96d31316b6ff78f03b31577e2ef27ae1f7f04a49ad486ab2db53b4d00b`
- capability matrix SHA-256: `5544b9b2d88ddc55192182ecdb6083a85ffd5fa857688425914ee93690ed4505`
- JSON gzip SHA-256: `ebc643c30a02384510625d5997f8d0d497275969e3923b0769a2a341c7cf7e9e`
- CSV gzip SHA-256: `d16f6e0390f3b8f1d39927adcf01c05b8fd3e5ee806a635a3084ef7422d53cbf`

The reconstructed files are the frozen full machine-readable 245-row artifacts; the executable runner regenerates the same row schema directly.
