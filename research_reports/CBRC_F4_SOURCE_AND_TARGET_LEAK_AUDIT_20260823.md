# CBRC F4 — Source and Target-Leak Audit

Researcher-ID: `EM-CBRCF4-381080`  
Task: `RS-CBRC-F4-POSITIVE-SEPARATION-RANK-LIFT-CLASSIFICATION`  
Owner branch: `research/cbrc-f4-positive-separation-rank-lift-classification`

## Audit verdict

`TARGET_LEAK_AUDIT_PASS`

No prohibited F0/F1/F2/F3/F3R/F3R2 full report, R063/R064/R065/FQ mathematics,
downstream coherent-BRC/wave research, Hodge/Shor mathematics, or external
quantum/wave theory was read or used.

No rank-two carrier, finite phase group, square/p-power scalar, norm, inner
product, quadratic form, Hadamard/Fourier object, or continuum equation was
constructed or preselected.

## Mathematical inputs actually used

1. Binding taskbook only as specification:
   - `research_tasks/COHERENT_BRC_F4_POSITIVE_SEPARATION_RANK_LIFT_CLASSIFICATION_20260823.md`
   - source commit: `bd10bc351dbe7c90b47a3ffba3ef7796479170f5`
   - blob SHA: `bde7320e8692bd00fb68ef3a9010fa9c30a29b2e`
2. Sole mathematical input:
   - `research_inputs/CBRC_F4_BLIND_POSITIVE_SEPARATION_RANK_LIFT_PACKET_20260823.md`
   - source commit: `c6bdd396f1777185b8791228492ca50f996307a7`
   - blob SHA: `68e078d05738ffcf8bb25e220edf08ab83bca626`

## Governance-only reads

The account-level governance entrypoints `00_BOOTSTRAP.md` and
`OPERATING_MANUAL.md` from `awdawmip/chatgpt-global-knowledge` were read only
for execution/synchronization procedure.  They supplied no mathematical
content to the F4 proof or countermodel.

Canonical global-knowledge snapshot used for this run:
`37cb19cdcae6813387da3714925316fb8027464a`.

## Independent derivation record

The following mathematical items were derived directly from the blind packet:

- the splitting `C ≅ Z e ⊕ T` from the primitive embedding plus retraction;
- the block form of an arbitrary additive automorphism on `C⊕C`;
- the finite-fiber minimum-envelope conservation identity;
- the mixed-difference/forced-period obstruction for every non-signed-
  permutation free block;
- an exact rank-one torsion-mediated globally zero-separating survivor on
  `Z ⊕ Z/2`;
- a strengthening on `Z ⊕ Z/3 ⊕ Z/2` preserving the old `R,J,S` scalar
  invariances;
- the weak-scalar period-six ablation witness.

No proof text from an earlier stage was imported.

## Target-leak checks

- Complex or quadratic integer carrier: **not read / not constructed**.
- Rank-two module: **not read / not constructed**.
- Finite phase group: **not read / not constructed**.
- Square norm / positive quadratic form: **not read / not constructed**.
- Inner product: **not read / not constructed**.
- Hadamard/Fourier/splitter target: **not read / not constructed**.
- Quantum/wave continuum interpretation: **not read / not used**.

## Important semantic boundary found internally

The blind packet does not state that newly added torsion directions must be
transitive under a new family of accepted unary shears, nor does it define
“genuinely mixes” as “the induced free quotient block is non-signed-
permutation.”  The F4 result therefore applies the operational bullets exactly
as written.  A stricter hidden meaning would be a new assumption and is not
imported here.

`TARGET_LEAK_AUDIT_PASS`
