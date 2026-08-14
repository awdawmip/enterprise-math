# RS-R057-AG-FR2-EXACT-INPUT-PAYLOAD-PUBLICATION

Driver-ID: `EM-DVR-R0457K`

Generation family: `R057 / R057G / R057X`

Purpose: transport only. Publish the four already-frozen exact Stage-H/Stage-I joint-surface JSON byte identities into a Git-checkout-accessible recovery payload so a later R057X FR2 replay runtime can pass its 4/4 exact-byte gate. No scientific recomputation or interpretation is authorized.

## Frozen anchors

- `R057X_STAGE_FR_FREEZE_IDENTITY_CHECKPOINT_SHA256`
  `dde3a3edd0a2af71885c6e686747e81cd96d15f692b51494f7416fd6625192c6`
- `R057X_STAGE_FR2_REPLAY_CHECKPOINT_SHA256`
  `3275fcc2720265e67a93a34bd7ae7da08a4f1301bfdbfed4ab0fac8cb870f4d8`
- immutable Stage-F V1 checkpoint
  `4cf6a1fd4d748e1175e77503247f41706aacb4946802a3da7bd03a52a4fdad54`
- Stage-F V1 disposition: `INSUFFICIENT`
- A Stage-H checkpoint
  `bf3c30df26f7a4095935bfce2682e7f8b4bb834ec2c74b838a5d73b26b7e41dc`
- G Stage-I checkpoint
  `a963b2fa951435655885b7eca4ec1d01561825bbb712396aab3516405560171f`

FR2 hard-stopped correctly because its active runtime contained 0/4 raw exact files. This task fixes only that transport defect.

## Exact payload identities

A sample surface:
- filename: `R057_A_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE.json`
- bytes: `2089833`
- SHA256: `4baad1a7c3528d9b147a3ee38fb5436a3e607a2141178a284f540bfc1ce5eaf3`
- accepted origin: exact recovery from original A Stage-H bundle
  `7985a4af5c118554411716b941633670b6429fcf905a72b6c166af9c5b457fd0`

A nuisance surface:
- filename: `R057_A_FROZEN_TRANSITION_NUISANCE_SURFACE.json`
- bytes: `50118`
- SHA256: `ac58760ca6f460961e41287452127060e3e3d2dfd9cf069a65fc6029f1b06e6f`
- same accepted A Stage-H bundle origin.

G sample surface:
- filename: `R057G_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE.json`
- bytes: `1467133`
- SHA256: `f50c9cdab6143e6d1e5339bfb3079e30b56e70991bca40ce9225cfdcc2415c22`
- accepted Stage-I frozen identity.

G nuisance surface:
- filename: `R057G_FROZEN_TRANSITION_NUISANCE_SURFACE.json`
- bytes: `44983`
- SHA256: `14b198f6d1b87cc40454453e99046a946b7f841a6b76469fbbf2f84009b1e723`
- accepted Stage-I frozen identity.

## Publication exception

Normal A/G source surfaces were intentionally sparse. Driver now authorizes a one-time **FROZEN_ARTIFACT_RECOVERY_PAYLOAD** publication because scientific freeze reconciliation cannot proceed while the exact bytes are only represented by hashes, local bundles, or File Library references.

The four JSON files may therefore be committed as ordinary Git blobs despite their size. This is an evidence-transport exception, not a new research artifact generation.

Required canonical recovery payload path:

`recovery_payloads/R057_FR2_EXACT_INPUTS/`

with exactly:

- `R057_A_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE.json`
- `R057_A_FROZEN_TRANSITION_NUISANCE_SURFACE.json`
- `R057G_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE.json`
- `R057G_FROZEN_TRANSITION_NUISANCE_SURFACE.json`
- `R057_FR2_EXACT_INPUT_PAYLOAD_MANIFEST.json`

The manifest must record exact byte length, SHA256, frozen parent checkpoint, origin/recovery provenance, and git blob SHA for each payload file.

## Ownership / execution

This may be executed jointly or sequentially by the existing A/G owners. Each owner may contribute only its own already-frozen bytes until its own pair is hash-verified. After both pairs are present, cross-arm reading is allowed solely for manifest verification because both source checkpoints are already frozen and Driver-accepted.

No new semantic transformation is permitted. Do not pretty-print, normalize JSON, change line endings, key order, whitespace, encoding, or final newline. Copy exact bytes only.

If exact bytes cannot be copied into the Git worktree without mutation, return hard stop rather than regenerating different bytes.

## Hard prohibitions

No coefficient refit.
No optimizer.
No symbolic regression.
No teacher/K/catalog expansion.
No new feature/operator/surrogate.
No parser/segmentation/assembly/readout change.
No Stage-F science replay.
No enrichment or hotspot analysis.
No cross-arm fitted rescaling.
No R057Y.
No D4.
No overwrite or deletion of Stage-H, Stage-I, Stage-F V1, Stage-FR or FR2 frozen artifacts.

## Exact transport gate

Before commit, verify each payload file by raw filesystem bytes:

1. exact byte length;
2. exact SHA256;
3. filename identity;
4. no text reserialization.

All four must pass.

After Git commit/push, independently re-read the committed blobs and verify the same length + SHA256 for all four.

Required status:

`R057_FR2_EXACT_INPUT_PAYLOAD_4_OF_4_PUBLISHED`

Anything less is:

`R057_FR2_EXACT_INPUT_PAYLOAD_INCOMPLETE`

and X FR2 replay remains blocked.

## Required frozen outputs

- four exact raw payload JSONs at the path above;
- `R057_FR2_EXACT_INPUT_PAYLOAD_MANIFEST.json`;
- deterministic transport checker / exact check results;
- recovery payload checkpoint/report.

Freeze and return:

`R057_FR2_EXACT_INPUT_PAYLOAD_CHECKPOINT_SHA256`

Then stop for Driver review.

## Next-stage rule

Only after Driver verifies `4_OF_4_PUBLISHED` may R057X resume as **FR2R**. FR2R must checkout the recovery payload in its own active runtime, verify the four file hashes again, and then execute the exact original Stage-F science contract. FR2R is not authorized by this task itself.

Epistemic label:

`FROZEN_ARTIFACT_TRANSPORT / NO_NEW_SCIENCE / NOT_THEOREM / NOT_CANONICAL`
