# BRC Critical-Degeneracy Matrix Large-Moment Asymptotic

Status: `RESEARCH CANDIDATE / EXACT FINITE EXPLICIT POSITIVE-RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parents: `WBRC-T33`, `WBRC-T36..T38`, merged PR #1166

## 1. Purpose and prior-art boundary

The classical large-moment / low-temperature leading law says that for the positive moment matrices

\[
(W_m)_{ij}=\sum_{e:i\to j}q_e^m
\]

the Perron exponent is governed by the maximum cycle geometric mean of the entrywise dominant-weight graph. Max-plus critical graphs/classes and refined Perron asymptotics in semifields of jets are classical (Akian--Bapat--Gaubert and related min/max-plus perturbation theory).

This note records the exact Enterprise/BRC specialization of the **subleading positive coefficient** to the Foundation exact-weight histogram carrier: the coefficient data are the dominant tie multiplicities already stored by `Lead=(M,d)`.

No generic max-plus, Puiseux/WKB, Perron perturbation or leading-coefficient novelty claim is made.

## 2. Dominant edge data

For each supported state edge `i->j`, define

\[
a_{ij}=\max\{q_e:e:i\to j\}>0,
\qquad
 d_{ij}=\#\{e:i\to j:q_e=a_{ij}\}.
\]

For every directed simple state cycle `C`, set

\[
Q_C=\prod_{(i,j)\in C}a_{ij},
\qquad
\mu_C=Q_C^{1/|C|}.
\]

Assume at least one state cycle exists and define the tropical/max-times cycle value

\[
\mu=\max_C\mu_C>0.
\]

A simple cycle is **critical** when its mean equals `mu`. The critical graph `G_c` is the union of all state edges belonging to at least one critical simple cycle.

For an exact root-free certificate, choose any reference critical cycle `C_0` of length `r_0` and product `Q_0`. Then a simple cycle `C` is critical exactly when

\[
\boxed{Q_C^{r_0}=Q_0^{|C|}},
\]

and is subcritical exactly when

\[
\boxed{Q_C^{r_0}<Q_0^{|C|}}.
\]

All comparisons are rational/integer-power comparisons.

## 3. Critical degeneracy matrix

Define the non-negative integer matrix

\[
\boxed{
K_{ij}=
\begin{cases}
 d_{ij},& (i,j)\in G_c,\\
 0,&\text{otherwise}.
\end{cases}}
\]

`K` forgets the absolute dominant rational weights and keeps only the tie multiplicities on the tropical critical graph.

A standard max-plus critical-graph fact is that every directed cycle entirely contained in `G_c` is itself critical. Equivalently, after a max-times eigenvector gauge, every critical edge is tight and multiplying tight equalities around any critical-graph cycle gives product `mu^length`.

This fact is used only as classical structural prior art; the exact checker below re-verifies it on the complete finite regression families.

## 4. Characteristic coefficient exponential sums

Write

\[
p_m(\lambda)=\det(\lambda I-W_m).
\]

As in PR #1166, expanding both the directed determinant cycle systems and every explicit parallel branch yields exact finite expressions

\[
\boxed{a_{k,m}=\sum_{b\in B_k}c_{k,b}b^m},
\]

where `a_{k,m}` is the coefficient multiplying `lambda^(n-k)`, every base `b` is positive rational, and every `c_{k,b}` is integer.

Choose the reference critical cycle `(r_0,Q_0)`. Every explicit branch-selected cycle-system base occupying `k` vertices satisfies

\[
\boxed{b^{r_0}\le Q_0^k}.
\]

Equality holds exactly when every selected branch is dominant on its cell and every constituent state cycle is critical.

Thus the non-decaying characteristic terms are precisely the dominant branch selections of cycle systems in the critical graph.

## 5. Limit polynomial equals the critical degeneracy characteristic polynomial

A cycle-system term of `K` contributes the product of `d_ij` over its selected critical edges. This integer product is exactly the number of ways to select one dominant explicit branch on every edge of the same critical state cycle system.

Therefore the equality-base terms of the normalized characteristic polynomial reproduce the full determinant cycle expansion of `K` coefficient by coefficient.

### Candidate BRC-CD1

\[
\boxed{
\mu^{-mn}p_m(\mu^m t)
\longrightarrow
\det(tI-K)
}
\]

coefficientwise as `m->infinity`.

The statement is independent of the particular algebraic representation of `mu`; its certificate surface is the root-free rational cycle equalities/inequalities above.

## 6. Perron correction

Polynomial root continuity gives convergence of the normalized eigenvalue multisets. Since `W_m` and `K` are non-negative matrices, their spectral radii are Perron roots.

Hence:

### Candidate BRC-CD2

\[
\boxed{
\frac{\rho(W^{(m)})}{\mu^m}
\longrightarrow
\rho(K).
}
\]

Derived logarithmic readout:

\[
\boxed{
\ln\rho(W^{(m)})
=
 m\ln\mu+\ln\rho(K)+o(1).
}
\]

The first term is classical tropical growth. The second term is the exact recurrent combinatorial-degeneracy correction supplied by the BRC histogram leading coefficients.

## 7. Recovery of earlier cases

### 7.1 Unique critical simple cycle

If the critical graph is one simple cycle of length `r`, `K` is a weighted cycle with edge entries `d_e`. Therefore

\[
\rho(K)=\left(\prod_{e\in C}d_e\right)^{1/r}=D^{1/r},
\]

recovering PR #1166:

\[
\rho(W^{(m)})^r/Q^m\to D.
\]

### 7.2 One state

If the largest loop weight occurs `d` times,

\[
K=[d],
\]

so the correction is exactly `d` and the log correction is `ln d`.

### 7.3 Several disjoint critical classes

If critical classes are disjoint blocks, `K` is block upper-triangular after state permutation and

\[
\rho(K)=\max_\alpha\rho(K_\alpha).
\]

Thus the dominant subleading critical class is selected by its combinatorial degeneracy growth.

### 7.4 Critical branching with unit edge degeneracy

Even if every critical cell has `d_ij=1`, a branching critical graph can have

\[
\rho(K)>1.
\]

Hence the subleading log correction is not merely a sum of parallel-edge `ln d_ij`; it can also arise from exponentially many **critical state-route choices**.

For example, if all four edges of a two-state complete critical graph have one dominant branch, then

\[
K=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
\rho(K)=2.
\]

Every individual critical simple cycle has multiplicity product 1, yet the recurrent critical graph has correction `ln 2`.

## 8. Exact gap and convergence-rate surface

For a characteristic exponential base `b` occupying `k` vertices that is not critical-surviving, define

\[
\eta_b=\frac{b^{r_0}}{Q_0^k}<1.
\]

Because there are finitely many characteristic bases,

\[
\boxed{\eta=\max\eta_b<1}
\]

is an exact rational gap certificate.

For moment orders that are multiples of `r_0`, every normalized characteristic coefficient differs from its `det(tI-K)` limit by an explicitly bounded integer coefficient sum times `eta^(m/r_0)`. In general the coefficient error is `O(eta^(m/r_0))`.

When the Perron root of `K` is simple, ordinary polynomial-root perturbation yields the sharper scalar rate

\[
\frac{\rho(W^{(m)})}{\mu^m}
=
\rho(K)+O(\eta^{m/r_0}).
\]

No simple-root rate is claimed when the limiting Perron root is multiple.

## 9. Hard boundaries

Freeze:

```text
LEADING_TROPICAL_EXPONENT = CLASSICAL_MAX_CYCLE_MEAN
BRC_SUBLEADING_CRITICAL_CORRECTION = RHO(CRITICAL_DEGENERACY_MATRIX)
UNIQUE_CRITICAL_CYCLE_CORRECTION = SPECIAL_CASE
ONE_CYCLE_DEGENERACY_PRODUCT != GENERAL_MULTI_CRITICAL_CORRECTION
CRITICAL_EDGE_PARALLEL_DEGENERACY != COMPLETE_CRITICAL_ROUTE_DEGENERACY
FLOATING_EIGENSOLVER != EXACT_CERTIFICATE
```

`K` is defined from explicit positive-rational branch histograms. Aggregated total-mass matrices generally do not retain the `d_ij` data required to reconstruct it.

## 10. Validation plan

1. Exhaust small 2-state multigraphs with parallel dominant alternatives and all 3-state support/weight assignments from a small exact rational alphabet.
2. Classify critical cycles using only exact rational power comparisons.
3. Build `G_c` and verify every simple cycle of `G_c` is critical in all regression samples.
4. Build exact characteristic exponential-base dictionaries for `W_m`.
5. For each coefficient, verify `b^r0<=Q0^k`; sum coefficients of equality bases and compare exactly with the corresponding coefficient of `det(tI-K)`.
6. Verify exact exponential gap bounds on moment orders divisible by `r_0`.
7. Add exact Perron sign brackets for examples with rational `mu` and rational `rho(K)`, including:
   - disjoint critical classes;
   - a genuinely branching critical graph with `rho(K)>1` despite all `d_ij=1`;
   - nonuniform critical edge weights where individual normalized entries do not converge but the characteristic/Perron correction does.
