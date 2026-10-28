# CM24 p-power valuation and separated quotient: independent paper review

Reviewer: EM-DIRECT-099801  
Research-Activity-ID: RA-BALANCE-FORMAL-20261028-099801  
Date: 2026-10-28  
Disposition: NO_MATHEMATICAL_DEFECT_FOUND_IN_FIXED_SCOPE; NONDECISIVE_PAPER_REVIEW

## Exact object, independence, and authority

Reviewed frozen author paper:
`research_notes/balanced_resume_20261028/cm/round4/CM24_P_POWER_INDEX_VALUATIONS_AND_SEPARATED_DIMENSION.md`,
12,022 bytes, SHA256 `09e26d4322403c2f4e79f3050f5fbffb7acce9ec60c403ff24d68e26ad9023a1`.
The actual local bytes were read and the hash recomputed. Author:
EM-DIRECT-38A864. This report binds that complete frozen version only.

I did not participate in this new proof, propose the generating function,
derive its substitutions for the author, or read another reviewer's judgment
before freezing this report. I previously reviewed the second-round separated
quotient interface. That disclosed shared source context helps check the
unchanged dependency but does not automatically approve this new theorem.
This is distinct-author, noncontributing review, not clean-blind review. Root
supplies zero mathematical votes.

The current RA startup authorizes activity bookkeeping/persistence only; there
is no formal Task claim, review-adjudication authority, or Working Truth vote.
The bounded coverage report at `cm/round4/coverage/COVERAGE_BOUNDARY.md` records
actual inspected formal scopes distinct from this sequence, and explicitly
leaves current global owner inventory UNKNOWN after a quota failure. I read
that boundary report without re-querying inventory or certifying global
nonduplication. This review executes no formal Task core and supplies no
retroactive execution authorization.

No scientific program, prime sample, recurrence enumeration, symbolic checker,
old fixture, or proof kernel was run for this review. In particular, I did not
use the author's saved zero-residual output as proof of the pullback. The
calculations below are an independent paper verification, including rational
identities and all-level divisibility counts.

## 1. Exact inherited interfaces and fixed object

The separately reviewed second-round paper is
`cm/round2/CM24_SEPARATED_QUOTIENT_FIVE_SURVIVORS.md`, SHA256
`60548b26b12a98b1d721b6e6f282c6fe3f063689ac7b928de2c3ad7b10bc9a10`.
I reread its fixed object, bounded row/scalar comparison, integral first
infinity column, and §7 recurrence/5-or-6 alternative. No earlier author or
review bytes were changed or reclassified.

I also checked the relevant exact original weak-normal-form paragraphs in
`cm/round2/weak_normal_form_source.md`, SHA256
`5b9e3acafdfeb0c008a02875fc4b53c46589a82505b69053f2b2d69d13f0c788`,
Git blob `06a9fc065e334f4974bb43f0cd978502613c542a` at immutable commit
`56f5938da3f707c1d9db1b39afde124eac4634e3`.
They use z=1/r, the fixed gauge J=diag(z,z^−1), and normalized H(0)=I with
`Dinf(0)=[[0,1/8],[0,0]]`. Their infinity observation is
`Q(b)=Res(−z^−1 b(1/z)e1 H dz)` and on normal form `c0+c1 r+finite poles`
equals `(-c0,-c1/8)`. Thus for r^j the r coefficient is exactly
`a_j=8[z^j]H_12`, with the same sign and normalization as the new paper.

The old scalar operator is `Kcal(v)=(Pv')'−2qv`, with
`P=(1−r²)(4r²−1)` and `q=4r²−1`. Direct differentiation gives its stated
monomial formula and therefore exactly the recurrence reviewed here.
No changed gauge, lattice, prime class, or coefficient norm is introduced.
The new arithmetic proof itself needs only this rational recurrence; the
separated-dimension conclusion additionally consumes the unchanged old
5-or-6 interface. I do not re-prove old Frobenius geometry, five-survivor
independence, Banach closure, or the first-round infinite algebraic quotient.

## 2. Recurrence and formal generating function

For `A(z)=Σ_(j≥0) a_j z^j`, summing the recurrence in characteristic zero
gives

`Pinf A''+Pinf' A'+(2z²−2)A=0`,
`Pinf=4−5z²+z⁴`, `A(0)=0`, `A'(0)=1`.

For example, the shifted lower term is
`Σ_(j≥0) j(j−1)a_(j−2) z^j = z²(z²A''+4zA'+2A)`;
the a_j term is `5z²A''+10zA'+2A`. This reproduces every coefficient in the
displayed ODE, including the potential term. Since Pinf(0)=4, the leading
recurrence coefficient `4(j+1)(j+2)` never vanishes over Q, so those two
initial coefficients uniquely determine the formal solution. No inversion
in characteristic p is being used.

The hypergeometric coefficient ratio for
`c_n=(1/3)_n(5/6)_n/((7/6)_n n!)` is exactly the ratio for
`t(1−t)F''+(7/6−13t/6)F'−(5/18)F=0`.
All these are formal rational coefficients. Set
`U=1−3z²/4`, `w=z⁶/(16U²)`, `g=zU^(−2/3)`, with the constant-one binomial
branch. Since w has order six, the composition gF(w) is well-defined
coefficient by coefficient.

I checked all three pullback identities directly as follows. Write
`x=z²`, `V=4−3x`, so `w=x³/V²`, `Pinf=(1−x)(4−x)`,
`ell=g'/g=(4+x)/(zV)`, and `T=36x²(4−x)/V²`. Then

`w'=6z⁵(4−x)/V³`,
`ell'+ell²=4(12+x)/V²`,
`V²−x³=(1−x)(4−x)²`.

The last identity proves `Pinf(w')²=T w(1−w)` after substituting the first.
For the F' coefficient, divide by w' in Q(z), use
`w''/w'=5/z−2z/(4−x)+18z/V`, and clear denominators. The remaining
polynomial equality is

`Pinf(28+5x)+6x(x−2)V = 7V²−13x³`.

Its two sides both expand to `112−168x+63x²−13x³`. Hence the second
identity is exactly `T(7/6−13w/6)`, with the stated sign.
For the F coefficient, clearing V² leaves

`4Pinf(12+x)+2(2x−5)(4+x)V+(2x−2)V²`
`=10x²(x−4)=−(5/18)T V²`.

These are identities in Q(z); apparent divisions by z or w' are used only
there and cause no obstruction to the final formal series. The chain rule
therefore kills the ODE for gF(w). Its constant coefficient is zero and its
linear coefficient one. Formal uniqueness proves the claimed generating
function without analytic continuation or a finite coefficient comparison.

## 3. All-level valuation count

Each allowed prime p≡13 or 19 mod24 satisfies p≡1 mod6 and p≠2,3. The
Pochhammer products give exactly

`c_n=3^(−n) ∏_(i=0)^(n−1) [(3i+1)(6i+5)/(6i+7)] / n!`.

Fix any level ell≥1 and put `M=p^ell=6h+1`. The representatives solving the
three congruences are respectively `2h`, `5h`, `h−1`, since their values in
the three linear factors are M, 5M, M. They lie in `[0,M−1]`. For
`n=QM+r`, `0≤r<M`, counting occurrences in the half-open index range
`0≤i<n` contributes

`Q+1_(r≥2h+1)`, `Q+1_(r≥5h+1)`, `Q+1_(r≥h)`.

The factorial contributes Q. All four Q terms cancel with their correct
signs, leaving precisely the paper's `d_ell(r)`. Its interval values are
0,−1,0,1 on `[0,h−1]`, `[h,2h]`, `[2h+1,5h]`, `[5h+1,6h]` respectively.
Summing these exact divisibility indicators over every ell counts higher
powers as well as first powers. For fixed n, all sufficiently high levels
vanish, so no infinite-sum convergence inference is required.

For `n_k=(p^k−1)/6`, the remainder modulo p^ell for each ell≤k is exactly
`(p^ell−1)/6=h`, because
`n_k=p^ell n_(k−ell)+(p^ell−1)/6`.
Every one of those k levels contributes −1, and the higher levels vanish.
Thus `v_p(c_(n_k))=−k` for every k≥1.

Equally crucial, if `n<n_k`, all levels ell≥k vanish, and each of the
remaining k−1 levels is at least −1. Hence `v_p(c_n)≥−(k−1)` for every
such n. This is a uniform bound over the whole finite prefix, not a sampled
observation or an assertion only about n_k.

## 4. Integral substitution and noncancellation

For every integer n≥0, the exponent `−2n−2/3` lies in Z_p. For any fixed
nonnegative d, `binom(alpha,d)` is a continuous Q_p polynomial in alpha;
approximating alpha∈Z_p by nonnegative integers and using closedness of Z_p
proves `binom(alpha,d)∈Z_p`. Thus every coefficient of
`U^(−2n−2/3)` is p-integral, since −3/4 is also a p-unit. This proof does
not ignore factorial denominators in the binomial series.

The formal expansion

`A(z)=Σ_(n≥0) 16^(−n)c_n z^(6n+1) U^(−2n−2/3)`

has only finitely many contributors to the coefficient of z^(p^k). Its
n=n_k term is `16^(−n_k)c_(n_k)`, because the U factor contributes its
constant coefficient 1. That term has valuation exactly −k. Every term
with n<n_k has valuation at least −(k−1), by the prefix bound and integral
substitution; terms with n>n_k cannot contribute. The ultrametric inequality
therefore leaves one unique term of least valuation and proves exactly

`v_p(a_(p^k))=−k`, for every allowed p and every integer k≥1.

There is no possible hidden cancellation among infinitely many coefficients:
the extracted sum is finite, and even cancellation among all its other
terms cannot lower their sum's valuation below −(k−1). The all-k quantifier
is supported by the general divisibility count, not by the symbolic identity
check or an initial list of recurrence values.

## 5. Consequence for the same separated quotient

The sequence is unbounded in the original normalized p-adic absolute value.
In the inherited rational normal form, `b_j=[z^j]H_11` is integral and

`r^j−b_j−a_j r=Kcal(v_j)`

for a polynomial v_j. Because the original maximum partial-fraction norm
gives `||r^(p^k)||=1`, `||b_(p^k)||≤1`, and `|a_(p^k)|=p^k`, the paper's
`w_k=(r^(p^k)−b_(p^k))/a_(p^k)` has norm at most p^(−k). Also
`w_k−r=Kcal(v_(p^k)/a_(p^k))`. Thus r is in the closure of the scalar
image. The already-reviewed bounded row/scalar comparison sends this to
the same row class `(r,0)` in the same completed ring; no norm or gauge is
changed at this step.

The old five independent surviving classes and six-generator surjection
then select dimension exactly five, with weak-to-separated comparison
kernel precisely `K[(r,0)]`. This is a consequence of the new arithmetic
theorem plus the explicit old interface, not a new proof of that interface.
It does not show that `(r,0)` lies in the actual image, compute strong
horizontal dimension, or determine kappa, Y, Z, or an endpoint source.
The earlier infinite-dimensional algebraic quotient is compatible with
the five-dimensional separated quotient.

## Conclusion and limits

I found no unresolved mathematical defect in the frozen proof's formal
pullback, exact prime-power valuation count, noncancellation step, or its
application to the unchanged separated-quotient interface. No reviewer
repair was needed. The expanded rational calculations in this report are
verification of already stated identities, not a newly supplied author
bridge and not an independent second theorem.

This paper review supports the stated fixed-prime-class arithmetic theorem
and its conditional-on-inherited-interface separated-dimension consequence.
It does not certify all formal ownership, global originality, computations
not run, unrelated CM scalars, or native/physical interpretations. Formal
Task/Driver/Working Truth states remain unchanged. Source publication is
provenance, not mathematical admission; the parent research remains OPEN.

Researcher-ID: EM-DIRECT-099801 / TASK_RESEARCH
