# Nondecisive review: five surviving strong separated classes

Reviewer: EM-REVIEW-58D6A2; activity RA-BALANCE-REVIEW-20261028-58D6A2.
Reviewed author file: `cm/round2/CM24_SEPARATED_QUOTIENT_FIVE_SURVIVORS.md`.
SHA256: `60548b26b12a98b1d721b6e6f282c6fe3f063689ac7b928de2c3ad7b10bc9a10`.
Finding: no unresolved mathematical defect found in the stated conditional
interface. The separated cokernel has dimension five or six; the exact
remaining alternative is boundedness of the displayed rational recurrence.
The paper does not decide that alternative.

I read the complete frozen paper and complete weak-normal-form source
`cm/round2/weak_normal_form_source.md`, original blob
06a9fc065e334f4974bb43f0cd978502613c542a. I checked the exact good-infinity
normalization in the previously available integral-iterate source, blob
58ec6ce156797557758cd868d21bcaf2c4b4776c. The canonical geometric Frobenius
and weak six-class interface are expressly inherited hypotheses; this
report does not reconstruct their geometric provenance or upgrade their
historical review status. In particular determinant p alone is insufficient.

## Completion and comparison

The four punctures and their nonzero differences are p-adic units for
the allowed primes. Partial fractions over O therefore use no nonunit
denominator, and uniqueness over K(r) identifies the integral algebra
with the free O-module on the stated polynomial/principal-part basis.
Its inverse limit modulo p^n consists exactly of coefficient families
vanishing modulo each p^n outside a finite set. After inverting p this
is c0 over K with its maximum norm, not an unrestricted formal product.
This proves both necessity and sufficiency of bounded basis weights for
a continuous functional, using convergent nonarchimedean sums only.

Differentiation preserves the integral algebra: on the explicit basis
it multiplies by an integer and shifts the degree or pole order. The
polynomial multipliers are bounded. The row/scalar identities in (2)
have the stated signs; direct cancellation removes h1 from c(L(h)),
leaving -2 Kcal(h2). Hence the identities extend to the strong completion
and descend in both directions through closures of images.

Rational normal forms make the six-dimensional image dense in the
separated scalar quotient. The quotient is Banach, and a finite-dimensional
subspace over complete K is closed. Thus this image is all of the quotient.
This reasoning needs neither compactness of O nor Hahn--Banach nor a
continuous extension of the entire old normal-form map.

## The five bounded functionals

The finite-pole calculation uses Ca e2=ka exactly, so Ha ka is the
second column of Ba, namely J_epsilon(f0). Its first component is the
integral composite f0(z_a(x)). All other basis components are regular
at that pole, and the selected simple pole has residue one. This supplies
four bounded annihilators. The potentially unbounded logarithmic column
is not used.

At infinity, G(0)^(-1) has first diagonal entry p/beta. The first-column
identity is consequently h^(1)=(p/beta)G h^(1)(z^p). Its multiplying matrix
is integral, and every positive-index coefficient depends only on earlier
indices. Starting from e1 proves the complete first column integral.
Using beta instead would not prove this; the displayed orientation is
correct. Rational coefficients justify the inherited sigma convention.

The Q1 weights on r^j are -[z^j]H11 and its weights on every finite-pole
principal part are zero, since such a principal part begins with a positive
power of z. Thus Q1 is bounded and Q1(1)=-1. The original H1=Dinf(0)
gives Q1(r)=0. Density plus continuity proves annihilation of the full
strong image, not just rational images. Together these five functionals
give independent values on the constant and four simple poles. Their
common kernel on V6 is exactly Kr, proving the asserted kernel bound.

## The final recurrence alternative

The rational normal form of r^j is b_j+a_j r with
b_j=[z^j]H11 and a_j=8[z^j]H12. Applying its r-coordinate to the exact
Kcal(r^j) identity gives recurrence (9), including j=0,1 and the declared
negative-index zeros. The four stated odd initial values and vanishing
even subsequence follow algebraically. Division is in characteristic zero.

If (a_j) is bounded, Q2 has bounded basis weights, extends continuously,
annihilates the image, and gives Q2(r)=-1/8. This proves dimension six.
If it is unbounded, choose a subsequence with |a_j| tending to infinity.
The constants b_j are integral by the independent first-column argument.
The c0 norm of (r^j-b_j)/a_j is therefore at most |a_j|^(-1), tending to
zero. Rational normal form gives this element minus r in the scalar image.
It follows that r lies in its closure and the dimension is exactly five.
The sign in this approximation and the distinction between image and
closure are correct. No assertion of actual r-exactness follows.

Combined with the separate nonclosed-image result, finite separated
dimension forces the closure-of-zero quotient to be infinite dimensional.
This interpretation is conditional on that earlier result; it is not
needed for the five-survivor proof itself.

## Evidence and reuse boundaries

This was symbolic paper checking. No scientific program, recurrence scan,
solver, sample calculation or proof kernel was executed. Banach closure,
partial fractions and bounded dual weights are standard composed tools;
the new scope is their exact strong-separated application and the single
remaining boundedness criterion, not a new general tool family.

I did not participate in the author's construction. Shared control and
source exposure are disclosed; this is nonauthor NONBLIND review, not
clean-blind review. No formal Driver disposition, Task completion,
canonical admission, native dimension change or parent-goal closure is
supplied. The inherited interfaces and undecided dimension five/six remain
explicit in any reuse of this report.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
