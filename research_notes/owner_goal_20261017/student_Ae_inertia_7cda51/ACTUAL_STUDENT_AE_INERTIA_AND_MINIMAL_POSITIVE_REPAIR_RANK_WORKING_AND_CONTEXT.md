# Actual Student Ae inertia and the minimum rank of a positive repair

Status at creation: LOCAL_AUTHOR_WORKING_COMPLETE_UNREVIEWED.
Same-family finite RESULT_ONLY / COMPOSE feasibility, not a new general Tool
or paper-count claim. Sole new mathematical author: A / EM-PUBLIC-7CDA51.
Root supplies control and zero mathematical vote. No new proof, formula or
constructive repair was requested from BFF, CF or 4A.

## 1. Exact finite question, discriminator and result

For every integer m>=7 retain the ORIGINAL actual carrier

 V=C[v]_(degree<=m-2),       dim(V)=m-1,
 rho_m(v)=(1+4v^2)^(-m),
 <f,g>_m=integral_R conjugate(f(v)) g(v) rho_m(v) dv.

Let Pi be the genuine orthogonal projection onto this V and let the actual
self-adjoint operator be

 Ae=Pi a(v) Pi,
 a(v)=(1/4-v^2)/(v^2+1/4)^2
     =8/(1+4v^2)^2-4/(1+4v^2).                         (I1)

The finite question is whether the negative part could be confined to a
uniformly bounded-rank exception. The exact answer is

 inertia(Ae)=(n_plus,n_minus,n_zero)
            =(ceil(m/2), floor(m/2)-1, 0).             (I2)

Here inertia means the inertia of the Hermitian quadratic form in the
ORIGINAL positive Student pairing. In particular Ae has full rank m-1.

For positive semidefinite operators C on the same actual V,

 min{rank(C): C>=0 and Ae+C>=0}=floor(m/2)-1.            (I3)

Thus an O(1)-rank positive repair, uniform in m, cannot absorb the entire
negative part. This conclusion kills ONLY that stated method. It is not
an obstruction to the actual signed trace, a quantitative Ae-prefix
bound, fullPsi, coefficient positivity, a different indefinite method or
the original Goal. No eigenvalue magnitude or condition-number estimate
is claimed.

The proof uses one new finite congruence to a path quadratic form with two
explicit constraints. The congruence is not unitary. Its path eigenvalues
are NOT asserted to be the actual Ae eigenvalues. A larger polynomial
space appears only as an auxiliary integrable SIGNED FORM used to compute
a restriction; it is not substituted for V or for the original Student
energy.

## 2. Necessary accepted interface, coverage and actual reading history

The sole necessary accepted model input is the actual-m Ae interface

 Source 878066668ccca45e66b8791833eaa0ce85ba26d3,
 repository awdawmip/enterprise-math,
 research_notes/owner_goal_20261016/
 parity_actual_Ae_pole_cut_prefix_feasibility_7cda51/
 ACTUAL_STUDENT_AE_PARITY_CUT_POLE_FACTORS_AND_FULL_TRACE_PREFIX_FEASIBILITY.md,
 17239 UTF8 bytes,
 SHA256 1c42dee3c1ebba1cdbac1b1e5ae7a5f21082043930343645b0dbdd73dd275241,
 Git blob 55f675dcf64b9edd5d969f2de5f7daef97f113b9.

Only its literal carrier/pairing and (A1), reproduced as(I1), are premises.
Its full body was already A's actual mathematical author responsibility;
the genuine BFF whole peer at Source
78643ff20f70e4f235f5dc55982e05a6a846412f and A's ordinary two-Source
closure remain their historical facts, not another vote on this new
inertia result.

During this new direction selection A made one precise managed
github_fetch_file at the above immutable author Source/path, received
the complete17239 body, checked returned GitOID and immutable URL, and
genuinely displayed/read the whole seven sections in one untruncated
output. The entire real caller is held as
next_direction_actual_accepted_Ae_interface in functions.store.
No new old-input commit/compare is claimed. The old review was not
fetched or reprinted in this phase.

Finite coverage: that17239 proves exact rank-two separated cuts in each
parity, entrywise positivity in an orthogonal sign convention, one positive
and one negative Rayleigh direction, and the exact signed-prefix caller.
It does not give complete inertia, nonsingularity, or(I3). The earlier
metric14021 kills a bounded-condition positive spectral reduction of Z;
it is not a premise here. Accepted Student semigroup19646/19190 were
genuinely consumed just before this direction, but supply no formula or
logical premise to(I2). Its integer-dilation diagnostic is a separate
completed COMPOSE reuse and is not extended here.

Classical finite Fourier orthogonality, the elementary spectrum of a path,
Hermitian congruence and the finite spectral theorem are explicitly reused
below. The new work is their full original-Ae restriction and the actual
finite sign computation. No broad catalogue/library search or new
scientific program was used.

## 3. An exact congruence, with the actual carrier as two constraints

Put y=2v and F(y)=f(y/2). Direct substitution in(I1) gives

 <f,Ae f>_m
  =2 integral_R (1-y^2)|F(y)|^2(1+y^2)^(-m-2) dy.      (I4)

Set y=tan(theta), -pi/2<theta<pi/2, and

 g(theta)=cos(theta)^m F(tan(theta)).

Since dy=cos(theta)^(-2)dtheta and
1-tan(theta)^2=cos(2theta)/cos(theta)^2, (I4) becomes

 <f,Ae f>_m
  =2 integral_(-pi/2)^(pi/2) cos(2theta)|g(theta)|^2 dtheta.
                                                              (I5)

For the next linear-algebra calculation ONLY, first allow auxiliary
polynomials F of degree at most m. The signed integral(I4) is still
absolutely convergent: its worst tail is O(y^(-2)).
We do NOT assign those extra two degrees the original rho_m norm.
They are not an enlarged actual Student carrier.

The homogeneous trigonometric monomials
sin(theta)^j cos(theta)^(m-j), j=0,...,m, span exactly

 g(theta)=sum_(j=0)^m x_j exp(i(2j-m)theta).             (I6)

This is an invertible complex change of coefficients: replacing sin and
cos by their two exponentials is the invertible homogeneous substitution
in degree m. There are L=m+1 coefficients.

The actual restriction deg(F)<=m-2 is equivalent to g(pi/2)=g'(pi/2)=0.
Indeed for the auxiliary polynomial, those two values recover, up to
nonzero signs, its coefficients of y^m and y^(m-1); all lower terms have
at least two factors cos(theta). In Fourier coordinates define

 c_j=(-1)^j,
 e_j=(j-m/2)(-1)^j,       j=0,...,m,
 K={x in C^L: c^T x=0, e^T x=0}.                       (I7)

Equation(I6) at pi/2 gives the first constraint. Its derivative gives the
second after multiplying by a nonzero scalar. Thus the actual V is
isomorphic to this precise codimension-two K; neither actual top degree
has been silently removed. The other endpoint constraints follow from
g(theta+pi)=(-1)^m g(theta) and are not additional conditions.

Let A_L be the REAL symmetric path matrix of size L with zero diagonal
and (A_L)_(j,j+1)=(A_L)_(j+1,j)=1. Orthogonality of the frequencies on an
interval of length pi gives

 2 integral cos(2theta)|g(theta)|^2 dtheta
       =pi x^* A_L x.                                  (I8)

Only neighbouring indices contribute, each integral being pi/2 before
the factor2 in(I5). Consequently the actual inertia of Ae is EXACTLY
the inertia of A_L restricted to K. The scalar pi is positive.

For completeness the vectors sin((j+1)ell*pi/(L+1)), j=0,...,L-1,
ell=1,...,L, diagonalize A_L, with eigenvalues

 2cos(ell*pi/(L+1)).                                   (I9)

The boundary values at j=-1 and j=L are zero, so the two-neighbour sine
identity proves(I9); distinct cosines and finite symmetry give a complete
basis. We next compute the TWO-CONSTRAINT restriction, not just this
auxiliary full path inertia.

## 4. Odd m: the two actual constraints remove two negative directions

Suppose m is odd. Write L=m+1=2r, so r=(m+1)/2>=4.
By(I9), A_L is invertible and has inertia(r,r,0).
Let h=(L-1)/2, so e_j=(j-h)c_j.

Reflection j->L-1-j commutes with A_L. It sends c to -c and e to e.
It follows that

 c^T A_L^(-1)e=0.                                      (I10)

Both diagonal contractions can be evaluated by a finite recurrence.
For A_L u=c put u_j=(-1)^j w_j and impose w_(-1)=w_L=0.
Then

 w_(j-1)+w_(j+1)=-1,
 w_(2t)=a if t is even, and -1-a if t is odd,
 w_(2t+1)=-1 if t is even, and 0 if t is odd,

where a=0 for even r and a=-1 for odd r. Substitution checks both
boundaries. Summing c_j u_j=w_j gives

 c^T A_L^(-1)c =
   -r                    if r is even,
   -(r+1)                if r is odd.                  (I11)

For A_L u=e the corresponding solution is

 u_j=(-1)^j w_j,
 w_j=-(j-h)/2
     +(L+1)/4 [(-1)^r cos(j*pi/2)+sin(j*pi/2)].        (I12)

The homogeneous terms cancel in w_(j-1)+w_(j+1); the linear part gives
-(j-h). At j=-1 and L the two displayed terms cancel, so(I12) is the
actual unique solution.

The finite square sum is
sum_(j=0)^(L-1)(j-h)^2=L(L^2-1)/12.
For the remaining weighted trigonometric sum in(I12),

 sum (j-h)[(-1)^r cos(j*pi/2)+sin(j*pi/2)]
      =-L if r is even, and 1 if r is odd.

These identities follow by separating even j=2t and odd j=2t+1:
sum_(t=0)^(r-1)(-1)^t is0 or1, and
sum t(-1)^t is -r/2 or(r-1)/2, respectively. Thus

 e^T A_L^(-1)e =
   -L(L^2-1)/24-L(L+1)/4              if r is even,
   -(L+1)(L-3)(L+2)/24                if r is odd.     (I13)

Both are strictly negative for the present L>=8.

The two-dimensional space
U=span{A_L^(-1)c,A_L^(-1)e} therefore has a negative-definite A_L
Gram matrix, by(I10)-(I13). Its A_L-orthogonal complement is exactly K:
pairing x with the two generators gives c^T x and e^T x.
Because U is nondegenerate,

 C^L=U direct_sum_(A_L-orthogonal) K.

This elementary congruence removes two negative directions and none
positive or null. Hence

 inertia(A_L restricted K)=(r,r-2,0)
       =((m+1)/2,(m-3)/2,0),          m odd.            (I14)

No general Schur-complement theorem is being taken without its relevant
nondegeneracy check.

## 5. Even m: retain the zero-mode coupling before the second restriction

Suppose m is even. Write L=m+1=2r+1, r=m/2>=4.
Now A_L has inertia(r,r,1). Its actual one-dimensional kernel is spanned by

 kappa_j=sin((j+1)pi/2),
 kappa_(2t)=(-1)^t,       kappa_(2t+1)=0.              (I15)

Here e_j=(j-r)(-1)^j. Direct alternating sums give

 if r is even: c^T kappa=1,   e^T kappa=0;
 if r is odd:  c^T kappa=0,   e^T kappa=-(r+1).       (I16)

Thus one of the two constraints couples NONTRIVIALLY to the full path
zero mode. It may not be discarded as if A_L were invertible.

If r is even set ell=c,u=e; if r is odd set ell=e,u=c.
Then ell^T kappa is nonzero and u^T kappa=0.
Put K1=ker(ell^T). It is a direct linear complement to span{kappa}.
The kernel is orthogonal to all vectors for the A_L form, so restriction
to K1 has inertia(r,r,0).

Because u is orthogonal to kappa, A_L v=u has a solution. Its contraction
t=u^T v is independent of the chosen solution. A finite recurrence gives

 t=-(r+1)                         if r is odd, u=c;
 t=-r(r+1)(r+2)/3                 if r is even, u=e.   (I17)

Here are explicit checks, including the boundary terms.

For odd r and u=c, again write v_j=(-1)^j w_j with
w_(2t)=a,-1-a alternately and w_(2t+1)=-1,0 alternately.
The boundary at j=L=2r+1 is0 exactly because r is odd; a is free,
representing kappa. The r+1 even positions contribute -(r+1)/2 and the
r odd positions contribute -(r+1)/2, giving the first value in(I17).

For even r and u=e one may use

 w_j=-(j-r)/2 +(r+1)/2 sin(j*pi/2)+a cos(j*pi/2),
 v_j=(-1)^j w_j.

The boundary at -1 vanishes; at L the sine is1 because r is even, so
it vanishes there too. The cosine contribution to u^T v is zero by
u^T kappa=0. The remaining two sums give

 -L(L^2-1)/24 -(r+1)r/2
       =-r(r+1)(r+2)/3,

since L=2r+1. This proves the second contraction in(I17) without choosing
a pseudoinverse or guessing its sign.

Move v along its kernel line to v1 in K1:
v1=v-[ell^T v/(ell^T kappa)]kappa.
Then A_L v1=u and v1^* A_L v1=u^T v=t<0.
For x in K1, its A_L pairing with v1 is u^T x. Therefore imposing the
remaining constraint u^T x=0 removes exactly this nondegenerate negative
direction from K1. The remaining space is the actual K of(I7), whence

 inertia(A_L restricted K)=(r,r-1,0)
       =(m/2,m/2-1,0),               m even.          (I18)

In particular the auxiliary path zero mode creates NO null direction
in actual Ae. The explicit coupling in(I16) and the negative contraction
in(I17) are both necessary for that conclusion.

Equations(I14),(I18), together with the genuine congruence(I4)-(I8),
prove(I2) for the entire original carrier and both m parities.

## 6. Exact minimum positive-repair rank and the limited method kill

Write q=n_minus(Ae)=floor(m/2)-1.
If C>=0 and Ae+C>=0, but rank(C)<q, the actual negative spectral
subspace E_minus of Ae has a nonzero intersection with ker(C).
For a nonzero f in that intersection,

 <f,(Ae+C)f>_m=<f,Ae f>_m<0,

a contradiction. Thus rank(C)>=q. This lower bound even holds for any
Hermitian rank<q additive correction, although PSD is the stated class.

Conversely the classical finite Hermitian spectral theorem in the
ORIGINAL positive pairing defines

 C=sum_(lambda_j<0) (-lambda_j) e_j e_j^dagger,

where the e_j are actual orthonormal Ae eigenvectors. Then C>=0,
rank(C)=q and Ae+C>=0. This is an existence/congruence statement, not an
executed eigenvector calculation. It proves(I3).

Equivalently every decomposition Ae=P-R with P,R>=0 has rank(R)>=q,
and the bound is attainable. Since q grows linearly with m, no fixed
rank r0, independent of m, suffices. The exact thresholds follow from
q=floor(m/2)-1, rather than merely one negative Rayleigh direction.

This does not contradict the older positive GLOBAL rank-two leakage
R_leak or the older rank-two separated cuts: neither was an assertion
that Ae itself is rank two or has a bounded-dimensional negative part.
The new result makes that distinction quantitatively exact in rank.

This result DOES NOT estimate the actual signed weighted-prefix
contractions K(Z), their row-minus-column cancellation, raw quadratic
and linear factors, an off-real analytic form, Ae-weighted fullPsi, or
coefficient margins. It does not show that other low-displacement-rank
methods fail. It excludes only the explicit PSD/additive-rank exception
method, and supplies complete finite inertia as a new exact input.

## 7. Scope, chronology, contributions and execution boundary

The original Student carrier, positive pairing and compressed Ae(I1)
are accepted upstream interfaces with actual A/BFF/CF/4A history. A's
17239 exact-pole/prefix construction and BFF's genuine old review keep
their actual credit. Those old votes do not review this new inertia
construction. The new trigonometric restriction, complete parity
recurrences and minimum-repair application were derived by A alone after
the previous three-duty Source checkpoint53 had genuinely closed.

During the scope selection Root received only author direction/progress,
not a request to supply mathematics. 4A separately asked occupancy of a
CM24 rank3 affine extension; A replied non-occupancy and only the title
metadata that this different Student inertia direction was occupied.
No new inertia formula, working body or repair was sent to 4A, BFF or CF.
No assertion is made about a future reviewer's unobserved private thoughts.
A's own exact new scope construction/candidate history is NONZERO.
Future whole review, if requested, must freshly establish its actual
scope history and consume a complete frozen artifact/Source.

The two signed prefixes of17239 still need their genuine quantitative
input. They are not an external-permission defect, but their missing
bound has not been fabricated here. M7/Native/query STOPs, inaccessible
objects, budgets UNKNOWN, no new identity and all historical
NONBLIND/HOLD/errors retain their literal boundaries.

Current actual actor is the same EM-PUBLIC-7CDA51,
SID MCP-9030ae3a22074e3dbc31679b7090f6b0,
activity RA-6665DBCD10BC1C3E4DED3C04,
canonical53/200 at actual Source
d3fe6c21ce8cdc63113e5cd693d678cbb0d9e6c7.
That already published checkpoint's helper1/CAS1, ownfull7/exact1MOD6ADD,
new Source-bound original startup/sameevent dual0, debt[] and five false
formal flags were genuinely closed before this mathematics resumed.
No extra activity helper54, new Source write or formal Task/Native
authority is inferred. Goal remains OPEN; this is not FINAL permission.

All calculations above are finite hand mathematics. Local code, if used
after composition, is solely prose persistence and necessary artifact
metadata; no matrix generation, arithmetic enumeration, scientific
import, solver, numerical integral or sampling has been performed.

## 8. Author completion and later acceptance boundaries

This file contains the whole proof and context, rather than an extract
requiring unreviewed auxiliary lemmas. The finite path spectrum and the
linear-algebra decompositions used here have their explicit proofs.
No shifted-weight Student energy theorem, condition-number assertion,
generic spectral no-go or unpublished third-party input is a premise.

At this creation cut the actual full-file author self-reading, fixed-byte
freeze, new author Source, genuine peer whole review and any ordinary
reception are NOT prefilled. Actual full-file self-reading and the fixed
byte metadata must occur separately after the prose write. The historical
creation text will then remain unchanged; any later observation belongs
outside this body rather than circularly rewriting the file.

Finite outcome: exact original-Ae signature and minimum PSD repair rank
are supplied at author level; bounded-rank-negative-exception feasibility
is negative. Signed Cauchy-prefix quantitative control, fullPsi and the
original research Goal remain OPEN/HOLD at their existing exact scope.
