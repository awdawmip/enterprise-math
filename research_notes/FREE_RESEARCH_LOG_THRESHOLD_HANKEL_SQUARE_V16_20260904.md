# Free Research — Squared Threshold Kernel and Antiperiodic Green Geometry

Status: `FREE_RESEARCH_FRONTIER / EXACT KERNEL SQUARE / ANTIPERIODIC LAPLACIAN RESOLVENT / LEADING ENERGY CONSTANT 4/PI^2 / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_LOG_THRESHOLD_HANKEL_GAP_V16_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Exact square of the valid/stopped sign operator

Let

\[
K(s,t)=\operatorname{sgn}(s+t-1),
\qquad 0\le s,t\le1,
\]

and

\[
(\mathsf Sf)(s)=\int_0^1K(s,t)f(t)dt.
\]

For fixed `s,u`, the two signs `K(s,t)` and `K(t,u)` disagree precisely when `t` lies between the thresholds `1-s` and `1-u`. That interval has length `|s-u|`. Therefore

\[
\boxed{
(\mathsf S^2)(s,u)
=\int_0^1K(s,t)K(t,u)dt
=1-2|s-u|.}
\tag{1.1}
\]

Thus

\[
\boxed{
(\mathsf S^2f)(s)
=\int_0^1(1-2|s-u|)f(u)du.}
\tag{1.2}
\]

This is a positive operator even though its integral kernel changes sign near the opposite corners.

---

## 2. Differential realization

For sufficiently regular `f`, differentiating twice gives

\[
\boxed{
(\mathsf S^2f)''(s)=-4f(s).}
\tag{2.1}
\]

The image satisfies the antiperiodic boundary conditions

\[
\boxed{
(\mathsf S^2f)(1)=-(\mathsf S^2f)(0),
\qquad
(\mathsf S^2f)'(1)=-(\mathsf S^2f)'(0).}
\tag{2.2}
\]

Hence `S^2` is the Green operator

\[
\boxed{
\mathsf S^2
=4(-\partial_s^2)^{-1}_{\rm anti},}
\tag{2.3}
\]

where the inverse is taken on the antiperiodic Sobolev domain.

The antiperiodic Fourier frequencies are

\[
(2k+1)\pi,
\qquad k\in\mathbb Z.
\]

Therefore

\[
\boxed{
\operatorname{Spec}(\mathsf S^2)
=\left\{
\frac4{(2k+1)^2\pi^2}:k=0,1,2,\ldots
\right\},}
\tag{2.4}
\]

with multiplicity two for each displayed value.

Taking signed square roots recovers

\[
\operatorname{Spec}(\mathsf S)
=\left\{
\pm\frac2{(2k+1)\pi}:k\ge0
\right\}.
\]

---

## 3. Sharp threshold Poincare inequality

Equation (2.4) gives the sharp estimate

\[
\boxed{
\|\mathsf Sf\|_2^2
\le\frac4{\pi^2}\|f\|_2^2.}
\tag{3.1}
\]

Equality holds exactly on the two-dimensional leading antiperiodic frequency space

\[
\operatorname{span}\{\cos(\pi s),\sin(\pi s)\}.
\]

Equivalently, for every `g` in the range of `S`,

\[
\boxed{
\int_0^1|g'(s)|^2ds
\ge\pi^2\int_0^1|g(s)|^2ds,}
\tag{3.2}
\]

which is the sharp antiperiodic Poincare inequality.

The prime-history threshold gap is therefore an ordinary one-dimensional geometric frequency gap after squaring the sign kernel.

---

## 4. Interpretation

The collision boundary `s+t=1` acts as a reflection wall. Passing through two valid/stopped comparisons produces the distance kernel

\[
1-2|s-u|,
\]

so the nonlocal prime-history threshold operator becomes a local antiperiodic Laplacian resolvent.

This gives a precise geometric chain:

\[
\boxed{
\text{prime-winding collision threshold}
\xrightarrow{\text{two comparisons}}
\text{antiperiodic interval Laplacian}
\xrightarrow{\text{lowest frequency}}
\frac4{\pi^2}.}
\tag{4.1}
\]

Thus the appearance of `pi` in the prime extension is not merely the spectrum of an ad hoc integral transform. It is the fundamental antiperiodic frequency of the logarithmic action interval.

---

## 5. Finite arithmetic consequence

Under the quantile coupling from the parent note, the finite prime-winding threshold operator satisfies

\[
\mathsf S_N^2
=\mathsf G_{\rm anti}+O_{2\to2}((\log N)^{-1/2}),
\]

where `G_anti` denotes the continuum kernel (1.2) compressed to the quantile-step subspace. Therefore

\[
\boxed{
\|\mathsf S_N^2\|_{2\to2}
\le\frac4{\pi^2}+O((\log N)^{-1/2}).}
\tag{5.1}
\]

This is the exact energy coefficient available for the additive valid/stopped channel once the arithmetic intertwiner is completed.

---

## 6. Boundary

Closed:

1. exact square kernel `1-2|s-u|`;
2. antiperiodic Green-operator realization;
3. sharp frequency and Poincare constant;
4. geometric explanation of the constants `2/pi` and `4/pi^2`;
5. finite prime-winding perturbative consequence.

Open:

1. identify the actual folded additive channel with the finite threshold Green block without residual leakage;
2. combine this block with the pair-interaction `1/9` sector and mixed boundary channels;
3. derive a closed native prime-error recurrence.
