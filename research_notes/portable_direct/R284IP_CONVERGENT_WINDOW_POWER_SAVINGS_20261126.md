# R284IP — Convergent-window power savings for critical exception counts
2026-11-26. Author proof, NOT_REVIEWED. Directed continuation of own R284 frontier; no shared Task claimed or modified. Original own registration r1-20261124-0256-r284gd-session-v1 recovered SUCCEEDED by native own-session recovery, Researcher-ID EM-DIRECT-0C386E, Activity RA-B82240E8488EF5A1DA5186C4; no runs. Fresh LEASED inventory r1-20261126-1604-owner-inventory last observed RUNNING. Current account canonical entry snapshot dc9803677d14b4684b828740bbda0b6f00dd21c3; project normative read main and Source P000 V5 foundation package, ACTIVE worldview retained. This work concerns the external arithmetic observer of the binary-tag safe-word total-count model, not native spatial or physical attribution.

Frozen science:
- IO @b6d9d4c99b9fcba85c5fca2e9eb83fe763d276cf:research_notes/portable_direct/R284IO_CRITICAL_TRANSCENDENCE_E_FUNCTIONS_20261126.md (irrationality of A and certified rational enclosure).
- IJ @75426bd0581d1826bfde31ac82cb5a632f53cc51:research_notes/portable_direct/R284IJ_THIRD_ORDER_CRITICAL_PROFILE_SHARP_EXCEPTION_SCALE_20261126.md (uniform strict sign bracket).
- IK @edf8d2a631c536cc4f7e9f4c94ed3fa77306c3bd:research_notes/portable_direct/R284IK_CRITICAL_EXCEPTION_EQUIDISTRIBUTION_20261126.md (lattice transfer).
- Earlier IM and IN general logarithmic discrepancy and obstruction remain distinct from the favorable-window result here. The actual minimum still relies on ID author-level global monotonicity, pending independent review.

## Theorem 1: uniform interval discrepancy at a denominator window
Let P(n)=A n^2+B n+C with real A,B,C, and let a/r be reduced, r>=4, |A-a/r|<=1/r^2. For every epsilon>0, every integer starting position v, every 0<=m<=r and every circular interval J (any endpoint convention),
| #{v<n<=v+m : {P(n)} in J} - m |J| | <= C_epsilon r^(1/2+epsilon).
The constant is uniform in A,B,C,a,r,v,m,J subject to these hypotheses. More generally, the same discrepancy for an interval of m arbitrary length is <= C_epsilon (m/r+1)r^(1/2+epsilon) by partition into contiguous blocks of length at most r. In particular any irrational A has unbounded denominator windows with normalized discrepancy O_epsilon(r^(-1/2+epsilon)) at m=r. No joint Diophantine assumption is needed for these windows.

Proof. Write e(x)=exp(2 pi i x), S_h=sum_{v<n<=v+m} e(hP(n)), f_m(k)=min(m,1/(2||2Ak||)), interpreting the second entry as infinity at zero. Exact pair difference (retaining the common product coordinate k=h d and all its multiplicities) and the geometric sum bound give
|S_h|^2 <= m+2 sum_{1<=d<m} f_m(hd).
Indeed P(n+d)-P(n)=2Ad n+Ad^2+Bd; the remaining phase is of modulus one, and each branch has m-d terms. This is an upper bound for the absolute-square observer, not a claim of cancellation equivalence for the complete phase carrier.

Spacing lemma: any block of <=floor(r/4) consecutive k has pairwise circular distance >=1/(2r) between {2Ak}. For 1<=ell<=r/4, r does not divide 2a ell (the first positive zero is r/gcd(2,r)>=r/2), so ||2a ell/r||>=1/r. Subtract 2ell/r^2<=1/(2r). By ordering distances to 0, each annulus j/(2r)<=||2Ak||<(j+1)/(2r) contains O(1) points (at most two on each side, including possible boundaries). Summing the reciprocal harmonic tail gives for one block sum f_m(k)<=C(m+r log(2r)). Therefore for K>=1 and m<=r,
sum_{k<=K} f_m(k) <= C(1+K/r)r log(2r).
Constants absorb r=4..7.

Put H=floor(sqrt(r)). For any dyadic U<=H, sum over U<=h<2U, h<=H, of |S_h|^2/h is at most
C m + (2/U) sum_{k<=2Um} tau(k) f_m(k).
Here tau(k) is the ordinary divisor count, bounding the number of allowed (h,d) with hd=k. This is exactly the shared product fiber, before absolute-square aggregation; independent frequency worst cases are avoided. For every delta>0, tau(k)<=C_delta k^delta: for p sufficiently large (j+1)<=p^(delta*j) for all j>=1, and for the finite remaining primes the sup of (j+1)p^(-delta*j) is finite. Since k<=2r^(3/2), the dyadic block bound is
C_delta r^(3delta/2)(m+r/U) log(2r).
Summing dyadic U yields sum_{h<=H}|S_h|^2/h <= C_delta r^(1+3delta/2) log^2(2r). Weighted Cauchy-Schwarz and sum 1/h<=1+log H then give
sum_{h<=H}|S_h|/h <= C_delta r^(1/2+3delta/4) log^(3/2)(2r).
Use the ordinary Erdős–Turán inequality for interval counts, with additive error O(m/(H+1)+sum |S_h|/h). Choose delta sufficiently small relative to epsilon and absorb logarithms. Endpoint inclusion follows by taking monotone limits of arcs. This proves the theorem uniformly in starting position, B and C, since the geometric bound did not depend on them. Classical external input: Erdős–Turán inequality, see Martin and Sitar, Mathematika 57 (2011), 1–29, DOI https://doi.org/10.1112/S0025579310001580 (publisher abstract checked; the classical fixed-interval version is sufficient, not their moving-target theorem), and https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Tur%C3%A1n_inequality for the exact standard inequality. No claim of novelty for classical discrepancy theory.

## Theorem 2: shrinking targets with an arbitrary denominator choice
For fixed real target t and fixed H0>0, count positive n<=M satisfying ||P(n)-t||<=H0/n. Split into dyadic blocks of n. On [2^j,2^(j+1)), the target is contained in a fixed arc of length min(1,2H0/2^j), with expected count O_H0(1). Apply theorem 1 after cutting each dyadic block into subblocks of length <=r. The total number of subblocks is O(M/r+log(2M)). Thus the count is
O_{epsilon,H0}(log(2M)+(M/r+log(2M))r^(1/2+epsilon)).
In particular at M=r it is O_epsilon,H0(r^(1/2+epsilon)) after absorbing log with a smaller epsilon in Theorem 1. The same bound holds for any fixed finite union of such moving arcs. This is uniform across every prefix of length <=r, not just the full denominator endpoint, which is essential for summing shrinking targets.

## Theorem 3: R284 exception power savings on an unbounded subsequence
Use s=s0, C0 and Z=Z0 from IJ, W=2Z/s, Q_n=((n-C0)/s)^2 with A=1/s^2. By IO, A is irrational (indeed transcendental). Let r run through denominators of its continued-fraction convergents, and X_r=floor Q_r for sufficiently large r. Then X_r~r^2/s^2. Under the frozen IJ expansion and ID global monotonicity, for every epsilon>0,
N_2(X_r)=2Z sqrt(X_r)+O_epsilon(X_r^(1/4+epsilon)),
N_3(X_r)=O_epsilon(X_r^(1/4+epsilon)).
Here N_2 counts actual failures of the two-term ceil rule; N_3 counts possible failures of the three-term rule including equality ambiguity, so actual failures are bounded by it.

Proof. IJ gives a uniform strict sign bracket of width H/q around T(q)=s sqrt(q)+C0+Z/sqrt(q). Put t(q)=s sqrt(q)+C0. For a large-n two-term exception q, t(q)<=n=ceil(t(q)) and n<=T(q)+H/q; conversely t(q)<=n and T(q)>n+H/q imply failure. As in IK, first obtain Q_n-q=O(1). Multiply n-t(q)=s(Q_n-q)/(sqrt(Q_n)+sqrt(q)) by sqrt(q). For bounded Q_n-q, the ratio sqrt(q)/(sqrt(Q_n)+sqrt(q))=1/2+O(1/q). Thus actual two-term failures in each band sandwich the integer points in [Q_n-W+K/n,Q_n] and [Q_n-W-K/n,Q_n] with one fixed K for all large n (enlarge K to make strict boundary comparisons harmless). Their difference from the ideal count G_W(Q_n)=#([Q_n-W,Q_n] intersect Z) is bounded by a fixed multiple of the indicator ||Q_n-W||<=K/n. This follows since only the lower endpoint moves, the interval has length O(1/n), and for large n it contains at most one integer. The upper endpoint, including equality, is retained. Similarly the three-term possible errors, by IJ/IK, lie in [Q_n-W-K/n,Q_n-W+K/n] intersect Z, giving the same shrinking-target bound. Successive bands are disjoint eventually, and at X_r the relevant index cutoff is r+O(1) with at most O(1) boundary points. Write W=17+beta, 0<beta<1. The ideal count is 17+1_{[0,beta]}({Q_n}), including the left and right endpoints; its integral is W. By theorem 1 at m=r the sum of ideal counts is Wr+O_epsilon(r^(1/2+epsilon)). By theorem 2 the entire moving-boundary correction is O_epsilon(r^(1/2+epsilon)), even though the target width varies with n. Finally Wr=2Z sqrt(X_r)+O(1), and translate epsilon exponents. Finite initial bands contribute O(1). This proves the subsequence results. For arbitrary X with M=s sqrt(X)+O(1), the same argument gives a valid error/upper bound O_epsilon((M/r+log(2M)) r^(1/2+epsilon)+log(2M)) for any convergent denominator r>=4. It can be combined by taking the smaller of this estimate and IM's all-X logarithmic estimate. The uniform power law for all X remains open; denominator gaps have not been bounded.

## Executed exact checks
From IO certified interval A in (1.06702880390241057864214614650799,1.06702880390241057864214614650800), rational interval continued fractions gave 29 common partial quotients (including integer part), all 29 approximation boxes checked against 1/r^2. Last certified convergent 3982670069243563/3732485997264432; prior large partial quotient 254 gives denominator 10979634443 after 43074094. Finite spacing inequality verified for every coprime 1<=a<r, 4<=r<=100, 1<=ell<=floor(r/4): 49,508 exact rational assertions. These are checks of denominator and spacing resources, not enumeration of actual K or N_2,N_3. Unbounded claims use the proof above. Reproduction (executed with Python Fraction; no floating-point signs):
```python
from fractions import Fraction as F
from math import gcd
Alo=F('1.06702880390241057864214614650799')
Ahi=F('1.06702880390241057864214614650800')
lo,hi=Alo,Ahi
p0,p1,q0,q1=0,1,1,0
out=[]
while lo//1==hi//1:
    c=lo//1
    p0,p1=p1,c*p1+p0
    q0,q1=q1,c*q1+q0
    out.append((c,p1,q1))
    if lo==c or hi==c: break
    lo,hi=1/(hi-c),1/(lo-c)
assert len(out)==29
assert out[-1]==(1,3982670069243563,3732485997264432)
for c,p,r in out:
    assert gcd(p,r)==1
    assert max(abs(Alo-F(p,r)),abs(Ahi-F(p,r))) < F(1,r*r)
checks=0
for r in range(4,101):
    for a in range(1,r):
        if gcd(a,r)!=1: continue
        for d in range(1,r//4+1):
            k=(2*a*d)%r
            assert F(min(k,r-k),r)-F(2*d,r*r)>=F(1,2*r)
            checks+=1
assert checks==49508
print(out, checks)
```
CF denominators in order: 1,14,15,179,373,552,9757,20066,29823,49889,428935,478824,4259527,38814567,43074094,10979634443,65920880752,76900515195,1065627578287,1142528093482,2208155671769,3350683765251,8909523202271,65717346181148,74626869383419,140344215564567,1197380593899955,2535105403364477,3732485997264432.

## Next
Use IO's nondegenerate rational differential system and IL's joint separation to study whether large convergent gaps for A force a compensating B separation on the intermediate windows. The new result proves genuine power savings on infinitely many scales without an unproved irrationality exponent, but does not settle all-X power savings or the finite irrationality measure of A. Extract explicit IJ remainder and explicit discrepancy constants for a certified finite sparse compensation algorithm. Preserve ID independent review pending; no formal Result/Working Truth admission claimed.
