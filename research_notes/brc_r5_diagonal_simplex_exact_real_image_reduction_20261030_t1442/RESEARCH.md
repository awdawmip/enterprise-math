# R5: Two-simplex diagonal reduction for actual real behavioral image membership

Date: 2026-10-30 Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Finite auxiliary two-measure stopping model; not native Heartbeat/X6 dynamics or a claim of external physics.

## Sources and provenance

Frozen GLOBAL_KNOWLEDGE_V1 main@f9f14fb361015e154dabef479961d7caadf25237 and Enterprise Math main@ea390dcadd5d3233200fad2aa0888d427f157db8, verified by GitHub connector in this run. Read global 00_BOOTSTRAP.md and OPERATING_MANUAL.md, math/code/EM rules, ACTIVE 我眼中的世界.md, project AGENTS.md, P000, joint observer preservation and Heartbeat X6 contracts, and portable research protocol. Predecessor: PR #1663 commit 30f58a195a07311dd7f3fe636b0fe487c916bd70, exact 647-row certificate of FULL/LR **four-dimensional convex-hull equality** for the A10/B10 equal nonzero P error shift. Existing certificate is reused, not duplicated.

GitHub transport login awdawmip identifies the account, not an execution Researcher. Native directed context: authority_granted=false; owner-control query returned CONTROL_QUOTA. This is a portable author proof, not a formal Source CLAIM, Result, review or admission.

## Exact model

Each row is (time,Pmass,Qmass,parent-index), with both measures normalized by 360:

~~~text
0 A (1,120,240,-1)     1 B (1,240,120,-1)
2 A0 (2,60,180,0)      3 A1 (2,60,60,0)
4 B0 (2,180,60,1)      5 B1 (2,60,60,1)
6 A00 (3,30,108,2)     7 A01 (3,30,72,2)
8 A10 (3,30,45,3)      9 A11 (3,30,15,3)
10 B00 (3,90,36,4)     11 B01 (3,90,24,4)
12 B10 (3,20,40,5)     13 B11 (3,40,20,5)
~~~

FULL has one stop probability for each of 14 histories; seedless LR has 12 keys (time,Pmass/Qmass) because A1/B1 and A11/B11 collide exactly. At time 4 all survivors stop. Each stop-path probability is its history's conditional survival times its local stop probability. Define (r,x,y,s) as sums over actual stopping histories: r = Qmass at A11/B11 only; x = (4-time)*Pmass for every time<=3 stop; y = (4-time)*Qmass similarly; s = Pmass at A10/B10 only. The source-labelled P and Q masses and time remain separate up to the observer.

For the original eta=delta=1/1000 terminal model, the observer map is exactly

~~~text
TP=4-x/360; TQ=4-y/360;
eP=21/100+TP/20+TQ/100+delta*s/360;
eQ=41/100+TP/200-TQ/30+eta*r/360.
~~~

This is invertible affine for nonzero eta,delta. Hence actual-image equality/membership in (r,x,y,s) is equivalent to that in the original (eP,eQ,TP,TQ). Positive terminal kernels and both collisions were established and checked by predecessor.

## Theorem 1: Exact FULL two-triangle and LR diagonal-fiber formulas

Let D = { (c,t) in R^2 : c>=0, t>=0, c+t<=1 }. For each (cA,tA),(cB,tB) in D, define ten real flow variables alpha,beta,U,V,W,Z,WB,ZB,C,Dv with constraints

~~~text
0<=alpha,beta<=1
0<=U<=alpha; 0<=V<=beta
0<=W,Z<=alpha-U; 0<=WB,ZB<=beta-V
0<=C<=(1-cA)*alpha; 0<=Dv<=(1-cB)*beta.
~~~

For fixed triangle parameters these are linear constraints. Define the affine map in flow variables

~~~text
r = 15*tA*alpha + 20*tB*beta
s = 30*C + 20*Dv
x = 360*(1-alpha)+720*(1-beta)+120*U+360*V
    +120*cA*alpha+120*cB*beta+30*W+30*Z+90*WB+90*ZB
    +30*C+20*Dv+30*tA*alpha+40*tB*beta
y = 720*(1-alpha)+360*(1-beta)+360*U+120*V
    +120*cA*alpha+120*cB*beta+108*W+72*Z+36*WB+24*ZB
    +45*C+40*Dv+15*tA*alpha+20*tB*beta.
~~~

Write P(cA,tA;cB,tB) for this compact convex four-coordinate polytope. Then the exact **actual, unconvexified real behavioral** observation sets satisfy

~~~text
O_FULL = union_{(cA,tA),(cB,tB) in D} P(cA,tA;cB,tB)
O_LR   = union_{(c,t) in D}              P(c,t;c,t).
~~~

Proof (forward): Denote the FULL conditional stop probabilities at a history h by a_h. Set alpha=1-a_A, beta=1-a_B; cA=a_A1, cB=a_B1; tA=(1-cA)*a_A11, tB=(1-cB)*a_B11. Put U=alpha*a_A0, V=beta*a_B0, W=(alpha-U)*a_A00, Z=(alpha-U)*a_A01, WB=(beta-V)*a_B00, ZB=(beta-V)*a_B01, C=alpha*(1-cA)*a_A10, Dv=beta*(1-cB)*a_B10. These obey precisely the displayed bounds. Expansion of the fourteen source-labelled stopping contributions gives the four formulas. Under LR, a_A1=a_B1 and a_A11=a_B11, so cA=cB and tA=tB.

Proof (converse): Given any feasible flows, choose root stops 1-alpha,1-beta. The remaining actions are a_A0=U/alpha, a_B0=V/beta, a_A1=cA, a_B1=cB, a_A00=W/(alpha-U), a_A01=Z/(alpha-U), a_B00=WB/(beta-V), a_B01=ZB/(beta-V), a_A10=C/[alpha*(1-cA)], a_B10=Dv/[beta*(1-cB)], a_A11=tA/(1-cA), a_B11=tB/(1-cB). Assign the value 0 to any 0/0; the corresponding numerator must then be zero by the constraints. Thus all actions are in [0,1] and exactly reproduce all flows. On the diagonal the A1/B1 and A11/B11 actions coincide, so this is **one seedless LR policy**, not a mixture over whole policies. QED.

Consequently, LR membership for a given rational FULL observation is reduced to an existence question over just **two nonlinear real parameters (c,t)**, with a finite rational linear feasibility problem in the remaining ten flows for any fixed rational (c,t). Fixed-slice infeasibility from a rational Farkas certificate is not the same as uniform infeasibility over the entire continuum of D.

## Theorem 2: Exact affine-rank phase diagram for every fixed LR fiber

The fiber P(c,t;c,t) has affine dimension 4 if t>0, dimension 3 if t=0 and c<1, and dimension 2 at (c,t)=(1,0). Every t>0 fiber already contains four-dimensional interior.

Proof: Set alpha=beta=1/2 and all eight non-root flows U,V,W,Z,WB,ZB,C,Dv to zero. Four separate feasible perturbations increase alpha by 1/4, W by 1/4, Z by 1/4, or C by (1-c)/4. In the (r,x,y,s) order, the four-by-four determinant of their observation differences is exactly

~~~text
det4(c,t)=-30375*t*(1-c)/16.
~~~

For t>0 the triangle constraint entails c<1, and this determinant is nonzero. If t=0 all points have r=0, while the W,Z,C variations give the three-dimensional (x,y,s) determinant -2025*(1-c)/4, nonzero when c<1. At c=1,t=0 both r and s vanish and the W,Z variations give the (x,y) determinant -135/2, nonzero. Therefore the three exact rank assertions follow. The anchor c=0,t=1/2 gives determinant -30375/32. QED.

## Validation and boundaries

The companion exact Python Fraction checker evaluates every one of 16,384 FULL and 4,096 LR deterministic policies, including zero-survival histories; checks 256 rational behavioral and 300 rational flow cases in both directions; confirms exactly two likelihood-ratio collisions; and independently computes the stated anchor determinant. Actual stdout is in EXACT_OUTPUT.txt. Finite checks corroborate the identities; the theorems for **all real** policies are established by the symbolic forward/converse construction and explicit determinant, not by sampling.

The four-dimensional FULL/LR convex-hull equality remains certified by the preceding 647-row exact certificate. This run neither proves nor disproves equality of the **actual** real behavioral images. P000 and native X6 semantics remain unchanged. No independent Driver mathematical admission is asserted.

## Next precise unit

Select a rational FULL vector v=(r,x,y,s) in the hull. Decide the exact sentence: exists c,t in R with c>=0,t>=0,c+t<=1 and the ten flow inequalities/equalities above at v? For candidate nonmembers, prove infeasibility **uniformly over the entire triangle** (for example symbolic two-parameter Farkas elimination or exact CAD, with rational proof records). Alternatively construct flows continuously for every FULL v to prove actual-image equality. The full source-labelled tree and rank4 hull certificate stay fixed; a failed numerical optimizer or finitely many LP slices is not a real nonmembership certificate.
