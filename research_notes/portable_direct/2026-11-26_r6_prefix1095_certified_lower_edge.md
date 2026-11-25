# PREFIX-1095 -- Certified first lower-band zero and finite closure of the negative tail

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_SYMBOLIC_AND_RATIONAL_CERTIFICATE / NOT_REVIEWED. R6 independent continuation of the same frozen Stage46 BRC observer. Researcher metadata EM-DIRECT-780BBE / TASK_RESEARCH, own RA-0ABD84561C86E53067DB0322, own recovery receipt r6-20261126-0554-own-recovery confirms original registration and no run. Current owner read r6-20261126-0554-owner-read SUCCEEDED / error=null, Source 8964bcbc828a59c9413e0745c1a5303aa4c32a58, as_of 2026-11-25T21:55:05.110345Z, LEASED filter empty; no execution/CLAIM authority asserted or shared Task mutated.

Frozen input P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), all other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. All paired six-axis Cell equality, port, phase, sign and ordered multiplicities remain in the original BRC CT observer. The following is an exact auxiliary radial observer realization, not native spatial collapse, new propagation, classical trigonometry/pi comparison or physical residual attribution.

Parents (immutable refs):
- 1264a0c983aa2784ce230a768cc85aeef09553c9:research_notes/portable_direct/2026-11-26_r6_prefix1094b_nine_state_density_anchor.md
- 73e04d060c31c64a3c9fcd3986ce03617a74f0b1:research_notes/portable_direct/2026-11-26_r6_prefix1094_radial_density_pencil.md
- f8e95de9568ac9e174179902e12d90f5d6e608a6:research_notes/portable_direct/2026-11-26_r6_prefix1093_grouped_euler_occupancy.md
- 8d25f98107e9602c08ad92e01254d808955431f4:research_notes/portable_direct/2026-11-26_r6_prefix1092_two_anchor_effective_positive_tail.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md

## 1. The new result

With R=36x=SB, t=sqrt(R), the actual effective signed density g of the frozen observer is strictly positive on 0<R<=25/16 (hence 0<x<=25/576 >1/24). Its first zero in the lower regular band is unique in 5/4<t<13/10, simple, and is enclosed by the EXACT rational interval

  6800006737/5368709120 < t_* < 3400003369/2684354560.

In x this gives approximately (0.04456320692786793, 0.044563206940974744), and for rho_last=1/x_*-1 the corresponding interval is approximately (21.440036717387258,21.440036723987262). Exact endpoints are t_lo^2/36,t_hi^2/36 and 36/t_hi^2-1,36/t_lo^2-1, not the rounded decimals. No zeros below t_*, and sign strictly negative immediately above it. This certifies the first negative spectral edge b_last of PREFIX-1075 and its local crossing order r=1, not automatically the still-open mother parameters p,d or B_fix,odd(32).

The proof uses the exact inherited CT density and analytic identities, unbounded integer/rational computation and explicit remainder bounds. No unverified point density, classical function approximation, float sign or finite grid extrapolation is used. All scientific conclusions retain the inherited conditional observer correspondence and unreviewed status.

## 2. Regular-singular gauge and the actual local solution space

Use the seven base density components y_h=mu_(0^(6-h),1^h), h=0,...,6, of PREFIX-1094b. Let H=diag(h), U_(h,h+1)=6-h, D_(h,h-1)=h. Their ODE is

  y'=L(R)y, L=[R(I-D)-U]^-1[H-I+(I-H)D].

Set e_h=ceil(h/2)=(0,1,1,2,2,3,3), G=diag(R^e_h), y=G Z. Exact symbolic cancellation gives

  R Z'=A(R)Z, A=R G^-1 L G-diag(e).

A has denominator LCM (R-36)(R-16)(R-4); there is no pole at R=0 in A. The indicial matrix A(0) has seven distinct eigenvalues -3,-2,-1,0,1/2,1,2. Its eigenvectors are chosen by SymPy rational nullspace (last free coordinate 1), then divided by max absolute entry. Denote their ordered column matrix V; ||V||_infty=4. The eigenvectors before max normalization are, respectively:
  (0,0,0,0,0,1/6,1)
  (0,0,0,29/720,1/20,1/6,1)
  (0,4/15,1/15,7/60,2/15,1/6,1)
  (6,1,0,0,0,0,0)
  (-35,-35/6,7/3,7/10,7/15,1/6,1)
  (-360/13,-60/13,36/13,1,0,0,0)
  (75/2,25/4,-5,-35/16,5/4,1,0).

The physical weighted measure inequality |y_h(R)|<=R^(h/2)y_0(R) holds first a.e. by the unit-character weight of the exact pushforward and then throughout the regular band by analyticity. PREFIX-1075's continuous character-sum density implies y_0=O(1) at the origin. Consequently Z=O(R^(-1/2)). By the regular-singular Frobenius theorem, the independent modes with leading exponents -3,-2,-1 cannot occur in such a solution: possible resonant higher-order logarithms do not remove the distinct most-negative leading powers. Equivalently, the dimension of the subspace with this growth bound is at most four. We construct four independent log-free solutions below; their distinct leading exponents make them independent. Thus they span the actual Z on the lower band. This is a statement about the scoped radial densities; all native path information remains upstream.

Let q(R)=(1-R/4)(1-R/16)(1-R/36)=1-49R/144+7R^2/288-R^3/2304. Exact calculation gives P(R)=q V^-1 A V polynomial of degree at most 3. P_0=diag(eigenvalues). Its coefficient infinity norms are exactly
  3, 22247/2520, 66313/26880, 13409/129024.

For lambda=0,1/2,1,2 write Z_lambda=R^lambda V sum_(n>=0) v_n R^n, with v_0 the corresponding coordinate vector. Coefficients satisfy

  ((lambda+n)I-P_0) v_n
    = sum_(k=1..min(3,n)) [P_k-q_k(lambda+n-k)I] v_(n-k).

The only resonance entries among these four series are (lambda,n,target exponent)=(0,1,1),(0,2,2),(1,1,2). Exact RHS at each is zero, and the free resonant coefficient is chosen zero. Therefore the four physical-basis series are log-free, with rational coefficients. Their convergence with rigorous remainder follows from the next bound.

## 3. Explicit convergence and residual payment

Use w_n=2^n v_n, N=200 and T_lambda=max(||w_198||_infty,||w_199||_infty,||w_200||_infty). For n>=201 and 0<=lambda<=2, each inverse diagonal is at most 1/(n-2) and |n+lambda-k|<=n+2. Hence

  ||w_n|| <= [sum_(k=1..3) 2^k ||P_k|| + (n+2)sum_(k=1..3)2^k|q_k|]/(n-2)
                * max_(k=1..3)||w_(n-k)||.

At n=201 the rational prefactor is 5025203/5349120<1, and it decreases for larger n (limit sum 2^k |q_k|<1). Induction gives ||w_n||<=T_lambda for every n>200. This proves convergence on |R|<2 with the explicit remainder
  ||sum_(n>200) V v_n R^n||_infty <= 4 T_lambda (|R|/2)^201/(1-|R|/2).

Actual rational calculations give T_lambda approximately 3.8923e-66,5.0186e-66,1.9420e-65,9.8264e-65. The respective analytic-factor tail bounds on 0<=R<=3/2 are about 4.805e-90,6.195e-90,2.398e-89,1.213e-88. These are basis truncation errors, not errors of the original physical state before coefficient identification.

For the two dilation states, exact reconstruction from the 35-to-7 relation of PREFIX-1094b gives mu_(0,0,0,0,1,2)=-R y_0+6y_1+(R/2)y_2-2y_3 and mu_(0,0,0,0,1,1)=y_2. Put h_Q=nu_Q/R. Their exact equations are
  R h_1'=-Z_2,
  R h_2'=h_2-[-Z_0+6Z_1+(R/2)Z_2-2RZ_3].
For each of the four series, solve coefficients by division by lambda+n-(Q-1), with a zero at resonance. All resonant forcing entries are exactly zero, including (lambda,n,Q)=(0,0,1),(0,1,2),(1,0,2). Thus the full physical nine-component vector (Z,h_1,h_2) is a linear combination of SIX log-free series: the four extended base modes and the two homogeneous additions h_1=1 and h_2=R. These include the global mixed integration constants; they are not omitted or inferred from a local ODE initial value.

For n>200 the extended analytic-factor coefficients (before R^lambda) have infinity norm <=64 T_lambda 2^(-n). Indeed Z coefficients <=4T 2^(-n); the h_1 RHS costs no more, and the h_2 RHS costs <=[7*4+2*(1/2+2)*4]T 2^(-n)=48T 2^(-n), followed by division by magnitude >=1. Thus all extended basis tails on [0,1] are bounded by 100 T_lambda 2^(-200), used below. The recurrence also provides derivative bounds on any t in [0,T0] with T0^2<2 by termwise differentiated geometric sums.

## 4. Exact moment anchors identify the six coefficients

Let C=(c_0,c_1/2,c_1,c_2) denote the coefficients in the normalized four modes; C_h1,C_h2 the homogeneous dilation constants. We do not rely on slow pointwise beta-kernel convergence. Instead use four global moments of y_0, with polynomial test (1-R/36)^k, k=2000,2400,2800,3200. Their values are computed exactly using the grouped integer CT recurrence of PREFIX-1093. Truncated basis functions are integrated on [0,1]. The omitted global contribution from [1,36] is bounded by (35/36)^k because y_0 is a positive probability measure of mass 1. Any mass at endpoints is included in the global integral and the same bound; y_0 has no atom at R=0 (inherited continuous density). The computed matrix M of truncated local integrals is rational because every power is integer or half-integer and the upper integration limit is 1.

Explicit rational incomplete beta recursion: J_a(k)=int_0^1 R^a(1-R/36)^k dR, a=0 or 1/2. J_a(0)=1/(a+1); then
  J_a(k)=[k J_a(k-1)+(35/36)^k]/(a+k+1),
  J_(a+1)(k)=36[(a+1)J_a(k)-(35/36)^(k+1)]/(a+k+2).
These follow by integration by parts (or differentiation of R^(a+1)(1-R/36)^(k+1)). This directly computes every basis integral without subtracting uncontrolled floating quantities.

Write actual equations (M+E) C=obs+eta, with |eta_i|<=(35/36)^k_i and ||E||_infty<=eb=sum of four certified basis tail bounds. Let c_hat=M^-1 obs, K=||M^-1||_infty eb, eta'=max_i sum_j |(M^-1)ij| (35/36)^k_j. If K<1 then

  ||C-c_hat||_infty <= (eta'+K||c_hat||_infty)/(1-K).

The exact inversion gave ||M^-1|| about 1.34019958e8, K about 1.056e-114, and uniform error <3e-18 (computed value about 2.87208123e-18). For nu_Q at k=2000 use the exact mixed dilation moments mu_abs(R^l)/(l+Q+1) and TV<=6^(Q+1)/(Q+1). Subtract the local four basis contributions and divide by J_Q(2000)>0 (homogeneous nu_Q=R^Q). Pay the tail of the four basis series, their coefficient errors, and the omitted global weighted variation. This gives error about 9.9731e-20 for C_h1 and 2.1164e-18 for C_h2.

The following enclosing intervals are exactly the indicated integers divided by 10^15 (not heuristic fitted point values):
  c_0:     [168413980883224,168413980883225]
  c_1/2:   [40314418041499,40314418041500]
  c_1:     [-10922003425169,-10922003425168]
  c_2:     [-1,1]
  C_h1:    [33682796176644,33682796176645]
  C_h2:    [2806899681387,2806899681388].

For c_2 the interval contains zero; no exact vanishing claim. All 6 constants are now rigorously identified to finite precision from original exact joint BRC moments. The existence of the local observer expansion is inherited/proved above; no free least-squares fit or numerical ODE integration.

## 5. Exact signed readout, Bernstein sign and first-root isolation

Start with the actual 66 Laurent terms of PREFIX-1082 and the exact 28x7 polynomial reconstruction of PREFIX-1094b. For each term with coefficient p(n), shift d=(-a,b,0,0,0,0), offset j=u-P=v-Q, apply the exact density operator p(7-R d/dR) to R^j mu_d, with mixed mu_d=mu_abs-Q nu_Q. Sum all terms before taking any bounds. Use the ODE for derivative elimination and replace nu_Q=R h_Q. Symbolic computation gives a polynomial row N(R) with nine integer-polynomial entries of degrees 9,10,9,9,8,8,7,9,8, such that

  g(R/36) = 36/(4*36^8) * R^3 / [(R-16)^3(R-4)^3] * N(R) dot (Z,h_1,h_2).

The prefactor is strictly positive in 0<R<4. The factor R^3 is extracted EXACTLY, rather than dividing a numerical error by a vanishing quantity at zero. The polynomial N is constructed in the companion code from the frozen source expressions, not fitted. Let F(t)=N(t^2) dot (Z(t^2),h_1(t^2),h_2(t^2)). Use series n<=40 and the midpoints of the six exact parameter intervals to define a rational polynomial F_40(t) of degree <=104. All omitted n=41..200 terms are bounded by their exact coefficient magnitudes, and n>=201 by the geometric majorant of section 3. Parameter uncertainty is paid by the half-width of each interval times the sum of absolute power coefficients evaluated at the interval's maximum t. Multiply vector tail bounds by the polynomial row norm; for derivative use the product rule plus differentiated geometric bound. These are conservative bounds on the ENTIRE interval, not point sampling.

On [0,5/4] the actual degree-104 Bernstein coefficients of F_40 have minimum about 164778368.3115592; parameter error <=0.068986574 and series error <0.000000492 (displayed conservative rounding). The exact rational comparison gives min Bernstein - full error > 10^8. A single Bernstein interval suffices, no subdivision. Since all Bernstein basis functions are nonnegative and sum to one, F(t)>10^8 throughout [0,5/4]. Consequently g(x)>0 for 0<x<=25/576, including the previous hypothesis x<1/24. This resolves the singular endpoint as well as the interior.

On [5/4,13/10] the exact derivative Bernstein maximum plus derivative error is less than -8*10^9 (display approx -8.14106623e9). Uniform function error on [0,13/10] is below 0.085; derivative error below 0.343. The two endpoint signs are strict (centers about +164778368.31 and -295714094.54). Hence F has exactly one zero there, simple, and no zero before it. Thirty exact bisection steps using the same uniform error bound yield the rational endpoints in section 1, with strict opposite signs. The derivative bound implies simplicity of g at the same positive t. No inference is made beyond the covered range about additional zeros or upper-band sign.

For clarity, the derivative tail computation uses q0=T0^2/2<1, J=201 and exponent offset a=2lambda: the contribution of n>=J is bounded by
  64 T_lambda T0^a q0^J/(1-q0)
and its t derivative by
  64 T_lambda T0^(a-1) q0^J[(a+2J)/(1-q0)+2q0/(1-q0)^2].
Every bound used in sign/derivative decisions is rational. All decimal approximations above are for display only.

## 6. Consequence for the previous infinite tail and finite negative mass

The specific hypothesis g>=0 on (0,1/24) of PREFIX-1092 and 1093 is now discharged at the author-proof level. Their already-saved exact anchor inequalities therefore give the stated 19 fixed-row infinite-tail certificates and the uniform threshold Q>=1100+24700(M+1), subject only to the inherited observer bridge and predecessor proof validity. For M=1 the same-row Q0=1000 certificate covers Q>=1000; the previously exact finite scan through 1900 has only negative Q=6..122. Combining these, for the frozen (m,r,k)=(0,1,115) experiment the full set of negative positions Q>=115 is exactly 115..122. Therefore

  N_full = D_0(123)/D_0(115)-1 = 0.07423055004043812 (rounded),
  N_tail(7) = -D_1(122)/D_0(115) = 0.0009682364760895871 (rounded),
  N_tail(U)=0 for every integer U>=8.

No new infinite scan. The fraction digest from PREFIX-1093 is 383b34fa31bd2a4658a51fc26c77ef8af2269164e3d0f61f018fa35097eff4e2. These exact equalities refer to this one frozen observer/experiment, not a result for arbitrary m,r,k or the mother problem.

## 7. Reproduction, verification and next

Companion standalone reproduction (immutable, exact readback):
dc4fcdd14e85a886f07b6484ee67acd260e5081a:research_notes/portable_direct/2026-11-26_r6_prefix1095_frobenius_certificate.py (blob f4e12c31e1f8f4dec0703836580a28a88bbc21de). It includes the original symbolic compression and K construction, the finite rational recurrence, exact CT moments, parameter enclosures, whole-interval Bernstein certificate and root bisection. The local executed calculation was split into three scripts (symbolic readout, gauge/series, anchors/sign), with the same formulas and assertions. The companion consolidates those computations and parent reproductions; it has not itself been independently rerun from the remote copy. Local exact runs completed: rank 28 and all 66 terms reconstructed; all 3 base and 3 mixed resonance compatibility entries zero; four 201-coefficient basis tables; exact integer recurrence through degree 3200 for y0, degree 2000 for each mixed anchor, all divisions exact; six bounded constants; full interval sign and derivative; 30 root bisection steps. The initial mixed h2 export attempt accidentally used a Python float zero in the n=0 previous-row placeholder and failed at rational interval serialization; corrected to Fraction(0), reran the entire anchor and sign calculation, and only corrected exact results are reported. The final local anchor/sign run took about 12.3 seconds before the derivative/bisection portion; no comparative performance claim. No independent review, native re-enumeration or checker formalization.

Next: independently reproduce the consolidated certificate and review load-bearing parent identities; then classify further lower-band zeros, determine whether b_last=b_low or additional sign changes occur, obtain certified c_last via derivative ratios, and work on the true mother p,d and B_fix,odd(32). The first edge is now tightly bracketed; do not repeat the large Gram-envelope optimization or finite sign scan for the resolved (0,1,115) tail. No Result freeze, Working Truth promotion, task closure or acceptance.
