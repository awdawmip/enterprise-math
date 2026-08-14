# R057X Stage FR2 — Exact-input clean Stage-F scientific replay

Researcher-ID: `EM-R057X-5E8C41`

Status: `FR2_HARD_STOP_EXACT_INPUT_UNAVAILABLE / NO_SCIENCE_REPLAY / AWAITING_DRIVER_REVIEW`

## Frozen anchors

- Stage FR checkpoint: `dde3a3edd0a2af71885c6e686747e81cd96d15f692b51494f7416fd6625192c6`
- Stage-F V1 checkpoint: `4cf6a1fd4d748e1175e77503247f41706aacb4946802a3da7bd03a52a4fdad54`
- Stage-F V1 disposition: `INSUFFICIENT`
- Stage-E checkpoint: `3937572b2f8099f9ce125a86ccf90ec9aad6f9470b0af9ec4b8026df67796385`

## FR2-0 exact byte gate

The FR2 taskbook requires the **current FR2 runtime to possess all four exact large-surface files** and requires byte-length plus SHA256 verification before any Stage-F science computation.

Expected identities:

- A sample: 2,089,833 bytes / `4baad1a7c3528d9b147a3ee38fb5436a3e607a2141178a284f540bfc1ce5eaf3`
- A nuisance: 50,118 bytes / `ac58760ca6f460961e41287452127060e3e3d2dfd9cf069a65fc6029f1b06e6f`
- G sample: 1,467,133 bytes / `f50c9cdab6143e6d1e5339bfb3079e30b56e70991bca40ce9225cfdcc2415c22`
- G nuisance: 44,983 bytes / `14b198f6d1b87cc40454453e99046a946b7f841a6b76469fbbf2f84009b1e723`

A direct `/mnt/data` runtime filesystem probe found none of these four exact target files.

The accepted A recovery is real and hash-anchored: its recovery transport/materializer provenance is traceable and the Driver has accepted the recovered identities. However, the recovered target files are not mounted as exact files in this FR2 runtime.

The accepted G Stage-I files are available as File Library references, but a File Library reference / parsed document view is not a byte-mounted file in the active runtime. FR2 explicitly prohibits treating parsed-equivalent JSON as the exact input.

Therefore the exact byte gate fails **before science**.

## Verdict

`FR2_HARD_STOP_EXACT_INPUT_UNAVAILABLE`

No Stage-F F1-F6 replay was executed. No motif enrichment, nuisance-light re-selection, BH test, coverage association or disposition logic was run.

V1 remains immutable and is neither upgraded nor rejected by FR2. No V2 checkpoint is created.

## Firewall

No refit, optimizer, symbolic regression, teacher/K/catalog/feature/operator expansion, parser/segmentation/assembly/readout mutation, interpolation, fitted cross-arm rescaling, R057Y read, or D4 work occurred.

Epistemic label: `FREEZE_RECONCILIATION / EXACT_INPUT_CLEAN_REPLAY / NO_NEW_SCIENCE / NOT_THEOREM / NOT_CANONICAL`.
