# Uniformly twisted Euler cohomology and the integral endpoint residual

Status: `FREE_RESEARCH / EXACT INTEGRAL BRIDGE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Why the mod-two bridge has an integral origin

The preceding theorem identified the chirality-holonomy space

\[
H^1(K_4;\mathbf F_2)
\]

with the mod-two endpoint-residual module.  A naive integral lift fails if one keeps ordinary untwisted graph coefficients:

\[
H^1(K_4;\mathbf Z)\simeq\mathbf Z^3,
\]

whereas the endpoint-sum residual has type

\[
\mathbf Z^2\oplus\mathbf Z/2.
\]

The resolution is that the endpoint map is not the ordinary oriented coboundary.  It is the coboundary for the unique fully tetrahedrally symmetric **nontrivial sign local system** on the graph.

Let every oriented edge of `K4` transport a one-dimensional integer fiber by multiplication by `-1`.  For an oriented edge `i -> j`, the twisted coboundary is

\[
(d_-v)_{ij}=v_j-(-1)v_i=v_i+v_j.
\]

Therefore:

\[
\boxed{
\text{endpoint-sum map}
=
\text{uniformly sign-twisted graph coboundary}.
}
\]

This is an exact integral statement, not merely a mod-two analogy.

## 2. The two symmetric chirality backgrounds

An overlap-sign connection on the six edges is an element of

\[
C^1(K_4;\mathbf F_2).
\]

Modulo vertex gauge, the `S4`-fixed classes are exactly two:

1. the flat class, represented by all edge bits zero;
2. the uniformly twisted class, represented by all edge bits one.

The flat class has face holonomy zero on every triangle.  Its integral coefficient transport is `+1`, and its coboundary is the ordinary oriented incidence map

\[
(d_+v)_{ij}=v_j-v_i.
\]

The uniformly twisted class has face holonomy one on every triangle.  Its coefficient transport is `-1`, and its coboundary is the endpoint-sum map

\[
(d_-v)_{ij}=v_j+v_i.
\]

Thus full tetrahedral symmetry alone does not force flatness.  It leaves precisely two symmetric phases:

\[
\boxed{
\text{untwisted global-}J\text{ phase}
\quad\text{or}\quad
\text{uniformly twisted projective-Euler phase}.
}
\]

An orientation-preserving transport axiom selects the first.  A shared-line reflection law selects the second.  Current P000/FCC incidence alone selects neither.

## 3. Ordinary and twisted incidence matrices

Orient every edge from the lower-labelled to the higher-labelled vertex in the order

\[
AB,AC,AD,BC,BD,CD.
\]

The ordinary incidence matrix is

\[
D_+=
\begin{pmatrix}
-1& 1& 0& 0\\
-1& 0& 1& 0\\
-1& 0& 0& 1\\
 0&-1& 1& 0\\
 0&-1& 0& 1\\
 0& 0&-1& 1
\end{pmatrix}.
\]

The uniformly twisted incidence matrix is

\[
D_-=
\begin{pmatrix}
1&1&0&0\\
1&0&1&0\\
1&0&0&1\\
0&1&1&0\\
0&1&0&1\\
0&0&1&1
\end{pmatrix}.
\]

Their Smith data are:

\[
\operatorname{SNF}(D_+)=\operatorname{diag}(1,1,1,0),
\]

\[
\boxed{
\operatorname{SNF}(D_-)=\operatorname{diag}(1,1,1,2).
}
\]

Consequently the graph one-cochain quotients are

\[
\operatorname{coker}D_+
\simeq
\mathbf Z^3,
\]

and

\[
\boxed{
\operatorname{coker}D_-
\simeq
\mathbf Z^2\oplus\mathbf Z/2.
}
\]

The primitive two-torsion is therefore created by the uniformly reversing local system on the odd triangular cycles of `K4`.

This is the standard signless-incidence phenomenon for a connected non-bipartite graph, specialized here to the tetrahedral Euler atlas.  No historical novelty is claimed for the general graph theorem.  The new project-level point is the exact identification of the previously derived endpoint residual with this chirality-twisted Euler coefficient system.

## 4. Why characteristic two hid the distinction

Modulo two,

\[
-1=+1.
\]

Therefore

\[
D_+\equiv D_-\pmod2.
\]

The untwisted and uniformly twisted coefficient systems become identical after reduction to `F2`.  This explains why both the Euler face-holonomy quotient and the endpoint residual reduce to the same three-dimensional `S4` module:

\[
\boxed{
H^1(K_4;\mathbf F_2)
\simeq
(\operatorname{coker}D_-)/2
\simeq
\operatorname{Aff}(\mathbf F_2^2,\mathbf F_2).
}
\]

The earlier mod-two bridge was therefore not accidental.  It was the characteristic-two shadow of two different integral coefficient systems.

## 5. The zero-total precision sector

The precision-pi endpoint residual was originally formulated with zero-total vertex and edge states:

\[
V_0=\left\{v\in\mathbf Z^4:\sum_i v_i=0\right\},
\]

\[
E_0=\left\{x\in\mathbf Z^6:\sum_e x_e=0\right\},
\]

\[
Q_0=E_0/D_-(V_0).
\]

For the twisted incidence,

\[
\sum_e(D_-v)_e=3\sum_i v_i,
\]

because every tetrahedral vertex occurs in three edges.

Hence total edge mass modulo three is invariant under the full twisted coboundary.  Define

\[
\overline T:\operatorname{coker}D_-\longrightarrow\mathbf Z/3,
\qquad
\overline T([x])=\sum_e x_e\pmod3.
\]

### Theorem 5.1 — exact neutral-sector sequence

There is a canonical exact sequence

\[
\boxed{
0\longrightarrow Q_0
\longrightarrow\operatorname{coker}D_-
\xrightarrow{\overline T}\mathbf Z/3
\longrightarrow0.
}
\]

Proof.

- Well-definedness follows from `sum(D_-v)=3 sum(v)`.
- Surjectivity is witnessed by one basis edge, whose total is one.
- If `sum(x)=3m`, choose a vertex vector with total `m`; subtracting its twisted coboundary produces a zero-total representative.
- If a zero-total representative is a full twisted coboundary, then `3 sum(v)=0`, hence `sum(v)=0`, so the representing vertex vector already lies in `V0`.  This proves injectivity of the neutral sector.

The sequence is non-split.  Indeed,

\[
\operatorname{coker}D_-\simeq\mathbf Z^2\oplus\mathbf Z/2
\]

has no element of order three, so it cannot contain the image of a section from `Z/3`.

Thus the precision-pi residual is the canonical total-neutral, index-three sector of the uniformly twisted Euler cohomology.

The quotient `Z/3` is a natural degree-three charge arising because every vertex touches three edges.  Its possible relation to the three positive axis families is a candidate interface, not yet an identity theorem.

## 6. A forced symmetric kernel-to-torsion bridge

Let

\[
K=\ker(C_{12}\to C_6)\simeq\mathbf F_2
\]

be the local binary root sheet.  The tetrahedral symmetry acts trivially on this abstract kernel bit.

Let

\[
\mathcal R_2=Q_0/2Q_0
\]

be the mod-two endpoint residual.  The fixed subspace of its `S4` action is exactly

\[
\{0,\tau\},
\]

where `tau` is the constant-one/torsion state.

Any `S4`-equivariant homomorphism

\[
\iota:K\longrightarrow\mathcal R_2
\]

is determined by `iota(1)`, which must be fixed by `S4`.  Therefore there are exactly two such maps:

1. the zero map;
2. the unique nonzero map sending the root-sheet generator to `tau`.

Hence:

\[
\boxed{
\text{ANY NONZERO FULLY }S_4\text{-SYMMETRIC BRIDGE}
\quad
K\to\mathcal R_2
\quad
\text{IS UNIQUE AND LANDS IN ENDPOINT TORSION}.
}
\]

This is stronger than a visual analogy and weaker than an unconditional native identification.  It proves that once one assumes a nonzero symmetry-respecting coupling between the local root sheet and the global endpoint residual, there is no remaining choice.

## 7. Projective Euler meaning of the twisted phase

In the untwisted phase a globally signed `J` exists.  The odd/sine channel is an ordinary global scalar coordinate relative to that sign.

In the uniformly twisted phase the local `J` changes sign across every edge and around every triangle.  It does not extend over a filled triangular face as a signed section.  Nevertheless:

\[
(+J)^2=(-J)^2=-1.
\]

All chirality-even observables descend:

- the half-period endpoint `-1`;
- the norm;
- the even/cosine channel;
- scalar polygonal period bounds;
- precision-pi readouts.

The odd/sine coordinate is instead a section of the sign local system.

Therefore the uniformly twisted phase has a natural **projective Euler structure**: it lacks one global signed generator but retains the scalar half-period and all reversal-even pi observables.

This gives an exact structural explanation for why continuous scalar mathematics can recover the common period while forgetting a discrete torsion sheet.

## 8. What is now resolved

The previous open statement was:

> determine whether the Euler chirality holonomy and the tetrahedral endpoint residual are really related or merely dimensionally analogous.

The answer is now two-tiered.

1. **Mod two:** they are canonically the same `S4` representation.
2. **Over the integers:** the endpoint residual is the one-cochain quotient for the unique fully symmetric uniformly reversing sign local system; it is not ordinary untwisted graph cohomology.

The torsion is exactly the integral memory of that twist.

## 9. Remaining native boundary

The remaining question is no longer algebraic classification.  It is dynamical selection:

1. Does actual six-dimensional Cell transport induce the flat symmetric phase or the uniformly twisted symmetric phase?
2. If it induces neither, which of the six edge-orbit holonomy classes appears?
3. Does an ambient-orientation rule force the flat phase?
4. Does a shared-line reflection or resonance rule force the uniformly twisted phase?
5. Is the canonical modulo-three total charge realized by the three positive-axis families?

Until such a transport law is derived, both symmetric phases must remain mathematically available.  The scalar Euler/precision-pi sector survives in either phase; a global oriented sine channel distinguishes them.
