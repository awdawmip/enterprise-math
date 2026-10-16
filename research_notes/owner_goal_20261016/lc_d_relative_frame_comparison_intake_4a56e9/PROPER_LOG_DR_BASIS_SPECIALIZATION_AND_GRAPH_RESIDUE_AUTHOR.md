# Proper logarithmic de Rham basis, specialization and graph-residue comparison

EM-P11-4A56E9, genuine SID MCP-387e35a6a7d24e8cb2c44e361b9ce5b9, own RA-C193E2AA39B9A6A6DDBB69B3, direct NONBLIND TASK_RESEARCH paper work. This is a separate author successor to the central-graph paper, not a modification of it or an extension of its independent review. All inherited CONTROL, old EM-T6-BFF294/fixed233 and LC contributions remain disclosed. No scientific program, new Task/run, Native vote or Tool registration is used. The fixed233 stopped budget remains0. This integrated author paper is UNREVIEWED.

The new finite algebraic-model theorem is that the actual proper log-de Rham H1 over A_n has the specific Weierstrass classes omega,eta as a basis; ordinary central H1 specialization is an isomorphism; the logarithmic Gauss-Manin residue in that basis has kernel R_n*(omega+eta); and the explicit proper Cech comparison identifies it with the canonical central crystalline graph image. The proof constructs these arrows rather than invoking an unspecified semistable comparison. A separate formal/completed/p-inverted realization, isogeny, cup multiplier and saved global sign are not supplied.

## Exact reused interface

The source is the actual Weierstrass family

    y^2=x^3+a(s)x+b(s),
    a(s)=3(4s-5), b(s)=4s^2-28s+22,
    s=S(1+t), S(r)=4r^3-3r.

Work over A_n=(Z/p^n)[[t]], p=13 or19 mod24, with the actual proper semistable algebraic model Y_n and its t-log structure. Put omega=dx/(2y), eta=x omega. Source7317568f2eca4aa89fa2f22266f390e5f07b6b5d, bundle CM24_SOURCE_GEOMETRY_THREE_ISOGENY_FIXED_LEGENDRE_20261015_FBF223.json, contains the full13972B source-geometry proof, SHA929e5b4364c846dacce8897f6e4aed0bd822a3e7b3b3d073f11e9594d5239305. I personally fetched its whole66821B carrier, verified all7members and read this entire member. Original owner18F24A, support63E74C9D and RootFBF223 mathematical map/matrix/GM contributions remain credited.

That old proof's rank-two de Rham basis is over the smooth base with 1-s^2 inverted. It is not a boundary log-H1 basis theorem. The present lemma constructs the actual proper classes before asking whether they form a basis. Sourcefbb8f54db09deae49c9905acdad2bf5608ec1702 supplies the matched finite algebraic HK2.20/2.23 comparison. The new central graph author paper is at Source1a5ebb33e1d2b13203a4f4ad233654642ba21e1b and has separately received genuine nonauthor PAPER_PASS from EM-PUBLIC-7CDA51: report15463B SHAcd6cc03721a78e75f422b905db95d82745c0429f711c377e2eb5c35a4fbd60da, personally read in full. Its actual author Source and original theorem are dependencies here. That paper-only review is not a review of this new argument; no PASS propagates to the present manuscript.

## 1. A literal infinity regularization

On the generic rational differential field, differentiation of the Weierstrass equation gives the identity

    h=y/x,
    d h=(x-a/x-2b/x^2) omega,
    eta-d h=(a/x+2b/x^2) omega.                    (1)

Indeed dy=(3x^2+a)dx/(2y), so the numerator of d(y/x) in the omega basis is ((3x^2+a)x-2(x^3+ax+b))/x^2. This is x-a/x-2b/x^2. There is no integration or division by p in (1).

The actual relative logarithmic omega is regular on the proper semistable model. At a smooth finite point use dx/(2y), or the equivalent dy/(3x^2+a) if y=0. At the node the Weierstrass Poincare-residue generator becomes a unit multiple of du/u=-dv/v in an etale chart uv=t. This follows by the invertible coordinate Jacobian and the p-unit smoothing derivative; it is the same semistable log-differential module of the matched HK paper. Infinity is smooth, and z=-x/y is a relative parameter there with omega a unit times dz. In particular x has pole2 and y pole3, so 1/x is regular and vanishes at infinity. Consequently the right side of (1) is regular at infinity. Eta itself has a second-kind pole there; h has a simple pole and supplies its exact principal part.

Let U=Y_n minus the infinity section. Choose V to contain infinity and omit the finite zero divisors of x and x+1. Those zero divisors do not contain infinity; equivalently they are the zero divisors of the rational functions after their known infinity poles have been removed. They are finite in this Weierstrass model. Thus U,V cover Y_n, h is regular on U intersect V, and eta-dh is a relative log form on V by (1). Removing x+1 as well will make the central comparison below literal. No assertion that a Cech cover is acyclic is needed just to define its canonical hypercohomology class.

For a two-open Cech/de Rham total complex use triples (alpha_U,alpha_V;beta_UV) with

    alpha_V-alpha_U=d beta_UV.

The following therefore define proper log-de Rham classes:

    [omega] = [(omega,omega;0)],
    [eta]   = [(eta,eta-dh;-h)],
    kappa   = [omega]+[eta]
            = [(omega+eta,omega+eta-dh;-h)].        (2)

They map by the ordinary Cech-to-hypercohomology map into H^1 R Gamma(Y_n,[O->Omega^1_log]). Refinement and changing a primitive by a function regular on V give the usual explicit total coboundary. We retain the particular rational primitive h; it is not silently declared globally regular or discarded. All coefficients in (1)-(2) are integral at the allowed primes. These formulas commute with n-reduction and with t=0.

## 2. Actual central chain comparison

At t=0 the central cubic is y^2=(x-2)(x+1)^2. On its base-changed normalization put

    v=y/(x+1), x=v^2+2, y=v(v^2+3),
    omega=dv/(v^2+3), eta=(v^2+2)dv/(v^2+3).

The reused identity omega+eta=dv does not by itself assert exactness on the singular curve. Its primitive is not a regular function at the node. We now keep the actual total cochain that (2) requires.

On the normalized inverse images of U,V define

    f_U=v,
    f_V=v-h=-v/(v^2+2).                            (3)

The first is regular on the normalization of U, which is P1 minus infinity. The second is regular on the inverse image of V: finite zeros of x=v^2+2 were removed, and it vanishes to order1 at infinity. The possible node branches were also excluded from V. Their difference on the overlap is f_V-f_U=-h. Thus in the normalization log de Rham complex the total differential of (3) is exactly

    (d v, d(v-h); -h),                             (4)

the normalized image of the specialized kappa cocycle in (2). At the two node preimages v=+nu,-nu the degree0 conductor quotient of f_U is

    f_U(+nu)-f_U(-nu)=2nu.                         (5)

In the notation of the central-graph paper's explicit short exact complex sequence 0->L_n->M_n->Q_n->0, (3) is a lift of the global degree0 quotient section2nu. By the definition of its connecting homomorphism, (4)-(5) give the exact equality

    sp(kappa)=delta_L(2nu).                        (6)

Here sp is the actual map on H^1 induced by restricting these proper Cech representatives to t=0. Existence of this map does not require ordinary H^1 tensor base change to be an isomorphism. The sign in (6) uses precisely the stated Cech convention and the quotient value at +nu minus value at -nu. Reversing that quotient reverses the graph generator as well.

Combining (6) with the separate central-graph theorem identifies sp(kappa) with 2nu j_n(1) in the actual finite-level central crystalline group through the matched HK comparison. In particular the saved scaling kappa/12 maps to (nu/6)j_n(1), with the fixed orientation, and its central crystalline image is fixed by the specified Frobenius. These are explicit consequences of that separate graph theorem. This manuscript does not pretend its separate review is a vote on the present class construction or subsequent basis/connection arguments.

The old jump calculation is reused, not claimed anew. The additional content is the concrete relative proper Cech representative (2), its infinity boundary h, the central normalized lift (3), and the chain comparison (6) inside the actual de Rham model. It replaces an unspecified appeal to a rational primitive by the relevant proper total cochains.

## 3. The boundary basis follows from explicit proper cohomology

We now prove the basis assertion, instead of borrowing it from the discriminant-inverted source. The argument applies to Y_n/A_n and its central C_n/R_n; use R for either base ring and Z for the corresponding proper cubic, with infinity section O. It also applies under coefficient reduction. All these schemes and sections are flat over R. Both2 and3 are units. In this section R denotes the underlying ring; every Omega_Z/R,log means relative to its stated log base, S_n for A_n or the standard log point T_n for R_n. It never means relative to a trivially logged R_n, whose absolute log-differential module would be different.

The same local residue calculation in section1 proves

    Omega^1_Z/R,log = O_Z omega.                   (7)

At smooth points this is the ordinary invariant differential; at the node it is a unit multiple of the semistable logarithmic generator. The coefficient is a unit because the two tangent roots are distinct and the smoothing chart has unit Jacobian. At infinity the parameter z=-x/y gives a unit leading coefficient. Thus (7) is a global trivialization, not just a rational differential identity or a statement on the punctured base.

Here is an elementary proper cohomology calculation over R. The plane Weierstrass cubic has hyperplane bundle O_Z(1)=O_Z(3O): its line at infinity cuts the section with multiplicity3. The plane exact sequence

    0 -> O_P2(-2) -> O_P2(1) -> O_Z(3O) -> 0

gives H^1(Z,O_Z(3O))=0. The needed projective-space facts work over any ring: H^1(P2,O(k))=0, and H^2(P2,O(-2))=0. They follow on the three standard affine charts by decomposing the Cech complex into Laurent monomials; a possible top-degree surviving monomial must have all three exponents negative, so has total degree at most-3. The mixed-sign monomials are Cech boundaries, giving the stated H^1 vanishing. No field-valued dimension or cohomological base-change theorem is being assumed.

Functions regular on Z minus O have the unique polynomial form P(x)+yQ(x). Their nonconstant monomials have distinct pole orders2i and2i+3 at O. This follows from the monic Weierstrass equation and the expansions x=z^-2 times a unit and y=-z^-3 times a unit. Even and odd pole orders do not cancel. This remains true for nonzero nilpotent coefficients over R_n: multiplication by the leading unit does not kill a nonzero coefficient. Hence

    H^0 O_Z=R,             H^0 O_Z(O)=R,
    H^0 O_Z(2O)=R+R x,    H^0 O_Z(3O)=R+R x+R y.  (8)

In each sequence O_Z(kO)->O_Z((k+1)O) the quotient is the leading principal-part line on O. It is identified with R using the parameter z. For k=2 the function y maps to a unit generator of the order3 quotient; for k=1 the function x does the same for the order2 quotient. The long exact sequences and the preceding H^1 O_Z(3O)=0 therefore give

    H^1 O_Z(2O)=H^1 O_Z(O)=0.

The sequence0->O_Z->O_Z(O)->principal-part-line->0, together with (8), now shows that the boundary

    R ~= H^1(Z,O_Z)                               (9)

is an isomorphism. In the two-open Cech convention above, the class of1/z is a generator. Notice that h=y/x=-1/z exactly. The degree0 Cech component of [eta] in (2) is -h=1/z. Its projection to H^1(O_Z) is therefore the generator (9), with that orientation convention. This is the actual proper class, including its infinity principal part.

For the nonnegative two-term complex L=[O_Z->O_Z omega], its elementary hypercohomology sequence is

    0 -> coker(H^0 d) -> H^1 R Gamma(L)
      -> ker(H^1 d) -> 0.

H^0 O_Z=R and H^0 Omega_log=R omega by (7)-(8), and d on global constants is zero. Moreover [eta] already maps onto the generator of H^1 O_Z. The hypercohomology edge map lands in ker(H^1 d), so this lifting proves that H^1 d=0 on all of the free rank-one H^1 O_Z. We obtain the exact sequence

    0 -> R[omega] -> H^1 R Gamma(L) -> R -> 0,     (10)

and [eta] is an explicit section on the displayed generator. It follows that [omega],[eta] are an R-basis. This proves the boundary basis without using Serre duality, a general Hodge-de Rham degeneration theorem or an unsupported reverse arrow from coherent cohomology.

All the Cech representatives, parameter and principal-part calculations commute with A_n->R_n and with n-reduction. On both sides the same two classes are a basis. Consequently the actual natural map

    H^1 R Gamma(Y_n,L_n) tensor_A_n R_n
      -> H^1 R Gamma(C_n,L_0n)                     (11)

is an isomorphism, taking the particular omega,eta classes to the particular central classes in (2). This is now ordinary H^1 base change proved by a basis computation; it is not inferred from derived specialization alone. Equation(11) agrees with the already matched HK specialization because that comparison sends the actual relative de Rham complexes and their restrictions to the same crystalline maps.

## 4. The actual logarithmic Gauss-Manin along t*d/dt

We specify the operator without asserting that algebraic Kahler differentials of Spec A_n over R_n are freely generated by dt. Let delta=t*d/dt be the chosen genuine R_n-derivation of A_n: on a power series sum c_j t^j it is sum j c_j t^j. Give it base-log value delta_log(t)=1. These satisfy delta(t)=t. This is a specified logarithmic derivation, not a silent identification of algebraic and continuous differential modules.

Local logarithmic lifts D_i of delta to Y_n exist directly on the actual charts. On a smooth strict chart lift delta keeping a relative coordinate fixed. On uv=t use D(u)=u,D(v)=0, with log values1,0; etale charts lift the derivation uniquely. Refining to an affine etale cover if necessary, these give the usual Cech log Gauss-Manin operator. Here is a direct degree1 construction showing its definition and independence. For a cocycle (alpha_i,beta_ij), where alpha_j-alpha_i=d beta_ij, put V_ij=D_j-D_i, a relative log derivation, and set

    alpha'_i=L_Di alpha_i,
    beta'_ij=D_i beta_ij + iota_Vij alpha_j.        (12)

Relative logarithmic2-forms vanish. Cartan's formula for the relative vector field gives L_V alpha=d iota_V alpha, so alpha'_j-alpha'_i=d beta'_ij. On a triple overlap the remaining defect is

    V_ij beta_jk + iota_Vij(alpha_j-alpha_k)=0.

Thus (12) is a cocycle. Changing the original cocycle by the total differential of functions f_i changes (12) by the differential of D_i f_i. Changing the local lifts by relative W_i changes it by the differential of iota_Wi alpha_i. This proves independence of representatives and lifts. It also proves the delta-Leibniz rule: on multiplying the original class by r in A_n the result is delta(r) times that class plus r times (12).

A finite affine etale cover and its affine intersections compute the indicated quasicoherent de Rham hypercohomology. Formula(12) therefore defines a canonical delta-connection on the actual proper H^1, throughout the semistable log base. It is its logarithmic Gauss-Manin operator, by this explicit Lie-derivative/Cartan construction. No underlying Frobenius lift or unidentified completed crystalline site is involved.

On the smooth locus t inverted, this construction is the same proper de Rham Gauss-Manin operator used in the old source proof. Its literal rational-differential identities retain their exact Cech terms. Their standard second-kind eta class is (2): the defining principal part is the one just retained, and changing its primitive by a regular function is a Cech coboundary, not an arbitrary holomorphic-basis change. We may therefore reuse the exact old matrix, without rerunning its calculation.

For columns of coefficients in the row basis e=(omega,eta), the matrix is

    nabla_s e=e C(s),
    C(s)=1/[6(s^2-1)] *
          [[-(2s-1), -(4s-5)],[-1,2s-1]].          (13)

This is the transpose of the saved period-column matrix. For delta the localized matrix is B(t)=t*S'(1+t)*C(S(1+t)). It actually has entries in A_n: S(1+t)-1=t(9+12t+4t^2), with the parenthesized factor a unit, and S(1+t)+1 is a unit. The denominator6 is a unit as well.

Independently, (12) is defined on the whole proper free module of section3, so its matrix in the proved omega,eta basis has entries in A_n. Its restriction to t inverted is (13). The element t is a non-zero-divisor of A_n, including for n>1, and our H^1 module is free. Hence A_n injects into A_n[t^-1], and the two matrices are equal already over A_n. This supplies the actual extension argument that a bare regular-coefficient observation would lack.

## 5. The graph image is the actual finite algebraic residue kernel

By (11) specialization of the relative basis is the central basis. Since delta(r) is divisible by t for every r in A_n, the reduction of its connection is an R_n-linear endomorphism N_n on that central module. It is the residue of the particular actual algebraic log-de Rham Gauss-Manin operator just constructed, transported into the central crystalline group by the matched HK model. We do not define N_n by assuming a separate direct-image log crystal with connection on every PD thickening, or identify it with an independently specified formal/crystalline monodromy operator without a comparison. The literal geometric source connection is the one verified in section4.

Using S(1+t)=1+9t+12t^2+4t^3, one has

    [t*S'(1+t)/(S(1+t)^2-1)]_(t=0)=1/2.

Consequently its matrix in (omega,eta) is

    N_n=(1/12)[[-1,1],[-1,1]],                    (14)

the transpose convention of the saved period residue. Both coordinates,12 and2nu are retained as units; no field-dimension shortcut is needed over R_n. For a column(a,b), (14) is((-a+b)/12)*column(1,1). Thus

    ker N_n = image N_n = R_n*(omega+eta),
    N_n^2=0.                                      (15)

Section2 identifies this actual central class with delta_L(2nu). Combining with the separate central-graph theorem gives

    ker N_n = j_n(R_n),
    (omega+eta)/12 = (nu/6) j_n(1)                 (16)

under the actual finite-level HK comparison and the fixed quotient orientation. Therefore, by the separate central-graph theorem, canonical crystalline Frobenius is the identity on this actual finite algebraic residue kernel. This statement uses an actual class and the actual logarithmic connection; it does not merely match two abstract lines with the same dimension or an eigenvalue.

The construction and matrices commute with n-reduction. The scalars in (16) are the fixed coefficient scalars, not a guessed v->v^p normalization lift. Any later transport into a separately specified formal/p-inverted source crystal must still preserve these concrete comparisons and conventions.

## 6. Exact remaining boundary

The new assembled paper argument provides the relative proper classes, their boundary basis, ordinary H^1 specialization, the actual chosen-log-derivation Gauss-Manin matrix and its central residue kernel, and the explicit proper Cech jump comparison for the literal algebraic finite-level model. Its use of the central graph/crystalline-Frobenius theorem is stated as a separate dependency, whose independent review is not automatically a review of this new argument. This successor itself remains UNREVIEWED.

No identification with a separately defined formal/completed log-crystalline site, derived inverse limit, or p-inverted Q_p[[t]] crystal has been proved here. Compatible coefficient modules do not by themselves identify such a site or justify an exchange of Rlim with cohomology. A Frobenius isogeny, cup multiplier, a separately specified crystalline direct-image connection/monodromy comparison, generic comparison to the exact saved formal Frobenius class and its determinant still need their actual interfaces. In particular we do not now declare the saved global mu, c, extension constants, LC A-C, whole D, dagger/gluing, original functional or parent Goal solved. No stopped233 code, budget or scientific execution is resumed.

Researcher-ID: EM-P11-4A56E9 / TASK_RESEARCH
Global-Knowledge-Sync: main@051d8cb / GLOBAL_KNOWLEDGE_V1
