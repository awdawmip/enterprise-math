# P018 — All-Power Quotient Transport, Supplement 01

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact whole-basin strict root-descent threshold  
Depends on: P018 all-power two-basin quotient transport  
Discipline: integer-only; this is an exact consequence of floor division and integer-root basin boundaries.

## 1. Setup

Fix

\[
p\ge1,\qquad k\ge1,\qquad d\ge2,
\]

and the source root basin

\[
B_{p,k}=\{n:k^p\le n<(k+1)^p\}.
\]

The previous all-power transport theorem proves that every `n in B_(p,k)` satisfies

\[
R_p(n//d)\in\{j,j+1\},
\qquad
j=R_p(k^p//d)<k.
\]

The remaining question is stronger: when is the **actual** quotient root strictly below `k` for every state in the source basin?

## 2. P018-APQ-T03 — Exact whole-basin strict-descent criterion

Status: `PROVED`.

The following are equivalent:

\[
\boxed{
R_p(n//d)<k
\quad\text{for every }n\in B_{p,k}
}
\]

and

\[
\boxed{(k+1)^p\le d k^p.}
\]

### Proof

The largest quotient state produced by the source basin is

\[
q_{\max}
=
\left\lfloor\frac{(k+1)^p-1}{d}\right\rfloor.
\]

Every quotient root is strictly below `k` exactly when

\[
q_{\max}<k^p.
\]

For positive integer `d`,

\[
\left\lfloor\frac{A}{d}\right\rfloor<B
\iff
A<dB.
\]

Substitute

\[
A=(k+1)^p-1,
\qquad B=k^p.
\]

Then

\[
q_{\max}<k^p
\iff
(k+1)^p-1<d k^p.
\]

Because both sides are integers, this is equivalent to

\[
(k+1)^p\le d k^p.
\]

∎

## 3. Relation to the square strict-descent theorem

For `p=2` and `d=2`, the criterion becomes

\[
(k+1)^2\le2k^2.
\]

This holds for every integer `k>=3`, recovering the current P018 square-root strict-descent result as a special case.

The all-power form shows exactly which part of that theorem is quadratic and which part is general: the finite-root descent mechanism is a perfect-power basin phenomenon, while the numerical threshold depends on `p` and `d`.

## 4. Consequence for quotient paths

If a finite quotient path has total divisor

\[
D=\prod_i d_i,
\]

then the final state is `Q_D(n)`. Therefore the entire path is guaranteed to end with `p`-root below `k` exactly when

\[
\boxed{(k+1)^p\le D k^p.}
\]

This is a statement about the final flattened quotient. It does not claim that every intermediate stage has already crossed the same root threshold.

## 5. Executable audit

`power_basin_quotient_window` now records the exact `strict_root_descent` bit, and `whole_basin_strict_root_descent` exposes the criterion directly.

`tests/test_p018_power_basin.py` checks the equivalence across bounded grids of exponents, basin indices and divisors. Finite tests audit the implementation; the proof above is exact.
