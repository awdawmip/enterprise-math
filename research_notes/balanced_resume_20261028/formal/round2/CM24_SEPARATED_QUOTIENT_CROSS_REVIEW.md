# Distinct-reader cross-check: CM24 separated quotient has five or six classes

Reviewer: EM-DIRECT-099801.
Activity: RA-BALANCE-FORMAL-20261028-099801.
Date: 2026-10-28 (Asia/Shanghai).
Finding: LOCAL_NONAUTHOR_PAPER_CHECK_NO_MUSTFIX_FOUND at the explicitly stated
normal-form and actual Frobenius interfaces. The value five versus six is not
decided by this review. This is not a Driver verdict, formal Task acceptance,
Working Truth, Foundation promotion, or parent closure.

## Exact object, reading, and independence

The complete frozen object reviewed is
`cm/round2/CM24_SEPARATED_QUOTIENT_FIVE_SURVIVORS.md`, SHA256
60548b26b12a98b1d721b6e6f282c6fe3f063689ac7b928de2c3ad7b10bc9a10.

I read the full original weak-normal-form paper in
`cm/round2/weak_normal_form_source.md`, with actual connector response
`weak_normal_form_readback_actual.json`, immutable commit
56f5938da3f707c1d9db1b39afde124eac4634e3 and Git blob
06a9fc065e334f4974bb43f0cd978502613c542a. Its exact repository path is
`research_notes/owner_goal_20261016/cm24_convergence_new_anchor/weak_six_boundary_normal_form/CM24_SIX_BOUNDARY_WEAK_COKERNEL_NORMAL_FORM_AUTHOR.md`.
Sections 2--4 provide the concrete gauges, normalized infinity Frobenius
identity, rational normal form and boundary-coordinate values used here.

I reused my previous independent check of the unchanged strong-completion
paper b19248580b174c7ce6aaacc453ab777f7c81f8ec820a5c153c4acd1cc2dca1e0
and my whole reading of its integral-iterate source, blob
58ec6ce156797557758cd868d21bcaf2c4b4776c. In particular I checked there the
actual canonical good-fiber value M(0)=diag(p/beta,beta), not merely det M=p.
I did not reconstruct the entire original geometric Frobenius proof anew.

I did not participate in this author's new construction, receive its partial
proof before freezing, or offer repairs during construction. Shared owner
control/source context is disclosed. This is a second distinct-reader paper
check, not clean-blind review or an additional author contribution. The other
reviewer was not consulted for a preliminary mathematical verdict.

All spaces here are external arithmetic Banach/module models; six cohomology
coordinates are not native spatial axes. P000 and Heartbeat semantics remain
unchanged.

## 1. The partial-fraction completion and its continuous dual criterion

Since p>=13, differences among 1,-1,1/2,-1/2 are p-adic units. The localizations
by f and q are therefore the same algebra as adjoining the four individual
linear-pole inverses. Partial fractions over O are valid: monic polynomial
division stays integral, and separating the poles uses only inverse powers
of their unit differences. No division by a nonunit multiplicity factorial
is needed when taking the formal Taylor coefficients.

Thus the stated countable partial-fraction family is a free O-basis of the
algebra, not just a K-vector basis after a change of lattice. Its uniqueness
in K(r) implies that divisibility by p^n is coefficientwise. Completing the
direct sum gives exactly O-valued coefficients tending to zero p-adically;
inverting p gives c0(K) in that same basis, with the maximum coefficient norm.

A bounded sequence of basis weights defines a convergent continuous linear
functional on c0(K), since every coefficient times its weight tends to zero
and K is complete nonarchimedean. Conversely continuity bounds the values on
the norm-one basis vectors. The paper uses exactly this elementary criterion,
not an unsupported Hahn--Banach or arbitrary-dual assertion.

## 2. Row/scalar comparison extends as an actual bounded identity

The multipliers P,A are integral polynomials, and differentiation sends each
partial-fraction basis vector to an integral scalar times another such vector.
All operators in the displayed elimination formulas are bounded on the
completion. I checked the signs of the scalar reduction directly:

    c(L(h1,h2))=-2(P h2')'
               +[A'+((4S-5)+A^2)/(2P)]h2.

Here A'=6q and S^2-1=-f q^2 imply the bracket is 4q. The result is exactly
-2 Kcal(h2). Together with
b-(c(b),0)=L(2P b2,0) and
L(-2Pv'+Av,v)=(-2Kcal(v),0), this gives mutually inverse bounded comparison
maps after quotienting by the corresponding closed images. The invertible
scalar -2 is harmless because p>=13.

Every rational localized input has normal form in V6. Rational localized
inputs are dense in the strong Banach space, so V6 has dense image in the
separated quotient. Its image has dimension at most six and hence is closed
in the Hausdorff Banach quotient. It must therefore be the whole quotient.
This proves the upper bound and surjectivity without first assuming that the
old six-coordinate boundary map extends continuously.

## 3. The finite residues use one integral column, not the whole log gauge

The relation C_a e2=k_a is exact for the stated constant matrix. Therefore
H_a k_a=B_a e2=J_epsilon(f0), and its first entry is f0(z_a(x)). The log(u)
term belongs to the other column and disappears from this particular selected
column by an exact identity, rather than by an estimate or omission.

The inherited f0 coefficients and polynomial z_a(x) coefficients are integral,
with z_a(0)=0 and f0(0)=1. Each selected coefficient is consequently integral.
This bounds the residue weights on the own-pole principal parts by one.
Polynomials and other-pole principal parts are regular at that point and give
zero residue. The four functionals extend to c0(K), annihilate the strong
scalar image by continuity/density, and still take the identity matrix on the
four simple-pole classes. All four independent survivors are paid without
assuming an integral bound on the whole logarithmic gauge.

## 4. The first infinity column is uniformly integral

The old weak-normal-form source gives the exact normalized relation
H(z)=G(z)H(z^p)G(0)^(-1), where G=M^(-T). The literal canonical good-fiber value
from the integral source gives G(0)^(-1)=diag(p/beta,beta). Thus the first
column satisfies h1=(p/beta)G h1(z^p).

Since det M=p and M is integral, (p/beta)G is integral. For every positive
coefficient index n, the composition h1(z^p) uses only indices at most
floor(n/p)<n. Starting from h1(0)=e1, coefficient induction proves integrality
of the whole first column. A constant coefficient term of the matrix does
not introduce a same-index unknown because p>1. The source's rational H
coefficients are fixed by coefficient Frobenius, as required by the stated
normalization; no generic semilinear identity was silently linearized.

Accordingly Q1 has bounded basis weights, kills the closed image, and sends
1 to -1. Its finite-pole weights vanish because at infinity those principal
parts contribute only nonnegative powers after the transformed one-form
factor. The old value H_11,1=0 ensures Q1(r)=0. Together with the four finite
residues, this leaves any relation among V6 in the line Kr and proves that
the other five classes are independent after separation.

## 5. The exact sixth-coordinate criterion and both alternatives

The rational normal-form observation is Q(n)=(-c0,-c1/8). Thus for r^j,
c0=[z^j]H_11=b_j and c1=8[z^j]H_12=a_j. This pays the factor eight and the
signs. Q2 is continuous on c0(K) exactly when h_j, equivalently a_j, is
uniformly bounded p-adically. All its finite-pole weights are zero.

If bounded, the functional extends, annihilates the strong image by density,
and Q2(r)=-1/8 gives a sixth independent class. The dimension is six and the
comparison kernel is zero.

The scalar identity for Kcal(r^j) gives the stated recurrence by taking its
normal-form r coefficient, with denominator 4(j+1)(j+2) nonzero in K. There
is no illicit characteristic-p division. The initial values a0=0,a1=1 and
the missing negative values zero force all even terms to vanish; the displayed
odd values follow by direct rational substitution. They are illustrative
identities, not evidence deciding the all-index valuation question.

If unbounded, choose indices with |a_j| tending to infinity. The rational
normal form of a polynomial has no finite principal parts, and its primitive
can be chosen polynomial by the same descending polynomial reduction. Hence
r^j-b_j-a_j r=Kcal(v_j) with v_j rational polynomial. Because b_j is integral,
the scaled input (r^j-b_j)/a_j tends to zero in the actual strong norm. Its
difference from r belongs to Kcal(Rhat). Therefore r lies in the closure of
that image. The already surviving five classes then force dimension five
and comparison kernel precisely Kr.

This proves both directions of the stated dichotomy: the sequence is either
bounded or unbounded, with corresponding dimensions six or five. No finite
list chooses the alternative. In the unbounded case the argument establishes
membership in the closure, not actual exactness of r. Those are different
statements and the paper correctly retains that distinction.

## 6. Interpretation with the previous strong result

The first-round algebraic cokernel is infinite dimensional, whereas the
separated quotient is finite dimensional. The exact sequence with kernel
closure(L(X))/L(X) consequently forces that kernel to be infinite dimensional;
otherwise an extension of two finite-dimensional spaces would be finite.
This conclusion adds no separated direction beyond the old six weak classes.

No must-fix gap was found in the new five-survivor proof or the exact
boundedness/5-versus-6 equivalence at its inherited inputs. I have not decided
the recurrence's p-adic boundedness, produced a strong primitive of r,
classified the strong horizontal kernel, or identified a basis of the
closure-of-zero quotient. Those remain actual open questions.

Validation here is independent paper reasoning plus exact text/hash binding.
No scientific program, finite coefficient scan, symbolic solver, prime sweep,
numerical computation, or Lean kernel was used. Recommended harvest is
RESULT_ONLY_STANDARD_COMPOSE with the exact integral partial-fraction lattice,
selected residue column, normalized first-column Frobenius multiplier and
the unchanged rational recurrence all retained as explicit conditions.

Researcher-ID: EM-DIRECT-099801 / TASK_RESEARCH
