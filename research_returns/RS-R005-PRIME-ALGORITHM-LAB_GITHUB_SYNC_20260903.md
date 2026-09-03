# GitHub Sync Receipt — RS-R005-PRIME-ALGORITHM-LAB

Date: `2026-09-03`
Status: `DURABLE_HANDOFF_PUBLISHED / PR_OPEN / NOT_MERGED / NOT_CANONICAL`

## Source lineage

- repository: `awdawmip/enterprise-math`
- continuation branch: `research/r005a-prime-algorithm-lab-20260903`
- parent research branch: `research/r005a-prime-algorithm-lab-20260810`
- parent commit: `14db099861661d3a57133374c2fb3b7cfe6012ec`
- first publication commit: `05a93b75ccdb2671a95dd87ebc2b14b711058b1c`
- pull request: `#1140`
- pull request base: `research/r005a-prime-algorithm-lab-20260810`

## Published repository-native material

Core review surface:

- `docs/R005A_P2_DEFICIT_SHADOW_INVERSION_20260902.md`
- `experiments/r005a_p2_gap_shadow_inversion.py`
- `experiments/r005a_p2_gap_shadow_inversion_regression.py`
- `experiments/r005a_p2_one_unit_guard_regression.cpp`
- patched `experiments/r005a_p2_discrete_gap916_patch.cpp`
- `research_returns/RS-R005-PRIME-ALGORITHM-LAB_20260902.md`

Audit surface:

- `research_artifacts/RS-R005-PRIME-ALGORITHM-LAB_20260902/`
- validation transcript and exact evidence rows
- original artifact manifest
- exact one-unit guard patch
- convenience ZIP SHA-256 receipt

The convenience ZIP itself is not required for repository-native review: its research/code/evidence contents are materialized as ordinary Git files. Its frozen local SHA-256 remains:

`5f89f6a755869dfa58dd0d457ef55c6c128fec3d70057909d7263bfe37505f95`

The PR diff is the authoritative Git-native complete patch for this publication.

## Claim boundary after publication

Publication changes durability only; it does not upgrade mathematical status.

- certified frontier remains `k <= 2822453183433`;
- `q=78553` remains blocked on a complete independently auditable exact-916-gap catalogue for starts `[1291005053866735,1294364244470160]`;
- no canonical/Foundation promotion;
- Lean formalization pending;
- no global novelty claim.

`main` is intentionally untouched by this publication.
