# Stage381-B — Exact double-r1 contact, cusp pinning, and uniqueness of the auxiliary global minimizer

Author-side theorem, Research2, 2026-11-02. Scientific source freeze is unchanged: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Parent Stage380-B is commit 2187681feaf8b93caeb05eff1ba97eab35a08a51 (PR #1736). Current behavior rules are read separately from canonical main. The theorem is for the original 16-label, four-independent-residual-channel Bernoulli/BRC *auxiliary* optimization. No native-X6 transfer or project admission is asserted.

## Original exact optimization and inherited premises

Let B_k(z)=z^k(1-z)^(3-k), k=0,1,2,3; w=(1,3,3,1), m=(61,21,9,9). Set

r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160;
D(a,z)=(1/2) sum_k w_k |B_k(a)-B_k(z)|;
b(x,y)=(5/32) sum_k w_k |r_k(x,y)|;
c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256.

The objective is T=33/1024+c(P)+c(Q), minimized over [0,1]^4 subject to b(P)+b(Q)<=B*=2 beta* + 11/5000. Here beta* is the inherited isolated r0=r1=0 simultaneous-root budget. Feasibility and global minimum attainment follow from the preceding rational feasible construction and compactness.

We use Stage379-B's proved localization and Stage380-B's proved Pareto wedge, unchanged in definition/scope. Every global minimizer can be swapped into:

P=(xP,yP) in (0.2308,0.2345) x (0.55,0.56);
Q=(xQ,yQ) in (0.2365,0.239] x (0.57566,0.57574);
r0(P)<=0<=r1(P), r0(Q)<0<=r1(Q), and b(P)+b(Q)=B*.

The original four-residual formula in this sign wedge simplifies EXACTLY (not by approximation) to

b(x,y)=(3/16)[4x(1-x)+y(1-y)]-45/256.      (1)

The original ALL-16-label cost in the boxes has exact form

c=C0(x,y)+(21/512)|delta(y)|,
C0=5157/32768-189x/256+93x^2/128-61x^3/256+33y^2/512-29y^3/512,
delta(y)=9/64-y^2(1-y).

There is one Q-box zero alpha=(1+sqrt(13))/8 of delta; 16alpha^2-4alpha-3=0.

## Stage381-B theorem

Under the exact inherited continuous-domain Stage379/Stage380 lemmas above, **the full original four-parameter auxiliary optimization has precisely one unordered global minimizer {P,Q}**.

After ordering xP<xQ, every minimizer satisfies the stronger and exact four equations:

r1(P)=r1(Q)=0, yQ=alpha=(1+sqrt(13))/8, b(P)+b(Q)=B*.  (2)

Equivalent algebraic system, with the root selected in the displayed strict parameter boxes:

16yQ^2-4yQ-3=0;
4xQ(1-xQ)^2+yQ(1-yQ)^2=21/32;
4xP(1-xP)^2+yP(1-yP)^2=21/32;
4[xP(1-xP)+xQ(1-xQ)]+yP(1-yP)+yQ(1-yQ)=15/8+(16/3)B*.

Exact rational isolation establishes:
0.23113 < xP < 0.23115;
0.55565 < yP < 0.55572;
0.237806902788 < xQ < 0.237806902794;
0.575693909432 < yQ < 0.575693909434.

Non-certifying decimal orientation: P about (0.231139116642445,0.555684475792775), Q about (0.237806902790747,0.575693909432999).

## Proof I: r1(P)=r1(Q)=0

From (1), bx=3(1-2x)/4>0 and by=3(1-2y)/16<0. Differentiating the original exact C0+absolute-value cost in its smooth branches gives

cx=-3(1-x)(63-61x)/256<0;
cy=(3y(1-y))/64 for y<alpha;
cy=(3y(18-25y))/256 for y>alpha.

Use the right derivative when perturbing upward through the Q cusp. Define lambdaX=-cx/bx, nuY=cy/(-by). For both complete boxes lambdaX>1: the rearranged numerator 61x^2+4x-1 is strictly positive already at the minimum x=0.2308 and increases. On the lower-y branch nuY<1 because y^2+7y-4>0 for y>=0.55. On Q upper-y branch nuY<1 because 25y^2+14y-16>0 for y>=0.57566. All comparisons are exact rationals at endpoints.

If r1(P)>0, increase yP, and uniquely increase xQ to preserve the EXACT active quadratic budget via the implicit function theorem (bx(Q)>0, dxQ/dyP=-by(P)/bx(Q)>0). The residual signs persist for a small displacement: r0(P) decreases when yP increases; r1(P) stays positive; increasing xQ keeps r0(Q)<0 and r1(Q)>=0. All fixed audit signs persist. The cost derivative is

d(cP+cQ)/dyP=(-by(P))[nuY(P)-lambdaX(Q)]<0,

contradiction. xQ=0.239 is merely an inherited localization boundary, not a physical feasible boundary; all formulas remain valid in a small open neighborhood while xQ<1/4.

If r1(Q)>0, increase yQ slightly and increase xP by the unique amount maintaining the exact active budget. This keeps r0(P)<=0 and r1(P)>=0 (increasing xP decreases r0(P), increases r1(P)); Q remains r1-positive by choosing the displacement sufficiently small. At the kink use the upward one-sided cy. The cost derivative is

(-by(Q))[nuY(Q)-lambdaX(P)]<0,

contradiction. Hence both r1 faces are required, stronger than the Stage380 union.

## Proof II: exact marginal slopes restricted to the two r1=0 faces

Write f(z)=z(1-z)^2=B1(z). Each face obeys 4f(x)+f(y)=21/32. Because g(x)=f'(x)=(1-x)(1-3x)>0 for these x and f'(y)=-(1-y)(3y-1)=-s(y)<0 for these y, this is a smooth increasing graph y(x), with y'=4g(x)/s(y)>0.

Its exact budget directional derivative factors:

Bdot=bx+y'by=[3/(4s(y))](y-x)(6xy-3x-3y+2)>0.   (3)

On each box x<y, s(y)>0; the final factor increases with x and decreases with y, and is strictly positive at (x_min,y_max) by rational arithmetic.

Let mu=-(cx+y'cy)/Bdot. For any rational lambda and one-sided branch define

H_lambda(x,y)=s(y)(cx+lambda bx)+4g(x)(cy+lambda by).  (4)

This is a bidegree-(2,2) polynomial with rational coefficients. By (3), H_lambda<0 iff mu>lambda; H_lambda>0 iff mu<lambda.

On the **entire closed P rectangle** and each version of the **entire closed Q rectangle** (even where the corresponding branch formula is used only on one side), exact tensor Bernstein degree-(2,2) coefficients give:

- P, lower-y cost branch, lambda=7/6: all 9 coefficients <0; min -643900929/128000000000, max -116807703/128000000000. Therefore muP>7/6.
- P, lower-y cost branch, lambda=5/4: all 9 coefficients >0; min 409208751/128000000000, max 953763561/128000000000. Therefore muP<5/4.
- Q, lower-y cost branch, lambda=5/4: all 9 coefficients <0; min -1532809843108119/512000000000000000, max -375303802826511/128000000000000000. Therefore muQ,low>5/4.
- Q, upper-y cost branch, lambda=7/6: all 9 coefficients >0; min 69710785232201/640000000000000000, max 1055742882942769/2560000000000000000. Therefore muQ,high<7/6.

The reproducible Python standard-library Fraction checker in REPRO_STAGE381B_MINI.py regenerates all 36 exact Bernstein controls and confirms the stated CSV SHA256. The expanded original author checker REPRO_STAGE381B.py additionally verifies algebraic identities and root enclosures. Each exact Bernstein control sign proves its full continuous rational rectangle.

## Proof III: the r0(P)=0 endpoint cannot block cusp approach from below

There is a unique simultaneous zero r0(P)=r1(P)=0 in the P rectangle: on the increasing r1-zero curve, r0 strictly decreases with x. Exact rational signs isolate its parameters as

0.231083 < x_beta < 0.231085 and 0.55550 < y_beta < 0.55552.

For example, r1(x_beta_low,y_beta_low)>0>r1(x_beta_low,y_beta_high), and similarly at x_beta_high; while r0(x_beta_low,y_beta_high)>0>r0(x_beta_high,y_beta_low). For r1=0, y grows as x, whereas r0 decreases in both coordinates, so this brackets the unique intersection. The inherited beta*=15r2(x_beta,y_beta)/16 and monotonicity of r2 on these coordinates give

15114451519803639/4000000000000000000 < beta*
< 120952336159413/32000000000000000.   (5)

The Q cusp alpha is in (0.575693909432,0.575693909434). Since r1 is increasing in x and decreasing in y, its unique zero at yQ=alpha occurs at

0.237806902788 < x_alpha < 0.237806902794.

Direct rational substitution in the quadratic budget and monotonicity in the Q box gives the strict bound

b(x_alpha,alpha)<b(0.237806902794,0.575693909432)<beta_lower+11/5000. (6)

If a minimizer had r0(P)=r1(P)=0, its P budget would be exactly beta*. The active joint budget would then require b(Q)=beta*+11/5000. Because BdotQ>0 on the r1Q face, (6) forces yQ>alpha. Thus for any minimizer with yQ<alpha we necessarily have r0(P)<0, so a small downward motion in xP along the P r1-zero face is allowed.

## Proof IV: cusp pinning and uniqueness

On the two r1-zero faces with exact active budget, a small change in xP determines a unique opposite change in xQ by (3); all original residuals stay in the inherited wedge. Differentiating objective along this feasible motion gives

d(cP+cQ)/dxP = BdotP [muQ - muP].  (7)

If yQ<alpha, Proof III gives r0(P)<0, so xP can be reduced. The exact Bernstein inequalities give muQ>5/4>muP, hence the derivative in (7) is positive, and decreasing xP strictly improves cost.

If yQ>alpha, increase xP instead. This preserves r0(P)<=0 and the two r1 equalities, while muQ<7/6<muP makes the derivative in (7) negative and again strictly improves cost.

At a double-r1 solution xQ=0.239 is impossible: r1(0.239,0.57574)>0 and r1_y<0; the Q face lies strictly inside the right boundary. All perturbations therefore remain feasible in the true original [0,1]^4 domain. Contradiction yields yQ=alpha.

Now alpha fixes xQ uniquely by strict increase of f(x) on x<1/3; P's exact r1-zero graph has BdotP>0, so its budget is strictly increasing and the exact joint budget chooses one xP; then r1(P)=0 chooses exactly one yP. Thus there is at most one ordered minimizer. Original compact attainment supplies at least one, so it is unique.

For existence and isolation, the independent exact Fraction checker brackets alpha, x_alpha and beta* as above; at xP=0.23113 the P r1=0 y-coordinate is between .55565 and .55566, while at xP=.23115 the face y-coordinate is between .55571 and .55572. The corresponding strict quadratic budget enclosures straddle target B*-b(Q). The resulting solution has r0(P)<0 because xP>0.23113>x_beta_high. This independently certifies feasibility of the isolated exact critical configuration.

## Evidence, scope, and next unit

Extended local exact program REPRO_STAGE381B.py was executed twice (emit and verify), with identical stdout and exact source checks. It emitted 36 controls in a 1802-byte certificate, SHA256 14e34213e9f9dad2b734c3ec8a8f93407d51e07d230f4fc01c9c74f4f7ed738c; marker STAGE381B_DOUBLE_R1_AND_Q_CUSP_EXACT_PASS. REPRO_STAGE381B_MINI.py independently regenerates the exact same CSV bytes/signs from the explicitly published coefficient matrices (marker STAGE381B_SIGN_CERTIFICATE_MINI_PASS). The method requires no third-party code or floating-point assumptions. The extended local proof, program, CSV and original standard output are separate runnable original materials, while this repository contains complete argument and a minimal exact checker.

This is PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / REPLAY_VERIFIED / UNREVIEWED / NOT_ADMITTED. Native research activity/CLAIM/Result and independent Driver mathematical review require separate valid authority. Original X6 P000 triadic slice, omitted third-coordinate semantics and preservation of future observers remain separate native-transfer obligations.

Next Stage382-B: independently audit inherited global localization and signed identities; derive an exact algebraic narrow interval for the optimum objective value; test an exact counterexample or identify the earliest assumption needing repair; investigate a typed observer-preserving bridge to P000 X6. Do not reinterpret this auxiliary continuous theorem as a native X6 theorem.