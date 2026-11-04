# D25: Next Sun defect coefficient and exact scalar-map obstruction

2026-11-04 Asia/Hong_Kong. TASK_RESEARCH author-side proof / exact finite check / UNREVIEWED / NOT_ADMITTED.

Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-onhour-enterprise-math-20260923, not the separate maintenance lane. This is an author-side portable checkpoint, not a native Source checkpoint or Result. The p373 H0/B0 rank/Frobenius benchmark (#1559) remains outstanding.

## Exact objects, retained observers

For p>=5 prime and alpha in Z_p, let c_k=binom(alpha,k)binom(-1-alpha,k), B_k=binom(2k,k), h_k=B_k*c_k, C=c_1=-alpha(1+alpha). Put F(X)=sum_(k=0)^(p-1)c_k X^k and H(t)=sum_(k=0)^(p-1)h_k t^k, t=X(1-X). Sun's polynomial congruence modulo p^2 makes E_alpha(X)=(F(X)^2-H(X(1-X)))/p^2 (mod p) a well-defined polynomial. These formulas use the **original truncations**, and keep the signs, source families, degree, p-valuations, evaluation and derivative operations distinct. The existing proved [X^(p+1)]E=(2-6C)c_p and E=X^(p+1)Q, deg Q<=p-3, are reused here.

## Theorem: second nonzero-eligible coefficient

For every p>=5 prime and alpha in Z_p,

  [X^(p+2)] E_alpha(X) == c_p*(12-22C-39C^2)/8 (mod p).

Proof. The exact infinite Clausen formal identity, with the upper truncation p-1 on both sides, yields at j=p+2:

D_j=[X^j](F^2-H(X(1-X)))
   =(B_(p+2)-2)c_(p+2)
     -((p+1)B_(p+1)+2C)c_(p+1)
     +(p(p-1)B_p/2-2c_2)c_p.

Put R1=c_(p+1)/c_p=(p(p+1)+C)/(p+1)^2,
R2=c_(p+2)/c_p=R1*((p+1)(p+2)+C)/(p+2)^2, and c_2=C(C+2)/4. These are polynomial identities after clearing the p-adic unit denominators p+1,p+2; the proof does not require c_p nonzero. Further,
B_(p+1)=2B_p(2p+1)/(p+1),
B_(p+2)=4B_p(2p+1)(2p+3)/((p+1)(p+2)).
Wolstenholme gives B_p == 2 (mod p^3). Substitution and expansion modulo p^3 gives
D_j == (p^2/8)*c_p*(12-22C-39C^2) (mod p^3).
The p^2 quotient proves the claim.

For alpha=-1/3 and alpha=-1/4, the established p-adic second-digit congruence c_p==C (mod p), with C=2/9 and 3/16 respectively, gives:

                 [X^(p+1)] E    [X^(p+2)] E
 original 216         4/27            35/243
 original 2304       21/128         4995/32768

The determinant formed by these two coefficient rows is exactly
(4/27)*(4995/32768) - (21/128)*(35/243)
= -695/663552 = -(5*139)/(2^13*3^4).

**Complete exact classification.** For any p>=5 other than 5 and 139, this determinant is a p-adic unit, hence E_216 and E_2304 are not constant-scalar multiples in F_p[X]. At the exceptional p=139, direct original finite truncated convolution mod 139^3 gives first three coefficient vectors (134,138,95) for E_216 and (36,35,84) for E_2304. The scalar 135 in F_139 matches degrees p+1,p+2 but leaves 95-135*84 ==14 (mod 139) at degree p+3; equivalently the first/third minor is 52. At p=5 both polynomials equal 2 X^6 in F_5[X] because the degree bound is 8 and their degrees 6,7,8 are (2,0,0). Thus, for **every prime p>=5**, E_216 and E_2304 are scalar-proportional in F_p[X] **if and only if p=5**.

The p=139 statements are explicit finite exact integer computations; the checker contains the complete binomial algorithm. The general p>=5 formulas and determinant are algebraic proofs.

## Reconnection to D25 signed mother objective

p=139 is in the requested target class p==19 (mod24). Original exact integer-binomial sums modulo 139^3 give
A=1024013, B=1004692, M_A=1619767, M_B=881538,
W=A+6*M_A ==139, V=B+8*M_B ==139 (mod139^3).
Yet the nonzero signed third digits satisfy
(A-B)/139^2 ==1, (6*M_A-8*M_B)/139^2 ==138 (mod139).
Their sum vanishes. This witness shows a valid weighted cancellation even when no scalar polynomial transport exists. It discriminates the scalar shortcut from the still-open evaluation-plus-derivative / signed Green/WZ route; it does not assert a universal W==V theorem.

Observer/BRC reuse: the exact carrier is the source-labeled signed degree/valuation histogram; the intended future maps are differentiation, Frobenius evaluation, weighted summation and Green transport. Plain positive BRC mass would erase signs, so no such quotient is taken. The scalar-proportionality test is a rigorous failure of a specific fiber compression; higher-order observer structures remain available. No native X6 experiment is claimed.

## Executed checks and continuation

Independent direct-truncation Python standard-library checker: all 166 primes 5<=p<=1000, both families, first two coefficients, 664 comparisons, 0 failures. p=139 third coefficient and the full original weighted sums checked additionally. No floating-point approximation. Keep the previous Sun p^2 square, cubic defect, derivative-order lemma and first-boundary proof as completed evidence. The next unfinished D25 scientific unit is a source-labeled **evaluation-plus-derivative signed third-digit transport**, tested first at 139 then at 13,19,373; direct Green/WZ boundary transport remains a parallel option. The frozen mother Delta_p-R_p==0 (mod p) remains OPEN. Separate p373 native [X]U mod139129, module rank, true semilinear Frobenius and independent replication remain NOT_EXECUTED. Research Source authority was not available on this run, so no native claim/run/Result was opened.

Citations: Z.-H. Sun, Note on super congruences modulo p^2 (2015), Theorem 2.2; classical Clausen identity and Wolstenholme congruence; preceding author notes 20261104_onhour_d25_sun_defect_leading_coefficient.md and 20261104_onhour_d25_sun_cubic_defect_frobenius_order.md.