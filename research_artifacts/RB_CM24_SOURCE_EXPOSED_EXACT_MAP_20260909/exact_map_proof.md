# Source-exposed exact map: identity and degree checkpoint

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

To exclude other common zeros, the computation gives nonzero field values for D0(Pplus), D0(Pminus), D0(Tminus), and the cleared value a*D0(Z). They are not floating estimates. The coefficient/function-field bases proved in section 1 make these exact nonzero witnesses. These checks and the displayed exhaustive zero divisor show that B0 is the only finite common zero of N,D0. Its common minimum order is exactly one, because N has order one there. **This does not yet determine the individual order of D0 at B0 or the value of X after cancellation there.** Those belong to the remaining full-fiber gate.

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

## 5. Boundary of this checkpoint

The full ODE/target identity, exact field/model facts, common-base divisor, degree and unsquared differential are now supported by the displayed algebra and proof. The hard target remains unchanged and this checkpoint remains INCOMPLETE. All four **complete** special-fiber divisors and their placement in the frozen, V4-normalized square-class/half-point classification are still to be finished. In particular the original formula's two empty fibers are 1 and lambda; an empty-infinity RR normalization must explicitly transport the target labels and Y, rather than use the original infinity fiber as though it were empty. Constant square classes and original-field descent must remain visible.

No conclusion here finishes the 1980-family classification, the period/homology index, an independent blind reconstruction, Working Truth or Foundation promotion. Full task PASS still requires the remaining gate plus appropriate independent checking and the exact durable return.

## 6. Computation and replay scope

Actual v1 and geometric-v2 source copies, certificates, stdout/stderr and receipts are kept under `runs/identity_v1/` and `runs/geometry_v2/`. The archived `.py.frozen` file is an exact source archive, not an alternate Python package entry point. Restore it at its canonical original path in an isolated checkout, or use the corresponding immutable source commit and that path. For an old receipt choose its old certificate with `--output`; do not compare an old checker with a later primary certificate.

The actual inline parent runner used `subprocess.run(..., timeout=600)`. The child sets the 4096 MiB Windows Job process-memory cap and checks a monotonic deadline at normalization boundaries; its cooperative checks alone are not a hard interruption of an in-progress multiplication or JSON encoding. The cap is an upper bound, not a measured peak. No natural-number quotient/root was requested in these checks, so actual BRC evaluations are zero. The reused integer polynomial APIs were actually called; coverage-only facade/precision tools are not labelled executed. Import, source hash and selected static-policy evidence do not by themselves certify all unrelated legacy code.
