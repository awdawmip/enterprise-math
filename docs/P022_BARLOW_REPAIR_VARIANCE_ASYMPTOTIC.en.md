# P022 — Total Event-Repair Variance Has an Exact Linear Asymptotic

Status: `ACTIVE RESEARCH NOTE / PROVED ASYMPTOTIC USING CLASSICAL LOCAL-TIME INVARIANCE / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: exact two-sided event repair; rotated `Z^2` four-wall representation; exact orientation variance; total-variance upper bound  
Cross-route relevance: P018/P023/P024 event-driven repair, observation-history uncertainty, quotient-path lifting

## 1. Question

The exact two-sided repair dimension is

\[
R_N=E_N+B_N,
\]

where `E_N` counts orientation bits released from the two sign walls and `B_N` counts side-label bits released from the two exchange walls.

Previous P022 results prove

\[
\mathbb E R_N=\Theta(\sqrt N)
\]

and

\[
\operatorname{Var}(R_N)=O(N).
\]

The missing question was whether mixed wall covariance could cancel the linear orientation variance strongly enough to make total variance sublinear.

It cannot.  In fact the variance has an exact positive linear constant.

---

## 2. Microscopic signed walks and the cardinal rotation

Let

\[
S_t=\sum_{j=1}^t\sigma_j,
\qquad
T_t=\sum_{j=1}^t\tau_j,
\]

where the microscopic signs `sigma_j,tau_j` are independent and uniformly distributed in `{−1,+1}` under the finite microscopic counting measure.

Define the integer rotation

\[
\boxed{
U_t=\frac{S_t+T_t}{2},
\qquad
V_t=\frac{S_t-T_t}{2}.
}
\]

At every microscopic step exactly one of `U,V` moves by `±1` and the other remains fixed.  Thus `(U,V)` is the standard cardinal walk on `Z^2`.

For horizon `N`, define wall local times at pre-step times `0,...,N-1`:

\[
A_S=\sum_{t=0}^{N-1}\mathbf1_{\{S_t=0\}},
\qquad
A_T=\sum_{t=0}^{N-1}\mathbf1_{\{T_t=0\}},
\]

\[
A_U=\sum_{t=0}^{N-1}\mathbf1_{\{U_t=0\}},
\qquad
A_V=\sum_{t=0}^{N-1}\mathbf1_{\{V_t=0\}}.
\]

The orientation component is exactly

\[
\boxed{E_N=A_S+A_T.}
\]

The split component is almost half of the two coordinate-axis local times.  The next sections quantify the difference exactly enough for variance asymptotics.

---

## 3. P022-VA01 — split repair equals half-axis local time plus an `L^2`-negligible correction

At time `t`, let `J_t^U` be the indicator that the next cardinal step moves the `U` coordinate; then

\[
J_t^U+J_t^V=1,
\qquad
\mathbb E[J_t^U\mid\mathcal F_t]
=\mathbb E[J_t^V\mid\mathcal F_t]
=\frac12.
\]

Let

\[
C_N=\sum_{t=0}^{N-1}\mathbf1_{\{U_t=V_t=0\}}
\]

be the cardinal-walk origin local time.

If `U_t=0,V_t!=0`, a split bit is created exactly when the next step moves `U`; similarly with `U,V` exchanged.  If `U_t=V_t=0`, moving either coordinate does **not** create a split bit.

Hence, with

\[
M_N=
\sum_{t=0}^{N-1}
\left[
\mathbf1_{\{U_t=0\}}\left(J_t^U-\frac12\right)
+
\mathbf1_{\{V_t=0\}}\left(J_t^V-\frac12\right)
\right],
\]

we have the exact identity

\[
\boxed{
B_N=\frac12(A_U+A_V)+M_N-C_N.
}
\]

The summands of `M_N` are martingale differences.  At the origin their sum is exactly zero, while on exactly one coordinate axis the increment is `±1/2`. Therefore

\[
\mathbb E[M_N^2]
\le
\frac14\mathbb E[A_U+A_V]
=O(\sqrt N).
\]

For the origin local time, write

\[
q_t=\Pr(U_t=V_t=0).
\]

Since this is the simultaneous return of the independent walks `S,T`, `q_t=0` at odd `t` and

\[
q_{2j}=\left(\frac{\binom{2j}{j}}{4^j}\right)^2=O(j^{-1}).
\]

The Markov property gives

\[
\mathbb E[C_N^2]
=
\sum_{t<N}q_t
+2\sum_{0\le s<t<N}q_s q_{t-s}
=O((\log N)^2).
\]

Consequently

\[
\boxed{
\mathbb E\left[
B_N-\frac12(A_U+A_V)
\right]^2
=o(N).
}
\]

Define the four-wall surrogate

\[
\boxed{
W_N=A_S+A_T+\frac12(A_U+A_V).
}
\]

Then

\[
\boxed{
\mathbb E[(R_N-W_N)^2]=o(N).
}
\]

Since the previous variance bound gives `E[W_N^2]=O(N)` as well, this implies

\[
\boxed{
\frac{\operatorname{Var}(R_N)-\operatorname{Var}(W_N)}{N}\to0.
}
\]

So the linear variance constant is completely determined by four one-dimensional wall local times.

---

## 4. Prior-art input: random-walk local time invariance

The required asymptotic input is classical.

For a recurrent centered one-dimensional random walk with finite variance, diffusive rescaling of its discrete local-time process converges to Brownian local time.  One canonical reference is:

A. N. Borodin, *An asymptotic behaviour of local times of a recurrent random walk with finite variance*, Teor. Veroyatnost. i Primenen. 26:4 (1981), 769–783; English translation, Theory of Probability and its Applications 26:4 (1982), 758–772, DOI `10.1137/1126082`.

P022 does not claim this invariance principle.

Here it is applied only to the finite family of linear projections `S,T,U,V` of the same two-dimensional microscopic walk.  Equivalently, the cross second moments below can be recovered directly from the corresponding two-variable local central-limit sums.  The project-specific content is the identification of the repair observable with this four-wall local-time combination.

---

## 5. Brownian cross-local-time lemma

Let `X,Y` be standard Brownian motions with instantaneous correlation `rho`, `|rho|<1`, and let `L_X,L_Y` be their local times at zero through time one in the occupation-density normalization.

For `s<=t`, the joint density at `(0,0)` is

\[
\frac{1}{2\pi\sqrt{s(t-\rho^2s)}}.
\]

Therefore

\[
\begin{aligned}
\mathbb E[L_XL_Y]
&=
2\int_0^1\int_s^1
\frac{dt\,ds}{2\pi\sqrt{s(t-\rho^2s)}}\\
&=
\frac{2}{\pi}
\frac{\arcsin|\rho|}{|\rho|}.
\end{aligned}
\]

with the continuous extension `2/pi` at `rho=0`.

For `|rho|=1/sqrt(2)`,

\[
\arcsin(1/\sqrt2)=\frac\pi4,
\]

so

\[
\boxed{
\mathbb E[L_XL_Y]=\frac1{\sqrt2}.
}
\]

This integral is elementary once the Brownian local-time limit is available.

---

## 6. P022-VA02 — the four wall covariance constants

The diffusive limits of the four projections are generated from two independent standard Brownian motions `B_1,B_2`:

\[
S\rightsquigarrow B_1,
\qquad
T\rightsquigarrow B_2,
\]

\[
U\rightsquigarrow\frac{B_1+B_2}{2},
\qquad
V\rightsquigarrow\frac{B_1-B_2}{2}.
\]

The standard facts

\[
\mathbb E[L_1^0(B)]=\sqrt{\frac2\pi},
\qquad
\mathbb E[(L_1^0(B))^2]=1
\]

give

\[
\boxed{
\frac{\operatorname{Var}(A_S)}{N}	o1-\frac2\pi,
}
\]

and the same for `A_T`.

Because `U` has variance rate `1/2`, its local time is scaled by `sqrt(2)`, so

\[
\boxed{
\frac{\operatorname{Var}(A_U)}{N}	o
2\left(1-\frac2\pi\right),
}
\]

and similarly for `A_V`.

The two original walks are independent, hence

\[
\operatorname{Cov}(A_S,A_T)=0.
\]

The two rotated Brownian projections are orthogonal, so

\[
\boxed{
\frac{\operatorname{Cov}(A_U,A_V)}{N}\to0.
}
\]

Each original/rotated pair has absolute normalized correlation `1/sqrt(2)`.  Correcting for the variance-rate `1/2` of the rotated coordinate, the cross second moment tends to `1`, while the product of the means tends to `2sqrt(2)/pi`. Hence for each of the four pairs

\[
(S,U),\ (S,V),\ (T,U),\ (T,V),
\]

we obtain

\[
\boxed{
\frac{\operatorname{Cov}(A_{\rm original},A_{\rm rotated})}{N}
\to
1-\frac{2\sqrt2}{\pi}.
}
\]

This constant is positive.

---

## 7. P022-VA03 — exact linear variance constant

Now expand

\[
W_N=A_S+A_T+\frac12A_U+\frac12A_V.
\]

The self-variance contribution is

\[
2\left(1-\frac2\pi\right)
+2\cdot\frac14\cdot
2\left(1-\frac2\pi\right)
=
3\left(1-\frac2\pi\right).
\]

There are four original/rotated cross pairs, each carrying coefficient `1/2` inside `W_N`.  Their total covariance contribution is

\[
2\cdot4\cdot\frac12
\left(1-\frac{2\sqrt2}{\pi}\right)
=
4-\frac{8\sqrt2}{\pi}.
\]

Therefore

\[
\boxed{
\frac{\operatorname{Var}(W_N)}{N}
\to
7-\frac{6+8\sqrt2}{\pi}.
}
\]

By VA01 the same limit holds for the exact repair variable:

\[
\boxed{
\lim_{N\to\infty}
\frac{\operatorname{Var}(R_N)}{N}
=
7-\frac{6+8\sqrt2}{\pi}.
}
\]

Numerically,

\[
7-\frac{6+8\sqrt2}{\pi}
\approx1.4888754182688317>0.
\]

Hence

\[
\boxed{
\operatorname{Var}(R_N)=\Theta(N),
\qquad
\operatorname{sd}(R_N)=\Theta(\sqrt N).
}
\]

This closes the lower-bound question left open by the previous variance-bound note.

---

## 8. Relation to the mean scale

The microscopic mean satisfies

\[
\mathbb E R_N
=
\frac{2(1+\sqrt2)}{\sqrt\pi}\sqrt N
-\frac1\pi\log N
+O(1).
\]

The standard deviation has leading scale

\[
\sqrt{
7-\frac{6+8\sqrt2}{\pi}
}
\sqrt N.
\]

Therefore relative fluctuations do not vanish:

\[
\boxed{
\frac{\operatorname{sd}(R_N)}{\mathbb E R_N}
\to
\frac{
\sqrt{7-(6+8\sqrt2)/\pi}
}{2(1+\sqrt2)/\sqrt\pi}
>0.
}
\]

So event-driven repair is sublinear compared with the raw `2N` microscopic sign bits, but it is **not sharply concentrated around a deterministic square-root budget**.

Mean repair, typical fluctuation scale, high-repair tail and worst-case repair remain distinct precision observables.

---

## 9. Why the finite covariance sign changes do not contradict the theorem

The exact finite covariance

\[
\operatorname{Cov}(E_N,B_N)
\]

changes sign at small and moderate horizons.  That is a genuine finite boundary and remains recorded.

VA03 does not assume this covariance is nonnegative.  Instead it replaces `B_N` by its axis-local-time principal part in `L^2`, computes the four-wall covariance matrix at diffusive scale, and only then takes the large-`N` limit.

Thus finite sign oscillation and positive asymptotic cross-wall contribution can coexist.

---

## 10. Precision consequence

The two-sided Barlow quotient now has four quantitatively separated repair scales:

- exact fiber: `2^(E+B)`;
- microscopic mean repair: `Theta(sqrt(N))` with a logarithmic correction;
- repair standard deviation: `Theta(sqrt(N))` with the explicit VA03 constant;
- worst repair: `N+1`.

The important architectural point is:

> event-driven compression removes linear *average* repair growth, but does not collapse uncertainty to a deterministic scalar budget; wall-local-time fluctuations survive at the same square-root scale as the mean.

This is a P022/A5 specialization.  A general theorem about quotient-path repair should be owned upstream only after stating the hypotheses that make a coarse path liftable by finitely many stabilizer-release local times.

---

## 11. Prior-art boundary

Established ingredients include:

- finite-variance random-walk invariance principles;
- Brownian local time;
- occupation-density formulas;
- central/local limit theorems;
- reflection/Weyl-group chambers.

The specific local-time invariance theorem used here is classical Borodin prior art as cited above.

P022-specific content is the exact decomposition of Barlow event repair into four wall local times plus an `L^2`-negligible thinning/origin correction, and the resulting explicit variance constant for this quotient repair state.

Historical novelty of that combination remains `NOVELTY_UNVERIFIED`.
