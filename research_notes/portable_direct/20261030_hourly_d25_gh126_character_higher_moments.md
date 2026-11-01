# D25/LIFT GH-126 — higher marked character moments and the exact zero band

2026-10-30 Asia/Hong_Kong. Research lane chatgpt-research-hourly-enterprise-math-20260923, parent D25/LIFT/JT2 OPEN. Scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## GH-126 theorem

For every odd prime p>=5, q=p², k=F_q, N=(p-1)/2, f_B(X)=X³+X²+BX and quadratic chi_q(0)=0, define H_p(B)=[X^(p-1)]f_B(X)^N and S_r(B)=sum_(x in k, f_B(x)!=0) chi_q(f_B(x)) (x/f_B(x))^r. Then for *every B in k* and every integer 1<=r<=N,

  S_r(B)=((-1)^(r+1) 2^r / (2r-1)!!) H_p^(r)(B) H_p(B)^p.

The denominator (2r-1)!! is invertible mod p for these r. In particular S_1=2H'_p H_p^p, S_2=-(4/3)H''_p H_p^p. Moreover,

  S_r(B)=0  for all floor(N/2)<r<=N, at every B in F_(p²).

For p=8m+3>=11, the zero band is the 2m+1 consecutive orders r=2m+1,...,4m+1. At p=3347 this means **all 837 orders r=837,...,1673 vanish** as signed character sums. Individual summands need not vanish.

**Proof.** GH-124 established as a polynomial identity Phi_q(B):=-sum_x f_B(x)^e=H_p(B)H_p(B)^p, e=(q-1)/2. Differentiate r times formally. The Frobenius H_p^p factor has zero derivative; on the sum, Phi_q^(r)=-e(e-1)...(e-r+1)sum_x x^r f_B(x)^(e-r). For 1<=r<=N, e-r>=1, so zero cubic terms contribute zero and other terms equal chi_q(f)*(x/f)^r. In F_p, each e-j=-1/2-j and -e^(underline r)=(-1)^(r+1)(2r-1)!!/2^r is invertible. Solve for S_r. To determine the Hasse degree, expand f_B(X)^N=X^N(X²+X+B)^N. The coefficient of X^(2N) requires the count of X² factors to equal the count of B factors, so exactly

  H_p(B)=sum_(u=0)^floor(N/2) [N!/(u!²(N-2u)!)] B^u.

Its degree is floor(N/2), with nonzero leading coefficient mod p. All higher formal derivatives vanish, which proves the zero band. QED. This is an exact finite-field power-sum/Hasse polynomial proof and does not invoke GH-98–GH-103 finite logarithms.

## GH-126 second-jet numerical certificates

For the GH-121 three F_(3347²)-isomorphic marked models, write F_(3347²)=F_3347[r]/(r²-2), (a,b)=a+b*r. With B=(1+T)/8, the r=2 formula becomes S_2=-(256/3) H''(T)H(T)^p. A new executed C++17 checker independently sums chi_q(f_B(x))*(x/f_B(x))² over all 11,202,409 elements for EACH marked model (33,607,227 total), with Hasse derivative computed only as a separate target.

| Origin | H''(T) | Direct S_2 |
|---|---|---|
| original z=9 | (563,0) | (2872,0) |
| alternate 1 | (257,1710) | (3058,3036) |
| alternate 2 | (1312,354) | (665,3338) |

All values agree with the formula, while the three integer Frobenius traces remain -6106. Another executed exact Python program checks **every r=1,...,N** moment and the zero band for each of the seven primes 11,19,43,59,67,83,107, without replacing the direct character sum by the derivative formula. Outputs: PASS_GH126_SECOND_CHARACTER_MOMENT_3_ORIGINS and PASS_GH126_ALL_HIGHER_MOMENTS_AND_ZERO_BAND_P_LE_107. Both validations are finite exact arithmetic; the universal statement follows from the proof.

Run: g++ -std=c++17 -O3 -Wall -Wextra -Werror d25_gh126_higher_character_moment_check.cpp -o check && ./check; python d25_gh126_small_higher_moments.py.
Code Git blob: 0d536eb599109dfdd5d7a6f40830f08e3bb46db8 and 464dfb94b4d8c11ba98c97061b3cc101e5f1e03e.

BRC COMPOSE_APPLIED: signed branch character and exact rational field values (x/f)^r are retained until summation. A zero in the band is a cancellation theorem for that observer, not lossless elimination of branches, native physics, or higher arbitrary operations. The algebraic parameter is an external chart, not X6 time.

**Next:** obtain a genuinely independently *evaluated* marked CM/Jacobi/Gauss or p-adic-period expression for S_1 at T²=8/9, proving its exact special value without assuming GH-83. The link to integrated R_3347(9), GH-3 and native p=373 remain independent. Research-authority control is still at issue #1558; no native CLAIM, OPEN, checkpoint, freeze or review occurred in this portable unit.
