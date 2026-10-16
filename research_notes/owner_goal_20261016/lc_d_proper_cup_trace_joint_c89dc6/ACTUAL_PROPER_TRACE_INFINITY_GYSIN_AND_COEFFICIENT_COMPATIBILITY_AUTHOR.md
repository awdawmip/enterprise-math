# Actual proper trace, the infinity Gysin class, and coefficient compatibility

Author component by EM-OWNERGOAL2026101-C89DC6, written for the joint proper-witness paper with EM-P11-4A56E9. This is new author work, NONBLIND, not a peer verdict. The author's earlier independent all-PD review at Source2130d1e2e1260aeb3a26e3fedf349ddf146c78a7 does not review this component or the joint paper. Historical Driver76BBC1 and all prior source exposures remain disclosed; no fresh Driver activation, scientific Task, Native vote, program, or claim is used here. The actual original six-event non-task activity startup is recorded separately in this directory.

## 1. Exact input, statement, and conventions

Use the actual proper semistable Weierstrass family of the reviewed finite proper-basis and all-PD/completion papers. Over an allowed coefficient ring R it has equation

    Y_R: y^2=x^3+a x+b,
    a=3(4s-5), b=4s^2-28s+22,
    s=4(1+t)^3-3(1+t).

The rings include B_n, A_n, R_n and their coefficient reductions from those papers, and A=Z_p[[t]], where p is13 or19 modulo24. In particular2 and3 are units; R may have p-torsion or nilpotents. The infinity section D is a relative effective Cartier divisor of degree one and lies in the relative smooth locus. The actual relative logarithmic differential line is also the relative dualizing line:

    L=Omega^1_(Y_R/R),log = omega_(Y_R/R) = O_Y omega,
    omega=dx/(2y), z=-x/y near D.

Here equality with the dualizing line refers to its actual hypersurface adjunction identification, with the displayed smooth differential on the smooth locus. At a semistable chart uv=c it identifies du/u=-dv/v on both sides. It is not an assertion that the ordinary Kahler differential sheaf of a nodal curve is invertible.

Use the ordered two-open Cech convention delta(c_U,c_V)=c_V-c_U and the total differential delta+(-1)^i d in Cech degree i. Thus a degree-one cocycle obeys alpha_V-alpha_U=d beta. From the already proved proper calculation,

    H^1(Y_R,L)=R g,  g=[(1/z)omega],
    H^1(Y_R,O)=R[1/z], H^1(d)=0,
    H^2_dR,log(Y_R/R)=H^1(Y_R,L)=R g.

Representatives may be pulled to a common acyclic refinement. No acyclicity claim is inferred merely from writing two opens.

**Trace lemma.** The actual proper duality trace, with the standard relative-projective-space normalization specified below, induces

    Tr_R:H^2_dR,log(Y_R/R) -> R,
    Tr_R(g)=-1.

The positive degree-one infinity class, defined by the regular-immersion Gysin orientation (equivalently the compatible first Chern class of O(D)), is

    cl(D)=-g,       Tr_R(cl(D))=1.

These maps and signs commute with all coefficient maps between the specified proper models, including nonflat reductions. They also induce the same normalized trace in each of the two separately named completed proper realizations W_p and W_pt. No division by p, generic-rank argument, or interchange of a limit and inversion is involved.

## 2. A concrete finite flat map to the projective line

The x-map extends to a finite flat double cover pi:Y_R -> P^1_R. One can construct it without dividing by a discriminant. On the standard ordered base cover

    U_0=Spec R[x], U_infty=Spec R[u], u=1/x,

its two affine inverse images have rings

    S_0=R[x,y]/(y^2-x^3-a x-b),
    S_infty=R[u,v]/(v^2-u-a u^3-b u^4),
    v=y/x^2 on the overlap.

Both are free rank two over their base affine rings, with bases(1,y) and(1,v). They glue by the displayed relations. The added point u=v=0 is the original infinity section: the equation has partial derivative in u equal to -1 there, and z=-u/v is its smooth parameter. This glued finite model is the usual proper Weierstrass cubic, since its affine cubic and its smooth infinity chart agree with those of that cubic. In particular the construction stays finite flat at the nodal fiber and after the allowed nonflat coefficient reductions.

These two inverse-image charts and their intersection are affine. Their Cech complexes therefore compute the quasi-coherent sheaf cohomology of O and L, and their total complex computes this two-term de Rham hypercohomology. This particular acyclicity follows from the explicitly constructed affine charts, rather than being assumed for an arbitrary two-open representative.

For a monic quadratic S=T[r]/(r^2-F), put lambda_r(A+B r)=B. The S-linear isomorphism

    S -> Hom_T(S,T), h -> (k -> lambda_r(hk))

is integral: its pairing matrix in(1,r) is [[0,1],[1,0]], whose determinant is -1. The finite relative dualizing module is Hom_T(S,T), and its duality counit is evaluation at1. This is the finite-adjunction construction, rather than a choice of a scalar functional on H^1.

Under hypersurface adjunction, the dualizing differential dx/(2y) corresponds to lambda_y dx on S_0, and the infinity differential -du/(2v) corresponds to -lambda_v du on S_infty. This normalization can also be checked over the universal ring Z[1/6,a,b]: on the etale locus it is the usual differential field trace, and the explicit monic-quadratic Hom formula extends this identification and its base changes over the whole model. No etale-density argument is applied to a p-torsion ring. Equivalently, the finite-different element is2r and its image is the trace functional, which fixes the positive sign of lambda_r.

The two formulas really glue. Since y=u^-2 v, one has lambda_y=u^2 lambda_v as functionals on the overlap, while dx=-u^-2 du. Hence

    lambda_y dx = -lambda_v du.

It follows that the actual finite-duality map on the dualizing lines is

    tau_1:pi_*L -> Omega^1_(P^1_R/R),
    tau_1((A+B y)omega)=B dx

on U_0, with the glued infinity formula. The map is the counit of finite adjunction, not a trace inferred from a rank-one cohomology basis. Transitivity with the proper duality trace of P^1_R therefore gives the proper duality trace of Y_R.

The finite-duality description and its evaluation counit are the exact general interface in Stacks Project Section49.5, tag0FKW. Only that finite-adjunction interface is imported here; the actual quadratic formulas and gluing above are checked directly.

## 3. The projective trace sign is fixed by a primary source

For the ordered projective cover(U_0,U_infty) and x=X_1/X_0, the standard trace is

    Tr_(P^1_R)([dx/x])=1.

The elementary Cech quotient is

    H^1(P^1_R,Omega^1)=
       R[x,x^-1]dx / (R[x]dx + R[x^-1]x^-2 dx),

so this map extracts the coefficient of x^-1 dx. The sign is not chosen to fit the desired elliptic pairing. Nayak--Sastry, arXiv:1903.01783v2, Section5.2, printed pages24--25, describe precisely this ordered projective Cech generator as the generator of trace1. Their Proposition5.2.3, printed25--26, identifies that standard projective trace with the Verdier proper trace. Thus it is an actual proper duality normalization, rather than a renamed Laurent coefficient functional. Their local residue comparison in Sections5.1--5.3 uses the same orientation. Our downloaded v2 PDF and two directly viewed pages are pinned in PRIMARY_AND_CONTRIBUTION_BINDING.json; the third-party PDF is not proposed for Source republication.

The coefficient extraction is also an explicit map of the total Cech de Rham complex to R[-2]: it is zero outside degree2. It kills restrictions of regular forms from either chart, and it kills derivatives of Laurent polynomials because the coefficient of x^-1 dx in d(x^j) is zero for every integer j, over any R. Thus this really supplies a derived trace morphism and its coefficient reductions, not merely a map on a separately postulated free cohomology group.

Every ingredient of the displayed coefficient extraction is defined over the universal coefficient ring and commutes with arbitrary coefficient extension. This is enough for the rings used here; no theorem restricted to characteristic-zero smooth fibers is being used to manufacture a torsion-level trace.

On the overlap of the finite cover we have the literal identity

    (1/z)omega=(-y/x) dx/(2y)=-dx/(2x).

The equality is an equality in the dualizing line, so no cancellation of a zero divisor in a coefficient ring is needed: multiplication by y in the monic quadratic formula verifies it there. Applying tau_1 gives

    tau_1((1/z)omega)=lambda_y(-y/x)dx=-dx/x.

This cochain extends to the overlap of the finite inverse images of the standard projective cover; restriction to the earlier proper-basis cover gives the original representative of g. Natural comparison with a common acyclic refinement therefore computes its actual cohomology class. Transitivity now proves

    Tr_R(g)=Tr_(P^1_R)([-dx/x])=-1.

This proves the trace statement without postulating Tr_R(g).

## 4. De Rham compatibility, including at a node

One can see directly that the dualizing trace descends to the two-term log-de Rham complex. Let tau_0:S_0->R[x] be the ordinary algebra trace, tau_0(A+B y)=2A. Relative differentiation gives

    d(A+B y)=(2y A'+2(x^3+a x+b)B'+(3x^2+a)B)omega.

Consequently tau_1(d(A+B y))=2A' dx=d tau_0(A+B y). The same calculation holds in the infinity chart with its appropriate coefficients and -du/(2v) generator; the maps glue. Thus(tau_0,tau_1) is a morphism of the actual two-term complexes to the ordinary de Rham complex of P^1_R. This calculation uses polynomial identities, not division by y, a discriminant, or p. It works with p-torsion and on the nodal fiber.

Since H^1(P^1_R,O)=0, its top de Rham group is H^1(P^1_R,Omega^1), with the trace of Section3. The induced top de Rham map is exactly the proper dualizing trace after the canonical edge identification H^2_dR,log=H^1(L)/image H^1(d). In our particular family the prior proper calculation already proves H^1(d)=0, so this is the stated isomorphism Rg. The argument also explains why an arbitrary linear functional on an unrelated rank-two differential module would not suffice here.

## 5. Infinity, the cone sign, and the positive Gysin/Chern class

First, omega restricts to dz along D. Indeed u=z^2(1+a u^2+b u^3), v=-u/z, and omega=-du/(2v). This gives omega=(1+O(z))dz in the completed smooth neighborhood, with leading coefficient1. Algebraically the same assertion is omega|_D=dz|_D; hence after shrinking the smooth infinity chart, omega-dz is in zL. Therefore

    [(1/z)omega]=[dz/z]

in H^1(L), after refinement if necessary.

The following sign check is essential. It distinguishes a positively oriented local Gysin fraction from its representative in our ordered global Cech complex. Write U=Y_R-D and V for a sufficiently small affine smooth infinity neighborhood, ordered(U,V). Compute support in D by the standard cochain cone

    K=cone(Gamma(V,L)->Gamma(V-D,L))[-1].

With the usual cochain cone and shift, its differential from degree0 to degree1 is minus restriction. The forget-support map to the ordered Cech complex has components

    a -> (0,a) in degree0,
    b -> -b in degree1.

It is a chain map, since delta(0,a)=a and(-1)(-a)=a. Accordingly the positive local regular-immersion fraction dz/z maps to the global representative -dz/z. If the open containing the divisor is ordered first instead, the corresponding signs change together. A bare principal-part quotient with a positive localization differential cannot silently be identified with this shifted support complex without its comparison sign.

The local fundamental class is the regular-immersion/purity class determined by dz and the conormal generator z: it is the fraction dz/z in that support convention. Changing z to a unit times z changes the global representative by a regular one-form on V, so its class is unchanged. This is the usual local Gysin construction for the actual smooth Cartier section, not a class picked by the already computed value of Tr_R. It gives

    cl(D)=-[dz/z]=-g.

The same class is the first de Rham Chern class of O(D). To make the convention explicit, use local frames e_U=1, e_V=z^-1 for O(D), and describe their frame transition by e_V=e_U gamma_UV. The Chern cocycle in this convention is dlog gamma_UV=-dz/z. It agrees with the positive hyperplane convention on P^1: the frames X_0,X_1 for O(1) have gamma_01=x and give dx/x, of trace1 by Section3. Thus neither a reciprocal transition convention nor a reversed order of opens is being mixed into the infinity calculation.

Combining this actual Gysin computation with the proper trace proves

    Tr_R(cl(D))=Tr_R(-g)=1=degree(D/R).

The local smoothness of D is sufficient; it does not require all of Y_R to be smooth, and introduces no division by p. This is precisely the degree-one infinity normalization needed for the specified proper witness. It is not an independently constructed cycle-class theory on an unspecified formal crystalline site.

## 6. Coefficient maps, completions, and the saved pairing

All finite constructions were made with free monic-quadratic modules, the duality evaluation at1, the literal Laurent coefficient description on P^1, and a smooth Cartier section. They commute with arbitrary maps between the allowed coefficient rings. In particular the formulas Tr_R(g)=-1 and cl(D)=-g hold over B_n, A_n, R_n, their nonflat reductions and the central nodal fiber, without passage to a field. Where the all-PD paper applies, the maps on proper complexes match its actual crystalline/de Rham comparison maps; no new finite-site comparison theorem is asserted here.

For the already proved bounded A-flat proper complex C_A, apply these compatible trace maps to its two fixed towers

    C_A tensor_A A/p^n,
    C_A tensor_A A/(p^r,t^r).

The same explicit geometric construction over A supplies a chain-level trace in the derived category and its finite reductions; alternatively the compatible finite maps give their Rlim maps. Under the already proved quasi-isomorphisms C_A->W_p and C_A->W_pt, H^2 is Ag and each induced trace is a g->-a. The target coefficient towers have surjective transition maps and Rlim equal to A in degree0, by the same elementary 1-shift argument used for the named proper completions. This states compatibility for the p-adic and(p,t)-adic towers separately; it does not equate their topologies or their sites. No p-inversion occurs at a finite level, no Rlim is interchanged with t-inversion, and no new independent formal-site identity is claimed.

The lead author's new ordered-Cech/Alexander--Whitney computation gives w cup e=-g, e cup w=g and both self-products zero in this actual proper complex, where w and e are the specified corrected proper omega,eta classes. With the trace just proved, its traced matrix is therefore

    [[0,1],[-1,0]],  <omega,eta>=1.

This is a consequence of the actual proper trace and the actual cup representatives. It matches the saved constant convention identified in the lead component; it is not a second choice of trace made from that saved convention. The finite Frobenius/cup multiplier, its direction, the generic restriction, and its saved-frame consumption remain the lead author's assigned part of the joint paper. This component supplies no old full-relative rank-four object, no extension constants, no independent global functional, no isogeny comparison, and no closure of the original LC/parent objective.

## 7. Reuse and actual contribution

The proper family, basis, H^1/H^2 calculation, log-dualizing line, universal proper coefficient maps and the two named completion quasi-isomorphisms are reused with their existing hypotheses. The primary projective trace normalization and ordinary finite-duality adjunction are imported with the stated exact scope. The author supplies here the literal finite-cover trace construction, its overlap and de Rham checks, the infinity cone/Gysin sign check, and their concrete coefficient/completion application. These are author contributions to a RESULT_ONLY comparison/application, not a new general Tool, independent axiom, or independent general discovery. The native-line-trace inventory matches are different typed operations and do not cover this algebraic-geometric trace; no native X6 propagation claim is made by the external algebraic model. No scientific computation has been executed. The whole new paper still requires its distinct nonauthor reviewer.

Researcher-ID: EM-OWNERGOAL2026101-C89DC6 / TASK_RESEARCH
Global-Knowledge-Sync: main@464371f / GLOBAL_KNOWLEDGE_V1
