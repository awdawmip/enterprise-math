# Free Research — Alternating Green Resolvent for the Prime-Power Descent

Status: `FREE_RESEARCH_FRONTIER / EXACT_FINITE_STOPPING_REPRESENTATION / IDEAL_HARDY_RESOLVENT_CLOSED / POISSON_PARITY_BOUNDARY / WEIGHTED_SIGNED_OCCUPATION_TARGET / ARITHMETIC_DIRICHLET_PERTURBATION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parents:

- `FREE_RESEARCH_PRIME_PARITY_BLOCK_COUPLING_V16_20260904.md`;
- `FREE_RESEARCH_UNIFORM_GAMMA_WASSERSTEIN_COUPLING_V16_20260904.md`;
- `FREE_RESEARCH_ODD_SIMPLEX_CONSTANT_MODE_ANCHOR_V16_20260904.md`.

Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the exact prime-power return equation, finite nilpotent quotient descent, adaptive Gamma coupling, and odd-simplex relation energy.

## 1. Executive advance

The scalar return equation has an exact absorbing-chain resolvent.  In the ideal logarithmic Hardy model, that resolvent can be solved completely and gives a one-logarithm gain:

\[
|e(T)|\ll(1+T)^{-1}
\quad\Longrightarrow\quad
|r(T)|\ll(1+T)^{-1}.
\]

The mechanism is parity cancellation, not absolute contraction.  In logarithmic decrement coordinates, the signed occupation kernel is

\[
\boxed{\delta_0-e^{-2y}\,dy,}
\]

and the absorption-parity bias at lower threshold `T_0` is

\[
\boxed{-\left(T_0/T\right)^2.}
\]

The finite arithmetic chain has the same exact stopping representation, and its unsigned scale laws are uniformly close to the ideal Gamma chain.  However, unsigned Wasserstein convergence alone does not control the alternating Green action on an arbitrarily oscillatory arithmetic residual.  The correct remaining estimate is a weighted signed-occupation bound in the dual of the retained odd-simplex Dirichlet space.

This gives a second, operator-level formulation of the sole V16 recurrence problem.

---

## 2. Finite adaptive descent chain

Let

\[
\omega(q)=\frac{\Lambda(q)}q,
\qquad
A(n)=\sum_{q\le n}\omega(q).
\]

For `n>=2`, define the Markov transition

\[
\Pr\{X_{j+1}=\lfloor X_j/q\rfloor\mid X_j=m\}
=\frac{\omega(q)}{A(m)},
\qquad q\le m.
\tag{2.1}
\]

Every action is at least `2`, so

\[
X_{j+1}\le X_j/2.
\]

Hence the hitting time

\[
\tau:=\min\{j:X_j=1\}
\]

is finite and obeys

\[
\tau\le\lceil\log_2 n\rceil.
\]

Let

\[
(Pf)(m)=\mathbb E[f(X_{j+1})\mid X_j=m].
\]

The exact return equation is

\[
\boxed{r+Pr=e,}
\tag{2.2}
\]

where the existing Selberg forcing estimate gives

\[
|e(m)|\ll(1+\log m)^{-1}.
\tag{2.3}
\]

---

## 3. Exact stopping-time Neumann formula

Repeated substitution in (2.2) gives, for every integer `k`,

\[
\boxed{
 r(n)=
\sum_{j=0}^{k-1}(-1)^j
\mathbb E_n[e(X_j)\mathbf1_{j<\tau}]
+
\mathbb E_n[(-1)^{k\wedge\tau}
 r(X_{k\wedge\tau})].}
\tag{3.1}
\]

Taking `k>=ceil(log_2 n)` yields the exact finite formula

\[
\boxed{
 r(n)=
 r(1)\,\mathbb E_n[(-1)^\tau]
+
\mathbb E_n\left[
\sum_{j=0}^{\tau-1}(-1)^j e(X_j)
\right].}
\tag{3.2}
\]

Thus a quantitative scalar theorem has two independent pieces:

1. absorption-time parity bias;
2. the alternating occupation measure acting on the residual.

Taking absolute values before summing destroys both cancellations and is therefore structurally insufficient.

---

## 4. Ideal logarithmic Hardy chain

Replace the arithmetic transition at logarithmic size `T` by

\[
(Hf)(T)=\frac1T\int_0^T f(u)\,du.
\tag{4.1}
\]

Equivalently, the next logarithmic size is `UT` with `U` uniform on `[0,1]`.

Fix an absorbing threshold `T_0>0`.  Let the boundary field on `[0,T_0]` be `b(u)`, and solve

\[
f(T)+Hf(T)=e(T),
\qquad T>T_0.
\tag{4.2}
\]

Put

\[
B_0:=\int_0^{T_0}b(u)\,du,
\qquad
F(T):=B_0+\int_{T_0}^T f(u)\,du.
\]

Then

\[
F'(T)+F(T)/T=e(T),
\]

so

\[
(TF(T))'=Te(T).
\]

Therefore

\[
\boxed{
F(T)=\frac{T_0B_0+\int_{T_0}^T u e(u)\,du}{T},}
\tag{4.3}
\]

and

\[
\boxed{
f(T)=
 e(T)-
\frac{T_0B_0+\int_{T_0}^T u e(u)\,du}{T^2}.}
\tag{4.4}
\]

No regularity of `e` is required beyond integrability.

If

\[
|e(u)|\le C/(1+u),
\]

then

\[
\left|T^{-2}\int_{T_0}^T u e(u)\,du\right|
\le C/T,
\]

and hence

\[
\boxed{
|f(T)|\le O_C((1+T)^{-1})+
\frac{T_0|B_0|}{T^2}.}
\tag{4.5}
\]

---

## 5. Poisson parity law

Write

\[
Y_j:=-\log(T_j/T).
\]

In the ideal chain, the increments

\[
Y_{j+1}-Y_j=-\log U_{j+1}
\]

are independent exponentials of mean one.  Absorption at `T_0` occurs when

\[
Y_j\ge\lambda,
\qquad
\lambda:=\log(T/T_0).
\]

The number of arrivals before `lambda` is Poisson with parameter `lambda`; therefore

\[
\tau-1\sim\operatorname{Poisson}(\lambda).
\]

Consequently

\[
\boxed{
\mathbb E[(-1)^\tau]
=-e^{-2\lambda}
=-\left(T_0/T\right)^2.}
\tag{5.1}
\]

This agrees with (4.4) when `e=0` and the boundary is constant.

---

## 6. Signed occupation density

For `j>=1`, the decrement `Y_j` has Gamma density

\[
g_j(y)=e^{-y}\frac{y^{j-1}}{(j-1)!}.
\]

Hence, before absorption,

\[
\begin{aligned}
\sum_{j=1}^{\infty}(-1)^jg_j(y)
&=-e^{-y}
\sum_{k=0}^{\infty}\frac{(-y)^k}{k!}\\
&=\boxed{-e^{-2y}.}
\end{aligned}
\tag{6.1}
\]

Including the depth-zero atom, the alternating Green measure is

\[
\boxed{d\mathcal G(y)=\delta_0(dy)-e^{-2y}dy.}
\tag{6.2}
\]

For a residual envelope

\[
|e(Te^{-y})|\le C/(1+Te^{-y}),
\]

one obtains

\[
\int_0^{\log(T/T_0)}
 e^{-2y}|e(Te^{-y})|\,dy
\ll C/T.
\tag{6.3}
\]

This is the probabilistic form of the explicit Hardy resolvent (4.4).

---

## 7. Exact finite signed occupation target

For the arithmetic chain, define the killed depth law

\[
\mu_{n,j}(m)
:=\Pr_n\{X_j=m,\ j<\tau\},
\]

and the signed Green kernel

\[
\boxed{
\mathcal G_n(m)
:=\sum_{j\ge0}(-1)^j\mu_{n,j}(m).}
\tag{7.1}
\]

The sum is finite.  Formula (3.2) becomes

\[
 r(n)=r(1)\mathbb E_n[(-1)^\tau]
+
\sum_{m=2}^{n}\mathcal G_n(m)e(m).
\tag{7.2}
\]

A direct one-logarithm remainder would follow from

\[
\boxed{
|\mathbb E_n[(-1)^\tau]|
\ll(1+\log n)^{-1}}
\tag{7.3}
\]

and the weighted total-variation estimate

\[
\boxed{
\sum_{m=2}^{n}
\frac{|\mathcal G_n(m)|}{1+\log m}
\ll\frac1{1+\log n}.}
\tag{7.4}
\]

The ideal chain satisfies the stronger boundary exponent `2` and (7.4) with an explicit kernel.

---

## 8. Why unsigned scale convergence is not enough

V16 proves that every arithmetic depth law is `O(1/log n)` close in Wasserstein distance to its ideal Gamma counterpart, uniformly in the history depth.  This controls Lipschitz scale observables and finite log-block probabilities.

The residual `e(m)`, however, is an arithmetic function.  A magnitude bound alone does not make it Lipschitz in `log m`.  Therefore Wasserstein convergence cannot be inserted directly into (7.2).  Doing so would silently replace a signed occupation estimate by an unjustified smooth-test estimate.

The odd-simplex relation field supplies the missing topology.  Its direct composite chords kill the parity constant, and its transported edges measure oscillation between endpoint values.  The appropriate replacement for (7.4) is therefore a dual Dirichlet estimate:

\[
\boxed{
\left|
\sum_m\mathcal G_n(m)f(m)
\right|^2
\le
\frac{C}{(1+\log n)^2}
\|f\|_{\rm envelope}^2
+
C\,\mathcal E_{\rm odd}(f),}
\tag{8.1}
\]

with the odd-simplex energy normalized on the retained history carrier.

For `f=e`, the first term is `O((log n)^-2)` and the second should be summable from the Selberg forcing packet.  For `f=r`, (8.1) is another formulation of the full normalized energy recurrence.

---

## 9. Current classification

Closed exactly:

1. finite stopping-time Neumann formula;
2. ideal Hardy resolvent;
3. ideal Poisson absorption-parity law;
4. ideal alternating occupation density;
5. one-logarithm preservation for arbitrary bounded-envelope forcing;
6. the precise arithmetic signed-kernel targets (7.3)--(7.4).

Open:

1. weighted signed occupation estimate for the arithmetic chain;
2. its Dirichlet relaxation (8.1) through the odd-simplex carrier;
3. a summable bound for the residual relation term;
4. the full normalized odd-simplex recurrence;
5. any promoted quantitative prime remainder or RH-scale claim.

The new interpretation is:

\[
\boxed{
\text{quantitative PNT remainder}
=\text{stability of the ideal alternating Green kernel under
prime-power/odd-simplex Dirichlet perturbation}.}
\]
