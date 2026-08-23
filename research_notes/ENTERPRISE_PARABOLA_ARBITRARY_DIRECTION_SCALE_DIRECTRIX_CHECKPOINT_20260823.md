# Enterprise parabola — arbitrary-direction frame, scale correction, lattice index, and folded directrix

Status: `RESEARCH_CHECKPOINT / CANDIDATE_THEOREM_PACKAGE / NOT_CANONICAL`

Date: `2026-08-23`

Researcher-ID: `EM-RPBL-7E4C2A`

Task-ID: `RS-ENTERPRISE-PARABOLA-ARBITRARY-FRAME`

Base source: `522d1f9847b087eff380d79b506cb6924f5fa7cd`

## 0. Scope and claim typing

This checkpoint continues the already obtained standard-shape candidate

\[
T_1^2+T_2^2=\lambda U
\]

from the six basic directions to an arbitrary directed segment.

The following current foundations are retained:

- three positive native axes and three native right sectors;
- canonical directed-displacement addresses in `min=0` form;
- sector-local native Pythagorean length;
- directed line gauge and the distinction between a groupoid inverse trace and a newly decoded canonical reverse trace.

Additional user-frozen premise for this research line:

> Rotating any directed segment by carrier `120°` gives its Enterprise-orthogonal direction, and this applies to the segment itself.

Semantic classification:

- the integer address, cyclic rotation, directed trace, and native segment length are current declared/derived project objects;
- the carrier linear solve `(alpha,beta)` is an `I0_IMPLEMENTATION_CARRIER` calculation;
- the signed two-face unfolding and trace-group completion are `N2/N3 CONDITIONAL_DERIVED` tools;
- the focus/directrix theorem below is `DOMAIN_RESTRICTED_EXACT_RECOVERY`, not an N0 promotion;
- the current frozen directed gauge gives `NONRECOVERY` of the shape parabola as a global focus/directrix locus.

No classical focus/directrix definition is used to select the quadratic shape. The focus/directrix property is recovered only after the shape has independently been fixed by the rotated frame and constant-acceleration/discrete-quadratic law.

## 1. Arbitrary directed frame

Let

\[
S=(a,b,c)\in\mathbb N_0^3,\qquad \min(a,b,c)=0,\qquad S\ne0.
\]

Define the cyclic `120°` rotation

\[
\rho(a,b,c)=(c,a,b),\qquad \rho^2(a,b,c)=(b,c,a),\qquad \rho^3=\mathrm{id}.
\]

Write

\[
R=\rho S,\qquad R_2=\rho^2S.
\]

In the implementation carrier,

\[
S+R+R_2=(a+b+c)(1,1,1),
\]

so their carrier classes satisfy

\[
S+R+R_2\equiv0.
\]

This carrier relation is used only to decode/verify the frame. It is not promoted to a native vector identity.

Define

\[
\Delta_S=a^2+b^2+c^2-ab-bc-ca.
\]

For a carrier displacement represented by a canonical triple

\[
X=(A,B,C),
\]

define

\[
\alpha_S(X)=
\frac{(a-b)A+(b-c)B+(c-a)C}{\Delta_S},
\]

\[
\beta_S(X)=
\frac{(c-b)A+(a-c)B+(b-a)C}{\Delta_S}.
\]

Then

\[
X\equiv \alpha S+\beta R
\]

in the implementation carrier, and the coefficients are unique.

Let

\[
m=\min(\alpha,\beta,0)
\]

and define the local positive frame components

\[
(U,T_1,T_2)=(\alpha-m,\ \beta-m,\ -m).
\]

They satisfy

\[
U,T_1,T_2\ge0,\qquad \min(U,T_1,T_2)=0,
\]

and

\[
X\equiv US+T_1R+T_2R_2.
\]

### Exact inversion proof

Choose the carrier basis in which a triple `(x,y,z)` is represented by `(x-z,y-z)`. The two frame columns are

\[
S\mapsto(a-c,b-c),
\]

\[
R\mapsto(c-b,a-b).
\]

Their determinant is

\[
\det
\begin{pmatrix}
 a-c & c-b\\
 b-c & a-b
\end{pmatrix}
=\Delta_S.
\]

Cramer's rule gives the displayed formulas for `alpha` and `beta`.

## 2. Scale defect in the previous arbitrary-direction formula

The previous equation

\[
T_1^2+T_2^2=\lambda U
\]

is exact when `S` itself is part of the frame data and one copy of `S` is declared to be one local unit.

It is not, by itself, invariant under replacing the same direction by `kS`.

Define the oriented native length of the chosen segment

\[
q_S=L_E(S)=\sqrt{a^2+b^2+c^2}.
\]

The three rotated segments have the same oriented native length because cyclic permutation preserves the sum of squares.

The physical local coordinates are

\[
u=q_SU,\qquad t_1=q_ST_1,\qquad t_2=q_ST_2.
\]

Therefore the ray-scale-invariant Enterprise parabola with physical aperture/latus-rectum parameter `Lambda>0` is

\[
\boxed{
q_S\bigl(T_1^2+T_2^2\bigr)=\Lambda U.
}
\tag{P-E}
\]

Equivalently, with the frame-relative parameter

\[
\lambda=\frac{\Lambda}{q_S},
\]

one recovers

\[
T_1^2+T_2^2=\lambda U.
\]

### Scale covariance proof

For `S'=kS`,

\[
\Delta_{S'}=k^2\Delta_S,
\qquad
q_{S'}=kq_S,
\]

and the exact coefficient formulas give

\[
(\alpha',\beta',m',U',T_1',T_2')
=\frac1k(\alpha,\beta,m,U,T_1,T_2).
\]

Hence

\[
q_{S'}\bigl((T_1')^2+(T_2')^2\bigr)
=\Lambda U'
\]

is equivalent to `(P-E)`.

Thus:

- `lambda` is a framed-step parameter;
- `Lambda=q_S lambda` is the scale-independent physical parameter.

## 3. One-line global formula

The candidate `(P-E)` is equivalent to the following compact formula in the two carrier coefficients:

\[
\boxed{
q_S\,\beta^2
=
\Lambda\bigl(\alpha-\min(\beta,0)\bigr).
}
\tag{P-global}
\]

The two nonzero pieces are:

1. `alpha>=0`, `beta>=0`:

\[
q_S\beta^2=\Lambda\alpha;
\]

2. `beta<=0`, `beta<=alpha`:

\[
q_S\beta^2=\Lambda(\alpha-\beta).
\]

In the third local sector, where `alpha` is the minimum, `(P-E)` has only the origin as a solution. Hence the parabola occupies exactly the two native right sectors adjacent to the opening direction `S`.

## 4. Signed parameter and exact fold map

Let `t` be physical signed transverse coordinate and set

\[
u=\frac{t^2}{\Lambda}.
\]

Let

\[
\widehat S=\frac{S}{q_S},\qquad
\widehat R=\frac{R}{q_S},\qquad
\widehat R_2=\frac{R_2}{q_S}.
\]

The continuous analytic completion is

\[
P(t)=V+u\widehat S+
\begin{cases}
 t\widehat R,&t\ge0,\\
 (-t)\widehat R_2,&t\le0.
\end{cases}
\tag{Param}
\]

Equivalently,

\[
\beta=\frac tq_S,
\qquad
\alpha=\frac{t^2}{\Lambda q_S}+\min\left(\frac tq_S,0\right).
\]

The map

\[
\operatorname{Unfold}_S(U,T_1,T_2)
=
\bigl(q_SU,\ q_S(T_1-T_2)\bigr)
=(u,t)
\]

is facewise isometric on the two sectors adjacent to `S` and sends `(P-E)` exactly to

\[
\boxed{t^2=\Lambda u.}
\]

This is the precise recovery statement:

> An Enterprise parabola is an ordinary parabola in the axis-relative two-face unfolding, then folded back into the three-positive-axis carrier presentation.

This is `EXACT_RECOVERY_AFTER_AXIS_RELATIVE_UNFOLDING`, not proof that the classical signed plane is N0.

## 5. Exact discrete integer parabola

Let

\[
h,\kappa\in\mathbb N,
\qquad n\in\mathbb Z.
\]

Define local components

\[
U_n=\kappa n^2,
\]

\[
(T_{1,n},T_{2,n})=
\begin{cases}
(hn,0),&n\ge0,\\
(0,-hn),&n\le0.
\end{cases}
\]

Then

\[
T_{1,n}^2+T_{2,n}^2
=\frac{h^2}{\kappa}U_n.
\]

The exact native displacement is obtained by carrier-to-native decoding:

\[
D_E(V\to P_n)
=
\operatorname{Decode}_E
\left(
\kappa n^2 S+h n_+R+h n_-R_2
\right),
\]

where

\[
n_+=\max(n,0),\qquad n_-=\max(-n,0),
\]

and `Decode_E` means the unique nonnegative `min=0` decode of a carrier displacement. It is not a native common-diagonal equivalence declaration.

The physical aperture is

\[
\boxed{
\Lambda=q_S\frac{h^2}{\kappa}.
}
\]

Thus every integer direction has infinitely many exact integer-addressed parabola points; no numerical fitting is required.

In physical finite-difference variables, if transverse speed is `v=q_Sh` and axial second difference is `a=2q_S kappa`, then

\[
\boxed{
\Lambda=\frac{2v^2}{a}.
}
\]

This is independent of the scale chosen to encode the direction.

## 6. Arithmetic visibility: the frame index is Delta_S

The determinant computation in Section 1 also gives

\[
\boxed{
[\Lambda_{\mathrm{carrier}}:\mathbb ZS+\mathbb ZR]=\Delta_S.
}
\]

For primitive `S`, the Smith normal form is

\[
\operatorname{SNF}(S,R)=\operatorname{diag}(1,\Delta_S).
\]

Therefore:

- the rotated frame is geometrically valid for every nonzero direction;
- it is a full lattice basis only when `Delta_S=1`;
- otherwise the integral local frame occupies an index-`Delta_S` sublattice, and arbitrary global lattice points have local coordinates with denominators dividing `Delta_S`.

### Unimodular classification

For canonical nonzero integer directions,

\[
\Delta_S=1
\]

holds exactly for the six directions

\[
(1,0,0),\ (0,1,0),\ (0,0,1),
\]

\[
(0,1,1),\ (1,0,1),\ (1,1,0).
\]

Hence the previously obtained six clean direction formulas are precisely the six unimodular frames. Every genuinely new arbitrary direction necessarily carries an arithmetic sampling index greater than one.

Example:

\[
S=(3,4,0),\qquad q_S=5,\qquad \Delta_S=13.
\]

For `h=kappa=1`, the first exact local points are

\[
(U,T_1,T_2)=(1,1,0),(4,2,0),(9,3,0),\ldots
\]

and

\[
(U,T_1,T_2)=(1,0,1),(4,0,2),(9,0,3),\ldots
\]

while their global canonical addresses begin

\[
(0,4,1),(4,14,0),(15,33,0),\ldots
\]

and

\[
(4,1,0),(14,10,0),(30,27,0),\ldots
\]

The apparent sparsity/sector changes in the global address display are arithmetic frame effects, not deviations from the parabola equation.

## 7. C3 covariance and reversal aperture chirality

Simultaneous cyclic rotation gives

\[
\operatorname{Coord}_{\rho S}(\rho X)
=
\operatorname{Coord}_S(X),
\]

and preserves `q_S`, `Delta_S`, and `(P-E)` exactly.

For reversal, let

\[
\iota S=(M-a,M-b,M-c),
\qquad M=\max(a,b,c).
\]

Then `iota` is an involution, commutes with `rho`, and the six directions form

\[
C_3\times C_2\cong C_6.
\]

However, the oriented native length generally changes:

\[
q_{\iota S}^2-q_S^2
=M\bigl(3M-2(a+b+c)\bigr).
\]

Carrier inversion sends a parabola with fixed frame-relative `lambda` to the reverse parabola with the same `lambda`. For fixed physical aperture `Lambda`, the reverse image has

\[
\boxed{
\Lambda_{\mathrm{rev}}
=
\chi_S\Lambda,
\qquad
\chi_S=\frac{q_{\iota S}}{q_S}.
}
\]

Thus one cannot demand both:

- invariance under rescaling the axis representative; and
- reversal invariance of the same physical aperture,

unless the chosen direction is reversal-length symmetric.

The equality `chi_S=1` holds exactly when

\[
2(a+b+c)=3M.
\]

For a canonical direction with active coordinates `x>=y>=0`, this is

\[
x=2y.
\]

Examples:

- `S=(1,0,0)`: `chi=sqrt(2)`;
- `S=(3,4,0)`: `chi=sqrt(17)/5`;
- `S=(2,1,0)`: `chi=1`.

This is a candidate **parabolic aperture chirality invariant** induced by the already frozen reversal asymmetry of the directed native gauge.

## 8. Focus/directrix recovery: one abstract line, folded right-angle directrix

Let

\[
f=\frac{\Lambda}{4}.
\]

In the unfolded `(u,t)` frame, the parabola has focus

\[
F=(f,0)
\]

and directrix

\[
u=-f.
\]

The equality

\[
(u-f)^2+t^2=(u+f)^2
\]

is equivalent to

\[
t^2=4fu=\Lambda u.
\]

### Folded realization

The focus folds to

\[
F_E=V+f\widehat S.
\]

The abstract directrix vertex `-f widehat S` has the carrier-positive realization

\[
D_0=V+f\widehat R+f\widehat R_2.
\]

The directrix folds into two positive native arms:

\[
\mathcal D_1
=
\{D_0+s\widehat R:s\ge0\},
\]

\[
\mathcal D_2
=
\{D_0+s\widehat R_2:s\ge0\}.
\]

For the `t>=0` wing, the matching directrix point is

\[
Q(t)=D_0+t\widehat R;
\]

for the `t<=0` wing it is

\[
Q(t)=D_0+(-t)\widehat R_2.
\]

In the corresponding trace-group-completed right-sector chart,

\[
\|P(t)-F_E\|^2=(u-f)^2+t^2,
\]

while

\[
\|P(t)-Q(t)\|^2=(u+f)^2.
\]

Therefore `(P-E)` is exactly the focus/directrix locus in that frame completion.

Interpretation:

> The two wings share one abstract straight directrix in the unfolded frame. Its native carrier realization is a two-arm right-angle directrix in the sector opposite the opening axis.

No global native negative axis is introduced. The signed coefficient is carried by a groupoid inverse inside the selected frame completion, which remains distinct from a canonical positive reverse trace.

## 9. Why the frozen directed gauge does not give the same parabola

The current directed gauge canonically redecodes a negative component into other positive axes. It is therefore not the signed face-completion norm used in Section 8.

An exact counterexample already appears in the unit frame.

Take

\[
S=(1,0,0),\qquad R=(0,1,0),\qquad \Lambda=4,\qquad f=1.
\]

The point

\[
P=\frac14S+R
\]

lies on the shape parabola because

\[
1^2=4\cdot\frac14.
\]

For the focus `F=S`, the forward displacement `F->P` decodes to

\[
(0,7/4,3/4),
\]

so

\[
\ell_E(F\to P)^2=\frac{29}{8}.
\]

The reverse displacement `P->F` decodes to

\[
(7/4,0,1),
\]

so

\[
\ell_E(P\to F)^2=\frac{65}{16}.
\]

The matching directrix distance in the completed face is

\[
(u+f)^2=\left(\frac54\right)^2=\frac{25}{16}.
\]

Neither directed orientation agrees.

Classification:

- shape parabola vs current directed-gauge focus/directrix conic: `NONRECOVERY` globally;
- shape parabola vs frame-group-completed focus/directrix construction: `EXACT_RECOVERY`;
- the two objects must not be conflated.

## 10. Universal fold seam and carrier corner

In the unfolded frame, the parameterized parabola is smooth and has constant axial second difference.

The fold map is

\[
\operatorname{Fold}_S(u,t)
=
 u\widehat S+
\begin{cases}
 t\widehat R,&t\ge0,\\
 (-t)\widehat R_2,&t\le0.
\end{cases}
\]

Its one-sided transverse derivatives at the vertex are

\[
\partial_t^+=\widehat R,
\qquad
\partial_t^-=-\widehat R_2.
\]

Their carrier difference is

\[
\partial_t^+-\partial_t^-
=\widehat R+\widehat R_2
\equiv-\widehat S.
\]

For the exact discrete sequence with transverse step `h` and axial coefficient `kappa`, the unfolded second difference is

\[
\Delta^2P_n=2\kappa S
\]

for every `n`.

In the folded carrier presentation,

\[
\Delta^2_{\mathrm{carrier}}P_n=2\kappa S
\qquad(n\ne0),
\]

but at the vertex

\[
\boxed{
\Delta^2_{\mathrm{carrier}}P_0=(2\kappa-h)S.
}
\]

The seam defect is

\[
-hS.
\]

This is a gluing/fold cocycle, not a failure of the native quadratic law. It is handled by the existing `T9_HOLONOMY_COCOYCLE_GLUING` method family; no new general tool is claimed.

Carrier-visible consequence:

- the two outward tangent rays are `R` and `R_2`, separated by carrier `120°`;
- a traversal through the vertex turns by carrier `60°`;
- after axis-relative unfolding, the tangent is continuous.

Thus the apparent cusp is a presentation signature of the fold.

## 11. Scale-corrected mother cone

Introduce a physical slice parameter `D`. The arbitrary-direction homogeneous conic carrier is

\[
\boxed{
q_S(T_1^2+T_2^2)=UD.
}
\tag{Q-E}
\]

In physical unfolded coordinates

\[
u=q_SU,
\qquad
t=q_S(T_1-T_2),
\]

this becomes

\[
t^2=uD.
\]

Important slices:

- `D=Lambda`: parabola `t^2=Lambda u`;
- `u+D=2R`: circle slice `(u-R)^2+t^2=R^2`;
- `D-u=2A`: hyperbola slice `(u+A)^2-t^2=A^2`.

The extra factor `q_S` is required when `U,T_1,T_2` are coefficients in an arbitrary segment frame. The uncorrected `T^2=UD` remains valid only after choosing a unit-normalized frame.

## 12. Exact checker

Checker:

`experiments/enterprise_parabola_arbitrary_frame_checker.py`

Local checker file SHA-256:

`1bcb59b23eb62d104006581ed40efb7eae585e6e56df7087393005ace0af12ca`

Exact run at component bound `12`:

- canonical nonzero directions: `468`;
- primitive directions: `276`;
- direction-point frame inversion / canonicalization / C3 / scale checks: `219,492`;
- determinant/index checks: `468`;
- six-element C6 orbit checks: `468`;
- exact discrete parabola states: `144,900`;
- discrete state digest: `3acbd9be2825d051cc866dfc557bd5e95daed4c4f64e78364c640bab5bed27d4`;
- fold-seam checks: `6,900`;
- seam digest: `b2307e5e1b5392bbecbe22c1e193b3e039986121dd3e42a7b4f65c3fb5b28d0d`;
- mismatch count: `0`.

Finite enumeration supports the algebraic proofs but is not used as a substitute for them.

## 13. Result classification

### Candidate theorem package that survived

1. arbitrary-direction coefficient inversion;
2. scale-corrected parabola `(P-E)`;
3. compact global formula `(P-global)`;
4. exact signed parameterization and two-face unfolding;
5. exact infinite integer sample family;
6. frame-lattice index `Delta_S`;
7. six directions are exactly the unimodular frames;
8. C3 covariance;
9. reversal aperture factor `chi_S`;
10. exact focus/directrix recovery in trace-group completion;
11. folded two-arm directrix;
12. universal vertex fold cocycle;
13. scale-corrected mother cone `(Q-E)`.

### Claims explicitly not made

- no promotion of the continuum unfolding to N0;
- no claim that the current directed gauge is a symmetric metric;
- no claim that the directed-gauge focus/directrix conic equals the shape parabola;
- no claim that carrier Euclidean smoothness is native smoothness;
- no claim of canonical-foundation status before independent review.

## 14. Next discriminating work

The highest-value successor is not another plot. It is an independent theorem audit with three kill tests:

1. verify that the user-frozen arbitrary-segment `120°` orthogonality is consistent under composition of translated frames, not only at one base point;
2. determine whether the trace-group-completed local norm has a choice-independent gluing certificate, or must remain an axis-relative tool;
3. classify all lattice points on `(P-global)`, including fractional local-coordinate cosets of the index-`Delta_S` frame, rather than only the guaranteed integer-local subfamily.

Until those tests pass, the correct status is:

`EXACT_ALGEBRAIC_CANDIDATE / FRAME_RELATIVE_GEOMETRIC_RECOVERY / NOT_YET_CANONICAL`.
