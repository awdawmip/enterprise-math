# Tetrahedral slice transport, half-turn holonomy, and Euler phase

Status: `FREE_RESEARCH / EXACT CARRIER THEOREM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Objective

The four FCC three-axis slices have previously been organized as the four vertices of a tetrahedral `K4`, with their six shared line families as the six edges.  A remaining question was whether the local chiral complex structures on the four slices glue canonically, and whether the resulting transport is flat.

This note gives a sharp answer.

1. Incidence alone does **not** determine the chirality transition on a shared line.  There are exactly two orthogonal bridges fixing that line and sending one slice normal to the other: a proper short rotation and an improper bisector reflection.
2. The proper bridge preserves the local complex structure; the improper bridge reverses it.
3. The explicit oriented normal-sphere embedding canonically selects the proper bridge as shortest `SO(3)` transport.
4. Proper chirality gluing is determinant-flat, but its full connection is not flat: the transport around every triangular face of the normal tetrahedron is exactly a half-turn on the starting slice.
5. This half-turn equals the square of the local chiral operator.  After the intrinsic rotation half-period is identified with classical pi, the face holonomy is exactly `exp(pi J)=-1`.

Thus the four-slice carrier does not merely admit an Euler character: every normal-tetrahedron face realizes the Euler half-turn as geometric holonomy.

## 2. Tetrahedral normals and slice planes

Use the four outward tetrahedral normals

\[
\begin{aligned}
n_0&=(1,1,1),\\
n_1&=(1,-1,-1),\\
n_2&=(-1,1,-1),\\
n_3&=(-1,-1,1).
\end{aligned}
\]

They satisfy

\[
n_i\cdot n_i=3,
\qquad
n_i\cdot n_j=-1\quad(i\ne j),
\qquad
n_0+n_1+n_2+n_3=0.
\]

The slice associated with `i` is

\[
P_i=n_i^\perp.
\]

For `i\ne j`, the common line is

\[
L_{ij}=P_i\cap P_j
=\mathbf R\,(n_i\times n_j).
\]

The six vectors `n_i x n_j`, up to sign, are exactly the six `<110>` FCC line families.

Define the local chiral operator

\[
J_i(v)=\frac1{\sqrt3}\,n_i\times v,
\qquad v\in P_i.
\]

The vector triple-product identity gives

\[
J_i^2=-I_{P_i}.
\]

The same normalization `1/sqrt(3)` is the critical Cell radius already selected by the triangular overlap geometry.  Here it appears independently as the unique positive scalar that converts the skew operator `n_i x` into a complex structure.

## 3. The two overlap bridges

Fix `i ne j`, and write

\[
c_{ij}=n_i\times n_j,
\qquad
m_{ij}=n_i-n_j.
\]

Then

\[
\lVert c_{ij}\rVert^2=8,
\qquad
\lVert m_{ij}\rVert^2=8.
\]

### 3.1 Proper shortest rotation

Let `[c]_x` denote the matrix of `v -> c x v`.  Define

\[
\boxed{
A_{ij}
=-\frac13I
+\frac16c_{ij}c_{ij}^{\mathsf T}
+\frac13[c_{ij}]_\times .
}
\]

This is Rodrigues' formula with axis `c_ij`, cosine `-1/3`, and the sign chosen so that `n_i` travels to `n_j` along the short oriented great-circle arc.  Direct exact calculation gives

\[
A_{ij}^{\mathsf T}A_{ij}=I,
\qquad
\det A_{ij}=1,
\]

\[
A_{ij}n_i=n_j,
\qquad
A_{ij}c_{ij}=c_{ij},
\qquad
A_{ji}=A_{ij}^{-1}.
\]

### 3.2 Improper bisector reflection

Define the Householder bridge

\[
\boxed{
H_{ij}
=I-\frac14m_{ij}m_{ij}^{\mathsf T}.
}
\]

It also satisfies

\[
H_{ij}^{\mathsf T}H_{ij}=I,
\qquad
H_{ij}n_i=n_j,
\qquad
H_{ij}c_{ij}=c_{ij},
\]

but

\[
\det H_{ij}=-1,
\qquad
H_{ij}^2=I.
\]

### Theorem 3.1 — overlap-transport dichotomy

Among orthogonal maps that fix `L_ij` pointwise and send `n_i` to `n_j`, there are exactly two: `A_ij` and `H_ij`.  They have opposite determinant.

Proof.  Split `R^3` as the fixed line `L_ij` plus its orthogonal two-plane.  In the two-plane, an orthogonal map sending the unit vector `n_i/sqrt(3)` to `n_j/sqrt(3)` is determined by the sign chosen for the perpendicular unit vector.  The two choices are the proper rotation and the reflection above.

Consequently, the bare `K4` incidence relation cannot choose a chirality transition.  A transport convention is additional structure.

Freeze:

`FCC_INCIDENCE_ALONE_DOES_NOT_DETERMINE_CHIRALITY_TRANSPORT`.

## 4. Determinant controls the local complex-structure sign

For every orthogonal map `T`, cross products obey

\[
T(a\times b)=\det(T)\,(Ta\times Tb).
\]

If `T n_i=n_j`, then for `v in P_i`,

\[
T J_i v
=\det(T)J_jTv.
\]

Hence

\[
\boxed{
T J_iT^{-1}=\det(T)J_j.
}
\]

In particular,

\[
A_{ij}J_iA_{ij}^{-1}=J_j,
\]

whereas

\[
H_{ij}J_iH_{ij}^{-1}=-J_j.
\]

Thus the previously introduced `F2` chirality edge bit is exactly the determinant parity of the selected orthogonal overlap transport.

The oriented normal-sphere embedding, together with ambient orientation and the short-geodesic rule, selects `A_ij`; therefore its determinant chirality cocycle is trivial.  The mirror convention selects `H_ij`; every edge then carries the nontrivial sign and every triangle has odd determinant holonomy.

This proves both a positive and a negative result:

- the embedded oriented carrier has a canonical proper chirality bridge;
- the incidence graph without that embedding does not.

## 5. Exact triangular holonomy of the proper bridge

For three distinct indices `i,j,k`, define the based face transport

\[
\operatorname{Hol}_{ijk}
=A_{ki}A_{jk}A_{ij}.
\]

### Theorem 5.1 — tetrahedral face half-turn

For every ordered triple of distinct indices,

\[
\boxed{
\operatorname{Hol}_{ijk}
=Q_i
:=\frac23n_in_i^{\mathsf T}-I.
}
\]

The right side is independent of which of the two orientations of the face boundary is used, because it is an involution.

It satisfies

\[
Q_i n_i=n_i,
\qquad
Q_i v=-v\quad(v\in P_i),
\qquad
Q_i^2=I,
\qquad
\det Q_i=1.
\]

Thus the proper transport around a triangular face is a rotation by one half-turn about the normal `n_i`.

### Exact base-face computation

For the face `0 -> 1 -> 2 -> 0`,

\[
A_{01}=\frac13
\begin{pmatrix}
-1&2&2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix},
\]

\[
A_{12}=\frac13
\begin{pmatrix}
1&2&2\\
2&1&-2\\
-2&2&-1
\end{pmatrix},
\]

\[
A_{20}=\frac13
\begin{pmatrix}
1&2&-2\\
-2&-1&-2\\
-2&2&1
\end{pmatrix}.
\]

First,

\[
A_{12}A_{01}=\operatorname{diag}(-1,1,-1).
\]

Then

\[
A_{20}A_{12}A_{01}
=\frac13
\begin{pmatrix}
-1&2&2\\
2&-1&2\\
2&2&-1
\end{pmatrix}
=\frac23n_0n_0^{\mathsf T}-I.
\]

Tetrahedral symmetry and reversal of the oriented boundary give the remaining faces and ordered triples.

## 6. The face holonomy is the square of `J`

On `P_i`,

\[
J_i^2=-I_{P_i}.
\]

Theorem 5.1 therefore gives the exact operator identity

\[
\boxed{
\operatorname{Hol}_{ijk}|_{P_i}
=J_i^2
=-I_{P_i}.
}
\]

This supplies a new geometric role for the imaginary unit:

\[
\boxed{
J_i
=\text{a chirality-selected square root of tetrahedral face holonomy}.
}
\]

The two roots `+J_i` and `-J_i` correspond to the two possible orientations of a quarter-turn frame.  The endpoint half-turn itself does not remember which orientation was used.

Every oriented shared line vector in `P_i` is reversed after one face loop:

\[
\operatorname{Hol}_{ijk}(n_i\times n_j)
=-(n_i\times n_j).
\]

Hence the holonomy acts directly on line segments: it fixes each underlying unoriented line family while reversing its orientation.

## 7. Spherical area and the phase `pi`

Normalize the normals to the unit sphere.  Every side of a normal-tetrahedron face has cosine

\[
\cos\alpha=-\frac13.
\]

For the equilateral spherical triangle, the spherical cosine law gives its vertex angle `beta`:

\[
\cos\beta
=\frac{\cos\alpha-\cos^2\alpha}{\sin^2\alpha}
=-\frac12.
\]

Therefore

\[
\beta=\frac{2\pi}{3},
\]

and the spherical excess is

\[
\boxed{
3\beta-\pi=\pi.
}
\]

The four congruent faces tile the unit normal sphere, each with area `pi` and total area `4 pi`.

The bridges `A_ij` are precisely geodesic parallel transports between the tangent planes `P_i=T_{n_i/sqrt(3)}S^2`.  The spherical holonomy theorem therefore assigns signed phase `+pi` or `-pi` according to boundary orientation.  At the operator level both orientations have the same endpoint because

\[
\exp(+\pi J_i)=\exp(-\pi J_i)=-I.
\]

Thus the exact rational matrix theorem and the standard spherical-area theorem agree:

\[
\boxed{
\operatorname{Hol}_{ijk}|_{P_i}
=\exp(\pi J_i)
=-I.
}
\]

After the previously constructed intrinsic rotation half-period satisfies `pi_rot=pi`, this becomes

\[
\boxed{
\operatorname{Hol}_{ijk}|_{P_i}
=\exp(\pi_{\rm rot}J_i).
}
\]

This is an Euler identity realized by one tetrahedral normal face.

## 8. Relation to the half-turn chirality obstruction

Reversing the orientation of the triangular boundary changes the lifted holonomy angle

\[
+\pi\longleftrightarrow-\pi,
\]

but does not change the finite endpoint `-I`.

This is exactly the geometry of the previously proved half-turn-lift no-go theorem:

- the finite half-turn residue has two equally short lifts;
- reflection exchanges the lifts;
- the endpoint does not choose one;
- an oriented path or chirality choice does.

The normal-tetrahedron face gives a canonical geometric witness for that ambiguity.  The clockwise and counterclockwise face loops realize the two lifts of the same orientation-reversal endpoint.

Hence the backtracking `C2` is no longer merely an abstract exceptional residue.  It is concretely realized by the two oriented lifts of tetrahedral face holonomy.

This statement does **not** identify that `C2` with the separate tetrahedral endpoint-sum torsion class.  Their actions differ: face holonomy reverses all oriented tangent directions while preserving their unoriented lines; endpoint-sum torsion exchanges opposite-edge supports in the affine residual model.

## 9. Two distinct obstruction layers

The calculation separates two structures that must not be conflated.

### 9.1 Chirality or determinant layer

The edge sign

\[
\varepsilon_{ij}=\det(T_{ij})\in\{+1,-1\}
\]

controls whether `J_i` is transported to `J_j` or `-J_j`.

For the proper bridges `A_ij`, all signs are `+1`; the `F2` chirality cocycle is flat and a coherent global choice of the sign of `J` exists, unique up to simultaneous reversal.

### 9.2 Connection phase layer

Even with determinant-flat proper bridges, the product around a triangular face is

\[
-I,
\]

not the identity.  This is curvature inside the complex-linear `U(1)` transport, not a failure to orient `J`.

Therefore

\[
\boxed{
\text{flat chirality sign}
\not\Rightarrow
\text{flat rotation connection}.
}
\]

The local complex structures glue, but local frames acquire a central half-turn around each face.

This is the finite tetrahedral manifestation of the standard distinction between an oriented tangent bundle and a flat trivialization of that bundle.

## 10. Mirror transport gives the contrasting non-complex-linear loop

If every edge uses the reflection `H_ij`, then a triangular composite has determinant `-1`, fixes the starting normal, and acts as a reflection on the starting tangent plane.  It conjugates

\[
J_i\longmapsto-J_i.
\]

Hence it is not a `U(1)` phase holonomy at all; it lies in the other component of `O(2)`.

The two choices therefore have sharply different outcomes:

\[
\begin{array}{c|c|c|c}
\text{bridge}&\det&J\text{-transport}&\text{triangle loop}\\
\hline
A_{ij}&+1&J_i\mapsto J_j&-I\in SO(2)\\
H_{ij}&-1&J_i\mapsto-J_j&\text{reflection}\in O(2)\setminus SO(2)
\end{array}
\]

This proves that requiring complex-linear Euler transport selects the proper bridge.

## 11. Consequences for Enterprise Euler geometry

The local three-axis and global four-slice descriptions now meet in one exact chain:

```text
four tetrahedral slice normals
 -> shared FCC line axes
 -> unique short proper overlap rotations
 -> coherent local chiral structures J_i
 -> half-turn phase holonomy around each K4 triangle
 -> chirality-selected square root J_i
 -> continuous character label exp(pi J_i) = -1
```

The formula

\[
\exp(\pi J_i)+I=0
\]

therefore has the following carrier-level meaning:

> Parallel transport an oriented line segment through the three slice changes around one normal-tetrahedron face.  The segment returns to the original slice on the same unoriented line, with its orientation reversed.  The signed lifted phase of this transport is one intrinsic half-period.

## 12. Exact status and open native boundary

Closed at the embedded FCC carrier level:

1. explicit proper and improper overlap bridges;
2. determinant control of the local `J` sign;
3. proof that incidence alone is insufficient;
4. canonical proper bridge from oriented shortest normal-sphere transport;
5. exact half-turn holonomy around every triangular slice loop;
6. identification of the face holonomy with `J_i^2`;
7. geometric realization of the two signed half-turn lifts;
8. separation of chirality flatness from `U(1)` connection curvature.

Still open at native P000 level:

1. proving that native six-dimensional Cell transition semantics selects the proper short transport rather than merely allowing it as a carrier readout;
2. constructing the transport directly from operation-safe native Cell/gate data rather than the ambient cross product;
3. deciding whether the resulting `U(1)` face curvature lifts to a native cohomology class;
4. relating, by an explicit intertwiner if one exists, the face half-turn, the endpoint-sum residual `C2`, and paired-Pell shell signs.

The first missing theorem is now sharply stated:

`NATIVE_CELL_TRANSPORT_SELECTS_ORIENTED_SHORTEST_SO3_SLICE_BRIDGE`.

Until that theorem is proved, the present result is an exact and canonical **carrier theorem**, not a Foundation identity.