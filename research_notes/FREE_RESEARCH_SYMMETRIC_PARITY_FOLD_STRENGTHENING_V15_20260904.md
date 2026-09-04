# Free Research — Symmetric Parity-Fold Strengthening

Status: `FREE_RESEARCH_FRONTIER / SYMMETRIC_PROJECTION EXACT / SINGLE CONDITIONAL-VARIANCE READOUT / SHARED-FIRST DEGREE-THREE ENERGY / NATIVE DECAY OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PARITY_FOLDED_SQUARE_SCALAR_READOUT_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Strengthening

The oriented parity fold is

\[
F_N(a,b)=
\begin{cases}
f(q_{ab}(N)),&ab\le N,\\
f(q_a(N)),&ab>N.
\end{cases}
\]

The parity sign

\[
\varepsilon_N(a,b)=2\mathbf 1_{ab>N}-1
\]

is symmetric under `a<->b`, and the product action measure is symmetric. Therefore the signed scalar observable sees only the symmetric projection

\[
\widetilde F_N(a,b)
:=\frac{F_N(a,b)+F_N(b,a)}2.
\]

Explicitly,

\[
\boxed{
\widetilde F_N(a,b)=
\begin{cases}
f(q_{ab}(N)),&ab\le N,\\
\dfrac{f(q_a(N))+f(q_b(N))}{2},&ab>N.
\end{cases}}
\tag{1.1}
\]

One has the exact identity

\[
\boxed{
\mathbb E_{\pi_N}[\varepsilon_NF_N]
=
\mathbb E_{\pi_N}[\varepsilon_N\widetilde F_N].
}
\tag{1.2}
\]

Orthogonal projection gives

\[
\boxed{
\operatorname{Var}_{\pi_N}(\widetilde F_N)
\le
\operatorname{Var}_{\pi_N}(F_N).
}
\tag{1.3}
\]

Thus every scalar bound in the parent note remains valid with the smaller symmetric-fold variance.

---

## 2. Positive odd-square domination survives

Choose the variance center `-f(N)`.

On `ab<=N`,

\[
\widetilde F_N(a,b)+f(N)=\delta_{ab}f(N).
\]

On `ab>N`,

\[
\widetilde F_N(a,b)+f(N)
=\frac{\delta_af(N)+\delta_bf(N)}2.
\]

By convexity,

\[
\left|\frac{\delta_a+\delta_b}{2}\right|^2
\le\frac{|\delta_a|^2+|\delta_b|^2}{2}.
\]

After summing against the symmetric tail measure, the two terms are equal. Hence

\[
\boxed{
A_N^2\operatorname{Var}(\widetilde F_N)
\le
\sum_{ab>N}u_au_b|\delta_af(N)|^2
+
\sum_{ab\le N}u_au_b|\delta_{ab}f(N)|^2.
}
\tag{2.1}
\]

The same stopped odd-square majorant therefore controls the strengthened carrier.

---

## 3. Pair `S_3` mixer on the symmetric subspace

For a symmetric pair field `F(a,b)=F(b,a)`, row and column means agree:

\[
R_F(a)=\mathbb E_cF(a,c).
\]

The pair-valued lift--transpose--project mixer reduces to

\[
\boxed{
(\mathcal K_3^{(2)}F)(a,b)
=\frac{F(a,b)+R_F(a)+R_F(b)}3.
}
\tag{3.1}
\]

Only two centered Hoeffding sectors remain:

\[
\begin{array}{c|c}
\text{sector}&\text{eigenvalue}\\ \hline
s(a)+s(b)&2/3\\
h_+(a,b)&1/3.
\end{array}
\]

The centered spectral radius is still `2/3`, but the transposition `a<->b` edge vanishes identically.

---

## 4. Single shared-first conditional-variance energy

For symmetric `F`, the two nonzero transposition energies are equal after averaging. Consequently

\[
\begin{aligned}
\mathcal D_p(F)
&=\frac16\mathbb E_{a,b,c}
\left[
|F_{ab}-F_{cb}|^2+|F_{ab}-F_{ac}|^2
\right]\\
&=\frac13\mathbb E_{a,b,c}|F_{ab}-F_{ac}|^2.
\end{aligned}
\tag{4.1}
\]

The spectral-gap inequality `Var(F)<=3D_p(F)` becomes

\[
\boxed{
\operatorname{Var}_{p\otimes p}(F)
\le
\mathbb E_{a,b,c}|F(a,b)-F(a,c)|^2.
}
\tag{4.2}
\]

The right side is exactly twice the averaged conditional variance of the second history slot given the first:

\[
\boxed{
\mathbb E_{a,b,c}|F(a,b)-F(a,c)|^2
=2\mathbb E_a\operatorname{Var}_b(F(a,b)).
}
\tag{4.3}
\]

Thus the scalar prime readout can be placed on one shared-first three-history packet rather than the sum of three transposition packets.

---

## 5. Strengthened scalar theorem

Define

\[
\widetilde{\mathcal G}_N(f)
:=
\mathbb E_{a,b,c\sim p_N}
\left|
\widetilde F_N(a,b)-\widetilde F_N(a,c)
\right|^2,
\qquad
p_N(a)=u_a/A_N.
\]

The parity-fold resolvent, covariance bound, symmetric projection and (4.2) give

\[
\boxed{
|f(N)|
\le
\frac{2C_G}{A_N}
+\sqrt{\widetilde{\mathcal G}_N(f)}
+\|f\|_\infty
\left|1-\frac{2C_2(N)}{A_N^2}\right|.
}
\tag{5.1}
\]

For the normalized prime error,

\[
\boxed{
\left|\frac{\psi(N)}N-1\right|
\le
\sqrt{\widetilde{\mathcal G}_N(r)}
+O\left(\frac1{\log N}\right).
}
\tag{5.2}
\]

This is stronger than the parent estimate `sqrt(3 D_N)` and better aligned with the existing V13/V14 conditional-variance carrier.

---

## 6. Chamber decomposition of the shared-first energy

Fix the first action `a` and compare second actions `b,c`.

- If `ab,ac<=N`, the difference is
  \[
  f(q_{ab}(N))-f(q_{ac}(N)),
  \]
  the quotient-cloud relation energy at the intermediate vertex `q_a(N)`.

- If `ab,ac>N`, the difference is
  \[
  \frac{f(q_b(N))-f(q_c(N))}{2},
  \]
  because the common `f(q_a(N))/2` cancels. This is a tail one-step relation field with an extra factor `1/4` in energy.

- If exactly one of `ab,ac` is valid, the difference is an explicit valid/stopped boundary relation. No state is erased; it is one of the moving-cutoff mixed chambers already isolated by the rectangular tail-return bridge.

Therefore

\[
\boxed{
\widetilde{\mathcal G}_N
=
\text{valid/valid lower quotient variance}
+
\frac14\text{ stopped/stopped tail relation}
+
\text{mixed boundary relation}.
}
\tag{6.1}
\]

This exact three-way partition is the next coefficient audit. It is narrower than controlling all three transposition energies independently.

---

## 7. Updated boundary

Closed:

1. exact symmetric projection without changing the scalar parity observable;
2. monotone reduction of folded variance;
3. preservation of the stopped odd-square majorant;
4. collapse of the degree-three Poincare bridge to one shared-first conditional variance;
5. strengthened scalar readout (5.2);
6. exact valid/valid, stopped/stopped and mixed chamber typing.

Open:

1. prove a coefficient-safe recurrence for the three terms in (6.1);
2. show the mixed boundary term is fully absorbed by the V14 coefficient-potential and lower-scale tail system;
3. derive decay of `widetilde G_N(r)` without importing PNT;
4. promote a native logarithmic prime remainder.
