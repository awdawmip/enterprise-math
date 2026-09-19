# Common differential rigidity for the fixed CM(-24) target

Researcher: EM-RB-1EB0B6. Task: RS-RB-CM24-COMMON-DIFFERENTIAL-RIGIDITY / TP2-F588CAD6A9583BB015B3. Actual CLAIM5744662393 / ER-F6F23D03479064A62FCD.

Status: completed source-exposed non-author check of the Driver's geometric candidate, with explicit researcher-formulated arithmetic/application corollaries awaiting appropriate ordinary review. This is not a clean blind derivation, Driver acceptance, canonical promotion, or parent closure. Proposition-level authorship is recorded in NONAUTHOR_REVIEW.json.

## 1. Inputs, quantifiers and result

Keep the task's smooth projective curves C and D, field L=Q(alpha,beta,i) of degree16 with alpha>0, alpha^4=3, beta>0, beta^2=2, i^2=-1 in the positive imaginary embedding, and s=alpha^2. The algebraic coordinates are the task's named model, not new native axes or a modification of P000.

    C: t^2=R^3-3R,        D: w^2=(R+2)t,
    k=-i*alpha*(s*beta-2),
    lambda=35+24*beta-20*s-14*s*beta,
    phi=(dR/w)*(1+k/t),
    E0: Y^2=C0*X*(X-1)*(X-lambda),
    C0=-i*alpha*(9+3*beta+2*s+4*s*beta)/4,
    omega0=dX/Y.

We consume the accepted input f0=(X0,Y0), X0=N/D0 and Y0=w*delta(X0)/(t+k), with its exact sign, canceled base point and degree six. The full original formula is retained by reference and extracted unchanged in ACCEPTED_INPUTS.json. Its accepted unsquared identity is f0*omega0=phi, and j(E0)=2417472+1707264*beta. The admission source is RR-F79FA3D36EF85CC4C6CE with DR-7D70258F6D39E9B6B00D at 0f4fc206e6c3a950cdd7c7587a455bfc829d8a33. That later accepted scope, not the proof file's historical INCOMPLETE header, controls this input. No old map computation is rerun.

**Geometric theorem G.** Over the algebraic closure of L, every morphism f:D->E0 with degree six and

    f*omega0=c*phi,  c nonzero,

has f=epsilon*f0+T, where epsilon is +1 or -1, c=epsilon, and T is a constant point of E0. Conversely all those maps have the asserted degree and pullback. Neither f0 nor f is assumed primitive. Their full Jacobian kernels, image lattices and period indices are not assumed connected or saturated.

**Centered corollary E.** If also f sigma=[-1]f for sigma(R,t,w)=(R,t,-w), then T belongs to E0[2]. There are eight distinct centered maps for the unspecified proportional scalar, four with each sign. There are four distinct X-coordinate functions. These statements concern actual maps, not counts of parameter systems.

**Arithmetic corollary K.** For any declared field K containing L inside the chosen complex field, general maps in G are K-defined exactly when T is K-rational. For d in K*, let Ed:y^2=d*x*(x-1)*(x-lambda), omega_d=dx/y. A K-defined degree-six map h:D->Ed with h*omega_d=b*phi exists exactly when there is b in K* with d*b^2=C0. Explicit maps and the full Galois condition are given in section7. In particular equal j alone does not establish a K-isomorphism or a K-defined map. Proper-subfield descent outside this K-containing-L domain is not resolved by the simplified statement.

## 2. Jacobian conventions and the positive degree identity

Work first over the algebraic closure with its fixed complex embedding. Choose the unique point P on D above O of C. It is L-rational: the quadratic cover has odd local valuation ord_O((R+2)t)=-5, so the unique point above O has ramification index2 and residue degree1. The accepted special-fiber data give f0(P)=(0,0). Choosing another base point would only change the translation constants below.

Let aP:D->J=Jac(D)=Pic^0(D) send Q to [Q-P]. Define u,u0:J->E0 by

    u aP=f-f(P),        u0 aP=f0-f0(P).

Their existence and uniqueness are the Albanese property. Both are surjective, since the curve maps are nonconstant. The Abel-map pullback on regular differentials is an isomorphism, hence

    u*omega0=c*u0*omega0.                                    (2.1)

Use the canonical principal polarizations lambda_J and lambda_E. For a homomorphism u:J->E0 define

    u^dagger=lambda_J^(-1) u^vee lambda_E : E0->J.

These are integral morphisms: both polarizations are isomorphisms. Under canonical Jacobian autoduality this dagger is the Picard pullback along f. Here is the convention check. The dual morphism pulls line bundles back; restricting along aP gives (u aP)*M=(f-f(P))*M=f*M for M in Pic^0(E0), since translations act trivially on degree-zero divisor classes. The canonical Picard and principal-polarization identifications on the two curves give exactly the displayed adjoint; the simultaneous conventional signs cancel. Equivalently its action on a point of Jac(E0) represented by [A]-[B] is the divisor class [f^*A-f^*B]. Thus this is the positive, not negative, push-pull convention.

Pushforward of that divisor gives degree(f)*([A]-[B]), including ramification multiplicities. It follows that

    u u^dagger=[6],        u0 u0^dagger=[6].                  (2.2)

The same polarizations make dagger an involution reversing composition. This is the graph-transpose/Picard functoriality from Jacobian autoduality, with no division by a polarization degree.

Primary inputs for this paragraph are Milne, Jacobian Varieties, Proposition2.2, Proposition6.1, Corollary6.3, Theorem6.6 and Lemma6.9. Their hypotheses hold: D is smooth, proper, geometrically connected, of positive genus; E0 is nonsingular; the base point is specified; the polarizations are canonical and principal. The divisor computation above supplies (2.2) directly.

## 3. Common connected kernel and every finite isogeny factor

A nonzero homomorphism from an abelian variety to an elliptic curve in characteristic zero has nonzero differential. Indeed its image is the elliptic curve, and its reduced/smooth kernel has codimension one. The rank of its tangent map is therefore one. This uses the characteristic-zero kernel statement, not an assumption excluding a finite disconnected part.

Equation (2.1) makes the tangent kernels equal. If B0=(ker u0)^0, the restriction u|B0 has zero differential, hence is zero by the preceding observation. Thus B0 is contained in (ker u)^0. Reversing u and u0 gives

    B=(ker u0)^0=(ker u)^0.                                  (3.1)

No equality of the full kernels has been deduced.

For an explicit construction of the common quotient, choose a Poincare complement B' of B in J. Its dimension is one. The intersection F=B intersect B' is finite, and B x B' -> J is an isogeny. The elliptic quotient Q=B'/F exists. The map B x B' -> Q, (b,b')->[b'], is constant on the kernel of the addition isogeny, so finite faithfully-flat descent gives q:J->Q. Its kernel is exactly B: if q(b+b')=0, then b' belongs to F and hence b+b' belongs to B. This constructs the quotient J/B without assuming u0 has connected full kernel.

Both u and u0 factor as

    u=v q,        u0=v0 q,

where v,v0:Q->E0 are nonzero homomorphisms of elliptic curves, thus finite isogenies. If g=q aP, then g is nonconstant and

    degree(v)*degree(g)=degree(v0)*degree(g)=6.

Their common isogeny degree m divides six. It is left undetermined; setting m=1 would be unjustified. This factorization includes every possible finite component of the full kernels. It computes no lattice saturation or parent period index.

Milne, Abelian Varieties, section8 and Proposition8.1 justify the kernel/isogeny facts; Proposition12.1 supplies the complement. Quotienting B' by F uses Sutherland, Lecture5, Theorem5.11: a finite subgroup of an elliptic curve is the kernel of a separable isogeny. Here the base is algebraically closed of characteristic zero and F is finite, so its field/stability hypotheses hold. The construction just given checks how it produces the common quotient in this situation.

## 4. Same dual image and the integral norm36 equation

Duals reverse composition. Since v and v0 are isogenies, their duals are surjective isogenies (Milne, Abelian Varieties, Theorem11.1). Therefore

    image(u^dagger)=lambda_J^(-1) image(q^vee)
                  =image(u0^dagger)=A0.                      (4.1)

Here A0 is an elliptic subvariety. It is nonzero by (2.2). We only use the image of q^vee, not any assertion that q^vee or u0^dagger is an isomorphism. In particular (4.1) is not a primitive-map shortcut.

Set P0=u0^dagger u0 in End(J). On the shared image A0, P0 is multiplication by six, because

    P0 u0^dagger = u0^dagger[6]

and u0^dagger is surjective onto A0. Now form the integral endomorphism

    A=u u0^dagger in End(E0).

Using (4.1), (2.2), and the adjoint composition rule gives

    A A^dagger
       =u (u0^dagger u0) u^dagger
       =u [6] u^dagger
       =[36].                                                (4.2)

Since A is an elliptic endomorphism and its adjoint is its elliptic dual, (4.2) says degree(A)=36. No rational quasi-isogeny has been substituted for A and no unknown finite index was canceled. This proves the candidate's central implication for nonprimitive maps as well.

## 5. Actual CM identification and complete integral calculation

The discriminant -24 order has Hilbert class polynomial

    H_-24(Z)=Z^2-4834944*Z+14670139392.                        (5.1)

This exact polynomial is the D=-24 row of Joan-C. Lario's original CM table. It was also independently generated locally by fmpz_poly.hilbert_class_poly(-24), python-flint0.8.0 / FLINT3.3.1; the input, exact output, command and runtime are preserved. This is a class-polynomial cross-check, not a computation of phi periods.

The characterization in Sutherland's Lecture20, section20.3, defines H_D by precisely the geometric j-values with endomorphism ring the order of discriminant D; Theorem20.12 proves integrality. The native integer checker verifies that the accepted j0=2417472+1707264*beta annihilates (5.1) using beta^2=2. Therefore

    End_overline(L)(E0) = O_-24 = Z[sqrt(-6)],
    End^0_overline(L)(E0)=Q(sqrt(-6)).                         (5.2)

This is a use of the exact CM characterization and class polynomial, not a label-based inference from j. The discriminant is fundamental: -6 is squarefree and -6 is 2 modulo4, so its maximal ring of integers has the stated integral basis. One may first work over C; geometric endomorphisms descend to the algebraic closure of L, for their finite kernels are torsion subgroups and the associated quotient/isomorphism data are algebraic. This also follows from invariance of homomorphisms under extension of an algebraically closed base.

For a+b sqrt(-6), degree is the positive field norm a^2+6b^2. Analytically this is the real determinant of multiplication on the elliptic period lattice; equivalently elliptic duality sends sqrt(-6) to its conjugate. No value of that lattice or its index for f0 is needed. The lattice explanation identifies the norm, not an absolute period.

Since A in (4.2) is integral, write A=a+b sqrt(-6) with a,b integers. Then

    a^2+6b^2=36.                                             (5.3)

The existing BRC facade gives |b|<=2 and exact square-root remainder traces for a^2=36,30,12 when |b|=0,1,2. Only the first is a square. Thus

    A=epsilon[6], epsilon in {+1,-1}.                         (5.4)

The integrality gate is essential: (-30+12 sqrt(-6))/7 has rational norm36 but is not integral. The correct CM field is also essential: 6i has norm36 in the Gaussian order. These are scope counterchecks, not counterexamples to the fixed E0 theorem. Both are retained in the exact certificate.

## 6. Relative scalar, translations and centered maps

From (2.2), u0(P0-[6])=0. The image of the connected J under P0-[6] is connected and contains zero, so it lies in B, the identity component of ker u0. By (3.1), u kills B. Hence

    A u0=u P0=[6]u.

Equation (5.4) gives [6](u-epsilon u0)=0. Its image is a connected subgroup contained in the finite E0[6], so it is zero. Consequently

    u=epsilon u0,      c=epsilon,
    f=epsilon f0+T,
    T=f(P)-epsilon f0(P).                                   (6.1)

This proves G. In particular c was retained throughout and is forced only at the end. The negative map is a genuine solution with pullback -phi; silently setting c=1 would lose it.

The accepted f0 has X0 fixed by sigma and Y0 odd in w, so f0 sigma=[-1]f0. For (6.1),

    f sigma=-epsilon f0+T,        [-1]f=-epsilon f0-T.

These are equal exactly when [2]T=0. The four points are O_E,(0,0),(1,0),(lambda,0), all defined over L. The eight maps are distinct: an equality between different signs would make [2]f0 constant, whereas equal signs cancel and force the same T. Thus E holds. Arbitrary translations in G are not restricted to this finite set.

For use with the original cover, the four target translations act by

| T | M_T(x) | M_T'(x) |
| --- | --- | --- |
| O_E | x | 1 |
| (0,0) | lambda/x | -lambda/x^2 |
| (1,0) | (x-lambda)/(x-1) | (lambda-1)/(x-1)^2 |
| (lambda,0) | lambda*(x-1)/(x-lambda) | lambda*(1-lambda)/(x-lambda)^2 |

The centered maps are

    (X,Y)=(M_T(X0), epsilon*M_T'(X0)*Y0).                      (6.2)

Direct cleared polynomial identities verify both the same target equation and the unsquared differential. These rational formulae extend to elliptic automorphisms at their displayed poles; each sends O_E to the indicated T and preserves the invariant differential, hence is the corresponding translation. This gives the fixed-target Klein-four operations only, without S4 relabeling or a source-sign quotient. For the normalized pullback c=+1 there are four centered maps, not eight.

## 7. Exact twist multiplier and descent

Let K contain L and let d in K*. Choose eta in the algebraic closure with

    eta^2=d/C0.

Keep this choice explicit. The isomorphism to the fixed target is

    iota_eta:Ed->E0, (x,y)->(x,y/eta),
    iota_eta*omega0=eta*omega_d.                              (7.1)

If h*omega_d=b*phi, then f=iota_eta h satisfies f*omega0=c*phi with

    c=eta*b.                                                  (7.2)

Applying G yields c=epsilon and

    h=iota_eta^(-1)(epsilon f0+T),
    b=epsilon/eta,        d*b^2=C0.                          (7.3)

For a fixed root eta, these are all geometric maps in this domain. Changing eta to -eta changes the same representation to (-epsilon,-T), not to a new map. A centered map requires T in E0[2] and has explicit coordinates

    x=M_T(X0),        y=eta*epsilon*M_T'(X0)*Y0.               (7.4)

Here is the exact Galois condition. For tau fixing K set chi_tau=tau(eta)/eta in {+1,-1}. Since f0 is K-defined,

    tau(h)=h
    iff [chi_tau](epsilon f0+tau(T))=epsilon f0+T.            (7.5)

If chi_tau=-1, (7.5) would make [2]epsilon f0 a constant map, impossible. Thus every chi_tau must be +1, so eta belongs to K. Equation (7.5) then reduces to tau(T)=T. Conversely eta in K and T in E0(K) plainly suffice. This proves K-rationality precisely in the stated domain. A proportional scalar b of two K-defined nonzero differentials lies in K: compare any nonzero coefficient in a K-basis of H^0(D,Omega^1). Thus (7.3) is equivalent to the K-condition d/C0 being a square, with its multiplier retained.

For fixed b in K* satisfying d*b^2=C0, choose eta=1/b and epsilon=+1. The four centered maps are

    (x,y)=(M_T(X0), M_T'(X0)*Y0/b).                           (7.6)

If b is additionally prescribed to be exactly1, the literal coefficient d must equal C0, not merely its square class. An isomorphic twist with d!=C0 changes the chosen invariant differential.

The geometric endomorphisms in (5.2) are all defined over L. Indeed the derivative embedding rho:End(E0)->overline(L) is faithful in characteristic zero. Its image is Z+Z*sqrt(-6), contained in L since sqrt(-6)=i*alpha^2*beta up to sign. Galois conjugation over L fixes every derivative multiplier, hence fixes every endomorphism. This proves End_L(E0)=End_overline(L)(E0); it is not an assumption from j. The same holds for K containing L. For proper subfields that do not contain the stated model/map constants no such conclusion is silently extended.

More generally, when the models descend to a smaller field but f0 need not, the unsimplified condition is

    [chi_tau](epsilon*tau(f0)+tau(T))=epsilon*f0+T.            (7.7)

Any action on phi and any proposed descent of f0 must also be retained there. This report does not solve all such proper-subfield problems or claim a minimal field of definition.

## 8. Application to the complete retained index

The frozen index has 45 rows for 4+2 and 90 for 2+2+2, with sixteen compatible unramified twist labels per row before the prior exclusion. The prior empty-fiber result removes four labels in each 4+2 row, leaving the stated 540 and 1440 indexed systems. All rows and exclusion masks were consumed from the pinned JSONs; none was regenerated and no RR/ODE parameter search was run. INDEX_APPLICATION.json records the exact file hashes and the unique stored row of the accepted map.

An indexed solution falls under the present theorem only after all its original gates hold: nonsingular target, nonzero constants and differential scalar, smooth source normalization, exact degree six after cancellation, genuine cover lift, and the full unsquared fixed-k differential. An even-divisor triple or a degenerate parameter point is not enough. Over an algebraic closure any resulting target with this fixed lambda is transported to E0 by (7.1), keeping its multiplier. The original form Y=wH is deck anti-equivariant. Therefore every such genuine solution has X equal to one of the four functions in (6.2).

The accepted f0 has branch labels (0,infinity,infinity,0,0,0) in source order (O,T0,Tplus,Tminus,Pplus,Pminus). Its occupancy type is 4+2+0+0. Fixed-target V4 translations preserve that multiset. Thus no genuine full-degree/full-differential map represented by a 2+2+2 indexed system can occur. This application corollary is stated separately for independent ordinary review; it does not say that its relaxed polynomial equations or degenerate loci are empty.

For the 4+2 index the theorem gives one geometric V4/sign orbit of genuine maps, with the exact twist/scalar restrictions of section7. It does not count coefficient representations, assert a number of nonempty parameter systems, or solve every row's saturation/field equations. Relative to the accepted source's fixed half-point and row convention, the stored empty-infinity representative is

    z=lambda*(X0-1)/(X0-lambda),

with labels (1,lambda,lambda,1,1,1), transport (0 1)(lambda infinity), and retained twist labels (Tplus,T0,Tminus). These are consumed accepted data, not a new matching enumeration. Proper-subfield descent, arbitrary K-rational translation groups, and degenerate representations remain outside the finite map statement.

The actual finite factor m and any parent period integer, homology index or absolute normalization have not been computed. The six-block proof, its 80-map predecessor pins, and all old index sources remain intact. The RB parent remains OPEN.

## 9. Decisive check, evidence and review routing

The original candidate author is EM-DVR-5816EB, at the exact source/hash in NONAUTHOR_REVIEW.json. Sections2–6 above complete and verify that candidate's stated common-kernel, integral dual-norm, CM and geometric-translation implications; no changed hard target, primitive assumption or repaired false lemma is smuggled in. The exact arithmetic field-of-definition formulation and residual-index application in sections7–8 are explicitly researcher-formulated corollaries; their acceptance requires another appropriate reviewer. Publication and a researcher PASS do not admit them canonically.

The native checker imports the unchanged pinned RB ring and BRC interfaces. It verifies H_-24(j0)=0 by an integer ideal identity, all finite norm cases, universal V4 target/differential identities, and twist transport. The certificate has ten polynomial checks, six tamper checks and three norm/scalar boundary tests. Local FLINT output cross-checks the independent primary H_-24 table. None of these finite calculations replaces sections2–6's geometric reasoning or the primary CM theorem.

Primary references, accessed during this execution:

- [Milne, Jacobian Varieties](https://www.jmilne.org/math/xnotes/JVs.pdf), Proposition2.2, Proposition6.1, Corollary6.3, Theorem6.6, Lemma6.9: the differential/Albanese/autoduality inputs used with smooth projective curves and canonical principal polarizations.
- [Milne, Abelian Varieties](https://www.jmilne.org/math/xnotes/AVs.pdf), section8, Proposition8.1, Theorem8.2, Theorem11.1, Proposition12.1: characteristic-zero kernels, finite isogenies, duals and complements. The connected-versus-full-kernel distinction is retained in section3.
- [Sutherland, 18.783 Lecture20 (2023)](https://math.mit.edu/classes/18.783/2023/LectureNotes20.pdf), section20.3 and Theorem20.12: the exact CM-order root characterization and integrality of H_D. Its Remark20.5 also distinguishes geometric j-isomorphism from field-defined twists.
- [Sutherland, 18.783 Lecture5 (2023)](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf), Theorem5.11: the finite elliptic quotient used in section3, over the stated algebraically closed characteristic-zero base.
- [Lario, original CM table](https://web.mat.upc.edu/joan.carles.lario/ellipticm.htm), h_2 row -24: the coefficients in (5.1), independently reproduced locally by FLINT.

No analytic period of phi, hosted Actions calculation, clean-blindness claim, new tool family or Foundation promotion is part of this result.
