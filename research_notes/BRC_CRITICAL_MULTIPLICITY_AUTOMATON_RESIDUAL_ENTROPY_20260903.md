# BRC Critical Multiplicity Automaton and Residual Dominant-Path Entropy

Status: `RESEARCH CANDIDATE / MAIN-BACKED PARENTS / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCCENT-20260903`
Parents: PR #1167 (`critical-degeneracy matrix`) and PR #1168 (`exact critical-log selector`)

## 1. Scope and prior-art boundary

For a finite explicit positive-rational branch system, the main-backed large-moment result constructs the non-negative integer critical-degeneracy matrix

\[
K_{ij}=d_{ij}
\]

on tropical critical edges and zero elsewhere, and proves

\[
\frac{\rho(W^{(m)})}{\mu^m}\to\rho(K).
\]

Perron growth of non-negative integer matrices, topological entropy of finite directed graphs/shifts of finite type, determinant zeta identities and thermodynamic/zero-temperature language are classical/general mathematics. No generic novelty claim is made.

The BRC-specific content here is the exact interpretation of `K` as a **critical dominant-branch multiplicity automaton**, connecting finite dominant tie multiplicity, recurrent critical-route branching, rational gauge invariance and the exact critical-log root selector.

## 2. Expanded critical multigraph

Replace every positive entry `K_ij=d` by exactly `d` parallel directed branch symbols from state `i` to state `j`.

Call the resulting finite directed multigraph

\[
\mathcal C_{\rm mult}.
\]

Then ordinary matrix multiplication gives, exactly,

\[
\boxed{
(K^n)_{ij}
=
\#\{\text{length-n critical dominant branch words }i\to j\}.
}
\]

Let

\[
B_n=\sum_{i,j}(K^n)_{ij}.
\]

Since a critical graph has a directed cycle, `B_n>0` for every `n>=0`.

By the classical finite-matrix growth formula,

\[
\boxed{
\lim_{n\to\infty}B_n^{1/n}=\rho(K),
}
\]

hence

\[
\boxed{
\Gamma_{\rm crit}
=
\ln\rho(K)
=
\lim_{n\to\infty}\frac1n\ln B_n.
}
\]

Thus `Gamma_crit` is the exponential multiplicity growth rate of recurrent paths that remain on the tropical critical layer while resolving every exact dominant tie as a distinct BRC alternative.

## 3. Unification of earlier `ln k` laws

### One recoalescence

For `d` equal dominant alternatives at one branch event,

\[
\ln d
\]

is the finite dominant-degeneracy surplus from `Lead(H)=(M,d)`.

### One critical circuit

For one critical simple cycle of length `r` with edge tie multiplicities `d_e`, let

\[
D=\prod_{e\in C}d_e.
\]

One full circuit multiplies the number of strongest branch words by `D`, so

\[
\boxed{
\Gamma_{\rm crit}=\frac1r\ln D.
}
\]

### General critical multigraph

When critical circuits overlap/branch, one cycle product is no longer complete. The correct multiplicity growth is

\[
\boxed{
\Gamma_{\rm crit}=\ln\rho(K).
}
\]

Even if every critical edge has `d_ij=1`, critical route branching can make `rho(K)>1`; for `K=ones(2x2)`, `Gamma_crit=ln 2`.

Therefore the exact hierarchy is

\[
\boxed{
\ln d
\longrightarrow
\frac1r\ln D
\longrightarrow
\ln\rho(K).
}
\]

## 4. Double-limit moment/free-energy form

For explicit branch moment matrix `W^(m)`, define the total length-n m-th path mass

\[
Z_{m,n}=\sum_{i,j}(W^{(m)n})_{ij}
=\sum_{|p|=n}w(p)^m.
\]

For each fixed `m` in a recurrent finite system, classical finite-matrix norm growth gives

\[
\lim_{n\to\infty}\frac1n\ln Z_{m,n}
=\ln\rho(W^{(m)}).
\]

Combining with the main-backed critical-degeneracy asymptotic yields

\[
\boxed{
\Gamma_{\rm crit}
=
\lim_{m\to\infty}
\left(
\lim_{n\to\infty}\frac1n\ln Z_{m,n}
-m\ln\mu
\right).
}
\]

So `Gamma_crit` is the exact residual exponential branch multiplicity after subtracting the tropical maximum-weight growth.

This resembles zero-temperature/residual entropy in classical thermodynamic formalism; the project claim is only the typed BRC specialization.

## 5. Critical multiplicity zeta

Define the formal critical multiplicity zeta

\[
\boxed{
Z_{\rm crit}(z)=\frac1{\det(I-zK)}.
}
\]

Its formal log expansion is

\[
\boxed{
\ln Z_{\rm crit}(z)
=
\sum_{n\ge1}\frac{\operatorname{tr}(K^n)}n z^n.
}
\]

Here `tr(K^n)` counts based closed length-n critical dominant branch words.

The smallest positive singularity/root is

\[
z_c=1/\rho(K),
\]

so

\[
\boxed{
\Gamma_{\rm crit}=-\ln z_c.
}
\]

This identifies the PR #1168 exact root selector with the radius/critical point of the critical multiplicity automaton.

## 6. Exact rational gauge invariance

Apply any positive rational vertex gauge

\[
q'_{ij,\alpha}=q_{ij,\alpha}\frac{h_j}{h_i}.
\]

For every ordered state pair, all parallel branch weights receive the same factor. Therefore:

- the dominant branch set in that cell is unchanged;
- `d_ij` is unchanged;
- every simple-cycle dominant product telescopes and is unchanged;
- the set of critical cycles and critical edges is unchanged.

Hence

\[
\boxed{K'=K}
\]

exactly, not merely up to similarity. Consequently

\[
p_{K'}=p_K,
\qquad
z_c'=z_c,
\qquad
\Gamma_{\rm crit}'=\Gamma_{\rm crit}.
\]

Thus the critical multiplicity automaton is already a gauge-quotiented integer observable of the explicit rational histogram system.

## 7. Zero law as absence of exponential multiplicity

For critical-graph-shaped integer `K`, the main-backed zero law says

\[
\Gamma_{\rm crit}=0
\]

iff every nonzero critical SCC is a unit-multiplicity directed simple cycle.

In automaton language this is equivalent to

\[
\boxed{
B_n\text{ is bounded in }n.
}
\]

Indeed in the zero case `K` is a permutation matrix on recurrent states (plus isolated zero states), so `B_n` is constant. Otherwise `rho(K)>1` and `B_n` grows exponentially.

## 8. Exact formal recurrence

Because `K` is finite integer, every entry of `K^n`, `B_n`, and `tr(K^n)` satisfies the integer linear recurrence induced by the characteristic polynomial of `K`.

Equivalently, the path-count generating matrix

\[
(I-zK)^{-1}
\]

and scalar generating series

\[
\sum_{n\ge0}B_n z^n
=\mathbf 1^T(I-zK)^{-1}\mathbf 1
\]

are exact rational functions with integer polynomial denominator dividing `det(I-zK)`.

Thus infinite critical dominant-path multiplicity is retained by finite exact recurrence data.

## 9. Boundaries

Freeze:

```text
CRITICAL_MULTIPLICITY_AUTOMATON = INTEGER_K
CRITICAL_WORD_COUNT_n = SUM_ENTRIES(K^n)
CRITICAL_RESIDUAL_ENTROPY = LN(RHO(K))
CRITICAL_RESIDUAL_ENTROPY = -LN(SMALLEST_POSITIVE_ROOT(det(I-zK)))
RATIONAL_VERTEX_GAUGE -> K_INVARIANT_EXACTLY
FINITE_ln_d -> UNIQUE_CIRCUIT_(ln D)/r -> GENERAL_ln rho(K)
TOPOLOGICAL_ENTROPY_LANGUAGE = CLASSICAL_INTERPRETATION
CRITICAL_RESIDUAL_ENTROPY != SHANNON_ENTROPY_CLAIM
```

This result does not recover labeled semantic provenance, signed/amplitude phases, or noncritical lower-weight path structure.

## 10. Validation plan

1. Exhaust `2x2` and `3x3` critical-graph-shaped matrices with entries `{0,1,2}` and verify matrix powers equal direct multigraph word enumeration for small lengths.
2. Verify zero-law structures have constant `B_n` and every nonzero-correction structure violates boundedness witnesses.
3. Verify Cayley-Hamilton recurrence for `B_n` and `tr(K^n)` exactly.
4. Verify the formal logarithmic derivative identity
   `-z p'(z)/p(z)=sum_{n>=1} tr(K^n) z^n` coefficientwise.
5. On explicit positive-rational branch graphs, apply several nonuniform rational vertex gauges and verify dominant ties, critical cycles and `K` are unchanged exactly.
6. Verify one-cycle, `ones(2x2)`, disjoint-class and golden-ratio critical examples recover the expected automaton interpretation.
