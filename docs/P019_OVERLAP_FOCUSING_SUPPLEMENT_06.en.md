# P019 — Overlap-Spectrum Focusing, Supplement 06: Higher-Order Future Overlap and Expansion Submodularity

Status: `ACTIVE RESEARCH NOTE`  
Depends on: P011 collision spectrum, P019 Directed Expansion Supplement 03, P019 Integer Focusing Supplement 05  
Scope: resolve the future collision/focusing excess `C` exactly into two-way, three-way, four-way, ... successor overlaps and derive marginal-expansion/submodular structure  
Discipline: these are exact finite-set and finite-graph results. No overlap order may be renamed Ricci curvature, shear, or matter-energy without an additional derivation.

## 1. Why resolve `C` further

The previous stage proved

\[
\Xi(A)=B(A)-C(A),
\]

with

\[
C(A)=\sum_{w\in F(A)}(m_A(w)-1).
\]

This total already captures future-state focusing, but it compresses pairwise merging and three-way, four-way, or deeper focusing into one integer.

P011 already gives the full collision spectrum of a finite map,

\[
J_k=\sum_w\binom{m(w)}k.
\]

The natural P019 question is therefore not to invent a new curvature scalar, but to ask: **what exactly is `C` inside the existing `J_k` spectrum?**

The answer is an exact alternating projection.

## 2. Definition: k-way successor overlap

For a current section

\[
A\subseteq V
\]

and the successor set of each source vertex

\[
S(v)=\{w:(v,w)\in E^+\},
\]

define the order-`k` successor overlap by

\[
\boxed{
O_k(A)
=
\sum_{\substack{T\subseteq A\\|T|=k}}
\left|\bigcap_{v\in T}S(v)\right|.
}
\]

It counts how many future targets are jointly shared by each `k`-source subset and then sums over all such subsets.

## 3. P019-OF-T01 — k-way overlap equals the local P011 collision spectrum

Status: `PROVED`

For each future target `w`, let

\[
m_A(w)=|\{v\in A:w\in S(v)\}|.
\]

Swap the order of summation. A fixed future target `w` is contained in exactly

\[
\binom{m_A(w)}k
\]

source subsets of size `k`.

Hence

\[
\boxed{
O_k(A)
=
\sum_{w\in F(A)}\binom{m_A(w)}k
=J_k^{\rm out}(A).
}
\]

The successor-overlap spectrum is therefore not a competing invariant. It is exactly the P011 collision spectrum of the causal incidence target map, expressed in set-intersection language.

The interface is now two-sided:

- P011 `J_k`: k-fold collisions viewed through fiber multiplicity;
- P019 `O_k`: k-way focusing viewed through common future reachability.

They are the same integer.

## 4. P019-OF-T02 — Focusing excess is an alternating projection of the full overlap spectrum

Status: `PROVED`

For every integer `m>=1`, the binomial identity

\[
(1-1)^m=0
\]

gives

\[
1-m+\binom m2-\binom m3+\cdots+(-1)^m=0.
\]

Therefore

\[
\boxed{
m-1
=
\binom m2-inom m3+inom m4-\cdots.}
\]

Summing over every future-target multiplicity gives

\[
\boxed{
C(A)
=J_2^{\rm out}(A)-J_3^{\rm out}(A)+J_4^{\rm out}(A)-\cdots.
}
\]

Equivalently,

\[
\boxed{
C(A)=O_2(A)-O_3(A)+O_4(A)-\cdots.}
\]

The central expansion identity therefore becomes

\[
\boxed{
\Xi(A)
=
B(A)-J_2+J_3-J_4+J_5-\cdots.
}
\]

Pair collision `J_2` alone systematically overcounts targets with multiplicity three or more; higher orders correct that overcount by inclusion-exclusion.

For example, if three sources all reach the same single future target,

\[
(J_1,J_2,J_3)=(3,3,1).
\]

The actual focusing loss is

\[
C=3-1=2,
\]

not `J_2=3`; the three-way term gives the exact correction:

\[
C=J_2-J_3=2.
\]

## 5. P019-OF-T03 — Pair collision bounds `C` and is controlled by maximum multiplicity

Status: `PROVED`

Let

\[
\mu(A)=\max_{w\in F(A)}m_A(w).
\]

For each `m>=1`,

\[
m-1\le\binom m2.
\]

Therefore

\[
\boxed{C(A)\le J_2^{\rm out}(A).}
\]

When `C(A)>0`,

\[
2\binom m2=m(m-1)\le\mu(A)(m-1),
\]

so summation gives

\[
\boxed{
2J_2^{\rm out}(A)
\le
\mu(A)C(A).
}
\]

One may externally abbreviate this as

\[
2J_2/\mu\le C\le J_2,
\]

but the integer core uses the cross-multiplied form and does not make the fraction primitive.

Thus pair-collision load has a controlled relation to actual focusing loss whenever the deepest target multiplicity is bounded.

## 6. P019-OF-T04 — Adding one source has an exact local marginal-expansion formula

Status: `PROVED`

Take

\[
v\notin A
\]

and define

\[
\Delta_v\Xi(A)
=
\Xi(A\cup\{v\})-\Xi(A).
\]

The new source has successor set `S(v)`. The genuinely new future states are exactly

\[
S(v)\setminus F(A),
\]

so

\[
|F(A\cup\{v\})|-|F(A)|
=|S(v)|-|S(v)\cap F(A)|.
\]

The current-section cardinality rises by one. Hence

\[
\boxed{
\Delta_v\Xi(A)
=
(|S(v)|-1)
-|S(v)\cap F(A)|.
}
\]

The right-hand side is precisely

\[
\boxed{
\text{new-source branch increment}
-
\text{existing-future overlap load}.
}
\]

This is a genuinely local focusing-source formula: evaluating the net expansion contribution of a new source requires only its successor set and its overlap with the already covered future set, not a hidden continuum scan.

## 7. P019-OF-T05 — Expansion has diminishing returns

Status: `PROVED`

If

\[
A\subseteq B,
\qquad
v\notin B,
\]

then

\[
F(A)\subseteq F(B).
\]

Therefore

\[
|S(v)\cap F(A)|
\le
|S(v)\cap F(B)|.
\]

Using T04,

\[
\boxed{
\Delta_v\Xi(A)
\ge
\Delta_v\Xi(B).
}
\]

Thus:

> **the same new source contributes no more net future expansion when added to a larger existing section.**

The mechanism is purely combinatorial: a larger existing section has already covered more future targets, making overlap with the new source more likely.

## 8. P019-OF-T06 — Future-section expansion is a submodular set function

Status: `PROVED`

Extend naturally to the empty set by

\[
F(\varnothing)=\varnothing,
\qquad
\Xi(\varnothing)=0.
\]

`|F(A)|` is a coverage function generated by unions of successor sets and is therefore submodular; `|A|` is modular. Hence

\[
\Xi(A)=|F(A)|-|A|
\]

is submodular:

\[
\boxed{
\Xi(A)+\Xi(B)
\ge
\Xi(A\cup B)+\Xi(A\cap B).
}
\]

The diminishing-returns form in T05 and the submodular inequality are equivalent finite-set views of the same structure.

This is important because it shows that the focusing/diminishing-return effect is not special to a hand-built radial black-hole example. **Every future-section expansion built from successor-set coverage carries this submodular structure.**

## 9. Meaning for local focusing-source decomposition

At this stage focusing can be written as

\[
\boxed{
C
=
O_2-O_3+O_4-\cdots
}
\]

and the marginal effect of one source as

\[
\boxed{
\Delta_v\Xi
=
\text{branch increment}
-
\text{future overlap load}.
}
\]

This is a stronger local source decomposition than the scalar `C` alone.

It still does **not** justify statements such as:

- `O_2` is Ricci focusing;
- `O_3` is shear;
- a fixed overlap order is matter-energy.

Continuum Raychaudhuri source terms have definite tensor/geodesic meanings. P019 `O_k` currently records only k-way future-overlap multiplicity.

The correct next question is whether microscopic causal graphs with the same `N,B,C` but different `O_k` spectra exhibit distinguishable transverse or directional deformation patterns.

If so, the full overlap spectrum becomes a candidate input for distinguishing shear-like from isotropic-focusing-like behavior.

## 10. A new testable distinction: equal total focusing can hide different higher-order spectra

Two local structures can have the same

\[
C=2
\]

in different ways:

- two independent pair collisions: `J_2=2,J_3=0`;
- one triple-target collision: `J_2=3,J_3=1`.

The total focusing loss `C` is identical while the higher-order spectrum differs.

Therefore

\[
\boxed{
C\text{ alone is not a complete local focusing invariant.}
}
\]

P011 already proves that the full collision spectrum reconstructs the fiber-size multiset. P019 now interprets this as reconstruction of the multiplicity profile describing how many source paths jointly hit each future target.

This gives the next stage a richer integer dataset for distinguishing concentrated high-multiplicity focusing from diffuse pairwise focusing.

## 11. Relation to established mathematics

The submodularity/coverage-function structure in T06 is established combinatorial-optimization mathematics and must not be claimed as an Enterprise Math invention.

What remains open for the project is the specific combination of:

- successor-coverage submodularity;
- the P011 collision spectrum;
- finite-precision fibers;
- causal-boundary and future-section dynamics;

and whether that integrated integer chain can support a falsifiable model of black-hole/focusing physics.

Novelty discipline therefore remains narrow: the mathematical tools retain their prior-art attribution, while the project investigates the particular integration and interpretation.

## 12. Stage ledger

- `P019-OF-T01`: k-way successor overlap equals the local P011 collision spectrum — `PROVED`
- `P019-OF-T02`: `C=J2-J3+J4-...` and `Xi=B-J2+J3-...` — `PROVED`
- `P019-OF-T03`: pair-collision bounds from maximum target multiplicity — `PROVED`
- `P019-OF-T04`: exact marginal-expansion formula for adding one source — `PROVED`
- `P019-OF-T05`: diminishing returns under section inclusion — `PROVED`
- `P019-OF-T06`: future-section expansion is submodular — `PROVED`

Executable checks:

- `src/enterprise_math/overlap_focusing.py`
- `tests/test_overlap_focusing.py`

## 13. Next-stage gate

The local focusing source has now been expanded from one total `C` into the full overlap spectrum.

The most valuable next problem is to construct minimal graph pairs with the **same `N,B,C` but different `O_k` spectra**, then identify finer integer observables that distinguish:

1. focusing concentrated in a few high-multiplicity future targets;
2. focusing dispersed over many pairwise overlaps;
3. directional or local-subsection asymmetry of the overlap spectrum;
4. which of these structures survive graph automorphisms and P018 refinement.

Only after this stage should shear-like versus curvature-like source decomposition be discussed.
