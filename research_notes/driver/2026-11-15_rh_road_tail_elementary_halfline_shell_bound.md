# RH composite-road: elementary non-asymptotic tail bound in the range 1/2<a<1

Status: DRIVER SCOPED MATHEMATICAL DERIVATION / exact unconditional bound only on the declared a-interval; NOT RH, NOT a -> 0, NOT formal Result admission, NOT TASK closure.
Date: 2026-11-15.
Original direction/source: EM-FREE-C4A91D composite-road handoff `research_handoffs/COMPOSITE_ROAD_RH_20260909/START_HERE.md`; current immutable task `RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD`; frozen original EM source `9d7c4c6eafc5479a6795a128fc0288fc893bed3c`. This is an independent Driver derivation and source relation, not authorship transfer or Researcher CLAIM.

## Theorem (elementary full-road shell bound; explicitly outside the difficult a -> 0 range)

Let `1/2<a<1`, `N` be a positive integer, and define the full-integer arithmetic road
```
R_a(n) = product_(p|n) (1-p^-a) = sum_(d|n) mu(d)/d^a,
S_a(N) = sum_(n=1)^N R_a(n),
c_a = 1/zeta(1+a) = sum_(d>=1) mu(d)/d^(1+a),
B_(a,N) = S_a(N)-1-c_a*(N+1/2).
```
The Dirichlet series for `c_a` is *absolutely* convergent for all `a>0`. Set
```
C(a) = 1/(1-a) + 1/a + 3/2.
```
Then, for every integer `N>=1`,
```
|B_(a,N)| <= C(a)*N^(1-a).
```
For every integer `M>=2`, the nonnegative escaping tail obeys
```
sum_(N>=M) B_(a,N)^2/N^2
     <= C(a)^2 * (M-1)^(1-2*a)/(2*a-1).
```
For every dyadic integer `L>=1`, the shell `L<=N<2L` obeys
```
sum_(L<=N<2L) B_(a,N)^2/N^2
     <= C(a)^2 * L^(1-2*a).
```
The proof makes no nontrivial claim about the limit `a->0`, and none of the above estimates uses a zero-free region, a version of RH, an unproved conditional Nyman gain or a phase-averaging replacement.

## Proof with explicit constants

Möbius expansion and finite divisor exchange give, identically,
```
S_a(N) = sum_(d<=N) mu(d)*d^-a * floor(N/d).
```
Subtract `c_a*N` to get the **exact identity**
```
S_a(N)-c_a*N
 = sum_(d<=N) mu(d)*d^-a *(floor(N/d)-N/d)
   -N*sum_(d>N) mu(d)*d^(-a-1).
```
With `0<a<1`, `|mu(d)|<=1` and `|floor(x)-x|<1`,
```
|S_a(N)-c_a*N|
 <= sum_(d<=N) d^-a + N*sum_(d>N) d^(-a-1)
 <= N^(1-a)/(1-a) + N^(1-a)/a.
```
The two last inequalities are elementary decreasing-function integral tests, including `N=1`. Since `0<c_a<1` (because `zeta(1+a)>1`) and `N^(1-a)>=1`,
```
|B_(a,N)| <= N^(1-a)*(1/(1-a)+1/a)+1+c_a/2
           <= C(a)*N^(1-a).
```
Squaring and dividing by `N^2` gives `B_(a,N)^2/N^2<=C(a)^2 N^(-2a)`.
For `2a>1` and `M>=2`, monotonicity and the integral comparison yield
```
sum_(N>=M) N^(-2a) <= integral_(M-1)^infinity x^(-2a) dx
                     = (M-1)^(1-2a)/(2a-1).
```
For `L<=N<2L` there are exactly `L` terms, each at most `L^-2a`; this gives the shell claim. Every constant and quantifier is explicit. QED.

## Boundary and relevance

1. This establishes an unconditional full-integer tail bound only for `1/2<a<1`, where the exponent `1-2a` is negative. It can serve as a far-from-zero regression benchmark for a proposed stronger proof and validates the dyadic shell bookkeeping in a simple regime.
2. The **absolute-value arithmetic method** ceases to yield a summable shell majorant at `a<=1/2`: its shell upper bound is constant at `a=1/2`, and increases like `L^(1-2a)` below `1/2`. This is a limitation of the displayed *majorant*, not a counterexample to the true arithmetic energy, not a lower bound, and not proof that the target fails.
3. The original hard objective asks for `D_a=O(a)` as `a->0+`, with an `a`-dependent escape scale `M(a)`. Our bound neither reaches this regime nor produces such an estimate. Any extension requires an actual arithmetic cancellation mechanism (or another genuinely stronger route) rather than silently substituting this crude absolute majorant.
4. The frozen tail task lists predecessor audit/kernel dependencies. This note does not declare them discharged, and the original historical proof/contributor records and any current owner claim remain intact.
