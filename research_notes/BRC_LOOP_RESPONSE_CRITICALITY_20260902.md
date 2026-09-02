# BRC recurrent loop response, cycle-quotient Hessian, and exact criticality polynomial

Status: `RESEARCH CANDIDATE / EXACT RATIONAL-INTEGER RESPONSE GEOMETRY`
Date: `2026-09-02`
Research mode: `TASK_RESEARCH continuation`
Foundation baseline: `main@edfbeacb13d1fa741c76cd7a6db328bd1b324ad3`
Parent research: `BRC_RECURRENT_LOGDET_LOOP_ZETA_20260902.md`

## 0. Setup

Let `G=(V,E)` be a finite directed multigraph. Every branch edge

\[
e:a\to b
\]

has positive rational weight `q_e>0`. Let

\[
W_{ab}=\sum_{e:a\to b}q_e
\]

be the total one-step mass matrix. Assume the finite recurrent system is stable, so

\[
S:=W^\star=(I-W)^{-1}\in M_n(\mathbb Q_{\ge0}).
\]

The loop-zeta/log-surplus coordinate from the preceding checkpoint is

\[
Z_{\rm loop}(W)=\det(I-W)^{-1},
\qquad
\Gamma(W)=-\ln\det(I-W).
\]

This note studies the exact first/second response of `Gamma` to branch weights and the exact uniform criticality boundary.

Generic log-determinant differentiation, convexity of exponential sums, cycle/coboundary duality, and Collatz/Perron-type criticality are classical themes. No generic novelty claim is made. The project-specific objective is an exact rational/integer BRC interface.

## 1. Edge-loop response

Introduce formal/logarithmic edge coordinates

\[
\theta_e=\ln q_e.
\]

Jacobi differentiation gives

\[
d\Gamma=\operatorname{tr}(S\,dW).
\]

For one explicit branch edge `e:a->b`,

\[
\frac{\partial W}{\partial\theta_e}=q_eE_{ab}.
\]

Therefore

\[
\boxed{
R_e:=\frac{\partial\Gamma}{\partial\theta_e}
=q_eS_{ba}.
}
\]

This is rational even though `theta_e` is a logarithmic readout.

Because

\[
S_{ba}=\sum_{m\ge0}(W^m)_{ba},
\]

we have

\[
\boxed{
R_e
=\sum_{m\ge0}q_e(W^m)_{ba}.
}
\]

Interpretation: `R_e` is the total positive mass of all closed walks with a distinguished occurrence of the branch edge `e`, written as that edge followed by an arbitrary return walk from `b` to `a`.

Candidate theorem name:

`BRC_RECURRENT_EDGE_LOOP_RESPONSE`.

## 2. Exact recurrent-edge support detector

Since `q_e>0`,

\[
R_e>0
\iff
S_{ba}>0.
\]

For `a!=b`, `S_{ba}>0` iff there is a directed path from `b` back to `a`. For a self-loop `a=b`, `S_{aa}>=1`.

Hence

\[
\boxed{
R_e>0
\iff
\text{edge }e\text{ lies on a directed cycle}.
}
\]

Equivalently,

\[
\boxed{R_e=0\iff e\text{ is transient/feed-forward}.}
\]

Thus the gradient support of `Gamma` exactly recovers the recurrent edge core while ignoring all inter-SCC feed-forward edges.

Candidate theorem name:

`BRC_LOOP_RESPONSE_SUPPORT_EQUALS_RECURRENT_EDGE_CORE`.

## 3. Gauge invariance of individual edge response

For a positive vertex gauge `h_v>0`, transform

\[
q'_e=q_e\frac{h_b}{h_a},
\qquad
W'=H^{-1}WH,
\qquad H=\operatorname{diag}(h).
\]

Then

\[
S'=(I-W')^{-1}=H^{-1}SH,
\]

so

\[
S'_{ba}=S_{ba}\frac{h_a}{h_b}.
\]

Therefore

\[
\boxed{R'_e=q'_eS'_{ba}=q_eS_{ba}=R_e.}
\]

The edge-loop response is a gauge invariant **before** summing over edges.

This strengthens the preceding scalar statement `Gamma(W')=Gamma(W)`.

## 4. Total loop susceptibility

Sum edge responses:

\[
\chi(W):=\sum_{e\in E}R_e.
\]

Aggregating parallel edges gives

\[
\chi
=\sum_{a,b}W_{ab}S_{ba}
=\operatorname{tr}(WS).
\]

Since

\[
S-I=WS,
\]

we obtain

\[
\boxed{
\chi(W)=\operatorname{tr}(S-I).
}
\]

Using the Neumann expansion,

\[
\boxed{
\chi(W)=\sum_{k\ge1}\operatorname{tr}(W^k).
}
\]

It is also the uniform log-scale derivative. For

\[
W(t)=tW,
\qquad
\Gamma(t)=-\ln\det(I-tW),
\]

we have

\[
\boxed{
\frac{d\Gamma(t)}{d\ln t}
=\chi(tW).
}
\]

At `t=1`, `chi` is an exact rational recurrent susceptibility.

Because

\[
\Gamma=\sum_{k\ge1}\frac{\operatorname{tr}(W^k)}k,
\qquad
\chi=\sum_{k\ge1}\operatorname{tr}(W^k),
\]

we have

\[
0\le\Gamma\le\chi,
\]

with equality only in the acyclic case `Gamma=chi=0`: any positive directed cycle has positive repeated traversals, so at least one `k>=2` trace term is positive.

Candidate theorem name:

`BRC_RECURRENT_TOTAL_LOOP_SUSCEPTIBILITY`.

## 5. Exact Hessian formula

Let

\[
H_{ef}:=
\frac{\partial^2\Gamma}
{\partial\theta_e\partial\theta_f}.
\]

For

\[
e:a\to b,
\qquad
f:c\to d,
\]

use

\[
dS=S(dW)S.
\]

Then

\[
\boxed{
H_{ef}
=\delta_{ef}q_eS_{ba}
+q_eq_fS_{bc}S_{da}.
}
\]

The formula is manifestly symmetric because the off-diagonal product commutes after swapping `e,f`.

Every entry is rational.

Candidate theorem name:

`BRC_RECURRENT_LOOP_RESPONSE_HESSIAN`.

## 6. Positive semidefiniteness

The closed-walk expansion is

\[
\Gamma(\theta)
=\sum_{k\ge1}\frac1k
\sum_{w\in\mathcal C_k}
\exp\!\left(\sum_e n_e(w)\theta_e\right),
\]

where `C_k` is the set of marked-start closed walks of length `k` and `n_e(w)` is the number of occurrences of edge `e` in `w`.

Therefore for any real edge vector `v`,

\[
\boxed{
v^THv
=\sum_{k\ge1}\frac1k
\sum_{w\in\mathcal C_k}
q(w)
\left(\sum_e n_e(w)v_e\right)^2
\ge0.
}
\]

Thus `H` is positive semidefinite.

No probability interpretation is required. It is the exact quadratic closed-loop response of the positive branch mass.

## 7. Gauge kernel on a strongly connected recurrent core

A vertex potential `phi:V->R` defines the edge coboundary

\[
(d\phi)_e=\phi_b-\phi_a
\qquad(e:a\to b).
\]

Every closed walk telescopes, so

\[
\sum_{e\in w}d\phi_e=0.
\]

Hence

\[
H\,d\phi=0.
\]

Conversely, assume the positive-support digraph is strongly connected and

\[
v^THv=0.
\]

Every positive term in the displayed sum-of-squares formula must vanish, so the sum of `v_e` around every directed closed walk is zero.

Fix a root `r`. For every vertex `x`, choose a directed path `P:r->x` and define

\[
\phi_x=\sum_{e\in P}v_e.
\]

This is path-independent: if `P_1,P_2:r->x`, append the same directed return path `Q:x->r`; both `P_1Q` and `P_2Q` are closed, so their `v`-sums are zero and `P_1,P_2` have the same sum.

For every edge `e:a->b`, compare a root-to-`a` path plus `e` with a root-to-`b` path, using a common return path from `b` to `r`. This gives

\[
v_e=\phi_b-\phi_a.
\]

Therefore

\[
\boxed{
\ker H=\operatorname{im}d
}
\]

on a strongly connected support graph.

For `m=|E|`, `n=|V|`,

\[
\boxed{
\operatorname{rank}H=m-n+1.
}
\]

So `H` descends to a positive definite exact-rational quadratic form on the recurrent cycle/gauge quotient edge space.

Candidate theorem name:

`BRC_RECURRENT_CYCLE_QUOTIENT_POSITIVE_METRIC`.

This is a positive log-weight gauge statement only. It does not identify the quotient with signed/oriented holonomy carriers without an explicit typed bridge.

## 8. General graph kernel decomposition

For a general finite support graph:

- every edge not lying on a directed cycle has `R_e=0` and an identically zero Hessian row/column;
- `Gamma` decomposes additively across cyclic SCCs;
- Hessian cross-blocks between distinct SCCs vanish;
- inside each cyclic SCC, the kernel is exactly the vertex-gauge coboundary space.

Thus the nondegenerate recurrent response geometry is the direct sum of the cycle/gauge quotients of the cyclic SCCs.

Feed-forward transport is invisible to this metric even though it may substantially change the canonical state potential `x`.

## 9. Pure integer response formulas

Choose a common denominator `D` for all branch weights and write

\[
q_e=\frac{a_e}{D},
\qquad a_e\in\mathbb N_{>0}.
\]

Let the aggregated integer mass matrix be `A`, and put

\[
B=DI-A,
\qquad
\delta=\det B>0,
\qquad
C=\operatorname{adj}(B).
\]

From the preceding determinant synthesis,

\[
S=(I-W)^{-1}=\frac{D}{\delta}C.
\]

Hence

\[
\boxed{
R_e=\frac{a_eC_{ba}}\delta.
}
\]

For `e:a->b`, `f:c->d`,

\[
\boxed{
H_{ef}
=\frac{
\delta_{ef}a_eC_{ba}\delta
+a_ea_fC_{bc}C_{da}
}{\delta^2}.
}
\]

Therefore the entire gradient/Hessian response geometry is rational with a common determinant-controlled denominator.

Define the integer Hessian numerator

\[
K_{ef}
:=
\delta_{ef}a_eC_{ba}\delta
+a_ea_fC_{bc}C_{da}.
\]

Then

\[
H=K/\delta^2.
\]

Thus positive semidefiniteness and gauge-kernel claims can be certified after denominator clearing by a symmetric integer matrix.

Candidate theorem name:

`BRC_RECURRENT_INTEGER_RESPONSE_CERTIFICATE`.

## 10. Exact uniform criticality polynomial

Now drop the assumption that the unscaled system is stable and consider uniform scaling

\[
W(t)=tW,
\qquad t\ge0.
\]

For rational `W=A/D`, define the integer polynomial

\[
\boxed{
p(t)=\det(DI-tA)\in\mathbb Z[t].
}
\]

Let

\[
\mathcal S=\{t\ge0:tW\text{ is total-mass stable}\}.
\]

Stability is downward closed: if `tW h<h`, then `sW h<h` for `0<=s<=t` (strict for every `s<t`; if `t` is itself stable the same certificate applies at `s=t`).

If the support graph is acyclic, `W` is nilpotent after topological ordering. Then every `tW` is stable and

\[
p(t)=D^n.
\]

Assume the support contains a directed cycle. Repetition of any cycle of positive product gives a finite upper bound on stable `t`, so

\[
t_c:=\sup\mathcal S<\infty.
\]

For every `t<t_c`, `tW` is stable, so `I-tW` is invertible and `p(t)>0` by continuity from `p(0)=D^n>0`.

At `t=t_c`, `I-t_cW` must be singular. Otherwise its inverse is continuous near `t_c`; the stable canonical potentials

\[
x(t)=(I-tW)^{-1}\mathbf1\ge\mathbf1
\]

would converge to a positive vector at `t_c`, yielding stability there and, by strictness/openness, beyond `t_c`, contradiction.

Therefore

\[
\boxed{p(t_c)=0.}
\]

No smaller positive root exists because all `t<t_c` are stable/invertible.

Hence:

\[
\boxed{
\text{if recurrence exists, }t_c
=\text{the smallest positive real root of }p(t).
}
\]

This gives an exact algebraic criticality object without a floating eigenvalue oracle.

Candidate theorem name:

`BRC_RECURRENT_INTEGER_CRITICALITY_POLYNOMIAL`.

## 11. Exact rational susceptibility below criticality

For rational `t` with `0<t<t_c`,

\[
Z(t)=\frac{D^n}{p(t)}
\]

is rational, and

\[
\Gamma(t)=\ln Z(t).
\]

Differentiate with respect to `ln t`:

\[
\boxed{
\chi(t)
=\frac{d\Gamma(t)}{d\ln t}
=-\frac{t p'(t)}{p(t)}.
}
\]

This is an exact rational function at every rational stable scale.

The same quantity is

\[
\boxed{
\chi(t)=\operatorname{tr}((I-tW)^{-1}-I)
=\sum_{k\ge1}t^k\operatorname{tr}(W^k).
}
\]

If `t_c` is a root of multiplicity `r>=1`, then as `t->t_c^-`,

\[
\Gamma(t)\to+\infty,
\]

and

\[
\boxed{
\chi(t)\sim\frac{r t_c}{t_c-t}\to+\infty.
}
\]

Thus the determinant polynomial provides both the exact phase boundary and an exact rational susceptibility throughout the stable rational scales.

Candidate theorem name:

`BRC_RECURRENT_CRITICAL_SUSCEPTIBILITY`.

## 12. Rational certificate lower bounds on the critical scale

Any positive rational stability potential `h` defines

\[
\alpha(h)=\max_i\frac{(Wh)_i}{h_i}<1
\]

for the current stable scale.

Then for every

\[
0\le t<\frac1{\alpha(h)},
\]

we have

\[
tWh<h,
\]

so `tW` is stable.

Thus

\[
\boxed{
t_c\ge\frac1{\alpha(h)}.
}
\]

This is a rational certified lower bound whenever `W,h` are rational.

Optimizing this bound is related to the classical Collatz-Wielandt/Perron characterization and may require an irrational optimal ray even for rational `W`. Therefore this note does **not** promote a canonical rational optimizer. The exact algebraic critical root `p(t_c)=0` and finite rational certificates remain separately typed objects.

## 13. New structural split

The recurrent positive BRC layer now has three distinct exact objects:

```text
STATE POTENTIAL:
    x=(I-W)^(-1)1
    gauge-dependent / transient-sensitive

LOOP SURPLUS:
    Gamma=-ln det(I-W)
    gauge-invariant / SCC-additive / transient-blind

LOOP RESPONSE GEOMETRY:
    R_e=dGamma/dln(q_e)
    H_ef=d^2Gamma/dln(q_e)dln(q_f)
    gauge-invariant / recurrent-edge-supported
    positive definite on cycle/gauge quotient
```

Under uniform scaling, the integer criticality polynomial

\[
p(t)=\det(DI-tA)
\]

controls where the stable recurrent geometry ceases to exist as a finite positive-mass object.

## 14. Hard boundaries

This candidate does not claim:

- signed/amplitude response;
- complex logdet phase;
- infinite-state response geometry;
- a probability/Fisher interpretation of `H`;
- a canonical rational Perron/Collatz optimizer;
- that the positive cycle/gauge quotient is the same object as earlier signed/oriented holonomy;
- generic novelty of logdet derivatives, thermodynamic convexity, graph cohomology, or Perron criticality.

The intended project contribution is the exact rational/integer packaging and typed BRC synthesis.
