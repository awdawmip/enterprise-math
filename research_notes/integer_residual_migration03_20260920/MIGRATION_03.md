# Migration 03 — certified polar-to-A2 cell membership

Status: locally tested engineering candidate; not main integration, independent
review, native X6 geometry or a new accepted mathematical tool family.
Researcher: EM-DIRECT-4A5102. Activity: RA-1094DE57986E6E3FDCEA65DA.
Parent source: awdawmip/enterprise-math@621fafbb0a8e6c842b870cf2eed2e48f88a7e80b.
Continue the existing research/integer-residual-m01-angular-20260919-4a5102 branch.

## Recovery and actual consumer

The interrupted predecessor had already published migration 02 (browser BigInt
phase bins and exact CV squared) and its activity checkpoint. Those results were
consumed, not repeated as new work. Its Python consumer blob
`aa2bc95087117b55f06878d71731e097a5eb5d0e` was recovered byte-for-byte and retained
as `evidence/migration03/frozen_m02_multiplication_lab.py` for differential tests.

The existing `multiplication_lab.diagnostics` now has an opt-in exact cell path:

```python
from nollm_visual_toolkit.multiplication_lab import (
    smallest_factors, prime_phases, phases, diagnostics,
)
spf = smallest_factors(4096)
phi = phases(spf, prime_phases(spf))
result = diagnostics(phi, cell_scale=(1, 2), exact_scale=10**12)
assert result['cell_membership_exact']['status'] == 'CERTIFIED_ALL'
```

`cell_scale=(numerator, denominator)` is the exact **layout** scale, not the CV
readout scale or numerical interval precision. Both entries must be positive
integers; the existing layout range one-half through three is preserved.
Do not simultaneously pass a different legacy float `scale`.
`cell_bits` / `cell_max_bits` control the finite interval refinement budget.
`include_cell_certificates=True` includes replayable per-identity certificates;
the default keeps aggregate counts, the exact ordered-phase source digest and
explicit unresolved identities rather than storing every intermediate record.
The digest binds the supplied phase list, not its external origin or generation
history. The input is not modified and cell occupancy never merges native states.

The exact branch never calls float `sqrt`, `sin`, `cos`, `rounded_hex`, or the
legacy floating CV. It executes the existing BRC root/division facade and the
existing AngularDispersion source/readout. Missing BRC fails explicitly; there is
no approximate fallback. Existing default/legacy diagnostics remain unchanged.
The browser quantizer has NOT been switched to this implementation in this slice.

## Integer carrier, residuals and proof obligations

The source remains `(n, phase_tick, 65536, scale_numerator, scale_denominator)`.
Do not recover it from pixels, floats or guessed rational denominators. Equivalent
unreduced scale expressions keep distinct source records.

For dyadic scale S=2**bits, interval endpoints are integers L,U enclosing [L/S,U/S].
Addition, multiplication and rational scaling round outward using the existing BRC
integer quotient/remainder. Square roots are enclosed by integer root evaluation.
`root_ratio_bound(n,d,bits)` retains the exact polynomial certificate

    n*S*S = d*k*k + R,  0 <= R < d*(2*k+1).

R is NOT an additive root tail. All certificate integer fields use decimal strings
for JSON, with separately typed statuses and booleans.

Only the existing 65,536-position phase model is supported. Start at cos(pi/2)=0
and sin(pi/2)=1, take fourteen positive half-angle radicals, then use binary angle
addition and quadrant symmetries. This obtains the required phase enclosures
without evaluating floating pi or transcendental functions. Outward rounding and
intersection with independently valid first-quadrant [0,1] bounds preserve the
exact algebraic value inductively. This is not a general transcendental engine.

In the declared A2 display chart, set

    A = scale*sqrt(n)*cos(theta), B = scale*sqrt(n/3)*sin(theta),
    (q,r,s) = (A-B, 2*B, -A-B).

The source therefore satisfies q+r+s=0 exactly. This is a local display-coordinate
statement; it does not identify the project's native six-dimensional world.

For an integer cube cell a and residual delta=x-a, strict inequalities
`abs(delta_i-delta_j)<1` for all pairs certify a unique nearest cell. To see
sufficiency, any nonzero integer cube-lattice difference z has sum zero, can be
split into t unit positive/negative transfers, and satisfies ||z||^2 >= 2*t.
If max(delta)-min(delta)=M<1, then delta dot z <= M*t; hence
`||delta-z||^2-||delta||^2 >= 2*t*(1-M)>0`.
The implementation proves the inequalities for the whole enclosing box, not just
its midpoint. Failure of this sufficient test yields UNRESOLVED_BOUNDARY, never a
selected speculative cell.

For rational point sources, preserve the actual old rule: coordinate halves round
toward positive infinity, followed by largest-error correction with q,r,s priority.
Nearest-region inequalities are checked exactly after correction. Tie conventions
are part of the observer contract, not a statement that all nearest points agree.

Quarter-turn phases have a shared radical times integer coefficients. An interval
box erases this correlation and may straddle a true tie forever. The narrow
cardinal adapter retains the common radical and determines the sign of
`a*sqrt(n/d)+b` by sign separation followed by comparing `a*a*n` and `b*b*d`.
No squaring of unknown signs is allowed. Exact half-up and error comparisons then
apply the same old tie priority, including irrational q=s ties. Other phases keep
the honest interval/refinement boundary; no all-input termination is claimed.

`verify_cell_record` replays exact source, precision schedule, intervals, residuals
and the declared tie rule. It is not a signature, source-origin authentication,
independent review or a substitute for retained phase-generation provenance.

## Concrete failure witnesses and retained uncertainty

One exact source is n=3, tick=16384, scale=1/2. Its cube coordinates are
(-1/2,1,-1/2). The original float observer returned (0,1), while the unchanged
mathematical tie rule selects (-1,1). Both are nearest boundary cells; the defect
is unstable execution of the declared tie rule, not a wrong interior-distance
claim. Nine such finite witnesses from the local old/new scan are retained in
`evidence/migration03/boundary_witnesses.json`; this is not a claim that exactly
nine defects exist, or that all old experiments were wrong.

An initial interval-only matrix left three identities unresolved at 192 bits:
rank/scale1/2 n=2927; rank/scale1 n=811; rank/scale3/2 n=811. Inspection showed exact
quarter-turn q=s symmetry, still unresolved at 512 bits. The shared-radical adapter
resolves them by source algebra rather than tolerance. Final 4096-point runs of
all three phase modes and scales 1/2,1,3/2 are CERTIFIED_ALL.

Tests also deliberately exhaust a coarse precision budget. An unresolved identity
makes exact occupied-cell/collision/max-load totals null. The report supplies
occupied-cell bounds and the unresolved identity list. It must not report a
precise global count derived from only the certified subset.

## Validation and limits

See validation.json and the replayable scripts. The final source suite has 58
tests: 24 new plus 34 retained. No failures, errors or skipped tests. Checks include
7,500 rational cube-round cases against Fraction and finite nearest-point search,
975 root-ratio certificates, 2,025 interval products, 2,048 cardinal sources,
high-precision phase/coordinate containment, exact and near-boundary cases,
negative/large integers, source ordering, typed JSON tamper rejection, actual BRC
execution, and a real diagnostics test with float geometry functions disabled.
The 100-digit test oracle is supplementary finite evidence, not exact equality
at a boundary: rational oracle cases use Fraction instead of rounded decimals.

Twenty-seven old/new legacy scenarios are byte-structurally equal as Python report
values against the frozen M02 consumer. The existing exact-arithmetic policy
passes the new module and the unchanged angular module. The mixed legacy module
is NOT declared float-free. Wall-clock measurements in benchmark files are only
telemetry, never inputs to cell decisions.

The source-slice runner intentionally excludes two HTML tests. They and the M02
browser results are previous pinned evidence, not rerun or extended certification
of this new Python quantizer. Full Enterprise Math initialization, full package
and repository regression, JavaScript/browser cell-port tests, Safari/iOS,
independent review and main integration remain unverified. The source-slice
bundle retains an explicitly isolated EM initializer: NEVER copy it into the
production repository. Apply migration03.patch to the pinned source instead.

## Reproduce

With the retained source slice (or full candidate checkout) and test dependency
mpmath already installed:

```sh
python tools/run_migration03.py --report evidence/migration03/replayed_tests.json
python tools/benchmark_migration03.py --count 4096 --out evidence/migration03/replayed4096.json
python tools/benchmark_migration03.py --count 65536 --modes golden --scales 1/1 --out evidence/migration03/replayed65536.json
```

Production uses no mpmath; tests fail explicitly when their oracle is unavailable.
No network fetch, dependency installation, hosted CI or daemon is performed by
these scripts.

## Reuse and next smallest unit

REUSE_EXECUTED: existing exact_arithmetic.py (blob
35ea95b0916494b83a92386e3e313928362dd79e), its unchanged core/division dependencies,
and AngularDispersion. EXTEND_EXISTING_TOOL: a narrow dyadic-phase/A2 observer
adapter with shared-source correlation, not a new general scalar family.
Current T0_BRC and precision-tool routing was consulted. Finite affine moment
summaries do not authorize nonlinear occupancy collapse; an incomplete code
search is not proof that no other reusable tool exists.

Next: complete-checkout integration and port this exact cell contract to the
existing browser consumer, with Python/BigInt full-record comparison, explicit
source scale text parsing, shared-radical ties and unresolved-state presentation.
Then migrate defaults only after those actual consumers and their callers are
validated. Do not restart M01/M02 or add another generic residual class. Preserve
candidate/admission separation, P000, original source identity and every frozen
M02 browser change.
