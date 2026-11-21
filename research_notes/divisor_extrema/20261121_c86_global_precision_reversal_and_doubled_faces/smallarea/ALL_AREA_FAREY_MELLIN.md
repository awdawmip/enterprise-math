# C86: an exact all-area Farey formula and a two-variable Mellin comparison

## 0. Object and result

Use C84–C85's endpoint-normalized Haar function F_theta(a): a covolume-a lattice,
marks (u,(1-theta)u+theta*v,v), and three independent uniform source phases.
All lattice relations are retained. This is the established auxiliary readout
model for the original H(0,1) integer arrangements, under the same X6 typing and
the previously proved inventory-limit bridge.

This note gives an exact all-a formula, eliminates all source phases, and then
integrates the scale a analytically. The remaining difference I_theta-I_mid is
a two-dimensional integral of a finite sum of algebraic powers. In particular,
the C85 small-area obstruction no longer requires a six-variable lattice/phase
integration.

Write zeta=zeta(2), gamma=1/20 and p=gamma+2=41/20. For the quarter point,

\[
\boxed{I_{1/4}-I_{1/2}
=-\frac1{2\zeta(1-\gamma)(1+\gamma)(2+\gamma)}
\int_0^1\int_{1/3}^1
 r^\gamma\frac{3x-1}{x^2}H(r,x)\,dx\,dr.}\tag{1}
\]

The function H is specified completely below and in `mellin_chambers.json`.
It is a sum of at most 28 terms on each of ten rational chambers:

\[
H(r,x)=\sum_j c_j|a_j+b_jx+d_jrx|^{41/20}.\tag{2}
\]

All c_j,a_j,b_j,d_j are rational. Chamber changes occur when r or rx crosses
1/3,1/2,2/3. No random samples enter (1) or (2). The independent integer cubature
certificate described in Section 7 now proves I_(1/4)<I_(1/2). The numerical
value from an uncertified order-16 Gaussian computation is approximately
-0.00174292875; that observation is separate from the proof.

## 1. Connected Farey direction graph

Fix a lattice and source phases away from boundaries. The collision window P
is an open bounded convex set containing 0. If a nonprimitive vector hits P,
the corresponding same-sign primitive vector also hits P. Let S be the finite
set of hitting primitive vectors. Graph vertices are their unoriented
directions {v,-v}. Two vertices are joined when |det(v,w)|=a.

This graph is connected when nonempty. In lattice coordinates, sort the actual
signed rays around the full circle. Two successive rays with angle less than
pi have determinant 1: otherwise normalize the first primitive vector to
(1,0), and shear the second to (k,n), where n>=2 and 0<k<n. The primitive point
(1,1) lies in conv{0,(1,0),(k,n)} and strictly between those rays, contradicting
successiveness and convexity. Delete the at most one gap of angle at least pi;
the resulting chain is connected. The rank-one exception has one unoriented
vertex and is connected directly. Identifying opposite signed rays preserves
connectivity.

The graph is noncrossing on the projective circle. Normalize any edge to the
coordinate axes. An edge crossing it would have representatives (b,c),(d,e)
with c,e>0,b>0,d<0. Its determinant b*e+c*|d| is at least 2, a contradiction.

### Every bounded face is triangular

Here is an elementary finite proof, avoiding a global tessellation assumption.
For the finite vertex set choose a large integer N, and apply the unimodular
matrix with rows (1,N) and (N,N^2+1). All transformed denominators have absolute
value greater than 1; this is possible because the finitely many nonzero
integer polynomials N*m+(N^2+1)*n eventually avoid 0 and +/-1. Orient each
representative to have positive denominator.

Suppose a cycle of length at least four has no chord. Select its vertex (p,q)
with maximal denominator q. The two adjacent denominators are strictly smaller
than q: equal denominators >1 cannot form determinant 1. For a given sign,
pb-qa=+/-1 determines at most one neighboring denominator b in 1,...,q-1.
Hence the two distinct smaller neighbors have opposite determinant signs.
Their denominators add to q and their numerators add to p. They are therefore
Farey parents and have determinant 1 with each other, a chord. Contradiction.

In the noncrossing circular embedding, the boundary of any bounded face is a
convex polygon. A chordless face of length >=4 is impossible by this argument.
All bounded faces are triangular. Conversely every three-cycle is a face:
all graph vertices lie on the circle, so no other vertex is inside its triangle.
Let D,e,t be vertex, edge, and triangle-face
counts. Euler now gives, including the empty graph,

\[
\boxed{\mathbf1_{D=0}=1-D+e-t.}\tag{3}
\]

There is no restriction on a in (3).

## 2. Exact phase-integrated formula

Let h_v be the hit indicator of the actual vector v and

\[
D_v=h_v+h_{-v}-h_vh_{-v}.
\]

Every unoriented edge has four positive ordered basis representations. Every
Farey triangle has six positive ordered representations (v,w) with its third
direction v+w. Thus

\[
e=\frac14\sum_{\det(v,w)=a}D_vD_w,\qquad
t=\frac16\sum_{\det(v,w)=a}D_vD_wD_{v+w}.\tag{4}
\]

The sums here run over positive unimodular bases of the lattice. The familiar
unfolding intensity is 1/(zeta*a). The D term is exactly C84's primitive first
moment, 7*A(theta)/(8*zeta*a). Consequently, for every a>0,

\[
F_\theta(a)=1-\frac{7A(\theta)}{8\zeta a}
+\frac1{\zeta a}\left(\frac{E_\theta(a)}4-
\frac{T_\theta(a)}6\right),\tag{5}
\]

where E and T are the ordinary positive-determinant integrals of the phase
averages in (4). This is an exact finite-event formula, not a truncation of an
infinite inclusion-exclusion series.

To evaluate each phase average, expand D into its three displayed terms.
There are 9 edge configurations and 27 triangle configurations. Each selected
configuration is a finite coefficient-point set K containing 0, with points
from +/-e1,+/-e2 and, in the triangle case, +/-(e1+e2). Its coefficient is the
product of the signs in D. Replace K by its convex hull, which preserves every
projection width. Write

\[
W_K(t)=\max_{(m,n)\in K}(m+nt)-
\min_{(m,n)\in K}(m+nt).
\]

For basis vectors v,w, the endpoint-phase factor is

\[
E_K(v,w)=
(1-\operatorname{width}_x(K(v,w)))_+
(1-\operatorname{width}_y(K(v,w)))_+.
\]

The complete three-phase volume equals E_K times
1-width_{ell_theta}(K(v,w)). This last quantity is nonnegative on the endpoint
support, because theta is between 0 and 1. All three phases have therefore
been integrated exactly.

## 3. Polygon edge widths and the 15 kernels

For any convex polygon,

\[
\operatorname{width}_\ell(K)
=\frac12\sum_{\text{polygon edges }e}|\ell(e)|.\tag{6}
\]

Symmetrize theta with 1-theta, using endpoint exchange in the complete
configuration sum. Set

\[
g_\theta(v)=\frac{|\ell_\theta(v)|+|\ell_{1-\theta}(v)|}2
-|\ell_{1/2}(v)|.
\]

For each polygon edge write its integer coefficient vector as k times a
primitive vector. Complete that primitive vector to a positive unimodular
basis and change variables so that it becomes the first basis vector.
Then g(edge)=k*g(v). Translation of K does not change its widths. An integer
shear of the second basis vector preserves the determinant measure.

An additional reflection of the coefficient polygon is allowed only in the
full v,w integral: it reverses determinant, which is restored by exchanging
the two ambient endpoint coordinates; g is invariant under that exchange and
under v->-v. This reflection is not asserted as a fixed-(r,s) kernel identity.

`enumerate_width_kernels.py` performs these exact finite operations on all
9+27 configurations. The 142 resulting polygon-edge terms combine to 15
integer polygons K with rational coefficients c_K. The raw and combined
lists are both retained in `width_kernels.json`. The resulting all-area gap is

\[
F_\theta(a)-F_{1/2}(a)
=\frac1{\zeta a}
\int_{\mathbb R^2}g_\theta(v)
\left[B(v)-\int\delta(\det(v,w)-a)
\sum_Kc_KE_K(v,w)\,dw\right]dv,\tag{7}
\]

where

\[
B(v)=(1-|v_1|)_+(1-|v_2|)_+
-(1-2|v_1|)_+(1-2|v_2|)_+.
\]

Keeping this unsimplified B is essential. Its integral against homogeneous g
is (7/8) times the first endpoint-overlap integral, explaining C85's coefficient,
but the factor 7/8 does not hold pointwise.

## 4. Exact one-dimensional correlations and zero-shift cancellation

The function g vanishes when v1,v2 have the same sign. Write v=(r,-s), r,s>0.
On det(v,w)=a put w=(r*t,a/r-s*t); the delta measure is exactly dt. Hence

\[
E_K(v,w)=h_{K,r}(t)h_{K,s}(t-a/(rs)),\qquad
h_{K,r}(t)=(1-rW_K(t))_+.\tag{8}
\]

Let R_K,r,s(u)=integral h_K,r(t)h_K,s(t-u)dt, and K(a;r,s) be the signed
sum of these correlations at u=a/(rs).

For completeness the finite width identity is

\[
\boxed{\sum_K c_K(W_K)_*(dt)=\delta_1-\delta_2.}\tag{9}
\]

It is checked by exact piecewise-affine algebra, implemented in
`line_kernel.zero_shift_identity()`. Each nonflat affine width piece contributes
constant pushforward density 1/|slope|; each flat minimum contributes an atom
whose weight is the length of that piece. The sum of the continuous densities
is zero on each of (0,1),(1,3/2),(3/2,2),(2,3),(3,infinity); the only remaining
atoms have weights +1 at 1 and -1 at 2. These intervals contain every width
break value of all 15 polygons, so the verification is complete.

Applying (9) to (1-rz)_+(1-sz)_+ gives, for every r,s,

\[
\boxed{K(0;r,s)=(1-r)_+(1-s)_+-(1-2r)_+(1-2s)_+.}\tag{10}
\]

Thus the B term in (7) cancels pointwise at zero scale. No such ordering is
claimed at positive shift. Indeed K(1/4;1/2,1/2)=9/32 exceeds K(0;1/2,1/2)=1/4.

## 5. Integrating the whole scale variable

For a fixed polygon, write its compact linear spline as

\[
h_{K,r}(t)=\sum_i A_i(r)(t-t_i(r))_+,
\]

where A_i are the slope jumps. Symmetrize the correlation in r,s, which is
equivalent to replacing R(u) by [R(u)+R(-u)]/2. Four integrations by parts give

\[
\boxed{
\int_0^\infty\left[R(0)-\frac{R(u)+R(-u)}2\right]u^{\gamma-2}du
=\frac{\sum_{i,j}A_i(r)A_j(s)|t_i(r)-t_j(s)|^{\gamma+2}}
{2(1-\gamma)\gamma(1+\gamma)(2+\gamma)}.}\tag{11}
\]

Here 0<gamma<1. All boundary terms vanish: the even correlation difference is
O(u^2) at zero, its first three derivatives are bounded there, and its
derivatives vanish beyond a finite shift; its constant tail is multiplied by
u^(gamma-1). In distributional form R'''' is the convolution of the two slope
jump measures. At a positive shift the even fourth derivative supplies one
half of the sum over absolute knot differences, producing the factor 1/2.

Each individual left side is nonnegative. In fact

\[
2R(0)-R(u)-R(-u)
=\int[h_r(t+u)-h_r(t)][h_s(t+u)-h_s(t)]dt\ge0,
\]

because both h_r and h_s are decreasing functions of the same W_K. The signed
sum over c_K still needs a separate comparison.

Using (10), (11), a=rs*u and the two opposite-sign quadrants in (7), one obtains

\[
I_\theta-I_{1/2}
=-\frac1{\zeta(1-\gamma)(1+\gamma)(2+\gamma)}
\int_0^1\int_0^1
g_\theta(r,-s)(rs)^{\gamma-1}
\sum_Kc_K\sum_{i,j}A_i(r)A_j(s)|t_i(r)-t_j(s)|^p\,ds\,dr.
\tag{12}
\]

For any fixed interior theta, g is supported where r and s are comparable.
Rescaling t by r makes every spline uniformly supported and uniformly
Lipschitz. Each individual correlation energy is O(r^(-gamma)) on this cone.
After multiplication by the remaining factors and ds=r*dx, the absolute
integral is O(integral_0^1 r^gamma dr). Thus the finite sum and the integrations
can be exchanged; there is no unproved cancellation of divergent integrals.

## 6. Scaled knots and the finite two-variable formula

Define the scaled spline f_K,r(z)=h_K,r(z/r). Its knot positions z_i(r)=r*t_i(r)
are affine in r on each of the four intervals

\[
(0,1/3),\quad(1/3,1/2),\quad(1/2,2/3),\quad(2/3,1).
\]

Its slope jumps a_i=A_i/r are integers. The only width break levels are
1,3/2,2,3, so this list of parameter intervals is complete.

On r>=s put s=xr. The signed knot sum after rescaling is

\[
H(r,x)=\sum_Kc_K\sum_{i,j}a_i(r)a_j(xr)
|xz_i(r)-z_j(xr)|^p.\tag{13}
\]

Each argument is a_r+b_s*x+c_rs*r*x, with rational coefficients. Exact collection
of these terms gives `mellin_chambers.json`: 10 chambers, with 16–28 terms each.
The generating script retains every polygon's affine knots and jumps.

For 0<theta<=1/2,
g_theta(r,-xr)=r*((1-theta)*x-theta)_+. Equation (12) therefore becomes

\[
\boxed{I_\theta-I_{1/2}
=-\frac2{\zeta(1-\gamma)(1+\gamma)(2+\gamma)}
\int_0^1\int_0^1
r^\gamma\frac{((1-\theta)x-\theta)_+}{x^2}H(r,x)\,dx\,dr.}\tag{14}
\]

Substituting theta=1/4 proves (1). Values at chamber boundaries are obtained by
continuous limits of the splines; those boundaries also have zero area.

## 7. Certified strict quarter-versus-midpoint comparison

The companion `../certify_mellin_integral.py` applies exact integer interval
arithmetic and a weighted-centroid quadrature rule to (1). The singular factor
r^(1/20) is retained in the measure and its moments are integrated exactly.
The remaining H has bounded second derivatives because 41/20>2. The code
splits interior and chamber-crossing cells and adds rigorous second-derivative
error bounds; all twentieth roots are certified by integer-power comparisons.

The recorded 96 by 96 certificate uses 217801 integer root checks, 8867
interior cells and 349 chamber-crossing cells. With

\[
D=5192296858534827628530496329220096=2^{112},
\]

its complete weighted integral J in (1), including the error bound, satisfies

\[
\frac{47828603618162895693842731261707}{D}
\le J\le
\frac{73935364512703374265618536738084}{D}.
\]

In particular J is strictly positive. The converted moment difference obeys

\[
\boxed{-0.002116643<I_{1/4}-I_{1/2}<-0.001369250<0.}
\]

The exact tighter rational bounds and all cell error quantities are retained
in `../mellin_integral_certificate.json`; the decimals displayed here are
deliberately widened. This proves the whole Haar comparison, including all
positive areas. No extrapolation from the a>=1/2 comparison is used.

## Dependencies and evidence

The mathematical inputs are C84's endpoint marks and first moment, C85's
convex-window direction graph ingredients, and the previously established
positive-unimodular-basis unfolding. The new steps are all-area chordality,
the exact 9+27 sign expansion, polygon-edge reduction, zero-shift distribution
identity, and analytic radial Mellin integral.

The finite computation uses rational hulls, integer determinant changes of
basis, rational spline coefficients and complete lists of breakpoints. It is
not a floating empirical classification. The optional Gaussian evaluation in
`explore_mellin_kernel.py` is explicitly exploratory. The sign certificate for
the remaining two-variable integral is the independent companion result in
Section 7.

`verify_finite_reduction.py` independently checks the stored certificate without
importing any generating module. It verifies all 9+27 source configurations,
all 142 edge transformations by explicit integer affine witnesses, all 15
combined coefficients, the complete pushforward measure (9), all 60 scaled
spline parameter cells, and the ten collected chambers. For each spline band
it proves the affine identity and every support inequality at all vertices of
the rational band; linearity extends the checks to the entire band. No finite
sample is used as a substitute for an interval or chamber proof.
