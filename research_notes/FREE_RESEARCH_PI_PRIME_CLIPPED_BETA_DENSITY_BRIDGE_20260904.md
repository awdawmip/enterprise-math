# Free Research — Clipped-Beta Pushforward Density Bridge

Status: `FREE_RESEARCH_FRONTIER / CANONICAL_TV_MATCHING_NO_GO / ENDPOINT_DISINTEGRATION_CLOSED / CLIPPED_BETA_PROFILE_DOMINATION / MEAN_CHANNEL_STRICT / DENSITY_BRIDGE_CLOSED_AT_RESEARCH_NOTE_STRENGTH / END_TO_END_NATIVE_REMAINDER_INTEGRATION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V13_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` using the existing scale-enumeration, relation-observable, weighted-variance/Laplacian, and quotient-provenance layers.  No new general-purpose tool family is claimed.

## 1. Executive result

The V13 density bridge can be closed, but not by proving that the deepest high/low marginals are asymptotically uniform in the canonical logarithmic prime-power measure.

That proposed uniform matching is false.  The induced marginal has a genuine Beta profile.  In normalized logarithmic coordinate `s in [0,1]`, its limiting density is

\[
3(1-s)^2,
\]

whose total-variation distance from the uniform density is the nonzero constant

\[
\boxed{\frac{2\sqrt3}{9}}.
\]

The correct bridge is instead:

1. remove the final-endpoint conditioning by an exact law of total variance;
2. dominate each actual high/low marginal by a self-similar **clipped Beta profile**;
3. use monotonicity of the mass-weighted variance under positive measure domination;
4. retain a scale-uniform comparison between the clipped profile and the canonical shell measure;
5. spend the extra profile mass inside the already available strict mean-channel budget.

For every fixed `K >= 1`, define the clipped profile

\[
\Phi_{K,L}(t)
:=\max\left\{\frac{t^2}{2},\frac{L^2}{2K}\right\},
\qquad 0\le t\le L.
\]

Its logarithmic mass coefficient is

\[
\boxed{
I_K=\int_0^1\max\left\{\frac{u^2}{2},\frac1{2K}\right\}\,du
=\frac16+\frac1{3K^{3/2}}.
}
\]

After the three colors and the high/low coefficients `(1/2,2,2)` are included, the limiting history-mean coefficient is

\[
\boxed{
q_K=3I_K=\frac12+\frac1{K^{3/2}}.
}
\]

Hence `q_K<1` whenever

\[
K>2^{2/3}.
\]

The especially clean choice `K=4` gives

\[
\boxed{q_4=\frac58,}
\]

while the normalized profile and the canonical shell measure remain mutually comparable within the exact factor `4`.

Thus the density mismatch is not an additive uncontrolled error.  It is absorbed into a positive, self-similar profile state with a strict contraction budget.

---

## 2. Arithmetic setup

Let

\[
u_q:=\frac{\Lambda(q)}q\ge0,
\qquad
A(X):=\sum_{q\le X}u_q,
\]

and assume the already established bounded first-mass discrepancy

\[
\boxed{|A(X)-\log X|\le C}
\tag{2.1}
\]

for all `X>=1`.  Put

\[
L:=\log Y.
\]

For one fixed deepest color, the histories are

\[
a\le Y,
\qquad b,c>Y,
\qquad abc\le Y^3.
\]

The aggregate high marginal is

\[
\mu_H(a)
:=u_a\sum_{\substack{b,c>Y\\bc\le Y^3/a}}u_bu_c,
\qquad a\le Y,
\tag{2.2}
\]

and one low marginal is

\[
\mu_L(b)
:=u_b\sum_{\substack{a\le Y,\ c>Y\\ac\le Y^3/b}}u_au_c,
\qquad Y<b\le Y^2.
\tag{2.3}
\]

They have exactly the same total mass: both are coordinate pushforwards of the same one-color deepest-history measure.

---

## BPD-T01 — Uniform shell moments from bounded discrepancy

For `R,Z>=1` and integer `k>=1`, define

\[
M_{R,k}(Z)
:=\sum_{R<q\le RZ}u_q
\log^k\left(\frac{RZ}{q}\right).
\]

Let

\[
B_R(t):=A(Rt)-A(R).
\]

Then

\[
|B_R(t)-\log t|\le2C.
\]

Stieltjes summation gives the exact identity

\[
\boxed{
M_{R,k}(Z)
=k\int_1^Z B_R(t)
\log^{k-1}\left(\frac Zt\right)\frac{dt}{t}.
}
\tag{3.1}
\]

Consequently,

\[
\boxed{
\left|M_{R,k}(Z)-
\frac{\log^{k+1}Z}{k+1}\right|
\le2C\log^kZ.
}
\tag{3.2}
\]

At `R=1`, since `A(1)=0`, the right side improves to

\[
C\log^kZ.
\tag{3.3}
\]

For `k=0`,

\[
\left|M_{R,0}(Z)-\log Z\right|\le2C,
\]

again with `C` at `R=1`.

This lemma is the only analytic input needed for the density bridge.

---

## BPD-T02 — Explicit high and low convolution profiles

For `1<=Z<=Y`, define

\[
Q_Y(Z)
:=\sum_{Y<b\le YZ}u_b
\bigl(A(Y^2Z/b)-A(Y)\bigr).
\tag{4.1}
\]

This is the mass of ordered pairs `b,c>Y` with `bc<=Y^2Z`.  Applying BPD-T01 and (2.1),

\[
\boxed{
\left|Q_Y(Z)-\frac12\log^2Z\right|
\le4C\log Z+4C^2.
}
\tag{4.2}
\]

Likewise define

\[
P_Y(Z)
:=\sum_{a\le Z}u_a
\bigl(A(YZ/a)-A(Y)\bigr).
\tag{4.3}
\]

This is the mass of pairs `a<=Z`, `c>Y` with `ac<=YZ`.  Then

\[
\boxed{
\left|P_Y(Z)-\frac12\log^2Z\right|
\le3C\log Z+2C^2.
}
\tag{4.4}
\]

The deepest marginals therefore have the exact forms

\[
\boxed{
\mu_H(a)=u_aQ_Y(Y/a),
}
\tag{4.5}
\]

and

\[
\boxed{
\mu_L(b)=u_bP_Y(Y^2/b).
}
\tag{4.6}
\]

Their common leading profile is quadratic in the remaining logarithmic distance to the shell boundary.

---

## BPD-N01 — Canonical total-variation matching is impossible

The leading high measure is

\[
\beta_H(a)
=\frac12u_a\log^2(Y/a),
\]

and the leading low measure is

\[
\beta_L(b)
=\frac12u_b\log^2(Y^2/b).
\]

BPD-T01 gives

\[
\sum_{a\le Y}\beta_H(a)
=\frac16L^3+O(CL^2),
\]

and the same law for the low shell.

In normalized logarithmic coordinate `s`, both probability measures converge to

\[
p_\beta(s)=3(1-s)^2,
\qquad 0\le s\le1.
\]

The crossing point with the uniform density is

\[
s_0=1-\frac1{\sqrt3}.
\]

Therefore

\[
\begin{aligned}
\|p_\beta-1\|_{\rm TV}
&=\int_0^{s_0}\bigl(3(1-s)^2-1\bigr)\,ds\\
&=\boxed{\frac{2\sqrt3}{9}}.
\end{aligned}
\tag{5.1}
\]

Moreover, summing the errors in (4.2)--(4.4) gives actual-to-Beta total variation `O(C/L)` after normalization.  Hence actual-to-canonical total variation tends to the nonzero value (5.1), not to zero.

Thus the V13 mother question must be corrected:

\[
\boxed{
\text{ACTUAL MARGINAL}\not\approx_{1+o(1)}
\text{UNIFORM CANONICAL SHELL MEASURE}.
}
\]

The Beta bias is structural and must be included in the recursive energy state.

---

## BPD-T03 — Endpoint conditioning disappears by positive ANOVA

For a finite positive measure `mu`, define its mass-weighted variance

\[
\mathscr V_\mu(f)
:=\inf_{c\in\mathbb R}
\sum_x\mu(x)|f(x)-c|^2.
\tag{6.1}
\]

If `M_mu>0`, then

\[
\boxed{
\mathscr V_\mu(f)
=\frac1{2M_\mu}
\sum_{x,y}\mu(x)\mu(y)|f(x)-f(y)|^2.
}
\tag{6.2}
\]

Suppose a color-history measure is partitioned by final endpoint:

\[
\mu=\sum_m\mu_m.
\]

Writing `bar f_m` for the mean in endpoint fiber `m` and `bar f` for the aggregate mean,

\[
\boxed{
\mathscr V_\mu(f)
=\sum_m\mathscr V_{\mu_m}(f)
+\sum_mM_m|\bar f_m-\bar f|^2.
}
\tag{6.3}
\]

In particular,

\[
\boxed{
\sum_m\mathscr V_{\mu_m}(f)
\le\mathscr V_\mu(f).
}
\tag{6.4}
\]

Therefore no estimate uniform in each fixed endpoint `m` is needed.  One first sums the V13 high/low inequality over endpoints, and the omitted cross-endpoint term is positive.

This removes the most singular part of the original formulation of the bridge.

---

## BPD-T04 — Positive measure domination controls arbitrary readouts

If finite measures satisfy

\[
\mu\le\nu
\]

pointwise, then

\[
\boxed{
\mathscr V_\mu(f)\le\mathscr V_\nu(f)
}
\tag{7.1}
\]

for every real readout `f`, with no boundedness assumption.

More precisely, if

\[
\nu=\mu+\rho,
\]

then

\[
\boxed{
\mathscr V_\nu(f)
=\mathscr V_\mu(f)+\mathscr V_\rho(f)
+\frac{M_\mu M_\rho}{M_\mu+M_\rho}
|\bar f_\mu-\bar f_\rho|^2.
}
\tag{7.2}
\]

All density-defect terms are positive.

This is why total variation alone was insufficient but positive measure domination is sufficient: an arbitrarily large readout on a small exceptional set is retained inside the positive defect energy rather than discarded.

---

## BPD-T05 — The self-similar clipped-Beta profile

Fix `K>=1`.  For a logarithmic shell of length `L`, define

\[
\boxed{
\Phi_{K,L}(t)
:=\max\left\{\frac{t^2}{2},\frac{L^2}{2K}\right\}.
}
\tag{8.1}
\]

The clipping point is

\[
t=L/\sqrt K.
\]

Its continuum mass is

\[
\begin{aligned}
\int_0^L\Phi_{K,L}(t)\,dt
&=\frac{L^2}{2K}\frac{L}{\sqrt K}
+\int_{L/\sqrt K}^L\frac{t^2}{2}\,dt\\
&=\boxed{\left(\frac16+\frac1{3K^{3/2}}\right)L^3}.
\end{aligned}
\tag{8.2}
\]

Define the discrete high and low profile measures

\[
\nu_H^{(K)}(a)
:=u_a\Phi_{K,L}(\log(Y/a)),
\qquad a\le Y,
\tag{8.3}
\]

and

\[
\nu_L^{(K)}(b)
:=u_b\Phi_{K,L}(\log(Y^2/b)),
\qquad Y<b\le Y^2.
\tag{8.4}
\]

A bounded-variation Stieltjes estimate using (2.1) gives

\[
\boxed{
M(\nu_H^{(K)})
=I_KL^3+O(CL^2),
\qquad
M(\nu_L^{(K)})
=I_KL^3+O(CL^2),
}
\tag{8.5}
\]

where

\[
I_K=\frac16+\frac1{3K^{3/2}}.
\]

The high-shell error is bounded explicitly by `CL^2/2`, and the shifted low-shell error by `CL^2`.

The profile is exactly self-similar under multiplicative translation of a logarithmic shell.  The high shell `[1,Y]` and low shell `(Y,Y^2]` therefore carry the same normalized profile after rescaling.

---

## BPD-T06 — Scale-uniform equivalence to the canonical shell energy

On every atom,

\[
\frac{L^2}{2K}
\le\Phi_{K,L}(t)
\le\frac{L^2}{2}.
\tag{9.1}
\]

Let `sigma` be the canonical shell measure with atom weight `u_q`, and normalize both `sigma` and `nu^(K)` to probability measures.  Since the average profile value lies between the same minimum and maximum, their Radon--Nikodym density satisfies the exact bounds

\[
\boxed{
\frac1K
\le
\frac{d\widehat\nu^{(K)}}{d\widehat\sigma}
\le K.
}
\tag{9.2}
\]

Consequently,

\[
\boxed{
\frac1K\operatorname{Var}_{\widehat\sigma}(f)
\le
\operatorname{Var}_{\widehat\nu^{(K)}}(f)
\le
K\operatorname{Var}_{\widehat\sigma}(f).
}
\tag{9.3}
\]

The comparison constant is independent of `Y`.  It need be paid only when translating the profile state to or from the canonical shell state, not at every recursive step.

---

## BPD-T07 — Actual marginals are multiplicatively dominated

From (4.2), for every high atom,

\[
Q_Y(Y/a)
\le\frac12\log^2(Y/a)+4CL+4C^2.
\]

Since `Phi_(K,L)` dominates both the quadratic term and the floor `L^2/(2K)`, define

\[
\boxed{
\delta_K(Y)
:=\frac{8KC}{L}+\frac{8KC^2}{L^2}.
}
\tag{10.1}
\]

Then

\[
\boxed{
\mu_H\le(1+\delta_K(Y))\nu_H^{(K)}.
}
\tag{10.2}
\]

The low estimate (4.4) gives the sharper factor

\[
1+\frac{6KC}{L}+\frac{4KC^2}{L^2},
\]

so (10.1) is a common bound for both branches:

\[
\boxed{
\mu_H,\mu_{L_1},\mu_{L_2}
\le(1+\delta_K(Y))\nu^{(K)}
}
\tag{10.3}
\]

after the canonical logarithmic shell identification.

By BPD-T04 and homogeneity,

\[
\boxed{
\mathscr V_{\mu_i}(f)
\le(1+\delta_K(Y))
\mathscr V_{\nu_i^{(K)}}(f).
}
\tag{10.4}
\]

This is the required energy-weighted density comparison.

---

## BPD-T08 — Closed mean-channel coefficient

Let

\[
T_Y=\frac92L^3+O(CL^2)
\tag{11.1}
\]

be the full ordered degree-three packet mass from V13.  Apply the exact V13 high/low inequality in every color/endpoint fiber:

\[
\mathscr V_{\rm mean}
\le\frac12\mathscr V_H
+2(\mathscr V_{L_1}+\mathscr V_{L_2}).
\tag{11.2}
\]

Then:

1. sum over endpoints and use BPD-T03;
2. apply the marginal domination BPD-T07;
3. use one common normalized clipped-profile energy envelope;
4. sum the three colors;
5. divide by the full packet mass `T_Y`.

The resulting full-packet mean coefficient is

\[
\boxed{
q_K(Y)
\le
(1+\delta_K(Y))
\left(
\frac12+\frac1{K^{3/2}}
+O_K\left(\frac C{L}\right)
\right).
}
\tag{11.3}
\]

Therefore

\[
\boxed{
q_K(Y)\longrightarrow
q_K:=\frac12+\frac1{K^{3/2}}.
}
\tag{11.4}
\]

For every fixed

\[
K>2^{2/3},
\]

there exists a finite threshold `Y_0(C,K)` such that

\[
q_K(Y)<1
\qquad(Y\ge Y_0).
\]

The standard `S_3` channel keeps its exact coefficient `1/9`.  Hence the slow channel is the history mean, now also strictly contractive.

---

## 12. Explicit robust choice `K=4`

For `K=4`,

\[
\Phi_{4,L}(t)
=\max\left\{\frac{t^2}{2},\frac{L^2}{8}\right\},
\]

and the clipping point is `L/2`.  Its mass is exactly

\[
\boxed{
\int_0^L\Phi_{4,L}(t)\,dt
=\frac5{24}L^3.
}
\tag{12.1}
\]

Thus

\[
\boxed{
q_4=3\cdot\frac5{24}=\frac58.
}
\tag{12.2}
\]

The density condition number is exactly `4`, and the common arithmetic domination error is

\[
\boxed{
\delta_4(Y)
=\frac{32C}{L}+\frac{32C^2}{L^2}.
}
\tag{12.3}
\]

This gives a concrete, non-asymptotic design point:

\[
\boxed{
\text{canonical/profile condition number }4
\quad\leftrightarrow\quad
\text{limiting mean coefficient }5/8.
}
\]

More generally, the Pareto curve is

\[
\boxed{
K\quad\leftrightarrow\quad
q_K=\frac12+K^{-3/2}.
}
\tag{12.4}
\]

Among profiles that dominate the quadratic Beta weight and have pointwise condition number at most `K`, the clipped profile is the pointwise mass-minimal choice.

---

## 13. Cascade consequence

Let logarithmic scales satisfy

\[
L_k=3^kL_0.
\]

After inserting BPD-T08 into the V13 two-channel recurrence, the mean channel has the form

\[
E_{k+1}
\le
\left(q_K+O_K(3^{-k})\right)E_k
+C_K3^{-k},
\tag{13.1}
\]

while the standard channel has coefficient `1/9`.  Since

\[
q_K>1/3,
\]

the mean homogeneous rate is the slower one.  The summable coefficient perturbation changes only the multiplicative constant, so

\[
\boxed{
E_k=O_K(q_K^k).
}
\tag{13.2}
\]

Writing

\[
\alpha_K:=-\log_3q_K>0,
\]

this is

\[
\boxed{
E(N)=O_K\bigl((\log N)^{-\alpha_K}\bigr)
}
\tag{13.3}
\]

along the cube-root hierarchy, provided the remaining already-typed lower-scale forcing is inserted in the same profile state.

For `K=4`,

\[
\boxed{
\alpha_4=\log_3(8/5)\approx0.42781574.
}
\tag{13.4}
\]

As fixed `K` tends to infinity,

\[
\alpha_K\uparrow\log_3 2\approx0.63092975.
\]

Thus the profile bridge supports every fixed exponent

\[
\alpha<\log_3 2
\]

at the research-note recurrence level.  A final identification with the full odd-simplex energy would, through

\[
4U_N^2|\psi(N)/N-1|^2\le3\mathfrak E_N,
\]

yield the conditional native remainder

\[
\frac{\psi(N)}N-1
=O_\beta\bigl((\log N)^{-\beta}\bigr)
\]

for every

\[
\beta<\frac12\log_3 2.
\]

This last statement remains conditional on the end-to-end identification of the profile recurrence with the complete energy `mathfrak E_N`; it is not yet promoted as a closed theorem.

---

## 14. Exact checker

The script

- `scripts/check_free_research_beta_profile_density_bridge.py`

verifies with `Fraction` only:

1. pair energy equals twice mass times mass-weighted variance;
2. endpoint disintegration and positivity of the between-endpoint term;
3. the exact positive mixture-variance identity;
4. finite measure domination and variance monotonicity;
5. the exact `K=4` clipped-profile mass `5/24`;
6. the exact mean coefficient `5/8`;
7. the exact profile condition number `4`;
8. atomwise absorption of an analytic discrepancy by the profile floor;
9. the closed affine recurrence with `q=5/8` and forcing ratio `1/3`.

The real-log shell estimates (3.2), (4.2), and (4.4) are analytic derivations, not floating-point experiments.

---

## 15. Updated boundary

Closed at research-note theorem strength:

1. the canonical total-variation matching no-go;
2. the correct Beta limiting marginal;
3. exact removal of endpoint conditioning;
4. an energy-valid positive density comparison for arbitrary readouts;
5. a common self-similar high/low profile state;
6. scale-uniform profile/canonical variance equivalence;
7. strict mean coefficient `1/2+K^{-3/2}`;
8. explicit robust coefficient `5/8` at condition number `4`.

Still open:

1. formal composition of this profile state with every term of the existing relation-return equation;
2. a Lean formalization of the finite measure/disintegration/profile coefficient layer;
3. checking the complete normalized energy bookkeeping against `mathfrak E_N` without double-counting chamber mass;
4. promotion of the conditional logarithmic energy rate to an end-to-end native theorem;
5. any RH-scale estimate, Working Truth, or Foundation promotion.

The mathematical density bridge itself is no longer an unspecified pushforward comparison.  It has an explicit carrier, positive defect mechanism, tunable contraction/conditioning curve, and a finite exact checker.
