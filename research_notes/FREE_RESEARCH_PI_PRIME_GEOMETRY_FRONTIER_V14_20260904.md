# Free Research — Pi-to-Prime Geometry Frontier V14

Status: `FREE_RESEARCH_CURRENT_FRONTIER / PNT_CLOSED_BY_REAL_SMOOTHING / FULL_PROVENANCE_AND_TWO_CHANNEL_ANOVA_CLOSED / STANDARD_ONE_NINTH / MEAN_CLIPPED_BETA_STRICT / PUSHFORWARD_DENSITY_BRIDGE_CLOSED_AT_RESEARCH_NOTE_STRENGTH / END_TO_END_NATIVE_RATE_INTEGRATION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V13_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Stable chain

The stable V13 chain remains:

\[
\boxed{
\begin{aligned}
\text{prime }p
&=\text{irreducible Krawtchouk birth direction},\\
p^a
&=\text{winding-layer birth},\\
\det\mathcal W_M
&=\operatorname{lcm}(1,\ldots,M),\\
\psi(M)&=\log\det\mathcal W_M,\\
\psi(M)&\sim M,\\
\pi(M)&\sim M/\log M.
\end{aligned}}
\]

The deepest degree-three carrier is

\[
(j,v_1,v_2,v_3,m),
\]

its complete history-vector variance splits as

\[
\mathcal V_{\rm full}
=\mathcal V_{\rm mean}+\mathcal V_{\rm std},
\]

and the standard channel contracts by exactly `1/9`.

The history mean obeys the exact high/low certificate

\[
3|\Delta\mu|^2
\le\frac12|d_H|^2+2(|d_{L_1}|^2+|d_{L_2}|^2).
\]

---

## 2. V14 correction: the induced measure is Beta, not uniform

Let

\[
u_q=\frac{\Lambda(q)}q,
\qquad
A(X)=\sum_{q\le X}u_q,
\qquad
|A(X)-\log X|\le C.
\]

For one deepest color, the high and low marginal kernels are

\[
\mu_H(a)=u_aQ_Y(Y/a),
\qquad
\mu_L(b)=u_bP_Y(Y^2/b),
\]

where

\[
\left|Q_Y(Z)-\frac12\log^2Z\right|
\le4C\log Z+4C^2
\]

and

\[
\left|P_Y(Z)-\frac12\log^2Z\right|
\le3C\log Z+2C^2.
\]

Thus the normalized logarithmic marginal converges to

\[
\boxed{3(1-s)^2\,ds,\qquad0\le s\le1.}
\]

Its total-variation distance from the uniform logarithmic shell measure is

\[
\boxed{2\sqrt3/9.}
\]

Therefore the V13 target of a `1+O(1/log Y)` comparison directly with the uniform canonical shell measure is impossible.  The Beta bias is macroscopic and structural.

---

## 3. Endpoint fibers no longer obstruct the bridge

For a finite measure `mu`, write

\[
\mathscr V_\mu(f)
=\inf_c\sum_x\mu(x)|f(x)-c|^2.
\]

If

\[
\mu=\sum_m\mu_m
\]

is the partition by final endpoint, then

\[
\boxed{
\mathscr V_\mu(f)
=\sum_m\mathscr V_{\mu_m}(f)
+\sum_mM_m|\bar f_m-\bar f|^2.
}
\]

Hence

\[
\sum_m\mathscr V_{\mu_m}(f)
\le\mathscr V_\mu(f).
\]

The density comparison may therefore be proved only for the aggregate color marginal.  No uniform estimate at each fixed endpoint `m` is required.

---

## 4. Clipped-Beta profile state

For fixed `K>=1`, logarithmic shell length `L`, and remaining shell distance `t`, define

\[
\boxed{
\Phi_{K,L}(t)
=\max\left\{\frac{t^2}{2},\frac{L^2}{2K}\right\}.
}
\]

The associated high and low shell measures are

\[
\nu_H^{(K)}(a)
=u_a\Phi_{K,L}(\log(Y/a)),
\]

and

\[
\nu_L^{(K)}(b)
=u_b\Phi_{K,L}(\log(Y^2/b)).
\]

They are the same normalized profile after multiplicative shell rescaling.

Their mass coefficient is

\[
\boxed{
I_K
=\frac16+\frac1{3K^{3/2}},
}
\]

and their masses satisfy

\[
M(\nu_H^{(K)}),M(\nu_L^{(K)})
=I_KL^3+O(CL^2).
\]

The normalized profile probability measure and normalized canonical shell measure satisfy the exact scale-uniform comparison

\[
\boxed{
K^{-1}\le
\frac{d\widehat\nu^{(K)}}{d\widehat\sigma}
\le K.
}
\]

---

## 5. Energy-valid density domination

The arithmetic convolution errors are absorbed by the profile floor.  With

\[
\delta_K(Y)
=\frac{8KC}{\log Y}
+\frac{8KC^2}{(\log Y)^2},
\]

all three aggregate branch marginals satisfy

\[
\boxed{
\mu_H,\mu_{L_1},\mu_{L_2}
\le(1+\delta_K(Y))\nu^{(K)}.
}
\]

Positive measure domination gives, for arbitrary readouts,

\[
\boxed{
\mathscr V_{\mu_i}(f)
\le(1+\delta_K(Y))
\mathscr V_{\nu_i^{(K)}}(f).
}
\]

This is stronger and safer than total-variation control: no boundedness assumption on `f` is needed, and every discrepancy is retained in a positive variance identity.

---

## 6. Strict mean coefficient

Combining:

1. the endpoint law of total variance;
2. the V13 high/low coefficients `(1/2,2,2)`;
3. the three deepest colors;
4. the full packet mass `9/2*(log Y)^3+O((log Y)^2)`;
5. clipped-profile domination;

gives

\[
\boxed{
q_K(Y)
\le
(1+\delta_K(Y))
\left(
\frac12+\frac1{K^{3/2}}
+O_K\left(\frac1{\log Y}\right)
\right).
}
\]

Therefore

\[
\boxed{
q_K(Y)\longrightarrow q_K
:=\frac12+K^{-3/2}.
}
\]

For every fixed

\[
K>2^{2/3},
\]

the history-mean channel is strictly contractive for all sufficiently large `Y`.

The standard channel remains exactly `1/9`.

---

## 7. Explicit design point and tradeoff curve

Taking `K=4` gives

\[
\Phi_{4,L}(t)
=\max\{t^2/2,L^2/8\},
\]

\[
\int_0^L\Phi_{4,L}(t)\,dt
=\frac5{24}L^3,
\]

and

\[
\boxed{q_4=\frac58.}
\]

At the same time, profile and canonical normalized variances differ by at most the exact factor `4`.

The full contraction/conditioning Pareto curve is

\[
\boxed{
K\longleftrightarrow
q_K=\frac12+K^{-3/2}.
}
\]

Large fixed `K` approaches the optimal coefficient `1/2`; smaller `K` gives better canonical comparability.

---

## 8. Quantitative recurrence suggested by V14

At cube-root logarithmic scales

\[
L_k=3^kL_0,
\]

the V14 profile recurrence has slow coefficient `q_K`, while arithmetic forcing has ratio `1/3`.  Since `q_K>1/3`, the resulting profile-energy exponent is

\[
\boxed{
\alpha_K=-\log_3q_K.
}
\]

For `K=4`,

\[
\boxed{
\alpha_4=\log_3(8/5)
\approx0.42781574.
}
\]

As fixed `K` tends to infinity,

\[
\alpha_K\uparrow\log_3 2
\approx0.63092975.
\]

Thus the accumulated V13/V14 recurrence supports every fixed energy exponent

\[
\alpha<\log_3 2,
\]

subject to the remaining end-to-end identification with the complete odd-simplex energy.

If that identification is completed without further power loss, the coercive inequality

\[
4U_N^2|\psi(N)/N-1|^2\le3\mathfrak E_N
\]

would give every error exponent

\[
\beta<\frac12\log_3 2
\approx0.31546488.
\]

This is a conditional V14 consequence, not yet a promoted native prime-remainder theorem.

---

## 9. Formal packet

New V14 artifacts:

- `research_notes/FREE_RESEARCH_PI_PRIME_CLIPPED_BETA_DENSITY_BRIDGE_20260904.md`;
- `research_notes/FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V14_20260904.md`;
- `scripts/check_free_research_beta_profile_density_bridge.py`.

The exact checker uses `Fraction` only for the finite identities.  The shell estimates use the analytic bounded-discrepancy input and are not presented as numerical experiments.

---

## 10. Updated boundary

Closed at research-note theorem strength:

1. the original canonical-TV density target is disproved;
2. the correct high/low Beta profile is derived with explicit errors;
3. endpoint conditioning is removed by positive ANOVA;
4. actual marginals are multiplicatively dominated by one self-similar profile family;
5. profile/canonical energy equivalence is scale-uniform;
6. the mean channel has strict coefficient `1/2+K^-3/2`;
7. `K=4` gives the explicit robust pair `(condition number 4, coefficient 5/8)`.

Open:

1. formal composition of the profile state with every term of the relation-return equation;
2. Lean formalization of the finite measure and clipped-profile layer;
3. a single end-to-end normalization audit against `mathfrak E_N`;
4. promotion of the V14 recurrence rate to a native quantitative theorem;
5. any RH-scale claim, Working Truth, or Foundation promotion.

The unique remaining mathematical bridge identified in V13 has been converted into an explicit positive profile theorem.  The remaining work is integration and formal verification rather than discovery of another density estimate.
