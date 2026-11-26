# R284IM - Common resonance frequency lattice and improved logarithmic discrepancy
2026-11-26. Author proof, NOT_REVIEWED. Continuation of the existing direct-research R284 line, no new shared Task or protected owner mutation. Same auxiliary binary-tag safe-word total-count observer as IL, not a native physical attribution. P000 V5, joint relation and ACTIVE worldview retained. Account entry blobs checked at main@6fd1cd7501eea091c7a3a29343a1deb156b1f670. Original own registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, recovery confirms not closed and no runs. Owner inventory r1-20261126-1300-owner-read RUNNING at latest observation before publication; no claim inferred.

Frozen scientific inputs:
- IL: 0ba4281d63293680694a2bb4843b732fd2cf819f:research_notes/portable_direct/R284IL_QUANTITATIVE_JOINT_DIOPHANTINE_SEPARATION_20261126.md (joint separation and true-K exception accounting, including the standard Fourier estimates).
- IJ: 75426bd0581d1826bfde31ac82cb5a632f53cc51:research_notes/portable_direct/R284IJ_THIRD_ORDER_CRITICAL_PROFILE_SHARP_EXCEPTION_SCALE_20261126.md (third-order sign band, author-level ID monotonicity dependency).

## Main result (general joint-resonance theorem)

Let A,B,C be fixed real numbers and suppose for every positive integer T,
max(||TA||,||TB||) >= exp(-K T log(T+2))
for some K>0. Write Q_n=A n^2+B n+C and D_M for interval discrepancy of its first M fractional parts. For L=c log M/log log M with sufficiently small fixed c>0, there is a constant C1 such that
D_M = O(L^(-1/2) log(2L) exp(C1 sqrt(log(2L)))).
In particular D_M=O_epsilon(L^(-1/2+epsilon)) for every epsilon>0, improving IL's exponent 1/3 without a stronger Diophantine hypothesis.

For the R284 critical constants A=1/s0^2, B=-2C0/s0^2, C=C0^2/s0^2, IL supplies the hypothesis. Thus, with L_X=log X/log log X, and conditional on the fixed author-level IJ/ID dependencies,
N(X)=2Z0 sqrt(X)+O_epsilon(sqrt(X) L_X^(-1/2+epsilon)),
N_3(X)=O_epsilon(sqrt(X) L_X^(-1/2+epsilon)).
Here N counts actual failures of the two-term ceil rule and N_3 counts three-term failures or candidate sign-ambiguous budgets. The latter stronger candidate bound retains all near-integer residuals. No true-K finite comparison is rerun or new numerical uniform remainder constant asserted.

## 1. Common quadratic denominator across Fourier frequencies

Let e(x)=exp(2 pi i x), H=floor L, and S_h=sum_{n=1}^M e(h A n^2+h B n) for 1<=h<=H. The constant C only rotates the sums. Choose c so that K L log(L+2)<=log M/8 for all sufficiently large M.

Case I. If ||r A||>=M^(-1/2) for every integer 1<=r<=2H^2, then every shift correlation for h,k<=H has size O(M^(1/2)), by the geometric-sum bound for ratio e(2hk A). The van der Corput differencing inequality with H shifts gives |S_h|^2/M^2=O(1/H+M^(-1/2)). Erdős-Turán (ET) therefore gives D_M=O(log(2L)/sqrt(L)).

Case II. Otherwise choose one r0<=2H^2 with ||r0 A||<M^(-1/2). Reduce the nearest rational a0/r0 to a/r with gcd(a,r)=1. Then r<=2H^2 and A=a/r+delta with |delta|<M^(-1/2)/r. Use this SAME rational for every frequency. This common denominator preserves the relationship between harmonics which the separate IL differencing bounds did not exploit.

If |delta|>=M^(-3/2), split n into r residue classes. The rational quadratic part is constant modulo one on a class. For n=b+rj, the phase h delta (b+rj)^2+h B(b+rj) has second derivative of absolute size 2h|delta|r^2 in j. The standard second derivative estimate used in IL, summed across classes, yields
|S_h|/M = O(r sqrt(h|delta|)+1/(M sqrt(h|delta|))+r/M)
          = O(L^(3/2) M^(-1/4)).
This is uniform in h<=H and smaller than any fixed negative power of L. We can therefore restrict to |delta|<M^(-3/2).

## 2. The common linear resonance lattice

Set eta=M^(-1/4). Call h<=H resonant when ||hrB||<=eta, and write b_h for the nearest integer to hrB. For nonresonant h, split into the same r residue classes: the derivative in j of the remaining phase is h r B+2h delta r n. Its drift away from hrB is at most 2H r M^(-1/2)=o(eta). Thus throughout each progression the derivative lies in one unit interval with distance >=eta/2 from its endpoints; it is monotone. The first derivative estimate used in IL gives |S_h|/M=O(r M^(-3/4)).

If the resonant set is empty this finishes Case II. Otherwise all rational numbers b_h/h on the resonant set are IDENTICAL: for resonant h,k,
|k b_h - h b_k| <= (h+k) eta <= 2H eta < 1.
The left side is an integer, hence zero. Write the common reduced rational v/j (j>=1). All resonant h are multiples of j, and ||jrB||<=eta (take any such h and multiply its approximation error by j/h). Furthermore ||jrA||<=jr |delta|. If jr<=L, the latter is at most L M^(-3/2), and the former at most M^(-1/4). But joint separation requires their maximum >=M^(-1/8). Contradiction. Thus
jr > L.
No independence of the two coefficients has been assumed: the retained joint denominator is the paid separation resource. This is a scope-specific exact compression of the frequency information for the ET observer, not a replacement of the joint count state.

## 3. Gauss transport on the resonant frequencies

For resonant h write hB=b_h/r+eps_h with |eps_h|<=eta/r. Split the original summation into full consecutive blocks of length r plus one incomplete block. The rational phase e((h a n^2+b_h n)/r) is r-periodic. In a block the slow phase h delta n^2+eps_h n changes by at most 2H |delta| M r+eta (up to a harmless endpoint bound). By |e(x)-e(y)|<=2 pi |x-y|, freeze the slow phase at the block's initial n and pay this variation. The normalized result is
|S_h|/M <= |G(h a,b_h;r)|/r+O(H r M^(-1/2)+eta+r/M),
where G(c,b;r)=sum_{n mod r} e((c n^2+b n)/r).

The Gauss bound is elementary and includes even/composite denominators. Squaring the absolute value, put the difference of the two indices equal to k mod r; the sum over the other index is zero unless r divides 2c k, in which case its modulus is r. Thus |G(c,b;r)|^2<=r gcd(2c,r). Since gcd(a,r)=1,
|G(h a,b_h;r)|/r <= sqrt(2 gcd(h,r)/r).
In particular the composite denominator, its gcd with every harmonic and the actual signed phase are retained through the cancellation step. No positive-mass substitution for the signed sum is made.

## 4. Aggregate the correlated harmonic contributions

Because resonant h are contained in j times the positive integers, and gcd(jk,r)<=gcd(j,r) gcd(k,r),
sum_{resonant h<=H} sqrt(2 gcd(h,r)/r)/h
 <= sqrt(2 gcd(j,r))/(j sqrt(r)) sum_{k<=H/j} sqrt(gcd(k,r))/k
 <= sqrt(2/(jr)) (1+log H) sum_{d|r} d^(-1/2).
Indeed sqrt(gcd(k,r))<=sum_{d|r, d|k} sqrt(d), then interchange the finite sums and use the harmonic bound. The first prefactor is <=sqrt(2/L) by jr>L.

For completeness, the divisor sum is <= product_{p|r}(1-p^(-1/2))^(-1). Its logarithm is O(sum_{p|r} p^(-1/2)): the constants are uniform for p>=2. If the distinct primes are ordered p_i, then p_i>=i+1, and their number is at most log_2 r. Therefore this logarithm is O(sqrt(log(2r))). Since r<=2H^2, the divisor sum is at most exp(O(sqrt(log(2L)))). This proof uses only elementary bounds on distinct primes and does not require the prime number theorem.

All paid phase-variation and nonresonant errors, when summed with ET weights 1/h, are polynomially small in M times polylog factors. The ET truncation term 1/H is O(L^-1). We obtain the main discrepancy estimate. Since log(2L) exp(O(sqrt(log(2L))))=O_epsilon(L^epsilon), the stated exponent form follows.

This theorem differs from IL: one common denominator and a single exact frequency lattice replace the independent bounds O(sqrt(h/L)). The improvement holds for every fixed coefficient pair satisfying IL's joint separation, not just the particular critical constants. The signed Gauss correlations and the finite residual paid for slow phase freezing are both necessary in the argument.

## 5. Transfer to the actual exceptional budgets

Use IL section 4 verbatim at its hypothesis level: IJ localizes the crossing to the three-term expression with O(1/q) sign band. Integer budgets in a complete two-term exception band are counted by the ideal interval (Q_n-W,Q_n], W=2Z0/s0, with ambiguity only within O(1/n) of Q_n-W. Three-term ambiguous budgets lie in the same shrinking bands. On dyadic blocks of n, prefix interval discrepancy bounds the number of such possible ambiguities by O(1+M D_M+(M/2)D_floor(M/2)) with comparable constants. Sum the blocks, first discarding n<=sqrt(M) at cost O(sqrt(M)), and using the comparable log scales for the rest. Also the ideal interval counts sum to MW+O(M D_M). There are s0 sqrt(X)+O(1) complete bands for q<=X. Substitution proves both asserted exception estimates, with the explicit subpower factor as in the main discrepancy theorem if desired. ID is still NOT_REVIEWED; no independent review or formal task completion is claimed.

## 6. Author checks (exact integers and rationals, actually run)
These finite checks are not the proof of the unbounded result. They independently test the combinatorial shift count, the composite gcd inequality, and common rational lattice condition. Source code and output:

```python
from math import gcd
from fractions import Fraction
count=0
for r in range(1,101):
 for h in range(1,101):
  c=sum((2*h*k)%r==0 for k in range(r))
  assert c==gcd(2*h,r) and c<=2*gcd(h,r)
  count+=1
print('exact Gauss shift-count cases:',count)
c=0
for r in range(1,61):
 for j in range(1,61):
  for k in range(1,61):
   assert gcd(j*k,r)<=gcd(j,r)*gcd(k,r)
   c+=1
print('exact joint gcd inequalities:',c)
H=48; ep=Fraction(1,1000); c=0; multi=0
for den in range(1,61):
 for num in range(den):
  x=Fraction(num,den); a=[]
  for h in range(1,H+1):
   v=h*x; b=(2*v.numerator+v.denominator)//(2*v.denominator)
   if abs(v-b)<=ep:a.append((h,b))
  if a:
   t=Fraction(a[0][1],a[0][0])
   assert all(Fraction(b,h)==t and h%t.denominator==0 for h,b in a)
   c+=1;multi+=len(a)>1
print('nonempty resonance rational cases:',c,'multiple frequencies:',multi)
```
Output:
exact Gauss shift-count cases: 10000
exact joint gcd inequalities: 216000
nonempty resonance rational cases: 1440 multiple frequencies: 810

Classical estimates used: same IL pinned van der Corput first/second derivative and ET inequalities (IL cites https://doi.org/10.1016/j.indag.2015.11.009 and https://arxiv.org/abs/0903.1834). The new complete Gauss estimate and common-rational lattice argument are proved directly above. Fourier analysis is for the declared auxiliary arithmetic observer; it makes no claim of native physical geometry.

## Next
The separation lower bound itself is unchanged: polynomial separation and power-in-X exception savings are still open. Explore stronger quantitative separation via simultaneous rational/exponential constraints or improve the divisor-weight factor through the exact Gauss vanishing conditions, and separately extract explicit uniform IJ remainder for sparse BRC fallback. Do not repeat completed ID finite enumeration absent an identified proof defect.
