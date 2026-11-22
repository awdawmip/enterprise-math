# RH short correlation / ancestor-envelope checkpoint

Date: 2026-11-22. Researcher `EM-DIRECT-B5750A / TASK_RESEARCH`.
Activity `RA-60C6D083A81B19084A74C5BA`.
Scientific premise freeze: `9fc068244e4f1117f1e75df5eb0285c6697d21d7`.

Start with [REPORT.md](REPORT.md). This coherent batch contains four proofs,
two finite computation scripts and their complete interval outputs. It adds:

- the exact squarefree-supported matching error and full-vector convergence;
- the summable background's explicit short-interval tail and retained affine prefix;
- mixed-phase domination by original negative-packet retention;
- an ancestor envelope with a maximal-interpolant description and discrete
  Dirichlet contraction, evaluated on the original 38 packets;
- uniform matching stability of the computable U/Z packet budgets across
  all permitted integer partitions, trees and packet cutoffs.

The mathematical status is author proof and strict finite computation. The
actual unbounded reference arithmetic estimate remains open. No independent
Review, RH proof or canonical truth promotion is asserted.

## New files

- `rh_short_interval_20261122/SHORT_INTERVAL_STRUCTURE_AND_UNIFORM_TRANSFER.md`
- `rh_reference_certificate_20261122/ACTUAL_REFERENCE_SPLIT.md`
- `rh_reference_certificate_20261122/certify_reference_split.py`
- `rh_reference_certificate_20261122/reference_split_certificate.json`
- `rh_phase_dominance_20261122/MIXED_PHASE_DOMINANCE_AND_ANCESTOR_ENVELOPE.md`
- `rh_phase_dominance_20261122/certify_ancestor_compression.py`
- `rh_phase_dominance_20261122/ancestor_compression_certificate.json`
- `rh_short_root_20261122/UNIFORM_ADAPTIVE_REFERENCE_STABILITY.md`

## Reproduce

From a workspace containing the prior dependency directories, run:

```bash
python3 rh_reference_certificate_20261122/certify_reference_split.py
python3 rh_phase_dominance_20261122/certify_ancestor_compression.py
```

The reference calculation reuses the complete road cache when available;
otherwise it invokes the original generator. The ancestor calculation uses
the old interval certificate without rebuilding the road. Both use outward
integer intervals with denominator `10^60` and exact rational geometry.

Prior dependency anchor:
`2e8a9aad42950ce4e0980e284772f23ba8e8da21:research_notes/portable_direct/rh_triangle_correlation_20261122_b5750a/`.
The downloadable bundle includes the unchanged dependency scripts, data
and proof notes needed to follow the new results. The cache is reproducible
and is deliberately not packaged.

All comparisons retain the full integer population, unit, true endpoints,
complete prefix, and typed auxiliary-readout scope. Reproduction success
does not imply the unbounded arithmetic conclusion.
