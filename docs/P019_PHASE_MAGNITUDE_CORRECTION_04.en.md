# P019 — Correction 04: Finite-Precision Magnitude Must Not Erase Causal Phase

Status: `ACTIVE CORRECTION / SUPERSEDING INTERPRETATION NOTE`  
Corrects: the overstrong physical reading in the first P019 stage that directly called the finite-width `q_lambda=0` region a “horizon basin”  
Mathematical status: the first-stage arithmetic results for the `q_lambda=0` interval, width, projection, and singleton threshold remain valid; what changes is their **physical semantics**.

## 1. Core correction

The first stage defined

\[
q_\lambda(n;h)
=
\left\lfloor\frac{\lambda|n-h|}{n}\right\rfloor
\]

and proved that

\[
H_\lambda(h)=\{n:q_\lambda(n;h)=0\}
\]

is a finite integer interval that shrinks as precision increases.

That set is real within the model. But interpreting it directly as a physically thickened event horizon is insufficient because the absolute value has deleted the most important causal information:

\[
\boxed{
\epsilon(n;h)=\operatorname{sgn}(n-h).
}
\]

For `n<h`, `n=h`, and `n>h`, even when `q_lambda` has collapsed to `0`, `epsilon` remains

\[
-1,\quad0,\quad+1.
\]

The corrected statement is therefore:

> **`H_lambda(h)` is a zero-resolvable magnitude/clock-rate basin. It is not automatically the causal horizon itself. The exact horizon is first a phase boundary.**

## 2. P019-PM-T01 — The correct finite-precision state is phase × magnitude, not their signed product

Status: `PROVED / DESIGN CORRECTION`

Define

\[
\boxed{
O_\lambda(n;h)
=
(\epsilon(n;h),q_\lambda(n;h)).
}
\]

The ordered pair must be retained. Keeping only

\[
\epsilon q
\]

would collapse

\[
(-1,0),\quad(0,0),\quad(+1,0)
\]

to the same integer `0` whenever the magnitude vanishes.

This is exactly consistent with the P006 lesson that direction/sign and nonnegative magnitude must remain distinct typed channels.

The minimum P019 state is therefore

\[
\boxed{
\text{phase channel}
\times
\text{precision-magnitude channel}.
}
\]

## 3. P019-PM-T02 — The exact Schwarzschild horizon is the unique zero-phase vertex at every precision

Status: `PROVED`

By definition,

\[
\epsilon(n;h)=0
\iff
n=h,
\]

and

\[
q_\lambda(h;h)=0.
\]

Hence for every positive `lambda`,

\[
\boxed{
O_\lambda(n;h)=(0,0)
\iff
n=h.
}
\]

The **exact phase boundary does not thicken into multiple vertices merely because magnitude precision is finite.**

What thickens is instead

\[
\boxed{
\{n:\text{magnitude channel}=0\}=H_\lambda(h).
}
\]

That set can simultaneously contain

- inner phase `(-1,0)`;
- exact horizon `(0,0)`;
- outer phase `(+1,0)`.

## 4. P019-PM-C01 — Clock state `K=0` does not imply “at the horizon”

Status: `COUNTEREXAMPLE TO STRONG CLOCK-HORIZON IDENTIFICATION`

At square precision,

\[
K_\sigma(n;h)=R_2(q_{\sigma^2}(n;h)).
\]

Because `q` is a nonnegative integer,

\[
K_\sigma=0
\iff
q_{\sigma^2}=0.
\]

Take

\[
\sigma=2,\qquad h=10.
\]

Then

\[
K_2(9;10)=K_2(10;10)=K_2(11;10)=0,
\]

but their phases are respectively

\[
-1,\quad0,\quad+1.
\]

Therefore at coarse precision

\[
\boxed{
K=0\not\Rightarrow\text{horizon phase}=0.
}
\]

The first-stage singleton threshold

\[
\lambda\ge h+1
\]

must now be read as:

> **the finite completeness threshold at which the zero-magnitude/clock basin shrinks to the unique phase boundary, not an ontological threshold at which the event horizon changes from thick to thin.**

## 5. P019-PM-C02 — The same nonzero clock state also fails to determine causal direction

Status: `COUNTEREXAMPLE`

Take

\[
\sigma=2,\qquad h=3.
\]

Then

\[
K_2(2;3)=1,
\qquad
K_2(4;3)=1,
\]

while

\[
\epsilon(2;3)=-1,
\qquad
\epsilon(4;3)=+1.
\]

So even a nonzero clock magnitude satisfies

\[
\boxed{
K\text{ alone does not determine causal phase.}
}
\]

A time-rate value cannot be treated as the full spatial-direction state.

## 6. P019-PM-T03 — The charged model must also retain `sign(P)` and `g_lambda` as separate channels

Status: `PROVED`

The RN stage defined

\[
g_\lambda(n;a,b)
=
\left\lfloor\frac{\lambda|P(n)|}{n^2}\right\rfloor.
\]

The correct typed observation is

\[
\boxed{
O^{RN}_\lambda(n)
=
(\operatorname{sgn}P(n),g_\lambda(n)).
}
\]

Because the magnitude channel uses an absolute value, it cannot recover positive versus negative causal phase by itself.

For

\[
a=5,\quad b=5,\quad\lambda=5,
\]

states with `g_lambda=0` occur in both negative and positive phases.

Thus RN also has

\[
\boxed{
\text{zero magnitude}
\ne
\text{zero phase}.
}
\]

If `P(n)=0`, the pair is necessarily `(0,0)`. For a nonsquare discriminant, however, horizon boundary components may live entirely on crossing edges with no `(0,0)` primal vertex.

## 7. P019-PM-T04 — “Slower time causes spatial convergence” is not currently a derived causal theorem

Status: `NO-GO / UNDERDETERMINATION RESULT`

Fix any clock label `K=k`. Without an extra law coupling `K` to directed future incidences, finite causal graphs with the same current section size can realize

\[
\Xi>0,
\qquad
\Xi=0,
\qquad
\Xi<0.
\]

Take

\[
A=\{x_1,x_2\}
\]

and assign the same clock label `k` in all three models:

- if the two states reach 4 distinct future vertices, `Xi=+2`;
- if they reach 2 distinct future vertices, `Xi=0`;
- if both merge into one future vertex, `Xi=-1`.

The clock label is identical while every expansion sign is possible.

Under the current axioms,

\[
\boxed{
\text{clock slowdown}
\not\Longrightarrow
\text{causal-space contraction}
}
\]

not because the physical idea has been experimentally refuted, but because the mathematics still lacks a coupling law.

## 8. The more robust current interpretation: a common source, not yet a one-way cause

In the Schwarzschild stage:

- phase comes from `sign(n-h)`;
- magnitude comes from `q_lambda(n;h)`;
- clock state comes from `R_2(q)`.

They share the same underlying radial residual `n-h` but are different projections of it.

The RN stage makes the separation clearer:

- causal phase = `sign P(n)`;
- precision magnitude = quotient of `|P(n)|`;
- horizon boundary = zero vertices + sign-crossing edges.

The stronger current research starting point is therefore

\[
\boxed{
\text{one underlying causal residual}
\longrightarrow
\begin{cases}
\text{phase/direction},\\
\text{finite clock/rate magnitude},\\
\text{boundary structure}.
\end{cases}
}
\]

rather than prematurely asserting

\[
\text{time slows}\to\text{space contracts}.
\]

A directional causal claim can be restored only if a later non-arbitrary clock-to-incidence coupling is found.

## 9. What survives from the original intuition

The overstrong form being rejected is:

> “the clock value itself determines spatial convergence.”

The structurally stronger surviving possibility is:

> **time rate, causal direction, and spatial cross-section convergence may be different projections of one deeper discrete causal structure.**

The next task is to find a local, natural, falsifiable rule from phase/magnitude state to the Supplement 03 quantities

\[
B(A),C(A),\Xi(A).
\]

If no such rule exists, the common-cause interpretation should be retained and the strong one-way causal interpretation abandoned.

## 10. Formal terminology replacement for earlier P019 text

From this supplement onward:

- “zero horizon basin” should be replaced by **zero-magnitude basin**;
- “horizon becomes a unique shell at terminal precision” should be replaced by **zero-magnitude basin becomes phase-complete at terminal precision**;
- `q_lambda=0` alone is not a horizon definition;
- horizon/boundary uses Supplement 02's

\[
\partial_\xi G=(V_0,E_{\pm});
\]

- a magnitude observation must never silently replace its phase channel.

The earlier integer interval, width, projection, and clock-shell calculations remain valid; their subject is finite-resolution magnitude/rate structure rather than the ontology of the horizon itself.

## 11. Stage ledger

- `P019-PM-T01`: phase × magnitude typed state is required — `PROVED / DESIGN CORRECTION`
- `P019-PM-T02`: Schwarzschild exact zero-phase vertex is unique at every precision — `PROVED`
- `P019-PM-C01`: clock `K=0` can contain inner/horizon/outer phases — `COUNTEREXAMPLE`
- `P019-PM-C02`: the same nonzero clock state can occur in opposite causal phases — `COUNTEREXAMPLE`
- `P019-PM-T03`: charged observation also requires phase/magnitude separation — `PROVED`
- `P019-PM-T04`: clock label alone does not imply expansion sign without a coupling law — `UNDERDETERMINATION / NO-GO`

Executable checks:

- `src/enterprise_math/phase_magnitude.py`
- `tests/test_phase_magnitude.py`

## 12. Next step

The next stage should stop adding coordinate formulae and attack only

\[
\boxed{
(\text{phase},\text{clock magnitude})
\stackrel{?}{\longrightarrow}
\text{directed incidence constraints}
\longrightarrow
B,C,\Xi.
}
\]

Any candidate rule must be:

1. local;
2. integer-valued;
3. compatible with typed scale;
4. unable to confuse observer-coordinate effects with invariant law;
5. correct on Schwarzschild/RN specializations;
6. falsifiable by counterexample rather than reverse-engineered to reproduce a black-hole answer.
