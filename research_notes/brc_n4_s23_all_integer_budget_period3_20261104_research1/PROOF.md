# BRC N=4 / S23: the exact integer-budget optimum for every K

2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: PR #1765, K=4 proof at d301f2591aee747da0f911ec8a58ac23124a53f7.

## Model and theorem

Fix s=1/2, h=1/42, v=1/21, p=11/42, q=10/42. Tagged T distributions are P_T=(p,1/2,q), Q_T=(q,1/2,p); coarse B distributions are P_B=(p,1-p), Q_B=(q,1-q). T costs 3/2, B costs 1. Nonnegative integer (m,n) is feasible at integer budget K iff 3m+2n<=2K.

For A in {T,B}, f_A(t)=-ln(sum_y P_A(y)^t Q_A(y)^(1-t)). The **correct shared-exponent** mixed Chernoff information is C(m,n)=max_{0<=t<=1}[m f_T(t)+n f_B(t)].

**Theorem.** For EVERY integer K>=1, the **unique global maximizer** is
```
(m_K,n_K)=(2 floor(K/3), K mod 3).
```
Moreover every other feasible allocation (m,n) satisfies
```
C(m_K,n_K)-C(m,n)>1/6000000 .
```
Thus K divisible by 3 optimizes pure T; K=3a+1 (a>=1) uses one B, K=3a+2 (a>=1) uses two B; K=1,2 use pure B. In particular K=5 first requires two B samples.

## Complete analytic proof

Let c=C_T=max_t f_T(t)=f_T(1/2) by tagged T's reflection symmetry; b=f_B(1/2); d=C_B=max_t f_B(t); e=d-b. Exactly:
Z_T=1/2+sqrt(440)/42, Z_B=(sqrt(110)+sqrt(992))/42, c=-ln Z_T, b=-ln Z_B.

For B, the tilted success weight pi_t lies in [q,p]. Put L=ln(176/155), mu=q(1-q)L^2 and g=f'_B(1/2). Then f''_B(t)=-pi_t(1-pi_t)L^2<=-mu, where mu>1/350, while
g=-(sqrt(110)ln(11/10)+sqrt(992)ln(31/32))/(sqrt(110)+sqrt(992))
has |g|<1/120000. Global strong concavity gives
0<=e<=g^2/(2mu)<E=175/14400000000=7/576000000.

The accompanying exact rational interval verifier establishes
b>1/10000; 2b-c>1/10000; 2c-3b>1/4000000; and 1/4000000-5E=109/576000000>1/6000000.
Consequently d>=b>0, 2d-c>1/10000, and Delta=2c-3d>1/4000000-3E>2E>0. This also implies c>3d/2>d and c-d>d/2>1/20000.

For any (m,n), the linear separate-optimizer upper bound is U(m,n)=mc+nd. It is **only an upper bound**, not the mixed information. For n>=3, exchanging three B observations for two T observations keeps cost 3 and increases U by Delta>0. Therefore a linear maximizer must have n<=2. For fixed n=0,1,2, increase m to floor((2K-2n)/3) since c>0. Writing K=3a+r, the linear gaps of these residue candidates below (2a,r) are:

| r | n=0 | n=1 | n=2 |
|---|---|---|---|
| 0 | optimal | c-d | 2(c-d) |
| 1 | d | optimal | c-d |
| 2 | 2d-c | d | optimal |

Omit nonexistent entries at small K. A prior n>=3 exchange improves U by >=Delta; a nonmaximal m loses >=c. Therefore (m_K,n_K) is the unique linear maximizer and every other feasible pair trails it by at least
delta=min(Delta,c-d,2d-c,d,c)>1/4000000-3E.

Return to **one common t** for mixtures: C(m,n)<=mc+nd, while C(m_K,n_K)>=m_K f_T(1/2)+n_K f_B(1/2)=m_K c+n_K b. Because n_K<=2, this last value is >=m_K c+n_K d-2E. Hence for every rival
C(m_K,n_K)-C(m,n)>delta-2E>1/4000000-5E=109/576000000>1/6000000.
QED for all K.

## Evidence, scope and BRC reuse

VERIFY.py uses only Fraction and isqrt, with each sqrt enclosed by adjacent rationals of denominator 10^29 and logarithms by 24-term arctanh sums plus strict remainders. It checks all displayed scalar bounds and **117811 feasible competing allocations** for every K=1..100 by strict rational intervals. The all-K conclusion follows from the analytic exchange proof; the loop is finite corroboration.

T retains source-tagged observation identity; B merges erasure and minus source. This exact BRC observer distinction underlies the model. The result is a complete theorem for this fixed sampling experiment, with no claim of native X6 time evolution. The separate ten-label decoder minimax mother problem remains at its recorded open [1/2,2/3].

Native Owner/Researcher-ID/CLAIM and formal Result/review remain unverified; this is author-side material. Next research varies rational s around the efficiency crossover using the actual cost 2-s and the same shared-exponent criterion.
