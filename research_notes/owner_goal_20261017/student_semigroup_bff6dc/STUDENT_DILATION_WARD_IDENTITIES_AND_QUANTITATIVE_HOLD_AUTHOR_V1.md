# Student dilation Ward identities and quantitative HOLD

First durable local author artifact of the previously complete Ward chat
argument. Sole new author: BFF / EM-DVR-BFF6DC; original session
MCP-47562f9f432d4978a7bea0dd60ecc4aa and
DA-144D0C4639CACEEE75DC; no Researcher RA.
Classification: finite exact RESULT_ONLY / COMPOSE, with quantitative HOLD.
This text does not alter the separate Student semigroup V1/V2 artifact,
its proof, or either temporary review. No new Source or final artifact/
Source review exists for this Ward text at creation.

## 1. Exact old inputs, actual reading and original carrier

Use the original positive Student space
V={complex polynomials in v of degree at most N=m-2}, dimension m-1, with

    <f,g>_m=integral_R conjugate(f(v))g(v)(1+4v^2)^(-m) dv,
    D=d/dv, J=-iD, u=-1/2+i v,
    alpha=m-1/2, X=vD-alpha I.

Every adjoint, norm, projection, trace and matrix below uses this SAME
positive pairing and full carrier, including the odd top degree. Pi is
its orthogonal projection from the ambient weighted L2 space to V, and
Q=I-Pi. Formulas involving X outside V are used only on the explicit
rational/polynomial domain specified below. No Student m is replaced by
m+1 or m+2.

The first exact accepted input is A's finite gauge/metric whole:

    repository awdawmip/enterprise-math
    Source eea5c7884f0d68acc5f9a358c4223a2dea2aba26
    research_notes/owner_goal_20261016/
    parity_actual_student_metric_distortion_feasibility_7cda51/
    ACTUAL_STUDENT_FINITE_GAUGE_AND_METRIC_DISTORTION_AUTHOR_FEASIBILITY.md
    14021 UTF8 bytes
    SHA256 0c34814d56fa6578dd5807f2ebb8cf5dd16b63f424c8be02ae070412e280c502
    Git blob e3ebd9f2ff753a62bcda9e3a1f572683112dd422.

Its genuine 4A peer is

    Source 89c2670a7e9c49811286d563d04117b3d203c142
    research_notes/owner_goal_20261016/reviews/
    parity_student_metric_distortion_nonauthor_4a56e9/
    ACTUAL_STUDENT_METRIC_DISTORTION_COMPLETE_WHOLE_REVIEW_INTERFACE.json
    13701 bytes, Git blob b47b69d218c17437d0da21b9f6710315708ea043.

BFF personally managed-fetched and completely read both immutable bodies,
checked returned Git blobs and immutable URLs, and kept the actual calls
under bff_metric_intake_author and bff_metric_intake_peer. This intake did
not make a new old-input commit/compare call and does not claim one.

The second exact old whole is the accepted wide partial:

    Source 92496320c34767dc1f63b6e18d76170cb6b59f47
    research_notes/owner_goal_20261016/
    parity_actual_lens_full_q_and_ae_obstruction_partial_7cda51_bff6dc/
    PARITY_ACTUAL_LENS_SHADOW_FULL_Q_AND_AE_BOUNDARY_PARTIAL_WHOLE_JOINT_AUTHOR.md
    62848 UTF8 bytes
    SHA256 460c8a0feae8689f7a993b27eb5cd783ca79776b97255337ff54ea4aa2633a87
    Git blob d76850be41fad6fe397d3d5714683f5664034ccb.

Its Part III contains the complete actual Ae compression proof originally
called 8313. It identifies the original finite Ae, after the specified
iota conjugation and ALL original rank corrections, with

    a(v)=1/(1+4v^2),
    B=Pi a Pi,
    Ae=8 Pi a^2 Pi-4B.                                (1)

The old two true peer Sources are
43f967f750443f688a0c421aae1252f0f576341b and
c07678e240aace68ec3bc4a9493c5fffa69e5a0a. BFF was a genuine author of
the old whole, personally consumed its complete final text and deltas,
then personally closed original author3 plus both peer pairs, seven
Sources/222618 bytes. This is honest reuse of that history, not a new
readback or somebody else's API. The old wide quantitative Ae/Psi HOLD
is retained. We do not replace (1) by a bare unconjugated form.

## 2. The actual signed kernel and the precise new question

The original matrix and finite gauge are

    Z=Z_lambda=uJ-alpha I+gamma_lambda(J)=X+C_lambda(J),
    gamma_lambda(J)=[exp(lambda J)f(lambda J)^(-1)-I]/lambda,
    f(t)=(exp(t)-1)/t,
    C_lambda(J)=gamma_lambda(J)-J/2.

At lambda=0 all expressions are removable finite expressions.
C_lambda is an even real-coefficient nilpotent polynomial. With the
Bernoulli coefficients defined by t/(exp(t)-1),

    C_lambda(J)=sum_(k=1)^(floor(N/2))
                B_(2k)lambda^(2k-1)J^(2k)/(2k)!,
    T=exp(sum_(k=1)^(floor(N/2))
                B_(2k)lambda^(2k-1)J^(2k)/[2k(2k)!]),
    Z=T X T^(-1).

Let B_mon be the monomial basis in actual orthonormal coordinates and
S=T B_mon. Then Z=S diag_(j=0)^N(j-alpha) S^(-1).
Define the finite matrix polynomial

    P_z(x)=S diag_(j=0)^N(x^j) S^(-1),
    P_z(1)=I, P_z'(1)=Z+alpha I,
    P_z(exp(s))=exp(alpha s)exp(sZ).                    (2)

For a polynomial matrix, # means coefficientwise actual adjoint, with
the analytic variable unchanged. For REAL y set

    Q_y=P_z#(y)=P_z(y)^dagger,
    K_H(x,y)=tr H[P_z(x),Q_y].                          (3)

The quantitative caller under investigation uses

    m>=2^1000, 64sqrt(m)<=z<=m/256, lambda=pi/z,
    1<=x,y<=exp(1/m).                                  (4)

Identities below make sense already for m>=7; no quantitative claim is
thereby extended below (4). The letter C_lambda is the actual large
matrix correction, not a scalar constant or the unrelated linear
coefficient Cstar in the original Psi.

For the literal normalized full matrix V=Z/A_n and U=V+V^dagger,

    tr Ae[V,U]=A_n^(-2)tr Ae[Z,Z^dagger],
    partial_x partial_y K_Ae(1,1)=tr Ae[Z,Z^dagger].     (5)

These equalities use the COMPLETE actual Z: its baseline, zeta and all
cross terms are present. Any return to an unnormalized caller must keep
the original quadratic raw c^2 and linear raw c factors separately.
The original Psi term -4tau L_c(u)tr(Ae U) remains a separate obligation;
L_c is not the positive shadow reference.

For orientation only, a sufficient finite certificate would be a signed
kernel bound relative to the appropriate real shadow reference L_sh(z).
The scalar endpoint argument in the separate semigroup proof gives

    |partial_x partial_y K_Ae(1,1)|
       <=4m^2 N^4 sup_square |K_Ae|
       <=4m^6 sup_square |K_Ae|.                       (6)

Thus sup |K_Ae|<=C m^(-4) A_n^2 L_sh(z) would suffice for an O(m^2 L_sh)
bound in (5). This is ONLY one sufficient reference certificate; it is
not necessary, is not paid here, and does not settle the physical
complex-lens continuation or the original Psi linear term. A generic
unweighted estimate merely gives a multiple of m times the square of
the very large semigroup envelope and does not supply signed cancellation.

## 3. Integration by parts and the exact rank-two leakage

Write rho=(1+4v^2)^(-m). Since rho'/rho=-8mv/(1+4v^2),
the formal adjoint of vD-alpha on the rational/polynomial domain is

    X^dagger_formal=-vD-1-alpha-v rho'/rho
                   =-X-2ma.                           (7)

Indeed 2alpha=2m-1 and
-1-2alpha+8mv^2/(1+4v^2)=-2m/(1+4v^2).
Compressing (7) to V gives the ACTUAL finite adjoint

    X^dagger=-X-2mB.                                   (8)

All integrations used here are between vectors in V or aV, and their
images under X. A vector in V grows at most |v|^(m-2);
multiplication by a lowers the growth by two powers. The boundary terms
in the one integration by parts are bounded by a polynomial power times
rho and tend to zero at both infinities. These rational functions and
their X images are in the original weighted L2 space. We are not
asserting an unqualified adjoint-domain identity on the entire ambient
unbounded operator.

Set

    R_a=Pi a Q a Pi=(QaPi)^dagger(QaPi).                (9)

Since X V is contained in V, QXPi=0. Taking adjoints using the domain
just checked, and then multiplying by aPi, gives

    Pi X Q a Pi=-2m Pi a Q a Pi=-2m R_a.               (10)

For clarity, Pi X^dagger_formal Q=0 follows from QXPi=0;
using (7) therefore yields Pi X Q=-2m Pi a Q on the
particular Q a V domain. No vanished boundary term is being assumed.

The positive R_a has EXACT rank two. Polynomial division gives, for
each f in V,

    a f=p(v)+[b_0+b_1 v]/(1+4v^2),

with p in V. Hence QaV is contained in span{Qa,Q(va)}.
If a(b_0+b_1v) belonged to V, the degree-at-most-one numerator would
be divisible by the degree-two denominator, so both coefficients
would vanish. Thus these two quotient classes are independent,
rank(QaPi)=2, and rank R_a=2. This is a leakage statement: it does not
say that Ae, F, Z or their kernels have rank two, or that Ae is PSD.

The scalar derivative identity

    v a'(v)=2a(v)^2-2a(v)

and (10) now give, with all products correctly compressed,

    Pi[X,a]Pi=[X,B]-2mR_a=2Pi a^2 Pi-2B,
    [X,B]=2(Pi a^2 Pi-B)+2mR_a,
    Ae=4[X,B]+4B-8mR_a.                              (11)

In particular the last boundary term has NEGATIVE coefficient -8m.
Dropping it would change the actual original Ae.

## 4. Exact scaled-C identities for the whole signed kernel

The original relation [Z,J]=-J implies

    P_z(x)J=x^(-1)J P_z(x),
    P_z(x)C_lambda(J)=C_lambda(x^(-1)J)P_z(x).          (12)

For real y>0, taking the actual adjoint gives

    C_lambda(J)^dagger Q_y
       =Q_y C_lambda(y^(-1)J^dagger).                 (13)

There is no coefficient conjugation ambiguity because C_lambda has
real coefficients at the real physical lambda in (4).
Also P_z(x) commutes with Z and Q_y commutes with Z^dagger, whence
finite trace cyclicity gives

    tr Z[P_z,Q_y]=0, tr Z^dagger[P_z,Q_y]=0.           (14)

Adding the two identities, using X+X^dagger=-2mB, gives
2mK_B=tr(C_lambda+C_lambda^dagger)[P_z,Q_y].
Use (12)-(13) to move the second product in each trace. With

    Delta_x C=C_lambda(J)-C_lambda(x^(-1)J),
    Delta_y C^dagger=
       C_lambda(J)^dagger-C_lambda(y^(-1)J^dagger),

the resulting exact identity is

    2m K_B(x,y)=tr{[Delta_x C+Delta_y C^dagger]P_z(x)Q_y}.   (15)

The WHOLE bracketed matrix, followed in order by P_z and Q_y, is
inside the trace. This is not scalar tr(Delta C) multiplied by a matrix,
nor a pointwise positivity claim about the signed kernel.

At lambda=0, C_0=0, so (15) gives K_B=0. That is a separate removable
finite special case, not a quantitative conclusion for lambda=pi/z>0.

Finally tr[X,B]W=tr B[W,X] for finite W. Applying (11) to (3) yields

    K_Ae(x,y)
      =4 tr B[[P_z(x),Q_y],X]
         +4 K_B(x,y)-8m K_Ra(x,y).                    (16)

This is the new Ward reduction with its true nested commutator and
rank-two leakage. Neither of those signed terms has been deleted or
controlled by a probability interpretation.

## 5. A real actual-norm obstruction to one shortcut, and the kill

There is a useful check on what (15) can legitimately mean.
Multiplication by a is a positive contraction, hence 0<=B<=I.
In a degree-ordered actual orthonormal Student basis, X is triangular
with diagonal j-alpha. Write X=D_0+T_0 with T_0 strictly triangular.
By (8), the Hermitian part is -mB. Therefore

    ||(X+X^dagger)/2||_HS^2
      =sum_j(j-alpha)^2+(1/2)||T_0||_HS^2
      <=m^2(m-1).

Since max_j|j-alpha|<m, it follows that

    ||X||<=m+sqrt(2)m sqrt(m-1)<3m^(3/2).              (17)

The exact accepted raw lower bound in the same model and domain (4)
gives, with n the largest even integer <=m-2,

    ||Z||>=2^(4m-7)/m^(3/2).

The giant threshold in (4) easily pays the subtraction of (17), giving

    ||C_lambda(J)||=||Z-X||
          >=2^(4m-8)/m^(3/2).                        (18)

A small scalar symbol, or small positive lambda by itself, therefore
does NOT imply a mild actual operator C_lambda(J) in the original
Student norm. This specifically rules out that shortcut to estimating
(15). It does not rule out a better estimate for Delta C, signed trace
cancellation, the nested term, or R_a relative to a real reference.
It is NOT a no-go theorem for K_Ae, Ae, Psi or coefficients.

The finite identities (11),(15),(16) are the closed author output.
A new quantitative estimate for the nested B term and the rank-two
signed kernel relative to the physical real/complex reference is still
missing. Applying generic HS/CS at this point would just reproduce the
old unwanted loss. The present bounded trial therefore stops at

    EXACT_FINITE_WARD_IDENTITIES
    / HOLD_MISSING_SIGNED_NESTED_AND_RANK_TWO_REFERENCE_CONTROL.

No optimization of the same generic loss, no new norm, and no assertion
that the sufficient certificate in Section2 is necessary is made.
The full Psi linear term, physical complex lens, raw c^2/c restoration,
and all old quantitative HOLD boundaries remain untouched.

## 6. Temporary independent review, real history and artifact status

BFF first developed and supplied the complete Ward argument as chat-only
hand mathematics. At that time no durable Ward artifact, pin, Source or
final context existed. BFF's new construction history is NONZERO.
Root then asked CF about this precise NEW Ward scope BEFORE giving its
formula or proof. CF disclosed zero new body/formula, internal candidate,
construction or repair; title/theme metadata was NONZERO, and old
Student, Green signed-prefix, rank-two and V1/V2 review history stayed
warm. CF is not described as globally blind or as a new author.

One actual old-reading correction must be kept: Root explicitly confirmed
CF's real complete old wide62848/PartIII8313 reading, correcting the
earlier overly narrow description of that old reading. CF reused that
genuine history and his current full14021 reading, with zero additional
old-primary API or commit/compare calls for this review. BFF does not
borrow CF's observation as BFF's own API.

CF independently checked the complete Ward chat and its domain/branch
notes. The entire temporary outcome received and accurately acknowledged
by BFF was:

    ARGUMENT_ONLY_PASS_BOUNDED_EXACT_IDENTITIES_WITH_QUANTITATIVE_HOLD_
    PENDING_ARTIFACT_SOURCE_FINAL_CONTEXT,
    0 identified mathematical must-fix / 0 construction or repair.

The review explicitly checked the original rho IBP, the rational domain
V+aV, QXPi=0, the negative -8mR_a term, polynomial-division rank two,
both trace-Z zeros, scaled-C matrix order, the positive nested sign,
and the actual C norm obstruction. It explicitly retained the unpaid
nested/R_a relative bounds and did not call the norm obstruction a
no-go for cancellation. The lambda=0 finite case was not extrapolated.

No reviewer repair or proof patch was supplied, and the original
Student V1/V2 arguments and reviews were not revised because of this
Ward opinion. This first durable Ward text records those same finite
arguments and their exact quantitative HOLD. CF's temporary chat
opinion is NOT prefilled as a review of this newly written artifact,
new actual Source or final context. Any future final whole review
must receive and read the real artifact and bind its actual Source.

Persistence here is prose plus necessary file metadata only. No
scientific program, numerical sample, enumeration, new search, Native
execution, formal Task, helper, RA, identity or budget reset was used.
No Source permission follows from this local write. Root contributes
control coordination, not a mathematical vote.

