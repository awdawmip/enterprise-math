# C86 independent review: doubled-face integral and the QT support threshold

## Outcome and scope

**PASS, with one corrected display typo and no remaining substantive finding.**

The review covers the new geometric normalization, the complete angular
integration, the directed midpoint error bound, the QT capacity proof and its
sharp witness, and the binding of the final saved kappa certificate to its
seven generators. It does not claim a second execution of the entire outer
kappa mesh, and it is an internal project review rather than external peer
review.

Reviewed sources:

- `../triangle/CHORDAL_CORRECTION.md`
- `../triangle/DOUBLED_FACE_INTEGRAL.md`
- `../triangle/QT_SUPPORT.md`
- `../triangle/doubled_face_integral.py`
- `../triangle/certify_doubled_face.py`
- `../triangle/doubled_face_certificate.json`

The original H(0,1) problem and all integer relations remain unchanged. This
review applies to the auxiliary Haar/Palm model under C85's existing bridge
and its established scope.

## 1. Basis multiplicity and Palm normalization

For A<4, at most one direction has both actual signs. On a face containing
that direction, the actual four-vector set is exactly one of

\[
\{-v,v,w,v+w\},\qquad \{-v,v,w,-v-w\}.
\]

For the first pattern, the two possible rooted descriptions are related by
\((v,w)\mapsto(-v,v+w)\); their determinants have opposite signs. Thus exactly
one has positive determinant. For the second pattern, the central triangle
chooses the sign of the doubled vector, while positive determinant chooses
which of its other two vectors is w. Again the count is exactly one.

Consequently QP and QT have coefficient 1, with neither an additional factor
1/2 nor an additional factor 1/3. Positive-unimodular-basis unfolding therefore
has the established coefficient 1/zeta(2). Integration over the source x is
already part of the Palm quantity; it introduces no further division by A.

For QP, cyclic affine symmetries of the triangle give three equivalent
sectors. A reflected triangle symmetry reverses determinant. Combining it
with \((v,w)\mapsto(-v,v+w)\) reverses determinant a second time and preserves
the actual offset set, giving the other three sectors. The sectors have
disjoint interiors and exhaust the direction circle.

On the chosen sector, v=u(1,-t), w=(z,1/u-tz), one has

\[
dv=u\,du\,dt,\qquad dw\,\delta(\det(v,w)-1)=dz/u.
\]

Thus the basis measure is exactly du dt dz. The factor six from sectors
cancels the factor 1/6 from the cubic convolution formula, leaving the stated
coefficient 1/zeta(2) in the final one-dimensional u integral.

## 2. Source geometry and exact angular integral

The constraints x±v in rT are exactly

\[
x=(u,ut)+(X,Y),\quad X,Y\ge0,\quad X+Y\le r-2u.
\]

The constraints y=x+w and y+v in rT similarly give
y=(0,ut)+Z with Z in (r-u)T. The determinant condition is

\[
L_t(Z)-L_t(X,Y)=1/u+ut.
\]

Since \(tu(r-2u)\le r^2/8<1\), the second chord is wholly on its descending
branch throughout A<4. This verifies the domain of the convolution formula;
no unaccounted angular branch remains.

For an independent exact check of the angular integral, put

\[
f_1=\frac{(H-ut)^3}{t(1-t)},\quad
f_2=\frac{(H-Mt)^3}{t(1-t)^2},\quad
f_3=\frac{(N-ut)^3}{(1-t)^2}.
\]

The following primitives were derived independently and differentiated by
exact symbolic arithmetic:

\[
\begin{aligned}
P_1={}&H^3\log t-(H-u)^3\log(1-t)
       +u^3t^2/2+(u^3-3Hu^2)t,\\
P_2={}&H^3\log t+(H-M)^3/(1-t)
       -(H-M)^2(H+2M)\log(1-t)-M^3t,\\
P_3={}&(3Nu^2-2u^3)t-u^3t^2/2
       -3u(u-N)^2\log(1-t)-(u-N)^3/(1-t).
\end{aligned}
\]

The two H^3 log(epsilon) terms cancel exactly. Substituting H=M-1/u into
the evaluated first two primitives gives precisely the first four terms of
S_r(u). Substituting N=u-1/u and t=1-u^(-2) into the third gives

\[
u^3/2-3u+3/(2u)+u^{-3}+(6/u)\log u.
\]

The original displayed formula omitted the plus sign immediately before the
last logarithmic term; the executable already had the correct addition.
The author corrected the display during review.

The integration domain u_-<u<r/2, the split at u=1, and the condition A>2
follow directly from H>0 and r-2u>0. All logarithm arguments are positive on
the stated A<4 domain.

## 3. Directed interval integration

The D2 product, inverse and logarithm rules correctly enclose the first two
derivatives. The compact source constraint r-2u>=0 and the lower bound

\[
L=2u+1/u-r\ge2\sqrt2-r>0
\]

justify the code's refinement of the value interval for L. Retaining the
previous derivative intervals after this refinement remains safe: each still
contains the actual derivative, and the refined value interval contains the
actual value.

For an exact cell [a,b], the midpoint remainder is bounded by
(b-a)^3 sup|S''|/24. Each cell endpoint is an outward interval containing its
exact algebraic endpoint, the midpoint evaluation contains the exact midpoint
value, and the derivative interval is evaluated over the union enclosure of
the full cell. The separately enclosed cell width contains the exact width.
The implemented interval products and symmetric error addition therefore
enclose the exact cell integral even though the algebraic endpoints are not
stored as exact symbolic radicals.

Monotonicity of QP in A follows from its original positive inclusion integral.
Thus rounding its outer area endpoints down and up is valid. The code avoids
evaluating the singular limiting formula at A=4. The new subtraction of tau
is used only when the actual area's cell upper endpoint is strictly below
8/3, precisely where the QT-zero theorem applies.

## 4. QT capacity and the sharp threshold

For both signed sectors, m=2x-v is coordinatewise nonnegative and has total
coordinate sum at most two. Maximizing L_t(y) with y,z in T and y+z=m gives
the three cases in QT_SUPPORT.md: fill the vertical coordinate first, then
the horizontal coordinate. The constructed optimizer also leaves z in T;
there is no missing lower constraint from the second point.

Because L_t(v)=0, the two endpoint L-values sum to twice the source L-value.
Swapping y and z supplies the negative deviation, so the same calculation
bounds the absolute determinant.

The complete case split was checked by direct substitution:

| Direction sector | Case I | Case II | Case III |
|---|---:|---:|---:|
| v=u(1,-t) | ≤1/6 | ≤3/16 | ≤1/6 |
| v=-u(1,-t) | ≤1/8 | ≤1/8 | ≤1/8 |

The intermediate u bounds and the stated increasing/decreasing quadratic
ranges are correct. All fifteen final one-variable rational inequalities
were additionally certified by exact Bernstein coefficients on their full
rational t intervals; no floating-point test is used for these assertions.

The witness

\[
x=(1/2,1/4),\quad v=(1/2,-1/4),\quad w=(-1/4,1/2)
\]

has all four points in T and determinant 3/16. Rescaling to determinant one
therefore gives area 8/3. Enlarging the triangle and translating this fixed
configuration into its interior gives an open set of positive Haar/Palm
measure for every A>8/3. Hence the capacity bound proves the genuine support
threshold, not merely a necessary estimate:

\[
Q_T(A)=0\quad(A<8/3),\qquad Q_T(A)>0\quad(A>8/3).
\]

## 5. Recorded checks and final constant

`audit_doubled_face.py` completed successfully and wrote
`doubled_face_review_checks.json`. In addition to the exact algebra above, it
verified the final certificate's four-part rational sum and all seven source
SHA-256 bindings. The saved interval is

\[
\frac{8879797996758579248357681281004993}{2^{112}}
\le\kappa_3\le
\frac{9325116056440067185142329372765413}{2^{112}},
\]

whose displayed approximations are
[1.71018688620671388655486, 1.79595202479841387041990]. In particular, the safely
widened strict assertion is

\[
\boxed{1.7101<\kappa_3<1.796.}
\]

This review establishes the new normalization and analytic inputs to that
certificate. The complete outer mesh was executed by its author, not rerun
as part of this independent review; that distinction is recorded in the
machine-readable review result.
