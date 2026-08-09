# P022 Barlow Coordination Precision Supplement 02 — Coordinate-Sensitive Support Recovers Signed Drift

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE MOMENT RECONSTRUCTION / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: BC01–BC04 and Barlow prefix normal form  
Purpose: distinguish the precision of an actual shell-layer set from the precision of its cardinality

## 1. Correction to a tempting interpretation

BC02 proved a surprising statement:

\[
S_n(k)=3(2n-|k|)
\qquad(|k|<n),
\]

so the **number** of vertices on every non-extreme shell layer is independent of stacking.

This must not be misread as saying that the actual shell-layer geometry is stacking-independent.

Its coordinate-sensitive shape still retains the signed prefix imbalance. In fact one first integer moment recovers that imbalance exactly.

Thus

\[
\boxed{
\text{shell-layer set}
\text{ and }
|\text{shell-layer set}|
\text{ have different minimum precision}.}
\]

## 2. Symmetric triple-coordinate representation

Take positive imbalance `delta=d>=0`. The vertical support is

\[
V_{c,d}=H_c+\Delta_d^+
\]

and may be written

\[
V_{c,d}
=
\{(q,r):
-c\le q,r,q+r\le c+d
\}.
\]

Introduce

\[
x=q+c,
\qquad
y=r+c,
\qquad
z=c+d-q-r.
\]

Then

\[
x+y+z=3c+d,
\]

and the remaining inequalities become symmetric bounds on `x,y,z`.

Therefore the finite set of admissible triples is invariant under every permutation of the three coordinates. Hence

\[
\sum x=\sum y=\sum z
=\frac{3c+d}{3}|V_{c,d}|.
\]

Returning to axial coordinates gives

\[
\boxed{
\frac1{|V_{c,d}|}\sum_{(q,r)\in V_{c,d}}q
=
\frac1{|V_{c,d}|}\sum_{(q,r)\in V_{c,d}}r
=rac d3.}
\]

Negative imbalance is the reflected support, so the signed statement is

\[
\boxed{
\sum q=\sum r
=\frac{\delta}{3}|V_{c,|\delta|}|.}
\]

The divisibility by three is automatic from the lattice symmetry.

## 3. P022-BCS01 — vertical support reconstructs signed imbalance

Let

\[
K=|V_{c,|\delta|}|
\]

and let

\[
M_q=\sum_{(q,r)\in V}q.
\]

Then

\[
\boxed{
\delta=\frac{3M_q}{K}.}
\]

Thus the complete coordinate-sensitive **minimum-vertical existence set** on a selected target layer determines `delta` itself, including sign.

This strengthens the earlier Barlow BS05 result. There we recovered `delta` from the full distance+shortest-count language via coefficient moments. The count observable is not needed for this minimality statement:

> **the full coordinate-sensitive native distance/existence language on one selected layer already recovers the signed prefix imbalance.**

Indeed, the distance function identifies exactly the endpoints reachable at distance `|k|`; that set is `V`, and its first moment recovers `delta`.

So shortest-path multiplicity adds richer geometry, but it does not increase the minimum stacking state for the complete coordinate-sensitive one-layer distance language.

## 4. P022-BCS02 — every expanded support keeps the same centroid

For nonnegative integer `s`, consider

\[
H_s+\Delta_d^+.
\]

The same triple-coordinate symmetry applies with `c` replaced by `s`, and the axial centroid remains

\[
(d/3,d/3).
\]

Therefore all nested expansions used to construct graph shells share one centroid determined solely by signed drift.

If the imbalance is negative, every centroid is reflected to

\[
(\delta/3,\delta/3).
\]

## 5. P022-BCS03 — non-extreme shell layers retain signed drift in their first moment

A non-extreme shell layer is the set difference

\[
\bigl(H_{c+t}+\Delta_d\bigr)
\setminus
\bigl(H_{c+t-1}+\Delta_d\bigr),
\qquad t=n-|k|>0.
\]

Both nested sets have centroid `delta/3`. Therefore their difference does as well.

Let its cardinality be

\[
N=3(2n-|k|).
\]

Then either axial first moment is

\[
\boxed{
M_q=M_r
=rac{\delta N}{3}
=\delta(2n-|k|).}
\]

Hence

\[
\boxed{
\delta
=rac{M_q}{2n-|k|}.}
\]

So although **cardinality is completely stacking-independent** on every non-extreme layer, the coordinate-sensitive shell layer itself still contains the full signed imbalance in its first moment.

This is an unusually sharp loss-of-information example:

\[
\boxed{
\text{same layer cardinality}
\not\Rightarrow
\text{same layer support shape}.}
\]

## 6. Extreme layers

For `|k|=n`, the shell layer equals the vertical support itself. BCS01 gives

\[
\delta=3M_q/K.
\]

If only the cardinality `K` is retained, BC03 shows that the sign is lost and only

\[
|\delta|
\]

remains recoverable.

Therefore on an identified extreme layer there is a strict hierarchy:

\[
\boxed{
\text{coordinate-sensitive set}
\to \delta
\to |\delta|
\to K.}
\]

The first arrow is exact equivalence up to finite relabeling of the represented drift states; the second is a deliberate reflection quotient.

## 7. Precision table for one selected shell layer

For fixed shell radius `n` and selected layer `k`:

### Full coordinate-sensitive membership / distance function

Required stacking state:

\[
\boxed{\delta_k.}
\]

### Only first axial moment

Still sufficient and exactly equivalent to `delta_k` once `(n,k)` and the layer size are query context.

### Layer cardinality, non-extreme `|k|<n`

Required stacking state:

\[
\boxed{\text{none}.}
\]

The answer is always `3(2n-|k|)`.

### Layer cardinality, extreme `|k|=n`

Required stacking state:

\[
\boxed{|\delta_k|.}
\]

This is a concrete four-level example of how merely changing the observation—from set membership to first moment to cardinality—changes the exact quotient.

## 8. Relation to the multiplicity hierarchy

The new result clarifies what geodesic multiplicity is and is not doing.

It is **not** the first observable capable of seeing stacking phase. Coordinate-sensitive distance support already sees signed `delta`.

Multiplicity becomes essential when the future language asks finer questions such as:

- how many shortest witnesses reach the same endpoint;
- geodesic interval profiles;
- shell multiplicity spectra;
- count-enriched composition.

Those observables distinguish states that can share the same existence support/cardinality shadows.

So the geometry hierarchy should be written more carefully as

\[
\text{coordinate support shape}
\quad\text{vs}\quad
\text{support cardinality}
\quad\text{vs}\quad
\text{witness multiplicity},
\]

not as one total linear order. Different observables can be incomparable even when they come from the same primitive graph.

## 9. P023/P024 consequence

This is a direct worked example of the general future-language rule:

- preserving the whole coordinate-sensitive relation requires one signed integer;
- applying the `cardinality` observation can erase that integer completely on non-extreme layers;
- applying `cardinality` on an extreme layer erases only its sign;
- aggregating top and bottom into one whole-shell cardinality erases their allocation and retains only `delta_n^2+delta_-n^2`.

The successive quotients are not chosen by an abstract global precision order. They are induced by the declared observations.

The general theorem remains A2/P023/P024-owned; this note is a P022 geometry specialization.

## 10. Executable assets

`p022_barlow_coordination.py` now includes exact first-moment formulas and inverse recovery functions for both vertical supports and shell-layer sets.

The tests compare those moments against explicit polynomial-support and contact-shell enumeration over all short periodic stackings.
