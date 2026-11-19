# EC49FUD — Sharp two-trial composite minimax law at every top-bin resolution

Date: 2026-11-20. Evidence: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.
Line: EC49FUC-S continuation; immutable scientific input: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (BRC16943 parent). No independent native Bellman verification or new claim/review is asserted. External price-prior readout only; the original native X6/P000 model and its provenance are preserved.

## Model and objective

The one-sided clipping-interface experiment (EC49FUB/FUC) has `m=1469/64`, `L=951/1280`, `U=3/4`, `W=9/1280`, `E=1048576/18958647` and real `e<=E`. Its continuous distribution `nu_e` has affine density proportional to `1-e*m*z` on `[L,U]`; the two hypotheses are
`H-: nu_e`, `H+: (1-q_e)nu_e+q_e delta_U`, where
`q_e=575*(41217719*e-2359296)/(45529434409*e-2630615040)`.
The uncertain **same** `e` governs both hypotheses and both i.i.d. samples; the two one-sided *weak-limit* distributions define the experiment, not a conditional law at the singleton boundary.

The observer reports only `Y=1{Z>=U-delta}` at a known width `delta=xW`, `0<=x<=1`; there are two independent reports `Y1,Y2`. Denote `K=Y1+Y2`. Put

`p_e(x)=P-(Y=1)=x*(1-e*m*(U-xW/2))/(1-e*m*(L+U)/2)`,
`r_e(x)=P+(Y=1)=p_e(x)+q_e*(1-p_e(x))`,
`V_e=r_e-p_e`, and `S_e=p_e+r_e`.

## Theorem (exact all-width two-sample minimax and threshold phase)

For `0<=x<=1`, among all possibly randomized decisions based on `K`, with equal hypothesis priors, one test minimizes the worst-case risk for **all real common parameters `e<=E`**:
- If `S_E(x)<1`, decide `H+` when `K>=1`.
- If `S_E(x)>1`, decide `H+` only when `K=2`.
- At equality, either rule (or any randomization on `K=1`) is minimax.
- At `x=1`, both observed laws are identical and the minimax error is `1/2`.

The exact risk is

```
D1_E(x)=(1-p_E(x))^2-(1-r_E(x))^2,
D2_E(x)=r_E(x)^2-p_E(x)^2,
R2*(x)= [1-max{D1_E(x),D2_E(x)}]/2,
p_E(x)=x*(141024*x+1512625)/1653649,
r_E(x)=(411225984*x^2+4410814500*x+3310244525)/8132285009.
```

There is exactly one transition `x*=0.3925698880989402...` in `(0,1)`, namely the positive root of

`1826870798324832*x^2+19595036598849125*x-7973962424326116=0`.

For `0<=x<x*` use `K>=1`; for `x*<x<1` use `K=2`. **The adversarial least-favorable parameter is always `e=E`**, despite the fact that the Bayes-optimal threshold for some *other* individual `e` can differ.

At `x=1/4` this specializes to the exact fraction
```
p_E=1547881/6614596,
r_E=4438649774/8132285009,
R2*(1/4)=1792706378557916871129377139144871/
          5787111167767792608343351627560992
        = 0.30977569405313504...
```
compared with the one-trial minimax error `37019714302905989/107583559782782728 = 0.3441019648...` from EC49FUC-S.

## Proof

For any fixed `e`, `0<=p_e<r_e<1` for `x<1`, with the limiting edge `p_e=0` at `x=0`. Under `H-` the count `K` has Binomial`(2,p_e)` law, and under `H+` it has Binomial`(2,r_e)` law. A likelihood-ratio comparison assigns `K=0` to minus and `K=2` to plus. At `K=1`, plus is favored exactly when

`r_e(1-r_e)>=p_e(1-p_e)` iff `p_e+r_e<=1`.

The two candidate probability advantages are `D1_e=(1-p_e)^2-(1-r_e)^2=(1-p_e)^2*q_e*(2-q_e)` and `D2_e=r_e^2-p_e^2=V_e*S_e`. Their difference is `D1_e-D2_e=2V_e*(1-S_e)`. Thus the optimal rule at `e=E` is the theorem's selected threshold.

We now prove the **same endpoint-optimal rule has its worst risk at E**. Introduce the exact affine-price means
```
a=mu_A=2807259/163840,
b=mu_B=41217719/2359296,
t=mu_T=45529434409/2630615040,
c=mu_C=a-m*W*x/2.
```
Here `b>t>a>=c>=mL>0`, `q'_e<0`, and `p'_e<=0`; hence `r'_e=(1-q_e)p'_e+q'_e(1-p_e)<0` for `x<1`, so `S'_e<0`.

First, `V_e=q_e(1-p_e)` is strictly decreasing for `x<1`. In fact, with `f_e(u)=u/(1-e*u)`,
```
d(log V_e)/de= -[f_e(b)-f_e(t)]+[f_e(a)-f_e(c)].
```
For `e<=E`, pairwise positive denominators and `b>t>a>=c` yield
```
((1-e*b)*(1-e*t))/((1-e*a)*(1-e*c)) <= b*t/(a*c) <= b*t/(a*mL).
```
Also `a-c<=mW/2`. The resulting ratio of the positive to negative bracketed differences is at most the exact fraction
`9383097168495465355/18295894360889780544<1`. Therefore `V'_e<0`. Because `S_e>0` and `S'_e<0`, `D2_e=V_e*S_e` is strictly decreasing in `e` for all `x<1`.

For `D1`, let `u=1-p_e=(1-x)(1-e*c)/(1-e*a)`. Direct differentiation gives
```
(1/2)*d(log D1_e)/de
 = [f_e(a)-f_e(c)]
   - [(1-q_e)/(2-q_e)]*[f_e(b)-f_e(t)].
```
The first-to-second difference ratio without the `(1-q)/(2-q)` factor is bounded by
```
((a-c)/(b-t))*((1-e*b)*(1-e*t))/((1-e*a)*(1-e*c))
 <= ((a-c)/(b-t))*b*t/(a*c).
```
This bound increases with `x`. For all `0<=x<=1/2` it is at most
`9383097168495465355/36678362354402067936`.
Since `q_e` decreases with `e` and `q_{-infinity}=23700188425/45529434409`,
```
(1-q_e)/(2-q_e) >=
(1-q_{-infinity})/(2-q_{-infinity})
=21829245984/67358680393
>9383097168495465355/36678362354402067936.
```
Consequently `D1'_e<0` whenever `0<=x<=1/2`, `x<1` (the `x=0` case follows from `q'_e<0`).

Now `S_E(x)` is strictly increasing on `[0,1]` with `S_E(0)=q_E<1`, `S_E(1)=2` and
`S_E(1/2)=31456437095054991/26895889945695682>1`.
Therefore the `E`-optimal `K>=1` region lies in `x<1/2`, where `D1'_e<0`; its `K=2` region enjoys `D2'_e<0` for every `x<1`.

For either chosen rule, the fixed-e equal-prior risk is `(1-Dj_e)/2`, maximized over admissible `e` at `E`. Conversely the simple endpoint subproblem `e=E` lower-bounds the minimax risk of every test. The rule optimal at `E` attains this bound for all nuisance parameters, establishing a saddle point and the theorem. At `x=1` both observations are constant. QED.

## Verification and scope

Accompanying `EC49FUD_TWO_TRIAL_BIN_VERIFY.py` checks all displayed rational identities, comparison certificates, endpoint threshold, the quarter-bin exact risk, and non-proof finite rational regressions. The proof uses the full analytic parameter half-line and all real widths; finite checks are regression only. The resulting all-width theorem strengthens the EC49FUC-S one-trial result and solves the specific two-i.i.d.-trial composite experiment, **not** the arbitrary-n or sequential adaptive-detector problem.

The readout `Y` erases continuous-versus-clipped source identity inside the upper bin; the retained carrier for this observer consists of `(A,B,C,q,nu,port U,epsilon,delta)` plus the source of the Bernoulli observation. Sufficiency is certified only for this declared two-trial hypothesis test, not future native six-axis Cell operations. Mathematical status remains AUTHOR_PROVED / PARENT_DEPENDENT / NOT_REVIEWED.

**Next question:** determine whether at `n>=3` the endpoint `E` remains least favorable for every detector width; if not, find the smallest `n` and an exact rational witness, then classify least-favorable parameter mixtures and threshold randomization without losing clipped-port provenance.
