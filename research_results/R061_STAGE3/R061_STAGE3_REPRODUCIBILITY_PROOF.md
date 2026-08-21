# R061 Stage 3 — Reproducibility Proof

Researcher-ID: `EM-R061S3-2F9622`

Executable checker:

`scripts/r061_stage3_validate_unoriented_segment_symmetry.py`

The checker regenerates Stage 3 evidence from the frozen Stage 2 decode and trace rules. It does not read a Stage 3 summary as expected truth.

It performs:

- Stage 2 point-pair decomposition regression on the `81`-vertex patch;
- explicit Stage 2 path replay through `a+b<=12` over seven translated starts and all three sectors;
- Stage 2 axis-gluing regression;
- all `6561` ordered and `3321` unordered endpoint-pair bidirectional audits;
- exact inverse-trace versus canonical-reverse typing;
- exact bidirectional spectra and a deterministic SHA256;
- exact reversal-symmetry-locus audit;
- translated/cyclic covariance and scaling;
- exact `d_max`, `d_sum`, and `d_2` metric audits;
- all `531441` ordered triangle triples using integer radical comparisons only;
- unit-step and `3-4-5` obstruction witnesses;
- mismatch preservation.

No theorem-critical decision uses floating point.

Current generated result:

`mismatch_count=0`

and

`bidirectional_pair_sha256=e1e8b729506277d662a5654d7cf076f860687dc8073984a296d96d3bc85fca6a`.

The finite checker is evidence. The orbit, no-go, and metric-construction claims are justified by the accompanying proofs.
