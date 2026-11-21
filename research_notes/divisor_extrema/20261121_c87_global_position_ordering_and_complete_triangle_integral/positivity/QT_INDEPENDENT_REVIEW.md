# C87 independent review: the complete QT positive integral

## Outcome

**PASS.** No substantive issue remains in the new QT geometry, support
cutoff, normalization, or whole-cell enclosure. One display-only omission of
plus signs between the three summands of Equation (14) was reported and
corrected; the executable already performed the correct additions.

Reviewed sources are `../triangle/QT_POSITIVE_INTEGRAL.md`,
`../triangle/qt_positive_integral.py`, the retained C86 QT capacity theorem,
and `../triangle/complete_qt_certificate.json`. The original H(0,1) observer,
native X6 interpretation and all integer competitors remain unchanged.

## 1. Normalization and support

The C86 count has exactly one positive ordered basis per QT face, hence its
Palm coefficient is 1/zeta(2). The three positive triangle direction sectors
are related by orientation-preserving triangle symmetries. The other three
sectors have normalized determinant capacity at most 1/8 and therefore cannot
contribute for A<4.

Within v=u(1,-t), w=(z,1/u-tz), the determinant delta Jacobian cancels the u
from dv, leaving du dt dz. The affine triangle reflection

\[
(x,y)\mapsto(x,r-x-y)
\]

sends t to 1-t and reverses ambient orientation. Simultaneously replacing w
by -v-w exchanges the two actual endpoints and reverses basis orientation.
Their composition preserves positive determinant and all four inclusion
conditions. Thus C_r(u,t)=C_r(u,1-t), and the total multiplier is exactly
3 times 2 divided by zeta(2).

The source constraints imply u<=r/2. The two endpoint levels s±1/u both lie
in [0,r], implying u>=2/r. The source support and
u(r-2u)<=r^2/8<1 force s-1/u<tr<s+1/u, so the two endpoint chords really do
remain on the claimed opposite linear branches. No missing chord branch is
hidden in the reduction.

## 2. The small-angle exclusion is valid

For 0<=t<=1/3, every one of the C86 positive-sector capacity cases is bounded
by (1+t)/8. The three required rational comparisons reduce, with positive
denominators, to

\[
t(8-15t+9t^2)\ge0,\qquad1-9t^2\ge0,
\qquad t(1-3t)\ge0.
\]

All are valid on the full interval. For the first polynomial, after t=z/3,
the quadratic factor has positive Bernstein coefficients 8, 11/2, 4.

If 8/3<A<=3, all t<1/3 are excluded because their capacity is strictly below
1/(2A). If 3<A<4, all t<4/A-1 are excluded by the same capacity comparison.
Therefore

\[
t_0(A)=\min\{1/3,4/A-1\}
\]

is a safe lower cutoff. Reflection supplies the corresponding upper cutoff.
The displayed integration region [2/r,r/2] times [t0,1/2] includes all support
and stays away from t=0 for each fixed A<4.

## 3. Exact source elimination and its factors

Writing the source as x=(a,s-ta), let Y and Z be the endpoint horizontal
coordinates. The relation Y+Z=2a-u gives b=Y+Z and h=Y-Z. The source lower
bound and endpoint nonnegativity yield b>=max(u,|h|). The upper and lower
source-layer bounds reduce exactly to the interval length in Equation (9).

The Jacobian from (a,Y) to (Y,Z) is 1/2 and from (Y,Z) to (b,h) is another
1/2. The b integral is

\[
\int_{b_0}^\infty(c-b/2)_+\,db=(c-b_0/2)_+^2.
\]

Thus the factor 1/4 in C=(1/4) integral K_+^2 dh is correct. K is concave,
has exactly the four listed possible knots, and tends to minus infinity with
the stated left and right slopes. Integrating its affine pieces gives the
two cubic tail terms and the three nonnegative Phi terms. Coincident knots
and crossings of K=0 are covered by the formula.

## 4. Full-cell enclosure, including changing knot order

For any actual parameter point in a rectangle, its four knot values lie in
the computed outward intervals. Its actual order cannot be rejected by the
code's interval-separated inversion test. Thus at least one retained
permutation applies to every actual point, even if orders change inside the
rectangle.

For that order, each adjacent width is nonnegative. Intersecting its interval
with the nonnegative axis preserves its true value. Phi is separately
nondecreasing in both endpoint values, directly from its integral definition;
evaluating it at the lower/lower and upper/upper endpoints gives a valid whole
rectangle range. Every remaining factor is treated by outward interval
arithmetic. Taking the hull across all retained orders therefore encloses
the whole parameter rectangle. Extra impossible orders can only enlarge the
enclosure, never omit an actual value.

The zero test is also safe: a concave broken line with both tails descending
to minus infinity attains its maximum at one of its knots or on a flat
segment between knots. If all knot upper bounds are nonpositive, K_+ vanishes
throughout the whole rectangle.

The algebraic u endpoints and r are outwardly enclosed, and the multiplier
du*dt contains the exact physical cell area. The implementation encloses each
exact cell; it does not silently replace exact cells by midpoint samples.

## 5. Independent exact three-dimensional check

`audit_qt_integral.py` validates the source formula through an independent
route. For fixed rational r,u,t, it returns to the original four points

\[
x-v,\quad x+v,\quad x+w,\quad x-v-w
\]

and imposes their twelve triangle half-space inequalities directly in the
three variables (source_x, source_y, basis_shear). It enumerates all rational
vertices, obtains each facet polygon and sums exact pyramid volumes. This
uses neither the layer-s elimination nor the new h elimination.

All 85 tested original polytopes, including 72 positive-volume cases, agree
exactly with the K_+^2 formula. In particular,

\[
r=5/2,\quad u=6/5,\quad t=1/2
\quad\Longrightarrow\quad C_r(u,t)=1/500.
\]

All 85 reflection identities also agree exactly. Three whole interval boxes
were additionally checked against 27 exact rational interior/corner values.
These finite checks supplement the preceding analytic proof; they are not
used as a substitute for a universal claim.

## 6. Final saved certificate

The review verified the final four-part rational sum and all eight source
SHA-256 bindings in `complete_qt_certificate.json`. Its interval is

\[
\frac{8879799718450538658554682430737307}{2^{112}}
\le\kappa_3\le
\frac{9259117095632433299866803560123257}{2^{112}},
\]

with displayed approximations
[1.71018721779252385043805, 1.78324108730662770168686]. A safely widened
conclusion is

\[
\boxed{1.7101<\kappa_3<1.7833.}
\]

`qt_independent_review_checks.json` records the actual successful review
checks. The complete outer kappa mesh was run by the author and was not rerun
in this review. This is an internal independent derivation and code review,
not an external peer-review claim.
