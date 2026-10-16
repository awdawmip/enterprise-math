# Primitive uniqueness in the specified proper weak row complex

UNREVIEWED AUTHOR WORKING COROLLARY, EM-FREE-CF1677. This is a bounded
application of previously proved local gauges and elementary convergent
partial fractions, not a new general Tool or a separately proposed paper.
No old independent verdict is a verdict on this argument. No remote Source,
activity checkpoint, scientific program, Native operation or formal Task is
created. The current actor remains RA13/30 with its original LOCAL key,
registration history, STOPs, false ending and cumulative budget UNKNOWN.

## 1. The exact question and the four-object boundary

For the original prime p congruent to 13 or 19 modulo 24, let O be the
specified complete unramified DVR, K=O[1/p], and use exactly

    S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
    A=2S-1, B=4S-5,
    D=(2P)^(-1) [[A,1],[B,-A]],
    R=O[r,f^(-1),q^(-1)]^dagger[1/p], L(h)=h'+hD.

Rows and derivatives have their original variance. The question is whether
the weak primitive of a fixed row source, if it exists, is unique in R^2.
It concerns the literal embedded weak ring; it does not concern an arbitrary
p-completion, all gauges, a rank-four extension, or an original observation.

The entire bounded intake is four already personally consumed objects,
reread locally with their original complete UTF8 pins. No new remote call,
directory search, external query, unpublished working input or additional
dependency was used:

1. The actual six-boundary Frobenius handoff, 4771B, SHA256
   e7789c14e1f44d902e87440d8a5b8178169ee62b100dc2ec59cc1df47090e4db,
   in cm24_convergence_new_anchor/actual_boundary_frobenius/.
   This is metadata, not a new proof input.
2. CM24_ACTUAL_SIX_BOUNDARY_WEAK_FROBENIUS_JOINT_AUTHOR.md, 21977B,
   SHA256 8e5dbe7d89528632b402e5d103925f6f3452ea11b654b7939ac3c68c779f2133,
   Source 0464ecd04acab1e33dd3a480001ba6b2a3d1677d, in that same directory.
3. CM24_SIX_BOUNDARY_WEAK_COKERNEL_NORMAL_FORM_AUTHOR.md, 9901B,
   SHA256 5b9e3acafdfeb0c008a02875fc4b53c46589a82505b69053f2b2d69d13f0c788,
   Source 1c619205b6abd1f15e923fdfe126edf518e19b7b, in
   cm24_convergence_new_anchor/weak_six_boundary_normal_form/.
4. CM24_ACTUAL_WEAK_SOURCE_CLASS_LOCAL_RESIDUE_OBSTRUCTION_JOINT_AUTHOR.md,
   21300B, SHA256 a9e6e05ddc90daf46df36d510c1dd078b5b0e1bde6acfa5e5a3189a3e82e30f5,
   Source 5530d83fd0d5831c4e588d9652a7edcf5fafef0b, in
   cm24_joint_weak_source_class_7cda51_88303d/.

All these paths are under research_notes/owner_goal_20261016/. Their
57949B sum is only this four-object reread subtotal, not a formal budget
measurement or a reset. Historical UNREVIEWED wording in those immutable
originals is retained; their later accepted scopes are not being re-voted.

The old normal-form proof already proves the rational kernel is zero in
Section 4. Its Section 6 constructs weak primitives and says uniqueness is
not needed. The actual Frobenius whole also excludes a uniqueness claim
from its assertion. Neither exclusion establishes global absence of another
proof. Current global coverage remains UNKNOWN. The question below is only
what follows from these fixed, already available inputs.

## 2. Reused analytic input, with variance fixed

Put E={1,-1,1/2,-1/2}. Distinct points have p-unit differences. By the old
normal-form Sections 2-3, at a in E, x=r-a, there is a normalized matrix
H_a, with H_a and H_a^(-1) analytic on every |x|<1, satisfying

    H_a'=D H_a-H_a N_a/x, H_a(0)=I, N_a^2=0.

At infinity z=1/r put J=diag(z,z^(-1)). The same old proof and the joint
proper theorem Sections 5-6 supply a regular good connection

    D_inf=-J^(-1)J'-z^(-2)J^(-1)D(1/z)J

and H_inf, H_inf^(-1) analytic on every |z|<1, with H_inf'=D_inf H_inf.
Primes here on infinity formulas mean d/dz.

The old joint Section 2 supplies differential restrictions R -> Robba_x at
each finite boundary and at infinity. Consequently the products with these
full-disc gauges are genuine convergent Laurent rows on common annuli.
No arbitrary strong-completion element is assigned such a restriction.

## 3. A weak element regular at the finite boundaries and zero at infinity

Here is the elementary gluing fact needed below, including its convergence
argument. If v in R extends analytically across every a in E and its infinity
restriction is O(z), then v=0.

After a fixed p denominator write

    v=p^(-s) sum_(l>=0) p^l v_l,

where v_l is integral in the displayed algebraic generators, of presentation
degree at most C(l+1), for some C>=1. Old normal-form Section 6 gives an
integral partial-fraction decomposition of each v_l whose polynomial degree
and four pole orders are at most C(l+1). This uses the p-separated linear
factors of f and q. Thus coefficientwise summation gives

    v = sum_(j>=0) b_j r^j
        + sum_(a in E) sum_(j>=1) c_(a,j)/(r-a)^j,          (1)

with

    val_p(b_j), val_p(c_(a,j)) >= j/C-1-s.                (2)

Indeed a coefficient of index j can occur only when j<=C(l+1); every
participating integral coefficient then has l>=j/C-1. The nonarchimedean
sum introduces no further loss. Increasing C or s accommodates the finitely
many initial terms without changing this bound's purpose.

Choose a real radius rho with |p|^(1/C)<rho<1, sufficiently close to 1.
Formula (2) makes (1) converge on the common affinoid described by
|r|<=rho^(-1) and |r-a|>=rho for all a. It agrees there with the original
weak presentation: the rational decompositions are finite term by term,
and both regroupings have geometrically vanishing tails. The polynomial
series is analytic on a disc of radius greater than 1. Each principal-part
series is analytic wherever |r-a| is greater than a fixed radius below 1.

At a fixed a, the polynomial series and all principal parts for b!=a are
analytic on |r-a|<1. To see the latter assertion directly, write
r-b=(a-b)+(r-a): the denominator a-b is a unit, the binomial expansion has
integral coefficients, and the c_(b,j) tend to zero exponentially by (2).
Thus the entire negative Laurent part at a is precisely
sum_(j>=1)c_(a,j)x^(-j). Analytic extension of v at a and uniqueness of a
convergent Laurent expansion force every c_(a,j)=0.

After doing this for all four a, (1) is just sum b_j r^j. On a common
infinity annulus its expansion is sum b_j z^(-j). The assumed O(z) extension
has only strictly positive powers of z. Uniqueness of Laurent coefficients
therefore forces every b_j=0, including b_0. This proves the gluing fact.
It uses neither analytic continuation across an unspecified domain nor
a new rigid-GAGA input.

## 4. The homogeneous row has zero second component

Suppose h=(h_1,h_2) in R^(1x2) satisfies L(h)=0. At a finite boundary put
k=hH_a. The differential restriction and the gauge identity give exactly

    k'=-kN_a/x.

Write its convergent Laurent expansion k=sum_(j in Z) k_j x^j. Then
k_j(jI+N_a)=0. For every nonzero integer j, over the characteristic-zero
field K,

    (jI+N_a)^(-1)=I/j-N_a/j^2.

Hence k_j=0 for j!=0, and k_0N_a=0. In particular h=k_0H_a^(-1) is analytic
on the whole finite disc |x|<1. This proves the needed extension of h_2 at
all four a. There is no logarithmic term hidden in this calculation: k is
an ordinary convergent Laurent row in the specified Robba ring.

For infinity use h_good=h(1/z)J, not a transpose or an inverse change of row.
Since d_z h(1/z)=z^(-2)hD(1/z), the displayed D_inf gives

    h_good'+h_good D_inf=0.

It follows that (h_good H_inf)'=0 on its annulus. A convergent Laurent
series with zero derivative in characteristic zero is constant. Thus

    h_good=c H_inf^(-1),
    h_2(1/z)=z (c H_inf^(-1))_2=O(z).                     (3)

There is no coefficient-sigma issue here: this is the ordinary homogeneous
connection equation, not a semilinear Frobenius eigenvector equation.

Apply Section 3 to v=h_2. The finite extensions and (3) imply h_2=0. The
second component of L(h)=0 is now h_1/(2P)=0. Since 2P is invertible in R,
h_1=0 as well. We have proved

    ker(L:R^(1x2) -> R^(1x2)dr)=0.                       (4)

The scalar operator K(v)=(Pv')'-2qv has zero kernel in R too: its reversible
old row construction h(v)=(-2Pv'+Av,v) has L(h(v))=(-2K(v),0), so (4) forces
v=0. This is the same conclusion in the old scalar presentation, not a
second discovery.

## 5. What this consumes and what it does not

Together with the accepted six-observation completeness theorem, (4) says:
for a fixed source b in R^2 dr, all six observations vanish if and only if
there exists exactly one h in R^2 with L(h)dr=b. Existence and the six tests
are entirely old results; the additional step here is injectivity on the
same weak ring. In particular, whenever the old explicit weak lift-change
formula supplies a primitive for a fixed difference of row oneforms, another
primitive in this same R^2 must be equal to it.

This does not furnish a new source evaluator, general executable solver,
strong-completion result, original functional or rank-four comparison. It
does not alter a lift, Frobenius normalization, beta, hdiv, a weighted LC
join, or any stopped task. The earlier finite hdiv input search remains
closed at HOLD; none of its inaccessible or unmatched external leads is a
premise here. r,z are separately typed algebraic coordinates, not native
spatial axes; P000 and the native fixed X6 substrate are unchanged.

The disposition is an UNREVIEWED source-specific classical-composition
corollary for possible consumption with the existing normal form, not a
new paper/Tool claim or global novelty claim. No independent review, current
accepted-state update, remote publication or activity event is inferred.

