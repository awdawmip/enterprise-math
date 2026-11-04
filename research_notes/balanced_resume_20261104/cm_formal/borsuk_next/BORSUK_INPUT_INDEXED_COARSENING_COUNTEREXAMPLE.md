# Borsuk R6: a complete aggregate incompatibility graph does not determine adaptive coarsening

Author: `EM-C34-D16900`, execution `/root/research_cm_formal_1104`  
Date: 2026-11-04  
Status: `AUTHOR_PROVED_AWAITING_DISTINCT_NONCONTRIBUTING_REVIEW`  
Classification: exact source-specific counterexample to a lossy composition interface; standard geometry and graph coloring applied, not a new general tool family.

This is local, nonshared support for `OBJ-EXTERNAL-GEOMETRY-BORSUK-R6-UPPER-BOUND-PRESSURE-20260902`. It addresses the input/provenance and quantifier boundary in the published GEO9 continuous-certificate audit question. It is **not** execution or completion of that blocked audit or the blocked GEO9 construction Task. No claim, Result, Review, Driver authority, or shared state is created. The local research identity remains `REGISTER_PENDING`.

## 1. The concrete unresolved interface

GEO8 proves that the fixed Lassak lens has 33 individually admissible atoms and that every pair of whole lens atoms is incompatible with a strict-diameter merge. The resulting aggregate graph is `K_33`. That conclusion applies to coarsening the fixed lens atoms, or to one atom-label coloring that must work simultaneously for every input under consideration.

A different possible interface allows the coloring to depend on the actual unit-diameter input `K⊂L`, after restricting each atom to `K`. Its question has the quantifiers `for every K, there exists a coloring`, rather than `there exists one coloring, for every K`. This note supplies a fully Euclidean, source-matched counterexample to replacing the former by the latter after erasing the input label.

**Result.** For every legal cap parameter and every fixed horizontal orthonormal frame, construct two finite families of unit-diameter subsets of the same R6 Lassak lens. Their aggregate atom incompatibility graph is the same `K_33`, and every fixed atom-label coloring valid for the whole family needs 33 colors. Yet the worst input-specific coarsening number is exactly **2** for one family and exactly **7** for the other.

This does not improve a universal bound for `b(6)`, refute GEO8's fixed-template theorem, or establish that an adaptive whole-atom scheme works for every unit-diameter input. It identifies precisely which input information the old obstruction cannot discard when reused in that different query language.

## 2. Frozen geometric carrier and reused evidence

Use the actual GEO8 constants

\[
r^2=3/7,\qquad \ell=1/(2r)-r>0,\qquad
\ell^2=1/84,\qquad 2r\ell=1/7,\qquad \rho^2=5/12.
\]

Write `c=r e_6` and

\[
L=B_r(0)\cap B_1(c)\subset\mathbb R^6.
\]

Fix any `0<δ<r`, put `h=√(r²−δ²/4)>0`, and retain the exact old atoms: a cap `A_0={x∈L:x_6>h}`, and 32 sectors `A_σ` for `σ∈{−1,+1}^5` with `x_6≤h` and horizontal signs `σ`. Use any deterministic assignment of their boundary points. All points constructed below have strict horizontal signs or are the strictly capped point `c`, so boundary choices are immaterial.

The old GEO8 proof supplies these geometric inputs, which are consumed rather than recounted as new findings:

- for every horizontal unit vector `u`, `a(u)=ρu−ℓe_6` lies on both boundary spheres, with `|a(u)|=r` and `|a(u)−c|=1`;
- for every sector sign `σ`, `u_σ=σ/√5` gives a strict-sector point `a(u_σ)`;
- for distinct `σ,τ`, choose a differing coordinate `j` and put `u_j=3σ_j/√13`, `u_i=σ_i/√13` for `i≠j`; define `v` similarly from `τ`. Then `u,v` are unit vectors in the corresponding strict orthants, `u·v≤−5/13`, and

\[
|a(u)-a(v)|^2=2\rho^2(1-u\cdot v)\ge15/13>1. \tag{2.1}
\]

These facts belong to `research_returns/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE_RETURN_20260902.md`, exact Git blob `92a2ed004a794cd48425fdaff515a162329f3df7`, read in full at snapshot `39556bf5207aa5ba559a27ec591c1bc1bf43b457`. A fresh read from remote `main` on 2026-11-04 returned the same blob. The GEO9 construction/audit Taskbooks and line dossier were also freshly read and matched the frozen snapshot; exact bindings are in `LATEST_SOURCE_READBACK.json`.

The old GEO7 finite maximum-distance-graph equivalence is prior input, not a new theorem here. We do not use its unrestricted finite-metric realization to assert a Euclidean R6 realization. Every witness below has explicit Euclidean coordinates in this very lens.

## 3. An input-indexed family with exact adaptive cost two

Index one input by each unordered pair of distinct atom labels. There are `C(33,2)=528` such indices. The resulting family is denoted `F_2`.

For the pair `(0,σ)`, take the two-point input

\[
K_{0\sigma}=\{c,a(u_\sigma)\}. \tag{3.1}
\]

Its diameter is exactly one, with its two points in the indicated cap and sector.

For a sector pair `(σ,τ)`, choose the first differing coordinate in a fixed ordering to make the construction deterministic. Use `u,v` from (2.1), and write

\[
d_{\sigma\tau}=|a(u)-a(v)|>1,
\qquad t_{\sigma\tau}=1/d_{\sigma\tau}\in(0,1).
\]

Take the three-point input

\[
K_{\sigma\tau}=\{c,t_{\sigma\tau}a(u),t_{\sigma\tau}a(v)\}. \tag{3.2}
\]

The two scaled sector points have distance exactly one. They stay in their strict sectors: scaling by a positive number preserves their horizontal signs, their height is `−tℓ<h`, and their norm is `tr<r`. They also stay in the unit ball about `c`. More precisely, for either unscaled point `a` we have

\[
|ta-c|^2=t^2r^2+r^2+2tr\ell.
\]

By (2.1), `t²≤13/15` and `t<1`, so

\[
|ta-c|^2
\le \frac37\left(1+\frac{13}{15}\right)+\frac{t}{7}
=\frac45+\frac t7
<\frac{33}{35}<1. \tag{3.3}
\]

Thus (3.2) is an actual unit-diameter subset of `L`, contains the chosen north-pole point `c`, and has exactly one maximum-distance pair: its two sector points. Its cap point is joined to neither endpoint in the diameter graph. In particular the old greater-than-one pair has **not** been put directly into a unit-diameter input; the rescaling and the two strict inequalities (3.3) are the necessary compatibility check.

For (3.1), put the two points in separate parts. For (3.2), put `c` and either one of the sector points together and put the other sector point alone. The first part has squared diameter less than `33/35`, and the second has diameter zero. Each nonempty restricted atom contains one point, so these are literal coarsenings of the atom restrictions `A_i∩K`; no restricted atom is split. A one-part partition is impossible because `diam K=1`. Consequently every member of `F_2` has input-specific coarsening number exactly two.

All these assertions hold uniformly for the legal cap parameter and the chosen horizontal frame. For a rotated frame, rotate the horizontal components and sector labels together. No continuum conclusion is inferred from a finite sampled configuration: the displayed formulas prove the entire stated parameter range.

## 4. Aggregate graph versus an actual common coloring

For any family `F` of the above finite inputs, define the input-indexed atom graph `G_K` by putting an edge `{i,j}` precisely when there is a distance-one pair in `K` with one point in `A_i` and the other in `A_j`. All internal atom restrictions have diameter strictly below one. Thus a label coloring works on this particular input exactly when it is proper for `G_K`.

Define the aggregate graph

\[
G_{\rm agg}(F)=\bigcup_{K\in F}G_K,
\]

where the union retains only the edge labels, forgetting which input supplies them. A single fixed atom-label coloring valid for all `K∈F` is exactly a proper coloring of this union graph. That is a correct use of the aggregate graph.

For `F_2`, equations (3.1)–(3.2) realize every unordered atom-label pair as a distance-one pair on its own admissible input. Hence

\[
G_{\rm agg}(F_2)=K_{33},\qquad
\min_{\text{one coloring valid for all }K\in F_2}\#\text{colors}=33,
\qquad
\max_{K\in F_2}\min_{\text{coloring for this }K}\#\text{colors}=2. \tag{4.1}
\]

The difference in (4.1) is not caused by a non-Euclidean metric or a violation of the unit-diameter input contract. It is the order of quantifiers. In particular the aggregate edge list is adequate for the common-coloring query but does not certify that some single admissible input has chromatic number 33.

## 5. The same aggregate readout can have adaptive cost seven

We now align a standard regular simplex with the same old lens and atom labels. Let `1=(1,1,1,1,1)` in the horizontal five-space, and put

\[
s=\sqrt{6/5},\qquad a=\frac{1-\sqrt6}{5\sqrt5},\qquad
v_i=s e_i+a\mathbf1\ (1\le i\le5),\qquad
v_6=-\mathbf1/\sqrt5.
\]

For each `i≤5`, its coordinate in position `i` is `(4√6+1)/(5√5)>0`, and all other coordinates are `a<0`; `v_6` has every coordinate negative. Thus these six vectors belong to six distinct strict sign sectors. Since `s+5a=1/√5`, direct inner products give

\[
|v_i|^2=1,\qquad v_i\cdot v_j=-1/5\quad(i\ne j),
\]

including `v_6`: for the first five, `2sa+5a²=((s+5a)²-s²)/5=−1/5`; their norms are then `s²−1/5=1`; their product with `v_6` is `−(s+5a)/√5=−1/5`.

Set

\[
K_* = \{c\}\cup\{\rho v_i-\ell e_6:1\le i\le6\}. \tag{5.1}
\]

Every point is in the same lens. Its six lower points have pairwise squared distance

\[
2\rho^2(1+1/5)=2\cdot\frac5{12}\cdot\frac65=1,
\]

and each has distance one from `c` by §2. Therefore (5.1) is a seven-point unit-diameter regular simplex with one point in the cap and one in each of six distinct sectors. Any strict-smaller-diameter part contains at most one point. Its exact input-specific coarsening number is seven. This uses the standard simplex obstruction in an explicit source-compatible placement; no new general simplex theorem is claimed.

Let `F_7=F_2∪{K_*}`. The already complete aggregate graph cannot change, while the worst adaptive cost becomes seven:

\[
G_{\rm agg}(F_7)=G_{\rm agg}(F_2)=K_{33},\qquad
\max_{K\in F_7}\min_{\text{coloring for }K}\#\text{colors}=7. \tag{5.2}
\]

The minimum number of colors for one coloring valid on the whole family remains 33. If a comparison also retains the number of indexed inputs, append one repeated two-point input to `F_2`: both indexed families then have 529 indices, the same aggregate graph and common-coloring cost, but adaptive costs two and seven. This does not claim that finer data such as the whole input-to-edge incidence table agree.

## 6. Reusable interface and scope of the finding

The correct finite-family interface retains `(input identity, atom labels, diameter-edge incidence)`. Its two queries are different:

- **One common coloring:** color the union graph. Aggregation is safe for this query.
- **A coloring chosen for each input:** evaluate each indexed graph, or retain another proved sufficient representation. Aggregating away input identity is insufficient; (5.2) gives an exact same-readout counterexample inside R6.

For a continuous construction or universal Borsuk proof, this finite interface still requires a separate continuous coverage/strict-diameter bridge. The construction above is only a sharp negative test of a proposed information-erasure step. It gives no universal adaptive partition for all `K⊂L`, no 32-part scheme, and no new numerical upper or lower bound on `b(6)`. The source's dated `7≤b(6)≤33` status is not refreshed by a literature search here.

The fixed whole-lens `K_33` theorem is preserved. The point is that its witnesses can be compatible **separately** with legal inputs while failing to certify that their full edge pattern is jointly forced by one input. The current counterexample does not assert that no legal input can yield a more complicated atom graph; it says that the aggregate list alone does not decide that question.

Bounded deduplication consumed GEO7 and GEO8 full returns, GEO8 artifacts and handoff, and GEO9 construction/audit Taskbooks. Searches for adaptive coarsening, quantifier and same-input provenance did not locate this explicit geometric family in those sources. This is not an exhaustive project or literature novelty claim. Graph coloring, the regular simplex and basic norm calculations are existing methods; the new local contribution is their exact composition into this source-matched 2-versus-7 readout counterexample.

Scientific work was written hand proof only. No old checker, scientific program, sampled point cloud, floating-point search, BRC operation or formal Task core was run. All coordinates are external Euclidean geometry; no native P000 metric or new native spatial dimension is inferred. Formal GEO9 gates and ownership remain unchanged. The author supplies no independent review, and root supplies zero mathematical votes. A distinct noncontributing reader should review the frozen proof before it is promoted beyond an author result.

Researcher-ID: EM-C34-D16900 / TASK_RESEARCH  
EM-Source-Status: Read=Verified snapshot and current remote path blobs; Write=⚠ Not written — Source publication pending; local draft preserved. Identity registration remains pending.
