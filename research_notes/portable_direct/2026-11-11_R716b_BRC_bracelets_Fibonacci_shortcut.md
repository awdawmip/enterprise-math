# R716b — Fibonacci law for unrooted odd BRC microphase histories

Date: 2026-11-11, Asia/Shanghai.
Scope: same explicit five-phase candidate event scheduler as R712–R716; odd m>=5; A=m+3; rooted edge-indexed phase-pair words versus unrooted orientation-free bracelets.
Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Inputs: R715 exact profile count (research commit ccc019123731b3ef59497c7f064151b0e3c00c7f) and R716 free dihedral-action theorem (research PR #2074).
Author-side derivation, not a formally admitted mathematical result.

## Theorem

Let Q_m be the number of D_m-orbits (bracelets) of all legal phase-pair cyclic words of odd length m with total area A=m+3; let U_m be the corresponding rooted oriented word count. With F_0=0, F_1=1 and F_{n+2}=F_{n+1}+F_n, for every odd m>=5,

Q_m = 4 F_{m-3},     U_m = 8m F_{m-3}.

The generating series and recurrence are

sum_{k>=0} Q_{2k+5} x^k = 4/(1-3x+x^2),
Q_{m+4} = 3 Q_{m+2} - Q_m (odd m>=5), Q_5=4,Q_7=12.

Thus, unlike the rooted generating function of R713 (with a squared denominator), the bracelet generating function has a first-power quadratic denominator; removing the root frame also lowers the scalar recurrence order.

## Exact proof

Put k=(m-5)/2. R715's exhaustive residual-vector classification gives

U_{2k+5}=8(2k+5)*sum_{r+s+t=k} binom(r+s,s)*binom(r+t,t).

R716 proves the dihedral action on these words is free, hence Q_{2k+5}=U_{2k+5}/[2(2k+5)]. For the formal power series S(x)=sum_{k>=0}Q_{2k+5}x^k/4, rearrange coefficientwise (each coefficient is a finite sum):

S(x)
 =sum_{r,s,t>=0} binom(r+s,s)binom(r+t,t)x^{r+s+t}
 =sum_{r>=0} x^r (sum_{s>=0}binom(r+s,s)x^s)^2
 =sum_{r>=0} x^r/(1-x)^{2r+2}
 =1/((1-x)^2-x)
 =1/(1-3x+x^2).

The coefficients b_k=[x^k]S(x) obey b_0=1, b_1=3 and b_k=3b_{k-1}-b_{k-2}. The even-index Fibonacci subsequence F_{2k+2} obeys the same recurrence and initial values. Therefore b_k=F_{2k+2}, giving Q_m=4F_{m-3}; multiplying by 2m recovers U_m. QED.

## Joint optimum as an exponentially thin exact subfamily

R715/R716 give the number J_m of bracelet words attaining both minimum area and minimum peak:

J_m=4 for m=4n+1 (n>=1);
J_m=4*(2+n^2) for m=4n+3 (n>=1).

Consequently the exact joint-optimal fraction among area-optimal bracelets is

J_m/Q_m = 1/F_{m-3}             (m=4n+1),
J_m/Q_m = (n^2+2)/F_{m-3}       (m=4n+3).

Both subsequences have exponential root rate

lim_{m->infty, m odd} (J_m/Q_m)^(1/m) = 1/phi,
where phi=(1+sqrt(5))/2.

This is a counting ratio on explicitly defined finite discrete histories, not a probability claim about a physical random scheduler.

## Exact algorithm and validation

Compute Q_m=4*F_{m-3} by the standard integer Fibonacci doubling identities F_{2n}=F_n(2F_{n+1}-F_n), F_{2n+1}=F_n^2+F_{n+1}^2. O(log m) big-integer multiplication/addition operations suffice (the bit cost depends on the integer multiplication algorithm). No trigonometric, amplitude or BRC-Shor arithmetic is involved.

The attached Python verifier uses integer fast doubling for 501 odd ring lengths m=5,...,1005 and independently evaluates R715's binomial-triple profile sum for the first 49 lengths m=5,...,101. It checks the derived second-order recurrence and returns R716B_FIBONACCI_BRACELET_EXACT_PASS.

BRC resolution: COMPOSE_APPLIED. The source-labelled event population remains intact; Q_m counts a specified dihedral reindexing quotient and does not imply that its elements are indistinguishable under the future V39 observer. Native Link/Port admission and observer-equivariance are the next discriminating checks.
