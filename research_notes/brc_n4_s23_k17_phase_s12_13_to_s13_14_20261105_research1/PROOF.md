# Exact BRC S23 K=17 auxiliary phase: 12/13 <= s <= 13/14

2026-11-05. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent immutable proof: `98fd9b94ed38a11b2d56daaeac313a3d432c7e5c` (11/12--12/13).

## Exact model

Set a=11/21, b=10/21 and K=17.
Complete observation T: P_T=(as,1-s,bs), Q_T=(bs,1-s,as).
Its two-output projection B: P_B=(as,1-as), Q_B=(bs,1-bs).
The Chernoff tilt t in [0,1] is SHARED by both observation types:

```
f_T(t,s)=-log(1-s+s*(a^t*b^(1-t)+b^t*a^(1-t)))
f_B(t,s)=-log((as)^t*(bs)^(1-t)+(1-as)^t*(1-bs)^(1-t))
F(m,n;s)=max_{0<=t<=1}(m*f_T(t,s)+n*f_B(t,s))
C_T(s)=F(1,0;s), C_B(s)=F(0,1;s), H(s)=f_B(1/2,s).
```
Feasibility: nonnegative integer counts (m,n) satisfy (2-s)m+n<=17.

## Theorem: complete integer argmax on the real continuum

There exists exactly one alpha with `92319/100000 < alpha < 92320/100000`
(numerical orientation: alpha approximately 0.923190359276).
Every maximizing feasible integer pair is as follows:

* 12/13<=s<alpha: only (13,3).
* s=alpha: precisely (13,3) and (0,17).
* alpha<s<13/14: only (0,17).
* s=13/14: only (14,2).

## Integer cost geometry

For fixed m the greatest B count is n_m(s)=17-2m+floor(ms), provided it
is nonnegative. Because C_B>0, lowering n never helps. Enumerating all
rational breakpoints k/m for 1<=m<=17 shows only 12/13 and 13/14 inside
the closed interval. On [12/13,13/14) the exact upper hull vertices are
(0,17),(13,3),(15,0). At s=13/14 the vertices are (0,17),(14,2),(15,0).
The four hull-edge differences are (13,-14),(2,-3),(14,-15),(1,-2),
all primitive integer vectors (gcd=1). F is convex and strictly increasing
in both counts, as a supremum of affine functions of (m,n). Thus global
integer maxima lie at hull vertices; primitive edges rule out hidden
integer optimizers at a two-vertex tie.

## Exact continuum analytic comparison

For all s in the interval:
```
C_T(s)=-log(1-s+2*s*sqrt(a*b))
H(s)=-log(s*sqrt(a*b)+sqrt((1-as)*(1-bs)))
L=log(a/b), J=log((1-bs)/(1-as)), rho=J/(L+J)
C_B(s)=rho*log(rho/(as))+(1-rho)*log((1-rho)/(1-as)).
```
The Bernoulli `rho` follows from the equal-KL Chernoff tilt optimum.
Bounds: 13*C_T+3*H <= F(13,3;s) <= 13*C_T+3*C_B.

For fixed tilt, the T overlap coefficient is positive affine in s;
the B coefficient is positive concave in s (weighted geometric mean).
Therefore their negative logs, then F, C_T and C_B, are convex in s.

Let G(s)=F(13,3;s)-17*C_B(s), D(s)=17*C_B(s)-15*C_T(s).
Partition [12/13,13/14] into 16 rational intervals [x,y], with
delta=1/10000. Convexity and one-sided secant inequalities yield, almost
everywhere for z in [x,y]:
```
F'(13,3;z) <= [13*C_T(y+delta)+3*C_B(y+delta)
              -13*C_T(y)-3*H(y)]/delta
C_B'(z) >= [C_B(x)-C_B(x-delta)]/delta
C_T'(z) <= [C_T(y+delta)-C_T(y)]/delta.
```
The exact executable checker certifies on EVERY one of the 16 cells:
```
17*(C_B(x)-C_B(x-delta)) >
  13*(C_T(y+delta)-C_T(y))+3*(C_B(y+delta)-H(y))
17*(C_B(x)-C_B(x-delta)) > 15*(C_T(y+delta)-C_T(y)).
```
Hence G is strictly decreasing and D strictly increasing across ALL
real s in the interval. Its six exact endpoint/boundary comparisons are:
```
13*C_T(12/13)+3*H(12/13) > 17*C_B(12/13)
17*C_B(12/13) > 15*C_T(12/13)
13*C_T(.92319)+3*H(.92319) > 17*C_B(.92319)
17*C_B(.92320) > 13*C_T(.92320)+3*C_B(.92320)
14*C_T(13/14)+2*H(13/14) > 17*C_B(13/14)
14*C_T(13/14)+2*H(13/14) > 15*C_T(13/14).
```
Continuity, strict monotonicity and these signs imply the unique
crossing with its exact tie; D>0 excludes 15T on the open phase;
the two right-endpoint inequalities establish 14T+2B unique optimum.

## Exact evidence and scope

Python stdlib `Fraction`, `isqrt`, outward sqrt grid 10^36 and atanh
log series with 34 terms and rigorous remainder
2*|v|^69/(69*(1-v^2)) for |v|<1/3. The checker asserts 32 strict
cell-wise inequalities and 6 signs, altogether 38, and enumerates
the complete cost-breakpoint/hull arithmetic. `RUN_EVIDENCE.txt`
records actual output from a locally executed equivalent, typeset
variant; published `VERIFY.py` is a transformation of the preceding
phase verifier with identical mathematical assertions and parameters.
No independent reviewer has accepted this author theorem.

This result concerns a typed T/B auxiliary information readout;
the original ten-label S23 minimax mother risk bracket [1/2,2/3]
remains separate. A bridge requires an explicit provenance-preserving
lawful encoder/decoder risk inequality, not a Chernoff exponent alone.

Next phase: 13/14<=s<=14/15; investigate the 14/15 cost jump,
and a lawful S23 risk bridge in parallel.
