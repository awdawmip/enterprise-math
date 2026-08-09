# P022 — Total Event-Repair Variance Has a Linear Upper Bound

Status: `ACTIVE RESEARCH NOTE / EXACT SECOND-MOMENT BOUND / LOWER ORDER OPEN`  
Owner: `program/p022-geometry-v2`  
Depends on: rotated `Z^2` four-wall repair; exact orientation variance; mixed repair moment calculus

## 1. Question

The exact total repair is

\[
r_N=E_N+B_N,
\]

with microscopic mean `Theta(sqrt(N))`.  The exact bivariate mechanism polynomial now makes the finite variance computable for every horizon, but that alone does not identify its growth class.

The four-wall representation supplies a simple rigorous upper bound.  In particular it rules out any required `N log N`, `N^(3/2)` or quadratic variance scale.

## 2. A rotated coordinate is a lazy one-dimensional walk

Under

\[
U_t=(S_t+T_t)/2,
\qquad
V_t=(S_t-T_t)/2,
\]

the microscopic pair process is the standard cardinal walk on `Z^2`.

Looking only at `U`, one step is

\[
+1,-1,0,0
\]

with equal microscopic weights, so

\[
\Pr(\Delta U=1)=\Pr(\Delta U=-1)=\frac14,
\qquad
\Pr(\Delta U=0)=\frac12.
\]

Its return probability at time `t` is

\[
\boxed{
p_t=\Pr(U_t=0)=\frac{\binom{2t}{t}}{4^t}.}
\]

## 3. P022-VB01 — exact second moment of coordinate-axis local time

Let

\[
L_N=\sum_{t=0}^{N-1}\mathbf1_{\{U_t=0\}}.
\]

The generating function of `p_t` is

\[
P(z)=\sum_{t\ge0}p_tz^t=(1-z)^{-1/2}.
\]

Therefore

\[
P(z)^2=(1-z)^{-1}
\]

and every convolution coefficient is exactly one:

\[
\boxed{
\sum_{s=0}^t p_sp_{t-s}=1.
}
\]

By the Markov property,

\[
\Pr(U_s=0,U_t=0)=p_sp_{t-s}
\qquad(s<t).
\]

Hence

\[
\begin{aligned}
\mathbb E[L_N^2]
&=\sum_{t=0}^{N-1}p_t
+2\sum_{0\le s<t<N}p_sp_{t-s}\\
&=\sum_{t=0}^{N-1}p_t
+2\sum_{t=1}^{N-1}(1-p_t).
\end{aligned}
\]

Thus

\[
\boxed{
\mathbb E[L_N^2]
=2N-\mathbb E[L_N].
}
\]

In particular,

\[
\boxed{
\mathbb E[L_N^2]<2N
}
\]

for every `N>0`.

This is an exact integer/rational identity, not only an asymptotic estimate.

## 4. P022-VB02 — split-repair second moment is `O(N)`

In the rotated walk, a split repair bit can occur only on a nonzero coordinate axis before a departure from that axis.

Let `L_N^U,L_N^V` be the zero local times of the two rotated coordinates.  Pathwise,

\[
\boxed{
B_N\le L_N^U+L_N^V.
}
\]

Therefore

\[
B_N^2
\le2(L_N^U)^2+2(L_N^V)^2.
\]

Taking expectations and using symmetry plus VB01 gives

\[
\boxed{
\mathbb E[B_N^2]
\le4\mathbb E[L_N^2]
<8N.
}
\]

So the split mechanism has at most linear raw second moment, regardless of its nontrivial covariance with the orientation mechanism.

## 5. P022-VB03 — total repair variance is `O(N)`

The orientation component already has an exact second moment and variance; in particular

\[
\mathbb E[E_N^2]=O(N).
\]

Using

\[
(E_N+B_N)^2\le2E_N^2+2B_N^2
\]

and VB02,

\[
\boxed{
\mathbb E[r_N^2]=O(N).
}
\]

Since variance never exceeds the raw second moment,

\[
\boxed{
\operatorname{Var}(r_N)=O(N).
}
\]

Therefore the standard deviation satisfies

\[
\boxed{
\operatorname{sd}(r_N)=O(\sqrt N).
}
\]

This rules out all superlinear variance scales.

## 6. What is and is not proved

The upper bound does **not** yet prove

\[
\operatorname{Var}(r_N)=\Theta(N).
\]

The missing issue is a matching lower bound.  The orientation component alone has variance `Theta(N)`, but variance is not monotone under addition: the mixed covariance with `B_N` could in principle cancel part of it.

The exact covariance theorem also shows the finite covariance changes sign, so no simple positivity argument is available.

Thus the current sharp status is:

\[
\boxed{
\operatorname{Var}(r_N)\le C N
}
\]

for an explicit finite constant `C`, while a matching `Omega(N)` bound remains open.

## 7. Why the convolution identity matters

The same normalized central-binomial sequence already appeared in one-sided orientation repair.  After the integer rotation it appears again as the exact return law of a lazy coordinate of the planar walk.

So two apparently different repair mechanisms are controlled by the same discrete return kernel, but on different wall families.  Their interaction is carried entirely by the mixed wall-order statistic, not by different one-dimensional return laws.

This narrows the remaining problem substantially:

> the unresolved part of total fluctuation is not marginal wall recurrence; it is the joint ordering/correlation of visits to the diagonal and coordinate wall families.

## 8. Prior-art discipline

Lazy simple random walks, central-binomial return probabilities, generating-function convolution, Markov local-time second moments and Cauchy-type second-moment bounds are classical.

The P022-specific content is the exact identification of the split repair with coordinate-axis departures in the rotated Barlow walk and the resulting finite-precision variance consequence.

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_repair_variance_bound.py`;
- `tests/test_p022_barlow_repair_variance_bound.py`.

The tests verify the convolution identity exactly, compare the lazy-axis local-time moments with direct cardinal-walk enumeration, validate the reconstructed two-sided orientation second moment, and check the linear certificate against the exact total variance from the bivariate mechanism polynomial.
