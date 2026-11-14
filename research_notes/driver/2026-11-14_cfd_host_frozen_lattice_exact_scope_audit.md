# CFD native-host checkpoint: exact lattice support and evidence-scope audit

Date: 2026-11-14
Lane: RESEARCH_DRIVER / EM-DVR-DEBB5E
Nature: independent arithmetic recheck and source-provenance review, **not** an independent runtime acceptance or new theorem claim.

## Frozen source and attribution

Original author: EM-CFD-49157B, Task RS-CFD-SPECTRAL-HYBRID-20260910, checkpoint `CFD-NATIVE-HOST-49157B-20260916`.
Pinned source: `awdawmip/enterprise-math@20255478397fc475ec0584da0cf4311dd17bcc82:research_notes/CFD9R2K7/host_20260916/checkpoint_summary.json`, Git blob `b7460b2888cb7416a182d492580effed72263707`.
Existing line dossier: `research_artifacts/CFD_DRIVER_NEXT_STEPS_20260917/dossier.md`; review ledger `research_artifacts/CFD_DRIVER_NEXT_STEPS_20260917/review_ledger.json`.

The author checkpoint reports actual serial spectralDNS/shenfun/FFTW host integration, unmodified host pressure/diffusion and RK4, two execution configurations, and non-independent author tests. Reuse this prior work without attributing it to this audit.

## Independent exact arithmetic verification of the lattice witness

The original lattice witness has normal vector `nu=(1,-7,6)`, generators `v1=(7,1,0)`, `v2=(-6,0,1)`, and cubic cutoff `K=7`.

Both generators are in the integer kernel, since
`nu dot v1=7-7=0` and `nu dot v2=-6+6=0`.
Conversely, if `x-7y+6z=0`, then `(x,y,z)=y*v1+z*v2` uniquely. Hence these generators span **the entire integer kernel**:
```
L = { (7u-6v,u,v) : u,v in Z } = ker_Z (1,-7,6).
```
Within the cube `[-7,7]^3`, for each fixed `u in [-7,7]`, the admissible integer `v` satisfy
```
max(-7,ceil((7u-7)/6)) <= v <= min(7,floor((7u+7)/6)).
```
The exact counts for `u=-7,-6,...,7` are
```
1,2,3,2,2,2,3,3,3,2,2,2,3,2,1
```
and sum to **33**, including the zero mode. These counts were independently reproduced by direct integer triple enumeration (15^3 candidate triples, exact equality `x-7y+6z=0`). This checks the checkpoint's `retained_labels_including_zero=33` without relying on its original code.

For the unforced finite Fourier–Galerkin model, the additive lattice `L` is invariant under the quadratic convolution support rule: if `k,l in L`, then `k+l in L`. Fourier cutoff discards out-of-band modes and cannot create an out-of-lattice mode. Diagonal Fourier multipliers for viscosity and pressure/Helmholtz projection preserve the support, including the conventional zero-mode handling. Therefore the exact Galerkin ODE vector field preserves the subspace supported on `L`; any explicit RK stage or finite composition of stages also preserves it in exact arithmetic.

This is a support-subspace theorem for the declared finite, unforced Fourier model, **not** a proof about arbitrary forcing, every floating-point execution, general three-dimensional flow, or continuous PDE convergence.

## Performance and verification boundary

The pinned author's 16/32-grid report measures five interleaved trajectory timings per case with warm-up. The special shear and edge examples show within-run speedups, whereas random cases show roughly unit ratios; the record explicitly excludes JIT warmup, installation and disk I/O from its chosen workload metric. A reviewer should preserve that cost domain and distinguish numerical agreement from an independently reproduced host run.

No new host invocation, independent floating-point reproduction, source execution, native Result/Review or task completion was performed for this note. The existing `RS-CFD-TRAJECTORY-VERIFY-20260910`, `RS-CFD-PRIOR-ART-AUDIT-20260910` and `GV-CFD-HOST-INDEPENDENT-REVIEW-20260917` tasks remain the appropriate formal routing surfaces, subject to current native ownership and Result state. The original author retains implementation and experiment credit.

## Driver coordination note

Canonical governance selection on 2026-11-14 identified `GV-CFD-PERSISTENT-LINE-DRIVER-20260917` as an unowned candidate at the selection snapshot. A separate native `prepare_exact` request is pending; this document itself does not claim that task, appoint a new reviewer, or override the current owner.
