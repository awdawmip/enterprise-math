# P022 — Exact Mixed Moments and Covariance of the Two Repair Mechanisms

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE MOMENT CALCULUS / ASYMPTOTIC OPEN`  
Owner: `program/p022-geometry-v2`  
Depends on: bivariate repair-mechanism polynomial; two-sided event repair; rotated `Z^2` four-wall representation  
Cross-route relevance: P011 weighted fiber moments; P018/P023/P024 state-dependent repair complexity

## 1. Why the mean is not enough

The two-sided coordination-history repair dimension is

\[
r=E+B,
\]

where `E` counts zero-wall/orientation repair and `B` counts diagonal-split/side-label repair.

The microscopic mean is already known to be `Theta(sqrt(N))`, while the orientation component alone has variance of order `N`.  To understand the fluctuation of the **total** repair, one must keep the mixed term

\[
\operatorname{Cov}(E,B).
\]

It cannot be discarded or assigned a sign by intuition.

## 2. Bivariate mechanism polynomial

The existing exact quotient-state polynomial is

\[
\boxed{
M_N(x,y)=\sum_h a_h x^{E(h)}y^{B(h)},
}

where `a_h` counts represented coordination histories of mechanism type `(E,B)`.

A history with repair type `(E,B)` has exactly

\[
2^{E+B}
\]

microscopic lifts.  Hence microscopic weighting is exactly evaluation at

\[
(x,y)=(2,2).
\]

Let

\[
\mathcal D_x=x\frac\partial{\partial x},
\qquad
\mathcal D_y=y\frac\partial{\partial y}.
\]

Then the Euler operators act diagonally on monomials:

\[
\mathcal D_x(x^Ey^B)=E x^Ey^B,
\qquad
\mathcal D_y(x^Ey^B)=B x^Ey^B.
\]

## 3. P022-CV01 — exact microscopic moment tensor from Euler derivatives

Since

\[
M_N(2,2)=4^N,
\]

the microscopic raw moments are

\[
\boxed{
\mathbb E[E]
=\frac{\mathcal D_xM_N(2,2)}{4^N},
\qquad
\mathbb E[B]
=\frac{\mathcal D_yM_N(2,2)}{4^N},
}
\]

\[
\boxed{
\mathbb E[E^2]
=\frac{\mathcal D_x^2M_N(2,2)}{4^N},
\qquad
\mathbb E[B^2]
=\frac{\mathcal D_y^2M_N(2,2)}{4^N},
}
\]

and

\[
\boxed{
\mathbb E[EB]
=\frac{\mathcal D_x\mathcal D_yM_N(2,2)}{4^N}.
}
\]

All numerators are integers obtained by the existing finite chamber recursion.  No enumeration of all `4^N` microscopic word pairs is required.

Equivalently, if the bivariate mechanism terms are `(E,B,a_(E,B))`, then each raw numerator is the finite integer sum

\[
\sum_{E,B}E^iB^j a_{E,B}2^{E+B}.
\]

## 4. P022-CV02 — exact covariance and total variance

The covariance is therefore

\[
\boxed{
\operatorname{Cov}_N(E,B)
=
\frac{M_{11}}{4^N}
-
\frac{M_{10}M_{01}}{16^N},
}
\]

where

\[
M_{ij}=\sum_{E,B}E^iB^j a_{E,B}2^{E+B}.
\]

Likewise

\[
\boxed{
\operatorname{Var}_N(E+B)
=
\frac{M_{20}+2M_{11}+M_{02}}{4^N}
-
\left(\frac{M_{10}+M_{01}}{4^N}\right)^2.
}
\]

Thus the complete finite total-repair variance is already encoded in the same bivariate quotient polynomial that records the two semantic repair mechanisms.

This is important architecturally: the ordinary univariate repair polynomial, which remembers only `r=E+B`, is enough for the total variance of `r`, but the bivariate state is required to attribute that variance to orientation, split and covariance components.

## 5. P022-CV03 — the finite covariance is not sign-definite

Small exact horizons rule out a monotone-sign heuristic.

The exact values include

\[
\boxed{\operatorname{Cov}_3(E,B)=-\frac18,}
\]

\[
\boxed{\operatorname{Cov}_{10}(E,B)=\frac{18609}{4194304}>0,}
\]

\[
\boxed{\operatorname{Cov}_{11}(E,B)=-\frac{144321}{33554432}<0,}
\]

and

\[
\boxed{\operatorname{Cov}_{12}(E,B)=\frac{5712175}{67108864}>0.}
\]

So the mechanism covariance changes sign more than once.

Consequently none of the following is currently justified:

- orientation and split repair are always positively correlated;
- they are always negatively correlated;
- their covariance can be dropped in the leading fluctuation law merely because the two event types live on different walls.

The sign oscillation is a reusable negative boundary for any upstream abstraction.

## 6. Four-wall interpretation of the mixed moment

Under the exact rotation

\[
U=(S+T)/2,
\qquad
V=(S-T)/2,
\]

the microscopic process is a standard cardinal walk on `Z^2`.

Then:

- `E` is the multiplicity-weighted visit/departure local time of the two diagonal walls `U=V` and `U=-V`;
- `B` is the departure count from the nonzero coordinate-axis union `UV=0`.

Therefore

\[
\mathbb E[EB]
\]

is a genuine joint local-time statistic of two intersecting wall families of the `B_2/C_2` arrangement.

The finite sign oscillation shows that this joint statistic contains nontrivial temporal ordering/intersection effects; it is not captured by multiplying the two separate wall means.

## 7. Exact finite computability versus asymptotic status

The finite covariance and total variance are now exact, integer-generated rational observables for every horizon `N`.

What remains open is their asymptotic reduction.  Current bounded computations suggest that the covariance is large enough to matter in the linear variance scale, but no asymptotic coefficient or eventual sign theorem is claimed here.

The next proof target is therefore:

\[
\boxed{
\text{derive an asymptotically sharp law for }M_{11}
\text{ from the four-wall }\mathbb Z^2\text{ walk.}
}
\]

A satisfactory proof must control the ordering of diagonal-wall visits and coordinate-wall departures, including the origin/wall-intersection correction.

## 8. Precision consequence

This produces another sharp separation among summaries of the same quotient:

- the mean repair says how much additional information is needed on average;
- the univariate repair polynomial gives the full distribution of total repair dimension;
- the bivariate mechanism polynomial distinguishes *why* repair is needed;
- the mixed derivative quantifies interaction between two different semantic branching mechanisms.

Thus equal total repair size does not imply equal repair semantics, and equal first moments do not determine total fluctuation.

## 9. Prior-art discipline

Multivariate generating functions, Euler differential operators and covariance extraction are classical.  Random-walk wall local times are also established objects.

The P022-specific contribution is the identification of the Barlow repair mechanisms with the two polynomial coordinates and with the two wall families of the rotated `B_2/C_2` lattice walk.  No historical novelty claim is made for the general generating-function calculus.

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_repair_covariance.py`;
- `tests/test_p022_barlow_repair_covariance.py`.

The tests compare the moment tensor against direct microscopic enumeration through short horizons, verify exact covariance/variance identities, and preserve the small-horizon covariance sign changes as regression boundaries.
