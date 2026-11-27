# R284KA — Effective joint scaling, unique-root onset and finite-jet remainder algorithm

2026-11-28. Author written proof, NOT_REVIEWED. Ordinary auxiliary arithmetic for the R284 observer, not a native spatial attribution. Own session MCP-8cd6c4fa26b9459d923ff73ba0082220 recovered by r1-20261128-0505-own-recovery; no own RUN. Prior owner inventory r1-20261128-0400-leased succeeded, as of 2026-11-27T20:03:17Z, no LEASED rows. Current inventory r1-20261128-0505-leased submitted, not yet consumed. No new Task, claim, Result or shared-owner mutation. Account entry blobs verified against main@9e6c04a30073abfc40c177cadeb377477b872151; P000 V4/V5, ACTIVE worldview, joint/residual and portable contracts consulted.

Frozen science: JZ 02c66d94c16294f6722efc0a76ab2b034548b7ae:research_notes/portable_direct/R284JZ_FINITE_JET_RANK_AND_RESULTANT_SIEVE_20261128.md (blob ad0b97218865f7b0785fe442802ac8321d77c169); JS b081101b186a92ca04358892d678eb64b9d8f786:research_notes/portable_direct/R284JS_UNIFORM_SCALING_ROOT_AND_EVENTUAL_UNIQUENESS_20261127.md; JT 23bd59c52f6ea136f84c7b2da94776d4b2bfbd00:research_notes/portable_direct/R284JT_SECOND_ORDER_SCALING_AND_ROOT_DISTANCE_20261127.md (blob 27c491e2f3988f7b0c61c307d79f1daeacd2f7b4). Reuse JS's limit and uniqueness argument and JT's certified lambda interval; these dependencies are not independently re-certified. New contribution: explicit uniform leading error and onset, plus an effective arbitrary fixed-order remainder construction (not numerical execution of higher-order constants).

## 1. Exact normalized joint carrier

As in JS, q>=64, d>=3, d^2<=4q, u=q+d, m=2q+d, l=d-k, R_n(k)=prod_{i=0}^{k-1}(n-i)/(n+i+3).
a_k=(k+1)(l+1)R_u(k)R_m(l), b_k=(k+1)l R_u(k)R_m(l-1) with b_k=0 at l=0.
V=sum a_k, Q=sum b_k, A=sum [(u-k)(u+k+2)/(2u(2u+1))](a_k+b_k),
E=R_u(d)(u-d)(2d+3)(m+2)/(2(2u+1)(4m+2)), W=A+E, Z=qA+Q+V.
C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2.

Put h=1/d, s=d^2/q, x=k/d, y=1-x, phi=x^2+y^2/2, F_k=R_u(k)R_m(l).
Use v=V/d^3, b=Q/d^3, j=(V-Q)/d^2, a=A/d^3, e0=E/d.
With T_k=l(2l+1)/(m-l+1)=s(y^2+hy/2)/(1+(s/2)(hx+h^2)), the exact relations are
v=h sum_{k=0}^d (x+h)(y+h)F_k,
j=h sum_{k=0}^d (x+h)(1-T_k)F_k,
b=v-hj.
Set t=1/u=s h^2/(1+sh) and
G(x,s,h)=[(3/2)s/(1+sh)-(x^2+2xh)s^2/(1+sh)^2]/[2(2+t)].
Then the weight in A is 1/4+h^2 G, hence
g=h sum G [2(x+h)(y+h)-h(x+h)(1-T_k)]F_k,
a=(v+b)/4+h^2 g, b-2a=-hj/2-2h^2g.
Also e0=R_u(d)(2+3h)/[2(2+2sh+sh^2)] * (2+sh+2sh^2)/(8+4sh+2sh^2).

Let P=3(4+s(3h+h^2))^2=48+hP1, P1=24s(3+h)+3s^2 h(3+h)^2,
T=32(3+s(h+h^2))=96+hT1, T1=32s(1+h).
The full normalized residual has the following exact expression, with no negative power of h:
F_d(s)=C/(q^3 d^5)
= -24aj -96h a g + P1 ab - T1 a^2 + h P e0 b
  - T[2 a s h(v+b)+s^2 h^3(v+b)^2].
All endpoint contributions and the small joint difference are retained. Rational extension at s=0 is understood.

## 2. Explicit leading error including derivative

Theorem: for every integer d>=1024,
sup_{s in [0,4]} |F_d(s)-L(s)| <= 10^7/d,
sup_{s in [0,4]} |F_d'(s)-L'(s)| <= 10^7/d,
where I=int_0^1 xy exp(-s phi) dx, J=int_0^1 x(1-s y^2)exp(-s phi) dx,
L=28s I^2-12IJ.
The constants are deliberately conservative.

Proof. Work on the complex neighborhood U=union of closed unit disks centered on [0,4], so |s|<=5, Re s>=-1. Each factor of R_(lambda q+d) for lambda=1,2 is (1+z)/(1+w), z=(s/lambda)h(1-ih), w=(s/lambda)h(1+ih+3h). Their absolute values are <=5h and <=11h, respectively. For d>=1024 the principal analytic log series has |log(1+z)-z|<=|z|^2 (likewise w). For k<=d the linear sum is -(s/lambda)(x^2+2xh). Per branch the accumulated error relative to -(s/lambda)x^2 is <=(25+121+10)h=156h. Joint log error <=312h. Since |exp(-s phi)|<=e<3, and exp(312/1024)<2, it follows that |F_k|<=6 and |F_k-exp(-s phi)|<=1900h. The same bound 6 holds for R_u(d).

The exact T_k has |T_k-s y^2|<=36h by the denominator bound 1-3h; |T_k|<=6. For v the integrand node error is at most 12h+(1/4)1900h=487h. The sum h times the number of nodes is <=2, and the derivative in x of xy exp(-s phi) is bounded by 11, with zero endpoint at x=1. The left Riemann sum error is <=11h/2. Therefore |v-I|<=1000h.
For j, the node error is <=42h+216h+6*1900h=11658h (split off h, T_k-s y^2, and product error). The x derivative of x(1-s y^2)exp(-s phi) is <=230, and its extra endpoint contributes <=3h. Thus |j-J|<=24000h.
The corresponding absolute-sum bounds give |v|<=4, |j|<=168, |b|<=5 and |b-I|<=1168h. In these absolute-sum bounds use h sum 1<=2, (x+h)(y+h)<=1/4+2h, x+h<=2, |1-T_k|<=7. The rational formula gives |G|<=20: |1+sh|>=.99, |t|<=6h^2, its numerator <=8+36(1+2h), denominator >=3. Using the absolute-sum bounds for v and b gives |g|<=200. Hence |a|<=3 and |a-I/2|<=600h. The rational formula for e0 gives |e0|<=10 (both original ratios (u-d)/(2u+1), (m+2)/(4m+2) have modulus <=1). Also |I|<=1/2.

Now |P1|<=400, |P1-72s|<=1320h, |T1-32s|<=160h, |P|<=49, |T|<=97. In the exact residual of section 1 compare -24aj, P1 ab, -T1 a^2 with -12IJ, 36s I^2, -8s I^2 respectively; all other terms carry h. Their errors divided by h are bounded by
24(600*168+24000/4),
1320*15+360(600*5+1168/4),
160*9+160*600*(3+1/4),
96*3*200,
49*10*5,
97(2*3*5*9+25*81/1024^2).
Their sum is strictly less than 10^7. This proves the uniform complex value bound. All functions are holomorphic on a neighborhood of each closed unit disk, since their rational denominators and log factors stay away from zero. Cauchy's derivative formula on the unit circle gives the same error bound for the first s derivative at each real center. This proves both inequalities without differentiating the discrete approximation.

## 3. Numerical effective onset of unique legal real root

Theorem: for every integer d>=40000000000000 (=4*10^13), C has exactly one legal real zero q_d, simple, positive below it and negative above it on q>=d^2/4. Moreover |q_d-alpha_* d^2|<=6*10^7 d. No claim is made about the optimal onset or all the intermediate d.

Proof. Reuse JS's R(alpha)=alpha E_alpha[1/y]-E_alpha[y], R<3alpha-1/2, R>=alpha-1, and derivative lower bound R'>=1-2/(3alpha)-1/(6alpha^2) for alpha>=9/10 (the same covariance argument as JS applies there, since the coefficient of E[1/y] is positive). The latter bound is >1/20 on that interval. The unique root s_*=1/alpha_* lies in (.9,1) by JS. JT proves lambda_*=s_*^2 L'(s_*)>.4, so L'(s_*)>.4.
For real s in [0,4], |I^(j)|<=1/6 for j=0,1,2. Write J=U-s B, U=int x exp(-s phi), B=int xy^2 exp(-s phi), with derivatives of U bounded by 1/2 and B by 1/12. Thus |J|<=5/6, |J'|<=11/12, |J''|<=1. Differentiating L twice gives |L''|<24. On |s-s_*|<=1/200 we have L'>.28.

Outside this interval, |L(s)|>1/2000000:
- For s<=1/8, L=12s I^2(7/3-R(1/s))<=12 I^2((10/3)s-1)<=-7 I^2, and I>=1/18; s=0 follows by continuity.
- For 1/8<=s<=10/9, alpha>=9/10 and R' >1/20 imply |R(1/s)-R(alpha_*)| >= (9/10)|s-s_*|/20. Here I>=1/24 (exp(10/9)<4). Hence |L|>=12*(1/8)*(1/24)^2*(9/10)*(1/20)*(1/200)=0.0000005859375 >1/2000000.
- For s>=10/9, alpha<=.9, R<3alpha-1/2<=2.2; thus 7/3-R>2/15. Use I>=1/360 (exp(4)<60) to obtain |L|>1/2000000.

At d>=4*10^13 the value and derivative errors are <=1/4000000, so F_d agrees in sign with L outside the interval and F_d'>1/4 inside. The intermediate value theorem and monotonicity give the unique simple root s_d, and hence q_d. Since F_d(s_*) is bounded by 10^7/d, the mean value theorem gives |s_d-s_*|<=4*10^7/d. On the chosen interval s_d*s_*>.8, so inversion yields the claimed q error. The signs reverse when converting s to q, as required. This is an explicit though very large sufficient onset; it is not a practical finite bridge from JR's d<=80.

## 4. Effective arbitrary fixed-order remainder, algorithmic bounds

The following extends the qualitative JV fixed-order expansion to computable upper envelopes, as requested by JZ. It is a written construction; no high-order numerical envelope is claimed.

For integer N>=1, form a polynomial log jet for each branch:
sum_{r=1}^{N+1} (-1)^(r+1)(s/lambda)^r h^r/r
  * sum_{i=0}^{k-1} [(1-ih)^r-(1+ih+3h)^r].
At k=x/h and h=1/d, evaluate each inner sum by the exact Faulhaber polynomial. The result is a polynomial in x,s,h: a monomial of i-degree j has at least h^(r+j), its finite sum is of degree <=j+1 in k, so the lowest h power is >=r-1. The h^0 coefficient is -(s/lambda)x^2. Truncate the polynomial at h^N. The tail in the finite polynomial is bounded by B_N h^(N+1), where B_N is the sum of absolute coefficients weighted by 5^(s-degree), since 0<=x<=1, h<=1. The omitted log series terms have combined error <=3*11^(N+2) h^(N+1) per branch (geometric tail per factor, at most d factors, 11h<=11/1024). Sum the two errors for the joint log, with y=1-x in the second branch. These give a computed log error constant L_N. If L_N h^(N+1)<=1, exponentiation costs at most 18 L_N h^(N+1) because the exact joint product is bounded by 6 and exp(1)<3. For the single endpoint branch the same estimates apply.

For each normalized node function in v,j,g and the endpoint e0, replace the product by exp of its polynomial log jet. The other factors are the explicit rational weights in section 1, analytic in h on |h|<=1/32 uniformly in s in U, x in [0,1]. Indeed the denominators 1+sh, 1+(s/2)(hx+h^2), 2+t, 2+2sh+sh^2 and 8+4sh+2sh^2 are separated from zero by elementary triangle bounds at |s|<=5. Bound the rational factors there by numerator absolute-coefficient sums and these denominator margins; bound the exponential by exp of the absolute-coefficient sum of the log jet on that disk. A computed bound M_N for each analytic node function on |h|=1/32 then gives a Taylor tail <=2 M_N 32^(N+1) h^(N+1) for h<=1/64, by Cauchy's formula and geometric summation. Add the earlier exponential replacement error times the bounded weight. The Taylor coefficients f_j(s,x), j<=N, are polynomials in x,s times exp(-s phi) (or the single endpoint exponential), explicitly obtainable by truncated rational arithmetic.

For the inclusive node sum of each f_j use Euler-Maclaurin:
h sum_{k=0}^d f_j(s,kh)=int f_j + (h/2)(f_j(s,0)+f_j(s,1))
+sum_{p=1}^P B_{2p} h^(2p)/(2p)! [partial_x^(2p-1) f_j(s,1)-partial_x^(2p-1) f_j(s,0)] + remainder.
Choose 2P>=N-j+1. The error is at most h^(2P) max_[0,1]|B_(2P)(x)|/(2P)! times sup |partial_x^(2P) f_j|, valid for complex values as well. The derivative bound is computed by differentiating the polynomial-exponential expression and taking weighted coefficient absolute sums (|s|<=5, |exp(-s phi)|<=3). Truncate all displayed terms of h-degree>N-j and add their explicit coefficient bounds. The prior node error is multiplied by h(d+1)<=2. Consequently one obtains explicit finite jets and computable error constants for v,j,g,e0. For b and a, use their exact polynomial relations; propagate errors through products in the division-free residual of section 1 using ordinary finite coefficient convolution and product error bounds (e.g. |AB-ab|<=|A-a||B|+|a||B-b|). This yields L_0=L and functions L_1,...,L_N and a computable K_N,D_N such that
sup_U |F_d(s)-sum_{j=0}^N h^j L_j(s)|<=K_N h^(N+1) for integer d>=D_N.
Cauchy gives the same derivative bound on [0,4]. Coefficient functions consist of integrals of polynomial-exponential weights, endpoints, sums and products, and are analytic with computable sup bounds on U. Bounds involving exp of explicit positive constants may be rounded upwards to integers by convergent Taylor bounds. No cancellation was assumed in bounding errors: the exact joint cancellation was performed first.

## 5. Effective transfer to the root jet

Let S_N(h)=s_*+sum_{j=1}^N a_j h^j, choosing a_j successively by the formal identity sum_{j=0}^N h^j L_j(S_N(h))=0 mod h^(N+1). At each stage the new coefficient has multiplier L'(s_*)>.4. Coefficients and upper bounds are computable from the certified s_* enclosure, analytic derivatives and finite integrals; interval refinement by rational Taylor bounds and bisection computes s_* to any requested precision, using its simple crossing (an exact equality at a rational midpoint can be avoided by searching for strict opposite-sign rational brackets).
Choose a positive rational radius r<=1/2 such that sum |a_j| r^j <=1/400, using computed upper bounds. Then S_N lies within the complex disk |s-s_*|<=1/400 on |h|<=r. If B bounds sum r^j sup|L_j| there, Cauchy's formula in h gives
|sum h^j L_j(S_N(h))| <=2 B r^(-N-1) h^(N+1), for h<=r/2.
For d also above the onset of section 3 and D_N, the exact residual at S_N is bounded by (K_N+2B r^(-N-1)) h^(N+1). Both S_N and s_d lie in the real local derivative interval, hence
|s_d-S_N(h)|<=4(K_N+2B r^(-N-1)) h^(N+1).
Since s_d and S_N are >.89, reciprocal error costs at most 2 times this bound. Finally expand 1/S_N in h to order N on the same disk, where |1/S_N|<=2. The Cauchy tail is <=4 r^(-N-1)h^(N+1). Multiplying by h^-2 gives the effective root remainder O(h^(N-1)), with explicit computable constant 8(K_N+2B r^(-N-1))+4 r^(-N-1).
In particular N=4m+2 supplies the JZ finite jet through c_(4m), with an actual algorithm for the required R and D0. One must still evaluate those constants for a chosen m; merely knowing the algorithm does not provide a useful numerical JZ onset.

## 6. Scope and next question

New numeric sufficient uniqueness onset 4*10^13, uniform leading error 10^7/d, and explicit finite algorithms for every fixed-order observer/root remainder. Author checked the written inequalities; no independent reviewer, high-order calculation or formal checker executed. JZ's subpower bound is unchanged. The threshold is very conservative and leaves a large finite bridge. Next: sharpen the uniform constants (separate local root and global sign bounds, use smaller real-domain product estimates or interval subdivisions) and actually compute a low-order effective root enclosure; pursue pointwise arithmetic exclusion rather than treating asymptotic uniqueness or sparsity as full non-equality.
