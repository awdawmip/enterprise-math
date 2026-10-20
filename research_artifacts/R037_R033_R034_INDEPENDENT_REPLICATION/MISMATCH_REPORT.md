# R037 mismatch report

Researcher-ID: `EM-R037-204389`

## Mathematical mismatches

**None found** in the theorem-critical R033/R034 formulas and finite reference data audited in this run.

The independent computations reproduced the FCC/HCP graph growth laws, first finite differences, stable boundary populations, common exposed-face count, finite rational topology certificate through radius 20, stable limit-shape data, intrinsic-scalar macro limits, local drift/covariance, finite propagation data through time 12, local third/fourth tensors, exact fourth/sixth radial moment formulas, and principal small-k spectral expansions.

## Evidence-grade differences

One frozen item becomes stronger rather than weaker:

- `R034-BARLOW-RETURN-GAUGE`: frozen grade was theorem candidate.  The audit gives a complete fiber-level gauge proof on the bi-infinite layer line: every interlayer hopping has a stacking-dependent phase but stacking-independent magnitude, and the line has no cycle flux.  A root-preserving diagonal gauge makes every fiber the same constant-magnitude Jacobi operator.  Within the ideal uniform-NN Barlow scope this upgrades all-time return probability and root local spectral measure universality to `REPRODUCED_EXACT`.

No claim was weakened to `FAILED_OR_MISMATCH`.

## Claims deliberately not promoted

- The exposed-face boundary complex is independently certified as a connected closed 2-manifold with Euler characteristic 2 for every `r=0..20`, but no all-radius induction was completed.  The all-`r` sphere statement therefore remains `THEOREM_CANDIDATE_ONLY`.
- The Barlow gauge is momentum-dependent and is not a physical-coordinate vertex permutation.  It does not imply a pointwise nonperiodic local CLT or a global uniform heat-kernel bound.  That stronger statement remains open.

## Provenance/process nonconformance

There is one process caveat that must not be hidden.  During setup, a GitHub API lookup of the frozen R034 owner-head commit unexpectedly returned a partial patch of the frozen experiment script **before** the independent R034 implementation was complete.  The script was never executed, imported, copied as a computation engine, or used to generate the audit outputs; the computations and proofs were rebuilt separately.  Nevertheless, the taskbook's preferred ordering was to defer frozen implementation/output inspection until after independent construction.

Therefore:

- R033 is clean with respect to frozen executable exposure;
- R034 mathematical replication is complete to the evidence grades in the matrix;
- the combined run must **not** be advertised as strict zero-exposure / provenance-clean independent replication;
- Driver may accept the mathematical audit with this caveat, or reissue only the R034 portion into a fresh clean conversation if a provenance-clean replication label is required.

This is a process-provenance limitation, not a discovered mathematical counterexample.
