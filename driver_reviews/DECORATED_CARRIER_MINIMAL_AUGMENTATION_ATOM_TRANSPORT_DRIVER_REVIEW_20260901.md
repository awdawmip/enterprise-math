# Decorated Carrier Minimal Augmentation — Driver Review

Driver-ID: `EM-DVR-P8H4Q2`  
Task: `RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT`  
Publication: `TP2-DCE2A9D900EF145F0E77`  
Result: `RR-AA2C14AA62C19342EB97`  
Date: `2026-09-01`

## Disposition

`REQUEST_REVISION / RESULT_ENVELOPE_ONLY / MATHEMATICAL_PAYLOAD_RETAINED`

The Generation-1 mathematical payload passes Driver review at the declared restricted strength, but the immutable Result record is not eligible for terminal acceptance because its `output_manifest` binds only the short Return while the frozen theorem is materially supported by additional proof/checker/atlas evidence and execution provenance.

The active Result contract requires `EVERY_OUTPUT_PINS_GIT_BLOB_AND_SHA256`. The source PR adds six frozen files: short Return, full proof artifact, machine-readable augmentation atlas, deterministic checker, execution record, and Result record. The immutable Result `RR-AA2C14AA62C19342EB97` lists only the short Return in `output_manifest`. The full proof, atlas, checker, and execution chain are therefore not bound by the Result envelope.

This is a control/evidence defect, not a mathematical rejection. The original Result remains immutable history.

## Mathematical audit retained

At the exact typed decorated-carrier strength, no Driver counterexample was found to the following claims.

### L1 -> L2

The marked carrier state identifies the stabilizer of the distinguished pairing state with `C2`, giving a typed splitting of

`1 -> C3=A3 -> S3 ->sgn C2 -> 1`.

For a fixed L1 holonomy `h: pi1(X) -> C2`, relative S3 lifts modulo kernel vertex gauge are classified by

`H^1(X; C3_h)`,

where the nontrivial C2 element acts on C3 by inversion.

For the accepted free-rank normal form with `beta=rank pi1(X)`, the frozen formula is correct:

- `d2=0` for `beta=0`;
- `d2=beta` for `h=0`;
- `d2=beta-1` for `h!=0`.

This follows because the bouquet local-system coboundary `C3 -> C3^beta` has rank zero for trivial monodromy and rank one as soon as at least one generator acts by inversion.

### L2 -> L3

For the standard split extension

`1 -> V4 -> S4 -> S3 -> 1`,

relative atom lifts of a fixed `rho: pi1(X) -> S3` modulo V4 kernel gauge are classified by

`H^1(X; V4_rho)`.

For `beta>=1`, the frozen dimension formula is correct:

`d3 = 2*beta - 2 + dim(V4^im(rho))`,

with `d3=0` for `beta=0`. It is the free-group cohomology formula `dim M^beta - rank(delta)` with `M=V4 ~= F2^2` and `ker(delta)=M^im(rho)`.

The four homomorphic complements `S3 -> S4` are conjugate by the regular V4 action. Changing a temporary section by V4 changes the coordinate cocycle by a twisted coboundary, so section choice is presentation/gauge rather than an independent unframed structural datum.

The Result also correctly preserves the negative boundary: the frozen lower reduct supplies no preferred nonzero C3 or V4 kernel-cohomology class. Selecting such a nonzero class requires exogenous typed structure.

These are standard finite-group extension and twisted-cohomology facts specialized to the project-local typed carrier interface. No historical novelty, Working Truth, Foundation, L4, factorization, additive-distance, or canonical theorem promotion is granted.

## Exact evidence-integrity defect

Immutable Result blob:

`sha1:945c619cd2d8959d3ae16d5d6446ceb326958c01`

Result SHA-256:

`sha256:22ec2c7b69fa0edfcb2c6c0e74b53ed761159bebf8a639540a740f6d2b96593e`

Its single manifest row binds only:

`research_returns/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_RETURN_20260901.md`.

But the short Return itself identifies as evidence:

- `research_artifacts/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT/full_research_return_20260901.md`;
- `research_artifacts/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT/augmentation_atlas_20260901.json`;
- `research_checks/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_CHECK_20260901.py`.

The execution record is also part of the immutable Result chain. Those load-bearing outputs must be dual-digest bound by a fresh Result rather than inferred from PR membership.

## Required revision

Publish Generation 2 under the same stable Task-ID with hard target:

`DCTRMIN_RESULT_ENVELOPE_REFROZEN_WITH_COMPLETE_LOAD_BEARING_DIGEST_CHAIN_AND_ZERO_MATH_DRIFT`.

The revision must preserve the Generation-1 short Return, full proof, atlas and checker byte-identically; replay the checker with the exact `PASS checks=8384` terminal line; freeze a fresh integrity manifest and execution record; and create a new immutable Result whose `output_manifest` carries `path + git_blob_sha1 + sha256` for every load-bearing preserved/new output.

Most important invariant:

`MATHEMATICAL_DELTA = NONE`.

If any preserved theorem byte or checker verdict changes, the work is no longer an integrity refreeze and must return as a substantive mathematical revision.

## Routing

Destination: `FOLLOWUP_TASK -> RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT / TP2-1C9E7635984115B9DEF1`.

Parent Objective `OBJ-DECORATED-CARRIER-TRANSPORT-AUGMENTATION-MINIMALITY` remains `OPEN` until a repaired Result receives terminal Driver acceptance. No separate mathematical successor is authorized from Generation 1.
