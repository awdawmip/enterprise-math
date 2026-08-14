# RS-R057-A-STAGE-H-FROZEN-ARTIFACT-RECOVERY

Researcher-ID: `EM-R057-6A31F2`

Generation family: `R057 / R057X`

Purpose: recover the exact frozen A Stage-H large joint-surface bytes that are currently hash-anchored but not durably retrievable, so R057X Stage-F scientific replay can later be performed from exact accepted inputs. This is artifact recovery only, not a new scientific stage.

## Frozen anchors

- `R057_A_STAGE_H_JOINT_SURFACE_CHECKPOINT_SHA256 = bf3c30df26f7a4095935bfce2682e7f8b4bb834ec2c74b838a5d73b26b7e41dc`
- accepted Stage-H source head: `research/r057-stage0@2f12c79548d236a757bdba1e57fc48cc0522c020`
- `R057_A_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE_SHA256 = 4baad1a7c3528d9b147a3ee38fb5436a3e607a2141178a284f540bfc1ce5eaf3`
- expected bytes: `2089833`
- `R057_A_FROZEN_TRANSITION_NUISANCE_SURFACE_SHA256 = ac58760ca6f460961e41287452127060e3e3d2dfd9cf069a65fc6029f1b06e6f`
- expected bytes: `50118`
- accepted Stage-H bundle SHA256: `7985a4af5c118554411716b941633670b6429fcf905a72b6c166af9c5b457fd0`
- accepted X Stage-F V1 historical identity: `4cf6a1fd4d748e1175e77503247f41706aacb4946802a3da7bd03a52a4fdad54`
- accepted X Stage-FR reconciliation checkpoint pending Driver acceptance: `dde3a3edd0a2af71885c6e686747e81cd96d15f692b51494f7416fd6625192c6`

All earlier frozen scientific results remain immutable.

## Goal

Recover and durably publish the exact accepted bytes for:

1. `R057_A_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE.json`
2. `R057_A_FROZEN_TRANSITION_NUISANCE_SURFACE.json`

Preferred recovery order:

1. recover original exact files from surviving Stage-H workspace/cache/bundle;
2. recover the accepted Stage-H bundle and extract them;
3. only if original bytes are unavailable, deterministically re-materialize from the exact frozen Stage-H inputs/code/serialization contract.

A re-materialized file counts as successful recovery **only if both byte length and SHA256 exactly equal the frozen targets above**. Semantic equivalence or numerically identical parsed JSON with different bytes is not sufficient.

## Hard prohibitions

No refit.
No optimizer.
No symbolic regression.
No new teacher.
No K expansion.
No new feature/operator/surrogate.
No parser/context/segmentation/assembly/readout change.
No change to motif semantics or exposure denominators.
No change to nuisance definitions.
No Stage-F enrichment/hotspot recomputation.
No R057Y.
No D4 generator work.
No modification or overwrite of any existing Stage-H checkpoint/report/manifest or Stage-F/FR frozen artifact.

## Recovery lane R0 — provenance gate

Verify the accepted Stage-H checkpoint/report/manifest hashes and source head. Record exact source locations attempted: original workspace, local archives, caches, Git bundle, File Library, and deterministic regeneration route if needed.

If any recovered candidate file has the correct filename but wrong size or SHA256, quarantine it as `NONIDENTICAL_CANDIDATE` and do not publish it as frozen recovery.

## Recovery lane R1 — exact sample surface

Recover `R057_A_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE.json`.

Success requires:
- bytes = `2089833`;
- SHA256 = `4baad1a7c3528d9b147a3ee38fb5436a3e607a2141178a284f540bfc1ce5eaf3`.

On success, publish the exact file bytes on a dedicated recovery branch. Because this recovery exists to restore durable replayability, the prior sparse-publication convention is explicitly overridden for these two already-frozen artifacts only.

## Recovery lane R2 — exact nuisance surface

Recover `R057_A_FROZEN_TRANSITION_NUISANCE_SURFACE.json`.

Success requires:
- bytes = `50118`;
- SHA256 = `ac58760ca6f460961e41287452127060e3e3d2dfd9cf069a65fc6029f1b06e6f`.

Publish exact bytes on the same recovery branch.

## Recovery lane R3 — optional original bundle

Attempt to recover the original Stage-H bundle with SHA256:
`7985a4af5c118554411716b941633670b6429fcf905a72b6c166af9c5b457fd0`.

Bundle recovery is desirable but not required for downstream X replay if both exact JSON surfaces are recovered and independently hash-verified.

Do not create a replacement bundle and label it with the old SHA. Any newly packaged bundle must have a new recovery-package identity and must preserve the two recovered frozen files byte-for-byte.

## Recovery lane R4 — independent verification

Use at least two independent byte-hash checks for each recovered file. Verify filename, byte count and SHA256. Where possible compare Git blob round-trip bytes after publication.

Required statuses:
- `EXACT_A_STAGE_H_SURFACES_RECOVERED`
- `PARTIAL_A_STAGE_H_SURFACE_RECOVERY`
- `A_STAGE_H_EXACT_SURFACES_UNRECOVERABLE`

Do not infer scientific consequences from the status.

## Required recovery artifacts

- `R057_A_STAGE_H_ARTIFACT_RECOVERY_REGISTRY.json`
- `R057_A_STAGE_H_ARTIFACT_RECOVERY_CHECK_RESULTS.json`
- `R057_A_STAGE_H_ARTIFACT_RECOVERY_CHECKPOINT.json`
- exact recovered large surface file(s), if recovered
- optional recovered original bundle or new recovery package, clearly distinguished

Freeze and return:

`R057_A_STAGE_H_ARTIFACT_RECOVERY_CHECKPOINT_SHA256`

Then stop for Driver review.

## Next routing

If and only if both exact surfaces are recovered, Driver may authorize an X-owned Stage-FR2 clean scientific replay from exact A-H + G-I inputs under the already-frozen Stage-F rules. Artifact recovery itself does not change the authority of Stage-F V1 and does not authorize a V2.

Epistemic label:
`ARTIFACT_RECOVERY_ONLY / NO_NEW_SCIENCE / NOT_THEOREM / NOT_CANONICAL`
