# P11 off-diagonal: a cut-preserving infinite primitive family

Researcher: **EM-P000-298FC9**. Session MCP-b0a6f2120b6f48d5ad3096180d42e0e1; RA-A10B7F7B4F7D04C137083FC2. Task RS-P000-P11-OFF-DIAGONAL-EQUAL-AREA-FIBER-PRODUCT; publication TP2-74D161216AAF385EE27F. Claim MCP-d4a06240a4876acc1ab18e8f, authenticated epoch 6060656264; ER-8AAACF67EF70A0F0126A; run RUN-bad5f7abfc8667ef2a63c7ac, generation 1.

This is a Researcher proof checkpoint, not a Driver acceptance or parent closure. The main new theorem is an explicit infinite sequence of pairwise different primitive off-diagonal P11 data. It is not the inherited scaling orbit of one datum. The full global primitive classification, ranks/generators of all fibers, and global zero-column classification are not claimed.

All triangles, curves and projective varieties here are external/derived arithmetic carriers. P000 remains the six-dimensional discrete Cell ontology with no native plane. The arithmetic is static, so no time coordinate is required. Both ordered triangle factors, their coupling sign, all square witnesses, denominators, parity, zero/composite values and sixteen recovered roots remain part of the retained carrier.

## 1. Inherited input and exact new reduction

Consume the accepted simultaneous Result RR-DA840CA11911B721506F and its Return at their stated strength. For ordered positive triangles

\[
P=(x,y,b),\quad Q=(X,Y,g),\quad x>y>0,\quad X>Y>0,
\]
\[
x^2+y^2=b^2,\quad X^2+Y^2=g^2,\quad xy=XY=2e,
\]
write
\[
a=x+y,\ c=x-y,\ f=X+Y,\ k=X-Y,
\quad K=g^2-b^2.
\]
Off diagonal means exactly K != 0. The parent proves the normal form, root-gcd normalization and factor swap; none is claimed as a new result here.

For a fixed rational ordered core (P,Q), put
\[
A=(a^2+f^2)/2,\qquad C=(c^2+k^2)/2.
\]
Then A>C>0 and A-C=8e. The remaining rational cut carrier is exactly
\[
\mathcal C_{A,C}:\quad d^2+\mu^2=A,\qquad d^2+\nu^2=C,\quad d>0. \tag{1}
\]
Every such point reconstructs
\[
h=K/(4d),\qquad t=((h-d)^2-b^2)/4,
\quad H=(h-d,h,h+d),\quad T=(t-e,t,t+e). \tag{2}
\]
Conversely every off-diagonal normal-form datum with that ordered core yields (1) and (2). The denominator d is nonzero by the strict row AP, and K != 0 ensures h != 0. Absolute values of mu and nu select the canonical nonnegative discriminant roots; both auxiliary signs can instead be retained in the curve carrier.

For integral cores, integral output requires exactly 4d | K, both integral square witnesses, and the parent's explicit parity conditions. Equivalently rational roots may be reconstructed first, cleared by one common denominator, and then normalized as in Section 3. The latter route does not assume parity: it proves it by actual integer roots.

The projective closure
\[
d^2+\mu^2=Aw^2,\qquad d^2+\nu^2=Cw^2
\]
is a smooth complete intersection of two quadrics in external projective 3-space. Indeed a dependence of the gradients with coefficients alpha,beta gives
\[
(\alpha+\beta)d=0,\ \alpha\mu=0,\ \beta\nu=0,
\ (A\alpha+C\beta)w=0.
\]
If one coefficient vanishes, the other equations force all coordinates zero. If both are nonzero, mu=nu=0, so (A-C)w^2=0 and then d=w=0, again impossible. Thus it is a genus-one curve (the standard smooth (2,2) complete-intersection genus formula). Existence of a rational point is still an arithmetic condition; genus one alone does not assert one exists.

The exact map to an elliptic curve is
\[
E_{A,C}:v^2=u(u-A)(u-C),\qquad (u,v)=(d^2,d\mu\nu). \tag{3}
\]
It has generically four sign preimages, not a claimed birational inverse. Its rational affine image away from v=0 is precisely the square-class locus
\[
[u]=[1],\quad[u-A]=[-1],\quad[u-C]=[-1]
\quad\text{in }\mathbb Q^*/\mathbb Q^{*2}. \tag{4}
\]
The inverse consists of the positive rational roots d=sqrt(u), mu=sqrt(A-u), nu=sqrt(C-u), plus retained sign choices satisfying d mu nu=v if the signed curve point is needed. In particular (4), rather than a point on E alone, is essential. No independent-triangle or unordered-factor quotient is taken.

## 2. A uniform new infinite-family theorem

Fix the inherited ordered core
\[
P=(21,20,29),\qquad Q=(35,12,37),\qquad e=210.
\]
Its invariants are
\[
(a,b,c;f,g,k)=(41,29,1;47,37,23),\quad K=528,
\quad A=1945,\quad C=265.
\]
The classical elliptic curve and rational seed are
\[
E:v^2=u(u-1945)(u-265),\qquad P_0=(9,2112). \tag{5}
\]
This seed encodes the old witness d=3, mu=44, nu=16. The new construction uses its elliptic group orbit, not its common-root scaling orbit.

**Theorem.** For each positive odd integer n, form nP_0=(u_n,v_n) by the ordinary elliptic group law, and set
\[
d_n=\sqrt{u_n}>0,\quad \mu_n=\sqrt{1945-u_n}>0,
\quad \nu_n=\sqrt{265-u_n}>0,\quad h_n=132/d_n,
\quad t_n=((h_n-d_n)^2-841)/4. \tag{6}
\]
All three displayed square roots are rational. Reconstruct the sixteen rational roots from (6), and let D_n be their least common denominator. Then
\[
H_n=D_n(h_n-d_n,h_n,h_n+d_n),
\quad T_n=D_n^2(t_n-210,t_n,t_n+210) \tag{7}
\]
are strict integer AP data with all eight outer cells pairable, h != 0, common recovered-root gcd 1, and ordered triangle factors D_n P,D_n Q. Distinct positive odd n give distinct primitive data. Thus (7) is an explicit infinite primitive off-diagonal family.

Here “explicit” means an exact rational group-law algorithm with a proved all-n domain, rational-square extraction and specified denominator normalization. It does not claim a rational parametrization of a genus-one curve by one free rational variable or a list of all its rational points.

### 2.1 Non-torsion is certified without a rank computation

The cubic in (5) is integral, monic and nonsingular. Its polynomial discriminant, up to the irrelevant sign convention, is
\[
\Delta_f=1945^2\,265^2\,1680^2.
\]
The prime 11 divides 2112 but divides none of 1945,265,1680. Hence 2112^2 does not divide Delta_f. The Lutz–Nagell theorem for integral monic cubics implies P_0 has infinite order. The exact checker also finds Delta_f mod 11 = 3 and
\[
\text{slope}(P_0)=29743/264,\qquad
u(2P_0)=1037419681/69696,
\]
whose nonintegrality is a second check of the same torsion obstruction. No CAS rank, rank upper bound, saturation or conjectural analytic rank is used.

Reference: Trinity College Dublin, *Elliptic Curves*, Chapter 6, Theorem 6.2, PDF pp. 91–94, https://www.maths.tcd.ie/pub/Maths/Courseware/EllipticCurves/EllipticCurves.pdf . This is prior classical mathematics; the task-specific part is the checked specialization.

### 2.2 Every odd multiple keeps both square cuts

For e_i in {0,1945,265}, write delta_i(R)=[u(R)-e_i]. The square-class multiplication law needed here has a direct proof. If a nonvertical line v=L(u) meets E at R,S,T with multiplicities, then
\[
f(u)-L(u)^2=(u-u_R)(u-u_S)(u-u_T).
\]
Evaluation at e_i, using f(e_i)=0, gives
\[
(u_R-e_i)(u_S-e_i)(u_T-e_i)=L(e_i)^2.
\]
Since T=-(R+S) and negation preserves u, delta_i(R+S)=delta_i(R)delta_i(S). The same calculation with a tangent proves delta_i(2R)=1. The factors used below never vanish: all nonzero multiples of P_0 have infinite order, whereas v=0 and the point at infinity are torsion. Inductively add 2P_0 to the previous odd multiple; the line is nonvertical because an odd multiple cannot equal plus or minus 2P_0. This avoids any unproved exceptional-point convention for the descent map.

At P_0 the three factors are 9,-1936,-256, whose square classes are (1,-1,-1). Every positive odd multiple therefore has those same classes. They give exactly the rational square roots in (6). Their signs also imply 0<u_n<265, so d_n,mu_n,nu_n are nonzero, real and rational. Equation (1) is now satisfied for every n, proving both cuts uniformly rather than by finite testing.

### 2.3 Primitive normalization and distinctness

Apply Section 3 to the rational reconstructed roots. Their upper-right discriminant is c=1. Consequently D_n clears the roots, gives all parity conditions, and already has gcd 1; no unexplained gcd cancellation or denominator deletion is present. All root pairs and both triangle factors are recovered by the inherited normal-form equivalence.

If two members of (7) were equal, the top-middle discriminant 29D_n would identify D_n. The row step would then identify d_n. Equal d implies equal u and hence nP_0=plus or minus mP_0. Infinite order and positive odd n,m force n=m. More generally the scaling-invariant ratio (row step)/(top hypotenuse)=d_n/29 already proves the primitive classes are distinct. The same argument keeps them distinct even after adding the factor-swap partners: the original branch has h>0 and the swapped branch h<0.

## 3. Exact denominator and sixteen-root gcd theorem

For any rational normal-form datum let
\[
\mathscr R=\{(h-d\pm a)/2,(h-d\pm b)/2,(h-d\pm c)/2,
(h\pm\mu)/2,(h\pm\nu)/2,
(h+d\pm f)/2,(h+d\pm g)/2,(h+d\pm k)/2\}
\]
be the multiset of all sixteen roots, with every cell position retained. Let D=lcm of their positive reduced denominators. Then D R is integral, and
\[
G=\gcd\{|Dr|:r\in\mathscr R\}>0
\]
gives the precise primitive scaling D/G. The positivity follows from e>0. Sum and product recovery directly give integer AP coordinates D H,D^2 T; dividing the actual roots by G proves the primitive datum. Zero roots do not affect the gcd.

There is a stronger useful calibration: **when the rational core is normalized to c=1, G=1 automatically.** The difference of the upper-right two scaled roots is D, so G divides D. If G>1, the smaller positive integer D/G would clear all rational roots, contradicting the definition of D. This proves the claim.

This calibration is globally available because c=x-y is strictly positive. Divide any rational normal-form datum by c at the root level before reconstruction; the ordered factors and K scale accordingly. For an already primitive integral datum, this normalization recovers D=c: the least denominator of r_i/c equals c/gcd(c,r_1,...,r_16)=c. It is therefore a reversible scaling normalization, not an erasure of the common scale in an unscaled observer. The stored carrier retains D and the original ordered root grid.

For the family in Section 2, c=1 without further rescaling. Any other positive integral scale L giving integer roots must be a multiple of D, and its common-root gcd is exactly L/D. This separates the new infinitely many primitive members from their nonprimitive scaling orbits.

## 4. Exact triangle parametrization and residual global object

Each positive integer right triangle has the classical complete Euclid form
\[
(x,y,b)=\bigl(s\max(m^2-n^2,2mn),\ s\min(m^2-n^2,2mn),\ s(m^2+n^2)\bigr),
\]
where s>0, m>n>0 are integers, gcd(m,n)=1 and m,n have opposite parity. The primitive leg order is restored by max/min; the two triangle factors remain separately labeled. Give the second factor its own (S,M,N). Their exact common-area equation is
\[
s^2mn(m^2-n^2)=S^2MN(M^2-N^2). \tag{8}
\]
No factor equality is substituted for (8). With K != 0, (8), (1), (2), the explicit parity conditions or the actual-root denominator construction, and primitive normalization are necessary and sufficient. The full off-diagonal problem is thus a family of the smooth genus-one cut curves (1) over the ordered equal-area Euclid parameter locus (8), with K=0 excluded. This identifies the object by exact equations and mutually inverse reconstruction, not by naming a surface by analogy. It does not assert that all these fibers have points, positive rank or the same arithmetic as the displayed fiber.

The universal model and Euclid parametrization are compositions of classical machinery with the inherited normal form. The new substantive result is that one specified off-diagonal fiber has a cut-preserving non-torsion orbit whose primitive reconstruction is injective.

## 5. Zero-column and sign strata are kept separate

For any fixed ordered core and each s in {1,0,-1}, a zero left/middle/right product column is respectively t=s e. Let
\[
(u_s,v_s)=(a,f),\ (b,g),\ (c,k)
\]
for s=1,0,-1. Necessarily and sufficiently, for one of the four sign pairs epsilon,eta in {+1,-1},
\[
h-d=\epsilon u_s,\quad h+d=\eta v_s,
\quad d=(\eta v_s-\epsilon u_s)/2>0,
\quad h=(\eta v_s+\epsilon u_s)/2\ne0, \tag{9}
\]
and the remaining nonautomatic cuts/parity hold. The row coupling follows because v_s^2-u_s^2=K. The middle cuts are precisely
\[
\mu^2=h^2-4(s-1)e,\qquad\nu^2=h^2-4(s+1)e. \tag{10}
\]
Thus the left-zero stratum has mu=|h| and the remaining cut nu^2=h^2-8e; the right-zero stratum has nu=|h| and mu^2=h^2+8e; the middle-zero stratum retains both mu^2=h^2+4e and nu^2=h^2-4e. Equations (8)–(10), signs, parity and the root gcd are an exact residual description of the global zero-column strata. They are not claimed to enumerate their global primitive solutions.

On the specific core of Section 2 the full zero-column classification is elementary and complete. Since h=132/d and 0<d<sqrt(265), solving t=e,0,-e gives positive candidates respectively
\[
d\in\{3,44\},\quad\{4,33\},\quad\{11,12\}.
\]
The values 44 and 33 exceed the cut interval. At d=4, C-d^2=249 is not a square. At d=11, A-d^2=1824 is not a square. At d=12, A-d^2=1801 is not a square. Exactly d=3 survives, with (mu,nu)=(44,16). Therefore this fixed-core zero-column family is exactly the inherited common-root scaling orbit (and its factor-swapped partner), whose primitive member is the old witness. The odd-multiple construction for every n>=3 leaves this boundary: equality d_n=3 would give nP_0=plus or minus P_0, impossible for infinite-order P_0.

Signs of recovered roots are never filtered: a negative column product gives opposite-sign roots; a positive product gives roots of the same sign; a zero product gives a zero root. The output retains the exact signs of H and T. The n=3 member has product signs (-,-,+), establishing a primitive off-boundary sign chamber different from the old zero-left witness. No assertion that the six regression sign patterns classify the entire real/rational orbit is made.

## 6. Concrete new member and finite verification

For n=3 the checker obtains
\[
d=8862094557/1036792417,\quad
\mu=44857760684/1036792417,\quad
\nu=14363912656/1036792417,
\]
\[
h=45618866348/2954031519,\qquad D=3062717478478191423.
\]
Its primitive integer data are
\[
H=(21118388056006541033,\ 47297294701742883116,\ 73476201347479225199),
\]
\[
T=(-3830548589317064615694537259248900784640,
-1860698535192144317804764879992440149550,
109151518932775980085007499264020485540).
\]
All sixteen roots, exact fractions and normal-form values are in offdiag_checks.json. They were checked against the inherited parent checker, imported with unchanged bytes. That imported code performs direct sum/product recovery, all cuts/parity and the actual sixteen-root gcd. The old root-height census is not rerun.

The predeclared finite set n=1,3,5,7,9,11 passed exact curve arithmetic, rational-square checks, integer reconstruction, gcd 1, ordered-factor recovery, distinct d/29 and factor-swap tests. The largest clearing denominator has 272 decimal digits. The polynomial chord identity and every fixed-core zero-column candidate were also checked. This is regression evidence; infinitude rests on Sections 2.1–2.3.

## 7. Observer/BRC accounting and remaining work

Retained: ordered P,Q; common-area relation; K and h sign; d,mu,nu; the signed elliptic point and integer n as auxiliary orbit provenance; all rational denominators and D; all sixteen cell-labeled roots; their exact scale and primitive gcd; AP H,T and zero/sign chambers. No prime-only view, factor-only interaction erasure or Boolean support replacement is taken.

The nonnegative discriminant convention forgets the sign of a square witness only for the declared unordered-root-pair reconstruction, for which the two signs visibly give the same pair. The signed elliptic point is still retained because group addition would not descend through simply forgetting v. The scaling-normalized readout has an exact inverse after D is restored; it is not declared safe for arbitrary unlisted operations. This applies T0_BRC provenance discipline and T6 observer-safe reconstruction. The static carrier lacks a supplied BRC path-composition law; no executable BRC transport or affine-moment theorem is asserted.

Smallest outstanding delivery units: independent line-Driver audit of this new uniform family and denominator argument; assess all required Task outputs against this strength; persist Source checkpoint and, only after the actual terminal scope is agreed and native conditions hold, a formal immutable Result. Mathematical residuals remain: global classification of (8), arithmetic of other fibers, complete global zero-column classification and any stronger rank/generator statements. Parent objective remains OPEN. No new Task is requested by this checkpoint.

No-repeat: do not re-prove the inherited two-triangle normal form; do not turn the old witness's common-root multiples into an infinite primitive family; do not replace (4) by an arbitrary point on E; do not promote six exact examples or the nontorsion lower bound to a global classification or exact rank.
