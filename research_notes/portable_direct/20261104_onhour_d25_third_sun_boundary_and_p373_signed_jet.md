# D25: third Sun defect coefficient and original p=373 four-source signed jet

Date: 2026-11-04. TASK_RESEARCH author-side portable science; UNREVIEWED / NOT_ADMITTED. Logical lane: chatgpt-research-onhour-enterprise-math-20260923 (distinct from maintenance). Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Mother objective: Delta_p-R_p = 0 mod p for p = 13,19 mod24, including original signed third-digit transport. Independent native p373 H0/B0 experiment remains outstanding (#1559).

## New all-prime theorem

Let p>=5 prime, alpha in Z_p, C=-alpha(alpha+1), c_k=binom(alpha,k)binom(-1-alpha,k), B_k=binom(2k,k), F(X)=sum_{k=0}^{p-1} c_k X^k, H(t)=sum_{k=0}^{p-1}B_k c_k t^k, and t=X(1-X). From the existing Sun congruence, E_alpha(X)=(F(X)^2-H(X(1-X)))/p^2 mod p is coefficientwise well-defined.

THEOREM: [X^(p+3)]E_alpha(X) = c_p (132-186C-505C^2-197C^3)/108 (mod p). This holds whether or not c_p is a unit.

PROOF: By the exact infinite Clausen identity, and because the omitted F-tail square begins at degree 2p>p+3, the coefficient of the original truncated difference at p+3 is

D_(p+3) = sum_{j=0}^3 (-1)^(3-j) binom(p+j,3-j) B_(p+j)c_(p+j) - 2 sum_{j=0}^3 c_(p+j)c_(3-j).

Put z as a formal variable, R_0=S_0=1, R_(j+1)=R_j ((z+j)(z+j+1)+C)/(z+j+1)^2, S_(j+1)=S_j (2z+2j+1)(2z+2j+2)/(z+j+1)^2; and c_0=1,c_(j+1)=c_j (j(j+1)+C)/(j+1)^2. Define Phi_3(z,C)=2 sum_{j=0}^3 (-1)^(3-j)binom(z+j,3-j) S_j R_j -2sum_{j=0}^3 R_j c_(3-j). These finite rational formulas are identities after clearing denominators, including if c_p is nonunit. Wolstenholme gives B_p=2 (mod p^3), hence D_(p+3)=c_p Phi_3(p,C) (mod p^3). Direct rational expansion at z=0 yields Phi_3(0,C)=Phi'_3(0,C)=0 and Phi''_3(0,C)/2=(132-186C-505C^2-197C^3)/108. All denominators 2,3 and z+j (j<=3) are p-units for p>=5, so the p^2 coefficient proves the result. QED.

For alpha=-1/3 and -1/4, p-adic binomial digits give c_p=C mod p (C=2/9,3/16 respectively), yielding the two exact rational constants [X^(p+3)]E_216 = 23170/177147 and [X^(p+3)]E_2304 = 106595/786432 mod p. These extend prior coefficients 4/27,35/243 and 21/128,4995/32768; do not assert scalar polynomial transport (already obstructed for p!=5).

## New original p=373 signed jet, preserving sources and observer order

Let a_k=(2k)!(3k)!/((k!)^5 216^k), b_k=(4k)!/((k!)^4 2304^k), A=sum a_k, B=sum b_k, M_A=sum k a_k, M_B=sum k b_k, W=A+6M_A,V=B+8M_B for k=0..p-1. Work mod p^3 in the quadratic ring s^2=2; x_a=(2+s)/4, x_b=(3+2s)/6, F_a=F_(-1/3)(x_a), F_b=F_(-1/4)(x_b), E_a=E_(-1/3)(x_a), E_b=E_(-1/4)(x_b). Derivatives are taken on original polynomials BEFORE Frobenius evaluation.

For target primes whose periods F_a,F_b vanish mod p, Sun's square plus its differentiated identity give the exact source-retaining relation

(W-V)/p^2 = P_square+P_derivative+Q_evaluation+Q_derivative mod p,

P_square=(F_a^2-F_b^2)/p^2,
P_derivative=[-(3s/2)F_a F'_a+(s/3)F_b F'_b]/p^2,
Q_evaluation=-E_a+E_b,
Q_derivative=(3s/4)E'_a-(s/6)E'_b.

The signed period numerator is combined and verified divisible by p^2 before division; no individual derivative term is assumed divisible. E and E' are reconstructed from the EXACT original finite truncations mod p^3 and then reduced modulo p. This map retains the separate (source, exponent, valuation, operation) observer tags.

For p=373, original binomial sums mod 373^3=51895117 are:
A=9878159; B=28243187; M_A=32950447; M_B=35390986; W=V=373.
The four contributions in F_373[s]/(s^2-2) are:
P_square=236, P_derivative=283+2s, Q_evaluation=5, Q_derivative=222+371s.
Constant part 236+283+5+222=746=2*373; s part 2+371=373. The two nonzero original unsigned-versus-moment digits are (A-B)/p^2=241 and (6M_A-8M_B)/p^2=132 mod p. Third defect coefficients are 105 and 7 mod 373. This is a finite exact signed source certificate, not a universal proof.

At p=139 this method reproduces the prior independent witness (17,106+64s,123,32+75s). p=13,19 also pass. The full standard-library exact checker covers 332 coefficients (both models, every 166 primes 5<=p<=1000) and all four original signed sources at 23 target-class primes p<=500; zero failures. It uses original factorial/binomial weighted sums, integer mod p^3, coefficientwise p^2 division and quadratic-extension evaluation, without floating point.

## Remaining scientific and control frontier

The next scientific step is a uniform signed Green/WZ or differential transfer relation for *all* defect coefficients and their derivatives, reproducing 13,19,139,373 and preserving differentiation-before-Frobenius, sign and original valuation. Existing first/second defect coefficients, scalar obstruction, p139 jet and two-seam Green results are consumed, not reset. The separate original p373 native H0/B0 [X]U mod139129, module rank, semilinear Frobenius and independent replication (#1559) are NOT_EXECUTED and are not replaced by the above finite hypergeometric calculation.

Current native service 0.6.11 reports research_authority_granted=false, CODE_UPGRADE_AVAILABLE, full_snapshot_verified=false; original continuation request onhour-d25-20261104-1702-continuation-read remains FAILED / SOURCE_TREE_SIZE_LIMIT, no reissue. No own current native CLAIM, run, checkpoint or Result is asserted, and no maintenance-lane identity was used.

Mathematical inputs: Z.-H. Sun, Note on super congruences modulo p^2 (2015); classical Clausen identity, Wolstenholme congruence, p-adic binomial digit lemma. Prior author notes: 20261104_onhour_d25_sun_defect_second_coefficient_scalar_obstruction.md and 20261104_onhour_d25_p139_signed_sun_observer_certificate.md.