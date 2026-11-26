# PREFIX-1103 - Quantitative sparsity of exact fallback scales by integer determinants

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_COMPUTATION / NOT_REVIEWED. Independent continuation of R6, RA-0ABD84561C86E53067DB0322, EM-DIRECT-780BBE / TASK_RESEARCH. Original registration receipt r6-20261123-2358-session-start-own-v1 read SUCCEEDED. Previous owner read r6-20261126-1252-owner-read-v1 read SUCCEEDED with empty LEASED filter; fresh r6-20261126-1354-owner-read-v1 last read RUNNING. No new CLAIM, Task, Result or Review. No shared owner rights inferred.

Frozen input unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Use the original exact radial BRC observer, retaining the full native signed/phase/ordered carrier. The following arithmetic concerns only its integer edge, not a new physical model or alternate propagator.

Immutable parents:
- 4b000fd990a72817573fa4bb2c0a09c2dc8ded70:research_notes/portable_direct/2026-11-26_r6_prefix1102_sparse_integer_edge.md
- 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md
- f0476c7795f31809302dae513504a06d1e9a9e4c:research_notes/portable_direct/2026-11-26_r6_prefix1101_adaptive_precision.md

## 1. Quantitative counting theorem

Inherit 1102: real edge k_*(m)=rho*m+c+d/m+O(m^-2), 9<d<10; when the S^-3 normalized sign oracle is undecided, dist(k_*(m),Z)=O(m^-2). Thus for every exceptional scale m>=m0 an integer j_m satisfies
|j_m-(rho*m+c+d/m)| <= C/m^2
for a common C>=0 (sum of the two inherited remainder constants). These constants are not yet effective numerically. No assumption on rho's irrationality is required. Let E be the set of such exceptional scales, or any subset of the set satisfying this inequality.

Theorem: #E intersect [1,N] = O(sqrt(N)); in fact o(sqrt(N)) for every fixed rho,c,d,C under the stated hypotheses. In the rational rho case the exceptional set is finite. For a block [M,2M), M>=m0 and M>C, partition into four half-open intervals of length M/4. In each subinterval all lattice pairs (m,j_m) are collinear. This is an exact integer-observer constraint, not a numerical fit.

Proof. Write e_i=j_i-(rho*i+c+d/i). For three distinct indices a<b<t in the subinterval, the integer determinant
T=(b-a)(j_t-j_a)-(t-a)(j_b-j_a)
has exact reciprocal contribution
d*(b-a)*(t-a)*(t-b)/(a*b*t).
The linear and constant terms cancel exactly. The error is
(b-a)e_t-(t-a)e_b+(t-b)e_a,
of absolute value <=2C(t-a)/M^2. Since t-a<=M/4, |T|<=10/64+C/(2M)<1, so T=0. Every triple is collinear. If there are at least two points, the common line has rational slope p/q in lowest terms, q>=1; all horizontal differences are divisible by q.

Let a,t be the extreme indices of a nonempty subinterval with at least two points. For each intermediate b, collinearity and linear interpolation give
d*(b-a)*(t-b)/(a*b*t) <= 2C/M^2.
Indeed, the reciprocal chord at b minus 1/b is exactly (b-a)*(t-b)/(a*b*t); the interpolation of errors minus the middle error is bounded by 2C/M^2. Thus (b-a)*(t-b)<=16CM/d. Every index is within R=sqrt(16CM/d) of one extreme. Combining the two endpoint intervals with the congruence mod q gives at most 2+2R/q points, including the two extremes. For zero or one point use the same upper bound with q=1. In particular the dyadic block count is at most 8+8sqrt(16CM/d); summing dyadic blocks proves O(sqrt(N)), since the geometric sum of square roots is O(sqrt(N)). The additive O(log N) term is harmless. The case C=0 is included.

For any pair a<t on the same line,
p/q=rho-d/(a*t)+(e_t-e_a)/(t-a).
Hence |rho-p/q|<=(d+2C)/M^2. If rho is irrational, for every fixed Q the finitely many rational slopes with q<=Q near rho are separated from rho by a positive distance; eventually every line with at least two points has q>Q. The dyadic count is then <=8+8R/Q for sufficiently large M. Summing and dividing by sqrt(N), the fixed initial portion vanishes; taking Q arbitrarily large proves o(sqrt(N)). If rho is rational, the finitely many classes of rho*m+c mod 1 either have positive fixed distance from Z, or are exactly integral before the d/m shift; since d>0, the latter have distance d/m for large m and cannot satisfy C/m^2. Thus E is finite, also giving o(sqrt(N)). This establishes a quantitative strengthening of 1102 without knowing which rationality case actually holds.

## 2. Use the existing exact separation certificate

1102 gives H=15250 and Delta=1752007270743434/46240091623245387169, with dist(h*rho,Z)>=Delta for 1<=h<=H. For a line with q<=H, the pair formula above gives
Delta<=|q*rho-p|<= (H*d+2C)/M^2,
using t-a>=q. Therefore when M^2>(10H+2C)/Delta, each nonsingleton line has q>=15251. The dyadic count tightens to
#(E intersect [M,2M)) <= 8+8sqrt(16CM/d)/15251.
This is a finite-threshold formula in the inherited C,m0; their numeric values are not asserted. It uses the original certified rational enclosure, not an approximate value of rho.

If an additional Diophantine estimate |rho-p/q|>=kappa/q^mu holds for all such rational approximants (kappa>0), q>=(kappa/(d+2C))^(1/mu)*M^(2/mu). The same proof then gives dyadic counts O(1+M^(1/2-2/mu)), hence O(log N) total for mu<=4, and O(N^(1/2-2/mu)) for mu>4. This is explicitly conditional; no such estimate for the actual rho is proved here.

The result bounds the NUMBER of potentially expensive exact fallback calls over 1..N. The cost per fallback still needs separate control. No uniform exact sign bound, finite startup constant, or full mother objective B_fix,odd(32) is claimed. The previously certified 18 row endpoints are unchanged.

## 3. Local sharpness illustration (synthetic, not actual BRC data)

The square-root local count cannot be improved uniformly using only bounded d,C and arbitrary slope/intercept at each M. For each M take d=10, C=1, rho=21+d/M^2, c=-2d/M. The integer line j=21m then satisfies the exact identity
rho*m+c+d/m-21m = d*(m-M)^2/(M^2*m).
For m=M+h in [M,5M/4], this line meets the C/m^2 tolerance exactly when d*h^2*(M+h)<=C*M^2. This is monotone for h>=0 and has Theta(sqrt(M)) solutions. Parameters vary with M; it is not a lower bound for a single fixed rho,c or for the frozen Stage46 observer.

Actual exact checks: 5,984 triples of 1<=a<b<t<=34 verified both determinant and interpolation identities. Synthetic tangent-line qualifying counts at M=10^4,10^6,10^8,10^10: 32,317,3163,31623. The 15,250-step prior certificate was independently recomputed; same minimum at h=5445. All decisions used Python Fraction/integer arithmetic. No full BRC sign oracle was rerun.

Reproduction code (executed):
```python
from fractions import Fraction as F
from itertools import combinations
checks=0
for a,b,t in combinations(range(1,35),3):
    assert (b-a)*(F(1,t)-F(1,a))-(t-a)*(F(1,b)-F(1,a))==F((b-a)*(t-a)*(t-b),a*b*t)
    assert ((t-b)*F(1,a)+(b-a)*F(1,t))/(t-a)-F(1,b)==F((b-a)*(t-b),a*b*t)
    checks+=1
assert checks==5984
for M,expected in zip((10**4,10**6,10**8,10**10),(32,317,3163,31623)):
    d=10; C=1; rho=21+F(d,M*M); c=-F(2*d,M)
    def inside(h): return d*h*h*(M+h)<=C*M*M
    lo,hi=0,M//4+1
    while hi-lo>1:
        h=(lo+hi)//2
        if inside(h):lo=h
        else:hi=h
    assert inside(lo) and not inside(lo+1) and lo+1==expected
    for h in (0,lo,lo+1):
        m=M+h
        assert rho*m+c+F(d,m)-21*m==F(d*h*h,M*M*m)
        assert (abs(rho*m+c+F(d,m)-21*m)<=F(C,m*m))==inside(h)
bl=F(6800006737,5368709120)**2/36
bu=F(3400003369,2684354560)**2/36
lo,hi=1/bu-1,1/bl-1
H=15250
best=min((min(lo*h-(lo*h).__floor__(),(hi*h).__ceil__()-hi*h),h) for h in range(1,H+1))
assert all((lo*h).__ceil__()>hi*h for h in range(1,H+1))
assert best==(F(1752007270743434,46240091623245387169),5445)
```

Next: make C and m0 effective from the certified density derivatives, exact centered moments and complement bounds; alternatively implement the adaptive two-candidate oracle and derive effective slope rational separation at increasing precision. Study the actual exact zero case and c2=0 independently. No shared result promotion or independent review.
