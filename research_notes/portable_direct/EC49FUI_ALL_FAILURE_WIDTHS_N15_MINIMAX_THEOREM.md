# EC49FUI — Exact composite minimax saddlepoint on EVERY n=15 first-count failure width

Date: 2026-11-20. Evidence: AUTHOR_PROVED / EXACT_RATIONAL_BOUNDS_AND_SPOT_CHECKS / PARENT_DEPENDENT / NOT_REVIEWED. This extends EC49FUH / Draft PR #2829, immutable source e22d4d5683092facfe01127b5000e80bd0320ce7, without republishing its already verified theorems. Frozen BRC16943 price-science source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, with EC49FUG / PR #2827 as the preceding first-count failure certificate. This is a theorem about the inherited clipped-price binomial observer, not a new native X6 physical dynamical or Bellman-optimality theorem.

## Model and exact interval

Fix 15 conditionally independent binary observations with a **single shared** finite nuisance \(e\le E=1048576/18958647\) under both hypotheses, and equal hypothesis priors. Set \(a=2807259/163840,\ \theta=(1-ae)^{-1}\in(0,\theta_E],\ \theta_E=(1-aE)^{-1}\). The auxiliary endpoint \(\theta=0\) means the limit \(e\to-\infty\), not an admissible finite nuisance.

For real normalized width \(x\in(0,1)\), retain the exact inherited coordinates
\[
 T(\theta,x)=1-p_e(x)=(1-x)(1-\beta x+\beta x\theta),\quad
 \beta=3/637,
\]
\[
 u(\theta)=1-q_e=\frac{C}{H+B\theta},\quad
 (C,H,B)=(21829245984,45529434409,-456083905).
\]
Under \(H_-\), the count \(K\) has law \(\mathrm{Bin}(15,p)\), \(p=1-T\). Under \(H_+\), it has law \(\mathrm{Bin}(15,r)\), \(r=1-Tu\). In particular the observer measures only a count, not the uncensored latent price/clip origin; no additional native-state equivalence is asserted.

Let \(u_E=4822040484/8132285009,\ u_I=C/H,\ \eta=141024/1653649\), and define \(F_j(\theta,x)=T(\theta,x)^j[1-u(\theta)^j]\). At the endpoints:
\[
 T_E=(1-x)(1+\eta x),\qquad T_I=(1-x)(1-\beta x).
\]
EC49FUH established the unique algebraic first-count gap crossing \(x_{15}\) and endpoint-Bayes \(K=1\) crossing \(x_B\), with exact rational isolations
\[
 \frac{2797}{10^7}<x_{15}<\frac{2798}{10^7}
 <\frac{2956}{10^7}<x_B<\frac{2957}{10^7}.
\]
Throughout the **entire open interval** \(x_{15}<x<x_B\), the endpoint Bayes decision is uniquely \(H_+\) iff \(K\ge1\), yet that pure test is not composite minimax.

## Main theorem — global exact rule, risk, and least-favorable limit

For **every real width \(x\in(x_{15},x_B)\)**, define rational/algebraic endpoint gaps
\[
 A(x)=F_{15}(\theta_E,x),\qquad I(x)=F_{15}(0,x),
\]
and signed \(K=1\) masses
\[
 d_E(x)=15T_E^{14}\{u_E^{14}(1-T_Eu_E)-(1-T_E)\},
\]
\[
 d_I(x)=15T_I^{14}\{u_I^{14}(1-T_Iu_I)-(1-T_I)\}.
\]
Here \(A>I\) and \(d_E>0>d_I\). Let
\[
 \boxed{\alpha(x)=1-\frac{A(x)-I(x)}{d_E(x)-d_I(x)}},\qquad
 \boxed{\lambda_E(x)=\frac{-d_I(x)}{d_E(x)-d_I(x)}}.
\]
Then \(\frac{74}{75}<\alpha(x)<1\) and \(0<\lambda_E(x)<1\). The **sharp composite minimax count rule** is
\[
 \boxed{
 \phi_x(K)=
 \begin{cases}
 0,&K=0,\\
 \alpha(x),&K=1,\\
 1,&2\le K\le15,
 \end{cases}
 }
\]
where \(\phi_x\) is the conditional probability of deciding \(H_+\).

Its **exact minimax equal-prior error risk** for every such real width is
\[
 \boxed{
 R^{mm}_{15}(x)=
 \frac{1-D_x^*}{2},\qquad
 D_x^*=A-(1-\alpha)d_E=I-(1-\alpha)d_I
 }
\]
or, equivalently,
\[
 D_x^*=(15\alpha-14)F_{15}(0,x)+15(1-\alpha)F_{14}(0,x).
\]
A matching least-favorable **limiting** common-nuisance mixture is \(\lambda_E(x)\delta_E+(1-\lambda_E(x))\delta_{-\infty}\) in the compactified nuisance space. It is not a finite-supported prior on the original half-line. The conditional randomization probability \(\alpha(x)\) is the unique optimal **permutation-invariant count-rule** choice at \(K=1\); different allocations across distinguishable one-hit sequences with the same aggregate randomization are statistically equivalent.

## Proof 1 — exact universal bounds on alpha

All estimates here are rational inequalities, simultaneously valid for every real \(x\in(x_{15},x_B)\). Put
\[
 g(x)=(1-u_E^{15})(1+\eta x)^{15}
       -(1-u_I^{15})(1-\beta x)^{15}.
\]
As \(A-I=(1-x)^{15}g(x)\) and \(g(x_{15})=0\), it suffices to bound \(g'\). We have \(0<\eta<1/10,\ 0<\beta<1/200\), and \(x<x_B<3/10000\), so
\[
 (1+\eta x)^{14}<(1+3/100000)^{14}<101/100.
\]
Consequently
\[
 0<g'(x)
 =15[(1-u_E^{15})\eta(1+\eta x)^{14}
       +(1-u_I^{15})\beta(1-\beta x)^{14}]
 <15[(1/10)(101/100)+1/200]<2.
\]
The parent-certified rational brackets therefore imply
\[
 0<A-I<2(x_B-x_{15})
 <2\frac{2957-2797}{10^7}=\frac1{31250}<\frac1{30000}.
\]

At \(\theta=0\), \(T_I=(1-x)(1-\beta x)>(2999/3000)\), hence \(T_I^{14}>99/100\). Also \(p_I=1-T_I=x+\beta x(1-x)>x>2797/10^7\) and \(0<u_I<1/2\). Thus
\[
 -d_I=15T_I^{14}
 \{p_I-u_I^{14}(1-T_Iu_I)\}
 >
 15\frac{99}{100}
 \left(\frac{2797}{10^7}-\frac1{2^{14}}\right)
 >\frac1{400}.
\]
For \(x<x_B\) the parent endpoint likelihood-ratio argument gives \(d_E>0\). Therefore
\[
 0<\frac{A-I}{d_E-d_I}
 <\frac{1/30000}{1/400}=\frac1{75},
 \qquad
 \boxed{74/75<\alpha<1}.
\]
Both signs also imply \(0<\lambda_E<1\).

## Proof 2 — global nuisance upper bound by strict concavity

For \(j=14,15\), we prove \(F_j(\theta,x)\) strictly concave on the full auxiliary interval \([0,\theta_E]\), uniformly in \(x\in(x_{15},x_B)\). Write \(S(\theta)=T(\theta)u(\theta)\). Then \(T''=0,\ T'>0,\ S'>0,\ S''=2T'u'+Tu''>0\), and
\[
 F_j''=j(j-1)[T^{j-2}T'^2-S^{j-2}S'^2]
        -jS^{j-1}S''.
\]
The exact sufficient inequality
\[
 u^{j/2}(u'/u)>T'/T
\]
forces the bracket to be negative and hence \(F_j''<0\). It holds *uniformly* because
\[
 \frac{T'}T\le\frac{\beta x}{1-\beta x}
  <\frac1{500000},\qquad
 u\ge C/H>\frac25,\qquad
 u'/u=\frac{-B}{H+B\theta}\ge\frac{-B}H>\frac1{100},
\]
and
\[
 \frac{(2/5)^8}{100}>\frac1{500000}.
\]
Here \(j/2\le 15/2<8\) and \(0<u<1\).

Let \(D_1=F_{15}\) be the signed discrimination gap of the rule \(K\ge1\). By binomial algebra the gap of \(K\ge2\) is \(D_2=15F_{14}-14F_{15}\). Therefore the proposed randomized rule has gap
\[
 D_\alpha=\alpha D_1+(1-\alpha)D_2
          =(15\alpha-14)F_{15}+15(1-\alpha)F_{14}.
\]
Since \(74/75<\alpha<1\), both coefficients are nonnegative and the first is strictly positive. Thus \(D_\alpha\) is strictly concave in \(\theta\). By the definition of \(\alpha\), \(D_\alpha(\theta_E)=D_\alpha(0)=D_x^*\). It follows that **for every finite nuisance \(e\le E\)**,
\[
 \boxed{D_\alpha(e,x)\ge D_x^*},
\]
strictly for \(e<E\) finite. This is the global upper bound \(R_e(\phi_x)\le(1-D_x^*)/2\), not a finite-grid extrapolation.

## Proof 3 — matching composite lower bound

At \(\theta_E\) the signed count-0 mass is negative, while all counts \(k\ge1\) have positive signed mass by the exact endpoint \(K\ge1\) Bayes threshold characterization. At \(\theta=0\), count-0 mass is negative and count-1 mass \(d_I<0\). We now prove all counts \(k\ge2\) have positive signed mass there, uniformly over the entire real width interval.

Indeed \(p_I=1-T_I<1/3000,\ r_I=1-T_Iu_I>1-u_I>1/2\), and \(u_I>2/5\). The likelihood ratio at count 2 is
\[
 \frac{\Pr_+(K=2)}{\Pr_-(K=2)}
 =\left(\frac{r_I}{p_I}\right)^2u_I^{13}
 >1500^2(2/5)^{13}>1.
\]
This ratio increases strictly with \(k\), so every \(k\ge2\) has positive signed mass.

The two-point limiting nuisance mixture with weight
\[
 \lambda_E=\frac{-d_I}{d_E-d_I}
\]
has **exactly zero** mixture signed mass at \(K=1\), negative at \(K=0\), and positive for all \(K\ge2\). Therefore \(\phi_x\) is Bayes-optimal for that mixture, regardless of its coin flip at \(K=1\).

By construction, the risks of \(\phi_x\) at \(\theta_E\) and at limiting \(\theta=0\) coincide and equal \((1-D_x^*)/2\). For *any* test, the supremum risk over finite \(e\le E\) dominates the convex combination of its risk at \(E\) and its limit as \(e\to-\infty\). Hence the Bayes risk for this two-point limiting mixture is a valid lower bound for the original composite problem. It matches the upper bound. QED.

**Crucial quantifier:** the nuisance is held fixed across all 15 trials before any hypothesis testing or limiting prior mixing; mixing the Bernoulli probabilities independently per trial would be a different model.

## Verification and provenance

Accompanying pure-standard-library Python Fraction verifier: EC49FUI_ALL_FAILURE_WIDTHS_N15_MINIMAX_VERIFY.py. It checks exact rational isolating brackets for \(x_{15},x_B\), every displayed uniform coarse inequality, the endpoint signed mass criterion, and five independent rational-width saddlepoint identities, including x=29/100000. The full real-width/nuisance result is the analytic proof above; five checks are regression, not evidence of exhaustive sampling.

At x=29/100000, \(\alpha\approx0.996692573960196,\ \lambda_E\approx0.981475010572011,\ R^{mm}\approx0.002182123251814\). These are approximations to the exact rational formulas in the theorem.

No present formal Task publication / live CLAIM, Result or Review is inferred by this research file; independent mathematical review remains NOT_REVIEWED. The parent BRC16943/Bellman source and clipped-price observer are unchanged. The exact result is for the interval \(x_{15}<x<x_B\), not the full detector-width range \(0<x<1\).

Next research frontier: characterize the \(n=15\) compound minimax game for x≥x_B as the endpoint Bayes count threshold changes; determine how many least-favorable nuisance support points, and which randomized count levels, are required. Also independently audit the source of the inherited clipping law and its latent residual, without changing the proven conditional observer statement.
