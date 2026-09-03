# Enterprise Math — Critical Ratio-Jet BRC Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION ADDENDUM / MAIN-BACKED / FINITE POSITIVE-RATIONAL`
Effective: `2026-09-03`
Parent: `ENTERPRISE_BRC_CRITICAL_ORBIT_FOUNDATION_20260903.md`
Theorem ledger: `ENTERPRISE_BRC_CRITICAL_RATIO_JET_THEOREM_LEDGER_20260903.json`

## 1. Purpose and prior-art boundary

This addendum freezes the main-backed exact BRC specialization developed in PRs #1177–#1180. Max-plus eigenvector scaling, finite exponential sums, simple Perron-root perturbation and determinant differentiation are classical. Enterprise Math promotes only the typed connection to explicit positive-rational branch histograms, the root-free rational certificate surface, and the reusable exact BRC interface.

No floating critical mean/eigenvalue, signed/amplitude semantics, infinite-state result or generic perturbation novelty is claimed.

## 2. Powered rational critical gauge — WBRC-T45

Let explicit positive-rational branches have tropical critical graph and critical-degeneracy matrix `K` as in WBRC-T39. Choose a reference critical cycle `C0` of length `r0` and dominant product `Q0`.

Inside each critical SCC, normalize one root potential to one. There exists a unique positive rational powered potential `H_v` satisfying every critical dominant state edge `u->v`:

\[
\boxed{a_{uv}^{r_0}H_v=Q_0H_u.}
\]

Path independence is equivalent to the root-free critical-cycle equalities

\[
Q_C^{r_0}=Q_0^{|C|}.
\]

Prime-valuation form: for every prime `p`,

\[
v_p(a_{uv})+g_{v,p}-g_{u,p}=\lambda_p,
\quad g_{v,p}=v_p(H_v)/r_0,
\quad \lambda_p=v_p(Q_0)/r_0.
\]

Thus the dominant valuation cochain is a constant rational mean plus a rational-valued coboundary. The possibly algebraic classical mean `mu=Q0^(1/r0)` is interpretation only; the certificate itself is rational.

For `m=r0*s`, on a critical cell,

\[
Q_0^{-s}(H_v/H_u)^s W^{(m)}_{uv}=W^{(m)}_{uv}/a_{uv}^m.
\]

Positive rational vertex gauge changes `H` covariantly but leaves the normalized residual exactly invariant.

## 3. Critical ratio histogram finite jet — WBRC-T46

On each critical cell with dominant weight `a_uv`, normalize every explicit branch weight to `q/a_uv`. Collect the distinct rational ratios

\[
1=\theta_0>\theta_1>\cdots>\theta_s>0
\]

and let `L_j,uv` count branches in cell `u->v` with ratio `theta_j`. Then

\[
\boxed{L_0=K}
\]

and, for every integer moment order `m>=0`, the critical residual matrix is the exact finite exponential sum

\[
\boxed{R^{(m)}=\sum_j\theta_j^mL_j.}
\]

For any truncation depth `t`,

\[
0\le R^{(m)}-\sum_{j\le t}\theta_j^mL_j
\le \theta_{t+1}^m\sum_{j>t}L_j
\]

entrywise. The entire moment-order sequence has rational generating matrix

\[
\sum_{m\ge0}R^{(m)}y^m=\sum_j\frac{L_j}{1-\theta_jy},
\]

hence an exact finite linear recurrence. The full ratio histogram/jet is invariant under positive rational vertex gauge and each `theta_j` has exact prime-valuation coordinates.

## 4. Irreducible residual first spectral response — WBRC-T47

Assume `K` is irreducible and the largest strict ratio layer is `(theta_1,L_1)` with `L_1!=0`. Write

\[
R_m=K+\theta_1^mL_1+\theta_2^mL_2+\cdots.
\]

Define

\[
p_0(z)=\det(I-zK),
\qquad
p_1(z)=\left.\partial_\varepsilon\det(I-z(K+\varepsilon L_1))\right|_{\varepsilon=0}.
\]

With

\[
\delta=\max(\theta_2,\theta_1^2)<\theta_1
\]

(or `theta_1^2` if no second layer),

\[
\boxed{\det(I-zR_m)=p_0(z)+\theta_1^mp_1(z)+O_{coeff}(\delta^m).}
\]

Let `z_c` be the WBRC-T41 exact smallest-positive-root selector for `p_0`. The exact first logarithmic response is

\[
\boxed{\beta=\frac{p_1(z_c)}{z_cp_0'(z_c)}>0.}
\]

Therefore

\[
\ln\rho(R_m)=\ln\rho(K)+\beta\theta_1^m+O(\delta^m).
\]

The Enterprise certificate is `(p_0, z_c selector, p_1)`; floating Perron eigenvectors are not required. Positivity follows classically from irreducibility, positive Perron vectors and `L_1>=0`, `L_1!=0`.

## 5. Full powered branch-ratio jet — WBRC-T48

Assume now that `K` is irreducible, so the critical graph covers the current state set and the powered potential `H` is defined globally. For every explicit branch `e:u->v`, define the exact rational powered ratio

\[
\boxed{\lambda_e=\frac{q_e^{r_0}H_v}{Q_0H_u}.}
\]

Then

\[
\boxed{\lambda_e=1\iff e\text{ is a critical dominant branch},}
\]

and every other explicit branch satisfies `0<lambda_e<1`.

Collect distinct ratios

\[
1=\lambda_0>\lambda_1>\cdots>\lambda_s>0
\]

and integer branch-count matrices `M_j`. Then `M_0=K`, and for `m=r0*s_index`:

\[
\boxed{
Q_0^{-s_{index}}D(H^{s_{index}})^{-1}W^{(m)}D(H^{s_{index}})
=\sum_j\lambda_j^{s_{index}}M_j.
}
\]

Hence

\[
\boxed{\rho(W^{(r_0s)})/Q_0^s=\rho\!\left(K+\sum_{j\ge1}\lambda_j^sM_j\right).}
\]

If a strict ratio exists, irreducibility gives the positive first correction

\[
\rho(W^{(r_0s)})/Q_0^s
=\rho(K)+c_1\lambda_1^s+O(\delta^s),
\qquad c_1>0,
\]

and the WBRC-T47 root-selector response gives its exact logarithmic coefficient.

For every strict characteristic cycle-system term of WBRC-T40, its normalized base is exactly the product of the selected powered branch ratios. Therefore every strict determinant base is at most `lambda_1`, and the positive first response ensures the `lambda_1` layer is root-active. Thus

\[
\boxed{\eta_{\mathrm{T40}}=\lambda_1.}
\]

The earlier determinant-level gap is exactly the largest powered-gauge noncritical/subdominant explicit branch ratio.

The complete full jet `((lambda_j,M_j))` is invariant under positive rational vertex gauge and is prime-valuation exact. It remains rational even when the classical critical mean is algebraic.

## 6. Boundaries

Freeze:

```text
POWERED_CRITICAL_GAUGE_CERTIFICATE = RATIONAL_H
ALGEBRAIC_CRITICAL_MEAN != ALGEBRAIC_CERTIFICATE_REQUIREMENT
CRITICAL_RATIO_HISTOGRAM != ABSOLUTE_CELL_MAXIMA_OR_LABELED_PROVENANCE
K_ALONE != SUBDOMINANT_RATIO_JET
RATIO_JET_FIRST_SPECTRAL_RESPONSE_REQUIRES_IRREDUCIBLE_K
FULL_POWERED_RATIO_JET_REQUIRES_IRREDUCIBLE_CRITICAL_GRAPH
T40_GLOBAL_GAP = MAX_STRICT_FULL_POWERED_BRANCH_RATIO  [within T48 scope]
POSITIVE_RATIO_LAYER_FIRST_RESPONSE > 0
POSITIVE_RATIO_JET_RESPONSE != SIGNED_CANCELLATION
REDUCIBLE_CRITICAL_CLASSES = SEPARATE_RESEARCH_FRONTIER
```

Canonical negative IDs: `WBRC-N26..N30`.

## 7. Tool routing

Reusable companion T0 subtool:

`t0.weighted_brc_critical_ratio_jet` -> `src/enterprise_math/brc_critical_ratio_jet.py`.

It is a reference exact implementation for rational powered potentials, critical/full ratio jets, rational moment normalization and exact determinant/root-response states. It is not a floating spectral engine or a runtime-complexity claim.
