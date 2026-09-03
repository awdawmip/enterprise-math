# BRC Critical Ratio Histogram and Finite Rational Exponential Jet

Status: `RESEARCH CANDIDATE / MAIN-BACKED PARENTS / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCRJET-20260903`
Parents: universal histogram `WBRC-T36/T38`, critical-degeneracy `WBRC-T39..T42`, and main-backed powered rational critical gauge PR #1177.

## 1. Scope and prior-art boundary

Finite exponential sums, moment sequences, rational generating functions, max-plus dequantization and multiscale eigenvalue perturbation are classical/general mathematics. Akian-Bapat-Gaubert style perturbation frameworks already organize leading exponents and auxiliary coefficient matrices in much greater generality.

The BRC-specific object here is narrower and exact: normalize each **explicit positive-rational critical cell histogram by its own dominant branch weight**. This produces a finite rational, positive, vertex-gauge-invariant carrier whose integer-moment readouts are exactly the powered critical residual matrices and whose atom at ratio `1` is the critical-degeneracy matrix `K`.

No generic perturbation-theory novelty is claimed.

## 2. Critical ratio histogram

Let the explicit branch weights in one tropical critical cell `u->v` be

\[
q_{uv,1},\ldots,q_{uv,c_{uv}}>0,
\]

and let

\[
a_{uv}=\max_\alpha q_{uv,\alpha}.
\]

Define the exact **critical ratio histogram**

\[
\boxed{
\mathcal R_{uv}
=
\sum_\alpha\left[\frac{q_{uv,\alpha}}{a_{uv}}\right]
\in\mathbf N[\mathbf Q_{>0}^{\times}].
}
\]

Every support ratio lies in `(0,1]`.

If `d_uv` branches attain the maximum, then the coefficient of `[1]` is exactly

\[
\boxed{[1]\mathcal R_{uv}=d_{uv}=K_{uv}.}
\]

Thus the critical-degeneracy matrix `K` is the leading atom of a richer exact normalized histogram.

## 3. Exact rational vertex-gauge invariance

Apply any positive rational vertex gauge

\[
q'_{uv,\alpha}=q_{uv,\alpha}\frac{r_v}{r_u}.
\]

The cell maximum transforms by the same common factor:

\[
a'_{uv}=a_{uv}\frac{r_v}{r_u}.
\]

Therefore every normalized branch ratio is unchanged:

\[
\boxed{
\frac{q'_{uv,\alpha}}{a'_{uv}}
=
\frac{q_{uv,\alpha}}{a_{uv}}.
}
\]

Hence

\[
\boxed{\mathcal R'_{uv}=\mathcal R_{uv}}
\]

entrywise on the critical graph.

This is stronger than gauge covariance: the ratio histogram is already an exact gauge-quotient carrier.

## 4. Moment residual readout

For every integer `m>=0`, apply the histogram moment character

\[
\Phi_m\left(\sum_qc_q[q]\right)=\sum_qc_qq^m.
\]

Then

\[
\boxed{
R^{(m)}_{uv}
:=
\Phi_m(\mathcal R_{uv})
=
\sum_\alpha\left(\frac{q_{uv,\alpha}}{a_{uv}}\right)^m
=
\frac{W^{(m)}_{uv}}{a_{uv}^m}.
}
\]

Thus the powered-rational-gauge residual from PR #1177 is not an `m`-dependent new state. It is the integer-moment readout of one fixed exact critical ratio histogram.

At `m=0`,

\[
R^{(0)}_{uv}=c_{uv}
\]

is the total explicit branch count in the critical cell.

As `m->infinity`,

\[
\boxed{R^{(m)}_{uv}\to d_{uv}=K_{uv}.}
\]

## 5. Finite rational ratio spectrum

Across all critical cells, collect the finite distinct normalized ratios

\[
1=\theta_0>\theta_1>\cdots>\theta_s>0.
\]

For each ratio define a non-negative integer matrix

\[
\boxed{
(L_j)_{uv}
=
\#\left\{\alpha:\frac{q_{uv,\alpha}}{a_{uv}}=\theta_j\right\}
}
\]

on critical edges and zero elsewhere.

Then

\[
\boxed{L_0=K.}
\]

Moreover the ratio histograms are equivalently encoded by the finite jet

\[
\boxed{
\mathfrak J_{\rm crit}
=\bigl((\theta_0,L_0),\ldots,(\theta_s,L_s)\bigr).
}
\]

The correspondence between `critical ratio histograms` and the finite ratio jet is exact and bijective.

## 6. Exact finite exponential decomposition

For **every** integer `m>=0`, not merely asymptotically,

\[
\boxed{
R^{(m)}
=
\sum_{j=0}^s\theta_j^mL_j
=
K+\sum_{j=1}^s\theta_j^mL_j.
}
\]

Thus the apparent asymptotic tower is a finite exact rational exponential sum.

The previous local branch-gap bound is the first truncation:

\[
0\le R^{(m)}-K
\]

entrywise, and if `theta_1` exists,

\[
\boxed{
0\le R^{(m)}-K
\le \theta_1^m\sum_{j>=1}L_j
}
\]

entrywise.

More generally, after retaining the first `t` subleading layers,

\[
\boxed{
0\le
R^{(m)}-\sum_{j=0}^t\theta_j^mL_j
\le
\theta_{t+1}^m\sum_{j>t}L_j
}
\]

entrywise.

No asymptotic `O` notation is needed for these finite-prefix bounds.

## 7. Moment-order rational generating function

Introduce a formal moment-order marker `y`. Then

\[
\begin{aligned}
\mathcal M(y)
&:=\sum_{m\ge0}R^{(m)}y^m\\
&=\sum_{j=0}^s L_j\sum_{m\ge0}(\theta_jy)^m.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal M(y)
=
\sum_{j=0}^s\frac{L_j}{1-\theta_j y}.
}
\]

In particular,

\[
\boxed{
\sum_{m\ge0}(R^{(m)}-K)y^m
=
\sum_{j=1}^s\frac{L_j}{1-\theta_j y}.
}
\]

The infinite residual moment sequence is therefore finitely represented by rational poles at exact positive rational reciprocals `1/theta_j` with non-negative integer residue matrices `L_j` up to the conventional scalar factor.

This is a generating-function identity, not a probability transform.

## 8. Prime-valuation representation

Every ratio `theta_j` is positive rational and therefore has exact finite-support prime valuations

\[
\nu(\theta_j)=(v_p(\theta_j))_p\in\bigoplus_p\mathbf Z.
\]

Thus the finite ratio jet can equivalently be stored as

\[
\boxed{
\bigl((\nu(\theta_j),L_j)\bigr)_{j=0}^s,
}
\]

with `nu(theta_0)=0`.

Under rational vertex gauge the ratios themselves are unchanged, so their prime-valuation coordinates are unchanged exactly.

The derived log gap of one layer is

\[
-\ln\theta_j
=
-\sum_pv_p(\theta_j)\ln p,
\]

but the exact carrier remains rational/valuation data.

## 9. Relation to the powered rational critical gauge

For the reference critical cycle `(r0,Q0)` and rational powered potentials `H_v` from PR #1177, moment orders `m=r0*s` satisfy on each critical edge

\[
Q_0^{-s}\left(\frac{H_v}{H_u}\right)^sW^{(m)}_{uv}
=R^{(m)}_{uv}.
\]

Therefore the powered gauge globally flattens all critical maxima to the common reference scale, while the critical ratio histogram records the exact **internal branch shape that remains after this flattening**.

The two objects are complementary:

- `H_v,Q0,r0` encode global critical max-weight gauge/mean structure;
- `mathcal R` or `J_crit` encode gauge-invariant within-cell relative branch structure.

## 10. Completeness and strictness boundaries

The finite ratio jet determines every normalized critical moment matrix `R^(m)` and every critical ratio histogram exactly.

However:

- `K=L_0` alone does not determine `L_1,L_2,...`;
- the powered potentials `H_v` plus `K` do not determine subdominant branch ratios;
- the ratio histogram deliberately forgets the **absolute** critical cell maxima `a_uv`, hence cannot recover the original branch weights without separate max/gauge data;
- equal normalized branch weights still coalesce by multiplicity and do not preserve semantic branch labels.

A minimal collision is

\[
\{1,1/2\}
\quad\text{vs}\quad
\{1,1/3\}.
\]

Both have dominant degeneracy `K=1` but different critical ratio jets and different `R^(m)` for every positive `m`.

## 11. Next spectral boundary

The exact finite ratio jet is sufficient input for all further normalized critical spectral corrections because

\[
R^{(m)}=K+\sum_{j>=1}\theta_j^mL_j.
\]

Determining the first nonzero correction to `rho(R^(m))` from this finite jet is a **separate** perturbation problem. Generic multiscale eigenvalue-jet theory is classical and can be singular when `K` has multiple critical Perron classes. No spectral correction formula is promoted by this note.

## 12. Frozen boundaries

```text
CRITICAL_RATIO_HISTOGRAM = CELL_HISTOGRAM_NORMALIZED_BY_DOMINANT_WEIGHT
RATIONAL_VERTEX_GAUGE -> CRITICAL_RATIO_HISTOGRAM_INVARIANT_EXACTLY
R_m = PHI_m(CRITICAL_RATIO_HISTOGRAM)
FINITE_RATIO_JET = ((theta_j,L_j))
L_0 = K
R_m = SUM_j theta_j^m L_j EXACTLY
MOMENT_ORDER_GENERATING_FUNCTION = SUM_j L_j/(1-theta_j y)
K != COMPLETE_CRITICAL_RATIO_SHAPE
POWERED_MAX_GAUGE != CRITICAL_RATIO_HISTOGRAM
FINITE_RATIO_JET != GENERIC_SPECTRAL_PERTURBATION_NOVELTY
```

## 13. Validation plan

1. Reuse the 19,823 cyclic branch samples from PR #1167/#1177.
2. Construct exact ratio histograms on every critical cell and verify gauge invariance.
3. Extract the finite global ratio spectrum and integer matrices `L_j`; verify `L_0=K` and exact histogram reconstruction.
4. For `m=0..8`, verify `R^(m)=sum_j theta_j^m L_j` entrywise and against direct explicit branch moment ratios.
5. Verify all finite-prefix entrywise tail bounds for every jet depth.
6. Through moment order 8, verify the rational generating-function recurrence/coefficient identity induced by `prod_j(1-theta_j y)`.
7. Verify prime-valuation round trips for every distinct ratio.
8. Apply several nonuniform rational vertex gauges and verify the entire finite ratio jet is unchanged exactly.
9. Verify strict collision examples with equal `K` but different ratio jets.
