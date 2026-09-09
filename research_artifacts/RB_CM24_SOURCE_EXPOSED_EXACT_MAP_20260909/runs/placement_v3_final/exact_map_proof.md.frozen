# Source-exposed exact map: full algebraic certificate candidate

Status: `INCOMPLETE / SOURCE_EXPOSED / RESULT_ONLY CANDIDATE`.

This is the current researcher's proof using the published formula as data. The researcher also authored the preceding blind reduction and received the Owner's field, local-order and base-point proof suggestions in this shared conversation. This is not a blind reconstruction or an independent review. No formal Result or Driver acceptance is asserted here.

The immutable formula input is `source_freeze.json`, SHA256 `85946a8cb4e736021cef6cd311c8cfffbde1cce34fe728255db4b6703f5887f2`. Its seven exact source pins and its original N, D0, k, lambda and Y conventions are retained. The published v1 computation established the full cleared ODE, not just its restriction to three critical points. The new geometric claims below combine exact identities with explicit divisor arguments; the program does not count roots numerically.

## 1. The coefficient and function-field bases

Put alpha>0, alpha^4=3, beta>0, beta^2=2, i^2=-1 with the positive imaginary embedding, and s=alpha^2. Let L=Q(alpha,beta,i). The original journal's omission of i is retained as a historical error; the present field declaration includes i explicitly.

The polynomial x^4-3 is Eisenstein at 3, so Q(alpha) has degree four. It is real, hence adjoining i has degree two. K0=Q(alpha,i) is the degree-eight splitting field of x^4-3. Its automorphisms r(alpha)=i alpha, r(i)=i and complex conjugation s0 generate D4. Their commutator subgroup is <r^2>. Every quadratic subfield lies in its fixed field Q(sqrt(3),i); its three quadratic subfields are Q(sqrt(3)), Q(i), Q(sqrt(-3)). None is Q(sqrt(2)). Thus adjoining beta to K0 has degree two and [L:Q]=16.

Consequently alpha^a beta^b i^c, 0<=a<4, 0<=b,c<2, form an actual Q-basis under the specified embedding. This justifies both zero and nonzero coefficient normal forms. The reduction is a sequence of monic symbolic relations, not an evaluation of a root or a quotient.

On C, t^2=f(R)=R^3-3R. The rational function f has odd order at R=0, so it is not a square in L(R). Hence {1,t} is a basis of L(C) over L(R). Together these statements make every nonempty reduced dictionary in the certificate a genuine nonzero function, rather than merely an unproved formal nonzero remainder.

The reused `check_squareclass_rr.py` uses ten formal exponent slots. This execution identifies its slots a,b,c with alpha,beta,i, retains R,t, and rejects any occurrence of the other five slots. It reuses integer addition, scaling, multiplication, curve reduction, section difference and twice_delta without editing the old module. D=2 delta satisfies D(R)=2t and D(t)=3R^2-3. It annihilates every coefficient relation and D(t^2-R^3+3R)=0, so it descends to this function field.

## 2. Full ODE and the actual target

Write the frozen formula as X=N/D0 and C4=-i alpha(9+3 beta+2s+4s beta). Retain C=C4/4 as an unevaluated scalar quotient. The actual denominator-cleared derivative is

    W=D(N)D0-N D(D0)=2D0^2 delta(X).

The exact computation verifies, in the entire ring L[R,t]/(t^2-f),

    (R+2)t W^2=C4(t+k)^2 N(N-D0)(N-lambda D0)D0.

No substitution t=-k, evaluation at sample points or necessary-only critical filter is used. Since C4, D0 and W are nonzero, this is precisely

    (R+2)t(delta X)^2=C(t+k)^2 X(X-1)(X-lambda).

The source's Y convention is retained exactly:

    Y=w W/[2(t+k)D0^2]=w delta(X)/(t+k),
    w^2=(R+2)t.

It follows that Y^2=C X(X-1)(X-lambda). There is no extraction of sqrt(C) or alteration to the source's twist. The field-basis witnesses show C, lambda and 1-lambda are nonzero. Thus this equation has a nonsingular projective elliptic model. For example the L-isomorphism u=CX, v=CY gives v^2=u(u-C)(u-C lambda).

The usual algebraic Weierstrass invariant computation gives

    j=256(1-lambda+lambda^2)^3/[lambda^2(1-lambda)^2].

The certificate additionally checks the exact cleared identity with

    j=2417472+1707264 beta.

This identifies the invariant of this explicit target model. It does not by itself compute an analytic period, homology index or prove the historical period-normalization claim.

## 3. All common base points, and degree

Set a=3(s-1) and

    A=a t+i alpha uN(R+s)(R-LN),  N=(R+2)A,
    r=-3-3 beta-2s-s beta.

The program verifies r*s=-LN, uN=(beta-1)(3-2s), uD=-2-(s-1)(beta-1), and the complete identity

    Norm_{L(C)/L(R)}(A)=-s uN^2(R+s)(R+3s)(R-r)^2.

All constants multiplying these factors are nonzero. The relevant distinctness tests (r, r-s, r+s, r+2, r+3s) are recorded as nonzero field normal forms. In particular r is an ordinary, unramified R-value. The following describes zeros on the geometric curve; all selected points in this proof are already defined over L.

At Tminus=(-s,0), t is a local parameter, R+s has order two and a is nonzero. Therefore ord_Tminus(A)=1. At R=-3s, t is nonzero. Direct exact substitution verifies

    B0=(-3s,6 i beta alpha) lies on C, A(B0)=N(B0)=D0(B0)=0.

The norm has a simple factor R+3s and the opposite t-point is not a zero of A, because the t coefficient a is nonzero. Thus ord_B0(A)=ord_B0(N)=1. The certificate also displays the nonzero value of D(A) at B0 as an explicit witness.

At R=r only the single point

    Z=(r,tZ),  a*tZ=-i alpha uN(r+s)(r-LN)

can be a zero of A. The other t-point cannot also be a zero since a and tZ are nonzero. The cleared equation a^2*tZ^2=a^2*f(r) is checked exactly, and the norm factor has multiplicity two, so ord_Z(A)=2.

At each Pplus=(-2,i beta), Pminus=(-2,-i beta), R+2 has order one and A is nonzero; these values are distinct from every norm-A root. Hence N has exactly the following finite zero divisor:

    div_0(N)=[Pplus]+[Pminus]+[Tminus]+[B0]+2[Z].

To exclude other common zeros, the computation gives nonzero field values for D0(Pplus), D0(Pminus), D0(Tminus), and the cleared value a*D0(Z). They are not floating estimates. The coefficient/function-field bases proved in section 1 make these exact nonzero witnesses. These checks and the displayed exhaustive zero divisor show that B0 is the only finite common zero of N,D0. Its common minimum order is exactly one, because N has order one there. This argument alone does not determine the individual order of D0 at B0. The additional full-fiber calculation in section 5 now proves that order is also one; the v2 source and its earlier limitation remain immutable at their published checkpoint.

At the elliptic point O, R has pole order two and t has pole order three, with respective leading terms u^-2 and u^-3 for u=R/t. In N the unique highest pole order is six, with coefficient i alpha uN; in D0 it is seven, from t R^2 with coefficient one. The coefficients are nonzero. In a polynomial reduced to t-degree <=1, weights 2 deg_R and 2 deg_R+3 have opposite parity, so no R/t cross-term can cancel a highest pole order. The exact N,D0 dictionaries verify these orders.

As sections of L(7O), N has order one at O and D0 has order zero; O is not a common base point. Thus the entire common base divisor is [B0]. Removing it from the two sections of L(7O) produces a base-point-free degree-six pencil, equivalently

    deg_C(X)=7-1=6.

Let D be the smooth projective normalization of w^2=(R+2)t over C. Its function field has degree two over L(C), since (R+2)t has odd order at T0, for example. The rational functions X,Y give the morphism to the nonsingular projective target by the extension argument in section 4. The target's X-coordinate has degree two, because its cubic has three distinct roots and is not a square in L(X). The function-field tower gives

    [L(D):L(X)]=2*6=12=2*[L(D):L(X,Y)],

so the actual map D -> E has degree six. The degree fields in the JSON are this divisor/tower theorem linked to its exact checks; they are not direct software root counts.

## 4. Unsquared differential and exceptional points

On the dense open set where the displayed denominators are nonzero, the derivative identity and the chosen Y give

    dX/Y = (t+k)/(w t) dR = (dR/w)(1+k/t) = phi.

This is unsquared and fixes the sign. With Y replaced by -Y, the target equation is unchanged but the difference dX/(-Y)-phi equals -2phi, which is nonzero. The countercheck clears denominators and exhibits a nonzero doubled numerator; it does not infer a sign from the squared ODE.

A rational map from a nonsingular source curve to this projective target extends uniquely at every missing point. One can see this directly in the source DVR: scale homogeneous coordinates by the least valuation, so all become integral and at least one is a unit; the target's homogeneous equation remains satisfied. These extensions agree on the dense open set. This is also the standard normal-curve/proper-target extension theorem (Stacks Project, Tag 0BXZ; primary reference read by the Owner). It establishes extension of the map, not the base-point or degree calculations above.

For completeness phi itself is regular at every possible exceptional point on D. At the three points t=0 over C, normalization gives orders

    ord(R-r0,t,w,dR)=(4,2,1,3),

so phi has order zero. At the two points over R=-2 the orders of R+2,w,dR are (2,1,1); t and t+k are units because k^2 is not -2, so phi again has order zero. At O the orders are (-4,-6,-5,-5) for R,t,w,dR; 1+k/t is a unit, so the order is zero. Every claim k!=0, k^2!=0, k^2!=2, k^2!=-2 is certified by a nonzero field normal form.

Away from these points phi can vanish only at t=-k. The cubic R^3-3R-k^2 has three distinct roots because k^2 is neither 2 nor -2; they avoid all six branch points and t is nonzero. At each root, t+k has a simple zero. Each has two unramified lifts to D, giving exactly six simple zeros of phi. Riemann-Hurwitz for the double cover of the genus-one C with six simple branch points gives g(D)=4, consistent with total canonical order six. The differential equality therefore extends globally and has no omitted pole or hidden sign repair at a canceled point.

## 5. Complete special fibers, including the canceled point

Put A1=N-D0 and Al=N-lambda*D0. The next exact computation proves three full conjugate-norm factorizations:

    Norm(D0)=-R(R-s)(R+3s) q2(R)^2,
    Norm(A1)=-(R+3s) q3(R)^2,
    Norm(Al)=-(R+3s) ql(R)^2.

The certified polynomial numerators are Q2=8*q2, Q3=16*q3 and Ql=16*lambda^5*ql. Their complete integer normal forms are in the certificate. q2 and q3 are monic, and ql has leading coefficient lambda. Every displayed denominator is symbolic and nonzero. Their construction compares the highest coefficients and then checks the entire squared polynomial, not only those coefficients.

For clarity, the method recovers a square without evaluating a scalar quotient. For a quartic F with leading coefficient c, put A=[R^3]F and B=4c[R^2]F-A^2. The candidate S=8c^2 R^2+4cAR+B is accepted only if S^2=64c^3 F exactly. The analogous sextic uses A=[R^5]F, B=4c[R^4]F-A^2, E=8c^2[R^3]F-AB, and S=16c^3 R^3+8c^2AR^2+2cBR+E, checking S^2=256c^5 F. Thus an incorrect lower coefficient fails the full identity.

For each Q2,Q3,Ql the checker gives a nonzero terminal constant in its pseudo-remainder chain with its derivative, proving it squarefree over L and hence over the algebraic closure. The chain with the t coefficient of D0,A1,Al respectively also ends in a nonzero constant. Every chain retains its leading-coefficient multipliers and verifies M*a=q*b+r at each step; no division or coefficient-content cancellation is used. Consequently a root of one of these factors selects exactly one of the two t-points, not two opposite simple zeros. Direct exact evaluations show all three factors avoid R=0,s,-s,-2,-3s. Thus they avoid the double-cover branch locus and B0.

Let E_inf be the effective degree-two divisor selected by Q2(R)=0, D0=0; let E_1 be the degree-three divisor selected by Q3(R)=0, A1=0; and let E_l be the degree-three divisor selected by Ql(R)=0, Al=0. These are reduced, L-defined effective divisors. Individual points need not be L-rational: the displayed equations specify the entire Galois-invariant divisor without silently adjoining or choosing roots. At each such point the norm has order two in the unramified local R-parameter and the opposite sheet is nonzero, so the relevant function has order two.

The factor R+3s occurs simply in all three norms. Each function vanishes at B0, an unramified R-point, and therefore each has order exactly one there. In particular D0, N, A1 and Al all have order one at B0. After cancellation X(B0) is finite, nonzero, and different from 1 and lambda. It can be specified exactly as D(N)(B0)/D(D0)(B0), with nonzero denominator; no numerical evaluation is needed. This resolves the individual-order limitation explicitly retained at v2.

At T0 and Tplus, D0 has order one: t is a local parameter and the nonzero QD value is the coefficient of its linear term; the other summand has order at least two. At O, A1 and Al have pole order seven with nonzero leading coefficients -1 and -lambda. Combining these facts with section 3 gives the complete divisors on C:

    div(X)   = [O]+[Tminus]+[Pplus]+[Pminus]+2[Z]
               -[T0]-[Tplus]-2E_inf,
    div(X-1) = 2E_1-[T0]-[Tplus]-2E_inf,
    div(X-lambda) = 2E_l-[T0]-[Tplus]-2E_inf.

Each zero fiber has total degree six, as does the pole fiber. There are no omitted points, poles, common factors or higher local orders. At a source double-cover branch point, the multiplicity in its special X fiber is exactly one. Thus the branch labels in the fixed source order (O,T0,Tplus,Tminus,Pplus,Pminus) are exactly (0,infinity,infinity,0,0,0). The zero and infinity blocks have sizes four and two; the one and lambda blocks are empty. A block being empty means absence of source double-cover branch points in that fiber, not absence of the fiber's degree-six inverse image.

## 6. Explicit half-point and unramified classes over L

First use the fixed-lambda translation

    x'=(X-lambda)/(X-1),
    Y'=(lambda-1)Y/(X-1)^2.

It transports old labels by (0 lambda)(1 infinity). The new finite zero block is empty, the one block is {T0,Tplus}, and the lambda block is {O,Tminus,Pplus,Pminus}; infinity is empty. Direct rational multiplication gives Y'^2=C*x'(x'-1)(x'-lambda) and dx'/Y'=dX/Y, so k, C and the differential direction are unchanged. This is a target V4 operation, not t -> -t, a source flip, or an anharmonic change of lambda.

Choose the following actual L-rational half-point, rather than an unspecified root:

    Q=(xQ,tQ), xQ=s(beta-1), tQ=i*beta*alpha^3*(beta-1),
    ell=2tQ*t-(3xQ^2-3)R+(3xQ^2-3)xQ-2tQ^2.

The checker verifies Q lies on C, ell(Q)=0, and

    Norm(ell)=-4tQ^2(R-xQ)^2(R+s).

tQ and xQ+s are nonzero. The line is the tangent at Q and its remaining intersection is Tminus, so 2Q=Tminus=T0+Tplus. Its rational divisor is 2[Q]+[Tminus]-3[O]. The chord of T0,Tplus is t, hence

    g=t/ell, div(g)=[T0]+[Tplus]-2[Q].

Use G0=1, G1=g, Gl=(R+2)ell. Their product is exactly F=(R+2)t, and these are precisely the base representatives allowed by the frozen square-class paper with its now specified half-point.

Here are explicit L-rational certificates for the unramified parts h0=x', h1=(x'-1)/g, hl=(x'-lambda)/Gl. For a function h=n/d whose conjugate norm equals H^2, put r=Tr(h)+2H. Then

    (h+H)^2=h*r.

This is a function-field identity with the involution t -> -t used only for the norm; it is not an equivalence of fixed-k maps. For h0 take H=Ql/(lambda^5 Q3). For h1 take

    H=4tQ(1-lambda)(R-xQ)Q2/Q3.

Both full norm equalities are checked. Write r=U/V by clearing these displayed denominators. The exact monic deflations and retained pseudo-quotient give

    M*U=removed*Q3*B,
    256*V=c*removed*Q3^3,
    K*B=J*S^2.

Here the certificate contains every coefficient of U,V,B,S and the nonzero scalar M,K,c, together with the identities. For h0, removed=R+3s, c=-lambda^5, J=R(R+s), M=16777216. For h1, removed=(R+3s)R(R-s)(R+s), c=1, J=R, M=1048576. The remaining degree-four polynomial in each case is checked to be a scalar square, and the exact branch valuations are respectively (1,0,1) and (1,0,0), in the order T0,Tplus,Tminus. Thus this is a square-class calculation, not a parity guess from the original 4+2 blocks.

Since R(R+s)=(R-s)*(t/(R-s))^2, the two actual classes are gamma_Tplus=R-s and gamma_T0=R. More concretely, with the indices 0,1 on M,K,S denoting these two computations, set

    alpha0=-M0*lambda^5*K0/256,
    alpha1=M1*K1/256,
    u0=(lambda^5 Q3 Al+Ql A1)/(lambda^5 A1*t*S0),
    u1=(Q3(1-lambda)D0*ell + H1num*A1*t)/(A1*t*R*S1),
    H1num=4tQ(1-lambda)(R-xQ)Q2.

The actual checker independently clears these expressions and verifies

    h0=alpha0*(R-s)*u0^2,
    h1=alpha1*R*u1^2.

All numerator and denominator functions are nonzero in the proved field basis. No constant has been declared a square or replaced by a floating approximation. For the third class put

    Hprod=(lambda-1)W/((t+k)A1^2),
    alphal=1/(C4*alpha0*alpha1),
    ul=Hprod/(t*u0*u1).

The full ODE gives h0*h1*hl=Hprod^2/C4 and R(R-s)(R+s)=t^2. Therefore hl=alphal*(R+s)*ul^2. The implementation also checks the complete third cleared reconstruction directly, independently of merely outputting this label. Thus the actual twist triple for x' is (Tplus,T0,Tminus), with all three scalar/function pairs over L explicitly retained. In particular C4*alpha0*alpha1*alphal=1; no extra constant extension is needed for this representation.

## 7. Exact matching to the frozen representative and RR divisor

The frozen assignment certificate uses source order (O,T0,Tplus,Tminus,Pplus,Pminus), target order (0,1,lambda,infinity), and only the four fixed-parameter V4 permutations. The new five-source binding checks the old assignment, corrected RR certificate/paper, empty-fiber paper, and raw freeze against the exact source commit 3a00ea191ad0380bf341af746a825e0b0c474874. These files were not edited, and their old enumeration was not rerun.

The actual source assignment (0,3,3,0,0,0) is already its fixed-parameter representative. Its unique frozen row chooses the lexicographically minimal empty-infinity representative (1,2,2,1,1,1), with transport (1,0,3,2). The auxiliary x' above is another legitimate empty-infinity coordinate, but is not that stored row. Apply the additional V4 translation

    z=lambda/x'=lambda*(X-1)/(X-lambda),
    Yz=-lambda*Y'/x'^2=lambda*(1-lambda)Y/(X-lambda)^2.

It preserves the same target equation and dz/Yz=phi. The checker runs the full fixed-k ODE again on the actual numerator lambda*A1 and denominator Al, and checks Wz=lambda*(1-lambda)W. Thus the composite transport, constants and derivative sign are tested, not inferred from a label count.

For z take G0=1, G1=(R+2)ell, Gl=g. Its branch blocks are empty, four-point and two-point, in that order. Write gp=R-s, gm=R+s. Explicit square-class representatives transported from section 6 are

    a0=lambda/alpha0, v0=1/(gp*u0),
    a1=-alphal/alpha0, v1=t*ul/(R*gp*u0),
    al=-lambda*alpha1/alpha0, vl=t*u1/(gp*gm*u0).

They give z=a0*G0*gp*v0^2, z-1=a1*G1*R*v1^2, z-lambda=al*Gl*gm*vl^2. The identities use gm/gp=R*(t/(R*gp))^2 and R/gp=gm*(t/(gp*gm))^2. The canonical triple is again (Tplus,T0,Tminus), relative to the displayed actual Q. Changing a base half-point would permute these geometric labels and scalar factors, so this precise choice is part of the result.

All finite scalar factors and all functions here lie in L. This proves descent of this displayed representation and map to the declared L, not to the smaller real field of the original erroneous field sentence. In particular the fixed nonzero k is imaginary, so one cannot erase i from the complete fixed-embedding data. No assertion of minimal coefficient field or descent of a different isomorphic model is made.

The canonical pole divisor is 2E_l. The effective degree-three divisor D_inf=E_l is explicitly L-defined by Ql(R)=0 and Al=0, not replaced by 3O. Its Picard class can be specified exactly as S=sum(E_l), under Pic^0(C)=C. From div(Al)=[B0]+2E_l-7[O], one obtains 2S=-B0. Since B0 is a finite non-origin point, S is not O. This supplies the actual general degree-three pole-class parameter as an L-rational Picard class; solving cubic point coordinates separately is unnecessary and is not claimed.

The three effective even zero parts for z,z-1,z-lambda are respectively E_1,[Z],E_inf. With the displayed half-point the base divisors are B_0=0, B_1=3[O]-[Q], B_l=[Q]. After the gamma twists, put B'_a=B_a+[O]-[T_a]. The exact identities imply

    div(v_a)=E_a-E_l+B'_a,
    v_a in L(E_l-B'_a).

Their positive degrees, hence genus-one RR dimensions, are (3,1,2), exactly the dimensions in the matched frozen row. Their two section equations are the corrected identities z-(z-1)=1 and z-(z-lambda)=lambda, with the same denominator/pole data. The product gamma is t^2. If eta=-lambda/alpha0^2, then eta^2=C4*a0*a1*al and

    2 delta(z)/(t+k)=eta*t*v0*v1*vl,
    delta(z)=(eta/2)*t*(t+k)*v0*v1*vl.

The sign follows from the explicit Yz transformation; it is not chosen by taking a square root. This also exhibits the old RR differential equation with a retained, nonzero scalar eta/2.

The empty finite block has nontrivial class Tplus, so this is a surviving 4+2 component, outside the 180 components excluded for a geometrically square empty fiber. The actual non-O pole class is also explicit. This is one map in one retained parameter component. It does not turn 1980 parameter families into a count of maps, solve the other components, or reverse any earlier valid exclusion.

## 8. Status and remaining acceptance boundary

The complete function-field ODE, target and j invariant, base-point cancellation, both degree-six claims, all four special-fiber divisors, explicit half-point and L-rational square classes, canonical fixed-parameter assignment, RR pole class and unsquared global differential now have the stated algebraic proof and actual exact checks. They concern this pinned source-exposed formula only. The candidate remains administratively INCOMPLETE until the complete proof receives the required independent checking and the gate-by-gate durable return is frozen; this status is not a newly weakened mathematical hard target.

No conclusion finishes the 1980-family classification, the period/homology index, an independent blind reconstruction, Working Truth or Foundation promotion. The parent gaps remain OPEN. No canonical Result or Driver verdict is created by this proof or its checker.

## 9. Computation and replay scope

Actual v1 and geometric-v2 source copies, certificates, stdout/stderr and receipts are kept under `runs/identity_v1/` and `runs/geometry_v2/`. The archived `.py.frozen` file is an exact source archive, not an alternate Python package entry point. Restore it at its canonical original path in an isolated checkout, or use the corresponding immutable source commit and that path. For an old receipt choose its old certificate with `--output`; do not compare an old checker with a later primary certificate.

The actual inline parent runner used `subprocess.run(..., timeout=600)`. The child sets the 4096 MiB Windows Job process-memory cap and checks a monotonic deadline at normalization boundaries; its cooperative checks alone are not a hard interruption of an in-progress multiplication or JSON encoding. The cap is an upper bound, not a measured peak. No natural-number quotient/root was requested in these checks, so actual BRC evaluations are zero. The reused integer polynomial APIs were actually called; coverage-only facade/precision tools are not labelled executed. Import, source hash and selected static-policy evidence do not by themselves certify all unrelated legacy code.
