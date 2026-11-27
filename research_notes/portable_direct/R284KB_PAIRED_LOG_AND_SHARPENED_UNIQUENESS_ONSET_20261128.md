# R284KB — Paired logarithmic residual and sharpened effective real-root onset

2026-11-28. Author written proof and exact rational certificate, NOT_REVIEWED. Ordinary auxiliary arithmetic of the R284 observer; no new native spatial attribution. Own session MCP-8cd6c4fa26b9459d923ff73ba0082220 metadata recovered via r1-20261128-0600-own-recovery, no own RUN. Previous owner inventory r1-20261128-0505-leased SUCCEEDED, as of 2026-11-27T21:06:38.613389Z, no LEASED rows. Current r1-20261128-0600-leased RUNNING at last check; no shared task mutation. Account entries verified against main@5ea2df445caa2aa064d4b50d862fe6a9535fc720; P000 V4/V5, ACTIVE worldview, portable and joint/residual contracts consulted.

Frozen input: KA 2ec462057a7401092c3627c153787deef3f1024f:research_notes/portable_direct/R284KA_EFFECTIVE_JOINT_SCALING_AND_FINITE_JET_REMAINDER_20261128.md (blob fcfe9e767e9cd6af0f4c709330b0b9683a145747), including the exact division-free joint carrier; JS b081101b186a92ca04358892d678eb64b9d8f786:research_notes/portable_direct/R284JS_UNIFORM_SCALING_ROOT_AND_EVENTUAL_UNIQUENESS_20261127.md for the limit-root enclosure. Reuse their definitions and algebraic identity, not a new scientific pin. KA previously gave sufficient d>=4*10^13 and error 10^7/d.

## Theorem
For all integer d>=1024, on s in [0,4] the full normalized residual F_d(s)=C(q,d)/(q^3 d^5), q=d^2/s, satisfies |F_d-L|<=2100/d. On [3/4,5/4] the sharper bounds |F_d-L|<=300/d and |F_d'-L'|<=1200/d hold. Rational extension at s=0. For every integer d>=25000, C has exactly one simple real root q_d in the legal domain q>=max(64,d^2/4), with positive sign below and negative above it. Further, |q_d-alpha_* d^2|<=3200 d. No all-integer exclusion is inferred from real-root uniqueness. JR's d<=80 integer exclusion and the prior JY/JZ subpower result are unchanged.

## 1. Paired log instead of independent log errors

Write h=1/d, x=k/d, y=1-x, phi=x^2+y^2/2. In a branch R_(lambda q+d)(k), lambda=1 or 2, each factor is (1+z_i)/(1+w_i), with z_i=(s/lambda)h(1-ih), w_i=(s/lambda)h(1+ih+3h). Use the same pair throughout: for |z|,|w|<=r<1,
log(1+z)-log(1+w)-(z-w)= integral along w to z of -t/(1+t) dt,
so its modulus <= |z-w| r/(1-r). This retains the joint numerator/denominator difference, rather than bounding two independent Taylor tails.

For |s|<=S, Re s>=0, h<=1/1024, take r=3Sh. The linear sum is -(s/lambda)(x^2+2xh) in the first branch and the same formula with y in the second. Since x^2+y^2/2<=1 and x+y/2<=1, the joint log error is bounded by h[2S+3S^2(1+2h)/(1-3Sh)]. The bracket is <61 for S=4 and <11 for S=3/2, by exact rational substitution at h=1/1024 (the envelopes are increasing in h). The single endpoint R_u(d) obeys the same upper bounds on log error. Since |exp(-s phi)|<=1, and exp(t)-1<=t/(1-t) for 0<=t<1, the joint product F_k=R_u(k)R_m(d-k) satisfies |F_k-exp(-s phi)|<=Perr*h and |F_k|<=M, where (Perr,M)=(65,1.064) globally, (12,1.012) locally. The same absolute M bounds R_u(d). This step is a joint-residual compression with an explicit error; it does not discard either factor.

## 2. Propagation through the exact KA carrier

Use the exact quantities from KA:
T_k=s(y^2+hy/2)/(1+(s/2)(hx+h^2)),
v=h sum (x+h)(y+h)F_k,
j=h sum (x+h)(1-T_k)F_k,
b=v-hj,
t=sh^2/(1+sh),
G=[(3/2)s/(1+sh)-(x^2+2xh)s^2/(1+sh)^2]/[2(2+t)],
g=h sum G[2(x+h)(y+h)-h(x+h)(1-T_k)]F_k,
a=(v+b)/4+h^2g.
Endpoint e0=R_u(d)(2+3h)/[2(2+2sh+sh^2)] * (2+sh+2sh^2)/(8+4sh+2sh^2).
All sums run k=0..d inclusive. Let I=int xy exp(-s phi), J=int x(1-s y^2)exp(-s phi), both over [0,1]. For Re s>=0, |I|<=1/6. Set D_t=1-S h(1+h)/2, T_max=S(1+h/2)/D_t and T_err=(S/2+S^2(1+h)/2)/D_t. Then |T_k|<=T_max, |T_k-sy^2|<=h T_err by triangle inequalities on its exact rational representation.

The absolute node sums for v,j are bounded by M(1/6+h(1+h)^2) and M(1+h)(1/2+h)(1+T_max). Indeed h sum xy=(1-h^2)/6, h sum x=(1+h)/2, h sum 1=1+h and x+y=1. For v-I the node error divided by h is <=Perr/6+M(1+h)^2. The left Riemann sum error divided by h is at most (1+S/2)/2 because |partial_x(xy exp(-s phi))|<=1+S/2 (|phi'|<=2), and its extra endpoint is zero. For j-J, decompose the node error into x(1-sy^2)(F_k-exp(-s phi)), x(sy^2-T_k)F_k and h(1-T_k)F_k. Its bound divided by h is
(1+h)(1+S)Perr/2+(1+h)T_err M/2+(1+h)(1+T_max)M.
The left Riemann error plus the endpoint divided by h is <=(1+3S+2S(1+S))/2+1 by differentiating x(1-sy^2)exp(-s phi). The endpoint has modulus <=1. Bounds for b use v-hj, including the sum of absolute node terms of b. Hence the absolute sum in g is bounded by G_max(v_max+b_max); G_max follows from the exact G by triangle inequalities. All envelope rational expressions are positive and increasing in h on the chosen range, so evaluating them at 1/1024 proves bounds for all smaller h.

The following verified bounds are respectively for S=4 and S=3/2:
|v|<=.18,.17; |v-I|/h<=14,4;
|j|<=2.7,1.3; |j-J|/h<=210,28;
|b|<=.183,.172; |b-I|/h<=17,5.3;
|G|<=6,1.2; |g|<=2.3,.42;
|a|<=.092,.087; |a-I/2|/h<=8,2.4;
|e0|<=.14 in both.
The bound for e0 follows directly from its exact displayed formula with |R_u(d)|<=M and reverse triangle inequalities in both denominators. These numbers bound the full complex expressions, not merely sample values.

Write P=48+hP1, P1=24s(3+h)+3s^2 h(3+h)^2 and T=96+hT1, T1=32s(1+h). We have |P|<=49, |T|<=97, |P1-72s|<=h p1err with p1err=530,97 respectively, and |T1-32s|<=32Sh.
KA gives the exact division-free residual
F_d=-24aj-96hag+P1 ab-T1 a^2+hP e0 b-T[2ash(v+b)+s^2h^3(v+b)^2].
Compare the three leading terms with -12IJ+36sI^2-8sI^2=L. Product-error bounds, divided by h, are
24(aerr*jmax+jerr/12);
p1err*amax*bmax+72S(aerr*bmax+berr/12);
32S*amax^2+32S*aerr(amax+1/12).
The remaining three terms are bounded after division by h by
96*amax*gmax;
49*.14*bmax;
97[2*amax*S(vmax+bmax)+S^2 h^2(vmax+bmax)^2].
The exact sum is below 2006 (ceiling 2006) for S=4, below 258 (ceiling 258) for S=3/2; rounded bounds 2100 and 300 suffice. On real s in [0,4] use S=4. On closed radius-1/4 complex disks centered on [3/4,5/4], use S=3/2, Re s>=1/2. All rational denominators and log factors are separated from zero on these disks and their neighborhoods. Cauchy's formula therefore gives |F_d'-L'|<=1200h on [3/4,5/4]. No separate real derivative estimate of the original sums is assumed.

## 3. Exact grid-to-continuum certificate

For real s in [0,4], write U=int x exp(-s phi), B=int xy^2 exp(-s phi), J=U-sB. For derivatives of order 0,1,2, |I^(j)|<=1/6, |U^(j)|<=1/2, |B^(j)|<=1/12, because 0<=phi<=1. Thus |J|<=5/6, |J'|<=11/12, |J''|<=1. Differentiating L=28sI^2-12IJ gives |L'|<12, |L''|<24. These are explicit global Lipschitz controls for the grid extension.

For each grid point evaluate the exponential integral against nonnegative polynomial weights x, xy, xy^2, and each times phi as needed. The Taylor polynomials of degrees 23 and 24 for exp(-z) bracket the exponential for z>=0 by the signed integral Taylor remainder. Thus exact rational polynomial integration and interval addition/multiplication enclose I,U,B and their first derivatives. No floating point error or estimated quadrature appears.

Executed certificate: all 751 grid points i/1000, i=0..750, have L upper bound <-1/10; all 2751 points i/1000, i=1250..4000, have lower bound >1/10. All 101 grid points i/200, i=150..250, have L' lower bound >1/4. Every point in either exterior closed interval is within 1/2000 of the relevant grid; every point of the interior closed interval within 1/400 of its grid. Consequently
L<-47/500 on [0,3/4]; L>47/500 on [5/4,4]; L'>19/100 on [3/4,5/4].
The actual executed Python Fraction code also checks all rational envelope constants of section 2. Output:
S 4 error bound ceiling 2006 claimed 2100
S 3/2 error bound ceiling 258 claimed 300
grid 751 2751 derivative 101 PASS; d>=25000, Fdprime>0.14 on [0.75,1.25]

Code: e35d58059a1024555acfc00ce8b852f90dbdc5f4:research_notes/portable_direct/R284KB_certificate.py; Git blob 68a432385fcc9991dba2935177a666fb5ac77ee6, SHA256 dcddb115ae616056eb7fdf7459055c18b6b96685e222befc8ab4b47f05db81ef. Local execution passed and local Git hash matches full immutable connector readback.

## 4. Unique root and explicit location

For d>=25000, 2100/d<47/500, so F_d has opposite strict signs on the two exterior intervals. On the interior, 1200/d<=.048<.05 and F_d'>.14. The intermediate value theorem gives exactly one simple root s_d in (3/4,5/4). The sign reverses in the q coordinate, q=d^2/s, and q>=d^2/4 implies q>=64 at this onset. JS gives s_*=1/alpha_*>.9 and s_*<1, so the mean value theorem with local error 300/d yields |s_d-s_*|<=300/(.14d). Since s_d*s_*>.75*.9, inversion yields |q_d-alpha_*d^2|<=3200d. This is a factor 1.6 billion improvement in the sufficient onset, not an optimal onset proof.

## 5. Scope and recovery

Scientific increment: paired-log error preserving numerator/denominator residual, two-domain bounds plus exact grid-to-continuum certification, explicit onset 25000 and root-location constant 3200. Not an independent review/formal checker or pointwise integer-root exclusion. Remaining finite bridge for real-root uniqueness: d below 25000 beyond previously verified ranges; JR integer exclusion for d<=80 remains separate. Next: exploit the newly bounded local interval to build tighter effective root jet / modular candidates; investigate efficient exact finite bridge without computing all high-degree polynomials. Preserve the existing JZ asymptotic sieve and original p-adic route; no claim about an integer-root-free tail.
