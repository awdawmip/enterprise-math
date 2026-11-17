# R243 — Exact optimal uniform first horizons for the reversible seven-source scalar observer

2026-11-17, Asia/Shanghai. Evidence: AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE_EXECUTED / NOT_REVIEWED.

## Source, hypotheses and question

Independent portable continuation of R242 at commit 6427030e552a22824a5fc5a9608826890650039b and R241 at 727b4b58a6072167f0864112e361d1e5be8cf1c9. Frozen original science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. We reuse R236 for strict monotonicity of r(s), R237–R240 for the nonnegative spectral expansion and Kantorovich coefficient bound, R241 for beta/r, and R242 for exact boundary first crossings.

For 39/100 < s < 41/100 the stationary reversible sticky-reset chain has

$$
\alpha=(1/5,1/4,3/10,9/20,s,2/3,t(s)),\qquad
t(s)=(1691s-2615)/(2615s-3539),
$$
$$
b_0=13/60,\quad b_j=(5/18)|1/2-\alpha_j|\ (1\le j\le6),\quad
\pi_j=b_j/(1-\alpha_j),\quad Z=\sum_{j=0}^6 b_j/(1-\alpha_j)^2,
$$
$$
P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j,\quad
\rho_j=b_j/((1-\alpha_j)^2Z).
$$

For every proper subset U of the six nonneutral sources, put D_U={0} union U, with W=(144,576,1440,4320,17280,86400,518400). The scalar principal-ideal-cardinality observable is

$$
\Phi_n(s)=\sum_{U\subsetneq[6]}W_{|U|}\rho_{D_U}^{T}P_{D_U}^{n-1}{\bf1}
=A(s)r(s)^{n-1}+R_n(s),\quad
E_n(s)=R_n(s)/(A(s)r(s)^{n-1}).
$$

The dominant root r and its coefficient A>0 come from the block omitting source 3. R242 proves E_n>0 and E_{n+1}<E_n for n>=2.

## Theorem: both smallest uniform horizons are now exact

Define N_d^unif as the least integer n>=2 such that E_n(s)<1/d for every real s in (39/100,41/100). Then

$$
\boxed{N_{100}^{unif}=752,\qquad N_{1000}^{unif}=1128.}
$$

These improve the formerly sufficient uniform horizons 1073 and 1449 from R241 and close the uniform-horizon question, without requiring parameter-wise monotonicity of E_n(s).

## Proof, part I: three-tier spectrum

For each killed source set D, detailed balance symmetrizes its substochastic matrix to

$$K_D=\operatorname{diag}(\alpha_i)_{i\in D}
+(\sqrt{b_ib_j})_{i,j\in D}.$$

K_D is symmetric positive definite, and the scalar observable has nonnegative spectral coefficients summing to M_D=W_{|D|-1}\sum_{i\in D}\rho_i. By rank-one interlacing, every nonleading eigenvalue is <=max_{i\in D}\alpha_i<4/5.

The dominant mask is 59 (omit 3). Let B be mask 55 (omit 4), with Perron root beta(s), and G be mask 51 (omit 3 and 4). R241 provides beta/r < q=1641223/1651305.

We prove the following strict uniform root bounds:

$$
\lambda_{\max}(K_G)<\Gamma=977/1000,\qquad
\lambda_{\max}(K_D)<\Delta=973/1000
$$

for all proper D other than masks 59, 55 and 51. For x>max alpha_i the secular test is

$$
\lambda_{\max}(K_D)<x\iff f_D(s,x)=\sum_{i\in D}b_i(s)/(x-\alpha_i(s))-1<0.
$$

For x>1/2, the source-4 term (5/18)(1/2-s)/(x-s) strictly decreases in s, while the source-6 term (5/18)(t(s)-1/2)/(x-t(s)) strictly increases. On any [l,u] in the parameter interval an exact upper envelope replaces those terms by their respective values at l and u. The accompanying executable certificate checks f_G(s,Gamma)<0 with one full-interval envelope, and all 16 exact negative signs for the four equal subintervals and the four parent masks 62, 61, 47, 31 (omitting sources 1, 2, 5, 6 respectively) at x=Delta. Every other proper mask misses at least one of those four sources and is a principal submatrix of a checked parent. All nonleading eigenvalues of mask 59 are also <Delta. These finite rational checks establish the asserted bounds for every real s.

## Proof, part II: spectral coefficient bounds

Write z_i=b_i/(1-\alpha_i)^2. The dominant-block amplitude formula and R240's Kantorovich result give

$$
A=W_5 S(r)^2/(ZQ(r)),\qquad
S(r)^2/Q(r)\ge (1680/1681)(Z-z_3),\quad z_3=50/1089.
$$

Since M_B=W_5(Z-z_4)/Z and M_G=W_4(Z-z_3-z_4)/Z, we derive

$$
M_B/A\le (1681/1680)(Z-z_4)/(Z-z_3)
\le c_B=13381178569/13505199120<1,
$$
$$
M_G/A<c_G=1681/8400.
$$

Indeed Z(s)=5(4538s-7153)/(16632(s-1)) increases, z_4(s)=(5/18)(1/2-s)/(1-s)^2 decreases, and z_4>z_3 over the whole interval. Inserting Z(41/100) and z_4(41/100) yields the exact c_B fraction above. From R241, A/T>eta=1042768025600/8424836672439, so T/A<c_0=1/eta, where T is total nonconstant spectral mass. R236 and R242's 39/100 endpoint rational root certificate give r(s)>r_0=990628/1000000.

## Proof, part III: sharp uniform certificate and optimality

Separate the full B block, the full G block and all remaining subleading/other-block modes. Their spectral masses are bounded by M_B, M_G and T, respectively. Positivity and the above root bounds give, for all n>=2,

$$
\boxed{
E_n(s)<
c_Bq^{n-1}
+c_G(\Gamma/r_0)^{n-1}
+c_0(\Delta/r_0)^{n-1}.}
$$

All three bases are less than one. The exact standard-library Fraction checker verifies the final rational inequality at n=752 (bound approximately 0.0099841667847703 <1/100) and n=1128 (bound approximately 0.0009966211791189 <1/1000); the decimal displays are not used as evidence. Its JSON records the 16 secular signs, exact rational constants, and SHA-256 and bit sizes of the strictly positive final exact rational margins. Thus these horizons work across the full interval and for all later n.

R242 established exact strict failures E_751(41/100)>1/100 and E_1127(41/100)>1/1000 for the boundary extension. Since fixed-n E_n(s) is continuous in s (finite exact transition powers and a simple isolated Perron eigenpair), parameters strictly inside the open interval and arbitrarily near 41/100 retain these failures. Since E_n strictly decreases in event-time n, no smaller integer is uniformly sufficient. This completes the proof.

## Reproduction, scope, and next problems

Run Python 3 standard library: python3 R243_uniform_optimal_horizons_check.py > R243_verification.json. The program uses exact Fraction arithmetic and exact integer cross-products; its output is PASS. Analytic envelopes + preceding pinned exact theorems support the all-real conclusion; the 16 rational checks are the finite certificate for the inequalities reduced by those analytic arguments.

This result concerns the derived scalar source-support principal-ideal-cardinality observer. It does not quotient native P000 six signed spatial axes, independent time or BRC signed/port/source/branch/provenance/multiplicity/weight/cross-moment state. Native EffectHistogram integration NOT_EXECUTED. Independent review NOT_REVIEWED; formal Task CLAIM/Result/Review not asserted.

Next useful investigations: parameter derivative of E_n(s) and its sign (no longer a dependency for uniform horizons), exact second-mode approximation error, and full input/precision/bit-complexity comparisons of 230-order exact recurrence, 256-state propagation and spectral approximation.
