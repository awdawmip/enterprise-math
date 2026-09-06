# Composite-road RH boundary slope closure and simplicity detector

Status: `RESEARCH FRONTIER / CONDITIONAL THEOREM UNDER RH + RH/SIMPLICITY EQUIVALENT CRITERIA / NOT FOUNDATION / NOT RH PROOF`
Date: `2026-09-06`
Researcher: `EM-FREE-C4A91D / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`
Progress-Event-ID: `EM-FREE-C4A91D-ROAD-BOUNDARY-SLOPE-CLOSURE-20260906`
Global journal source: `journal/enterprise-math/2026-09-06/20260906T155800+0800-em-free-c4a91d-road-boundary-slope-closure.md`
Parents:
- `research_notes/COMPOSITE_ROAD_RH_BOUNDARY_LAYER_20260906.md`
- `research_notes/COMPOSITE_ROAD_RH_COMPLETED_SCHUR_PICK_20260906.md`

## 1. Exact Poisson-Schur decomposition

Let

\[
\delta(a)^2=\|E_a-E_0\|_{\rm road}^2,
\qquad E_0=\mathbf1_{[1,\infty)},
\]

and, under RH,

\[
C_a(z)=\frac{X(z)}{X(z+a)},
\qquad X(z)=\xi(1/2+z).
\]

The completed-road note proves `C_a` is a Schur function on the right half-plane. Mellin-Plancherel gives

\[
\delta(a)^2=\frac1{2\pi}\int_{\mathbb R}
\frac{|1-C_a(it)|^2}{1/4+t^2}\,dt.
\]

The measure

\[
d\omega(t)=\frac{dt}{2\pi(1/4+t^2)}
\]

is harmonic measure at `z_*=1/2`. Poisson's formula therefore yields

\[
\int \Re C_a(it)d\omega(t)=C_a(1/2).
\]

Define

\[
D_a=\int [1-|C_a(it)|^2]d\omega(t)\ge0.
\]

Then exactly

\[
\boxed{
\delta(a)^2=2[1-C_a(1/2)]-D_a.
}
\]

Since

\[
C_a(1/2)=\frac{\xi(1)}{\xi(1+a)},
\]

and

\[
\frac{1-C_a(1/2)}a\to\frac{\xi'(1)}{\xi(1)}
=:\lambda_1
=1+\frac\gamma2-\frac12\log(4\pi),
\]

one immediately obtains under RH

\[
\delta(a)^2\le2\lambda_1a+O(a^2).
\]

Hence RH implies `delta(a)=O(sqrt(a))`. Conversely this rate makes `E_a` square-integrable for a sequence `a\downarrow0`, and Burnol's converse then gives RH. Thus

\[
\boxed{
RH\iff\|E_a-E_0\|_{\rm road}=O(\sqrt a)
\quad(a\downarrow0).
}
\]

This is an equivalent criterion, not an RH proof.

## 2. Exact radial-defect slope

Under RH, index distinct signed zero ordinates by real `\lambda` and let `m_\lambda` be the multiplicity. The canonical product gives

\[
|C_a(it)|^2=\prod_\lambda q_{a,\lambda}(t),
\]

where

\[
q_{a,\lambda}(t)=
\left(\frac{(t-\lambda)^2}{a^2+(t-\lambda)^2}\right)^{m_\lambda}.
\]

For one multiplicity cluster set

\[
d(m)=\frac1{2\pi}\int_{\mathbb R}
\left[1-\left(\frac{u^2}{1+u^2}\right)^m\right]du.
\]

A beta-integral evaluation gives

\[
\boxed{
d(m)=m\frac{\binom{2m}{m}}{4^m}.}
\]

For each fixed `\lambda`, scaling `t=\lambda+au` yields

\[
\frac1a\int [1-q_{a,\lambda}(t)]d\omega(t)
\to
\frac{d(m_\lambda)}{\lambda^2+1/4}.
\]

The global interchange is justified without an unproved spectral-tail hypothesis. Indeed,

\[
1-\prod_\lambda q_{a,\lambda}
\le\sum_\lambda(1-q_{a,\lambda})
\]

and

\[
1-q_{a,\lambda}(t)
\le m_\lambda\frac{a^2}{a^2+(t-\lambda)^2}.
\]

The exact Cauchy-kernel convolution is

\[
\frac1{2\pi a}\int_{\mathbb R}
\frac{a^2}{a^2+(t-\lambda)^2}
\frac{dt}{1/4+t^2}
=
\frac{a+1/2}{\lambda^2+(a+1/2)^2}.
\]

For `0<a\le1/2` this is at most `1/(\lambda^2+1/4)`, and under RH

\[
\sum_\lambda\frac{m_\lambda}{\lambda^2+1/4}<\infty.
\]

This gives a summable majorant for the upper bound. For any fixed finite zero set, separated-neighborhood scaling gives the matching sum of cluster limits; adding the omitted factors can only increase the radial defect. Letting the finite set grow gives the matching lower bound. Therefore

\[
\boxed{
\lim_{a\downarrow0}\frac{D_a}{a}
=
\sum_\lambda
\frac{d(m_\lambda)}{\lambda^2+1/4}.
}
\]

## 3. Closed global boundary slope

The standard xi/Hadamard identity on RH is

\[
\sum_\lambda\frac{m_\lambda}{\lambda^2+1/4}=2\lambda_1.
\]

Hence

\[
\boxed{
\lim_{a\downarrow0}\frac{\delta(a)^2}{a}
=
\sum_\lambda
\frac{c(m_\lambda)}{\lambda^2+1/4},
}
\]

where

\[
\boxed{
c(m)=m-d(m)
=m\left(1-\frac{\binom{2m}{m}}{4^m}\right).}
\]

This closes the global-slope conjecture from `COMPOSITE_ROAD_RH_BOUNDARY_LAYER_20260906.md`; the high-frequency tail is controlled by the positive radial-defect product and the summable xi zero weight.

## 4. Simplicity detector

For `m=1`, `c(1)=1/2`. For every `m>1`, `c(m)>m/2`. Therefore, under RH,

\[
\lim_{a\downarrow0}\frac{\delta(a)^2}{a}\ge\lambda_1,
\]

with equality iff all nontrivial zeros are simple.

Because a finite first-order boundary-energy law already implies RH by Burnol, one obtains the combined equivalence

\[
\boxed{
RH\ \&\ \text{all nontrivial zeros simple}
\iff
\|E_a-E_0\|_{\rm road}^2
=\lambda_1 a+o(a).
}
\]

This is an equivalent reformulation and multiplicity-sensitive road observable, not a proof of either statement.

## 5. Road/hole interpretation

The positive all-integer road has a square-root boundary layer under RH. Its pointwise first derivative is the globally singular prime-number-theorem error field, but the *energy* of the whole road has a finite first-order slope. Multiple zeros increase that slope above the simple-zero baseline.

Thus deleting the road and retaining only the prime tangent loses a multiplicity-sensitive spectral observable carried by the collective positive road.

## Status correction

This note supersedes only the previous note's sentence that the global boundary slope remained conjectural. Its local zero-profile computation remains valid and is used here.
