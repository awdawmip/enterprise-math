# PREFIX-676-R6 — Stochastic order and diagonal slot-phase transition for the frozen BRC observer

Date: 2026-11-10, Asia/Shanghai. Role: independent TASK_RESEARCH. Researcher-ID: EM-DIRECT-1659EA; Research-Activity-ID: RA-467440BA332695697F2EBC2F.

Scientific input: frozen pin f42f2906d77f24085c123f3ccfe9667d41caa96d. Status: AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. The two real probabilities p,z parametrize an observer of the Heartbeat World X6 first-stop process, rather than two primitive spatial dimensions. This is a mathematical result about the frozen observer.

## Problem and definitions

PREFIX-675 certified the entire p=0 edge. To extend exclusion to the two-variable domain we need to understand how observer variance changes when a second nonzero parameter is introduced.

Let A_n(k) be the original signed-path survivor multiplicities, at levels n=0,...,188, and define

\[
s_n(x)=\sum_{k=0}^{n}A_n(k)x^k(1-x)^{n-k},\quad 0\le x\le\tfrac12.
\]

Let Y_x denote the associated Poissonized first-stop time. The two clocks Y_p,Y_z are independent. Define

\[
Y(p,z)=\max(Y_p,Y_z),\qquad
\mu(p,z)=E[Y(p,z)],\quad W(p,z)=\operatorname{Var}(Y(p,z)),
\]
\[
V_q(p,z)=q^2 W(p,z)-q\mu(p,z),\qquad 12\le q\le24.
\]

## Theorem 676.1: marginal stochastic monotonicity

For every real 0<=x<=y<=1/2 and t>=0,

\[
\Pr(Y_x>t)\le\Pr(Y_y>t).
\]

Consequently the independent-clock maximum Y(p,z), and its mean, are stochastically nondecreasing in either p or z on [0,1/2] with the other parameter fixed.

**Exact proof.** Set c_{n,k}=A_n(k)/binom(n,k). The original recurrence produces 190 rows n=0,...,189; row 189 is empty. For every n<=188, symmetry gives c_{n,k}=c_{n,n-k}, and 8,836 checked integer cross-products verify

\[
A_n(k+1)\binom nk \ge A_n(k)\binom n{k+1}
\qquad(1\le n\le188,\ 0\le k<\lfloor n/2\rfloor).
\]

Thus the Bernstein coefficients c_{n,k} are symmetric and nondecreasing toward the center. Differentiation gives

\[
s_n'(x)=n\sum_{k=0}^{n-1}\binom{n-1}{k}
(c_{n,k+1}-c_{n,k})x^k(1-x)^{n-1-k}.
\]

Pair k with n-1-k. Symmetry makes the two coefficient differences opposites. For 0<=x<=1/2 the lower-index Bernstein weight is at least its reflected weight, so every pair contributes nonnegatively. Any unpaired central term is zero. Hence s_n'(x)>=0 throughout [0,1/2].

The frozen Poisson clock has the exact survival series

\[
\Pr(Y_x>t)=e^{-t}\sum_{n=0}^{188}s_n(x)\frac{t^n}{n!}.
\]

Every summand respects the ordering. The maximum's survival is
1-(1-Pr(Y_p>t))(1-Pr(Y_z>t)), also nondecreasing in each survival argument. This proves the theorem for the whole declared parameter interval.

## Theorem 676.2: exact variance comparison and a slot transition

For z in [0,1/2] write

\[
\Delta\mu(z)=\mu(z,z)-\mu(0,z),\qquad
\Delta W(z)=W(z,z)-W(0,z),
\]
\[
D_q(z)=V_q(z,z)-V_q(0,z)
      =q\bigl(q\Delta W(z)-\Delta\mu(z)\bigr).
\]

Define the three rational comparison points

\[
a=\frac{13}{250}=0.052,\quad
b=\frac{53}{1000}=0.053,\quad
c=\frac{27}{500}=0.054.
\]

The exact Fraction certificate returns the following **integer floors**, obtained from exact rational D_q values:

| z | floor(D_12(z)) | floor(D_24(z)) |
|---|---:|---:|
| 13/250 | 207 | 1015 |
| 53/1000 | -32 | 63 |
| 27/500 | -280 | -927 |

Moreover, at b=53/1000 the exact inequalities are

\[
\Delta W(b)>0,\qquad
17\Delta W(b)<\Delta\mu(b)<18\Delta W(b).
\]

The exact ratio

\[
q_0=\frac{\Delta\mu(b)}{\Delta W(b)}
\]

therefore lies strictly between 17 and 18, with the **unique** slot-sign transition for this fixed b:

\[
D_q(b)<0\ (12\le q<q_0),\quad
D_{q_0}(b)=0,\quad
D_q(b)>0\ (q_0<q\le24).
\]

For every real q in [12,24], at least one diagonal-edge crossover exists:

\[
\exists z_q\in(13/250,27/500):\quad D_q(z_q)=0.
\]

For the two practical slot schemes the brackets separate:

\[
\exists z_{12}\in(13/250,53/1000):D_{12}(z_{12})=0,
\]
\[
\exists z_{24}\in(53/1000,27/500):D_{24}(z_{24})=0.
\]

These are **existence** statements; uniqueness in z is not asserted.

**Exact proof.** For a/d rational, the finite survivor probabilities are

\[
s_n(a/d)=d^{-n}\sum_k A_n(k)a^k(d-a)^{n-k}.
\]

Define the exact Gamma-minimum kernels

\[
w_{nm}=\frac{\binom{n+m}{n}}{2^{n+m+1}},
\qquad
g_{nm}=\frac{n+m+1}{2}w_{nm}.
\]

With indices 0<=n,m<=188 the first two moments of the independent maximum are

\[
\mu(p,z)=\sum_n(s_n(p)+s_n(z))
          -\sum_{n,m}w_{nm}s_n(p)s_m(z),
\]

\[
E[Y(p,z)^2]/2
=\sum_n(n+1)(s_n(p)+s_n(z))
 -\sum_{n,m}g_{nm}s_n(p)s_m(z).
\]

All summands are rational, so Delta-mu, Delta-W and D_12,D_24 at a,b,c are computed exactly. Integer numerator tests produce the strict signs and at b the inequalities 17 Delta-W < Delta-mu < 18 Delta-W.

For each fixed z, D_q(z)/q=q Delta-W(z)-Delta-mu(z) is affine in real q. Both endpoint values are strictly positive at a and strictly negative at c; hence the same signs hold for every q in [12,24]. Polynomial continuity in z and the intermediate-value theorem give a zero inside (a,c). At b the endpoint q=12 comparison is negative and q=24 positive, yielding the two shorter existential brackets. QED.

## Reproduction and interpretation

The companion Python script
research_notes/portable_direct/PREFIX676_R6_STOCHASTIC_ORDER_AND_DIAGONAL_CROSSING.py
regenerates the original frozen 189-layer recursion using only integers and Fraction; its stdout is the companion JSON
research_notes/portable_direct/PREFIX676_R6_RESULTS.json.

The local author run verified 8,836 exact normalized-Bernstein coefficient inequalities, survivor reflection, 9,529 nonzero histogram cells, extinction at layer 189, six exact signed comparisons and the exact slot threshold bounds. Reported decimal-scaled floors and numerator/denominator bit lengths are audit summaries; the comparisons themselves use exact rational arithmetic.

**Research use.** Stochastic increase of Y and its mean does not imply monotonicity of the variance objective: at z=13/250 the diagonal wins, while at z=27/500 the edge wins, uniformly in q in [12,24]. The slot threshold at z=53/1000 provides a new exact partition for testing a two-dimensional Bernstein branch-and-bound search and rejects a blanket coordinatewise monotonic pruning assumption.

**Next unresolved scientific unit.** Compare each interior box's certified upper bound against the complete boundary optimum from PREFIX-675. Start with p>=1/64 and with z outside the previously certified strip. Treat the diagonal crossing as a regression witness when constructing interval pruning rules; retain the frozen science pin.

Sources: predecessor PREFIX-675 at Enterprise Math commit c8d034bda669497d88a53ecf4cae67d6bff4ff76; Source docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d. This independent artifact creates no shared CLAIM, Result, Review or Foundation admission.
