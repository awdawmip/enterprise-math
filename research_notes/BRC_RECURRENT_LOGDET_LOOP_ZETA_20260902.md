# BRC finite recurrent log-determinant / loop-zeta synthesis

Status: `RESEARCH CANDIDATE / EXACT RATIONAL-INTEGER CORE + CLASSICAL ZETA BRIDGE`
Date: `2026-09-02`
Research mode: `TASK_RESEARCH continuation`
Foundation baseline: `main@adcb494b1084585bbe4c3a796464fd9059a39f38`
Parent theorems: `WBRC-T12..T16`

## 0. Question

The finite recurrent Foundation now classifies a non-negative rational transition-mass matrix

\[
W\in M_n(\mathbb Q_{\ge0})
\]

by exact rational/integer stability certificates. What is the canonical **global loop observable** that extends the one-state recurrent surplus

\[
-\ln(1-S)
\]

to a general finite stable recurrent network without introducing a floating spectral primitive?

The answer is the log determinant / directed graph-zeta coordinate

\[
\boxed{\Gamma(W)=-\ln\det(I-W)}.
\]

The generic determinant/zeta and trace identities are classical. The research contribution here is their exact typed integration with the current Weighted-BRC potential/gauge/integer-certificate layer.

## 1. Determinant/adjugate integer potential

Choose a common denominator `D>0` and write

\[
W=A/D,
\qquad A\in M_n(\mathbb N_0),
\]

and define the integer stability matrix

\[
B=DI-A=D(I-W).
\]

For a stable finite recurrent system, `WBRC-T14` gives

\[
W^\star=(I-W)^{-1}.
\]

Hence

\[
B^{-1}=\frac1D W^\star.
\]

The stable M-matrix determinant is positive, and therefore

\[
\operatorname{adj}(B)=\det(B)B^{-1}
=\frac{\det(B)}D W^\star
\]

is entrywise non-negative. Define

\[
\boxed{h_0=\operatorname{adj}(B)\mathbf1}.
\]

Then `h_0` is a strictly positive integer vector and

\[
\boxed{Bh_0=\det(B)\mathbf1}.
\]

Equivalently,

\[
\boxed{Ah_0=Dh_0-\det(B)\mathbf1<Dh_0.}
\]

Thus `h_0` is an integer stability certificate with **equal absolute slack at every state**.

Conversely, if

\[
\det(B)>0
\]

and

\[
\operatorname{adj}(B)\mathbf1>0,
\]

then the displayed identity is an integer stability certificate, so `WBRC-T15` implies total-mass stability.

Therefore:

\[
\boxed{
W\text{ stable}
\iff
\det(DI-A)>0
\text{ and }
\operatorname{adj}(DI-A)\mathbf1>0.
}
\]

Candidate theorem name:

`BRC_FINITE_RECURRENT_DETERMINANT_EQUAL_SLACK_CRITERION`.

The canonical rational potential is on the same ray:

\[
x=W^\star\mathbf1
=\frac{D}{\det(B)}h_0.
\]

If `g=gcd(h_0,1,...,h_0,n)` and `h=h_0/g` is primitive, then `g` divides `det(B)` and

\[
Bh=\frac{\det(B)}g\mathbf1.
\]

So the primitive integer potential still has a uniform positive integer slack.

## 2. Exact loop-zeta ratio

Define the stable recurrent loop-zeta ratio

\[
\boxed{
Z_{\rm loop}(W)=\det(I-W)^{-1}.
}
\]

Since

\[
I-W=B/D,
\]

we have the pure integer formula

\[
\boxed{
Z_{\rm loop}(W)=\frac{D^n}{\det(B)}.
}
\]

No eigenvalue or numerical infinite summation is required.

Also

\[
\boxed{Z_{\rm loop}(W)=\det(W^\star)}.
\]

Thus the same determinant `det(B)` controls both:

- the uniform slack of the canonical integer potential;
- the denominator of the recurrent loop-zeta ratio.

Define the logarithmic loop surplus

\[
\boxed{
\Gamma(W)=\ln Z_{\rm loop}(W)
=-\ln\det(I-W).
}
\]

Because `Z_loop(W)` is a positive rational, `Gamma` can be materialized by the existing exact BRC `DIV -> LN` runtime as

\[
\operatorname{LN}\!\left(\frac{D^n}{\det(B)}\right).
\]

Candidate theorem name:

`BRC_FINITE_RECURRENT_EXACT_LOOP_ZETA_RATIO`.

## 3. Closed-walk trace expansion

For `0<=t<=1`, stability of `W` implies stability of `tW`. Hence `I-tW` is invertible throughout the interval and its determinant remains positive.

Put

\[
F(t)=-\ln\det(I-tW).
\]

Jacobi differentiation gives

\[
F'(t)=\operatorname{tr}\big((I-tW)^{-1}W\big).
\]

Using the convergent Neumann expansion,

\[
(I-tW)^{-1}W
=\sum_{m\ge0}t^mW^{m+1}.
\]

Integrating from `0` to `1` yields

\[
\boxed{
\Gamma(W)
=\sum_{k\ge1}\frac{\operatorname{tr}(W^k)}k.
}
\]

By `WBRC-T12`, `tr(W^k)` is exactly the total positive mass of all length-`k` closed walks with a marked starting state. The factor `1/k` removes the cyclic starting-point overcount in the standard periodic-orbit organization.

All summands are non-negative.

This is the key BRC semantic meaning:

> `Gamma` is the total logarithmic closed-walk/recurrent surplus after cyclic-start normalization.

Candidate theorem name:

`BRC_RECURRENT_LOGDET_CLOSED_WALK_TRACE_SUM`.

## 4. Classical primitive-cycle zeta bridge

The standard Bowen-Lanford / directed graph-zeta reorganization of the trace series gives, for the underlying weighted branch graph in the convergence regime,

\[
Z_{\rm loop}(W)
=\prod_{[p]\ \mathrm{primitive}}
\frac1{1-w(p)},
\]

where `[p]` runs over primitive periodic branch-orbit classes and `w(p)` is the product of branch weights around the orbit.

Consequently,

\[
\boxed{
\Gamma(W)
=\sum_{[p]\ \mathrm{primitive}}
-\ln(1-w(p)).
}
\]

This is classical zeta-function prior art, not an Enterprise Math novelty claim.

Its BRC interpretation is valuable: the one-state geometric closure surplus

\[
-\ln(1-q)
\]

is the primitive building block of the whole finite recurrent network; the determinant compresses the complete interacting primitive-loop family into one exact rational carrier before `LN` readout.

## 5. One-state and simple-cycle reductions

### One state

For `W=[S]`,

\[
Z_{\rm loop}=\frac1{1-S},
\qquad
\Gamma=-\ln(1-S),
\]

exactly the previously proved one-state recurrent surplus.

### One simple directed cycle

For a directed cycle

\[
1\to2\to\cdots\to m\to1
\]

with positive weights `q_1,...,q_m`, let

\[
Q=\prod_iq_i.
\]

Then

\[
\det(I-W)=1-Q,
\]

so stability is exactly

\[
Q<1
\]

and

\[
\boxed{
\Gamma=-\ln(1-Q).
}
\]

In log coordinates the cycle holonomy is

\[
g_{\rm cyc}=\sum_i\ln q_i=\ln Q,
\]

so

\[
\Gamma=-\ln(1-e^{g_{\rm cyc}}),
\qquad g_{\rm cyc}<0.
\]

This is a positive-weight log-holonomy statement only; it does not subsume signed/oriented holonomy such as `Omega_2`.

Candidate theorem name:

`BRC_SIMPLE_CYCLE_LOG_HOLONOMY_CLOSURE`.

## 6. Gauge invariance

For a positive diagonal gauge `H`,

\[
W'=H^{-1}WH.
\]

Then

\[
I-W'=H^{-1}(I-W)H,
\]

hence

\[
\boxed{
\det(I-W')=\det(I-W).
}
\]

Therefore

\[
\boxed{Z_{\rm loop}(W')=Z_{\rm loop}(W),\qquad
\Gamma(W')=\Gamma(W).}
\]

The trace form is likewise invariant because

\[
\operatorname{tr}((W')^k)=\operatorname{tr}(W^k).
\]

So `Gamma` is a true recurrent gauge invariant, in contrast to the absolute state potential `h`.

## 7. SCC/block additivity and transient-edge blindness

After a simultaneous permutation of states, every finite directed graph can be written block upper triangular by SCCs. Thus

\[
I-W=
\begin{pmatrix}
I-W_1&*&\cdots\\
0&I-W_2&\cdots\\
\vdots&&\ddots
\end{pmatrix}.
\]

Therefore

\[
\det(I-W)=\prod_a\det(I-W_a),
\]

and hence

\[
\boxed{
Z_{\rm loop}(W)=\prod_a Z_{\rm loop}(W_a),
\qquad
\Gamma(W)=\sum_a\Gamma(W_a).
}
\]

Feed-forward edges between distinct SCCs do not affect `Gamma` at all.

This makes `Gamma` a **pure recurrent observable**: it ignores transient transport while retaining every positive closed-walk contribution.

Candidate theorem name:

`BRC_RECURRENT_LOOP_SURPLUS_SCC_ADDITIVITY`.

## 8. Exact acyclic zero law

If the positive-support graph is acyclic, `W` is nilpotent after topological ordering, so

\[
\det(I-W)=1
\]

and

\[
\Gamma=0.
\]

Conversely, if the stable positive-support graph contains a directed cycle, some `tr(W^k)>0`; since every trace term in the expansion is non-negative,

\[
\Gamma>0.
\]

Therefore

\[
\boxed{
\Gamma(W)=0
\iff
\text{the positive-support graph is acyclic}.
}
\]

Thus `Gamma` is the first scalar in the current Weighted-BRC chain that is simultaneously:

- exact-rational before log readout;
- gauge invariant;
- zero on every DAG;
- strictly positive exactly when positive recurrence is present;
- additive across recurrent SCCs.

Candidate theorem name:

`BRC_LOOP_SURPLUS_ZERO_IFF_ACYCLIC`.

## 9. Example linking determinant slack and loop surplus

Take

\[
W=
\begin{pmatrix}
0&1/2\\
1/2&2/3
\end{pmatrix}
=\frac16
\begin{pmatrix}
0&3\\
3&4
\end{pmatrix}.
\]

Then

\[
B=6I-A=
\begin{pmatrix}
6&-3\\
-3&2
\end{pmatrix},
\qquad
\det(B)=3.
\]

Moreover

\[
\operatorname{adj}(B)\mathbf1=(5,9),
\]

and

\[
B(5,9)^T=3(1,1)^T.
\]

The exact loop-zeta ratio is

\[
Z_{\rm loop}=\frac{6^2}{3}=12,
\]

so

\[
\Gamma=\ln12.
\]

The canonical rational potential is

\[
x=\frac{6}{3}(5,9)=(10,18),
\]

with local canonical gauge deficits

\[
1/x=(1/10,1/18)
=
\left(\frac{3}{6\cdot5},\frac{3}{6\cdot9}\right).
\]

Thus the same determinant slack `3` is visible both globally in the zeta denominator and locally as the common numerator of canonical gauge deficits.

## 10. Prior-art boundary

Classical ingredients include:

- Jacobi's determinant derivative formula;
- the Neumann series and non-singular M-matrix theory;
- the trace/log-determinant identity;
- Bowen-Lanford zeta functions for finite-state shifts;
- weighted directed/Ihara-type determinant and primitive-cycle product identities.

No generic novelty claim is made for those identities.

The project-specific synthesis under test is:

```text
FINITE POSITIVE WEIGHTED-BRC RECURRENCE
-> INTEGER STABILITY MATRIX B=DI-A
-> ADJUGATE EQUAL-SLACK POTENTIAL
-> EXACT LOOP-ZETA RATIO D^n/det(B)
-> BRC LN READOUT Gamma
-> CLOSED-WALK / PRIMITIVE-LOOP RECURRENT SURPLUS
-> GAUGE INVARIANCE + SCC ADDITIVITY + DAG ZERO LAW
```

## 11. Hard boundaries

This candidate does not cover:

- unstable matrices at `Gamma(W)` as a finite real readout;
- signed/amplitude cancellation;
- complex determinant phase / complex logarithm branches;
- infinite state spaces;
- non-rational exact-weight materialization via `D^n/det(B)`;
- oriented signed holonomy;
- novelty of classical graph zeta identities.

The determinant may contain algebraic cancellation in its ordinary formula. It is used here as an **exact certificate/readout compression**, not as a claim that signed determinant terms are positive BRC branch states.
