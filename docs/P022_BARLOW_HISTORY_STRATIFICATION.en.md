# P022 — Terminal Shell Stratification Re-Encodes Coordination History

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE EQUIVALENCE / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: coordination-history reconstruction; layer path-total and extreme-layer cardinality formulas

## 1. History need not be stored as time history

The complete coordination history

\[
\mathcal H_S(n)=(S_0,S_1,\ldots,S_n)
\]

recovers the unordered absolute drift pair at every height

\[
P_q=\{|\delta_q|,|\delta_{-q}|\}.
\]

A different question is whether the same information can be encoded **inside one terminal radius-`n` shell**, if the shell remains stratified by height.

The answer is yes.

## 2. Non-extreme layer path total is injective in absolute drift

Fix terminal radius `n` and height

\[
0<q<n.
\]

For legal absolute drift

\[
d\in\{q\bmod2,q\bmod2+2,\ldots,q\},
\]

the exact layer shortest-path total is

\[
\boxed{
L_{n,q}(d)
=
\binom nq
\left[
3\,2^{n-q+(q-d)/2}(1+2^d)-6
\right].
}
\]

Its finite drift increment is strictly positive, so `L_(n,q)` is injective in `d`.

Therefore the unordered pair of path totals on the `+q` and `−q` layers recovers

\[
\boxed{
\{|\delta_q|,|\delta_{-q}|\}.
}
\]

## 3. P022-HS01 — closed 2-adic inversion on non-extreme layers

The inverse need not enumerate candidate drifts.

Set

\[
Y
=
\frac{L_{n,q}(d)/\binom nq+6}{3\cdot2^{n-q}}.
\]

Then

\[
\boxed{
Y=2^{(q-d)/2}+2^{(q+d)/2}.
}
\]

If `d=0`, the two powers coincide and `Y` is one power of two.

If `d>0`, let

\[
a=v_2(Y).
\]

Then `a=(q-d)/2` and

\[
\boxed{
\frac{Y}{2^a}-1=2^d.
}
\]

So `d` is read directly from the binary exponent.  The inversion is integer-only.

## 4. Extreme layer boundary

At

\[
q=n,
\]

all shortest paths are purely vertical and the total path count is

\[
\boxed{3^n}
\]

for every drift.  Path total therefore loses all drift information at the extreme layer.

But the extreme layer vertex count is

\[
\boxed{
A_{n,n}(d)
=
\frac{3n^2+6n+4-d^2}{4},
}
\]

which is strictly decreasing in nonnegative `d`.

Hence

\[
\boxed{
d^2=3n^2+6n+4-4A_{n,n},}
\]

and one exact integer square root recovers `d`.

## 5. P022-HS02 — terminal stratified profile

Define the terminal profile at radius `n` as follows:

- at height `q=0`, keep the fixed central layer path total;
- for every `1<=q<n`, keep the **unordered pair** of shortest-path totals on layers `+q` and `−q`;
- at `q=n`, keep the **unordered pair** of extreme-layer vertex counts instead of path totals.

Call this profile

\[
\boxed{\mathcal P_n.}
\]

By HS01 and the extreme inversion,

\[
\mathcal P_n
\Longrightarrow
(P_0,P_1,\ldots,P_n).
\]

The coordination formula then reconstructs every

\[
S_q.
\]

Conversely, coordination history reconstructs every `P_q` and therefore constructs `\mathcal P_n`.

Thus

\[
\boxed{
\mathcal P_n
\Longleftrightarrow
\mathcal H_S(n).
}
\]

The equivalence is up to the same positive/negative side exchange already invisible to whole-shell coordination.

## 6. History–stratification duality

This gives a finite and literal sense in which past information can be re-encoded spatially:

\[
\boxed{
\text{radius history}
\Longleftrightarrow
\text{terminal height stratification}.
}
\]

No continuous embedding or external time coordinate is used.  The equivalence follows from exact integer drift observables carried at different heights of the terminal shell.

The result does **not** say that arbitrary histories are spatially encoded by arbitrary geometries.  It is a Barlow-specific theorem whose proof uses the exact layer formulas.

## 7. Information-loss boundaries

The height labels are essential.

If all layer path totals are aggregated into the single global total `T_n`, distinct stratifications can collide.  FCC/HCP already give examples where coarse total information fails to recover the richer layer geometry.

Likewise, the terminal profile recovers only absolute drift pairs.  It does not recover signed orientation or labelled side assignment.  Those require the event-driven repair of the two-sided repair theorem.

So the information chain is

\[
\boxed{
\text{labelled signed stacking window}
\to
\mathcal P_n\simeq\mathcal H_S(n)
\to
\text{global shell aggregates}.
}
\]

Each arrow has an explicit repair boundary.

## 8. Executable assets

- `src/enterprise_math/p022_barlow_history_stratification.py`;
- `tests/test_p022_barlow_history_stratification.py`.

The inverse uses only integer arithmetic, `v_2`, bit length and `isqrt`.  Tests round-trip every reachable short unordered drift history through terminal profiles and verify the exceptional role of the extreme layer.
