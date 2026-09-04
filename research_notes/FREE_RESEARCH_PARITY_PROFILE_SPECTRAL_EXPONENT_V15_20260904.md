# Free Research — Spectral Exponent of the Parity-Scattering Profile

Status: `FREE_RESEARCH_FRONTIER / PROFILE OPERATOR MOMENT CLOSED / CRITICAL EXPONENT IDENTIFIED / CONDITIONAL POWER BARRIER CLOSED / FINITE ARITHMETIC BLOCK RECURRENCE OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PARITY_FOLD_ORTHOGONAL_SCATTERING_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Profile left by the exact scattering identity

After the valid/stopped separation channel receives the `S_3` standard-sector energy factor `1/9`, the pointwise survival profile is

\[
q(t)
=1-\frac{32}{9}t(1-t),
\qquad 0\le t\le1,
\tag{1.1}
\]

where

\[
t\simeq\frac{\log q_a(N)}{\log N}
=1-\frac{\log a}{\log N}
\]

is the child logarithmic scale.

The profile is positive, symmetric about `1/2`, equal to `1/9` at the balanced shell and equal to `1` only at the two cutoff boundaries.

The correct question is not its pointwise supremum. It is its action on scale-decay profiles under the logarithmic prime-winding measure.

---

## 2. Ideal logarithmic profile operator

Define

\[
(\mathcal T E)(L)
:=\int_0^1q(t)E(tL)\,dt.
\tag{2.1}
\]

For the power barrier

\[
E_\beta(L)=L^{-\beta},
\qquad 0\le\beta<1,
\]

we have

\[
\mathcal T E_\beta(L)
=M(\beta)E_\beta(L),
\]

where

\[
\boxed{
M(\beta)
:=\int_0^1q(t)t^{-\beta}\,dt
=
\frac1{1-\beta}
-
\frac{32}{9(2-\beta)}
+
\frac{32}{9(3-\beta)}.
}
\tag{2.2}
\]

In particular,

\[
M(0)=\int_0^1q(t)dt=\frac{11}{27}.
\]

Since `q(t)>0` and `-log t>0` on `(0,1)`, `M(beta)` is strictly increasing. Also

\[
M(0)<1,
\qquad
M(\beta)\to\infty
\quad(\beta\uparrow1).
\]

Therefore there is a unique critical exponent

\[
\boxed{\beta_*\in(0,1):M(\beta_*)=1.}
\tag{2.3}
\]

Clearing denominators gives

\[
\boxed{
9\beta_*^3-45\beta_*^2+86\beta_*-32=0,
}
\tag{2.4}
\]

and numerically

\[
\boxed{\beta_*=0.4818928032\ldots.}
\tag{2.5}
\]

---

## PPS-T01 — Exact rational safe exponent

For the rational exponent

\[
\beta=\frac{47}{100},
\]

a direct exact calculation gives

\[
\boxed{
M(47/100)
=\frac{17878100}{18464193}
<1.
}
\tag{3.1}
\]

The exact spectral margin is

\[
\boxed{
1-M(47/100)
=\frac{586093}{18464193}.
}
\tag{3.2}
\]

Thus `47/100` is a convenient robust energy exponent below the critical value. The corresponding scalar exponent after the parity-fold square-root readout is

\[
\boxed{47/200=0.235.}
\tag{3.3}
\]

No claim is made yet that the arithmetic recurrence satisfies the hypotheses needed to realize this exponent.

---

## 4. Arithmetic logarithmic profile moment

Let

\[
u_a=\Lambda(a)/a,
\qquad
A(N)=\sum_{a\le N}u_a=\log N+O(1),
\]

and put

\[
\alpha_{N,a}:=rac{A(q_a(N))}{A(N)}.
\]

For `0<=beta<1`, use the regularized barrier

\[
W_\beta(n):=(1+\log n)^{-\beta}.
\]

The bounded discrepancy of `A(e^x)` from `x` implies that the normalized logarithmic action measure has Kolmogorov discrepancy `O(1/log N)` from Lebesgue measure. The test profile

\[
h_{N,\beta}(t)
=q(t)\left(\frac{1+\log N}{1+t\log N}\right)^\beta
\]

has total variation `O_beta((log N)^beta)` because its only growing derivative is near `t=0`. Stieltjes summation therefore yields

\[
\boxed{
\frac1{A(N)}
\sum_{a\le N}u_a
q(\alpha_{N,a})
\frac{W_\beta(q_a(N))}{W_\beta(N)}
=
M(\beta)+O_{\beta}\left((\log N)^{\beta-1}\right).
}
\tag{4.1}
\]

The floor region `q_a(N)=O(1)` has normalized mass `O(1/log N)` and contributes the same `O((log N)^{beta-1})` order. Replacing `alpha_{N,a}` by `log q_a/log N` costs only `O(1/log N)` because `q` is Lipschitz.

Thus every fixed `beta<beta_*` has an eventual strict arithmetic profile gap.

This statement is a paper-level Abel/Stieltjes consequence of the existing first-mass law. A full formal asymptotic interface has not yet been written in Lean.

---

## PPS-T02 — Conditional power-barrier theorem

Suppose a nonnegative energy envelope `E(N)` satisfies, for all sufficiently large `N`,

\[
\boxed{
E(N)
\le
\frac1{A(N)}
\sum_{a\le N}u_a
q(\alpha_{N,a})E(q_a(N))
+
C(1+\log N)^{-\gamma}
}
\tag{5.1}
\]

for some

\[
\gamma>\beta,
\qquad
0<\beta<\beta_*.
\]

Then

\[
\boxed{E(N)=O((1+\log N)^{-\beta}).}
\tag{5.2}
\]

### Proof

By (4.1), choose `rho<1` and `N_0` such that

\[
\frac1{A(N)}
\sum_{a\le N}u_aq(\alpha_{N,a})
\frac{W_\beta(q_a(N))}{W_\beta(N)}
\le\rho
\]

for `N>=N_0`.

Choose `K` dominating the finite initial range and satisfying

\[
C W_\gamma(N)
\le(1-\rho)K W_\beta(N)
\]

for `N>=N_0`. Strong induction then gives

\[
E(N)
\le K\rho W_\beta(N)+(1-\rho)KW_\beta(N)
=KW_\beta(N).
\]

The theorem is an ordinary positive barrier argument once the profile moment is retained.

---

## PPS-C01 — Conditional prime remainder

The V15 symmetric parity-fold readout gives

\[
|r(N)|
\le\sqrt{E(N)}+O(1/\log N)
\]

whenever `E` dominates the shared-first folded energy.

Under (5.1), for every `beta<beta_*` and `gamma>beta`,

\[
\boxed{
r(N)
=O((\log N)^{-\beta/2}).}
\tag{6.1}
\]

Equivalently,

\[
\boxed{
\psi(N)-N
=O\left(N(\log N)^{-\beta/2}\right).
}
\tag{6.2}
\]

The robust rational specialization is

\[
\boxed{
\psi(N)-N
=O\left(N(\log N)^{-47/200}\right),
}
\tag{6.3}
\]

conditional on establishing the finite recurrence (5.1) with forcing exponent greater than `47/100`.

The V14 residual forcing has order `O((log N)^-2)`, so its exponent is more than sufficient; the unresolved issue is the exact block comparison producing the profile-weighted first term in (5.1).

---

## 7. What this closes

Closed:

1. the correct Mellin moment of the parity-scattering profile;
2. existence and uniqueness of the critical energy exponent;
3. its cubic equation and numerical value;
4. an exact rational safe exponent with certified margin;
5. an arithmetic log-profile moment from the first-mass discrepancy;
6. a conditional barrier theorem converting the profile recurrence into energy decay;
7. the resulting conditional scalar prime remainder.

Open:

1. prove the exact finite V14/V15 block recurrence (5.1);
2. incorporate the lower quotient-cloud variance as a typed lower-scale component rather than silently adding it to `q(alpha)`;
3. absorb the mixed valid/stopped chamber by the coefficient-potential identity with no coefficient duplication;
4. verify that the shared-first symmetric fold energy is dominated by the chosen block envelope at every scale;
5. remove the word `conditional` from (6.3).

The exponent `beta_*` is therefore an acceptance threshold for the remaining finite block theorem, not a promoted prime-number-theorem remainder.
