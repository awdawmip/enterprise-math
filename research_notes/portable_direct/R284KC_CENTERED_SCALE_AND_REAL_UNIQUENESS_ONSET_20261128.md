# R284KC — Centered-scale relative normalization, signed real envelopes and uniqueness at d>=600

2026-11-28. Author written proof and executed exact rational certificate; NOT_REVIEWED. Ordinary auxiliary arithmetic of the R284 observer, no new native spatial attribution. Own session metadata recovered under r1-20261128-0705-own-recovery, identity EM-DIRECT-0C386E / TASK_RESEARCH from original registration receipt r1-20261124-0256-r284gd-session-v1. No own RUN. Owner inventory r1-20261128-0705-owner-inventory-v1 SUCCEEDED with no LEASED rows as of 2026-11-27T23:06:08.110424Z; no shared task mutation. Account entry snapshot 469c997c5d8a76420ca7dff07b97a70d4bf21d79; global P000 V4 projection canonical blob matched, Source P000 V5, ACTIVE worldview, joint/residual constraints and portable research protocol applied.

Frozen sources: KB 061919f2371e5f87f09204fc9dbb304bf25d79a8:research_notes/portable_direct/R284KB_PAIRED_LOG_AND_SHARPENED_UNIQUENESS_ONSET_20261128.md; KA 2ec462057a7401092c3627c153787deef3f1024f:research_notes/portable_direct/R284KA_EFFECTIVE_JOINT_SCALING_AND_FINITE_JET_REMAINDER_20261128.md. Their original definitions and JS root enclosure are unchanged. KB's sufficient onset was 25000 and root location error 3200d.

## Theorem

For every integer d>=600, C(q,d) has exactly one legal simple real zero q_d on q>=max(64,d^2/4), positive sign below and negative sign above. Moreover |q_d-alpha_* d^2|<182d, where alpha_* is the JS limit root. This reduces the sufficient onset by a factor 125/3 and the location bound by a factor 3200/182. It does not prove integer-root exclusion for this tail.

## 1. Centered normalization of the complete joint residual

Use KA and KB's h=1/d, s=d^2/q, x=k/d, y=1-x, phi=x^2+y^2/2. Write psi=phi-1/3=(3/2)(x-1/3)^2, hence 0<=psi<=2/3. Define tilde F_d=e^(2s/3) F_d, tilde L=e^(2s/3)L. Multiply every observation v,j,b,a,g,e0 by e^(s/3); denote these centered observations by the same symbols only within this proof. The exact KA identity is homogeneous of degree two in these observations, so its displayed expression is unchanged, now representing tilde F_d. In particular no endpoint or signed joint difference is dropped. This is an invertible common scalar transformation for the sign, zeros and local derivative at zeros; the original F_d is recovered by multiplying by e^(-2s/3). It is an auxiliary analytic coordinate, not a native physical state.

The centered limit is tilde L=28s I^2-12 I J, with I=int xy exp(-s psi), U=int x exp(-s psi), B=int xy^2 exp(-s psi), J=U-sB. For Re s>=0 the centered limiting node weight has modulus <=1. The shifted finite product is exp(s/3)R_u(k)R_m(d-k), and the shifted single endpoint R_u(d) has leading exp(-2s/3). Both admit the same paired-log estimates below.

## 2. Tighter paired log: real sign cancellation and complex envelope

For lambda=1,2 use the original factors (1+z_i)/(1+w_i), z_i=(s/lambda)h(1-ih), w_i=(s/lambda)h(1+ih+3h), i=0..k-1 or 0..l-1, respectively. For |s|<=S<=4, h<=1/600, their moduli are <=r=(2+2h)S h<1 because i<=d-1. As in KB the difference of logs minus z_i-w_i has modulus <=r|z_i-w_i|/(1-r). The linear sum of differences in the first branch is -s(x^2+2xh); in the second it is -(s/2)(y^2+2yh). Because x^2+y^2/2<=1 and x+y/2<=1, the sum of magnitudes of all factor differences is <=S(1+2h). Thus after subtracting -s phi the log residual is bounded by h K_c, where
Q=(2+2h) S^2 (1+2h)/(1-r), K_c=2S+Q.
For the real interval 0<=s<=S the linear residual -2s h(x+y/2) is nonpositive and the paired log residual is nonnegative: z_i<=w_i and derivative -t/(1+t)<=0 along the real pair. They have magnitudes <=2Sh and Qh respectively, so the joint bound is improved to h K_r with K_r=max(2S,Q), not their sum. The same argument applies to the single endpoint (x=1 with only the first branch). Exponentiation for either envelope gives centered finite product magnitude <=M=1+h P_err and error versus its centered limiting weight <=h P_err, where P_err=K/(1-Kh), by exp(t)-1<=t/(1-t) for 0<=t<1. The certificate checks Kh<1. All estimates apply at h<=1/600; the positive envelopes increase with h and may be evaluated at h=1/600.

## 3. Weighted propagation through the exact KA carrier

Use the exact rational weights T_k, G and P,P1,T,T1 of KB/KA (T here without index is the scalar residual coefficient). The identities remain:
v=h sum (x+h)(y+h)F_k, j=h sum (x+h)(1-T_k)F_k, b=v-hj,
g=h sum G[2(x+h)(y+h)-h(x+h)(1-T_k)]F_k,
a=(v+b)/4+h^2g,
where F_k is now the centered finite product, and e0 has its original rational weight times the centered endpoint.
T_k=s(y^2+hy/2)/(1+(s/2)(hx+h^2)).
On a complex half-disk use D_t=1-S h(1+h)/2; on the real interval use D_t=1 since the denominator is >=1. Then |T_k|<=T_max=S(1+h/2)/D_t and |T_k-sy^2|<=h T_err=h(S/2+S^2(1+h)/2)/D_t.

As in KB, v_max=(1/6+h(1+h)^2)M and |v-I|<=h v_err with v_err=P_err/6+(1+h)^2 M+(1+S/2)/2. These follow by h sum xy=(1-h^2)/6, x+y=1, and the left Riemann error for xy exp(-s psi) with |partial_x|<=1+S/2; its extra endpoint is zero.

For j define W bounding |1-sy^2| and Wt bounding |1-T_k|. Use W=1+S,Wt=1+T_max in the complex region and W=max(1,S-1),Wt=max(1,T_max-1) on the real interval (T_k is nonnegative). Put Jw=(1+h)(1/2+h)Wt, Xw=(1+h)W/2, Aw=(1+h)Wt. These bound h sum (x+h)|1-T_k|, h sum x|1-sy^2| and h sum |1-T_k| respectively. On the real interval sharpen each by taking the minimum with its following weighted bound:
Jw <= (1+h)(1/2+h)+S[1/12+h(1+h)(2+h)/6]+Sh/2[1/6+h(1+h)/2],
Xw <= (1+h)/2+S/12,
Aw <= (1+h)[1+S(2+h)/6+Sh/4].
Indeed 0<=T_k<=S(y^2+hy/2) there, and the symmetric inclusive sums obey h sum x=(1+h)/2, h sum y^2=(1+h)(2+h)/6, h sum xy=(1-h^2)/6, h sum xy^2=(1-h^2)/12 (the latter follows by symmetry and x+y=1). This retains the weighted road/background instead of charging the worst y-node to all x.
The three-term decomposition of j's node error in KB now yields
j_max=Jw M,
j_err=Xw P_err+(1+h)T_err M/2+Aw M+(W+S/2+2S W)/2+1,
|j-J|<=h j_err.
The last two terms cover the left Riemann error and extra endpoint: derivative of x(1-sy^2) exp(-s psi) has bound W+2S xy+2S W <= W+S/2+2S W because |psi'|<=2. All envelopes used here are increasing in h, including the minimum of two increasing bounds.

For the rest reuse KB's division-free joint carrier and product-error estimate with these newly computed constants, now without rounding individual envelopes. In detail:
b_max=v_max+h j_max, b_err=v_err+j_max.
G_max=[(3/2)S/(1-Sh)+(1+2h)S^2/(1-Sh)^2]/[2(2-Sh^2/(1-Sh))].
g_max=G_max(v_max+b_max), a_max=(v_max+b_max)/4+h^2g_max, a_err=(v_err+b_err)/4+h g_max. The bound for g follows by rewriting its bracket as the sum of the two branch weights; the absolute sum of b is bounded by v_max+h j_max. The centered e0_max=M(2+3h)/(2(2-2Sh-Sh^2))*(2+Sh+2Sh^2)/(8-4Sh-2Sh^2).
p1err=24S+3S^2(3+h)^2, Pmax=48+h(72S+h p1err), Tbound=96+32Sh(1+h). By the exact KA residual
tilde F_d=-24aj-96h a g+P1 ab-T1 a^2+hP e0 b-T[2 a s h(v+b)+s^2 h^3(v+b)^2],
its difference from tilde L is bounded by h E(S), where E is the sum of the six terms
24(a_err j_max+j_err/12),
p1err a_max b_max+72S(a_err b_max+b_err/12),
32S a_max^2+32S a_err(a_max+1/12),
96 a_max g_max,
Pmax e0_max b_max,
Tbound[2 a_max S(v_max+b_max)+S^2 h^2(v_max+b_max)^2].
The three leading limits use I<=1/6 in modulus, a~I/2,b~I,j~J. All denominators are positive as envelope bounds at h=1/600,S<=4; the corresponding exact rational functions are holomorphic on a neighborhood of each closed disk used below. Each envelope is nonnegative and nondecreasing with h. E evaluated at h=1/600 therefore bounds the coefficient of h for every smaller h, both for real and complex variants. These are fully propagated representation errors, not structural residuals or inferred signs from a numerical fit.

## 4. Exact grid plus analytic Lipschitz bounds

On real s in [0,4], |I^(j)|<= (2/3)^j/6, |U^(j)|<= (2/3)^j/2, |B^(j)|<= (2/3)^j/12. Therefore |J|<=5/6, |J'|<=23/36, |J''|<=13/27. Differentiating tilde L gives |tilde L'|<8 and |tilde L''|<12; the exact numerical inequalities are in the certificate.

At each of the 1601 nodes s=i/400, i=0..1600, integrate polynomial weights x,xy,xy^2 and each times psi against degree-15 and degree-16 Taylor polynomials for exp(-s psi). The Taylor remainder has alternating sign for real nonnegative argument (integral remainder), hence these bracket all six integrals. Exact Fraction interval operations enclose tilde L and tilde L'. Cover the exterior by the block [0,3/4] and the 22 blocks [j/8,(j+1)/8], j=10..31. For each block, use S equal to the upper endpoint and a sign margin M_B equal to the minimum certified signed node value minus 8/800. Every point of the block is within 1/800 of its included nodes, so M_B is a strict lower bound on the signed limit. For each block the executed exact certificate verifies M_B>0 and E_real(S)<520 M_B. Thus for d>=600 the centered exact residual is strictly negative on [0,3/4] and strictly positive on [5/4,4].

For the middle interval [3/4,5/4], the grid lower bound for tilde L' minus 12/800 is >743/1000. On each radius-3/4 complex disk centered at a point of this interval, Re s>=0, |s|<=2. The complex envelope E_c(2) bounds the value error; Cauchy's formula bounds the derivative error by E_c(2)/(3/4)d^-1<440/d. Consequently tilde F_d'>743/1000-440/600>9/1000 on the entire middle interval. This proves existence and strict uniqueness of the simple root s_d in (3/4,5/4), and the sign pattern everywhere on [0,4]. Since q=d^2/s reverses orientation, d>=600 implies legal q>=d^2/4>=64 and the claimed signs and uniqueness. Multiplication by the positive exp(2s/3) cannot change a real zero or its multiplicity.

## 5. Root location

The executed certificate also gives E_real(5/4)<91. Both s_* (in (.9,1) by frozen JS) and s_d lie in the middle interval, where tilde L'>743/1000. Since tilde F_d(s_d)=0 and tilde L(s_*)=0, apply the mean value theorem to the LIMIT rather than the exact function: |s_d-s_*|<91/(.743d). Hence |q_d-alpha_* d^2|<91d/(.743*.75*.9)<182d. This avoids dividing by the small derivative margin of the finite residual at its sufficient onset.

## 6. Executed evidence and next question

Certificate 6b5c27e82f351a98358c5d46eac97364f5516cfb:research_notes/portable_direct/R284KC_certificate.py, blob a416261acfe80b29d7d8143ce3ae9fd49bae6e4a, SHA256 c3ce1fb8f4056203d197bd2393ec0041abf257064208cdc66b37b0e57a34044c. Locally executed Python Fraction, no floats in certification; remote full readback matched exact code and local Git blob. Actual output:
1601 exact rational grid nodes; 23 exterior blocks PASS; E/margin < 520
scaled limit derivative > 743/1000; complex error derivative < 440/d
d>=600: scaled exact derivative > 9/1000; local value error < 91/d; q error < 182*d

This is a sufficient threshold, not the optimal threshold. The remaining previously uncovered finite bridge for real-root uniqueness is reduced to 81<=d<=599 (subject to the precise JR/JS finite evidence ranges). The next discriminating unit is a certified interval recurrence in s across those d, followed by exact nearest-integer root candidate tests. The existing JY/JZ subpower sparsity theorem and separate JR integer exclusion remain at their existing evidence scope. Full integer-root non-equality remains open. No independent review or formal checker claimed.
