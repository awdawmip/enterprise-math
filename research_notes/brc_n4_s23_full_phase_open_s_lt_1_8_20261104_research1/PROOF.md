# BRC N=4 / S23: complete K=17 parameter phase diagram for 0<s<1/8

Date: 2026-11-04. Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Author-side analytic proof and exact rational computation; UNREVIEWED / NOT_ADMITTED. Continues PR #1765@d3cb424ea59b57d53ff71577e17a39c95822858a.

## Exact theorem

Put alpha=11/21, beta=10/21, and let 0<s<1/8. T is the source-labelled three-outcome pair P=(alpha*s,1-s,beta*s), Q=(beta*s,1-s,alpha*s), with cost 2-s. B is the two-outcome pair P=(alpha*s,1-alpha*s), Q=(beta*s,1-beta*s), cost 1. For m,n>=0 integer and m*(2-s)+n<=17, C_mix(m,n;s) is the Chernoff information of the product experiment evaluated at one common optimizing exponent. Set CT=C_mix(1,0;s), CB=C_mix(0,1;s), and g(s)=9*CT(s)-17*CB(s).

There is exactly one real s* in (1/9+10^-6,1/9+10^-5) with g(s*)=0, and

    1/9+9805774634637/10^18 < s* < 1/9+9805774634638/10^18.

The unique global optimizer for every real 0<s<1/8 is (m,n)=(0,17) for s<1/9; (9,0) for 1/9<=s<s*; and (0,17) for s*<s<1/8. At s=s*, precisely (9,0) and (0,17) tie. The left-hand switch at s=1/9 is an integer-feasibility jump; s* is a unique continuous Chernoff-value crossing.

## 1. Exact two-B dominance

For 0<s<1 set U=s*sqrt(alpha*beta)>0, V=sqrt((1-alpha*s)*(1-beta*s))>0, q=U+V. The B Bhattacharyya coefficient is q<1 strictly by Cauchy-Schwarz, since alpha!=beta. The symmetry optimizer for T is t=1/2 and its coefficient is 1-s+2U. Because alpha+beta=1,

    q^2=1-s+2U*q,
    (1-s+2U)-q^2=2U*(1-q)>0.

CB>=-log(q), while CT=-log(1-s+2U). Consequently CT<-log(q^2)<=2CB, strictly for every 0<s<1. This proves a universal dominance statement for the frozen T/B observer pair.

## 2. Integer feasibility and global comparison

For 1<=m<=8 and s<1/8, 0<m*s<1, so n<=floor(17-m*(2-s))=17-2m. Since the product Chernoff information maximizes the sum with a common exponent,

    C_mix(m,n;s) <= m CT(s)+n CB(s)
                 <= 17 CB(s)+m*(CT(s)-2CB(s)) < 17 CB(s).

Pure B configurations have unique optimum n=17 because CB>0. For m>=10, the T cost exceeds 10*(2-1/8)>17, so no such configuration is feasible. Nine T observations become feasible exactly when s>=1/9, and for 1/9<=s<1/8 the remaining budget is 9s-1<1, forcing n=0. The only two global candidates are therefore (0,17) and, when s>=1/9, (9,0). Their information gap is g(s).

## 3. Exact rational sign and root certificate

Let d=1-2sqrt(alpha*beta); CT=-log(1-d*s). Set H=log(alpha/beta), L=log((1-beta*s)/(1-alpha*s)), M=H+L, r=L/M. The maximizing Bernoulli tilt has success frequency r, giving CB=D_Bernoulli(r||alpha*s). Direct differentiation yields

    r'=(alpha-beta)*H/((1-alpha*s)*(1-beta*s)*M^2)
    CB'=r'*log(r*(1-alpha*s)/(alpha*s*(1-r))) - r/s + alpha*(1-r)/(1-alpha*s)
    g'=9*d/(1-d*s)-17*CB'.

The attached standalone VERIFY.py evaluates all signs with Fraction, isqrt and rigorously bounded atanh logarithms (19 terms, analytic tail), outward rounded on the 10^-44 grid. All asserted inequalities are rational.

(A) On [1/9,1/9+10^-6], 10 adjacent rational cells certify 9*CT(left)-17*CB(right)>0. Both informations are nondecreasing: CT directly, CB because lowering s is a parameter-independent Bernoulli thinning of the higher-s observation.

(B) On J=[1/9+10^-6,1/9+10^-5], 128 adjacent rational cells certify -1/1300<g'<-1/2500. The endpoint signs are opposite, and a second exact endpoint check certifies the 10^-18 open root bracket. Thus precisely one zero lies in J.

(C) On [1/9+10^-5,1/8], exact evaluation certifies CT'(s)<1/500, while CB is nondecreasing. For each closed segment [a,b], g(s)<=g(a)+9*(s-a)/500. Start with certified g(a)<0 at a=1/9+10^-5 and take b=min(a+25*(-upper(g(a))),1/8). Every segment satisfies upper(g(a))+9*(b-a)/500<0. 743 such segments exactly cover the remaining interval, yielding g<0 throughout.

Steps 1-3 establish the theorem for every real 0<s<1/8. At s=1/8 the feasible integer lattice changes (8 T plus 2 B becomes possible), so the next problem begins there. The underlying ten-label S23 minimax mother target remains the recorded open [1/2,2/3]; the present Chernoff observer theorem is kept in its own scope. Formal task CLAIM, independent review, and Result admission require their distinct native authority.