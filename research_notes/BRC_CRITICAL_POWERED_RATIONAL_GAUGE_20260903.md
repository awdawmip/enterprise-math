# BRC Critical Powered Rational Gauge and Prime-Valuation Flattening

Status: `RESEARCH CANDIDATE / MAIN-BACKED PARENTS / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCPRG-20260903`
Parents: `WBRC-T22` rational prime-valuation gauge, `WBRC-T36/T38` exact histogram/leading pair, and `WBRC-T39` critical-degeneracy matrix.

## 1. Scope and prior-art boundary

Max-algebra diagonal scaling/visualization, critical graphs and max-plus eigenvectors are classical/general mathematics. No generic novelty claim is made.

The BRC-specific goal is to show that for **positive rational dominant branch weights**, the critical-layer normalization can be certified entirely with rational powered data and exact prime valuations. No algebraic `mu`, fractional-power gauge, floating logarithm or eigenvector is required in the proof carrier.

## 2. Critical data

Let `a_uv` be the largest explicit branch weight in cell `u->v`, and let the tropical critical graph be the union of all simple cycles with maximum geometric mean.

Choose one reference critical cycle `C0` of length

\[
r_0=|C_0|
\]

and rational dominant product

\[
Q_0=\prod_{e\in C_0}a_e.
\]

The formal critical mean is

\[
\mu=Q_0^{1/r_0},
\]

but `mu` is **not** required as an exact runtime value.

For every other critical cycle `C`, main-backed root-free criticality gives

\[
\boxed{Q_C^{r_0}=Q_0^{|C|}.}
\]

## 3. Rational powered gauge certificate

Fix one root vertex in each critical SCC and normalize

\[
H_{root}=1.
\]

### Candidate PRG1

There is a unique positive rational value `H_v` on every vertex of that SCC such that each critical edge `u->v` satisfies

\[
\boxed{a_{uv}^{r_0}H_v=Q_0H_u.}
\]

Equivalently,

\[
\boxed{\frac{H_v}{H_u}=\frac{Q_0}{a_{uv}^{r_0}}.}
\]

Existence is obtained by multiplying these rational ratios along a directed path from the root. Path independence follows because around every critical cycle

\[
\prod_{e\in C}\frac{Q_0}{a_e^{r_0}}
=
\frac{Q_0^{|C|}}{Q_C^{r_0}}
=1.
\]

Uniqueness follows from strong connectivity and the root normalization.

Thus the entire normalization certificate lies in `Q_{>0}`.

## 4. Formal radical interpretation

Only after the rational certificate is frozen, one may formally write

\[
h_v=H_v^{1/r_0},
\qquad
\mu=Q_0^{1/r_0}.
\]

Then the powered equation becomes

\[
\boxed{a_{uv}\frac{h_v}{h_u}=\mu}
\]

on every critical edge.

The `h_v` need not be rational. This is interpretation, not the proof carrier.

## 5. Prime-valuation flattening

Apply the exact rational prime valuation map `nu_p=v_p` from `WBRC-T22`.

Define the finite-support rational valuation vectors

\[
\lambda_p=\frac{v_p(Q_0)}{r_0},
\qquad
 g_{v,p}=\frac{v_p(H_v)}{r_0}.
\]

Then every critical edge satisfies

\[
\boxed{
v_p(a_{uv})+g_{v,p}-g_{u,p}=\lambda_p
}
\]

for every prime `p`.

Hence the dominant-weight valuation 1-cochain on each critical SCC is

\[
\boxed{\nu(a)=\lambda+\delta(-g),}
\]

that is, a constant mean valuation plus an exact rational coboundary.

This is the prime-valuation/cohomological form of critical max normalization.

Moreover `r_0 g_v=nu(H_v)` is integral in every prime coordinate, so the fractional valuation gauge has denominator dividing `r_0` and is certified by the rational `H_v`.

## 6. Rational realization on moment subsequences

Let

\[
m=r_0s.
\]

Then `H_v^s` and `Q_0^s` are rational. Apply the ordinary rational diagonal gauge with state factors `H_v^s` to the moment matrix `W^(m)`, and divide by `Q_0^s`.

For a critical edge `u->v`:

\[
\begin{aligned}
Q_0^{-s}\frac{H_v^s}{H_u^s}W_{uv}^{(m)}
&=\frac{W_{uv}^{(m)}}{a_{uv}^m}\\
&=\sum_{\alpha:u\to v}\left(\frac{q_\alpha}{a_{uv}}\right)^m.
\end{aligned}
\]

If `d_uv` branches attain the maximum `a_uv`, then

\[
\boxed{
R^{(m)}_{uv}
:=
\frac{W_{uv}^{(m)}}{a_{uv}^m}
=
d_{uv}+
\sum_{q_\alpha<a_{uv}}
\left(\frac{q_\alpha}{a_{uv}}\right)^m.
}
\]

Therefore

\[
\boxed{R^{(m)}_{uv}\to d_{uv}=K_{uv}}
\]

entrywise on the critical graph.

The key point is that the realized residual entry is itself rational and can be computed directly as a cell moment ratio, even if `mu` and the unpowered gauge are algebraic.

## 7. Exact entrywise gap

If a critical cell has subdominant branches, define

\[
\theta_{uv}
=
\max_{q<a_{uv}}\frac q{a_{uv}}<1,
\qquad
c_{uv}=C_{uv}-d_{uv}.
\]

Then for every integer `m>=0`,

\[
\boxed{
0\le R^{(m)}_{uv}-d_{uv}
\le c_{uv}\theta_{uv}^m.
}
\]

If no subdominant branch exists, the equality `R^(m)_uv=d_uv` holds for every `m`.

Let

\[
\theta_*=\max_{critical\ cells}\theta_{uv}<1
\]

with zero for cells having no subdominant branch, and

\[
c_*=\max c_{uv}.
\]

Then the critical-edge max-entry error satisfies

\[
\boxed{
\|R^{(m)}-K\|_{\max}\le c_*\theta_*^m.
}
\]

This is a local branch-gap certificate complementary to the global characteristic gap `WBRC-T40`.

## 8. Gauge covariance and residual invariance

Apply an ordinary positive rational vertex gauge `r_v` to the original explicit branch weights:

\[
q'_{uv,\alpha}=q_{uv,\alpha}\frac{r_v}{r_u}.
\]

Critical cycles, critical edges and tie multiplicities remain unchanged. With root `o` fixed in one critical SCC, the powered certificate transforms as

\[
\boxed{
H'_v
=H_v\left(\frac{r_o}{r_v}\right)^{r_0}.
}
\]

This preserves `H'_o=1` and the powered edge equations.

More importantly,

\[
\boxed{
\frac{W_{uv}^{\prime(m)}}{(a'_{uv})^m}
=
\frac{W_{uv}^{(m)}}{a_{uv}^m},
}
\]

so the entire critical residual family `R^(m)` is exactly rational-gauge invariant.

## 9. Relation to existing Foundation layers

The hierarchy becomes

```text
explicit rational histogram
-> dominant cell data (a_uv,d_uv)
-> root-free tropical critical graph
-> rational powered gauge H_v
-> fractional prime-valuation flat form (lambda,g_v)
-> rational critical residual matrix R^(m)
-> K as m->infinity
-> p_K/root selector/Gamma_crit
```

This gives an exact bridge between:

- `WBRC-T22`: rational prime-valuation gauge coordinates;
- `WBRC-T38`: dominant tie multiplicity;
- `WBRC-T39`: critical-degeneracy matrix;
- `WBRC-T41/T42`: exact critical log correction.

## 10. Boundaries

Freeze:

```text
POWERED_CRITICAL_GAUGE_H_v IN Q_{>0}
FORMAL_UNPOWERED_GAUGE_h_v MAY_BE_ALGEBRAIC
CRITICAL_MEAN_mu MAY_BE_ALGEBRAIC
PROOF_CERTIFICATE DOES_NOT_REQUIRE_mu_OR_h_v_MATERIALIZATION
PRIME_VALUATION_GAUGE_COORDINATES g_v IN direct_sum_p Q
MOMENT_SUBSEQUENCE_m_MULTIPLE_OF_r0 -> ORDINARY_RATIONAL_GAUGE_REALIZATION
CRITICAL_RESIDUAL_R_m = CELL_MOMENT_RATIO
R_m -> K ENTRYWISE
LOCAL_BRANCH_GAP != GLOBAL_CHARACTERISTIC_GAP
```

No generic novelty claim is made for max-algebra visualization scaling. No general radical arithmetic engine, algebraic matrix runtime, noncritical full-matrix entrywise normalization, signed/amplitude or infinite-state extension is claimed.

## 11. Validation plan

1. Reuse the exact `2x2`/`3x3` branch catalogs from PR #1167.
2. For every cyclic sample, construct the critical graph, choose one root per critical SCC and solve rational `H_v` by path propagation.
3. Verify every critical edge equation `a_uv^r0 H_v=Q0 H_u` and path-independence.
4. Factor `Q0`, `H_v`, and critical `a_uv` into prime valuations and verify `v_p(a)+g_v-g_u=lambda_p` exactly for every appearing prime.
5. For `m=r0,2r0,3r0`, verify the rational powered-gauge expression equals the direct cell ratio `W^(m)_uv/a_uv^m` and obeys the exact branch-gap bound.
6. On nonuniform rational gauge transforms, verify covariance of `H_v` and exact invariance of every tested `R^(m)_uv`.
7. Verify unique-cycle, branching, multiple-critical-class and algebraic-mean examples, including cases where the formal `mu` is irrational but all powered certificates remain rational.
