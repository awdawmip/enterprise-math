# EC49FUL — Complete upper nine count-threshold minimax phases for 15 clipped-price observations

Date: 2026-11-20 (Asia/Shanghai). Evidence: **AUTHOR_PROVED / EXACT_FRACTION_BERNSTEIN_AND_RATIONAL_BOUNDS_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

## Scientific inputs and observer scope

Continuation of frozen BRC16943 binary clipped-price observation model, scientific pin 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab', inherited from EC49FUK immutable commit '136595d2efef0da4a17924f94c58a1982e182285', PR #2834. Prior j=2,...,6 theorems and original price model are dependencies, not reproved here. This result concerns the specified **15-trial binary count detector**, not native Heartbeat/X6 state identity or parent Bellman optimality. Latent price origins and signed/joint provenance stay at the parent layer.

Fifteen conditionally independent binary readouts share one unknown nuisance \(\varepsilon\le E=1048576/18958647\), common to both hypotheses and constant across trials, with equal hypothesis priors. Define
\[
\theta=(1-a\varepsilon)^{-1}\in(0,\theta_E],\quad a=2807259/163840,\quad \theta_E=31597745/1653649.
\]
The compactified endpoint \(\theta=0\) is the limit \(\varepsilon\to-\infty\), not a finite admissible nuisance. For normalized width \(0<x<1\), set
\[
\beta=3/637,\ \eta=141024/1653649,\quad
T(\theta,x)=(1-x)(1-\beta x+\beta x\theta),\quad
u(\theta)=\frac{C}{H+B\theta},
\]
\[
(C,H,B)=(21829245984,45529434409,-456083905),\qquad
u_I=C/H,\quad u_E=4822040484/8132285009,
\]
\[
T_I(x)=(1-x)(1-\beta x),\qquad T_E(x)=(1-x)(1+\eta x).
\]
Under H−, \(K\sim{\rm Bin}(15,1-T)\); under H+, \(K\sim{\rm Bin}(15,1-Tu)\). Define
\[
F_j(z)=\sum_{k=0}^{j-1}\binom{15}{k}(1-z)^kz^{15-k},\qquad
D_j(\theta,x)=F_j(T)-F_j(Tu).
\]
The risk of \(\phi_j(K)=\mathbf 1_{\{K\ge j\}}\) (decide H+) equals \((1-D_j)/2\).

## Theorem: all remaining upper-count phases are composite minimax

Let \(x_6\) be the inherited exact root of \(L_6(x)=1\). For integers \(j=7,\dots,14\), define \(x_j\) as the unique root in (0,1) of
\[
L_j(x)=\left(\frac{1-u_ET_E(x)}{1-T_E(x)}\right)^j u_E^{15-j}=1,
\]
and set \(x_{15}=1\). Each strict rational bracket below has denominator \(10^6\); the \(j=6\) bracket is inherited and rechecked.

| j | Strict lower numerator | Strict upper numerator |
|---|---:|---:|
| 6 | 271729 | 271731 |
| 7 | 351933 | 351935 |
| 8 | 433404 | 433407 |
| 9 | 515356 | 515360 |
| 10 | 597317 | 597321 |
| 11 | 678992 | 678996 |
| 12 | 760196 | 760200 |
| 13 | 840810 | 840814 |
| 14 | 920760 | 920764 |

**For every \(j=7,\dots,15\), every real \(x\in[x_{j-1},x_j]\) with \(x<1\), and every finite admissible common nuisance \(\varepsilon\le E\), the deterministic full-count test \(\phi_j\) is composite-minimax among all randomized tests of the complete 15-bit sequence.** Its exact error is
\[
\boxed{R_{15}^{\rm mm}(x)=\frac{1-D_j(\theta_E,x)}2
=\frac{1-F_j(T_E(x))+F_j(u_ET_E(x))}{2}.}
\]
For the displayed test its maximum error occurs at \(\varepsilon=E\), uniquely within each phase's interior. At switching widths the two neighboring threshold rules tie and both are minimax. At \(x=1\), both hypotheses yield \(K=15\) surely, so \(R_{15}^{\rm mm}(1)=1/2\). Combined with EC49FUJ/K, the deterministic threshold classification now covers the entire interval \(x_2\le x\le1\), without any further high-count nuisance randomization phase.

## Proof

### A. Endpoint Bayes lower bound

With \(p_E=1-T_E,\ r_E=1-u_ET_E\), the complete-sequence likelihood ratio for a count \(K=k\) is \(L_k=(r_E/p_E)^k u_E^{15-k}\), strictly increasing in k. For \(j\le14\), \(L_j(x)\) decreases strictly from infinity to \(u_E^{15-j}<1\) as x increases from 0 to 1, so the unique switch exists. The exact checker verifies all j=6,...,14 strict bracket signs and ordering. For \(x\in[x_{j-1},x_j]\), \(L_{j-1}\le1\le L_j\); thus \(\phi_j\) is endpoint-Bayes optimal for the *admissible* nuisance \(E\), over every randomized full-sequence test. For j=15 the same conclusion holds after x_14 because \(L_{15}>1\) on x<1. Therefore all composite tests have worst-case error at least \((1-D_j(\theta_E,x))/2\).

### B. Strict nuisance concavity and exact endpoint separation for j=7,...,12

Put \(S=Tu\). On \(0\le\theta\le\theta_E\),
\[
T'>0,\quad u'>0,\quad u''>0,\quad S'=T'u+Tu'>0,\quad S''=2T'u'+Tu''>0.
\]
For \(2\le j\le14\),
\[
F'_j(z)=15\binom{14}{j-1}z^{15-j}(1-z)^{j-1},\quad
F''_j(z)=15\binom{14}{j-1}z^{14-j}(1-z)^{j-2}(15-j-14z).
\]
Each j=7,...,12 phase lies inside the explicit rational box [lower(x_(j−1)), upper(x_j)]. The exact checker proves
\[
T\ge T_I(\operatorname{upper}(x_j))>\frac{15-j}{14}>
u_ET_E(\operatorname{lower}(x_{j-1}))\ge S.
\]
Consequently \(F''_j(T)<0<F''_j(S)\), and
\[
D''_j=F''_j(T)(T')^2-F''_j(S)(S')^2-F'_j(S)S''<0.
\]
This strict concavity makes the minimum of D over the compactified nuisance interval occur at an endpoint. Define the gap
\[
J_j(x)=D_j(0,x)-D_j(\theta_E,x).
\]
For each rational box, the companion program builds the exact degree-30 polynomial \(J_j(x)\), substitutes \(x=l+(r-l)y\), and constructs its degree-30 Bernstein coefficients \(b_{j,k}\) for \(0\le y\le1\). It verifies 186/186 strict rational inequalities
\[
\min_k b_{j,k}>c_j,\qquad
(c_7,c_8,c_9,c_{10},c_{11},c_{12})
=(18,23,29,33,37,38)/1000.
\]
Because the Bernstein basis is nonnegative and sums to one, \(J_j(x)>c_j>0\) for every real x in every target phase. Thus strict concavity gives \(D_j(\theta,x)\ge D_j(\theta_E,x)\), with strict inequality if \(\theta<\theta_E\).

### C. Direct derivative sign for j=13,...,15

Write \(t_1=T'=\beta x(1-x)\), \(Q=(1-uT)/(1-T)>1\), and \(u'_I=-CB/H^2>0\). Differentiate \(D_j\) to obtain the exact positive ratio
\[
\mathcal R_j(\theta,x)=
\frac{F'_j(S)S'}{F'_j(T)T'}
=u^{15-j}Q^{j-1}
\left[u+u'\left(\frac1{\beta x}-1+\theta\right)\right].
\]
If \(\mathcal R_j>1\), then \(D'_j=F'_j(T)T'-F'_j(S)S'<0\). For any \(\theta\in[0,\theta_E]\), x<=b, with \(u\ge u_I,\ u'\ge u'_I\), one has
\[
u+u'\left(\frac1{\beta x}-1+\theta\right)\ge
A_I(b):=u_I+u'_I(1/(\beta b)-1).
\]

For **j=13**, take \(a=760196/10^6\), \(b=840814/10^6\). The identity
\[
\partial_\theta Q=\frac{(1-u)t_1-u'T(1-T)}{(1-T)^2}
\]
and the following *exact rational inequality* establish \(\partial_\theta Q<0\) on the entire box:
\[
u'_I T_I(b)(1-T_E(a))>(1-u_I)\beta a(1-a).
\]
Indeed \(x>1/2\) implies \(t_1\le\beta a(1-a)\); also \(T\ge T_I(b)\) and \(1-T\ge1-T_E(a)\). For fixed \(\theta\), Q decreases with x because T decreases with x. Thus \(Q(\theta,x)\ge Q(\theta_E,b)\), and
\[
\mathcal R_{13}(\theta,x)\ge
u_I^2 Q(\theta_E,b)^{12}A_I(b)>1.
\]
The last lower bound is exactly rational and approximately \(1.0180786206690262\).

For **j=14**, put \(b=920764/10^6\). Since \(u\le u_E\) and \(T\ge T_I(b)\), without any derivative sign assumption on Q,
\[
Q\ge \frac{1-u_ET_I(b)}{1-T_I(b)},\quad
\mathcal R_{14}(\theta,x)\ge
u_I\left(\frac{1-u_ET_I(b)}{1-T_I(b)}\right)^{13}A_I(b)>1.
\]
The exact rational lower bound is approximately \(1.1843834830637603\).

For **j=15** and \(x\in[x_{14},1)\), \(Q\ge1\), \(u^{15-j}=1\), and
\[
\mathcal R_{15}(\theta,x)\ge A_I(1)>1
\]
with exact rational lower bound approximately \(1.4944556617848839\). Therefore \(D'_j(\theta,x)<0\) for j=13,14,15 throughout their full relevant phases; \(D_j(\theta,x)\ge D_j(\theta_E,x)\) follows.

### D. Minimax matching

Parts B and C prove \(D_j(\theta,x)\ge D_j(\theta_E,x)\) for every admissible parameter. Hence \(\phi_j\)'s worst-case risk is its endpoint E Bayes risk, matching the universal lower bound in part A. This proves the theorem.

## Reproducibility and remaining scientific questions

Companion program 'EC49FUL_COUNT_7_TO_15_VERIFY.py' uses only Python standard-library Fraction arithmetic. Local run on 2026-11-20: **PASS**, with 9 strict switch brackets, 186 Bernstein coefficient checks, twelve concavity-domain checks (two per j), and four additional exact derivative-sign inequalities for j=13,14,15. All signs are rational, not inferred by floating-point grids. Example: \(x=1/2\) lies between \(x_8\) and \(x_9\), so the minimax test is \(K\ge9\), with risk approximately \(0.19836953952241868\).

The result is **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**, with parent Bellman and joint clipped-price science inherited, not independently examined here. No formal task CLAIM, Result, Review, or change of active owner is asserted. Historical provenance: Researcher 'EM-DIRECT-8454C6', SID 'MCP-44cfc4e6f2094f96861854ebefc77e84'.

Next questions: (1) combine low-width randomization and all deterministic phases into one exact full \(x\in(0,1]\) partition, including boundary conventions; (2) classify arbitrary n and potential further finite-sample anomalies; (3) quantify how refining the detector to retain hidden price-origin or native joint provenance changes the statistical identification problem.
