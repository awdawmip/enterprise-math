# Tetrahedral endpoint-sum residuals

Author: **YUAN X**  
Affiliation: **Enterprise Number Theory**  
Prepared: 2026-09-03

This publication branch contains the English manuscripts associated with the four-slice/six-line residual project.

## Manuscripts

- `YUAN_X_Tetrahedral_Endpoint_Sum_Submission.tex` - focused journal submission: integral endpoint-sum cokernel, explicit normal forms, the characteristic-two `S4` non-splitting, affine-function model, and Lean 4 verification.
- `YUAN_X_Tetrahedral_Residuals_Double_Pell_Full.tex` - complete English preprint, additionally containing the FCC carrier certificate, square-half-trace/double-Pell arithmetic, the `P=99` identities, and a conditional Ramanujan `N=58` truncation theorem.

## Certified Lean checkpoints

Residual and symmetry stack:

- branch: `formalization/precision-pi-paper-ii-kernel-v1`
- strict theorem checkpoint: `95a9cd418f6abdb4916f5cf8182437af61dba9db`
- strict workflow run: `33657478048`

Arithmetic, majorization, and tail stack:

- branch: `formalization/precision-pi-paper-ii-v3`
- aggregate theorem checkpoint: `ca2b30c7ef45b470d0d5cb6955def48610cd9dd7`
- aggregate workflow run: `33659295408`
- accepted command: `lake build --wfail -KCI EnterpriseMath`

## Logical boundary

The classical Ramanujan-CM identity for the full `N=58` series is an external analytic input. The finite Lean development certifies the carrier, residual, symmetry, Pell, majorization, monotonicity, and geometric-tail components; it does not replace the modular identity.

## Artificial-intelligence disclosure

OpenAI's ChatGPT assisted with translation, language editing, organization of the exposition, literature discovery, numerical cross-checking, and parts of the Lean proof-development workflow. It is not an author. The named author assumes full responsibility for the mathematical content, citations, and dissemination.

## Locally validated PDFs

The rendered PDFs prepared from these sources were checked page by page with embedded fonts and no clipping or overlap.

- focused submission PDF SHA-256: `5d4b6152250a34a20167dc39a849acf9f513ed2779262a3a74fccb8367be81dd`
- full English PDF SHA-256: `081fb46549a22068d280e657fb22c50db2a5e246673dceb1ccdd403426fbd09d`
- revised Chinese PDF SHA-256: `90ec351f3e24694d4531cb4482b0e28b7d8f1bf08f622948ab1b3c5835883a3b`
