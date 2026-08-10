# P022 — Crossing-Lattice Certificate for Half-Defect Marker Nonvanishing

Status: `ACTIVE RESEARCH NOTE / EXACT SUFFICIENT CERTIFICATE`  
Owner: `program/p022-geometry-v2`  
Depends on: sparse zero-boundary flux  
Boundary: this does not prove global nonvanishing; it extracts the strongest immediate divisibility obstruction from the crossing coefficients without using their exact p-adic depths.

## 1. Exact marker equation

For a forced-midpoint prime with composite boundary, put

\[
m=(p-1)/2,
\qquad
z_j=v_p(F_j).
\]

The sparse zero-boundary formula gives

\[
\kappa_p:=v_p(D_m)
=
z_m+
\sum_{\substack{j<m\\p\mid F_j}}
z_jc_j,
\]

where

\[
c_j=\Delta c_p(j)
\]

is the signed difference between the two prime-halving DAG crossing multiplicities at the zero boundary `j`.

Only indices with `c_j!=0` can affect the marker.

## 2. P022-LI39 — the correction lives in an integer lattice

Define

\[
\boxed{
g_p=\gcd\{|c_j|:j<m,\ p\mid F_j,\ c_j\ne0\}.}
\]

If there is no nonzero crossing coefficient, set `g_p=0`.

Every zero depth `z_j` is an integer. Therefore

\[
\boxed{
\kappa_p-z_m\in g_p\mathbb Z.
}
\]

Equivalently, for `g_p>0`,

\[
\boxed{
\kappa_p\equiv z_m\pmod{g_p}.
}
\]

This does not require knowing any earlier zero depth individually.

## 3. P022-LI40 — nonvanishing by lattice mismatch

Two immediate exact certificates follow.

### No correction direction

If

\[
g_p=0,
\]

then

\[
\boxed{\kappa_p=z_m>0.}
\]

### Lattice mismatch

If

\[
g_p>0
\quad\text{and}\quad
g_p\nmid z_m,
\]

then zero is not in the allowed congruence class, so

\[
\boxed{\kappa_p\ne0.}
\]

Parity is only the special case `g_p=2` with odd midpoint depth.

The converse is false: `g_p|z_m` means only that exact cancellation is arithmetically possible. The actual weighted crossing sum may still miss `-z_m`.

## 4. The explicit target-family support collision is protected by the lattice

For

\[
p=369581,
\]

the only nonzero zero-boundary coefficient is

\[
c_8=-2.
\]

Thus

\[
\boxed{g_p=2.}
\]

The midpoint has depth

\[
z_m=1.
\]

Therefore before computing the exact correction we already know

\[
\kappa_p\equiv1\pmod2,
\]

and hence

\[
\boxed{\kappa_p\ne0.}
\]

The separately computed exact value is `-1`.

This is the first reason the `-1` marker is structurally preferable to treating the support collision as a failure: the collision itself generates a nontrivial lattice obstruction against cancellation.

## 5. Sharp negative control

For

\[
p=157,
\]

which is forced-midpoint with composite `p-2` but lies outside the selected `p=5,23 (mod 24)` subfamily, the only crossing coefficient is

\[
c_{16}=-1.
\]

Hence

\[
\boxed{g_p=1.}
\]

There is no congruence protection at all. The midpoint depth is one, and the exact correction is `-1`, giving

\[
\kappa_p=0.
\]

Thus the lattice certificate distinguishes the protected `369581` mechanism from a genuine cancellation mechanism.

## 6. Current target-family conjecture after the negative boundary

Finite evidence now suggests a weaker structural direction than global support avoidance:

> in the selected `p=5,23 (mod 24)` family, the crossing lattice may often be trivial (`g_p=0`) or have modulus greater than one when a genuine zero crossing occurs.

This is **not proved**. In particular, no global statement `g_p!=1` is claimed.

The exact research goal remains

\[
\kappa_p\ne0.
\]

LI39--LI40 provide a new route to that goal: it is enough to control the crossing lattice modulo the midpoint depth, rather than determine every earlier p-adic valuation.

## 7. Precision interpretation

For the future query “can this prime serve as a nonzero valuation marker?”, the complete earlier-depth vector

\[
(z_j)_j
\]

is often unnecessary. The quotient state

\[
(z_m,g_p)
\]

already certifies nonvanishing whenever `g_p=0` or `z_m mod g_p !=0`.

This is a P022 arithmetic specialization of task-relative precision: the gcd lattice is not a replacement for the exact defect when the congruence test is inconclusive.

## 8. Executable assets

- `src/enterprise_math/p022_barlow_marker_crossing_lattice.py`
- `tests/test_p022_barlow_marker_crossing_lattice.py`
