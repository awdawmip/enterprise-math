# BRC N=4 S23: cubic rational Chernoff optimizer and global 12th-order information certificate

Date 2026-11-04. AUTHOR_ANALYTIC_PROOF; EXECUTED_RATIONAL_AND_HIGH_PRECISION_AUDIT; UNREVIEWED; NOT_ADMITTED.

## Model and source

Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Continues the author-side source-label Chernoff analysis at PR #1765 head a968a47283af437d288bd0b3be1ea9ca48814286, specifically brc_n4_s23_chernoff_monotone_optimizer_band_cert_20261104_research1/PROOF.md. This is an independent two-state source-tagged BRC observation experiment; source tags are retained in T and intentionally projected to one event by B.

For real 0<s<=1 and 0<v=2h<=1/21, the two full-source laws are T_+=(s(1+v)/2,1-s,s(1-v)/2) and T_-=(s(1-v)/2,1-s,s(1+v)/2). Scalar observations B_± are Bernoulli(s(1±v)/2). Assigned sampling costs: c_T=2-s and c_B=1. Put k=s/(2-s), alpha=atanh(v), gamma=atanh(kv), X=s sqrt(1-v^2)/2 and Y=(2-s)sqrt(1-k^2 v^2)/2. The Chernoff coefficient is Z_s(delta)=X exp(alpha delta)+Y exp(-gamma delta), -1<=delta<=1; C_B=-log min Z_s. The preceding result proved the unique optimizer delta_*=[psi(kv)-psi(v)]/[alpha+gamma], where psi(x)=log(sqrt(1-x^2)atanh(x)/x), psi(0)=0, and 0<=delta_*<1/125.

## Theorem (uniform real-parameter, twelfth-order proxy)

Define the rational cubic exponent

d_3(s,v)=(1-k)v/6+(1-k)(9k^2+10k+9)v^3/180.                 (1)

For every real s,v in the above range:

(A) 0<=d_3<1/125; d_3(1,v)=0; d_3 decreases strictly as s increases for each fixed v>0, and extends to s=0 with d_3(0,v)=v/6+v^3/20.

(B) |delta_*-d_3|<=(347687/297000)v^5<(3/2)v^5.          (2)

(C) Writing C_3=-log Z_s(d_3), E_3=(9/8)v^12/(1-v^2)^2,

0<=C_B-C_3<=E_3<=1/6508893842035200 < 10^-15.           (3)

(D) With C_T=-log(1-s+s sqrt(1-v^2)), F=C_T/(2-s)-C_B and F_3=C_T/(2-s)-C_3,

F_3-E_3<=F<=F_3.                                            (4)

An outward rational interval certificate F_3<0 proves that scalar B has the larger optimized Chernoff information per assigned cost; F_3>E_3 proves the converse. Unlike the preceding linear rational proxy with an O(v^8) information bound, d_3 has an explicit uniform O(v^12) certificate.

## Proof

1. Positive-series tails. Write u(x)=atanh(x)/x-1 and 0<=x<=v<=1/21, and R=1-v^2>=440/441. By the positive atanh series,

0<=u<=x^2/[3(1-x^2)],
0<=u-x^2/3-x^4/5<=x^6/[7(1-x^2)],
0<=u-x^2/3<=x^4/[5(1-x^2)].

Also |log(1+u)-u+u^2/2|<=u^3/3, and, with a=x^2/3,
|u^2-a^2|/2<=(u-a)(u+a)/2<=x^6/[15(1-x^2)^2].
The log(1-x^2) series gives
|(1/2)log(1-x^2)+x^2/2+x^4/4|<=x^6/[6(1-x^2)].
Combining these exact tail estimates,

psi(x)=-x^2/6-19x^4/180+e(x),
|e(x)|<=Cpsi(v)x^6,
Cpsi(v)=1/(6R)+1/(7R)+1/(15R^2)+1/(81R^3)
<=33190017/85184000<1/2.                                (5)

The last number is an exact Fraction at R=440/441; no floating rounding is used in the bound.

2. Cancel the quadratic and quartic orders. Let N=psi(kv)-psi(v), D=atanh(v)+atanh(kv). From (5),

N=(1-k^2)v^2/6+19(1-k^4)v^4/180+r_N, |r_N|<=v^6.

By the positive atanh series,

D=(1+k)v+(1+k^3)v^3/3+r_D,
0<=r_D<=(1+k^5)v^5/[5(1-v^2)].

Write d_3=d_1 v+d_{3c}v^3, where
d_1=(1-k)/6, d_{3c}=(1-k)(9k^2+10k+9)/180.
The exact identities
(1+k)d_1=(1-k^2)/6,
(1+k)d_{3c}+(1+k^3)d_1/3=19(1-k^4)/180
make D*d_3-N start at order v^6. Since
0<=d_1<=1/6, 0<=d_{3c}<=7/45, D>=(1+k)v>=v,

|D*d_3-N|/v^6
<=1+(7/45)(2/3)+(1/6+(7/45)(1/441))*2/[5(440/441)]
=347687/297000<3/2.
Divide by D to obtain (2) using the exact predecessor optimizer N/D.

3. Location and monotonicity. The expression (1) is nonnegative; its k derivative is
partial_k d_3=-v/6+v^3(1-2k-27k^2)/180<=-v/6+v^3/180<0.
Because k=s/(2-s) increases strictly, d_3 decreases in s. Its largest endpoint value for 0<v<=1/21 is v/6+v^3/20<1/125, proving (A).

4. Convert exponent error to information error. For L(delta)=log Z_s(delta), the tilted mixture identity yields
L''=w(1-w)(alpha+gamma)^2<=(alpha+gamma)^2/4,
where w=X exp(alpha delta)/Z_s(delta). By exact interior optimality, L'(delta_*)=0. Taylor's integral bound and atanh(x)<=x/(1-x^2) give

0<=L(d_3)-L(delta_*)
<=(alpha+gamma)^2(d_3-delta_*)^2/8
<=[2v/(1-v^2)]^2[(3/2)v^5]^2/8
=(9/8)v^12/(1-v^2)^2=E_3.

The RHS increases in v; exactly at v=1/21 it is 1/6508893842035200. As C_B=-L(delta_*), C_3=-L(d_3), this proves (3). Subtraction in the unchanged T/B cost comparison proves (4). QED.

## Additional asymptotic coefficient and verification

For fixed k in (0,1], the exact optimized exponent has the convergent local expansion

delta_*=d_3+(1-k)(319k^4+357k^3+340k^2+357k+319)v^5/11340+O_k(v^7).

This fifth-order term can guide further polynomial surrogates; the quantitative inequality (2) is the certified all-parameter statement.

VERIFY.py was executed with Python fractions.Fraction; it checks the exact two cancellation identities, the tail constants and E_3. A separate 90-digit mpmath audit checks 30 declared rational s,v inputs and observes the true optimized information gap below E_3. RUN_EVIDENCE.txt is actual stdout. The analytic proof above establishes the universal quantifier; numerical samples audit code only. This is an author-side checkpoint, not a native CLAIM/Result or independent mathematical admission.

## Next mathematical unit

For fixed v=1/21, use (4) with directed rational intervals and endpoint normalization at s=0,1 to certify signs over disjoint full s-bands. The earlier locally unique crossing interval was (0.10243902443, 0.10243902445); global uniqueness at that finite v remains an open target. The original unrestricted ten-label decoder minimax interval [1/2,2/3] remains unchanged.
