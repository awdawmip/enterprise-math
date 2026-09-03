# BRC Full Powered Branch-Ratio Jet

Status: `RESEARCH / EXACT FINITE POSITIVE-RATIONAL / IRREDUCIBLE CRITICAL GRAPH`
Date: `2026-09-03`
Parents: PR #1177 powered rational critical gauge; PR #1178 critical ratio histogram finite jet; PR #1179 critical residual first spectral response; WBRC-T39..T44.

## 1. Scope

This note removes the remaining boundary in PR #1179 by normalizing **every explicit branch of the full moment matrix**, not only branches in tropical-critical cells.

Assume the critical-degeneracy matrix `K` is irreducible, equivalently its positive support is one strongly connected critical graph covering the current state set.  This gives one rational powered potential on all states.

Generic max-plus eigenvector scaling and Perron perturbation are classical.  The Enterprise/BRC content is the exact positive-rational powered certificate, the finite explicit branch-ratio jet, its gauge invariance, and the identification of the previous determinant gap with a branch-level ratio.

## 2. Powered rational potential

Choose a reference critical cycle `C_0` with length `r_0` and dominant product `Q_0`.  Fix one root state and normalize `H_root=1`.  PR #1177 gives the unique positive rational potential satisfying every critical dominant edge `u->v`:

\[
\boxed{
a_{uv}^{r_0}H_v=Q_0H_u.
}
\]

No value of the generally algebraic critical mean

\[
\mu=Q_0^{1/r_0}
\]

is required.

## 3. Full explicit branch ratio

For **every** explicit positive-rational branch `e:u->v` with weight `q_e`, define

\[
\boxed{
\lambda_e
=
\frac{q_e^{r_0}H_v}{Q_0H_u}
\in\mathbf Q_{>0}.
}
\]

### 3.1 Critical dominant branches

If `e` is tied at the dominant weight of a critical edge, the powered-potential equation gives

\[
\lambda_e=1.
\]

### 3.2 Every other branch is strictly subunit

Because the critical graph is strongly connected, for any edge `u->v` choose a critical path from `v` back to `u`.  Multiplying the powered-potential equations along that path shows that `lambda_e` equals the `r_0`-powered normalized product of the cycle obtained by adding `e`.

Critical maximality gives

\[
\lambda_e\le1.
\]

If equality held, that closed cycle would itself attain the critical mean, so `e` would lie on the critical graph; if `e` were a subdominant parallel branch on a critical cell, replacing the dominant branch by `e` makes the product strictly smaller.  Therefore

\[
\boxed{
\lambda_e=1
\iff
 e\text{ is a critical dominant branch},
}
\]

and all other explicit branches satisfy `0<lambda_e<1`.

## 4. Exact full finite jet

Collect the finitely many distinct ratios

\[
1=\lambda_0>\lambda_1>\cdots>\lambda_s>0
\]

and define the nonnegative integer branch-count matrices

\[
(M_j)_{uv}
=
\#\{e:u\to v:\lambda_e=\lambda_j\}.
\]

Then

\[
\boxed{M_0=K.}
\]

For `s_index>=0`, put `m=r_0 s_index` and

\[
D_s=\operatorname{diag}(H_v^{s_index}).
\]

The full moment matrix satisfies the **exact** rational similarity-normalization identity

\[
\boxed{
\widehat W_s
:=
Q_0^{-s_index}D_s^{-1}W^{(r_0s_index)}D_s
=
\sum_{j=0}^s\lambda_j^{s_index}M_j
=
K+\sum_{j\ge1}\lambda_j^{s_index}M_j.
}
\]

Indeed each explicit branch contributes exactly

\[
Q_0^{-s_index}\frac{H_v^{s_index}}{H_u^{s_index}}q_e^{r_0s_index}
=
\lambda_e^{s_index}.
\]

Thus the **full original recurrent moment matrix**, after exact rational similarity and scalar normalization, is a finite nonnegative rational exponential jet.

Because similarity preserves spectrum,

\[
\boxed{
\rho(W^{(r_0s_index)})/Q_0^{s_index}
=
\rho(\widehat W_s).
}
\]

## 5. Full first spectral correction

If there is at least one noncritical/subdominant branch, let `lambda_1` be the largest strict branch ratio and let `M_1!=0` be its count matrix.  Since `K` is irreducible, its Perron vectors are positive, so the first additive response to `M_1` is strictly positive.

Let

\[
\delta=
\begin{cases}
\max(\lambda_2,\lambda_1^2),&s\ge2,\\
\lambda_1^2,&s=1.
\end{cases}
\]

Then PR #1179 applies directly with moment variable `s_index`:

\[
\boxed{
\rho(W^{(r_0s_index)})/Q_0^{s_index}
=
\rho(K)+c_1\lambda_1^{s_index}+O(\delta^{s_index}),
}
\]

where

\[
c_1>0.
\]

If

\[
p_0(z)=\det(I-zK),
\qquad
p_1(z)=\left.\partial_\varepsilon\det(I-z(K+\varepsilon M_1))\right|_{0},
\]

and `z_c=1/rho(K)` is the existing exact root selector, then the logarithmic coefficient is

\[
\boxed{
\beta_1
=
\frac{p_1(z_c)}{z_c p_0'(z_c)}>0.
}
\]

Therefore

\[
\boxed{
\ln\rho(W^{(r_0s_index)})
=
s_index\ln Q_0
+\ln\rho(K)
+\beta_1\lambda_1^{s_index}
+O(\delta^{s_index}).
}
\]

If there is no strict branch ratio at all, the normalized matrix is exactly `K` for every `s_index` and there is no further correction.

## 6. Identification with the WBRC-T40 characteristic gap

A characteristic determinant term occupying `k` cycle-system vertices selects explicit branches whose raw product is `b`.  Along `m=r_0 s_index`, WBRC-T40 normalizes it by

\[
\eta_b
=
\frac{b^{r_0}}{Q_0^k}.
\]

The state potentials telescope around every determinant cycle, so exactly

\[
\boxed{
\eta_b=\prod_{e\in F}\lambda_e.
}
\]

Every strict term contains at least one strict branch ratio, hence

\[
\eta_b\le\lambda_1.
\]

Because `M_1>=0`, `M_1!=0`, and `K` is irreducible, the Perron response to `M_1` is strictly positive.  Thus the determinant first-derivative polynomial is nonzero at the Perron root and a base-`lambda_1` characteristic term survives.

Hence the exact T40 maximal strict normalized characteristic base is

\[
\boxed{
\eta_{\mathrm{T40}}=\lambda_1.
}
\]

The previous determinant-level gap is therefore the largest powered-gauge **branch-level** subcritical ratio.

## 7. Prime-valuation and ordinary gauge invariance

Every `lambda_e` is positive rational and has a finite exact prime-valuation vector.

Under an ordinary positive rational vertex gauge

\[
q'_e=q_e\frac{g_v}{g_u},
\]

PR #1177 gives

\[
H'_v=H_v\left(\frac{g_o}{g_v}\right)^{r_0}
\]

relative to the same normalized SCC root `o`, while `Q_0` is cycle-gauge invariant.  Therefore

\[
\boxed{\lambda'_e=\lambda_e.}
\]

Thus the complete full ratio jet

\[
\bigl((\lambda_j,M_j)\bigr)_{j=0}^s
\]

is an exact positive-rational vertex-gauge invariant.

## 8. Algebraic critical mean witness

For the critical 2-cycle

\[
0\xrightarrow{1/2}1,
\qquad
1\xrightarrow{1/3}0,
\]

we have

\[
r_0=2,
\quad Q_0=1/6,
\quad H=(1,2/3),
\quad \mu=1/\sqrt6.
\]

Add a subdominant branch `0->1` of weight `1/4` and a noncritical self-loop `0->0` of weight `1/10`.  Their full powered ratios are

\[
\lambda_{0\to1,1/4}=1/4,
\qquad
\lambda_{0\to0,1/10}=3/50.
\]

So the exact full jet is entirely rational even though the classical critical mean is irrational.

## 9. Hard boundaries

Freeze:

```text
FULL_POWERED_RATIO_JET_SCOPE = IRREDUCIBLE_CRITICAL_GRAPH
FULL_RATIO_BRANCH_e = q_e^r0 H_v / (Q0 H_u)
LAMBDA_e = 1 IFF CRITICAL_DOMINANT_BRANCH
FULL_NORMALIZED_MOMENT_MATRIX = SUM_j lambda_j^s M_j
M_0 = K
T40_GLOBAL_GAP = MAX_STRICT_FULL_BRANCH_RATIO
FULL_FIRST_RESPONSE_COEFFICIENT > 0
ALGEBRAIC_CRITICAL_MEAN != ALGEBRAIC_CERTIFICATE_REQUIREMENT
FULL_RATIO_JET = RATIONAL_GAUGE_INVARIANT
REDUCIBLE_CRITICAL_K = NOT_COVERED_BY_THIS_THEOREM
SIGNED_OR_COMPLEX_BRANCHES = NOT_COVERED
```

Reducible/multiple critical classes require a later blockwise theorem.  The statement also remains finite-state and positive-rational; no infinite-state or signed/amplitude extension is claimed.
