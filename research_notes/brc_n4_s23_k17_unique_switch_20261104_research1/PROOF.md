# BRC N4 / S23: unique K=17 Chernoff allocation switch with a 10^-18 rational bracket

Date: 2026-11-04. Scientific input pin: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Author-side proof and exact-rational executed certificate; unreviewed / not admitted. Continues PR #1765 at `0362a3de0fe88977eb6cdc22caa4e4749985ad84` and the earlier `ROOT_PROOF.md`.

## Theorem (exact scoped result)

Put `h=1/42`, `alpha=11/21`, `beta=10/21`, `a=alpha*s`, `b=beta*s`, and `J=[1/9+10^-6,1/9+10^-5]`. For the frozen three-label T observer `P=(a,1-s,b), Q=(b,1-s,a)` and two-label B observer `P=(a,1-a), Q=(b,1-b)`, define their separate Chernoff informations `C_T(s), C_B(s)`. T costs `2-s`, B costs 1. Define `g(s)=9*C_T(s)-17*C_B(s)`.

For **every real s in J**, `-1/1300 < g'(s) < -1/2500`. Consequently g has exactly one zero `s_*` on J. Moreover,

```text
1/9 + 9805774634637/10^18 < s_* < 1/9 + 9805774634638/10^18.
```

At K=17 the unique global integer-Chernoff-optimal allocation is `(9 T,0 B)` for `s in J` below `s_*`, and `(0 T,17 B)` for `s in J` above `s_*`. At `s=s_*` precisely those two allocations tie as global optima. This establishes the uniqueness of the **continuous switch on J**, not of all possible switches outside J.

## Analytical proof

The T experiment has a symmetric optimal Chernoff exponent `t=1/2`. Put

`d = 1 - 2*sqrt(alpha*beta)`, so `C_T=-log(1-d*s)` and `C_T'=d/(1-d*s)`.

For the B experiment define `H=log(alpha/beta)>0`, `L(s)=log((1-beta*s)/(1-alpha*s))>0`, `M=H+L` and `r=L/M`. At the maximizing common exponent of B, the tilted probability of label 1 is precisely `r`: its optimality equation is `r*H+(1-r)*(-L)=0`. Therefore the exact Bernoulli Chernoff information is

`C_B(s) = r*log(r/a)+(1-r)*log((1-r)/(1-a)) = D_Bernoulli(r||a).`

Here `L'=(alpha-beta)/((1-alpha*s)*(1-beta*s))`, hence

`r'=(alpha-beta)*H / ((1-alpha*s)*(1-beta*s)*M^2)`.

Ordinary differentiation gives the exact identity

`C_B' = r'*log(r*(1-a)/(a*(1-r))) - r/s + alpha*(1-r)/(1-a)`.

Thus `g'=9*d/(1-d*s)-17*C_B'` is an elementary real analytic function on J. The executable `VERIFY.py` encloses `g'` on each of **128 closed rational subintervals partitioning J** using Fraction interval arithmetic with outward grid rounding to 10^-44, exact `isqrt` square-root bounds and a 19-term atanh logarithmic sum with rigorous geometric remainder. It proves, with rational comparisons, `-1/1300<g'<-1/2500` everywhere. Since both inequalities are strict and g is differentiable, g is strictly decreasing on J.

Independent rational interval evaluation of g proves `g(1/9+9805774/10^12)>3*10^-16` and `g(1/9+9805775/10^12)<-2*10^-16`. The intermediate value theorem plus strict monotonicity yields exactly one zero. Deterministic rational bisection using the same certified enclosures proves the stated 10^-18 open bracket; no floating-point sign decision is used.

## Global integer-allocation comparison at K=17

Set `E(s)=C_T(s)-(2-s)*C_B(s)`. B(s_lo) is a Bernoulli thinning of B(s) for `s>=s_lo`, so `C_B(s)` is nondecreasing; `C_T(s)` is increasing, and `2-s` decreases. The exact script certifies on all J the uniform inequality

`C_B(start)>1/100000; 8*[C_T(end)-(2-end)*C_B(start)] < C_B(start)/10`.

For every feasible integer allocation with `1<=m<=8`, let `n<=floor(17-(2-s)m)` and `u=17-(2-s)m-n`. Throughout J, its fractional unused budget at maximal n is `m/9+m*(s-1/9)`, strictly between 1/10 and 1; smaller n only enlarges u. Because the mixed Chernoff information uses **one common exponent**, it obeys

`C_mix(m,n)<=m*C_T+n*C_B=17*C_B+m*E-u*C_B <17*C_B`.

The script also checks `9*(2-s)<17<10*(2-s)` on J. Thus for m>=9 only `(9,0)` is feasible, while m=0 gives `(0,17)` uniquely among pure-B choices. Their information difference equals g(s), completing the classification.

## Certificate and scope

Execute `python VERIFY.py` (Python standard library only) to reproduce the exact assertions, the 128-cell derivative coverage, interval root bisection and mixed-competitor exclusion. `RUN_EVIDENCE.txt` contains one actual local execution. The proof concerns the **classical source-labelled S23 Chernoff observer model**, not an assertion about P000's native six-axis space or the open ten-label mother minimax target `[1/2,2/3]`. Source provenance remains fixed; formal native CLAIM/Result and independent mathematical review remain outstanding.

Next mathematical question: analyze parameter-induced feasibility jumps when s crosses rational cost denominators, and compare the K=17 switch classification to longer budgets without treating frozen numerical observer data as native dynamics.
