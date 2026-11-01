# D25/LIFT GH-90 — derived adjoint observer resolves the missing first jet on double-root fibers

2026-10-29 / hourly TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is a noncanonical research note, not a native Source checkpoint, proof of LIFT/JT2, independently reviewed theorem, or a current ownership assertion.

Frozen scientific source pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Original Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7. Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. This is an auxiliary finite-field GH-3 certificate within the portable D25 workstream; the original task's second-digit LIFT goal is not discharged.

## Typed original sources and the exact question

Let p=4d+3 >=7 be prime, k=F_p, theta=z d/dz. Distinguish original S=sum_(i=0)^d c_i z^i and reflected U=sum_(j=0)^d h_j z^j, with c_0=h_0=1 and

c_(i+1)/c_i=(4i+1)^3/((4i+2)(4i+3)(4i+4)),
h_(j+1)/h_j=(4j+3)^3/((4j+4)(4j+5)(4j+6)).

All displayed recurrence denominators are units in their indicated ranges. Let L_minus=theta(theta-1/2)(theta-1/4)-z(theta+1/4)^3 and L_plus=theta(theta+1/4)(theta+1/2)-z(theta+3/4)^3. Their source identities, previously shown in GH-84, are

L_minus S=(c_d/8) z^(d+1),  L_plus U=0.

Let B(X,Y) be the signed ordered GH-84 concomitant

B(X,Y)=(1-z)(Y theta^2 X-(theta Y)(theta X)+(theta^2 Y)X)
 +(z-3)Y theta X/4+(3-5z)(theta Y)X/4+(2-7z)XY/16,

so that theta B(X,Y)=Y L_minus X+X L_plus Y. GH-89 established that B(S,U), Q_S and their scalar companions do NOT recover theta S when U(9)=theta U(9)=0.

## GH-90A — a second, SOURCE-FAITHFUL finite adjoint observable

Use Y=theta U, but do NOT claim Y is a homogeneous adjoint solution. The exact commutator is

L_plus (theta U)=[L_plus,theta]U=z(theta+3/4)^3 U.

Define V(z):=B(S,theta U)(z). Then the *complete* polynomial identity is

theta V=(c_d/8) z^(d+1) theta U + z S (theta+3/4)^3 U.          (90.1)

V(0)=0 and deg(V)<=2d+1=(p-1)/2<p. Since every integer n=1,...,2d+1 is a unit of F_p, coefficientwise theta integration is exact and UNIQUE:

V(z)=sum_(i,j=0)^d [c_i h_j (j+3/4)^3/(i+j+1)] z^(i+j+1)
    +(c_d/8) sum_(j=1)^d [j h_j/(d+1+j)] z^(d+1+j).           (90.2)

This is an explicit, independently evaluable original/reflected *finite-source convolution*. Every denominator is a p-unit; its derivation never divides by U, theta U, S, or an unknown target value. The two sums have distinct original-source provenance and must not be silently merged into a generic scalar oracle.

Proof: [L_plus,theta]=z(theta+3/4)^3; apply the GH-84 Lagrange identity to X=S, Y=theta U. Both terms in the right side of (90.1) have no constant coefficient. Expand U and S, integrate each positive exponent n in the permitted range, and use V(0)=0. This proves (90.2) identically, rather than just at z=9.

## GH-90B — faithful first-jet reconstruction at every ordinary double-root fiber

Let a in F_p\{0,1} satisfy U(a)=theta U(a)=0. Set E=(theta^2 U)(a), D=(theta S)(a). Then E != 0. Indeed the leading theta^3 coefficient of L_plus is 1-z; at an ordinary a the equation recursively determines all Taylor coefficients up to degree d<p from the first three jets. Three zero initial jets would force U=0, contradict U(0)=1.

Writing F=(theta^3 U)(a), the ordinary-point L_plus equation gives

(1-a)F+(3-9a)E/4=0, hence F=(9a-3)E/[4(1-a)].

Insert Y=theta U and Y(a)=0, theta Y(a)=E, theta^2 Y(a)=F into the *ordered* B formula. All terms containing Y(a) vanish, leaving

V(a)=(1-a)(-E D+F S(a))+(3-5a)E S(a)/4
    =E[(a-1)theta S(a)+a S(a)].                              (90.3)

This identity is exact for *every ordinary double root*, and reconstructs the missing signed first jet: theta S(a)=[V(a)/E-aS(a)]/(a-1). At the target a=9, for T=(8theta+1)S, equation (90.3) becomes

E*T(9)=V(9)-8E*S(9).                                          (90.4)

Consequently T(9)=0 on such a fiber is **equivalent** to the explicit source-only convolution certificate

V(9)=8(theta^2 U)(9)S(9).                                     (90.5)

This repairs the *information-loss* obstruction of GH-89: the scalar package (S,U,H,J,B,Q) by itself is insufficient, but adding the independently computable V from (90.2) separates the lost first jet. It does NOT prove the remaining special-value equality (90.5) for all primes. To prove GH-3, an independent arithmetic evaluation of the two sides is still required; using (90.3) to repackage T(9)=0 would be circular.

At p=23,d=5,a=9 the exact original-source tuple is S=20, U=0, E=22, V=1, T=0. Equation (90.4) reads 22*0=1-8*22*20=0 mod23. For p=11,d=2,a=7 there is an ordinary U-double root with S=8, theta S=5, E=2, V=7 and (a-1)theta S+aS=9 !=0 mod11; thus the general observer relation is not a universal target vanishing theorem.

## Author verification and boundaries

A standalone standard-library integer-mod-p checker independently generated c_i/h_j, reconstructed the *entire* V via the signed B formula and via (90.2), separately checked the complete derivative identity (90.1), and checked (90.3) on *all* F_p ordinary double-root fibers for all 154 primes 7<=p<2000 with p=3 (mod4). Results: PASS_GH90_COMPLETE_SIGNED_CONCOMITANT_AND_FINITE_CONVOLUTION 154 primes; PASS_GH90_ALL_ORDINARY_DOUBLE_ROOT_FIBERS 3463 root fibers. It also verified (90.4) on target roots, including p=23,47,71,167. Exact finite-field verification, not independent review, Lean formalization or native p=373 experimentation.

BRC / enterprise-coordinate interpretation: the signed operation (theta), ordered sources (c_i vs h_j), prime/parameter, and observer V are retained; the previously lost first jet is recovered on the scoped ordinary U-double-root fiber. These are external algebraic F_p charts; no unproved transfer to native Heartbeat X6 or a three-dimensional research slice is asserted. P000 ACTIVE and source pins unchanged.

## Immutable frontier / next action

Completed author unit: construct and prove the exact second finite-source adjoint V and the ordinary double-root first-jet recovery formula. Do not redo GH-84/85, GH-86/87 or GH-88/89. Next: independently evaluate the single finite convolution (90.2) at a=9 in U-double-root CM branches and establish (or refute) (90.5) without assuming the target; keep the U(9)!=0 GH-88 squared-source route separate. Retain the GH-83 Laurent first-pole correction B_0L, GH-20/21, W/S, six Hasse ports, R23/R36 and native p=373 obligations. Preserve existing old session/claim/staging and pending requests for #1558 control owner; current gateway observed version 0.6.11 and research_authority_granted=false, executor_binding_configured=false, active control quota 5/5, no new native session/CLAIM/OPEN/Source checkpoint. Actual native recovery/continuation remains unverified for this turn. No final Task freeze or admission is claimed.
