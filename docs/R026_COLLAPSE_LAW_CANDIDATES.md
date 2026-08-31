# R026 Surviving Cross-Domain Law Candidates

Status: `RESEARCH CANDIDATES / EXTERNALLY CALIBRATED / NOT CANONICAL`

Researcher-ID: `EM-R026-D19F1B`

## L1 — Residual-State Factorization Principle

Let `X` be the full state, `rho : X -> R` the proposed residual coordinate, and `C` the fixed solver/operator/context made available to the iteration. A permitted future observable or transition `F` can be represented exactly from residual state only when it factorizes through `(rho,C)`:

`F(x) = G(rho(x), C)`.

For an entire future language `L`, residual-only state is sound only if every permitted observable/transition in `L` respects the equivalence relation induced by `rho`.

**R026 status:** `SURVIVES_WITH_FACTORISATION_CONDITION`.

Positive witnesses: Euclidean remainder descent, additive error feedback, compensated summation, iterative refinement with sufficiently precise residual, multigrid residual correction, projection displacement, integer raster error accumulation.

Kill tests: nonlinear `x^2` with equal residual/different anchor; elastic-collision conservation; ill-conditioned refinement with residual quantized before correction.

**Novelty boundary:** the component algorithms are prior art. The Enterprise residue is the explicit cross-domain *sufficiency contract* and a candidate checker/compiler that decides whether a proposed residual quotient is valid for the declared future language.

## L2 — Anchor Necessity Boundary

For residual map `rho`, anchor/context can be dropped for an observable `F` **iff** `F` is constant on every residual fiber. Equivalently, a single witness

`rho(x)=rho(y)` but `F(x) != F(y)`

proves that residual-only state is incomplete.

This is the quotient-factorization test specialized to collapse semantics. R026 freezes it as an implementation guard rather than claiming a new abstract theorem.

Minimal witness: `r=1/4`, anchors `0` and `10`, future `F(x)=x^2`.

## L3 — Projection/Correction Duality

A coarse projection `P(x)=a` is safe for a declared task only in one of two regimes:

1. the discarded residual is irrelevant to every required future observable; or
2. a correction channel carries enough residual/context to reconstruct the required effect later.

Otherwise repeated projection can convert local quantization error into systematic drift, stalled refinement, wrong coarse equations, or conservation violation.

## L4 — Objective-Relative Collapse Policy

The wind-tunnel rejects a universal collapse direction. Policy utility is defined by the observable:

- DOWN / UP: one-sided lower/upper enclosure and conservative bounds;
- NEAREST: local metric/MSE objectives;
- distance-weighted stochastic: expectation preservation with variance cost;
- residual/error feedback: long-horizon correction when factorization and precision conditions hold;
- BRC: exact Boolean/result support only;
- FAR: adversarial/extremal control.

## L5 — Metadata Is State When It Changes the Future

Anchor, residual, phase, basin address, active-set identity, RNG state, branch support, precision and reconstruction data are charged as state whenever future results depend on them. A resource advantage cannot be claimed by renaming required state as “metadata”.

## Driver-facing theorem/tool residue

The strongest Enterprise specialization suggested by R026 is not a new numerical solver. It is a **Collapse Contract Compiler**:

`(full state, proposed collapse map, declared future language/observable, precision schedule)`

->

`{EXACT_QUOTIENT, RESIDUAL_SUFFICIENT, ANCHOR_REQUIRED, SUPPORT_ONLY, APPROXIMATE, INVALID}`

plus state/work/reconstruction accounting and automatically generated hostile witnesses when factorization fails.
