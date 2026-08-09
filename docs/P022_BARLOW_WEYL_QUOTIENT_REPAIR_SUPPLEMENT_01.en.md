# P022 — Stabilizer-Index Formula for `B_2/C_2` Quotient-Path Repair

Status: `ACTIVE RESEARCH NOTE / EXACT GROUP-ACTION SPECIALIZATION / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Parent: `P022_BARLOW_WEYL_QUOTIENT_REPAIR.en.md`

## 1. Local lift count

Let the signed-permutation group `W=B_2` act on labelled drift states.  For a legal canonical chamber transition

\[
p\to q,
\qquad 0\le p_1\le p_2,
\quad 0\le q_1\le q_2,
\]

write

\[
W_p=\operatorname{Stab}_W(p)
\]

and

\[
W_{p,q}=\operatorname{Stab}_W(p)\cap\operatorname{Stab}_W(q),
\]

the stabilizer of the canonical directed edge.

For the Barlow signed-step graph, `W_p` acts transitively on the labelled next lifts belonging to this coarse transition.  Therefore the number of labelled next states compatible with one fixed labelled lift of `p` is the orbit-stabilizer index

\[
\boxed{
\lambda(p,q)
=
\frac{|W_p|}{|W_{p,q}|}.
}
\]

The only values are `1`, `2`, and `4`.

---

## 2. P022-WS01 — stabilizer index equals the event rule

The chamber transition types give:

| source/transition | `|W_p|` | `|W_{p,q}|` | index | repair event |
|---|---:|---:|---:|---|
| interior | 1 | 1 | 1 | none |
| coordinate wall leaves zero | 2 | 1 | 2 | one orientation bit |
| diagonal splits | 2 | 1 | 2 | one side-label bit |
| diagonal remains diagonal | 2 | 2 | 1 | none |
| origin to `(1,1)` | 8 | 2 | 4 | two orientation bits |

Hence for every legal Barlow chamber edge,

\[
\boxed{
\frac{|W_p|}{|W_{p,q}|}
=2^{e(p)+b(p,q)},
}
\]

where `e(p)` is the number of zero coordinates of the source and `b(p,q)` is the diagonal-split indicator.

---

## 3. P022-WS02 — path lift multiplicity is a product of stabilizer indices

For a chamber history

\[
h=(q_1,\ldots,q_N),
\qquad q_0=(0,0),
\]

the local lift choices multiply, so

\[
\boxed{
|\operatorname{Lift}(h)|
=
\prod_{t=1}^{N}
\frac{|W_{q_{t-1}}|}{|W_{q_{t-1},q_t}|}.
}
\]

Using WS01,

\[
\begin{aligned}
|\operatorname{Lift}(h)|
&=
\prod_t2^{e(q_{t-1})+b(q_{t-1},q_t)}\\
&=
2^{E(h)+B(h)}.
\end{aligned}
\]

Thus the original event theorem and the group-action theorem are exactly the same finite quantity in two coordinate systems:

\[
\boxed{
\text{event count}
\longleftrightarrow
\text{stabilizer-index product}.
}
\]

---

## 4. Why the edge stabilizer matters

The vertex stabilizer alone is not enough.

At a diagonal state `(a,a)`, `|W_p|=2` whether the next coarse state

- remains diagonal, or
- splits into unequal coordinates.

If the edge remains diagonal, the coordinate-exchange reflection fixes **both** endpoints, so

\[
|W_{p,q}|=2
\]

and the index is one.

If it splits, the same reflection no longer fixes the directed edge, so

\[
|W_{p,q}|=1
\]

and the index is two.

Therefore repair is controlled by a **transition stabilizer loss**, not merely by the instantaneous amount of symmetry in the current coarse state.

This is important for any future abstraction: state-only symmetry counts can overpredict repair if the symmetry remains invisible to the next transition.

---

## 5. Upstream candidate lemma

The calculation suggests the following general route, but P022 does not claim it as a new general theorem.

Let a finite group `G` act by automorphisms on a labelled directed graph.  If the coarse future language retains a directed **edge-orbit path**, then for a chosen lift of one edge orbit the local number of compatible next lifts is governed by the action of the source vertex stabilizer on that edge orbit.  When that action is transitive, orbit-stabilizer gives

\[
\frac{|\operatorname{Stab}(v)|}
{|\operatorname{Stab}(v,e)|}.
\]

Products of such local indices are natural candidates for exact path-lift repair multiplicities.

If only vertex orbits are retained, several edge orbits can collapse together and extra state may be required.  This is precisely the kind of future-language distinction that A2/P023 must test before a general promotion.

---

## 6. Executable assets

Added:

- `src/enterprise_math/p022_barlow_stabilizer_lifting.py`;
- `tests/test_p022_barlow_stabilizer_lifting.py`.

The tests enumerate all small chamber transition types, compare the stabilizer index with the existing event branch factor, and verify the path product against the exact `2^(E+B)` microscopic fiber theorem.
