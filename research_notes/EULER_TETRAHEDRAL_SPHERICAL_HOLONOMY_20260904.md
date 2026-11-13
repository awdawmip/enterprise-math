# Tetrahedral slice transport and the Euler half-turn holonomy

Status: `FREE_RESEARCH / EXACT CARRIER HOLONOMY / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Main result

The four FCC three-axis carrier slices have normal vectors

\[
\begin{aligned}
n_A&=(1,-1,-1),&n_B&=(-1,1,-1),\\
n_C&=(-1,-1,1),&n_D&=(1,1,1).
\end{aligned}
\]

They satisfy

\[
\lVert n_v\rVert^2=3,
\qquad
n_u\cdot n_v=-1\quad(u\ne v),
\qquad
n_A+n_B+n_C+n_D=0.
\]

Thus the normalized vectors `u_v=n_v/sqrt(3)` are the vertices of a regular tetrahedron on the unit sphere.

For every ordered pair of distinct slices, take the unique shortest proper rotation `T_uv in SO(3)` carrying `u_u` to `u_v`.  Then for every three distinct slices `u,v,w`,

\[
\boxed{
T_{wu}T_{vw}T_{uv}
=
2u_u u_u^{\mathsf T}-I.
}
\]

The right side fixes the starting normal and negates its tangent plane.  Hence, on the starting three-axis slice,

\[
\boxed{
\left.T_{wu}T_{vw}T_{uv}\right|_{u_u^\perp}=-I.
}
\]

A line segment transported through any triangular three-slice loop therefore returns with its orientation reversed.  This is an exact finite matrix theorem.  No angle, trigonometric function, or numerical value of pi is required for the identity.

After the standard continuous phase identification, the same holonomy is

\[
\boxed{
\exp(\pi J_u)=-I,
}
\]

so the geometric Euler half-turn is the curvature holonomy of one tetrahedral slice triangle.

## 2. Exact Rodrigues transport

Let `[k]_x` denote the cross-product matrix `x -> k cross x`.  Since

\[
u_u\cdot u_v=-\frac13,
\qquad
u_u\times u_v=\frac{n_u\times n_v}{3},
\]

the shortest rotation has the rational form

\[
\boxed{
T_{uv}
=I+\frac13[n_u\times n_v]_\times
 +\frac16[n_u\times n_v]_\times^2.
}
\]

This expression proves directly that

\[
T_{uv}n_u=n_v,
\qquad
T_{vu}=T_{uv}^{-1},
\qquad
T_{uv}^{\mathsf T}T_{uv}=I,
\qquad
\det T_{uv}=1.
\]

For example,

\[
T_{AB}=\frac13
\begin{pmatrix}
1&2&2\\
2&1&-2\\
-2&2&-1
\end{pmatrix},
\]

\[
T_{BC}=\frac13
\begin{pmatrix}
-1&-2&2\\
2&1&2\\
-2&2&1
\end{pmatrix},
\]

\[
T_{CA}=\frac13
\begin{pmatrix}
1&-2&2\\
2&-1&-2\\
2&2&1
\end{pmatrix}.
\]

Their exact product is

\[
T_{CA}T_{BC}T_{AB}
=
\frac13
\begin{pmatrix}
-1&-2&-2\\
-2&-1&2\\
-2&2&-1
\end{pmatrix}
=
\frac23n_A n_A^{\mathsf T}-I.
\]

The same formula holds for all 24 ordered triangular loops.

## 3. Spin lift and the hidden sign

Write a quaternion as `(r,x)` with scalar part `r` and vector part `x`.  Define the integral scaled edge spinor

\[
\boxed{
p_{uv}=\left(1,\frac{n_u\times n_v}{2}\right).
}
\]

Every cross product has coordinates in `{0,+2,-2}`, so `p_uv` is integral, and

\[
N(p_{uv})=3.
\]

The corresponding unit spinor is

\[
q_{uv}=\frac{p_{uv}}{\sqrt3}.
\]

It projects to `T_uv` under the standard double cover `Spin(3)->SO(3)`.

For three distinct vertices define

\[
s_{uvw}=\frac{\det(n_u,n_v,n_w)}4\in\{+1,-1\}.
\]

### Theorem 3.1 — exact face-spinor product

\[
\boxed{
p_{wu}p_{vw}p_{uv}
=3s_{uvw}(0,n_u).
}
\]

Consequently

\[
\boxed{
q_{wu}q_{vw}q_{uv}
=s_{uvw}\left(0,\frac{n_u}{\sqrt3}\right),
}
\]

which is a pure unit quaternion and therefore squares to `-1`.

Reversing the triangular loop flips `s_uvw`, so the two oriented loops have opposite Spin lifts.  Nevertheless `q` and `-q` project to the same `SO(3)` rotation.  Therefore:

\[
\boxed{
\text{triangle orientation is retained as a Spin }C_2\text{ sign,}
}
\]

while

\[
\boxed{
\text{the tangent-plane Euler half-turn is orientation independent.}
}
\]

This gives a concrete new candidate bridge to the recurring project-level two-torsion phenomena, but no identity with the earlier tetrahedral residual `C2`, backtracking sign, or Pell-shell sign is asserted here.

## 4. The third appearance of the Cell radius

The scalar component of the shortest transition spinor is

\[
\sqrt{\frac{1+u_u\cdot u_v}{2}}
=
\sqrt{\frac{1-1/3}{2}}
=
\frac1{\sqrt3}.
\]

Thus the same number

\[
\boxed{r_{\rm Cell}=\frac1{\sqrt3}}
\]

now has three independent roles:

1. the critical overlap radius of the triangular Cell carrier;
2. the unique positive normalization in
   \[
   J=(R-R^{-1})/\sqrt3,
   \qquad J^2=-1;
   \]
3. the scalar/half-angle coordinate of every minimal transition spinor between tetrahedral slice normals.

The third equality is not fitted to pi.  It follows only from the regular tetrahedral Gram matrix.

## 5. Spherical triangle and pi

At a vertex `u`, the tangent toward another vertex `v` is proportional to

\[
t_{uv}=u_v+\frac13u_u.
\]

For distinct `u,v,w`,

\[
\lVert t_{uv}\rVert^2=\frac89,
\qquad
t_{uv}\cdot t_{uw}=-\frac49.
\]

Hence every spherical interior angle has cosine `-1/2`, so it is `2pi/3` in the standard Archimedean angular normalization.  The spherical excess is

\[
3\cdot\frac{2\pi}{3}-\pi=\pi.
\]

Equivalently, the four congruent spherical faces tile the unit sphere, whose area is `4pi`, so each face has area `pi`.

By the standard spherical holonomy/Gauss--Bonnet theorem, parallel transport around a geodesic triangle rotates its tangent frame by the enclosed oriented area.  Therefore the exact finite matrix result and the standard continuous result coincide:

\[
\boxed{
\text{spherical face area}=\pi
\quad\Longleftrightarrow\quad
\text{tangent holonomy}=\exp(\pi J)=-I.
}
\]

The algebraic product proves the half-turn first; standard spherical geometry identifies its continuous phase length as pi.

## 6. Relation to the O(2) globalization theorem

The preceding `O(2)` result showed that local signed generators may be glued by either identity or conjugation and that `-1` survives every chirality reversal.  The present theorem identifies an independent source of the same endpoint:

\[
\boxed{
\text{three minimal slice transports}
\longrightarrow
\text{one tangent half-turn }-I.
}
\]

The two layers must not be conflated:

- an edge `C2` handoff records discrete chirality reversal between local frames;
- the `SO(3)` product records noncommutative curvature of the tetrahedral normal connection;
- the face Spin sign remembers loop orientation;
- the projected tangent holonomy is the orientation-independent Euler endpoint.

Thus even a locally chirality-preserving connection can have nontrivial triangular half-turn holonomy.

## 7. Stronger geometric reading of Euler's identity

Within one starting slice, let `J_u` be its normalized chiral complex structure.  Then

\[
\boxed{
T_{wu}T_{vw}T_{uv}|_{u_u^\perp}
=
\exp(\pi J_u)
=-I.
}
\]

Accordingly, the geometric statement behind

\[
e^{i\pi}+1=0
\]

can be read as follows:

> parallel transport of an oriented line segment through the three minimal handoffs around any tetrahedral slice face returns the segment reversed; adding that reversed character to the identity character gives zero.

Here:

- `i` is the local tangent-plane chiral generator;
- `e` is continuous transport/composition;
- `pi` is the spherical-face holonomy phase;
- `-1` is line-segment reversal;
- `0` is additive cancellation of antipodal characters.

## 8. Boundaries

Proved at the selected FCC carrier level:

- the regular tetrahedral Gram relations of the four slice normals;
- the rational shortest-rotation matrices;
- the exact triangular matrix product;
- reversal of every tangent vector in the starting slice;
- the integral Spin lift and its orientation sign;
- the repeated appearance of `1/sqrt(3)`;
- the standard spherical-area/holonomy identification.

Not proved:

- that P000 native six-dimensional dynamics must use these shortest `SO(3)` handoffs;
- that the carrier sphere is the primitive native angle/area object;
- that the Spin sign is one of the already discovered native `C2` classes;
- that all admissible six-dimensional rotations factor through the four-normal connection.

The theorem nevertheless advances the native-lift problem substantially: the selected carrier already contains an exact three-handoff loop whose action on a line segment is the Euler half-turn.