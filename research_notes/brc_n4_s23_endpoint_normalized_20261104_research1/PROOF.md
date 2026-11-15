# BRC N=4/S23: endpoint-normalized twelfth-order Chernoff error certificate

Date: 2026-11-04. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen model

Scientific input is pinned to awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Direct predecessor: PR #1765@4914ce9caa8dd18710e62f6a70e5ae109dd4d46f, research_notes/brc_n4_s23_cubic_chernoff_global_v12_proxy_20261104_research1/PROOF.md.

For real 0<s<=1 and 0<v=2h<=1/21 put k=s/(2-s), R=1-v^2, alpha=atanh(v), gamma=atanh(kv), X=s sqrt(1-v^2)/2, Y=(2-s)sqrt(1-k^2 v^2)/2, and Z_s(d)=X exp(alpha*d)+Y exp(-gamma*d). These are the Chernoff coefficients of the two Bernoulli laws with success probabilities s(1+v)/2 and s(1-v)/2, parameterized by d in [-1,1]. The full-source laws are (s(1+v)/2,1-s,s(1-v)/2) and the swapped version. Assigned costs c_T=2-s and c_B=1.

The predecessor established the exact minimizing exponent

delta_*=[psi(kv)-psi(v)]/[alpha+gamma], psi(x)=log(sqrt(1-x^2)*atanh(x)/x), psi(0)=0,

and the cubic rational surrogate

d_3=(1-k)v/6 + (1-k)(9k^2+10k+9)v^3/180,

with both delta_* and d_3 in [0,1/125). Let C_B=-log Z_s(delta_*), C_3=-log Z_s(d_3), and C_T=-log(1-s+s sqrt(1-v^2)).

## New theorem: adaptive endpoint factors

For every real 0<s<1 and 0<v<=1/21:

(A) |delta_*-d_3| <= (16/5)(1-k)v^5 < 4(1-k)v^5.

(B) 0<=C_B-C_3<=32s(1-k)^2 v^12/R^2 = 128s(1-s)^2 v^12/((2-s)^2 R^2).

(C) 0<=(C_B-C_3)/[s(1-s)] <=32v^12/R^2 <=1/228828299134050 < 10^-14.

The information error extends continuously as zero at s=0 and at s=1, and the normalized error tends to zero when s->1. With F=C_T/(2-s)-C_B and F_3=C_T/(2-s)-C_3, the rigorous full-open-interval sign enclosure is

F_3/[s(1-s)]-32v^12/R^2 <= F/[s(1-s)] <= F_3/[s(1-s)].

The stronger pointwise lower correction is 128(1-s)v^12/((2-s)^2 R^2). This removes the preceding fixed absolute proxy error's endpoint obstruction.

## Proof

1. Differentiate the analytic remainder. Let u(x)=atanh(x)/x-1=sum_{n>=1} x^(2n)/(2n+1), and e(x)=psi(x)+x^2/6+19x^4/180, for 0<=x<=v, with R=1-v^2. At zero all formulas use their continuous extensions. The identity psi'(x)=u'(x)/(1+u(x))-x/(1-x^2), and u'/(1+u)=u'-u*u'+u^2*u'/(1+u), gives the error formula after the first two odd powers cancel.

Use elementary positive-series estimates:

0<=u-x^2/3<=x^4/(5R); 0<=u'-2x/3<=x^3/R;
0<=u'-2x/3-4x^3/5<=x^5/R; u<=x^2/(3R); u'<=x/R;
0<=x/(1-x^2)-x-x^3<=x^5/R.

They imply |u*u'-2x^3/9|<=x^5[7/(15R)+v^2/(5R^2)] and 0<=u^2*u'/(1+u)<=x^5/(9R^3). Consequently,

|e'(x)| <= x^5[37/(15R)+v^2/(5R^2)+1/(9R^3)] <3x^5.

The bracket is increasing in v and at v=1/21 is exactly 220166457/85184000 <3. Integrating over x from kv to v gives

|e(kv)-e(v)| <=v^6(1-k^6)/2 <=3(1-k)v^6.

2. Recover the endpoint factor in the optimizer. Write D=alpha+gamma=(1+k)v+(1+k^3)v^3/3+r_D, with 0<=r_D<=(1+k^5)v^5/(5R). Write N=psi(kv)-psi(v); its quadratic and quartic components are (1-k^2)v^2/6 and 19(1-k^4)v^4/180, and its remainder is e(kv)-e(v). Let d_3=(1-k)(v/6+P v^3/180), P=9k^2+10k+9<=28. The exact polynomial cancellation identities from the predecessor remove terms through v^4 in D*d_3-N. The remaining terms satisfy

|D*d_3-N| <= (1-k)v^6 [3+14/135+1/(15R)+(14/225)v^2/R].

The bracket is increasing in v and reaches exactly 941687/297000 <16/5 at v=1/21. Since D>=(1+k)v>=v and delta_*=N/D, (A) follows.

3. The curvature inherits the Bernoulli mass s. Both exponents and their connecting segment lie in [0,1/125]. For the positive mixture weight w=X exp(alpha d)/Z_s(d), the Chernoff exponent parameter is in [0,1]. The sum of coordinatewise minima of the two Bernoulli laws is 1-sv, so Z_s(d)>=1-sv>=20/21. Further X<=s/2, alpha<=v/R<=21/440, and exp(z)<=1/(1-z) for 0<=z<1. Thus

w<=[21s/40]/[1-21/(440*125)]=(28875/54979)s<s.

Set L(d)=log Z_s(d). The two-point exponential tilt identity gives L''(d)=w(1-w)(alpha+gamma)^2<=s(2v/R)^2. Since L'(delta_*)=0 and d_3 is in the same interval, Taylor's integral remainder and (A) give

0<=L(d_3)-L(delta_*) <= (1/2)(4sv^2/R^2)[4(1-k)v^5]^2
=32s(1-k)^2v^12/R^2,

which equals C_B-C_3, proving (B).

4. Normalize. Use 1-k=2(1-s)/(2-s). For t=1-s in (0,1), (2-s)^2=(1+t)^2>=4t, since (1-t)^2>=0. Dividing (B) by s(1-s) yields (C), and 32(1/21)^12/(1-1/21^2)^2 is exactly 1/228828299134050. Subtracting C_B and C_3 from the same cost-adjusted C_T proves the normalized F enclosure. The explicit factor in (B) gives zero error at both ends, and the normalized upper envelope tends to zero at s=1. QED.

## Verification and mathematical boundary

The companion VERIFY.py was actually run with Python Fraction and optional mpmath 100-digit checks; exact rational assertions establish the named envelope inequalities and constants, while ten rational parameter examples check the closed-form optimizer numerically. The theorem's real-domain coverage is from the analytic argument, not from sampling. Input source labels remain in T; B is a declared single-event observer, with no claim of arbitrary future-operation-safe quotient. The full ten-label decoder minimax mother bound remains [1/2,2/3]. This work supplies an endpoint-compatible certificate tool toward the open global uniqueness question at h=1/42.

Next: prove analytic endpoint continuations for G_3=F_3/[s(1-s)] and certify full-band signs or a globally signed derivative. Retain and report uncovered bands; alternatively construct a certified second crossing if found.
