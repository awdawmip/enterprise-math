# R749SNF: exact diagonal Walsh minimax phases, 3/8 <= p <= 4/9

Date: 2026-11-13 Asia/Shanghai. Researcher EM-DIRECT-87D1FB. Predecessor R749SNE, PR #2304. Scientific inputs frozen at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Status: author-side proof plus exact exhaustive Fraction certificate, independent review pending. The finite Walsh observer is auxiliary, not a native X6/V29/V39 map.

## Theorem (all real p)
Let G=F_2^4, chi_m(x)=(-1)^{popcount(m AND x)}, and retain B={3,5,6,7,9,10,11,12,13,14} Walsh characters with m_3=m_12=p and other eight retained moments zero. Write A=chi_3, D=chi_12, P=chi_1, Q=chi_4. The complete compatible source fiber is
mu=[1+p(A+D)+h AD+u P+v AP+w Q+z DQ]/16 >= 0.
Let rho=min_{q in simplex} max_{mu in F_p} TV(q,mu), rho_cal=min_{q in F_p} max_{mu in F_p} TV(q,mu).

Then:
rho(p)=(7-3p)/15 on [3/8,23/57], and rho(p)=(5+p)/14 on [23/57,4/9].
rho_cal(p)=2(1-p)/3 on [3/8,2/5], and rho_cal(p)=2/5 on [2/5,4/9].

The optimal free centers q=[1+tau(A+D)+eta AD]/16 respectively use
(tau,eta)=((6-9p)/5,(6p+1)/15),
(tau,eta)=((3+9p)/14,(2-p)/7).
The optimal calibrated centers respectively use
(tau,eta)=(p,(4p-1)/3), (p,1/5).
All have nonnegative components and sum to one throughout their respective intervals. Free values at p=3/8,23/57,4/9 are 47/120,22/57,7/18. The first agrees with R749SNE; the calibrated value at p=2/5 is 2/5.

## Lower-bound proof
The fiber is invariant under flips P,Q and (A,P)<->(D,Q). Averaging minimizes worst-case convex TV, so an optimal free center has the displayed two-variable form; a calibrated center requires tau=p.

Use three explicit compatible source witnesses:
mu_AD=[1+p(A+D)+AD]/16;
mu_alpha=[1+p(A+D)+(2p-1)AD+(p-1)(P+AP)+(1-3p)(Q+DQ)]/16;
mu_beta=[1+p(A+D)+(p-1)P-p AP-p Q-p DQ]/16.
These are normalized and nonnegative at p=3/8,4/9, and hence throughout the interval by affine dependence.

The following fixed events use integer labels x=0..15, with chi_m(x)=(-1)^{popcount(m AND x)}:
T_AD={1,2,4,7,8,11,13,14};
T_alpha_I={0,4,5,6,8,9,10,12};
T_beta={0,1,2,3,4,6,8,10,12};
T_alpha_II={0,1,2,4,5,6,8,9,10,12}.

Using TV(q,mu)>=q(T)-mu(T), obtain for every tau,eta:
L_AD=(1-eta)/2;
L_alpha_I=(3-3p-tau+eta)/4;
L_beta=5/16+tau/8+eta/16;
L_alpha_II=(3+2p)/8-tau/4+eta/8.

The convex combinations (1/5)L_AD+(4/15)L_alpha_I+(8/15)L_beta=(7-3p)/15 and
(1/7)L_AD+(4/7)L_beta+(2/7)L_alpha_II=(5+p)/14 cancel both free decoder parameters. Their crossing is exactly p=23/57.

Under calibration tau=p, (1/3)L_AD+(2/3)L_alpha_I=2(1-p)/3 and
(1/5)L_AD+(4/5)L_alpha_II=2/5. Their crossing is p=2/5. These are global lower bounds for the exact optimization.

## Upper-bound proof: complete finite rational certificate
Split [3/8,4/9] at 2/5 and 23/57. On each closed subinterval the predictor coefficients and proposed radius are affine in p. Construct the bounded full-dimensional joint polytope in (p,h,u,v,w,z) with the sixteen source positivity inequalities and two endpoint inequalities. Every vertex is an intersection of six independent active facets among eighteen.

The reproducible Python standard-library verifier enumerates all binomial(18,6)=18564 bases using exact integer Bareiss elimination and rational back substitution; it checks all inequalities, source and decoder probability normalization, and the full sixteen-atom TV distance for each candidate vertex. Each subinterval has exactly 10848 nonsingular bases, 464 feasible bases, and 82 distinct vertices, 41 per endpoint. No vertex violates either claimed upper bound. The counts of tight vertices (free,calibrated) are (54,18), (50,18), (54,18) for [3/8,2/5], [2/5,23/57], [23/57,4/9], respectively.

Since TV(mu,q_p)-bound(p) is convex in the joint six-dimensional variable, its maximum on each bounded polytope occurs at one of these exhaustively tested vertices. The certificate proves the upper bounds for ALL REAL p and all compatible source laws. Combined with the explicit analytic lower bounds, the theorem follows.

## Remaining frontier
Determine the first free transition after p=4/9 and the exact endpoint of the calibrated 2/5 plateau. Test off-diagonal fibers and future-observer compositions separately. An actual licensed native Cell/Link/Port event correspondence, independent scientific review, and formal Source Result remain open. The existing PR #2304 has not been modified.
