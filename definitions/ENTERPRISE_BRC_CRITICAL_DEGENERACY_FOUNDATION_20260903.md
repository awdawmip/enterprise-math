# Enterprise Math — Critical-Degeneracy BRC Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION ADDENDUM / MAIN-BACKED / FINITE-EXPLICIT-POSITIVE-RATIONAL`
Effective: `2026-09-03`
Parent: `ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md`
Theorem ledger: `ENTERPRISE_BRC_CRITICAL_DEGENERACY_THEOREM_LEDGER_20260903.json`

## 1. Purpose and prior-art boundary

This addendum freezes the exact BRC specialization of large-integer-moment recurrent asymptotics and its exact subleading log carrier from PRs #1166–#1168.

Maximum-cycle-mean spectral asymptotics, max-plus critical graphs, Perron--Frobenius perturbation, Sturm isolation and algebraic-root representations are classical/general mathematics. Enterprise Math claims the typed connection to the exact positive-rational histogram dominant multiplicities, the integer certificate surface, and the reusable BRC routing interface.

## 2. Dominant critical graph and degeneracy matrix

For each supported state edge `i->j`, let

\[
a_{ij}=\max\{q_e:e:i\to j\},
\qquad
 d_{ij}=\#\{e:i\to j:q_e=a_{ij}\}.
\]

For a simple state cycle `C`, define

\[
Q_C=\prod_{e\in C}a_e,
\qquad
\mu_C=Q_C^{1/|C|}.
\]

Let

\[
\mu=\max_C\mu_C.
\]

The critical graph is the union of simple cycles attaining `mu`. Define the non-negative integer matrix

\[
\boxed{
K_{ij}=\begin{cases}
d_{ij},&i\to j\text{ belongs to the critical graph},\\
0,&\text{otherwise}.
\end{cases}}
\]

Choose any reference critical cycle `C_0` of length `r_0` and product `Q_0`. Then exact classification is root-free:

\[
Q_C^{r_0}=Q_0^{|C|}
\]

for critical cycles and `<` for subcritical cycles.

## 3. Critical-degeneracy moment asymptotic

For the explicit branch moment matrix

\[
(W^{(m)})_{ij}=\sum_{e:i\to j}q_e^m,
\]

write

\[
p_m(\lambda)=\det(\lambda I-W^{(m)}).
\]

Every characteristic coefficient is a finite exact sum

\[
\sum_bc_bb^m,
\]

with rational bases and integer coefficients. A term occupying `k` cycle-system vertices obeys

\[
b^{r_0}\le Q_0^k.
\]

Equality terms are precisely dominant branch choices of critical cycle systems, and their multiplicities reproduce the determinant cycle expansion of `K`.

Therefore

\[
\boxed{
\mu^{-mn}p_m(\mu^m t)\longrightarrow\det(tI-K)
}
\]

coefficientwise, and

\[
\boxed{
\rho(W^{(m)})/\mu^m\longrightarrow\rho(K).
}
\]

Derived logarithmic readout:

\[
\boxed{
\ln\rho(W^{(m)})=m\ln\mu+\ln\rho(K)+o(1).
}
\]

Canonical ID: `WBRC-T39`.

## 4. Exact strict gap and rate

For every strict characteristic base `b` occupying `k` vertices define

\[
\eta_b=\frac{b^{r_0}}{Q_0^k}<1.
\]

There are finitely many such bases, so

\[
\boxed{\eta=\max_b\eta_b<1}
\]

is an exact rational certificate.

On moment orders `m=r_0s`, every normalized characteristic coefficient has an exact finite bound by an integer coefficient constant times `eta^s`; hence coefficient convergence is exponentially fast. If the Perron root of `K` is simple, ordinary finite polynomial root perturbation yields

\[
\rho(W^{(m)})/\mu^m
=
\rho(K)+O(\eta^{m/r_0}).
\]

Canonical ID: `WBRC-T40`.

## 5. Important special cases

### 5.1 Unique critical simple cycle

If the critical graph is one simple cycle of length `r` and

\[
D=\prod_{e\in C}d_e,
\]

then

\[
\rho(K)=D^{1/r},
\]

so

\[
\rho(W^{(m)})^r/Q^m\to D.
\]

This is the merged PR #1166 result.

### 5.2 Branching critical graph

Critical route branching contributes even without parallel edge ties. For

\[
K=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

all edge tie multiplicities equal one, but

\[
\rho(K)=2.
\]

Thus the subleading correction is `ln 2` from critical route growth.

### 5.3 Several critical classes

After critical SCC permutation, `K` is block diagonal and

\[
\rho(K)=\max_\alpha\rho(K_\alpha).
\]

The subleading winning class is the one with largest critical combinatorial growth.

## 6. Exact criticality polynomial and root selector

Define

\[
\boxed{p_K(z)=\det(I-zK)\in\mathbb Z[z]}.
\]

By the existing recurrent criticality-polynomial theorem `WBRC-T21`, the smallest positive root satisfies

\[
\boxed{z_c(K)=1/\rho(K)}.
\]

Hence the exact subleading log correction is

\[
\boxed{\Gamma_{\rm crit}=-\ln z_c(K)}.
\]

The exact state stores:

```text
p_K(z) in Z[z]
selector = SMALLEST_POSITIVE_REAL_ROOT
exact rational root, if present
otherwise a rational isolating interval
```

Since `p_K(0)=1`, every positive rational root has the form `1/q`, so rational roots are completely enumerable by the rational-root theorem before Sturm isolation of the irrational factor.

Canonical ID: `WBRC-T41`.

## 7. Zero law, threshold queries and finite readout

Since every positive critical edge lies on a directed cycle, `K` decomposes into recurrent SCC blocks.

For an irreducible non-negative integer block `A`, `A 1 >= 1`. If any row sum exceeds one, Perron strictness gives `rho(A)>1`. Therefore

\[
\boxed{
\Gamma_{\rm crit}=0
\iff
\text{every nonzero critical SCC is a unit-multiplicity directed simple cycle.}
}
\]

For a rational threshold `R>0`,

\[
\Gamma_{\rm crit}<\ln R
\iff
\rho(K)<R
\iff
\rho(K/R)<1.
\]

Thus the existing exact finite-recurrent stable certificate can answer rational threshold questions without materializing the algebraic root.

If an irrational selected root has a rational enclosure

\[
0<a<z_c<b\le1,
\]

then

\[
\boxed{
\ln(1/b)<\Gamma_{\rm crit}<\ln(1/a).
}
\]

Both bounds are existing rational BRC `LN` inputs and can be refined arbitrarily by further Sturm isolation.

If `z_c=a/b` is rational, the correction is exactly

\[
\ln(b/a).
\]

For a unique critical `r`-cycle with degeneracy product `D`,

\[
\Gamma_{\rm crit}=\frac1r\ln D.
\]

Canonical ID: `WBRC-T42`.

## 8. Irrational correction boundary

For

\[
K=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\]

\[
p_K(z)=1-z-z^2
\]

and

\[
\rho(K)=\varphi.
\]

Therefore `ln(phi)` is a genuine exact BRC critical correction. It must remain an algebraic-root selector or rational-log interval state; it cannot be forced into the rational `LN` argument type.

## 9. Hard boundaries

Freeze:

```text
LEADING_TROPICAL_EXPONENT = CLASSICAL_MAX_CYCLE_MEAN
BRC_SUBLEADING_CRITICAL_CORRECTION = RHO(CRITICAL_DEGENERACY_MATRIX)
ONE_CRITICAL_CYCLE_D_PRODUCT != GENERAL_MULTI_CRITICAL_CORRECTION
FLOATING_EIGENVALUE_OR_ROOT != EXACT_ENTERPRISE_CERTIFICATE
CRITICAL_LOG_EXACT_STATE = INTEGER_POLYNOMIAL + ROOT_SELECTOR
RATIONAL_ROOT -> EXISTING_DIV_LN
IRRATIONAL_ROOT -> SYMBOLIC_SELECTOR + RATIONAL_LN_BOUNDS
GENERAL_ALGEBRAIC_LN_MATERIALIZER = NOT_PROMOTED
TOTAL_MASS_ONLY != CRITICAL_DEGENERACY_COMPLETE
```

Canonical negative IDs: `WBRC-N19..N22`.

## 10. Tool routing

Reusable T0 subtool:

`t0.weighted_brc_critical_degeneracy` -> `src/enterprise_math/brc_critical_degeneracy.py`.

The tool is an exact reference implementation and uses finite simple-cycle enumeration/root isolation. It is not a runtime-complexity speedup claim and does not create a new top-level spectral tool family.
