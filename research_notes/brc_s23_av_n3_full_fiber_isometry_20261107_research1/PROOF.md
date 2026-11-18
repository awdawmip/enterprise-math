# S23 n=3: exact full-27 fixed-fiber total-variation geometry

Date: 2026-11-07. Author-side exact theorem, independent review pending.
Frozen scientific source: `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Prior frontier: Draft PR #1777@87f4ba417ba88cc440e52206254c47fd1b443f71, three-class exact minimax; full model interval `[5211/21952,5211/21952+49/100000000000]`.
Scope: S23 conditional AV auxiliary model; three conditionally iid outputs governed by one lawful real pair `a,c in [1/2,7/8]`.

## Exact setup
Let `z=(1-a)c`, `b=(1-a)(1-c)` and `a=1-z-b`. An ordered ternary word `w` with counts `(n0,n1,n2)`, total 3, has probability `a^n0*z^n1*b^n2`. The compressed three-Bernoulli observation law depends only on `z`. On its fiber, `1/16<=z<=7/16` and
```
a_min=max(1/2,1-2*z), a_max=min(7/8,1-8*z/7);
b_min=1-z-a_max,      b_max=1-z-a_min.
```
All lawful fiber points satisfy `a>=1/2`, `0<b<=1/4`.

## Theorem 1: all 27 output words have a common sign partition
For any two lawful points with the same z and `b<=b'`,
```
TV(Q_{z,b},Q_{z,b'})=(1-b)^3-(1-b')^3.
```
This holds for the **full ordered 27-outcome distribution**. Proof: as `b` varies with `z` fixed, `a=1-z-b`. For every word containing a 2 (`n2>=1`), derivative of its probability is
```
z^n1*a^(n0-1)*b^(n2-1)*(n2*a-n0*b).
```
Here `n0<=2`, and `n2*a-n0*b >= a-2*b>=0`. Thus all words containing a 2 increase. All words without a 2 but containing a 0 decrease because their derivative is `-n0*a^(n0-1)*z^n1<=0`. Word 111 stays constant. Therefore every output difference has its positive sign in the same event `A={at least one 2}`. Summing those differences gives `Q_{z,b'}(A)-Q_{z,b}(A)`; since `Q_{z,b}(A)=1-(1-b)^3`, the formula follows exactly for all real lawful parameters. In particular `b -> Q_{z,b}` is TV-isometric to the scalar `s(b)=1-(1-b)^3`.

The four-class observer `(A1=exactly one 2,A2=at least two 2,B=no 2 but some 0,C=111)` has output probabilities
```
(3*b*(1-b)^2, 3*b^2-2*b^3, (1-b)^3-z^3, z^3).
```
The first two coordinates increase (derivatives `3(1-b)(1-3b)` and `6b(1-b)`, positive for `0<b<=1/4`), B decreases, C stays fixed. Thus the **four-class and three-class observers preserve exactly the full 27-outcome TV for each pair on a common z fiber**.

## Theorem 2: exact per-fiber Chebyshev radius
For a *known z*, allow a separate output law M_z; define `r(z)=min_M max_{b in [b_min,b_max]} TV(Q_{z,b},M)`. Then
```
r(z)=D(z)/2,  D(z)=(1-b_min)^3-(1-b_max)^3.
```
A minimax center is the average of the two **full ordered** endpoint laws. Every intermediate coordinate lies between the endpoint coordinates by Theorem 1, so its distance from that midpoint is <= half the endpoint diameter. The TV triangle inequality on the two endpoints gives the matching lower bound. The identical argument works for the four- and three-class observers.

The diameter is an exact piecewise polynomial:
```
D(z)=(7/8+z)^3-(1-z)^3,    1/16 <= z <= 7/64;
D(z)=(1-z/7)^3-(1-z)^3,    7/64 <= z <= 1/4;
D(z)=(1-z/7)^3-(1/2+z)^3,  1/4  <= z <= 7/16.
```
It increases strictly on the first two intervals: the respective derivatives are `3[(7/8+z)^2+(1-z)^2]>0`, and `3[(1-z)^2-(1-z/7)^2/7]>0`; the second bracket is >= `9/16-1/7=47/112>0`. It decreases strictly on the third interval, whose derivative is `-3[(1-z/7)^2/7+(1/2+z)^2]<0`. Therefore the unique maximizer is `z=1/4`. At this fiber endpoints are `(a,c,b)=(1/2,1/2,1/4)` and `(5/7,7/8,1/28)`; its diameter equals `37/64-2269/21952=5211/10976`. Hence:
```
max_z r(z) = 5211/21952.
```

## Implication for the research route
This exact lower bound is **optimal among all single-fiber adversaries even with 27 ordered outputs**; splitting A into A1/A2 does not change any same-fiber pairwise TV or its Chebyshev radius. An improvement of the global *parameter-independent* minimax lower bound beyond `5211/21952` must use at least two different compressed probabilities z (or new model restrictions) to force a common stochastic decoder to reconcile different fibers. The previously verified full model interval remains `[5211/21952, 5211/21952+49/100000000000]`, as this theorem is deliberately fiber-local.

The n=3 monotonicity is special: for n=4 the output word 0002 has fixed-z derivative `a^2*(a-3*b)=-1/16` at lawful `(a,z,b)=(1/2,1/4,1/4)`; it violates the claimed n=3 sign structure.

## Verification and scope
`VERIFY.py` is a standard-library Fraction checker for exact endpoint masses, full 27-word normalization and sign alignment, four-class masses, midpoint radius and the n=4 derivative counterexample on nine rational fibers. The universal theorem is established by the derivative and piecewise inequalities above; the finite checks are regression evidence. Local development corrected an invalid interior interpolation test point before the successful run; only the corrected execution is cited. See `RUN_EVIDENCE.txt`.

The output histogram/quotient is typed to the declared marginal total-variation observer. It does not identify erased BRC branch/provenance or native X6 state as equal, change P000, or prove transfer to the six-source ten-label S23 mother model. This author-side proof creates no formal task CLAIM, result acceptance or independent review. Gateway status in this run: `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`; Owner still unconfirmed.
