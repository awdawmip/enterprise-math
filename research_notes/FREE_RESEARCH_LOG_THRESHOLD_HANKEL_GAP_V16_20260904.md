# Free Research — Log-Threshold Hankel Gap

Status: `FREE_RESEARCH_FRONTIER / CONTINUUM SPECTRUM CLOSED / DISCRETE PRIME-WINDING OPERATOR-NORM CONVERGENCE / GLOBAL THRESHOLD GAP / ADDITIVE SECTOR CLOSED / TWO-BODY INTERACTION COMPOSITION OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PARITY_FOLD_ORTHOGONAL_SCATTERING_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Executive result

The valid/stopped threshold geometry has a global spectral gap that is invisible to the pointwise profile supremum.

On logarithmic action coordinates, define

\[
(\mathsf Sf)(s)
:=\int_0^1\operatorname{sgn}(s+t-1)f(t)\,dt.
\tag{1.1}
\]

This compact self-adjoint Hankel operator has complete nonzero spectrum

\[
\boxed{
\lambda_{k,\pm}
=\pm\frac{2}{(2k+1)\pi},
\qquad k=0,1,2,\ldots.
}
\tag{1.2}
\]

Hence

\[
\boxed{\|\mathsf S\|_{2\to2}=2/\pi<1.}
\tag{1.3}
\]

For prime-winding weights

\[
u_a=\Lambda(a)/a,
\qquad
p_N(a)=u_a/A_N,
\qquad
A_N=\sum_{a\le N}u_a,
\]

define the finite threshold operator

\[
(\mathsf S_Nx)(a)
:=\sum_{b\le N}p_N(b)
\operatorname{sgn}(ab-N)x(b),
\tag{1.4}
\]

with any fixed convention on the zero boundary. Then

\[
\boxed{
\|\mathsf S_N\|_{L^2(p_N)\to L^2(p_N)}
=\frac2\pi+O((\log N)^{-1/2}).
}
\tag{1.5}
\]

In particular, `||S_N||<1` for all sufficiently large `N`.

This closes the one-variable correlated-boundary obstruction in the parity fold. The remaining block is the genuinely two-body valid-endpoint interaction and its mixed moving-cutoff chambers.

---

## 2. Continuum eigenvalue equation

Let `lambda!=0` and suppose

\[
\mathsf Sf=\lambda f.
\]

Writing

\[
C=\int_0^1f(t)dt,
\qquad
F(x)=\int_0^xf(t)dt,
\]

we have

\[
\lambda f(s)=C-2F(1-s).
\tag{2.1}
\]

Differentiating gives

\[
\boxed{\lambda f'(s)=2f(1-s).}
\tag{2.2}
\]

Applying (2.2) at `1-s` and differentiating once more,

\[
\boxed{f''(s)+\frac4{\lambda^2}f(s)=0.}
\tag{2.3}
\]

The endpoint equations are

\[
f(1)=-f(0),
\tag{2.4}
\]

\[
\lambda f'(0)=2f(1)=-2f(0).
\tag{2.5}
\]

Let

\[
\sigma=\operatorname{sgn}(\lambda),
\qquad
\omega=2/|\lambda|.
\]

Equation (2.5) forces

\[
f(s)=A\bigl(\cos(\omega s)-\sigma\sin(\omega s)\bigr).
\tag{2.6}
\]

The remaining endpoint equation and its derivative equivalent force

\[
\sin\omega=0,
\qquad
\cos\omega=-1.
\]

Thus

\[
\omega=(2k+1)\pi
\]

and

\[
\lambda=\frac{2\sigma}{(2k+1)\pi}.
\]

The eigenfunctions may be chosen as

\[
\boxed{
f_{k,\sigma}(s)
=\cos((2k+1)\pi s)-
\sigma\sin((2k+1)\pi s).}
\tag{2.7}
\]

Substitution into (1.1) verifies the sign and normalization directly.

If `Sf=0`, differentiating the zero equation gives `f(1-s)=0` almost everywhere, so the kernel is trivial. Compact self-adjoint spectral theory then makes the family in (2.7) complete.

---

## 3. Collision operator form

Let

\[
(\mathsf Hf)(s):=\int_0^{1-s}f(t)dt
\]

and let

\[
(\mathsf Jf)(s):=\int_0^1f(t)dt.
\]

Then

\[
\boxed{\mathsf S=\mathsf J-2\mathsf H.}
\tag{3.1}
\]

Thus `S` is the signed difference between the stopped-tail and valid-collision kernels. Its gap is a global overlap phenomenon of the triangular threshold graph, not a pointwise degree gap.

The leading positive and negative modes have wavelength `2` in the logarithmic action interval. This is the continuum version of the approximate sign-reversing mode isolated by the Selberg return operator.

---

## 4. Prime-winding logarithmic measure

Let

\[
s_a:=\frac{\log a}{\log N}\in[0,1]
\]

and define

\[
\nu_N
:=\sum_{a\le N}p_N(a)\delta_{s_a}.
\]

Its distribution function is

\[
F_N(s)=\frac{A(N^s)}{A(N)}.
\]

The first-mass law

\[
A(x)=\log x+O(1)
\]

implies the uniform discrepancy estimate

\[
\boxed{
\delta_N:=\sup_{0\le s\le1}|F_N(s)-s|
=O(1/\log N).
}
\tag{4.1}
\]

No PNT input beyond this already established Mertens-strength first-mass law is used.

---

## LTH-T01 — Quantile coupling

Let `Q_N:[0,1]->[0,1]` be the generalized quantile of `nu_N`. Uniform CDF discrepancy gives

\[
\boxed{|Q_N(u)-u|\le\delta_N}
\tag{5.1}
\]

away from the harmless clipped endpoints; the clipped form with the same bound is valid everywhere after changing representatives on null sets.

Pullback by `Q_N` is an isometry from `L^2(nu_N)` into the subspace of `L^2[0,1]` consisting of functions constant on the quantile intervals.

Under this pullback, the finite operator has kernel

\[
K_N(u,v)
=
\operatorname{sgn}(Q_N(u)+Q_N(v)-1).
\tag{5.2}
\]

The continuum kernel is

\[
K(u,v)=\operatorname{sgn}(u+v-1).
\]

If the two signs differ, then

\[
|u+v-1|\le2\delta_N.
\]

The strip

\[
|u+v-1|\le2\delta_N
\]

has area at most `4 delta_N`. Since `|K_N-K|<=2`,

\[
\boxed{
\|K_N-K\|_{L^2([0,1]^2)}
\le4\sqrt{\delta_N}.}
\tag{5.3}
\]

The Hilbert--Schmidt norm dominates the operator norm, hence

\[
\boxed{
\|\mathsf S_N-\mathsf S\|_{2\to2}
\le4\sqrt{\delta_N}.}
\tag{5.4}
\]

Strictly speaking, `S` on the right is compressed to the quantile-step subspace; its norm is no larger than the full continuum norm.

Therefore

\[
\boxed{
\|\mathsf S_N\|_{2\to2}
\le\frac2\pi+4\sqrt{\delta_N}
=\frac2\pi+O((\log N)^{-1/2}).}
\tag{5.5}
\]

A reverse approximation using step-function projections gives convergence rather than only the upper limit.

---

## 6. Consequences for parity-fold geometry

### Global action-field contraction

For every real action field `x`,

\[
\boxed{
\sum_ap_N(a)|(\mathsf S_Nx)(a)|^2
\le
\left(
\frac4{\pi^2}+O((\log N)^{-1/2})
\right)
\sum_ap_N(a)|x(a)|^2.}
\tag{6.1}
\]

This estimate is uniform over arbitrary correlations of `x` with the cutoff boundary. It therefore closes the precise gap left by replacing the pointwise profile by its supremum.

### Degree field

The row parity degree is

\[
\theta_N(a)
:=1-rac{2A(q_a(N))}{A(N)}
=(\mathsf S_N\mathbf1)(a).
\]

Hence

\[
\boxed{
\|\theta_N\|_{L^2(p_N)}
\le\frac2\pi+O((\log N)^{-1/2}).}
\tag{6.2}
\]

The ideal value is actually `1/sqrt(3)`; (6.2) is a robust operator bound that remains valid after correlation with arbitrary action fields.

### Threshold graph gap

The signed threshold graph has no persistent unit-modulus `+1` or `-1` mode in logarithmic `L^2`. The only possible slow modes in the full V15 packet must therefore live in the two-body interaction or moving-cutoff boundary channels, not in the one-variable action sector.

---

## 7. Relation to the pair `S_3` spectrum

The symmetric pair field decomposes into

\[
F(a,b)=m+s(a)+s(b)+h_+(a,b),
\]

where `s` has zero mean and `h_+` has zero row and column means.

Two independent strict constants are now available:

- threshold/additive overlap:
  \[
  \|\mathsf S_N\|^2
  \le4/\pi^2+o(1);
  \]
- genuine pair interaction under the `S_3` lift--project mixer:
  \[
  h_+\mapsto\frac13h_+,
  \qquad
  \text{energy factor }1/9.
  \]

Thus the abstract diagonal block has limiting upper spectral radius

\[
\boxed{
\max\left\{\frac4{\pi^2},\frac19\right\}
=\frac4{\pi^2}<1.}
\tag{7.1}
\]

What remains is not another spectral gap. It is the arithmetic intertwining theorem that identifies the additive component of the actual folded return packet with `S_N`, and routes every mixed valid/stopped interaction into the already retained V14 boundary state without coefficient duplication.

---

## 8. New geometric meaning of `pi`

The same program began with `pi` as a global completion constant of finite rotation/history geometry. The prime-winding extension now produces a second direct appearance:

\[
\boxed{
\frac2\pi
=\text{spectral radius of the continuum valid/stopped prime-history threshold operator}.}
\tag{8.1}
\]

Equivalently,

\[
\boxed{
\pi/2
=\text{inverse leading susceptibility of the logarithmic prime-collision boundary}.}
\tag{8.2}
\]

This equality is an exact spectral theorem, not a symbolic analogy. The arithmetic finite operators converge to the continuum operator using only the first prime-winding mass law.

It does not identify the `pi` completion constant with a native finite operator before the continuum limit; that stronger internal bridge remains a separate theorem.

---

## 9. Boundary

Closed:

1. exact continuum threshold spectrum;
2. exact norm `2/pi`;
3. uniform prime-winding CDF discrepancy;
4. quantile/HS operator convergence;
5. an asymptotic finite threshold spectral gap;
6. the one-variable correlated-boundary channel;
7. a new exact spectral role for `pi` in the prime extension.

Open:

1. the arithmetic additive/interaction intertwiner for the actual symmetric fold;
2. coefficient-safe incorporation of mixed valid/stopped chambers;
3. a full finite block recurrence;
4. an independent native quantitative prime remainder;
5. Lean formalization of the continuum spectral theorem and quantile perturbation.
