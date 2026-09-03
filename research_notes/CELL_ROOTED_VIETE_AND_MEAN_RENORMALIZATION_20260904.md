# Cell-rooted Viète product and geometric-harmonic mean renormalization

Status: `FREE_RESEARCH / EXACT FINITE IDENTITIES + GEOMETRIC COMPLETION / NOT FOUNDATION`  
Date: `2026-09-04`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Setup

Use the Cell-rooted rotor tower of order

\[
N_n=6\cdot2^n,
\]

with

\[
K_n=c_n+s_nJ,
\qquad
c_n^2+s_n^2=1,
\qquad
K_{n+1}^2=K_n.
\]

The first actual Cell/gate layer is `n=1`:

\[
c_1=\frac{\sqrt3}{2}=\frac{3r}{2},
\qquad
s_1=\frac12,
\qquad
r^2=\frac13.
\]

Define the inner and outer area readouts

\[
a_n=A_n^-=\frac{N_n}{2}s_n,
\]

\[
b_n=A_n^+=N_n\frac{s_n}{1+c_n}.
\]

The preceding theorem gives

\[
a_n<\pi<b_n,
\qquad
b_n-a_n=a_n\tau_n^2,
\qquad
\tau_n=\frac{s_n}{1+c_n}.
\]

At the exact physical anchor,

\[
\boxed{a_1=3},
\qquad
\boxed{b_1=12(2-\sqrt3)}.
\]

## 2. A Cell-rooted Viète product

The root relation gives

\[
s_n=2s_{n+1}c_{n+1}.
\]

Since `N_(n+1)=2N_n`,

\[
\begin{aligned}
a_n
&=\frac{N_n}{2}\,2s_{n+1}c_{n+1}\\
&=\frac{N_{n+1}}2s_{n+1}c_{n+1}\\
&=a_{n+1}c_{n+1}.
\end{aligned}
\]

Therefore

\[
\boxed{
a_{n+1}=\frac{a_n}{c_{n+1}}.
}
\]

Starting from `a_1=3`,

\[
\boxed{
a_n=\frac{3}{\prod_{k=2}^{n}c_k}.
}
\]

The longitudinal coordinates satisfy the target-free radical recursion

\[
c_{k+1}=\sqrt{\frac{1+c_k}{2}},
\qquad
c_1=\frac{\sqrt3}{2}.
\]

Hence

\[
c_2=\frac{\sqrt{2+\sqrt3}}2,
\]

\[
c_3=\frac{\sqrt{2+\sqrt{2+\sqrt3}}}{2},
\]

and so on. Taking the geometric completion `a_n -> pi` gives

\[
\boxed{
\frac3\pi
=
\frac{\sqrt{2+\sqrt3}}2
\frac{\sqrt{2+\sqrt{2+\sqrt3}}}{2}
\frac{\sqrt{2+\sqrt{2+\sqrt{2+\sqrt3}}}}{2}
\cdots.
}
\]

This is the Viète half-angle product rooted at the actual twelve-phase Cell/gate state rather than at the classical square. No historical novelty is claimed for the product identity itself; the project-specific content is the exact Cell origin of the seed `sqrt(3)/2` and of the finite baseline `3`.

In terms of the Cell radius,

\[
\sqrt3=3r,
\]

so the same product begins

\[
\frac3\pi
=
\frac{\sqrt{2+3r}}2
\frac{\sqrt{2+\sqrt{2+3r}}}{2}
\cdots.
\]

## 3. Exact two-sided recurrence without trigonometry

Let

\[
x=c_{n+1},
\qquad
y=s_{n+1}.
\]

Then

\[
c_n=2x^2-1,
\qquad
s_n=2xy.
\]

Writing `N=N_n`, one has

\[
a_n=Nxy,
\]

\[
b_n=N\frac{y}{x},
\]

\[
a_{n+1}=Ny,
\]

\[
b_{n+1}=2N\frac{y}{1+x}.
\]

It follows immediately that

\[
\boxed{
a_{n+1}^2=a_nb_n.
}
\]

Thus the next inner precision is the geometric mean:

\[
\boxed{
a_{n+1}=\sqrt{a_nb_n}.
}
\]

Further,

\[
\boxed{
b_{n+1}(a_{n+1}+b_n)=2a_{n+1}b_n,
}
\]

so

\[
\boxed{
b_{n+1}
=\frac{2a_{n+1}b_n}{a_{n+1}+b_n}.
}
\]

The next outer precision is therefore the harmonic mean of the new inner precision and the old outer precision.

Starting only from

\[
\boxed{
(a_1,b_1)
=
\left(3,12(2-\sqrt3)\right),
}
\]

one obtains the complete target-free precision tower by

\[
\boxed{
\begin{aligned}
a_{n+1}&=\sqrt{a_nb_n},\\
b_{n+1}&=\frac{2a_{n+1}b_n}{a_{n+1}+b_n}.
\end{aligned}
}
\]

Every operation is algebraic and no value of `pi` is used.

## 4. Strict interlacing

Because `0<x<1`,

\[
a_n=xa_{n+1}<a_{n+1},
\]

\[
\frac{b_{n+1}}{a_{n+1}}=\frac2{1+x}>1,
\]

and

\[
\frac{b_{n+1}}{b_n}=\frac{2x}{1+x}<1.
\]

Therefore

\[
\boxed{
a_n<a_{n+1}<b_{n+1}<b_n.
}
\]

The common limit is the Cell polygon completion and hence geometric `pi`.

## 5. Reciprocal arithmetic-geometric microsteps

Define reciprocal bounds

\[
\alpha_n=\frac1{b_n},
\qquad
\gamma_n=\frac1{a_n}.
\]

Then

\[
\boxed{
\gamma_{n+1}=\sqrt{\alpha_n\gamma_n}
}
\]

and

\[
\boxed{
\alpha_{n+1}
=\frac{\alpha_n+\gamma_{n+1}}2.
}
\]

Thus polygon doubling factors into two mean operations:

```text
old reciprocal outer + old reciprocal inner
  -> geometric update of the inner reciprocal
  -> arithmetic update using the new geometric state.
```

This is an asynchronous arithmetic-geometric mean flow. It explains why the Gauss-Legendre/AGM line is naturally adjacent to the Euler-Viète line, while preserving the distinction from the standard simultaneous AGM iteration.

## 6. Exact residual budget

The first width is

\[
\begin{aligned}
w_1
&=b_1-a_1\\
&=12(2-\sqrt3)-3\\
&=21-12\sqrt3.
\end{aligned}
\]

The polygon theorem gives

\[
\frac{w_{n+1}}{w_n}<\frac14.
\]

Therefore

\[
\boxed{
0<\pi-a_n<w_n
\le\frac{21-12\sqrt3}{4^{n-1}}.
}
\]

Similarly,

\[
0<b_n-\pi<w_n.
\]

Hence the exact statement “ignore residual gives `pi=3`” has a rigorous interpretation:

- the C12 Cell/gate layer resolves exactly the lower value `3`;
- every deeper rotation refinement contributes a positive algebraic correction;
- all unresolved corrections after level `n` lie inside a certified interval of width at most `(21-12sqrt(3))/4^(n-1)`.

## 7. Physical Cell area

The physical Cell radius obeys `r^2=1/3`, so its completed circular area is

\[
\operatorname{Area}(\text{Cell})=\frac\pi3.
\]

The exact C12 inscribed dodecagon already has area one. Therefore

\[
\boxed{
\operatorname{Area}(\text{Cell})
=1+\frac{\pi-3}{3}.
}
\]

The first unresolved physical area residual is bounded by

\[
0<\frac{\pi-3}{3}
<\frac{21-12\sqrt3}{3}
=7-4\sqrt3.
\]

At level `n`, the physical area interval is

\[
\boxed{
\frac{a_n}{3}
<
\operatorname{Area}(\text{Cell})
<
\frac{b_n}{3}.
}
\]

This makes the finite/continuous distinction literal: the finite Cell geometry contributes an exact polygonal area plus a shrinking residual annulus.

## 8. Relation to Euler's identity

At every level,

\[
K_n^{N_n/2}=-1.
\]

The same rotor that generates the area bounds therefore carries an exact finite half-turn identity. The common area limit `pi` is also its half-period phase length under the unique character completion.

Consequently the Viète product, the polygonal precision tower and Euler's identity are three readouts of one root process:

\[
\boxed{
\begin{aligned}
K_{n+1}^2=K_n
&\Longrightarrow c_{n+1}=\sqrt{(1+c_n)/2},\\
&\Longrightarrow a_{n+1}=\sqrt{a_nb_n},\\
&\Longrightarrow 3/\pi=\prod_{k\ge2}c_k,\\
&\Longrightarrow \operatorname{Exp}_J(\pi)=-1.
\end{aligned}
}
\]

## 9. Boundary

1. The geometric/harmonic recurrence and generalized Viète product are classical consequences of regular polygon doubling; no historical priority is claimed.
2. The Enterprise contribution is the typed derivation of the initial C12 rotor, the exact baseline `3`, the unit physical dodecagon, and the common embedding into the Cell-derived Euler character chain.
3. The standard AGM should not be declared identical to the staggered reciprocal iteration without an explicit conjugacy theorem.
4. This result remains at the carrier/character readout layer and does not redefine the primitive native metric.

Candidate freeze:

`AC-EM-FREE-F6D046-CELL-ROOTED-VIETE-MEAN-RENORMALIZATION-V1`:

> The actual C12 Cell/gate rotor supplies exact inner/outer precision values 3 and 12(2-sqrt(3)). Dyadic rotation roots update the lower value by a geometric mean and the upper value by a harmonic mean, producing a strictly nested target-free interval tower with common completion pi. Equivalently, the longitudinal root coordinates give the Cell-rooted Viète product 3/pi, while reciprocals form an alternating geometric-arithmetic mean flow.