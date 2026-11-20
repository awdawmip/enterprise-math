# Stage390-B — Exact quantitative cusp-slope separation and Stage381 uniqueness audit

2026-11-03; Research2 author-side independent implementation (Draft PR #1736). Parent Stage389-B at 97535ba3897f5ee67ba118884a974ffaab0b8b28, tested target Stage381-B at d4c0ce1f2ffd941a8f6556f87937cee5257b9953. Scientific pins unchanged: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.

## Original problem and inherited conditions

Keep all 16 distinct source-labelled Bernoulli comparisons per source and all four BRC residual channels. Let B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9),

r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160;
D(a,z)=(1/2)sum_k w_k |B_k(a)-B_k(z)|;
b(x,y)=(5/32)sum_k w_k |r_k(x,y)|;
c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256.

Minimize T=33/1024+c(P)+c(Q) subject to b(P)+b(Q)<=B*=2beta*+11/5000. beta* is the isolated budget where r0=r1=0 in the left box. Stage379-B and Stage380-B, on which this conditional theorem relies, place every global minimizer after source exchange in

P in (0.2308,0.2345)x(0.55,0.56); Q in (0.2365,0.239]x(0.57566,0.57574);
r0(P)<=0<=r1(P), r0(Q)<0<=r1(Q), joint budget active.

## New quantitative result

On each of the two r1=0 faces write y=y(x) and define Bdot=b_x+y'b_y>0 and mu=-(c_x+y'c_y)/Bdot, with the relevant one-sided derivative at the Q cusp alpha=(1+sqrt(13))/8. On the *entire closed P/Q rectangles*, with the original signed cost branches,

7/6+9/10000 < mu_P < 5/4-3/1000;
mu_Q,lower > 5/4+29/10000;
mu_Q,upper < 7/6-1/10000.

For a joint-budget-preserving motion on the double-r1 face,

d(c(P)+c(Q))/dxP = BdotP*(mu_Q-mu_P).

Thus when yQ<alpha this derivative is strictly greater than (59/10000)*BdotP>0, and when yQ>alpha it is strictly less than -(1/1000)*BdotP<0. These strict numerical ratios strengthen the qualitative sign comparisons in Stage381. With the inherited Stage379/380 lemmas, the original continuous four-parameter auxiliary problem has one unordered global minimizer satisfying r1(P)=r1(Q)=0, yQ=alpha and b(P)+b(Q)=B*.

## Proof and full-domain evidence

1. The original per-label Bernoulli differences have 31 fixed audit signs across the two boxes; retain Q's one variable k=2 comparison, delta(y)=9/64-y^2(1-y). Endpoint signs plus monotonicity of each B_k on the relevant intervals fix the signs. The exact signed expansion is
c=C0+(21/512)|delta(y)|,
C0=5157/32768-189x/256+93x^2/128-61x^3/256+33y^2/512-29y^3/512.
Using all four r_k, in the Stage380 nonnegative-r1/nonpositive-r0 wedge:
b=3[4x(1-x)+y(1-y)]/16-45/256.
Consequently bx=3(1-2x)/4>0; by=3(1-2y)/16<0;
cx=-3(1-x)(63-61x)/256<0;
cy,lower=3y(1-y)/64, cy,upper=3y(18-25y)/256.

2. The exact polynomial inequalities 61(0.2308)^2+4(0.2308)-1>0; (0.55)^2+7(0.55)-4>0; (0.57566)^2+7(0.57566)-4>0; and 25(0.57566)^2+14(0.57566)-16>0 give lambdaX=-cx/bx>1>nuY=cy/(-by), using the appropriate one-sided branch. If r1(P)>0, increase yP and compensate via increasing xQ at fixed exact budget: the cost derivative is (-byP)(nuY(P)-lambdaX(Q))<0. If r1(Q)>0, increase yQ and compensate via increasing xP: the same formula is negative, including the upward one-sided derivative at alpha. The signs of r0/r1 preserve the original feasible wedge. Derived localization boundaries are not boundaries of the original [0,1]^4. Both r1 faces are therefore necessary.

3. Put f(z)=z(1-z)^2, g(x)=(1-x)(1-3x)>0, s(y)=(1-y)(3y-1)>0. On r1=0, 4f(x)+f(y)=21/32 and y'=4g/s. Direct factoring yields
Bdot=3(y-x)(6xy-3x-3y+2)/(4s)>0.
The final factor increases with x and decreases with y in both rectangles; its minimum at (x_min,y_max) is positive by exact rational arithmetic. Moreover 0<s*Bdot=s*bx+4g*by<s*bx<1.

4. For a rational lambda, define the bidegree-(2,2) polynomial
H_lambda=s*(cx+lambda*bx)+4g*(cy+lambda*by)=s*Bdot*(lambda-mu).
The portable checker reconstructs H using rational sparse polynomial operations on the above derivatives, *not the coefficient matrices in the Stage381 code*. It converts all four cases to 9 tensor Bernstein coefficients each on the *whole closed P/Q boxes*. All 36 signs are strictly certified. Their signed minimum values, each greater than the stated additional margin, are:

P, -H_(7/6): 116807703/128000000000 > 9/10000;
P, +H_(5/4): 409208751/128000000000 > 3/1000;
Q lower, -H_(5/4): 375303802826511/128000000000000000 > 29/10000;
Q upper, +H_(7/6): 69710785232201/640000000000000000 > 1/10000.

The tensor Bernstein convex-hull property extends the four bounds to every real point of the boxes. Dividing by s*Bdot in (0,1) proves the new marginal ratio inequalities, then the cost-derivative inequalities.

5. Endpoint/cusp repair check (full from-source local checker, preserved as local attachment): exact r0/r1 monotonic comparisons bracket the unique simultaneous left root by 0.231083<xbeta<0.231085 and 0.55550<ybeta<0.55552. The budget beta* satisfies
15114451519803639/4000000000000000000 < beta* < 120952336159413/32000000000000000.
The cusp root alpha lies in (0.575693909432,0.575693909434), and its r1=0 Q root lies in (0.237806902788,0.237806902794). Exact rational budget substitution proves b(0.237806902794,0.575693909432)<beta_lower+11/5000. Hence if r0(P)=r1(P)=0 and budget active, the r1(Q) face has yQ>alpha. Therefore below alpha, any candidate has r0(P)<0 and can lower xP; above alpha it may increase xP. Both moves strictly improve cost by step 4. So yQ=alpha at a global minimizer. The alpha polynomial uniquely chooses yQ and f'(x)>0 uniquely chooses xQ. Since BdotP>0, the active budget uniquely chooses xP, followed by yP from r1(P)=0. Exact P budget inequalities at xP=0.23113 and 0.23115 straddle B* and place the solution at r0(P)<0. Nonempty compact feasible set supplies existence of a global minimizer.

## Actually executed evidence and scope

Portable Python Fraction reproducer output:
STAGE390B_EXACT_MARGINAL_CERTIFICATE_PASS 1802 14e34213e9f9dad2b734c3ec8a8f93407d51e07d230f4fc01c9c74f4f7ed738c
STRICT_MARGINS Q_LOW_MINUS_P > 59/10000; P_MINUS_Q_HIGH > 1/1000

The 1,802-byte 36-row CSV matches Stage381's original recorded digest, despite the independent reconstruction of polynomials. A more extensive executed local Fraction checker also reconstructs the full original labelled cost, tests exact endpoint/budget/root inequalities, runs twice with identical stdout, and is retained as a downloadable run artifact. GitHub stores this full mathematical argument, the complete 36-control CSV, portable exact checker, actual stdout and next unit. Publication is author-side evidence; formal native CLAIM/Result or independent Driver review require actual valid authority.

The statement is about this auxiliary continuous Bernoulli/BRC observer. P000 native X6, the third component of a three-dimensional slice, paths, timing and future-observer-preserving readout remain an independent typed transfer objective.

Next Stage391-B: inspect earliest upstream Stage366/367 or rational comparison obligation not already audited, while independently constructing an explicit candidate X6-to-three-component observer bridge or precise future-operation fiber counterexample.