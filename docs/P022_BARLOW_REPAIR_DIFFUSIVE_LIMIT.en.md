# P022 — Diffusive Limit of Event-Driven Repair as Four-Wall Brownian Local Time

Status: `ACTIVE RESEARCH NOTE / PROVED DISTRIBUTIONAL LIMIT USING CLASSICAL LOCAL-TIME INVARIANCE / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: four-wall repair decomposition; variance asymptotic; Weyl quotient interpretation  
Cross-route relevance: P018/P023/P024 state-dependent repair distribution and quotient-path uncertainty

## 1. From moment growth to a limit law

The exact repair dimension satisfies

\[
R_N=E_N+B_N.
\]

Current P022 results give

\[
\mathbb E R_N=\Theta(\sqrt N),
\qquad
\operatorname{Var}(R_N)=\Theta(N).
\]

These statements imply that mean and standard deviation have the same scale, but they do not identify the limiting shape of the repair distribution.

The four-wall representation does.

---

## 2. Brownian coordinates

Let `B_1,B_2` be independent standard Brownian motions and define the orthogonal combinations

\[
B_+=\frac{B_1+B_2}{\sqrt2},
\qquad
B_-=\frac{B_1-B_2}{\sqrt2}.
\]

Then `B_+,B_-` are also independent standard Brownian motions, although each is correlated with `B_1,B_2`.

For a one-dimensional Brownian motion `X`, write

\[
L(X)=L_1^0(X)
\]

for its zero local time through time one in the occupation-density normalization.

Define the four-wall Brownian repair variable

\[
\boxed{
\mathcal R
=
L(B_1)+L(B_2)
+
\frac1{\sqrt2}
\bigl(L(B_+)+L(B_-)\bigr).
}
\]

The first two terms correspond to the two original sign walls `S=0,T=0`.  The final two terms correspond to the two rotated exchange walls after the exact one-half departure thinning is combined with the `sqrt(2)` local-time scaling of a variance-`1/2` coordinate.

---

## 3. Prior-art input for joint local-time convergence

Random-walk local-time invariance is classical.  P022 relies on that theory rather than claiming it.

Relevant references include:

- A. N. Borodin, *An asymptotic behaviour of local times of a recurrent random walk with finite variance*, Teor. Veroyatnost. i Primenen. 26:4 (1981), 769–783; Theory Probab. Appl. 26:4 (1982), 758–772, DOI `10.1137/1126082`.
- R. F. Bass and D. Khoshnevisan, *Local times on curves and uniform invariance principles*, Probability Theory and Related Fields 92 (1992), 465–492.

The second reference supplies a uniform/joint invariance framework broad enough to treat a finite family of fixed linear wall observations of one underlying lattice walk.

The project-specific step is the already proved exact identification of Barlow repair with these wall observations and their path-lift semantics.

---

## 4. P022-DL01 — four wall local times converge jointly

Let

\[
A_S,A_T,A_U,A_V
\]

be the discrete wall local times through pre-step horizon `N` from the variance-asymptotic theorem.

Under diffusive scaling of the underlying microscopic pair walk, the joint local-time invariance principle gives

\[
\boxed{
\frac1{\sqrt N}
(A_S,A_T,A_U,A_V)
\Rightarrow
\left(
L(B_1),
L(B_2),
\sqrt2L(B_+),
\sqrt2L(B_-)
\right).
}
\]

The factors `sqrt(2)` on the rotated walls arise because

\[
U\rightsquigarrow\frac1{\sqrt2}B_+,
\qquad
V\rightsquigarrow\frac1{\sqrt2}B_-,
\]

and zero local time scales inversely with spatial scale.

Therefore the four-wall surrogate

\[
W_N=A_S+A_T+\frac12(A_U+A_V)
\]

satisfies

\[
\boxed{
\frac{W_N}{\sqrt N}
\Rightarrow
\mathcal R.
}
\]

---

## 5. P022-DL02 — exact repair has the same diffusive limit

The variance-asymptotic theorem proves the stronger approximation

\[
\mathbb E[(R_N-W_N)^2]=o(N).
\]

Hence

\[
\frac{R_N-W_N}{\sqrt N}
\to0
\]

in `L^2`, and therefore in probability.

Slutsky's theorem then gives

\[
\boxed{
\frac{R_N}{\sqrt N}
\Rightarrow
\mathcal R.
}
\]

So the square-root repair scale has a genuine, nondegenerate limit distribution.

---

## 6. P022-DL03 — the limit is not deterministic

A standard Brownian zero local time is nondegenerate; in particular it has nonzero variance

\[
1-\frac2\pi.
\]

The variance-asymptotic theorem independently computes

\[
\boxed{
\operatorname{Var}(\mathcal R)
=
7-\frac{6+8\sqrt2}{\pi}
>0.
}
\]

Thus no deterministic constant `c` satisfies

\[
R_N=c\sqrt N+o_{\Pr}(\sqrt N).
\]

The correct statement is a distributional one:

\[
\boxed{
R_N/\sqrt N
\text{ retains order-one random fluctuations.}
}
\]

This makes precise the earlier warning that a mean square-root budget is not a complete provisioning rule.

---

## 7. Mean and variance consistency

The Brownian variable has mean

\[
\boxed{
\mathbb E\mathcal R
=
\frac{2(1+\sqrt2)}{\sqrt\pi}.
}
\]

This matches the leading `sqrt(N)` coefficient of the exact microscopic mean.  The discrete mean additionally contains the lower-order correction

\[
-\frac1\pi\log N+O(1),
\]

which disappears after division by `sqrt(N)`.

Likewise

\[
\boxed{
\operatorname{Var}(\mathcal R)
=
7-\frac{6+8\sqrt2}{\pi},
}
\]

matching the independently derived discrete variance limit.

The agreement is a consistency check; the finite counting formulas remain the primary exact statements.

---

## 8. Weyl-chamber interpretation

The four lines

\[
S=0,
\quad
T=0,
\quad
U=0,
\quad
V=0
\]

are exactly the four reflection lines of the `B_2/C_2` signed-permutation arrangement after the cardinal rotation.

Thus `mathcal R` is a weighted total local-time functional of the limiting Brownian path against the reflection arrangement whose discrete orbit quotient generated the exact event-repair bits.

The discrete theorem

\[
|\operatorname{Lift}(h)|=2^{E(h)+B(h)}
\]

and the continuous limit

\[
R_N/\sqrt N\Rightarrow\mathcal R
\]

are therefore two scales of the same structure:

\[
\boxed{
\text{finite path-lift branching}
\longrightarrow
\text{reflection-wall local-time limit}.
}
\]

This is a P022 structural specialization.  Reflection groups, Brownian local times and invariance principles are prior art.

---

## 9. Precision consequence

At a long horizon, event-driven repair should not be summarized by any one of the following alone:

- worst-case repair `N+1`;
- mean repair;
- standard deviation;
- one quantile.

The normalized repair has a nontrivial limiting law whose randomness is generated by the wall-contact history of the coarse quotient path.

Therefore a future system that must provision repair resources at a declared confidence level needs the **repair distribution / wall-local-time state**, not merely a universal scalar precision parameter.

This is precisely the kind of task-relative distinction P018/P023/P024 may later abstract, but no general reflection-group repair theorem is claimed here.

---

## 10. Open frontier

The next P022-local questions are now sharper:

1. determine whether the Laplace transform or moments of `mathcal R` admit a useful closed form;
2. identify how much of the four-wall typed structure is lost when only total repair `E+B` is retained;
3. compare the `B_2/C_2` limit with higher-channel orbit quotients, where the earlier quadratic-history reconstruction already fails;
4. keep any general finite-group/reflection-group path-lifting theorem upstream-owned if the geometry assumptions disappear.
