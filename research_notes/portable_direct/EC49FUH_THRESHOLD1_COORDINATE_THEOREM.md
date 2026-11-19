# EC49FUH — Reciprocal-mass coordinate and sharp first-count minimax boundary

Date: 2026-11-20. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED. Independent portable research; no current Task CLAIM, formal Result, Driver Review or Foundation admission is asserted.

Frozen scientific parent: BRC16943 Source `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Direct mathematical predecessor: EC49FUG, immutable source `cc3b206a70f7d69fd76c164d987b2a784b94144f:research_notes/portable_direct/EC49FUG_GLOBAL_FIRST_TRANSITION_N15.md` (PR #2827). All conclusions below are about the inherited clipped-price **auxiliary conditional observation model**, not a new assertion about native X6 dynamics or a reproof of frozen Bellman optimality.

## 1. Model and new exact coordinate

Let
[
 E=rac{1048576}{18958647},quad m=rac{1469}{64},quad
 L=rac{951}{1280},quad U=rac34,quad W=U-L.
]
For (0<x<1), an unknown **common** finite nuisance parameter (ele E), and conditionally independent trials, use the inherited probabilities
[
 a=m(L+U)/2=rac{2807259}{163840},qquad
 c(x)=m(U-xW/2),
]
[
 p_e(x)=xrac{1-e c(x)}{1-e a},qquad
 q_e=rac{575(41217719e-2359296)}
            {45529434409e-2630615040},qquad
 r_e=p_e+q_e(1-p_e).
]
Under (H_-), the count (K) is (mathrm{Bin}(n,p_e)); under (H_+), it is (mathrm{Bin}(n,r_e)). Hypothesis priors are equal, randomized tests are permitted, and the same (e) is used under both hypotheses. In particular,
[
 D_{n,1}(e,x)
 =Pr_{H_+,e}(Kge1)-Pr_{H_-,e}(Kge1)
 =(1-p_e)^n[1-(1-q_e)^n].
]

Define the reciprocal-mass coordinate
[
 	heta=rac1{1-ae}in(0,	heta_E],quad
 	heta_E=rac1{1-aE},
 qquad eta=rac3{637}.
]
The following exact cancellation is the key new structural identity:
[
 a(2630615040-575cdot2359296)
       =45529434409-575cdot41217719
       =21829245984.
]
Together with (acdot2630615040-45529434409=-456083905), this yields
[
 oxed{1-p_e(x)=(1-x)(1-eta x+eta x	heta),}
]
[
 oxed{1-q_e=rac{21829245984}
                       {45529434409-456083905,	heta}.}
]
The original rational nuisance family therefore becomes an affine conditional survival factor and a positive convex reciprocal-affine residual factor. These identities are exact transformations of the **same model**; no independent sampling of nuisance parameters or clipping-origin compression is introduced.

## 2. Universal endpoint-minimum theorem for the first-count rule

**Theorem 1.** For every positive integer (n) and every real (0<x<1),
[
 oxed{inf_{ele E}D_{n,1}(e,x)
     =min{D_{n,1}(E,x),D_{n,1}(-infty,x)}.}
]
Here (-infty) denotes a limit of the original finite nuisance family, not an admitted finite parameter. In particular the first-count test (mathbf1_{{Kge1}}) has exact worst-case equal-prior risk
[
 oxed{sup_{ele E}R_{n,1}(e,x)=
 	frac12igl(1-min{D_{n,1}(E,x),D_{n,1}(-infty,x)}igr).}
]

**Proof.** Write (u(	heta)=21829245984/(45529434409-456083905	heta)). On the compact closure (0le	hetale	heta_E), denominators are positive, (0<u<1), and (u'>0, u''>0) because the numerator is positive and the denominator is positive with strictly negative slope. Moreover
[
 log D_{n,1}(	heta,x)
 =nlog(1-x)
  +nlog(1-eta x+eta x	heta)
  +log(1-u(	heta)^n).
]
The second term is strictly concave in (	heta). The function (g(u)=log(1-u^n)) on (0<u<1) is concave and strictly decreasing; (u(	heta)) is convex. Hence (gcirc u) is concave. Thus (log D_{n,1}) is strictly concave on ([0,	heta_E]). Every interior value is at least the smaller endpoint value (strictly greater when the endpoints tie). The two endpoints are (e=E) and the limit (e	o-infty). This proves the exact infimum, with no grid or asymptotic interchange. QED.

This theorem applies to the **particular first-count threshold**; it does not assert that every count threshold or every randomized test has endpoint-only worst nuisance.

## 3. Sharp n=15 algebraic onset inside the endpoint first-count region

The endpoint values simplify to
[
 u_E=1-q_E=rac{4822040484}{8132285009},quad
 u_infty=rac{21829245984}{45529434409},quad
 eta=rac{E,mW/2}{1-Ea}=rac{141024}{1653649}.
]
They satisfy
[
 D_{n,1}(E,x)=(1-x)^n(1+eta x)^n(1-u_E^n),quad
 D_{n,1}(-infty,x)=(1-x)^n(1-eta x)^n(1-u_infty^n).
]
Define the algebraic number
[
 t_n=left(rac{1-u_E^n}{1-u_infty^n}ight)^{1/n},
 quad x_n=rac{1-t_n}{eta+eta t_n}.
]
For (n=15), (0<x_{15}<1). Since the ratio
[
 rac{D_{15,1}(-infty,x)}{D_{15,1}(E,x)}
 =rac{1-u_infty^{15}}{1-u_E^{15}}
  left(rac{1-eta x}{1+eta x}ight)^{15}
]
is strictly decreasing in (x), the exact signs are
[
 x<x_{15}Rightarrow D_infty>D_E,qquad
 x=x_{15}Rightarrow D_infty=D_E,qquad
 x>x_{15}Rightarrow D_infty<D_E.
]
The exact Fraction certificate isolates the algebraic boundary without floating-point sign tests:
[
 oxed{rac{2797}{10^7}<x_{15}<rac{2798}{10^7}},
 qquad x_{15}approx0.00027974730814845366453.
]

There is a second, independent boundary for which (Kge1) is the *unique endpoint Bayes rule*. At (e=E) the count likelihood ratio is strictly increasing in (k), the (k=0) signed mass is negative, and the (k=1) signed mass is positive precisely when
[
 p_E(x)<b_{15}:=rac{q_E u_E^{14}}{1-u_E^{15}}.
]
Here (p_E(x)=(1512625x+141024x^2)/1653649) strictly increases from zero to one. Let (x_B) be the unique positive root of (p_E(x)=b_{15}). It obeys
[
 oxed{rac{2956}{10^7}<x_B<rac{2957}{10^7}},
 qquad x_Bapprox0.00029564755490901301761.
]
In particular (x_{15}<x_B). The complete endpoint-first-count region is (0<x<x_B).

**Theorem 2 (sharp classification on this entire region).** For (n=15) and (0<x<x_B):

* (0<xle x_{15}): the unique endpoint Bayes rule (mathbf1_{{Kge1}}) is also composite minimax across **all** finite (ele E), with exact value ((1-D_{15,1}(E,x))/2).
* (x_{15}<x<x_B): the same rule is uniquely endpoint Bayes but is **not** composite minimax; the actual composite minimax value is strictly greater than the endpoint Bayes risk.

**Proof.** On the first region Theorem 1 gives (D_{15,1}(e,x)ge D_{15,1}(E,x)) for all nuisance parameters. The endpoint Bayes risk is a universal lower bound for the composite game, and the first-count test attains it.

On the second region, (D_infty<D_E) and continuity supplies a sufficiently negative **finite** (e) with (D(e,x)<D(E,x)), so the unique endpoint Bayes test has larger composite risk. If a composite test attained the endpoint Bayes lower bound, it would have to equal that unique test at every binary observation (all endpoint elementary outcomes are strictly positive). The set of randomized tests on the finite binary observation space is compact, and the pointwise supremum of continuous risks is lower semicontinuous, so a minimax test exists. No such test can attain the endpoint lower bound, yielding strict inequality. QED.

Thus the earlier EC49FUG rational witness interval ([1/3500,29/100000]) lies within a **complete and sharply delimited** first-count-region phase change. It was not the entire interval.

## 4. Exact witness and verification scope

At (x=7/25000) the endpoint Bayes test is uniquely (Kge1), while the negative-infinity limiting risk exceeds its endpoint risk by
[
 rac12igl[D_{15,1}(E,7/25000)
              -D_{15,1}(-infty,7/25000)igr]
 >0
 quad(	ext{approximately }1.69823354863	imes10^{-7}).
]
The limit is only used to establish the supremum and the existence of a finite nuisance witness, not as a new member of the parameter set.

The accompanying Python standard-library `Fraction` verifier checks the reciprocal-coordinate cancellation, all positive-denominator preconditions, exact model identities across a set of rational test cases, exact rational isolation inequalities for both critical boundaries, and exact signed binomial mass inequalities at the rational witness. The universal log-concavity/endpoint theorem is proved analytically above; finite rational checks do not stand in for that proof. Author checked; no independent peer review or Lean proof. No Bellman or P000 promotion.

## 5. Next unresolved scientific frontier

The exact least-favorable **randomized** test and nuisance mixture when (x_{15}<x<x_B) remain unsolved. Theorem 1 is a sharp tool for the pure (Kge1) rule, not automatically for a randomized blend of thresholds (Kge1) and (Kge2). Analyze such mixtures with their full risk function and a genuine lower-bound saddlepoint before claiming sharp composite minimax values. Separately, classify later Bayes count-threshold regions and their first endpoint-minimax failures, retaining the shared nuisance, original clipping atom and explicit observer.
