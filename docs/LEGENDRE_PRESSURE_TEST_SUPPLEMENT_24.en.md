# Legendre Pressure Test — Supplement 24

Status: `PROVED RESEARCH NOTE`  
Scope: exact two-task scheduling between least-prime and cofactor-root precision  
Depends on: P017 L064, P023-S12 directed repair geometry, P023-S14 conditional task scheduling  
Discipline: this theorem compares exact finite representation costs. It does not prescribe a universal factoring algorithm and does not prove Legendre's conjecture.

## 1. Why L064 does not determine the first task

L064 proves a strong conditional asymmetry:

\[
\rho(P,R)\le2,
\]

while the reverse factor `rho(R,P)` can be much larger.

It is tempting to conclude that least-prime precision should always be acquired before cofactor-root precision.

That conclusion is false.

The first task itself has a class-count cost. A task with expensive reverse repair can still be the cheaper first task if it has substantially fewer classes or if it already determines the other task.

## 2. Exact two-task cost formula

Let

\[
N_P=|X/P|,
\qquad
N_R=|X/R|,
\]

and let

\[
\rho_{P\to R}=\rho(P,R),
\qquad
\rho_{R\to P}=\rho(R,P).
\]

For integer base `B>=2`, define

\[
L_B(n)=\min\{\ell:n\le B^\ell\}.
\]

Then P023-S14 gives the exact sequential costs

\[
\boxed{
C_{P\to R}
=
L_B(N_P)+L_B(\rho_{P\to R}),
}
\]

and

\[
\boxed{
C_{R\to P}
=
L_B(N_R)+L_B(\rho_{R\to P}).
}
\]

The optimal order is exactly the smaller of these two integers.

This criterion is complete for the two-task problem.

## 3. L065-A — Root first is strictly optimal at k=11

Status: `PROVED BY EXACT FINITE CLASSIFICATION`.

In the square basin

\[
(11^2,12^2)=(121,144),
\]

the actual composite-shell state has

\[
\boxed{N_P=5},
\qquad
\boxed{N_R=6},
\qquad
\boxed{|X/(P\cap R)|=6}.
\]

The directed repair factors are

\[
\boxed{
\rho(P,R)=2,
\qquad
\rho(R,P)=1.
}
\]

The second equality says that, in this basin, the cofactor-root coordinate already determines the least-prime shell.

In base two,

\[
C_{P\to R}
=L_2(5)+L_2(2)
=3+1
=4,
\]

whereas

\[
C_{R\to P}
=L_2(6)+L_2(1)
=3+0
=3.
\]

The final joint quotient has six classes, so its absolute lower bound is

\[
L_2(6)=3.
\]

Hence

\[
\boxed{
C_{R\to P}=3<4=C_{P\to R},
}
\]

and root-first is not merely better; it is optimal with zero scheduling slack.

## 4. L065-B — Factor first is strictly optimal at k=1737

Status: `PROVED BY EXACT FINITE CLASSIFICATION`.

At

\[
k=1737,
\]

the actual composite-shell state has

\[
\boxed{N_P=157},
\qquad
\boxed{N_R=109},
\qquad
\boxed{|X/(P\cap R)|=164}.
\]

By L064,

\[
\boxed{
\rho(P,R)=2,
\qquad
\rho(R,P)=8.
}
\]

Thus

\[
C_{P\to R}
=L_2(157)+L_2(2)
=8+1
=9,
\]

while

\[
C_{R\to P}
=L_2(109)+L_2(8)
=7+3
=10.
\]

Therefore

\[
\boxed{
C_{P\to R}=9<10=C_{R\to P},
}
\]

so factor-first is strictly optimal at this basin.

The final joint lower bound is

\[
L_2(164)=8,
\]

so even the better two-stage schedule still has one bit of sequential worst-case slack.

## 5. L065-C — No fixed factor/root order is universally optimal

Status: `PROVED` by L065-A and L065-B.

The two strict witnesses point in opposite directions:

\[
\boxed{
k=11:\quad R\to P\text{ is strictly better},}
\]

while

\[
\boxed{
k=1737:\quad P\to R\text{ is strictly better}.}
\]

Hence neither of the global rules

\[
\text{“always factor first”}
\]

nor

\[
\text{“always root first”}
\]

can be correct for exact finite precision acquisition.

The optimal order is basin-dependent.

## 6. Why conditional asymmetry is not enough

L064 only compares the **second-step** costs

\[
\rho(P,R)
\quad\text{and}\quad
\rho(R,P).
\]

S14 shows that a complete schedule must also pay for the first task itself.

Therefore the correct comparison is

\[
\boxed{
L_B(N_P)+L_B(\rho(P,R))
\quad\text{versus}\quad
L_B(N_R)+L_B(\rho(R,P)).
}
\]

not merely `rho(P,R)` versus `rho(R,P)`.

This gives a strict number-theoretic example of the general principle

\[
\boxed{
\text{conditional repair geometry}
\neq
\text{complete acquisition schedule}.
}
\]

## 7. Structural reading of the k=11 witness

At `k=11`, the root-to-factor repair factor is one. Thus every realized root block lies inside one least-prime block:

\[
R\subseteq P.
\]

So retaining `R` already retains all `P` information. Acquiring `P` first pays for a five-class coordinate that is later refined by `R`; acquiring `R` first immediately reaches the final joint quotient.

This is the exact mechanism behind the one-bit scheduling advantage.

## 8. Structural reading of the k=1737 witness

At `k=1737`, root precision is much cheaper as a first coordinate in raw class count:

\[
109<157.
\]

But it hides an eight-way least-prime ambiguity in one root fiber. The extra three binary repair symbols outweigh the one-bit saving in first-task class depth.

Thus a coarser-looking first coordinate can become more expensive once its worst local reconstruction burden is included.

## 9. Consequence for number-theoretic proof design

For a proof that needs both least-prime shell identity and cofactor-root identity, there is no globally correct static ordering heuristic.

The exact finite rule is:

1. count the currently realized task classes;
2. compute the directed repair factor to the other coordinate;
3. compare the two integer schedule costs;
4. for more than two tasks, use S14 conditional scheduling rather than extrapolating the two-task preference.

This is a proof-state optimization rule, not a claim about physical time or computational complexity of factoring integers in general.

## 10. Executable specification

- `src/enterprise_math/p017_root_factor_schedule.py`
- `tests/test_p017_root_factor_schedule.py`

Regression pins the exact `k=11` and `k=1737` class counts, directed repair factors, schedule depths, and opposite optimal directions. A bounded sweep also verifies that the returned preference is exactly the integer cost comparison and that both schedules respect the final joint-class lower bound.

## 11. Tool feedback

The full loop is now

\[
\boxed{
\text{P018 two-basin transport}
\to
\text{P023 directed precision geometry}
\to
\text{P017 L064 asymmetry}
\to
\text{P023 conditional scheduling}
\to
\text{P017 L065 order reversal}.
}
\]

This is a stronger form of theorem feedback than merely rephrasing an old result: the abstract tool exposes a new basin-dependent ordering theorem and simultaneously falsifies two natural global heuristics.
