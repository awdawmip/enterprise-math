# PREFIX-1108 — Adaptive coefficient-box lattice sieve: a contiguous Stage46 interval with 128 unresolved rows

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_AUXILIARY_COMPUTATION / NOT_REVIEWED. Continuation of R6 own Activity RA-0ABD84561C86E53067DB0322 (EM-DIRECT-780BBE / TASK_RESEARCH). The existing registration was recovered from the own session metadata; no formal run or new claim. Owner query r6-20261126-1854-owner-read-v1 was RUNNING at the last observation before this note; this is independent science, not a shared-state mutation.

## Frozen sources and scope

- P000 V5 at f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint/time companions. Same Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve the full six-axis Cell equality, port, sign, phase and ordered branch multiplicity in the native BRC joint carrier.
- 7e95625df3a8c21b6d370246065d51469afa6345:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.md (C=400000 sign-band theorem).
- bd6e81d3baba1aa8bcea7caec629814475fe5ab6:research_notes/portable_direct/2026-11-26_r6_prefix1107b_real_window_sieve.md (coefficient boxes and two previous certified windows).
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md (infinite-tail theorem, inherited through 1107).
- acd24d8499f11d2b8faa6cd0fd8567735f295333:research_notes/portable_direct/2026-11-26_r6_prefix1104_compressed_exception_sieve.md (signed Euclidean floor sum).
This is an exact auxiliary integer observation of the inherited BRC certificate; no new native propagation, classical comparison, density jet, or anchor computation.

## 1. Result

For every integer m in [100000000,64000000000), except 128 explicitly recoverable candidate scales, the global last-negative position equals

K_last(m) = floor((42880073440809287966549749811773*m + 198282020875361309249001917399666 + 19381725319283097639924876692052/m)/(2*10^30)).

Thus 63899999872 rows in a single contiguous range are certified, including the 1100000000 previously certified rows; the new certified count is 62799999872. In particular the entire contiguous interval [100000000,4000000000) is certified with zero exceptions. At each of the 128 remaining rows there is a unique candidate integer j and K_last is either j-1 or j. These are certificate-uncertainty candidates, not established exact zeros or actual expensive-fallback rows. The exact inherited coefficient boxes are sufficient for this result; no higher precision claimed.

## 2. Direct coefficient-box sieve (no A<M prerequisite)

Write f(m)=rho*m+c+d/m and E=400000. Let R=[r0,r1], C=[c0,c1], T=[t0,t1] be the 1107b boxes; 0<t0<=t1. Define the closed possible-integer band

L(m)=r0*m+c0+t0/m-E/m^2,
U(m)=r1*m+c1+t1/m+E/m^2.

Every integer within E/m^2 of f(m) is contained in [L(m),U(m)]. The box describes a conservative superset, not a claim that independently extreme coefficients are simultaneously attainable.

On integer subinterval [l,h] with l>=1, set x=(l+h)/2. For each positive real m in [l,h],

1/m - (2/x-m/x^2)=(m-x)^2/(m*x^2)>=0,
(l+h-m)/(l*h)-1/m=(m-l)*(h-m)/(l*h*m)>=0.

Since E/m^2<=E/l^2, we obtain affine outer bounds

a_l=r0-t0/x^2, b_l=c0+2*t0/x-E/l^2;
a_u=r1-t1/(l*h), b_u=c1+t1*(l+h)/(l*h)+E/l^2.

Then a_l*m+b_l <= L(m) <= U(m) <= a_u*m+b_u.

The count of integer pairs in this outer strip is exactly
sum_{m=l}^h (floor(a_u*m+b_u)+floor(-a_l*m-b_l)+1).
Every summand is nonnegative. Use the signed Euclidean floor sum of 1104 after clearing denominators. If the count is zero, discard the whole block. If positive and l<h, bisect into two disjoint integer subblocks. For l=h, both envelopes equal the true box endpoints, so enumerate the remaining integer j exactly. Termination follows from finite bisection. By induction on the block tree, the surviving pairs are exactly the integer pairs of the *box band*, not just the outer strips. No narrow-strip collinearity assumption, nor A<M restriction from 1104, is used. The cost is the number of visited nodes times poly(log h) for fixed rational input bit length (or polynomial in both input bit lengths); no uniform polylog total complexity is claimed. A zero-count block uses only two floor sums.

For this finite range an explicit global upper bound on U-L is (r1-r0)*64000000000+(c1-c0)+(t1-t0)/100000000+2E/100000000^2 < 1/8 (approximately 4.089422718e-9). At a zero-candidate scale, the rational midpoint fhat lies strictly between the same two consecutive integers as the entire closed band. Thus floor(fhat) lies below f-E/m^2, and its successor above f+E/m^2; both offsets are at most 2 by the width bound. The signs are strict by 1107, and 1097 gives the global last-negative conclusion. At a candidate scale with unique j in the band, j-1 and j+1 are outside it, each at most 2 from f, and strictly negative/positive respectively. Then K_last is j-1 if D_m(j)>=0 or j if D_m(j)<0. Exact zero is included in this dichotomy. No signs asserted at the 128 candidate j.

## 3. Exact execution evidence

Window (inclusive l,h), outer count at root, visited nodes, zero leaves, final candidates:
100000000 199999999 0 1 1 0
200000000 999999999 10 9 5 0
1000000000 1999999999 0 1 1 0
2000000000 3999999999 1 5 3 0
4000000000 7999999999 2 65 32 1
8000000000 15999999999 7 315 153 5
16000000000 31999999999 25 1389 672 23
32000000000 63999999999 100 5769 2786 99

First unresolved pair: (7208283829,154545870084).
Total candidates 128, total visited nodes 7554 (including two previously certified window checks). The canonical compact JSON list of all ordered pairs (no spaces, list of lists, increasing m) has SHA256 c3169c9517f4722b6db3b848b76931ff5d6d3334966f0a790a226636e7d1e5d9. This digest is an additional replay check, not a substitute for the proof.
Actual local Python Fraction runs: 10000 signed floor-sum comparisons and 500 small interval brute comparisons passed; all eight windows computed exactly. No floating-point decision. The large range was not scanned. No exact CT sign calls.

## 4. Reproduction (Python 3 standard library)

```python
from fractions import Fraction as F
from math import lcm
import random,hashlib,json
D=10**30
R=[F(21440036720404643983243551290966,D),F(21440036720404643983306198520807,D)]
C=[F(99141010437680654620437916203756,D),F(99141010437680654628564001195910,D)]
T=[F(9690862659641548432988461360525,D),F(9690862659641549206936415331527,D)]
E=400000

def fs(n,m,a,b):
    q,a=divmod(a,m); ans=q*n*(n-1)//2
    q,b=divmod(b,m); ans+=q*n
    while True:
        if a>=m:
            q,a=divmod(a,m); ans+=q*n*(n-1)//2
        if b>=m:
            q,b=divmod(b,m); ans+=q*n
        y=a*n+b
        if y<m: return ans
        n,b=divmod(y,m); m,a=a,m

def sumfloor(l,h,a,b):
    w=lcm(a.denominator,b.denominator)
    return fs(h-l+1,w,int(a*w),int((a*l+b)*w))

def strip(l,h):
    x=F(l+h,2)
    al=R[0]-T[0]/x**2; bl=C[0]+2*T[0]/x-F(E,l*l)
    au=R[1]-T[1]/(l*h); bu=C[1]+T[1]*F(l+h,l*h)+F(E,l*l)
    return sumfloor(l,h,au,bu)+sumfloor(l,h,-al,-bl)+(h-l+1)

def isolate(l,h):
    stack=[(l,h)]; leaves=[]; points=[]; visited=0; initial=strip(l,h)
    while stack:
        a,b=stack.pop(); cnt=strip(a,b); visited+=1
        assert cnt>=0
        if cnt==0: leaves.append((a,b)); continue
        if a==b:
            low=R[0]*a+C[0]+T[0]/a-F(E,a*a)
            high=R[1]*a+C[1]+T[1]/a+F(E,a*a)
            jl=-((-low.numerator)//low.denominator); jh=high.numerator//high.denominator
            assert cnt==jh-jl+1
            points.extend((a,j) for j in range(jl,jh+1)); continue
        mid=(a+b)//2; stack.extend([(mid+1,b),(a,mid)])
    assert sum(b-a+1 for a,b in leaves)+len({a for a,j in points})==h-l+1
    return initial,visited,leaves,points

rng=random.Random(1108)
for _ in range(10000):
    n=rng.randrange(0,50);m=rng.randrange(1,100);a=rng.randrange(-200,200);b=rng.randrange(-200,200)
    assert fs(n,m,a,b)==sum((a*i+b)//m for i in range(n))
allpts=[]
windows=[(10**8,2*10**8-1),(2*10**8,10**9-1),(10**9,2*10**9-1),(2*10**9,4*10**9-1),(4*10**9,8*10**9-1),(8*10**9,16*10**9-1),(16*10**9,32*10**9-1),(32*10**9,64*10**9-1)]
expected_counts=[0,0,0,0,1,5,23,99]
for (l,h),expected in zip(windows,expected_counts):
    outer,n,leaves,pts=isolate(l,h)
    assert len(pts)==expected
    print(l,h,outer,n,len(leaves),len(pts));allpts+=pts
for _ in range(500):
    l=rng.randrange(10**8,64*10**9-100);h=l+rng.randrange(0,100)
    _,_,_,pts=isolate(l,h)
    expected=[]
    for a in range(l,h+1):
        lo=R[0]*a+C[0]+T[0]/a-F(E,a*a);hi=R[1]*a+C[1]+T[1]/a+F(E,a*a)
        expected.extend((a,j) for j in range(-((-lo.numerator)//lo.denominator),hi.numerator//hi.denominator+1))
    assert pts==expected
width=(R[1]-R[0])*64*10**9+(C[1]-C[0])+(T[1]-T[0])/10**8+F(2*E,10**16)
assert width<F(1,8)
assert len(allpts)==128
assert hashlib.sha256(json.dumps(allpts,separators=(',',':')).encode()).hexdigest()=="c3169c9517f4722b6db3b848b76931ff5d6d3334966f0a790a226636e7d1e5d9"
print(json.dumps(allpts,separators=(',',':')))
print("certified",64*10**9-10**8-len(allpts))
```

The local execution used these functions and equivalent driver cells; the assembled remote code is not claimed separately executed unless a later replay establishes it.

## 5. Next

Use the previously certified higher-precision anchor data or regenerate a tighter coefficient box (not just midpoint rounding) to decide the 128 pairs. Reuse the candidate list rather than rescan the entire range. Test the first unresolved scale at 7208283829 with the signed observer certificate. Improve output-sensitive complexity when boxes are sufficiently narrow; a large uncertainty box can create many candidates. Uniform Diophantine separation, exact zero, remaining spectral zeros and B_fix,odd(32) remain open. No formal Task/Result promotion or independent mathematical review.
