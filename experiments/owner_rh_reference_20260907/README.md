# Exact N=8 prime+Cauchy reference, eta=9/10

This auxiliary package produces a rigorous interval enclosure of one declared
32-dimensional reference matrix and passes it to an independent Fraction inertia
certificate. It does not assert RH, full-window positivity, or physical dynamics.

`reference_builder.py` is the Arb producer. `inertia_certificate.py` and its tests
are independently owned by `/root/stability_research`. The producer neither calls
the old eta=1 positivity checker nor assumes the historical candidate count 8.

## Matrix and preserved labels

Order is O- modes 1..8, O+ modes 1..8, S- modes 1..8, S+ modes 1..8, with supports
[-log2,0], [0,log2], [-log3,-log2], [log2,log3]. Each mode is the normalized
Dirichlet sine on its labelled interval and zero off that interval.

The matrix is `[[81/100 A,B],[B^T,D]]`. A and D retain complete archimedean,
finite-prime and both pole-channel terms. B is exactly `B_prime+B_Cauchy`; it
contains neither pole cross nor regular arch cross. Prime shifts retain the exact
Fraction endpoint comparisons and prime powers {2,3,4,5,7,8,9}. No branch-label or
parity quotient is taken.

The reused source is `../../scripts/rh_log3_n8_arb_certificate.py`, SHA256
`4e337855d8605125ded80c029022fdc950d1b92cf78ce772480a7b99b9dad49b`, byte-identical
to source head `d0a4eca2a49a9167848ba4d5d5cfd7eb03d355f7`. Only the two required
16x16 diagonal blocks are constructed, using its exact prefix, Hurwitz-zeta tail,
and rigorously enclosed algebraic/exponential remainder. The actual new run uses
K=256, P=10, 384 bits, within the independently audited convergent domain. Every
product denominator `1-((abs(alpha_i)+abs(alpha_j))/c_K)^2` must be provably positive.

## Cauchy calculation and error contract

For each old/shell pair the actual left interval is put first. In particular,
S- precedes both old intervals. The inherited `ordered_distinct_laplace` gives
`L_ij(c)=integral integral phi_i(x)phi_j(y) exp(-c(y-x)) dx dy`, and the entry is
`-1/2 integral_0^infinity L_ij(c) dc`. The 1/2 occurs exactly once; symmetry is
assembled by transposing the finished cross block.

The finite part uses `acb.integral` on dyadic panels from 0 to C0=20000. Its callback
is meromorphic, consisting only of rational functions and exponentials of c;
pole-containing complex balls produce non-finite values. No branch-cut functions
are introduced in c. Default resource bounds are 4000 evaluations per panel,
100000 per entry, 2000000 total callbacks, depth 20, degree 32. Absolute and
relative tolerance goals are 2^-60. A finite but wider-than-requested result remains
an enclosure and will be judged by the independent inertia verifier; resource or
non-finite failures return UNDETERMINED, not a spectral conclusion.

In python-flint 0.9.0, a Python exception raised by the callback may surface as a
Cython SystemError chain rather than the original exception. The top-level
producer catches it and emits UNDETERMINED without bounds. An independent forced
entry-budget test verified that behavior; the backend made 12 callbacks while
unwinding a limit-1 trigger. The configured callback guard is therefore an abort
trigger, not a promise of zero extra foreign-function callbacks during unwinding.

The omitted c tail is bounded in absolute value by
`2 norm_i norm_j alpha_i alpha_j/(3 C0^3) < 10240/C0^3`.
This follows from the four numerator exponentials being bounded by 1 and the
denominator by c^4; use pi<4, log2>2/3, log(3/2)>2/5. At C0=20000 the entry tail
is 1/781250000 = 1.28e-9. It is added as an Arb error ball to every cross entry.
The 16x16 cross tail norm is below 2.048e-8 by row/column sums. Finite quadrature
error, the inherited arch tail, all rounding, and this Cauchy tail are already
inside the exported matrix. No additional frequency-tail beta is to be added.

## Exact export and independent input boundary

The JSON schema is `owner_rh_reference_bounds_v1`; successful production has
`status="ENCLOSED"`, eta `"9/10"`, dimension 32, labels, and a symmetric 32x32
`bounds` array with entries `{"lo":"p/q","hi":"p/q"}`. This status means only
entry enclosure, not an inertia certificate.

Export calls Arb's directed `lower()`/`upper()`, reads exact `man_exp()` data, then
rounds lower downward and upper upward to the dyadic grid 2^-160 using integer
shifts. Each extra widening is less than 2^-160. There is no decimal formatting or
parsing of displayed midpoint/radius text. Extremely small panel-error diagnostics
therefore do not create enormous decimal denominators.

Top-level provenance binds the inherited and current producer source hashes,
actual Python/flint version, and exact algorithm parameters. A component cache is
optional, but reuse requires its explicit trusted SHA256 as an argument; matching
self-reported cache parameters alone is insufficient. Matrix-interval semantics
still depend on the producer audit. The independent Fraction checker proves the
inertia of the bound input interval family, not the correctness of arbitrary
self-reported matrix entries.

## Actual isolated environment and CLI

The owner prepared and tested Python 3.12.14 and python-flint 0.9.0 without changing
the system interpreter or bundled runtime. In PowerShell, from the worktree root:

```powershell
$env:PYTHONPATH = 'C:/Users/Administrator/AppData/Local/Temp/em-owner-flint-py312'
& 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' experiments/owner_rh_reference_20260907/reference_builder.py --K 256 --P 10 --prec 384 --cauchy-cutoff 20000 --output experiments/owner_rh_reference_20260907/reference_bounds_fresh.json --components-output experiments/owner_rh_reference_20260907/reference_components_fresh.json --progress-output experiments/owner_rh_reference_20260907/reference_progress_fresh.json
```

Python API is `build_reference_bounds(...) -> JSON-safe payload`. Failures have
status UNDETERMINED, reason, parameters and diagnostics, and no complete bounds.
CLI writes the payload with LF and exits nonzero on UNDETERMINED. Successful
output is handed to `certify_interval_inertia(bounds,labels)` and subsequently
`verify_interval_inertia(...)` from the independent tool.

## Preserved run history

- run001: K256/P10/384/C0=20000; components succeeded, but direct exact export of
  an exponentially tiny radius exceeded Python's 4300-digit integer-string limit
  after 8 cross entries. The saved status is UNDETERMINED. This is a representation
  failure, not a mathematical or inertia failure. The components cache SHA256 is
  `6769025e9448c1c0c57c4b3653f902f9486c34f2e963eaa4633968afcc91260e`.
- run002: same mathematics, with rigorous 2^-160 export; all 256 cross entries,
  4096 panels, 174828 callbacks were enclosed. Its original JSON remains unchanged.
  The owner independently certified 8 negative and 24 positive dimensions using
  the two rational shifted matrices, then verified the witness.
- After run002, explicit trusted-cache SHA and current producer-source provenance
  were added. `run002_reference_builder_snapshot.py.txt` is a byte reconstruction
  obtained by reversing that single recorded post-run patch; its reconstruction
  status is explicitly recorded in `run002_source_reconstruction.json`. It is not
  falsely labelled as a source hash captured during run002.
- run003: final source-bound ENCLOSED payload, producer SHA256
  `67a15aaebe4a27b59dd29b1e833da456e85581705eb601eeba712818c37f92ca` and explicit
  trusted-cache SHA recorded. Its eta, labels and bounds are canonical-JSON
  byte-identical to run002. The independent witness was rebound and verified:
  8 negative, 24 positive, 0 zero in both shifted rational matrices.
  `reference_inertia_report_run003.json` is the final verification report;
  `reference_run002_run003_comparison.json` preserves the comparison.

No mathematical cutoff or series-order increase was needed in response to the
first independent inertia result. Historical eta=1 flags, float eigenvalues and
the candidate q=8 are never proof inputs.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
