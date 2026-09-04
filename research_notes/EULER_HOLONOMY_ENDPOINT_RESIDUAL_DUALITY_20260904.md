# Euler face holonomy and tetrahedral endpoint residual are the same mod-two S4 module

Status: `FREE_RESEARCH / EXACT FINITE REPRESENTATION BRIDGE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Statement of the bridge

Two three-dimensional `F2` modules have appeared independently in the Enterprise Math program.

The first is the chirality-holonomy space of the four-slice overlap graph:

\[
\mathcal H
=
C^1(K_4;\mathbf F_2)/\delta C^0(K_4;\mathbf F_2)
\simeq\mathbf F_2^3.
\]

The second is the mod-two reduction of the tetrahedral endpoint-sum residual:

\[
\mathcal R_2
=
\left(E_0/\delta V_0\right)/2\left(E_0/\delta V_0\right)
\simeq
(\mathbf Z^2\oplus\mathbf Z/2)/2
\simeq\mathbf F_2^3.
\]

The equality of dimensions alone proves nothing. This note constructs an explicit `S4`-equivariant isomorphism and identifies its distinguished invariant line.

The result is:

\[
\boxed{\mathcal H\simeq_{S_4}\mathcal R_2.}
\]

Under this map, the unique nonzero `S4`-invariant chirality-holonomy class corresponds to the mod-two image of the primitive endpoint-sum two-torsion class.

This is a representation-level identification. It does not identify the local kernel element of `C12 -> C6` with the integral endpoint-sum torsion generator as native operations.

## 2. Face holonomy as an even function on four vertices

Let the tetrahedron have vertices

\[
V=\{A,B,C,D\}.
\]

For an overlap-sign cochain `epsilon`, write the four face holonomies as

\[
(h_{ABC},h_{ABD},h_{ACD},h_{BCD}).
\]

Their sum is zero because each edge occurs in exactly two faces:

\[
 h_{ABC}+h_{ABD}+h_{ACD}+h_{BCD}=0.
\]

Associate each face to its opposite vertex:

\[
A\leftrightarrow BCD,
\quad
B\leftrightarrow ACD,
\quad
C\leftrightarrow ABD,
\quad
D\leftrightarrow ABC.
\]

Define the opposite-face value function

\[
F_\varepsilon:V\to\mathbf F_2
\]

by

\[
\boxed{
(F_\varepsilon(A),F_\varepsilon(B),F_\varepsilon(C),F_\varepsilon(D))
=
(h_{BCD},h_{ACD},h_{ABD},h_{ABC}).
}
\]

It satisfies

\[
\sum_{v\in V}F_\varepsilon(v)=0.
\]

Thus face holonomy takes values in the canonical even-parity permutation module

\[
\mathcal E(V)
=
\left\{F:V\to\mathbf F_2:\sum_vF(v)=0\right\}.
\]

The face-flatness theorem says that the kernel of this map is exactly the coboundary space. Therefore it induces an isomorphism

\[
\boxed{\mathcal H\simeq\mathcal E(V).}
\]

The construction uses only the canonical opposite-face duality and is `S4`-equivariant.

## 3. Endpoint residual as the same even function module

Choose any affine labeling

\[
A=(0,0),
\quad B=(1,0),
\quad C=(0,1),
\quad D=(1,1)
\]

of the four vertices by `F2^2`. Every permutation of the four points is affine because

\[
\operatorname{AGL}(2,2)\simeq S_4.
\]

The endpoint residual normal coordinates are

\[
(p,q,e)\in\mathbf F_2^3,
\]

with affine evaluation

\[
f_{p,q,e}(x,y)=e+px+qy.
\]

Its four values are

\[
\boxed{
(e,e+p,e+q,e+p+q).
}
\]

They always have even parity. Conversely, any even four-value vector determines a unique affine function:

\[
e=F(A),
\qquad
p=F(A)+F(B),
\qquad
q=F(A)+F(C).
\]

Therefore evaluation gives a canonical `S4`-equivariant isomorphism

\[
\boxed{\mathcal R_2\simeq\mathcal E(V).}
\]

The adjective canonical is justified despite the temporary coordinate labeling: on four points the set of affine transformations is the full symmetric group, and the image is the coordinate-free even-parity subspace.

## 4. Explicit holonomy-to-residual formula

Combining the two maps gives the desired bridge.

Let

\[
h_D=h_{ABC},
\quad
h_C=h_{ABD},
\quad
h_B=h_{ACD},
\quad
h_A=h_{BCD}.
\]

Then

\[
\boxed{
\begin{aligned}
e&=h_A=h_{BCD},\\
p&=h_A+h_B=h_{BCD}+h_{ACD},\\
q&=h_A+h_C=h_{BCD}+h_{ABD}.
\end{aligned}
}
\]

The inverse map is

\[
\boxed{
\begin{aligned}
h_{ABC}&=e+p+q,\\
h_{ABD}&=e+q,\\
h_{ACD}&=e+p,\\
h_{BCD}&=e.
\end{aligned}
}
\]

These formulas are mutual inverses over `F2`.

Consequently two edge-sign cochains are gauge-equivalent if and only if they have the same endpoint residual code under this bridge.

## 5. The invariant class is exactly the torsion line

The `S4`-invariant vectors in the four-point permutation module are the constant functions. Inside the even-parity subspace there are exactly two:

\[
0000,
\qquad
1111.
\]

The nonzero one corresponds on the holonomy side to

\[
\boxed{
h_{ABC}=h_{ABD}=h_{ACD}=h_{BCD}=1.
}
\]

It is represented, for example, by assigning sign `1` to all six overlaps.

Under the explicit bridge it maps to

\[
(p,q,e)=(0,0,1),
\]

which is the nonzero constant affine function. In the integral endpoint-sum quotient this is precisely the mod-two shadow of the primitive order-two residual class.

Therefore:

\[
\boxed{
\text{UNIQUE S4-INVARIANT GLOBAL CHIRALITY DEFECT}
\longleftrightarrow
\text{ENDPOINT-RESIDUAL TWO-TORSION MOD 2}.
}
\]

This closes a previously open representation-level bridge.

It does **not** prove that one local overlap flip is the same physical operation as the integer endpoint-sum torsion generator. The theorem identifies the resulting global `S4` modules and their unique invariant lines.

## 6. The six remaining states reconstruct the six line families

The eight even functions on four points decompose as:

1. the zero function;
2. the constant-one torsion function;
3. six nonconstant affine functions.

Each nonconstant affine function is `1` on exactly two vertices. Its support is therefore one of the six two-element subsets of `V`, hence one edge of `K4`.

Thus the six non-invariant holonomy classes are naturally the six line-family/edge states.

Adding the torsion function complements the support:

\[
f\longmapsto f+1,
\qquad
\operatorname{supp}(f+1)=V\setminus\operatorname{supp}(f).
\]

For a two-point support, the complement is the unique opposite edge. Therefore the invariant torsion class acts by opposite-edge exchange.

This recovers the earlier endpoint-residual affine geometry directly from the Euler chirality-holonomy module.

## 7. Orbit structure

The `S4` orbit decomposition of either module is exactly

\[
\boxed{1+1+6.}
\]

- one zero state;
- one invariant torsion state;
- one orbit of six edge states.

No other `S4`-equivariant identification can move the invariant torsion state into the six-element orbit. In particular, once zero is fixed, the invariant line is forced.

The nontrivial bridge is therefore rigid at the level relevant to the torsion class.

## 8. Relation to projective Euler descent

The root-cover transition bits live on overlaps. Their graph gauge class is an element of `mathcal H`. The present theorem sends that class to an endpoint residual state.

- Flat chirality transport maps to the zero residual state.
- The uniform all-face-flip defect maps to pure two-torsion.
- The six other nonzero defect classes map to the parity shadows of the free `A2` residual directions.

This sharpens the statement that continuous scalar completion can lose discrete information. The known real endpoint-residual completion erases the integral torsion sheet while retaining the free two-dimensional residual plane. Under the bridge, the unique symmetric chirality defect is exactly the class attached to that erased torsion line.

The scalar Euler half-period endpoint remains invariant under local root inversion, so it is blind to this line. The oriented sine/odd channel is not.

## 9. Boundaries

The theorem proves an exact finite `S4`-module isomorphism. It does not prove:

- that a local `C12 -> C6` kernel element and the integral endpoint-sum torsion generator are identical native operations;
- that physical six-dimensional Cell transport realizes the uniform all-face-flip class;
- that the other two holonomy directions disappear under native completion;
- that the mod-two bridge uniquely lifts to an integral isomorphism;
- that the tetrahedral residual, backtracking chirality, and Pell shell sign are all one native class.

The correctly narrowed new frontier is:

> determine whether actual native transport induces the invariant holonomy line, one of the six edge classes, or only the flat zero class, and whether the representation bridge lifts to an operation-preserving integral construction.
