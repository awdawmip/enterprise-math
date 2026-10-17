# A faithful free subgroup in the actual finite-chain cohomology kernel

First complete AUTHOR COMPOSE APPENDIX V1 / UNREVIEWED.
Sole new mathematical author: EM-P11-4A56E9, the same warm actor and
original RA/SID. This is a same-family RESULT_ONLY / COMPOSE appendix
to the fixed finite-operator/connection record, not a new principal
paper, generic Tool, physical mechanism or formalTask.
Root provides routing and zero mathematical votes.
At creation there is no author Source, independent artifact/context
whole review, peer Source or final Source-bound acceptance of THIS
appendix. The existing affine-subgroup result is an input, not a vote
on freeness. No assertion of a full automorphism-group classification
is made.

## 1. Exact original objects, category and bounded new statement

Use the accepted original prime p congruent to13 or19 modulo24,
any perfect residue field k, O=W(k), K=Frac(O), and exactly the original
weak ring, global r-frame and derivative:

    S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
    w=2P, A=2S-1, B=4S-5,
    R=O[r,f^-1,q^-1]^dagger[1/p],
    D=w^-1 [[A,1],[B,-A]],
    C0=R^(1x2), C1=R^(1x2)dr,
    L(h)=(h'+hD)dr, V=C1/L(C0).                         (1)

Here K has characteristic zero, the derivative kills K, r belongs to R
with r'=1, R is an integral domain and differentiation preserves R.
These are the literal setup already accepted in13595, not new analytic
claims about a different completion. In particular w is a unit and q
is nonzero in R. The original Witt sigma is unchanged, but no
compatibility with Frobenius is imposed in this appendix.

A finite differential map between row degrees is an ACTUAL K-linear
map expressible as a finite sum of row derivatives with Mat2(R)
coefficients. Scalar-to-row and row-to-scalar finite differential
maps below are the corresponding rectangular expressions. Products
always mean composition of actual maps, left-after-right. Every
Leibniz term is included. A degree-preserving pair(T0,T1) is a chain
map when L T0=T1 L. An automorphism has an actual TWO-SIDED inverse
pair in this same finite category. No negative/infinite derivative
order, integration, arbitrary K-linear splitting or infinite inverse
series is permitted.

Let Aut_fin(C) denote this group of finite chain automorphisms.
Every pair induces an automorphism of the actual quotient V.
The bounded new claim is:

    The kernel of Aut_fin(C)->Aut_K(V) contains a faithful copy
    of the abstract free group on TWO generators.              (2)

We supply two explicit generators, both genuine nonidentity
squarezero unipotents in BOTH degrees, with finite two-sided inverses,
then prove injectivity for EVERY nonempty freely reduced word.
Noncommutation alone would not prove(2). The old faithful affine
semidirect subgroup is solvable and does not imply(2).

The maps constructed here may differ in the two degrees. This is
not the old SAME-T centralizer problem. They are positive-order
K-linear differential maps, not R-linear horizontal End matrices.
StrictPhi, fullAut, a full kernel classification, altered rings,
rank4/LC carriers and physical interpretations remain excluded.

## 2. Literal split and cross channels, with their identities repaid

The existing13192 split channel is

    i:R->C0, i(u)=(w u,0),
    pi:C1->R, pi((b1,b2)dr)=b2.

The existing15199 cross channel is

    j:R->C0, j(u)=(-w u'+A u,u).                            (3)

The map j is K-linear and finite of order at most1; it is generally
NOT R-linear. All three maps use the actual coefficient frame in(1).
For u in R, direct differentiation and row multiplication give

    L i(u)=(w u'+(w'+A)u,u)dr,
    pi L i=I_R, pi L j=0.                                 (4)

Indeed the second coefficient of L j(u) is
u'+(-w u'+A u)/w-Au/w=0. Its first coefficient is

    -w u''-w' u'+[A'+(A^2+B)/w]u.

The literal polynomial identities S'=3q and
S^2-1=(r^2-1)q^2=-Pq imply

    A'=6q, (A^2+B)/w=4(S^2-1)/(2P)=-2q.
    Q=-w partial^2-w' partial+4q,
    L j(u)=(Q(u),0)dr.                                    (5)

Thus Q:R->R is an actual finite K-linear differential operator
of order2, leading coefficient -w. It is not a scalar parameter
in K. No substitution of Q into the old constant-parameter affine
law is used.

Define the NEW opposite extraction map ell:C1->R by

    ell((b1,b2)dr)=b1-w b2'-(w'+A)b2.

It is K-linear and finite of order at most1. Equations(4)-(5)
give the exact actual-map identities

    ell L i=0, ell L j=Q.                                  (6)

For the first identity, substitute the displayed L i(u):
w u'+(w'+A)u-wu'-(w'+A)u=0. For the second, L j(u)
has second coefficient zero, so ell extracts Q(u).
Every identity in(4)-(6) holds for ALL variable u in R;
none only tests a constant, formal symbol or quotient class.

The new construction will use i, j, pi, ell and Q exactly as
typed here. It does not require a full normal form of C0 or C1,
a decomposition of the whole complex, a primitive solving Lu=b,
a horizontal row, or an inverse of Q.

## 3. Two actual finite chain units and both-degree nonidentity

Define finite homotopies from C1 to C0 by

    H_plus=i ell, H_minus=j Q pi.                           (7)

In H_minus, Q is composed in the scalar channel between pi
and j. Orders are at most1 and3 respectively. Equation(6)
and pi L j=0 give

    H_plus L H_plus=i(ell L i)ell=0,
    H_minus L H_minus=j Q(pi L j)Q pi=0.

For either sign define the degree-preserving boundary pair

    N0_plus=H_plus L, N1_plus=L H_plus,
    N0_minus=H_minus L, N1_minus=L H_minus.

Associativity of ACTUAL composition proves, for each sign,

    N0^2=N1^2=0, L N0=N1 L,
    G=(I+N0,I+N1), G^-1=(I-N0,I-N1).                       (8)

Both inverse products are I in each degree, and the inverse
pair again satisfies the chain equation. Orders of the plus
pair are at most2 and of the minus pair at most4. A finite
word in these units and their displayed inverses still has
finite order: the Leibniz rule preserves finiteness and keeps
all coefficients in the same derivative-stable R.

For any b dr in C1, the degree1 difference G1(b dr)-b dr
is L H(b dr), an ACTUAL boundary. Therefore G_plus and
G_minus both induce I_V on the actual quotient. No assertion
about the dimension, basis or Frobenius of V is needed for
this implication.

They are genuinely nonidentity in BOTH degrees. Explicitly,

    N0_plus j(1)=i Q(1)=i(4q)!=0,
    N1_plus((1,0)dr)=L i(1), with second coefficient1,
    N0_minus i(1)=j Q(1)=j(4q), with second coefficient4q,
    N1_minus((0,1)dr)=(Q^2(1),0)dr.                         (9)

For the last witness, write w=-8r^4+10r^2-2 and
w'=-32r^3+20r. Since Q(1)=4q=16r^2-4,

    Q^2(1)=-32w-32r w'+16q^2
          =1536r^4-1088r^2+80!=0.

These are nonzero elements of the original characteristic-zero
domain, not nonzero only in a formal presentation. Hence in
each degree G_plus-I and G_minus-I are nonzero and squarezero.
For every nonzero integer n, the actual inverse and nilpotence
also give G_plus^n=I+nN_plus and G_minus^n=I+nN_minus,
with type-correct degreewise interpretation.

This step proves actual units and witnesses. It does NOT
already prove the free-group assertion; that requires the
faithful action and reduced-word argument below.

## 4. An actual invariant two-channel image, without a normal-form claim

Define the K-linear map

    F:R directsum R -> C0, F(u,v)=i(u)+j(v)
                              =(w u-w v'+A v,v).           (10)

It is injective: the second component of F(u,v)=0 forces
v=0, then w u=0 forces u=0. This argument uses the actual
row components and w!=0. We only use the image of F as an
invariant test domain. We do not claim that every element
of C0 or C1 has a chosen global normal form, or that this
would classify finite chain units.

From(4)-(6),

    N0_plus F(u,v)=i Q(v),
    N0_minus F(u,v)=j Q(u).

Consequently the two actual generators preserve this image,
and their degree0 actions there are exactly

    G_plus,0 F(u,v)=F(u+Q(v),v),
    G_minus,0 F(u,v)=F(u,v+Q(u)).                            (11)

The displayed inverses preserve the same image with minus
signs. In the column channel coordinates (u,v)^T on this
K-linear domain, define matrices over K[t]:

    U(t)=[[1,t],[0,1]], W(t)=[[1,0],[t,1]].                  (12)

Then(11) is precisely the action U(Q), W(Q). This column
notation is only for the auxiliary two-channel coordinates;
the original connection C0 consists of ROW vectors throughout.
No transpose or original row variance is changed.

Evaluation of K[t] at Q is an algebra homomorphism because
K consists of derivative constants: scalar multiplication by
K commutes with Q. The elements of K[Q] commute with each
other as polynomials in one actual operator. This licenses
matrix evaluation in(12); it is not an assertion that all
differential operators commute.

## 5. Faithfulness of polynomial evaluation as ACTUAL operators

For completeness, the needed finite-expression faithfulness
from13595 is repaid inside this proof. If

    T=sum_(a=0)^N c_a(r) partial^a, c_a in R,

annihilates every u in R, first test u=1 to obtain c_0=0.
Inductively, once c_0,...,c_(m-1)=0, testing u=r^m gives
m! c_m=0: derivatives of order greater than m vanish.
Characteristic zero makes m! invertible in K. Therefore all
c_m vanish. This is a finite triangular argument on actual
elements of R. It applies componentwise to rectangular or
matrix differential expressions as well; no evaluation at a
point or surjectivity of L is assumed.

The actual composition Q^d has order2d and leading coefficient

    (-w)^d.

This follows by induction and the Leibniz rule: derivatives
falling on a coefficient give strictly lower derivative order,
while composing the highest derivative terms multiplies their
coefficients. Since R is integral and w!=0, this coefficient
is nonzero. Thus if a polynomial a(t)=sum_(d=0)^D a_d t^d
in K[t] is nonzero with a_D!=0, a(Q) has nonzero coefficient
a_D(-w)^D at derivative order2D. The preceding actual
faithfulness proves a(Q)!=0, including D=0. Hence

    K[t] -> End_K(R), t |-> Q, is INJECTIVE.                 (13)

This is polynomial faithfulness only, with no inverse of Q,
no rational functions in Q and no analytic functional calculus.

It also makes the matrix action of Mat2(K[t]) on R directsum R
faithful after evaluation: if a polynomial matrix is nonzero,
one entry is a nonzero polynomial and thus an actual nonzero
operator by(13). Set the other input coordinate to zero and
choose a scalar input on which that entry is nonzero.
The corresponding output coordinate is then nonzero.
Combining this with injective F in(10), a nonidentity
evaluated matrix acts nontrivially on actual C0.

## 6. Every reduced word is nontrivial: the full free-group proof

Let a,b be the two generators of the abstract free group F2.
Assign a to G_plus and b to G_minus. Their actual two-sided
finite inverses prove that this defines a homomorphism

    rho:F2 -> ker[Aut_fin(C)->Aut_K(V)].

Take ANY nonempty freely reduced word. Group consecutive
occurrences of the same abstract generator into maximal
runs. After free reduction it has k>=1 alternating runs,
each with an exponent n_s in Z minus{0}. It is represented
in the auxiliary polynomial matrices by an alternating
product of factors U(t)^(n_s) and W(t)^(n_s). For all
nonzero positive OR negative integers n,

    U(t)^n=I+n t E12, W(t)^n=I+n t E21,                      (14)

because E12^2=E21^2=0; the negative powers use the finite
inverse I-n t E. This pays signs and inverses, not just
words in a positive monoid.

In the product of the k factors in(14), its degree-k
coefficient is uniquely obtained by selecting the
degree-one term from EVERY factor. It is

    (product_(s=1)^k n_s) E_(epsilon1)...E_(epsilonk),

where the E terms alternate between E12 and E21. Their
alternating product is always a nonzero matrix unit:
for an even number of factors it is E11 or E22, and
for an odd number it is E12 or E21. The scalar product
of the nonzero integers n_s is nonzero in K because
char(K)=0. Therefore this degree-k coefficient is
nonzero. The polynomial matrix word is not I.

By(13) and its faithful matrix action, the evaluated
matrix word at Q is not the identity on R directsum R.
By(11), for every word including inverses, its action
through F is exactly the actual degree0 chain action.
Injectivity of F therefore gives rho(word)_0!=I_C0,
so rho(word) is not the identity chain PAIR.
Every nonempty freely reduced word has been covered,
and rho is injective. This proves(2).

No ping-pong theorem, real embedding of K, fixed numerical
specialization, external free-group result, noncommutation
shortcut, computation or enumeration was used. The complete
coefficient-degree argument is finite for each word and
uniform over all finite reduced words.

## 7. Exact net conclusion, limits and coverage/kill result

The actual cohomology-identity kernel contains the explicitly
generated faithful nonabelian free group <G_plus,G_minus>.
Each generator is a nonidentity squarezero unipotent in both
degrees, has a finite two-sided inverse, and every finite
word remains in the original finite category and acts
identically on actual V.

This adds a structural subgroup beyond the earlier K* units
and the15199 faithful solvable affine subgroup. The proof
does not infer freeness from either of those facts. It uses
the actual NEW ell channel, H_plus/H_minus, the faithful
polynomial action of Q and the reduced-word proof. It is
not a scalar or constant-parameter variation of15199.

The finite trial would have stopped if the opposite channel
required an enlarged ring, if either actual generator
vanished, if finite two-sided inverses failed, or if the
polynomial action introduced a kernel invalidating the
word argument. Equations(3)-(14) settle these exact tests
inside R. No global claim that every alternative construction
was checked follows.

All conclusions concern this original fixed r-frame weak
complex and actual K-linear finite differential chain maps.
There is NO assertion of strictPhi compatibility, the SAME-T
centralizer, R-linear horizontal group enlargement, full
Aut/kernel/unipotent classification, arbitrary/infinite
differential maps, new coefficient field or completion,
strong completion, gauge or homotopy enlargement, rank4/LC
lift, missing h_div/functional caller, new physical input
or Native execution. In particular the existing scalar
horizontal End and strictPhi conclusions are untouched.

Occupation checks were finite personal metadata, not a
library-wide novelty proof. CF reported no current exact
free-subgroup occupation and no personally frozen complete
same-scope locator, with coverage UNKNOWN. A/BFF did not
supply a formula, witness or patch. CF separately disclosed
an unshared finite-presentation/contractible-summand
normal-form association NONZERO, without mathematical
content. That is not a used lemma or coauthor input.
Our free-group construction was already NONZERO before
receiving that metadata. Nothing here claims an actual
full contractible normal form.

This is a standard same-family RESULT_ONLY / COMPOSE
appendix suitable for merging into the finite-operator/
connection theorem record. It is not a new paper, generic
Tool, general discovery mechanism or automatic successor
research obligation. No neighboring parameter paper is
created.

## 8. Exact real inputs, personal custody, credit and chronology

All repository locators below are in awdawmip/enterprise-math.
They are already personally whole/Source-consumed inputs.
Their unchanged bodies and exact immutable bindings are
honest REUSE; no new old-Source GET, comparison, whole vote
or receipt is asserted for this write.

(1) Actual finite-category13595, MY earlier author unit:
 Source a7cb776961129885007ae3e9051a1f3e226a6305
 research_notes/owner_goal_20261016/cm24_finite_differential_cochain_image_4a56e9/FINITE_ORDER_DIFFERENTIAL_COCHAIN_MAPS_ACTUAL_SCALAR_COHOMOLOGY_IMAGE_AUTHOR.md
 13595 UTF8bytes
 SHA256 7604fb1c126429a1006a235eb6532b4934014c09e0c4a53f30cd1fe7aec1dd4a
 Gitblob 1f9343722f18fc5bc0bf9aff64dfcd5c61e6f860
 https://github.com/awdawmip/enterprise-math/blob/a7cb776961129885007ae3e9051a1f3e226a6305/research_notes/owner_goal_20261016/cm24_finite_differential_cochain_image_4a56e9/FINITE_ORDER_DIFFERENTIAL_COCHAIN_MAPS_ACTUAL_SCALAR_COHOMOLOGY_IMAGE_AUTHOR.md

Its literal R/D and finite category are used. Its finite
faithfulness is repaid in Section5, not hidden as a review
vote. The earlier actual Source/author whole remains real.
This pass selectively reread its saved Source36 receipt
for Section1 setup and its explicit scope exclusions.
That receipt is at
 /workspace/control_worktrees/4a56e9-published36-source-aa206ce-20261017/research_activity_records/RA-C193E2AA39B9A6A6DDBB69B3/readbacks/3164b5f87551bd07e7c508823c4e285feef976c89b08d5fd00d21e2b330e4feb.json
There was no old-body rehash or fresh API. It explicitly
did NOT classify units or the automorphism kernel.

(2) Actual split i/pi and unit13192, MY earlier author unit:
 Source 53d477ab6c87545cf084098a39beea6162007d6c
 research_notes/owner_goal_20261017/cm24_finite_chain_automorphism_unit_kernel_4a56e9/FINITE_CHAIN_AUTOMORPHISMS_TRIVIAL_COHOMOLOGY_EXPLICIT_UNIT_FAMILY_AUTHOR_COMPOSE_V1.md
 13192 UTF8bytes
 SHA256 ee0190ceb1b09d040102a65fab85d6dfd96f5487ca9ced4d8b1d9bd8041bf749
 Gitblob fc6ac83f73da3964d2bc772835fb243f458208c7
 https://github.com/awdawmip/enterprise-math/blob/53d477ab6c87545cf084098a39beea6162007d6c/research_notes/owner_goal_20261017/cm24_finite_chain_automorphism_unit_kernel_4a56e9/FINITE_CHAIN_AUTOMORPHISMS_TRIVIAL_COHOMOLOGY_EXPLICIT_UNIT_FAMILY_AUTHOR_COMPOSE_V1.md

Its own author/Source whole and CF's15181 genuine NONBLIND
technical peer/our ordinary2/28373 are already closed.
The literal i/pi identity is repaid in Section2 here.
Neither its old peer nor my old authorship supplies an
independent new review of this free-group construction.

(3) Actual new cross-channel15199, CF's author unit:
 Source abc19c08abe2ae3f810e662e31f50537f2c6f70e
 research_notes/owner_goal_20261017/cm24_finite_chain_unipotent_kernel_cf1677/FINITE_CHAIN_COHOMOLOGY_IDENTITY_UNIPOTENTS_AND_AFFINE_SUBGROUP_AUTHOR_COMPOSE_V1.md
 15199 UTF8bytes
 SHA256 9f63db380010300a12614879efcd946064674ecc06521dd3113dc5d8b6cbf7bb
 Gitblob 4b2e122df030e2858a11af5acee2635cd54f8953
 https://github.com/awdawmip/enterprise-math/blob/abc19c08abe2ae3f810e662e31f50537f2c6f70e/research_notes/owner_goal_20261017/cm24_finite_chain_unipotent_kernel_cf1677/FINITE_CHAIN_COHOMOLOGY_IDENTITY_UNIPOTENTS_AND_AFFINE_SUBGROUP_AUTHOR_COMPOSE_V1.md

CF owns the new j, actual Q computation, cross homotopy,
squarezero family and faithful affine-group application.
I personally read its complete local15199 whole and
personally fetched its immutable whole body, commit and
exact1ADD/soleparent before independently freezing my
NONBLIND technical whole15707. This is actual custody,
not borrowed CF/Root API. Its exact original full caller is
 /workspace/enterprise-math/research_notes/owner_goal_20261017/reviews/cm24_finite_chain_unipotents_nonauthor_4a56e9/OWN_CF_UNIPOTENT_AUTHOR_ACTUAL_FULL_SOURCE_COMMIT_COMPARE_RAW.json

My complete15707 review is now Source
 a34a1ead117967d6f588df2f39ff7fba6de3f159,
 research_notes/owner_goal_20261017/reviews/cm24_finite_chain_unipotents_nonauthor_4a56e9/FINITE_CHAIN_UNIPOTENTS_AND_FAITHFUL_AFFINE_SUBGROUP_NONBLIND_INDEPENDENT_WHOLE_REVIEW_AND_CONTEXT.md,
 SHA25609d05f21dcf4f988770b4fd158d69b0378e7f0a569ef5317d3daa55144d062bb,
 Gitblob8a3f08595ef9e34d1131b58934f9a06a0682bf54.
My own full Source/exact1 closure is real. CF separately
reported his genuine complete ordinary ownSource reception
of the pair2/30906 closed. His API observation remains HIS,
not an extra call by me. The previous whole covers the
affine input only and is not an independent self-review of
this new free-group appendix. Equations(3)-(5) are fully
repaid here, while preserving CF's construction credit.

The sole NEW author of ell, the paired homotopies(7), the
actual invariant-channel proof, Q-polynomial faithfulness
application and complete free reduced-word construction
is EM-P11-4A56E9. These were new manual construction
NONZERO, including private algebra before the complete
author chat. Root only authorized a bounded direction and
persistence; Root did not construct or mathematically
accept the result. CF occupation-only replies supplied
no proof or repair. No prospective reviewer has been
treated as a coauthor or an already independent voter.

A metadata-only delegated check had no separate old
custody and returned UNKNOWN without new reading,
calculation or proof. It supplies no evidence or vote.
The exact input/custody statements above come from MY
prior actual records and unchanged saved bodies.

## 9. Current actor, execution limits and exact remaining state

The same warm actor remains EM-P11-4A56E9,
 SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9,
 RA RA-C193E2AA39B9A6A6DDBB69B3.

Current36/175 is already actually Source-bound at
 aa206ce72426db583d71a66e5b7a453695936c5e,
 with complete root
 /workspace/control_worktrees/4a56e9-published36-source-aa206ce-20261017.
The actual original newSource36 startup and SAMEevent
checkpoint previously returned0, activity_allowed=true,
persistence_allowed=true, sync_debt_events=[], with all
five formal authority flags false. This is honest REUSE
of that closed binding; no new guard is claimed here.
Public Source identity is not an attested MCP session;
the original attestationfalse, RA state KNOWN and budget
UNKNOWN history are not relabelled. ParentGoal stays OPEN.

This appendix is after event36's fixedcut and was NOT
silently added to its22 calls,23 metadata or175 readbacks.
No helper37, RA/checkpoint append, new registration,
identity/budget reset, Source/main mutation or new
scientific/formalTask permission has occurred for it.
No external query, scientific program, solver, coefficient
generation, enumeration or experiment was used. Text
tools only persist/read this authored prose and compute
its NEW byte identities. Old STOP/HOLD/errors/UNKNOWN,
false endings and all previous warm contributions remain.

The complete new author argument was first sent to Root
in chat before this first persistence. This file is a
new complete appendix, not restoration of any missing
old frozen bytes. The input13595 selected local reuse and
the15199 already genuine whole/Source custody above are
real; no fake fresh three-input API call is asserted.

A future reviewer must state its actual warm/NONBLIND
and constructive exposure, read THIS complete proof
and context independently, and bind the actual new
author Source when available. Section1's inherited
weak-ring setup must be personally grounded; the needed
finite identities, rectangular maps, actual faithfulness,
all-word argument and scope limits are repaid here.
There is no requirement to pretend old13595/13192/15199
were already wholly read by a prospective reviewer;
their own real necessary-input boundary decides that.
No review, temporary chat pass, new Source, final
acceptance or future activity count is prefilled.

First actual complete self-reading and its new
UTF8bytes/SHA256/Gitblob output will fix this V1 exactly
once. Until an independent complete technical review
and actual Source-bound receptions genuinely occur,
this record remains AUTHOR-PROVED / UNREVIEWED,
same-family RESULT_ONLY / COMPOSE only.

