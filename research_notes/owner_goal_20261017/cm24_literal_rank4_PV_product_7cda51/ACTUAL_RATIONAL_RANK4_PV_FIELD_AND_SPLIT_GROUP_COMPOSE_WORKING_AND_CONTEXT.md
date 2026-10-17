# Actual Picard–Vessiot field and group of the fixed rational rank-four extension

LOCAL AUTHOR WORKING / AUTHOR-PROVED / UNREVIEWED.
Same-family RESULT_ONLY COMPOSE appendix for the existing literal W.
Sole new construction and proof: EM-PUBLIC-7CDA51 (A).
This is a bounded application of classical Picard–Vessiot theory and
algebraic-group facts to an already fixed actual carrier. It is not a new
general Tool, independent principal paper, weak-R statement or old Task closure.
Root supplies CONTROL/routing and zero mathematical construction/votes.

## 1. The original field, row matrix and exact output

Keep the original characteristic-zero field K=Frac(W(k)), with the original
allowed p congruent to13 or19 modulo24. Put F=K(r), with derivation d/dr.
No replacement of this constant field by the complex numbers is made.

Use the exact original ROW connection

 S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
 D=(2P)^(-1)[[2S-1,1],[4S-5,-2S+1]],
 V=F^(1x2), nabla(v)=v'+vD.                                  (1)

The actual accepted self-extension is

 omega=1/(r-1), D4=[[D,omega I2],[0,D]],
 W=F^(1x4), nabla4(u,v)=(u'+uD,v'+vD+omega u),
 i(v)=(0,v), pi(u,v)=u.                                      (2)

In particular the scalar pole is r=1, NOT an invented dr/r at a new
deleted point. The original ring K[r,f^-1,q^-1] contains omega.
Both occurrences of D, all block positions, i and pi are literal.

Here is the proposed new bounded conclusion. The system has an explicit
formal Picard–Vessiot realization over this SAME F with constants K.
For the normalized formal horizontal matrix Y of V at the ordinary point
r=0, and the formal scalar T specified below, its actual field is

 E_W=E_V(T),        E_V=F(Y_ij),                              (3)

and T is transcendental over E_V. With COLUMN coordinates relative to
the displayed basis of horizontal ROWS, its group scheme over K is

 Gal_D(E_W/F)=SL2_K x Ga_K,
 S(g,t)=[[g,0],[-t g,g]].                                   (4)

Here the actual automorphism parameters are sigma(Y)=g^T Y and
sigma(T)=T+t. Its action on Y4 is the constant left multiplier S(g,t)^T;
on the usual column fundamental matrix Y4^T it is right multiplication
by S(g,t). Formula(4) is thus a genuine homomorphism for conventional
automorphism composition, not an unmarked opposite-group convention.
The original ROW connection and its i,pi have not been changed.
Also Gal_D(E_V/F)=SL2_K, represented on these horizontal coordinates.

The extension in(2) remains the original non-split rank2-by-rank2
sequence. A split PRODUCT of algebraic groups in(4) does not mean the
rank-four representation or this module sequence splits.
The conclusions do not identify the old unknown LC/functional caller,
give a weak completion/Frobenius lift, or compute any Student quantity.

## 2. Exactly two accepted literal inputs and the new coverage boundary

The first input is A's original literal W author body:

 Source bf42a27f668c94f94f5ad0add71b20088d279312,
 research_notes/owner_goal_20261017/cm24_literal_rank4_self_extension_7cda51/CM24_LITERAL_RATIONAL_RANK4_SELF_EXTENSION_RESIDUE_COMPOSE_WORKING_AND_CONTEXT.md,
 12072 UTF8B,
 SHA256 ca7f1e584f82d5949ef581259bcca78332b8b85e3cef9ebea86898092b82050c,
 GitOID 09b7cd0ec928607a8ffb1dd600ceede037573e6f.

Its original whole, own immutable author Source and true technical-peer
ordinary unit12072+15819=27891 were actually complete earlier. That history
is honestly reused. This phase A reread the exact original opening and
sections1-4 selected lines1-150 for the actual K, ROW type, matrix, pole,
injection/projection and non-splitting convention. No new full12072
semantic print, old Source API or old compare is claimed in this phase.
Its old proof did not assume rank2 irreducibility or state the PV group.

The second is CF's accepted finite-algebraic-cover no-line body:

 Source 1f951c0fdb92a44f5203d8b03fe7d4e759e6f2ce,
 research_notes/owner_goal_20261016/cm24_algebraic_invariant_line_feasibility_cf1677/CF1677_FIXED_CONNECTION_NO_ALGEBRAIC_INVARIANT_LINE_AUTHOR_WORKING.md,
 16471 UTF8B,
 SHA256 064dc5abb56807e94f4e8b6b19899399bbe7cb938c66f75c1bf45be1ecdfaf01,
 GitOID 364c9fa51eed88ab74476d2c89e45562218639fb.              (5)

It states for ANY constant extension C/K and finite algebraic L/C(r)
that the SAME ROW D has no stable one-dimensional L-line. It explicitly
does not exclude lines over general differential or formal analytic fields.
Its original UNREVIEWED/Sourcepending/old17 status is a creation snapshot;
the later bounded acceptance routed by Root and BFF's real old custody
history are not erased or converted into this author's new peer vote.

This phase A personally obtained the exact full16471 via managed immutable
fetch_file, printed and genuinely read its opening/all7sections/full
context without truncation, and checked actual UTF8/SHA/GitOID/URL.
A did not borrow CF/BFF's semantic read or API. CF first supplied only
the exact40 Source with other locator fields UNKNOWN. One targeted actual
REST commit response identified its SINGLE added path/OID and sole parent
693cfc169ebe6c81b779d1efb587aec406c07dfc; then the actual full file was
fetched at that Source. No broad directory/catalog search was used.
No separate old commit-compare API or old peer-body whole is claimed.
The two nested13905/9610 antecedents in(5) were NOT newly whole-read by A;
the accepted16471 contract, with its full proof personally read, is used.

Occupation/coverage was checked before writing this new proof:
BFF's fixed11686 covers horizontal F-linear End/Aut/indecomposability,
not the full PV group/field, and BFF does not occupy this new scope.
CF's old4510 rank2 PV feasibility stopped at REUSE/no literal consumer;
it did NOT accept PV=SL2 and did not supply this actual W consumer.
Both responses are bounded personal metadata, not global-library absence.
Neither11686 nor4510 is a logical proof input here. Only(1),(2),(5)
and the classical methods explicitly used below are needed.

## 3. A concrete PV realization without changing the constant field

The point r=0 is ordinary: P(0)=-1, and omega(0)=-1.
Write the rational D in its actual formal Taylor series at0.
There is a unique Y in GL2(K[[r]]) satisfying

 Y'=-YD,                 Y(0)=I2.                           (6)

Indeed the coefficient of r^j determines Y_(j+1) by division by j+1;
every nonzero integer is invertible in K. This is formal algebra,
not an assertion of a p-adic convergence radius or integral denominators.
The determinant differential equation and trD=0 give detY=1.

Define the actual formal primitive

 T=log(1-r)=-sum_(j>=1)r^j/j in rK[[r]],
 T'=1/(r-1)=omega,          T(0)=0.                          (7)

Only this formal power series is meant, not a branch of a physical or
complex logarithm. In particular no primitive in the old weak ring is
being asserted. Put

 Y4=[[Y,-T Y],[0,Y]].                                       (8)

Direct block differentiation using(6),(7) gives Y4'=-Y4 D4 and Y4(0)=I4.
For its upper-right block B=-TY, specifically,

 B'=-omega Y+T YD=-omega Y-BD.

This checks the minus sign, the ROW equation and the exact original
upper-right omega block. Also detY4=(detY)^2=1.

Set E_V=F(Y_ij) and E_W=F((Y4)_ab), as actual subfields of K((r)).
A Laurent series in characteristic zero has derivative0 exactly when
only its constant coefficient remains. Therefore

 Const(K((r)))=K,       Const(E_V)=Const(E_W)=K.             (9)

The fields are generated by entries of an invertible fundamental matrix,
with no new constants. They are actual Picard–Vessiot extensions in the
usual characteristic-zero sense, rather than abstract conjectural PV
objects over a possibly non-algebraically-closed constant field.
The associated simple PV rings are the fundamental-matrix rings
F[Y_ij,detY^-1] and F[(Y4)_ab,detY4^-1]. The transpose matrices
Y^T and Y4^T solve the conventional column systems U'= -D^T U and
U4'= -D4^T U4, and generate exactly these same rings. This only records
the coordinate convention of the original horizontal rows.
We use the standard PV correspondence, restriction to PV subextensions
and constant-field base-change theorem in their classical form.

## 4. Why passing to algebraically closed constants loses no actual type

Let Kbar be an algebraic closure of K, carrying zero derivation.
This is a proof base change, not a replacement of the original K in
the definition of W or in the conclusion(4).

For either E=E_V or E_W, an element algebraic over K has derivative0:
differentiate its separable minimal polynomial over K. By(9) it belongs
to K. Thus K is relatively algebraically closed in the finitely generated
characteristic-zero field E. The extension E/K is regular; in particular
E is linearly disjoint from every finite algebraic K'/K.

Moreover Const(EK')=K'. To see this directly, take a K-basis b_j of K'
and write any element as sum e_j b_j with e_j in E. Linear disjointness
makes the b_j E-linearly independent. Derivative0 gives e_j'=0 for every
j, hence e_j in K by(9). The union over finite K' proves

 Const(E Kbar)=Kbar.                                       (10)

Consequently these actual PV extensions base change to the corresponding
PV extensions over Kbar(r), and their group schemes base change over K
as well. Equality of closed subgroup schemes after the faithfully flat
extension Kbar/K will imply equality over the ORIGINAL K.
No embedding of the p-adic field into the complex numbers is required.

## 5. Deriving SL2 from the actual finite-cover no-line input

Work first over Kbar. Let G2 be the PV group of E_V Kbar/Kbar(r).
Since detY=1, it is a closed subgroup of SL2_Kbar.

Suppose G2 were proper. Its identity component G2^0 then has Lie algebra
a proper subalgebra of sl2, hence dimension at most2. Every Lie algebra of
dimension at most2 is solvable. In characteristic zero the connected
linear algebraic group G2^0 is therefore solvable. The classical
Lie–Kolchin theorem supplies a common invariant line in its two-dimensional
horizontal COLUMN-coordinate representation relative to its row basis.
This also covers G2^0={1}.
If the identity component had dimension3 instead, it would equal SL2
and G2 could not have been proper.

Here is the exact algebraic-cover consequence, not the unsupported
shortcut 'irreducible implies SL2'. The fixed field

 F'= (E_V Kbar)^(G2^0)

is finite algebraic over Kbar(r), because G2/G2^0 is finite.
For a nonzero constant column c spanning that invariant line, h=c^T Y is
horizontal. Under G2^0 it changes by a scalar, so its projective
coordinate h2/h1 belongs to F' whenever h1 is nonzero.
If h1=0 identically, the line is already the rational second axis.
In either chart a generator with entries in F' spans a line stable for
the SAME connection d/dr+right D. This is forbidden by(5) with
C=Kbar and L=F'. Thus G2 is not proper:

 G2=SL2_Kbar, and by(10)/faithful descent,
 Gal_D(E_V/F)=SL2_K.                                       (11)

This reasoning uses no scalar-End premise. It handles finite groups,
imprimitive finite components and every proper connected subgroup;
rational irreducibility alone would not have been enough.

## 6. Exact field recovery and the genuinely new additive primitive

First T is not algebraic over F. If it were algebraic in a finite
extension H/F of degree d, the derivation commutes with the field trace.
Taking trace in T'=omega would give a rational h=Tr_(H/F)(T) with

 h'=d/(r-1).

The derivative of a rational function has residue0 at r=1, whereas the
right side has residue d, nonzero in characteristic zero. This is impossible.
Thus F(T)/F is the standard additive PV extension, with group Ga_K.

All entries of(8) belong to E_V(T). Conversely its diagonal blocks give
every entry of Y, and its actual upper-right block B gives

 T=-(1/2)tr(BY^-1).                                        (12)

Therefore E_W=E_V(T) as claimed in(3), with no missing 'field recovery'
assumption. This is the original literal matrix, not merely an abstract
tensor/log construction with unidentified injection/projection.
It remains to prove T is transcendental even over E_V; that is not
inferred just from its transcendence over F or the old non-split sequence.

## 7. The full group: projections, mixed dependence and the exact block action

For any differential automorphism sigma of E_W fixing F, equations(6),(9)
give sigma(Y)=g_sigma^T Y with constant g_sigma and detg_sigma=1.
Similarly sigma(T)=T+t_sigma. We use composition sigma*tau=sigma o tau.
Constants are fixed, so the order is explicitly

 sigma(tau(Y))=g_tau^T g_sigma^T Y=(g_sigma g_tau)^T Y,
 sigma(tau(T))=T+t_sigma+t_tau.

Thus sigma |-> (g_sigma,t_sigma) is a homomorphism. The same identities
represent the group functor over constant-field algebras. In the basis(8),

 sigma(Y4)=S(g,t)^T Y4, sigma(Y4^T)=Y4^T S(g,t),
 S(g,t)=[[g,0],[-t g,g]].                                  (13)

This is a faithful closed subgroup H of SL2_K x Ga_K: the field E_W is
generated by Y and T, so the two actions together lose no automorphism.
Its projections onto both factors are surjective, because E_V and F(T)
are actual PV subextensions, with groups(11) and Ga respectively.
No linear-disjointness assertion has been assumed to reach this point.

Base change H to Kbar and let h be its Lie algebra. The two projection
maps remain surjective, including on Lie algebras in characteristic zero.
The bracket in sl2 plus the central one-dimensional additive factor gives

 [h,h] subset sl2 x {0}.

Its first projection is all sl2, because [sl2,sl2]=sl2: for the usual
e,f,h0, one has [e,f]=h0, [h0,e]=2e, [h0,f]=-2f.
Hence sl2 x {0} is contained in h. Surjectivity to the additive factor
then supplies {0} x Lie(Ga) too. Thus

 h=sl2 directsum Lie(Ga).

A closed subgroup with this full Lie algebra has the same dimension
as the connected group SL2_Kbar x Ga_Kbar, and must be the whole group.
Faithful descent in section4 now gives H=SL2_K x Ga_K over the original
K, with the actual faithful matrix representation(13).

The multiplication is explicitly
S(g,t)S(h,u)=S(gh,t+u), where S(g,t)=[[g,0],[-tg,g]].
The untransposed left multipliers on Y4 occur in the reverse order,
as their covariance requires; they are not mislabeled a homomorphism.
This checks the sign, composition order and central additive factor.
It is not an unproved semidirect action or a quotient by an unidentified
finite subgroup. This completes(4).

In particular the kernel of restriction to E_V is the full Ga. If T
were algebraic over E_V, that kernel would have dimension0. Therefore T
is transcendental over E_V. Equivalently,

 E_W=E_V(T) is a rational one-variable extension of E_V,
 trdeg_F(E_V)=3,        trdeg_F(E_W)=4.                     (14)

The last equalities are the usual PV dimension theorem applied to the
actual groups just computed. They are not assumptions on the formal
coefficients or a numerical computation.

## 8. What this actual carrier supplies and what it does not

The old standard rank2 PV sketch had no identified literal rank4 consumer
and was correctly stopped at REUSE. The accepted actual W now provides
such an object, and(3),(4),(8),(12)-(14) supply its full field and group
with the original matrices and sequence. This is a concrete same-family
classical input, not a claim of a new general PV classification.

The group is a direct product, while the four-dimensional representation
has the nontrivial additive block. Its unipotent radical is Ga, its
reductive quotient is SL2, and its additive translations act nontrivially.
In particular nothing here splits the fixed module sequence, contradicts
the old residue obstruction, or replaces W by a rank3 extension of a
trivial line. BFF's prior End/Aut/indecomposability result is retained,
not re-voted or used as a premise of(4).

There is no assertion about a weak overconvergent PV field, integral
denominators, Frobenius/sigma lift, p-curvature, functional comparison,
LC/hdiv or an unidentified original rank4 Task. The formal K((r)) used
here is a differential extension, not a finite algebraic cover. Its
horizontal rows do not contradict(5). It is also not claimed to lie in
the old dagger ring. Native axes, observations and physical time are
unchanged and are not identified with r or the formal series parameter.

## 9. Actual work history, kill gate and complete creation context

The old accepted W body and the one newly whole-read16471 body are the
only mathematical inputs. No new library search, external classical
primary, scientific program, solver, sampling, code evaluation of the
connection, Native operation or query budget was used.
Administrative JSON/UTF8/hash and managed exact Source reads are distinct
from the hand proof above.

The original bounded gate was to distinguish an actual PV classification
of this W, with a recoverable primitive and original coefficient field,
from a generic SL2 slogan or another missing-carrier label.
The affirmative chain above passes that gate at AUTHOR-PROOF level.
If the accepted finite-cover contract did not concern this SAME row D,
if the original K or block pole were changed, if a new constant entered
the chosen fields, or if(12) failed, the claimed actual conclusion would
be HOLD, rather than repaired by invoking an unrelated weak-R theorem.
If an existing frozen same-W PV classification already covered(4), this
would be REUSE and no new artifact would be needed. The bounded coverage
responses did not identify one; they were not an all-library novelty claim.

A's internal derivation/construct history is NONZERO. The exact old
omega=1/(r-1) and ROW convention were selected-reread from A's original
accepted W before this proof was written; no new pole or matrix was
introduced. This is not an independent review of A's own result.
A truly entire-read the first-written body before any freeze and caught
a ROW/PV composition-order error in the new action parameterization.
The initial actual bytes are preserved. A corrected the new coordinate
representation to S(g,t), explicitly computed both composition orders,
and kept the literal D4/field/recovery proof unchanged. This is one
author self-correction, with zero external construction or repair.
The complete actual delta and final actual whole reading are external
observations, not presumed by this history paragraph.
BFF/CF only supplied existing coverage and exact Source metadata, not
new construction or repair. Root supplied no proof or mathematical vote.

4A is preparing the future NONBLIND technical whole under Root's route.
He disclosed generic representation/private associations NONZERO,
no new body read and0 actual participation in this new author construction
or repair at the prebody cut. Before this write A supplied him only the
two OLD exact input tuples/contracts, no unfinished new PV formulas.
A future independent technical verdict and actual author Source binding
must be genuinely completed; they are not presumed here.

Creation status: AUTHOR-PROVED_UNREVIEWED_RESULT_ONLY_COMPOSE_APPENDIX.
The actual written file still must be genuinely self-whole-read and
externally fixed once. No selfreading, final byte pin, independent PASS,
future Source, oldTask closure or event is recursively filled into this
creation text.

Canonical A remains EM-PUBLIC-7CDA51,
SID MCP-9030ae3a22074e3dbc31679b7090f6b0,
RA-6665DBCD10BC1C3E4DED3C04, current53/200, Goal OPEN.
All old STOP/HOLD/UNKNOWN and budgets remain. No helper54, main write,
new formal Task, science program, Native execution or identity is authorized.

Global-Knowledge-Sync: main@67a02007 / GLOBAL_KNOWLEDGE_V1

