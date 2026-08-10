# Legendre Pressure Test — Supplement 27

Status: `PROVED RESEARCH NOTE`  
Scope: next-`p`-square overshoot calculus for the split-shell statistic `S(k)`  
Depends on: P017 L067, P018 quotient-root threshold, exact p-rough cofactor windows  
Discipline: this is exact finite integer arithmetic. It does not estimate the asymptotic size of `S(k)` and does not prove Legendre's conjecture.

## 1. The new statistic S(k) still hides a boundary mechanism

L067 defines

\[
S(k)=\#\{p:\text{the realized least-prime shell }p\text{ meets two cofactor-root classes}\}.
\]

This is already an exact arithmetic observable, but the definition still sounds like a shell-by-shell image computation.

The present supplement exposes the single integer boundary responsible for every possible split.

## 2. The next p-weighted square above k²

Fix a prime

\[
p\le k.
\]

Set

\[
j_p
=R_2\!\left(\left\lfloor\frac{k^2}{p}\right\rfloor\right)
\]

and define

\[
\boxed{m_p=j_p+1.}
\]

Then `m_p` is the least positive integer satisfying

\[
\boxed{p m_p^2>k^2.}
\]

Define the positive overshoot

\[
\boxed{
\tau_p
=p m_p^2-k^2.
}
\]

This is exactly the P018 quotient-root threshold state, measured as an offset from the lower square boundary.

The boundary quotient

\[
q=m_p^2
\]

is where the stripped cofactor root changes from `j_p` to `j_p+1`.

## 3. P017-L068-A — Exact numbers of raw quotient slots on both sides

Status: `PROVED`.

The open exact cofactor window is

\[
W_p(k)
=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}p\right\rfloor
\right].
\]

Let `L_p` be the number of raw quotient states in this window strictly below `m_p^2`, and `U_p` the number at or above `m_p^2`.

Then

\[
\boxed{
L_p
=
\left\lceil\frac{\tau_p}{p}\right\rceil-1,
}
\]

and

\[
\boxed{
U_p
=
\max\!\left(
0,
\left\lfloor\frac{2k-\tau_p}{p}\right\rfloor+1
\right).
}
\]

### Proof of the lower formula

Write

\[
k^2=pq_0+r,
\qquad
q_0=\left\lfloor\frac{k^2}{p}\right\rfloor,
\qquad
0\le r<p.
\]

Since

\[
\tau_p
=p(m_p^2-q_0)-r,
\]

we have

\[
\left\lceil\frac{\tau_p}{p}\right\rceil
=m_p^2-q_0.
\]

The lower raw quotient states are

\[
q_0+1,\ldots,m_p^2-1,
\]

so their number is

\[
m_p^2-q_0-1
=
\left\lceil\frac{\tau_p}{p}\right\rceil-1.
\]

### Proof of the upper formula

The upper endpoint of the source basin is

\[
k^2+2k.
\]

Because

\[
pm_p^2=k^2+\tau_p,
\]

the number of `p`-spaced quotient states beginning at `m_p^2` and remaining below that source upper endpoint is

\[
\left\lfloor\frac{2k-\tau_p}{p}\right\rfloor+1
\]

when `tau_p<=2k`, and zero otherwise. ∎

## 4. P017-L068-B — Raw split iff p < tau_p <= 2k

Status: `PROVED`.

The exact cofactor window meets both adjacent root basins if and only if

\[
L_p>0
\quad\text{and}\quad
U_p>0.
\]

By L068-A,

\[
L_p>0
\iff
\left\lceil\frac{\tau_p}{p}\right\rceil\ge2
\iff
\tau_p>p,
\]

while

\[
U_p>0
\iff
\tau_p\le2k.
\]

Therefore

\[
\boxed{
W_p(k)\text{ crosses the root boundary}
\iff
p<\tau_p\le2k.
}
\]

This is a single-integer criterion.

## 5. Equivalent source-state picture

The root boundary state is

\[
n_*=p m_p^2=k^2+\tau_p.
\]

The immediately preceding `p`-multiple quotient state is

\[
n_*-p=p(m_p^2-1).
\]

The raw split criterion is exactly

\[
\boxed{
k^2<n_*-p<n_*\le k^2+2k.}
\]

Thus a raw factor shell can meet both root branches precisely when the open square basin contains the two consecutive `p`-multiple states straddling one cofactor-square boundary.

This makes the split a finite incidence event, not an abstract root ambiguity.

## 6. P017-L068-C — Realized split = raw boundary crossing + two-sided p-rough occupancy

Status: `PROVED`.

Define the lower and upper raw subwindows

\[
W_p^-
=
W_p(k)\cap(-\infty,m_p^2-1],
\]

and

\[
W_p^+
=
W_p(k)\cap[m_p^2,\infty).
\]

The actual least-prime shell consists exactly of the `p`-rough quotients inside `W_p(k)`.

Therefore the shell genuinely realizes both root values if and only if

\[
\boxed{
W_p^-\text{ contains a }p\text{-rough integer}
}
\]

and

\[
\boxed{
W_p^+\text{ contains a }p\text{-rough integer}.
}
\]

Equivalently,

\[
\boxed{
r_p=2
\iff
p<\tau_p\le2k
\text{ and both sides are }p\text{-rough occupied}.}
\]

The overshoot condition is necessary for the raw geometry; the roughness condition is exactly the realizability filter.

## 7. P017-L068-D — Exact sum formula for S(k)

Status: `PROVED`.

For each prime `p<=k`, define two Boolean occupancy bits

\[
\ell_p(k)
=
\mathbf1[W_p^-\text{ contains a }p\text{-rough integer}],
\]

\[
u_p(k)
=
\mathbf1[W_p^+\text{ contains a }p\text{-rough integer}].
\]

Then

\[
\boxed{
S(k)
=
\sum_{p\le k\atop p\text{ prime}}
\ell_p(k)u_p(k).
}
\]

Since either occupancy bit is automatically zero when the corresponding raw subwindow is empty, this formula may equivalently be written with the explicit overshoot gate

\[
\boxed{
S(k)
=
\sum_{p\le k\atop p\text{ prime}}
\mathbf1[p<\tau_p\le2k]\,
\ell_p(k)u_p(k).
}
\]

This is an exact finite arithmetic decomposition of the L067 second repair-spectrum coordinate.

## 8. Raw split spectrum

Define the envelope count

\[
\boxed{
S_{\rm win}(k)
=
\#\{p\le k:\ p\text{ prime},\ p<\tau_p\le2k\}.
}
\]

Then

\[
\boxed{S(k)\le S_{\rm win}(k).}
\]

The difference

\[
S_{\rm win}(k)-S(k)
\]

counts prime shells whose exact quotient window crosses the root boundary but whose least-prime realizability filter empties at least one side.

At `k=6,p=3`, this happens explicitly: the raw upper branch contains `q=16`, but `16` is not `3`-rough, so the actual `p=3` shell does not split.

This is the one-shell version of the broader candidate-envelope versus realized-state correction.

## 9. Examples

### k=18, p=7

The `p=7` shell is a genuine split shell from L064. L068 identifies the exact threshold offset `tau_7`, gives positive lower and upper raw slot counts, and both sides contain `7`-rough quotients (`47` below and `49` at/above the square boundary).

### k=6, p=3

The overshoot lies in the raw split range, so `L_p,U_p>0`. But the upper p-rough occupancy bit vanishes. This isolates the false raw split created by the envelope.

## 10. Research meaning

The new statistic `S(k)` is no longer an opaque image count. It decomposes into two layers:

\[
\boxed{
\text{next }p\text{-square boundary position}
}
\]

and

\[
\boxed{
\text{two-sided }p\text{-rough occupancy around that boundary}.
}
\]

The first layer is completely controlled by Euclidean quotient/root arithmetic. The second is the genuinely sieve-theoretic part.

This sharply isolates where further number-theoretic work is needed.

## 11. Executable specification

- `src/enterprise_math/p017_root_split_overshoot.py`
- `tests/test_p017_root_split_overshoot.py`

The executable layer checks the slot formulas against the exact cofactor windows, verifies the raw split criterion, and confirms that realized split primes agree with the independent L067 split-shell compiler.

## 12. Tool feedback

The loop is

\[
\boxed{
\text{P018 quotient-root threshold}
\to
\text{P017 next-}p\text{-square overshoot}
\to
\text{P011/P023 repair spectrum coordinate }S(k).
}
\]

This converts a generic future-threshold tool into a new exact sieve-facing arithmetic observable.
