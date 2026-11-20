# C85 — the midpoint is worse throughout the first overlap interval

## Statement and scope

Use C84's endpoint-normalized Haar readout function
\(F_\theta(a)\), with marks
\((u,(1-\theta)u+\theta v,v)\), three independent uniform source phases,
and a Haar lattice of covolume \(a\). These are auxiliary joint readout
coordinates for the original integer arrangement model; no lattice point
independence is assumed.

**Theorem.** For every \(a\geq 1/2\),

\[
\boxed{F_{1/4}(a)-F_{1/2}(a)
\geq \frac{7/270-QK(a)}{\zeta(2)a}>0,}
\tag{1}
\]

where, on \(1/2\leq a\leq1\),

\[
Q=\frac{3\log3-2}{4},\qquad
K(a)=\int_0^1\frac{(2r-r^2-a)_+^3}{r^2}\,dr,
\tag{2}
\]

and \(K(a)=0\) for \(a\geq1\). In particular,

\[
K(1/2)=-\frac{9\sqrt2}{10}-\frac12
-\frac32\log(1-1/\sqrt2),
\qquad QK(1/2)<0.022395<\frac7{270}.
\tag{3}
\]

The previous exact comparison covered \(a\geq1\). Equation (1) covers the
entire additional interval \([1/2,1)\), where two or three collision
directions may occur. It does not settle the full-source Mellin inequality,
because that also contains \(0<a<1/2\).

A stronger position-range statement follows from the same proof:

\[
\boxed{F_\theta(a)>F_{1/2}(a)
\quad\text{if }a\geq1/2,
\quad\theta\in[1/5,4/5]\setminus\{1/2\}.}
\tag{4}
\]

Thus throughout this area range, the midpoint has a smaller uniqueness
probability than every other fixed reading position in that central interval.

## 1. The finite-direction formula for general position

For two endpoint vectors \(v,w\), set

\[
E_2(v,w)=\prod_{j=1}^{2}
\bigl(1-\operatorname{range}\{0,v_j,w_j\}\bigr)_+,
\qquad
E_3(v,w)=\prod_{j=1}^{2}(1-|v_j|-|w_j|)_+.
\]

Write \(\ell_\theta(v)=(1-\theta)v_1+\theta v_2\), and define

\[
W_{2,\theta}=E_2
\bigl[1-\operatorname{range}\{0,\ell_\theta(v),\ell_\theta(w)\}\bigr],
\qquad
W_{3,\theta}=E_3[1-|\ell_\theta(v)|-|\ell_\theta(w)|].
\tag{5}
\]

The bracketed terms are nonnegative wherever the corresponding endpoint
weight is positive: the range of a convex combination is at most the
convex combination of the two endpoint ranges. Hence no further positive
part is needed in (5). Let

\[
J_{i,\theta}(a)=\int_{\mathbb R^4}
\delta(\det(v,w)-a)W_{i,\theta}(v,w)\,dv\,dw.
\]

C83's finite-direction proof transfers to these marks without change in its
counting: when \(a>1/2\), any two nonparallel collision directions are a
unimodular pair; at most three unoriented directions occur; if three occur,
their actual hitting representatives make a parallelogram based at zero.
These facts use only that the endpoint coordinates lie in a unit rectangle.
The primitive first moment is C84's \(7A(\theta)/(8\zeta(2)a)\). Therefore

\[
\boxed{F_\theta(a)=1-\frac{7A(\theta)}{8\zeta(2)a}
+\frac{J_{2,\theta}(a)-J_{3,\theta}(a)}{\zeta(2)a},\quad a>1/2.}
\tag{6}
\]

At \(a=1/2\), any newly admitted determinant-two configuration would
require a maximal-area triangle in the closed endpoint square; this is a
zero phase-volume boundary. Equivalently use continuity in \(a\). Thus all
subsequent bounds hold at the closed endpoint too.

## 2. Reducing the position gap to one primitive vector

Both \(J_{2,\theta}\) and \(J_{3,\theta}\) are concave functions of \(\theta\):
their endpoint factors do not depend on \(\theta\), and their bracketed
factors are concave by convexity of range or absolute value. Both are also
symmetric under \(\theta\leftrightarrow1-\theta\). Swapping the endpoint
coordinates reverses determinant; for fixed \(v\), the change
\(w\mapsto v-w\) preserves \(E_2\) and the three-point range while reversing
determinant, and \(w\mapsto-w\) does the same for \(E_3\). These changes
justify the symmetry with the positive determinant convention.

Consequently
\(\Delta J_i=J_{i,1/2}-J_{i,\theta}\geq0\), and (6) gives

\[
F_\theta-F_{1/2}
\geq\frac{(7/8)[A(1/2)-A(\theta)]-\Delta J_2}{\zeta(2)a}.
\tag{7}
\]

For any three real numbers \(0,x,y\),

\[
\operatorname{range}\{0,x,y\}
=\frac{|x|+|y|+|x-y|}{2}.
\tag{8}
\]

The three edge terms in the integral have the same value. For example,
the unimodular substitutions \((v,w)\mapsto(-w,v-w)\) and
\((v,w)\mapsto(w-v,-v)\) preserve determinant and preserve endpoint
triangle widths by translating the three vertices. Thus

\[
\Delta J_2
=\frac32\int\delta(\det(v,w)-a)E_2(v,w)g_\theta(v)\,dv\,dw,
\tag{9}
\]

where endpoint symmetry permits the even position gap

\[
g_\theta(v)=\frac{|\ell_\theta(v)|+|\ell_{1-\theta}(v)|}{2}
-|\ell_{1/2}(v)|\geq0.
\]

Take \(0<\theta\leq1/2\). The gap vanishes if \(v_1v_2\geq0\). For
\(v=(r,-s)\), \(0<s\leq r\), direct piecewise evaluation yields

\[
g_\theta(r,-s)=\bigl[(1-\theta)s-\theta r\bigr]_+.
\tag{10}
\]

Sign reversal and endpoint exchange therefore reduce (9) to

\[
\Delta J_2=6\int_0^1\int_{\theta r/(1-\theta)}^r
[(1-\theta)s-\theta r]I_2(a,r,s)\,ds\,dr,
\tag{11}
\]

where
\(I_2=\int\delta(ry+sx-a)E_2((r,-s),(x,y))\,dx\,dy\).

## 3. A simple convolution upper bound

The nonzero support of \(E_2\) has \(x<1\) and \(y<1-s\).
Set \(X=1-x\), \(Y=1-s-y\). Then \(X,Y\geq0\),

\[
ry+sx-a=T-sX-rY,\qquad T=r+s-rs-a.
\]

Each one-coordinate phase overlap is at most the corresponding distance
to that upper endpoint, so \(E_2\leq XY\). Extending its support to the
whole positive quadrant gives the exact elementary bound

\[
0\leq I_2(a,r,s)
\leq\int_{X,Y\geq0}\delta(sX+rY-T)XY\,dX\,dY
=\frac{T_+^3}{6r^2s^2}.
\tag{12}
\]

Substitute \(s=qr\) in (11). Since \(q\leq1\),

\[
r+s-rs-a=r(1+q)-r^2q-a\leq2r-r^2-a.
\]

It follows that

\[
\boxed{\Delta J_2\leq Q_\theta K(a),\qquad
Q_\theta=(1-\theta)\log\frac{1-\theta}{\theta}-1+2\theta.}
\tag{13}
\]

At \(\theta=1/4\), \(Q_\theta=Q\) and
\((7/8)(A(1/2)-A(1/4))=7/270\). Equations (7) and (13) prove (1).
The integrand defining \(K(a)\) decreases with \(a\), so (3) proves its
strict positivity throughout the claimed area range.

## 4. Closed form and exact arithmetic for the comparison constant

For \(b=\sqrt{1-a}\), \(1/2\leq a\leq1\), direct integration gives

\[
K(a)=-b^6-\frac{16}{5}b^5+\frac92b^4+10b^3-3b^2-6b
-6(1-b^2)^2\log(1-b).
\tag{14}
\]

The integral formula (2) is preferable for numerical evaluation near
\(a=1\), where (14) has cancellation. A positive series follows instead
from \(r=1-u\):

\[
\boxed{K(a)=48\sum_{n=0}^{\infty}
\frac{b^{n+7}}{(n+3)(n+5)(n+7)}.}
\tag{15}
\]

Indeed expand \((1-u)^{-2}\) and integrate
\((b^2-u^2)^3\); every term is nonnegative. Consecutive series terms have
ratio smaller than \(b\), so a partial sum has an explicit geometric
remainder. The accompanying Fraction program bounds \(b=1/\sqrt2\) between
rational numbers, evaluates 96 terms, and bounds the tail using this ratio.
It treats \(\log3\) and \(\log4\) by their positive atanh series with a
rational remainder. The resulting intervals and strict rational tests are
in `half_area_certificate.json`; no floating value enters a sign proof.

## 5. The central three-fifths of possible positions

Let \(e=1/2-\theta\), \(1/5\leq\theta<1/2\). From C84's rational formula,

\[
\frac{A(1/2)-A(\theta)}{e^2}
=\frac{2(3-4\theta)}{15(1-\theta)^2}
\geq\frac{11}{24}.
\tag{16}
\]

The displayed ratio increases with \(\theta\), as its derivative is
\(4(2\theta-1)/[15(\theta-1)^3]>0\).
Writing \(z=2e\),

\[
Q_\theta=(1+z)\operatorname{atanh}z-z.
\]

Its power series divided by \(z^2\) has nonnegative coefficients, so
\(Q_\theta/e^2\) increases with \(e\). Therefore

\[
\frac{Q_\theta}{e^2}
\leq\frac{100}{9}\left(\frac45\log4-\frac35\right).
\tag{17}
\]

Combining (7), (13), (16), and (17),

\[
F_\theta(a)-F_{1/2}(a)
\geq\frac{e^2}{\zeta(2)a}
\left[\frac{77}{192}
-\frac{100K(1/2)}9\left(\frac45\log4-\frac35\right)\right].
\tag{18}
\]

The bracket is strictly positive by the same exact rational certificate.
Symmetry proves (4).

## 6. Relation to the outstanding full-source problem

This theorem establishes a signed contribution on \([1/2,\infty)\) to
\(I_{1/4}-I_{1/2}\). In particular,

\[
I_{1/4}-I_{1/2}
\leq\frac1{20}\int_0^{1/2}(F_{1/2}-F_{1/4})a^{-19/20}\,da
-\frac7{855\pi^2}
-\frac1{20\zeta(2)}\int_{1/2}^1
[7/270-QK(a)]a^{-39/20}\,da.
\tag{19}
\]

The first integral remains the unproved term. Paired sampling suggests it
is already negative, but that observation is kept separate from this proof.
The exact comparison above uses neither those samples nor a pointwise
Jensen inequality for the phase-dependent critical scale.

There is a convenient explicit lower bound for the entire signed
high-area contribution. For \(1/2\leq a\leq1\) and \(0\leq h\leq1\),

\[
(h-a)_+\leq2(1-a)(h-1/2)_+.
\]

Consequently \(K(a)\leq8(1-a)^3K(1/2)\). Put
\(d=7/270\), \(C=QK(1/2)\), \(z=2^{-1/20}\), and

\[
P=\int_{1/2}^1(1-a)^3a^{-39/20}da
=-\frac{20}{19}-60+\frac{20}{7}-\frac{20}{41}
+\left(\frac{40}{19}+60-\frac{10}{7}+\frac5{41}\right)z.
\]

Integrating (1) on \([1/2,1]\) and the exact C84 formula on
\([1,\infty)\) gives

\[
\boxed{\frac1{20}\int_{1/2}^\infty
(F_{1/4}-F_{1/2})a^{-19/20}da
\geq G:=\frac1{\zeta(2)}\left(\frac{2dz}{19}-\frac{2CP}{5}\right)
>\frac{1361}{10^6}.}
\tag{20}
\]

The exact certificate encloses \(G\) between
\(0.001361166259206372\) and \(0.001361166259206373\), with both endpoints
rounded outwards. For \(\zeta(2)\) it uses Machin's identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\) and alternating-series remainders.
That identity follows by the tangent addition formula with the angles
in their specified first-quadrant ranges. The rational interval for
\(z\) is verified by raising both endpoints to the twentieth power.

Thus a sufficient remaining condition for the whole-source comparison is

\[
\boxed{\frac1{20}\int_0^{1/2}(F_{1/2}-F_{1/4})a^{-19/20}da
<\frac{1361}{10^6}.}
\tag{21}
\]

The low-area sign change already proved in C84, together with (1) and
continuity, also confines at least one intersection of the two universal
curves to \((0,1/2)\); there are no intersections at larger area.

For the original stock model, take a fixed regular source region \(K\)
of positive area with \(J_{\min}>0\). Whenever \(L^2J_{\min}\geq1/2\),
C84's whole-competitor inventory limit and (1) imply

\[
\Phi_{1/4,K}(L)-\Phi_{1/2,K}(L)
\geq\frac{2(d-C)}{\zeta(2)L^2}\int_K J(X)^{-1}\,dX>0.
\tag{22}
\]

The normalization is still the full number of arrangements. The analogous
bound for \(\theta\in[1/5,4/5]\) follows from (18).

### Pinned dependencies

- C83 `HAAR_FINITE_INTERVAL.md`, enterprise-math commit
  `20c3c2a6cb769a816cedf0ec04cf199149bfa86f`: finite direction geometry and
  positive unimodular-basis unfolding.
- C84 `READING_POSITION.md`, commit
  `01f50954ee37548372464c68a311f7df2dba0632`: endpoint marks, first moment,
  exact \(A(\theta)\), continuity, and original-inventory bridge.

The new contribution is the edge-range reduction, the convolution bound,
the strict half-area comparison, and its uniform position-range corollary.
