# BRC Critical-Degeneracy Exact Log-Correction Carrier

Status: `RESEARCH CANDIDATE / EXACT FINITE INTEGER CRITICAL MATRIX / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parents: `WBRC-T21`, `WBRC-T38`, merged PRs #1166/#1167

## 1. Purpose

Merged PR #1167 gives the multi-critical large-moment correction

\[
\frac{\rho(W^{(m)})}{\mu^m}\to\rho(K),
\]

where `K` is the non-negative integer critical-degeneracy matrix built from the exact histogram dominant tie multiplicities on tropical critical edges.

The correction is therefore

\[
\Gamma_{\rm crit}=\ln\rho(K).
\]

The current Enterprise exact-arithmetic policy does not use a floating eigensolver as primitive state and does not provide a general arbitrary-algebraic root evaluator. This note supplies an exact symbolic carrier for the correction using the existing `WBRC-T21` criticality-polynomial principle.

## 2. Integer criticality polynomial

Define

\[
\boxed{p_K(z)=\det(I-zK)\in\mathbb Z[z]}.
\]

Because `K` is a critical graph, it has at least one recurrent directed cycle and

\[
\rho(K)\ge1.
\]

By `WBRC-T21`, applied to the integer matrix `K`, the smallest positive real root is

\[
\boxed{z_c(K)=\frac1{\rho(K)}}.
\]

Hence

\[
\boxed{\Gamma_{\rm crit}=-\ln z_c(K)}.
\]

This is an exact semantic identity even when `z_c` is irrational algebraic.

## 3. Exact root-selector carrier

Define a symbolic carrier

```text
CriticalRootSelector(
  polynomial = p_K in Z[z],
  selector = SMALLEST_POSITIVE_REAL_ROOT,
  isolating_interval = [a,b] subset Q_{>0},
  exact_rational_root = optional Fraction
)
```

The isolating interval is an exact certificate:

- no positive root lies below `a`;
- exactly one distinct positive root lies in `[a,b]` (or the selected root is an exact rational endpoint);
- the selected root is the smallest positive root of `p_K`.

No decimal approximation is part of the semantic state.

## 4. Rational-root simplification

Since

\[
p_K(0)=1,
\]

any positive rational root of the primitive integer polynomial must have numerator 1. Thus every positive rational candidate is of the form

\[
\boxed{z=1/q}
\]

where `q` divides the absolute leading coefficient of `p_K`.

Therefore rational roots can be enumerated and divided out exactly before isolating any irrational positive root.

For the remaining rational polynomial factor, no rational bisection endpoint can be a root. Sturm-sequence root counts then isolate the smallest irrational positive root without endpoint ambiguity.

The exact smallest positive root is the minimum of:

- the finite rational-root set in `(0,1]`;
- the smallest Sturm-isolated irrational root in `(0,1)`.

## 5. Derived BRC log carrier

The exact critical log state is

```text
CriticalLogCorrection(
  K,
  p_K,
  root_selector=z_c,
  rho_semantic=1/z_c,
  log_semantic=-LN_ALGEBRAIC_ROOT(z_c)
)
```

This notation does **not** mean the current rational `LN` runtime can directly materialize an arbitrary algebraic input. It preserves the exact mathematical object until a supported specialization is available.

### 5.1 Rational selected root

If `z_c=a/b in Q_{>0}`, then

\[
\Gamma_{\rm crit}=\ln(b/a),
\]

which routes directly through the existing rational `DIV -> LN` facade.

### 5.2 Unique critical cycle

For one critical cycle of length `r` and degeneracy product `D`,

\[
p_K(z)=1-Dz^r.
\]

Hence

\[
z_c=D^{-1/r},
\qquad
\Gamma_{\rm crit}=\frac1r\ln D.
\]

If `D` is a perfect `r`-th power, `z_c` is rational and the existing rational runtime materializes it directly. Otherwise the exact root remains a one-polynomial algebraic selector, while the equivalent `ln D / r` readout can be formed using existing rational `LN` plus symbolic division.

### 5.3 Branching critical graph with rational correction

For

\[
K=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

\[
p_K(z)=1-2z,
\qquad
z_c=1/2,
\qquad
\Gamma_{\rm crit}=\ln2.
\]

This is pure critical-route degeneracy despite unit edge tie multiplicities.

## 6. Irrational correction is genuinely necessary

Consider

\[
K=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]

Every edge lies on a critical directed cycle in a realizable dominant-weight graph: the state-0 self-loop and the 2-cycle can both have the same maximum cycle mean.

Then

\[
p_K(z)=1-z-z^2.
\]

Its smallest positive root is

\[
z_c=\frac{\sqrt5-1}{2},
\]

and

\[
\rho(K)=\frac{1+\sqrt5}{2}=\varphi.
\]

Thus

\[
\Gamma_{\rm crit}=\ln\varphi
\]

is not a rational-log input. Any Foundation interface that forces the correction into rational `LN` would be false/incomplete.

The correct exact state is the integer polynomial plus its smallest-positive-root selector (optionally with a rational isolating interval).

## 7. Zero-correction structural law

Because `K` is a critical graph, every nonzero edge belongs to a directed cycle. Consequently there are no edges between distinct SCCs; after permutation, `K` is block diagonal over recurrent irreducible SCCs.

For one irreducible non-negative integer block `A`, every row sum is at least one. Therefore

\[
A\mathbf1\ge\mathbf1.
\]

If any row sum is strictly greater than one, irreducibility and Perron--Frobenius strictness give

\[
\rho(A)>1.
\]

Hence `rho(A)=1` iff every row sum is exactly one. Since entries are non-negative integers, every row then contains exactly one `1`; irreducibility forces the support to be one directed simple cycle.

Therefore:

### Candidate BRC-CL1

\[
\boxed{
\Gamma_{\rm crit}=0
\iff
\text{every critical SCC is a unit-multiplicity directed simple cycle.}
}
\]

Equivalently, the correction is strictly positive iff the critical graph has either:

- a dominant parallel tie `d_ij>1`; or
- critical route branching inside some SCC.

## 8. Exact inequalities without root materialization

The selector also supports exact comparison against rational thresholds `q>0` through Sturm root counts / polynomial signs and rational interval refinement.

Thus questions such as

\[
\Gamma_{\rm crit}<\ln R
\]

can be reduced to

\[
\rho(K)<R
\iff
z_c>1/R
\]

and certified by exact root-count placement, without materializing `rho(K)`.

This is consistent with the existing Enterprise policy: semantic algebraic roots may be located/order-compared exactly before any optional numerical readout.

## 9. Boundaries

Freeze:

```text
CRITICAL_LOG_CORRECTION = -LN(SMALLEST_POSITIVE_ROOT(det(I-zK)))
INTEGER_CRITICALITY_POLYNOMIAL = EXACT_STATE
ALGEBRAIC_ROOT_SELECTOR != FLOATING_EIGENVALUE
RATIONAL_SELECTED_ROOT -> EXISTING_DIV_LN_RUNTIME
IRRATIONAL_SELECTED_ROOT -> KEEP_SYMBOLIC_OR_ISOLATED
GENERAL_ALGEBRAIC_LN_MATERIALIZATION = NOT_PROMOTED
ZERO_CORRECTION <=> UNIT_SIMPLE_CYCLE_CRITICAL_COMPONENTS
```

Generic Sturm root isolation, rational-root theorem, Perron-Frobenius and algebraic-number representations are classical prior art.

## 10. Validation plan

1. Implement exact `p_K(z)=det(I-zK)` coefficient construction for small non-negative integer `K`.
2. Implement exact rational-root extraction using the constant-term-one restriction.
3. Implement Fraction-only polynomial gcd/Sturm sequence and isolate the smallest remaining irrational root in `(0,1)`.
4. Exhaust all `2x2` and `3x3` matrices with entries in `{0,1,2}` whose every positive edge lies on a directed cycle; verify:
   - a smallest positive selector exists;
   - selector is rational or has exact unique isolating interval;
   - zero-correction structural criterion matches `z_c=1`;
   - if the structural criterion fails then the selector lies strictly below 1.
5. Check special forms:
   - simple cycle: `1-D z^r`;
   - all-ones `2x2`: `1-2z`;
   - golden-ratio matrix: `1-z-z^2`, irrational selector isolated inside a rational interval such as `(3/5,5/8)`.
6. Rebuild critical-degeneracy matrices from selected #1167 examples and verify their correction polynomial/selectors agree with the known rational bracket targets.
