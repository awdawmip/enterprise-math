# P023 — Borrow Composition, Supplement 05

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact additivity and telescoping of coarse precision borrow along reductive trajectories

## 1. Definition

For a reductive operation `T(n)<=n` and positive precision ratio `r`, define

\[
\boxed{
B_r^T(n)=Q_r(n)-Q_r(T(n)).
}
\]

By P023-T17 this is equivalently computable from the reductive gap and the current within-fiber detail.

## 2. P023-T19 — Two-step borrow composition

Let `T` and `S` be reductive on the visited states:

\[
T(n)\le n,
\qquad
S(T(n))\le T(n).
\]

Then

\[
\boxed{
B_r^{S\circ T}(n)
=
B_r^T(n)+B_r^S(T(n)).
}
\]

### Proof

This is the exact telescoping identity

\[
Q_r(n)-Q_r(S(T(n)))
=
\bigl(Q_r(n)-Q_r(T(n))\bigr)
+
\bigl(Q_r(T(n))-Q_r(S(T(n)))\bigr).
\]

No approximation or asymptotic argument occurs.

## 3. P023-T20 — Finite trajectory telescoping

For a finite reductive trajectory

\[
n_0\ge n_1\ge\cdots\ge n_m,
\]

define the local borrow

\[
b_i=Q_r(n_{i-1})-Q_r(n_i).
\]

Then

\[
\boxed{
\sum_{i=1}^{m} b_i
=
Q_r(n_0)-Q_r(n_m).
}
\]

Thus total coarse precision loss depends only on the endpoints, while the local borrow profile records how that loss is distributed along the route.

## 4. Relation to P019 collapse-word stabilization

P019 proves that a fixed finite word of perfect-power collapses stabilizes at a greatest fixed point, and for a collapse word with exponent lcm `L` the eventual state is `C_L(n0)`.

Therefore every reductive transient route from `n0` to the same stable endpoint has the same total `r`-borrow:

\[
\boxed{
B_{\mathrm{total}}
=
Q_r(n_0)-Q_r(C_L(n_0)).
}
\]

But the local distribution can depend on word order and transient states.

### Minimal example

Take `n0=8`, `r=2`.

One collapse-word route is

\[
8\xrightarrow{C_2}4\xrightarrow{C_3}1,
\]

which, when treated as the composed word `C_3 C_2`, gives the one-word transition

\[
8\to1
\]

with borrow profile

\[
(4).
\]

The opposite order, repeated as a fixed word, gives

\[
8\to4\to1
\]

with borrow profile

\[
(2,2).
\]

Both routes have total borrow `4` because both endpoints project from `Q_2(8)=4` to `Q_2(1)=0`.

This separates two observables:

- **total borrow** — endpoint invariant;
- **borrow profile** — transient/path information.

## 5. Connection to P010/P011

P010/P011 emphasize that equal final states need not preserve intermediate history. P023-T20 gives a precision analogue:

\[
\text{same endpoint}
\Longrightarrow
\text{same total coarse borrow},
\]

but not the same local borrow sequence.

Thus total borrow is a coarse additive invariant, while the borrow profile is a finer historical witness that may be lost by stable-equivalence quotienting.

This is exactly the kind of distinction P023 is intended to police: a quotient may preserve the invariant one cares about while destroying route-level reconstructive information.

## 6. Executable audit

- `src/enterprise_math/p023_borrow_cocycle.py`
- `tests/test_p023_borrow_cocycle.py`

The reference tests exhaust all finite two-step chains `n>=mid>=end` below 80 across positive precision ratios below 10, check finite trajectory telescoping, and retain the explicit `8->1` versus `8->4->1` collapse-word witness.
