# PREFIX-1113 — independent exact lattice-window audit and one-window extension

2026-11-26, RESEARCH_DRIVER lane. Source author EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 retains ownership and scientific attribution. Exact source c152e7e760402a273759bffb745e362da20adc43:research_notes/portable_direct/2026-11-26_r6_prefix1113_correlated_density_jet.md. Shared source exposure: independent implementation of the finite arithmetic certificate only, not independent discovery or full analytic jet review. P000 V5 and Stage46 frozen carrier unchanged; mother B_fix,odd(32) open. Inherited density correspondence, global sign and remainder E=400000, and coefficient bounds are hypotheses for this audit, not newly certified here.

## Proof of finite enumeration

For integer m>=10^8 use closed band [L(m),U(m)] with L=R0*m+C0+D0/m-E/m^2, U=R1*m+C1+D1/m+E/m^2, bounds from author. On [l,h], upper U is convex (D1,E positive), so its endpoint chord is an upper bound. The lower bound is the sum of the exact affine part, midpoint tangent of convex D0/m and endpoint chord of concave -E/m^2. This improves the envelope by retaining the full varying error instead of a constant payment. For l=h use exact band. At integer m, the number of integer heights in the enclosing strip is floor(upper)+floor(-lower)+1, always nonnegative because lower<=L<=U<=upper. Sum these exactly with a lattice-transposition floor sum. A zero strip excludes all its integer scales; nonzero strips bisect, until singleton exact tests. This proves exhaustive enumeration by finite induction. The separate width bound <1 shows at most one candidate height per scale. For a noncandidate m, the author conditional floor formula is uniquely fixed (any coefficient-box midpoint value lies inside the band).

Independent floor sum recurrence: after signed divmod reduction, 0<=a,b<m, H=floor((a(n-1)+b)/m); count for each height j=1..H the n-ceil((mj-b)/a) valid abscissas. Hence S(n,m,a,b)=nH-S(H,a,m,m-b+a-1), after adding extracted quotient terms; H=0 terminates, a>0 if H>0. Recursion strictly reduces modulus. All arithmetic exact Python Fraction/integer. Small signed brute-force crosscheck 8*8*19*19=23104 cases passed.

## Actual local results

54 original doubling windows: 11684 nodes, 77 ordered pairs, first (207957228264351034193960,4458610610261256681284249), last (1794024571438443984060989,38463952688948443486610499), exclusive end 1801439850948198400000000, certified scales 1801439850948198299999923. Compact JSON pair digest 9b64cd21d585e2e48fd0ecc13d9bcd0b43e3e5b2208b63b347bff56cf1b1d5a3 exactly matches author's result. Last four node/candidate counts (155,1),(757,5),(2267,15),(8361,56).

New additional complete doubling window [1801439850948198400000000,3602879701896396800000000): 33593 nodes, 228 pairs, first (1808361573644522910876996,38771338542707298066444769), last (3601647961094176808737408,77219464539829667334833219), certified scales 1801439850948198399999772, digest ce5035cd48ab1a0b27a1d0084dd744899ea1d53fd49fe671b1e373dd92742a0b. Total 55 windows, 45277 nodes, 305 retained scales. All retained cases remain unresolved, not counterexamples or actual zeros. Prefix before first candidate unchanged. No new Native Review or Result acceptance; this is arithmetic verification and conditional finite extension.

## Reproduction (same exact algorithm as executed locally)

```python
from fractions import Fraction as F
from math import lcm
import hashlib,json
G=10**65;E=400000
R=[F(x,G) for x in (2144003672040464398327479053201895915383511059205534267009916916214,2144003672040464398327479053201895915383511059210197732368843911261)]
C=[F(x,G) for x in (9914101043768065462450064423603705069195427223725835702541366890385,9914101043768065462450064423603705069195427227358928449222727898668)]
D=[F(x,G) for x in (969086265964154881996259248069036009606517198695813510593558216221,969086265964154881996259248069036009606517555410313270831834289680)]
def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)
def floor_sum(n,m,a,b):
    if not n:return 0
    q,a=divmod(a,m);r,b=divmod(b,m)
    ans=q*n*(n-1)//2+r*n
    h=(a*(n-1)+b)//m
    if not h:return ans
    return ans+n*h-floor_sum(h,a,m,m-b+a-1)
def S(a,b,l,h):
    b=a*l+b;m=lcm(a.denominator,b.denominator)
    return floor_sum(h-l+1,m,int(a*m),int(b*m))
def band(m,i):return R[i]*m+C[i]+D[i]/m+F((-1 if i==0 else 1)*E,m*m)
def strip(l,h):
    if l==h:return floor(band(l,1))-ceil(band(l,0))+1
    x=F(l+h,2)
    al=R[0]-D[0]/x**2;bl=C[0]+2*D[0]/x
    e0=-F(E,l*l);e1=-F(E,h*h);s=(e1-e0)/(h-l)
    al+=s;bl+=e0-s*l
    au=(band(h,1)-band(l,1))/(h-l);bu=band(l,1)-au*l
    return S(au,bu,l,h)+S(-al,-bl,l,h)+h-l+1
for n in range(1,9):
 for m in range(1,9):
  for a in range(-9,10):
   for b in range(-9,10):
    assert floor_sum(n,m,a,b)==sum((a*i+b)//m for i in range(n))
def isolate(l,h):
    stack=[(l,h)];pts=[];nodes=0;covered=0
    while stack:
        a,b=stack.pop();cnt=strip(a,b);nodes+=1;assert cnt>=0
        if not cnt:covered+=b-a+1;continue
        if a==b:
            lo,hi=ceil(band(a,0)),floor(band(a,1));assert cnt==hi-lo+1
            pts.extend((a,j) for j in range(lo,hi+1));continue
        mid=(a+b)//2;stack.extend(((mid+1,b),(a,mid)))
    assert covered+len(set(a for a,j in pts))==h-l+1
    return nodes,pts
def digest(p):return hashlib.sha256(json.dumps(p,separators=(',',':')).encode()).hexdigest()
l=10**8;out=[];stats=[]
for k in range(55):
    h=2*l-1
    assert (R[1]-R[0])*h+C[1]-C[0]+(D[1]-D[0])/l+F(2*E,l*l)<1
    n,p=isolate(l,h);stats.append((l,h,n,len(p)))
    if k==54:
        assert (n,len(p),digest(p))==(33593,228,'ce5035cd48ab1a0b27a1d0084dd744899ea1d53fd49fe671b1e373dd92742a0b')
    else:out+=p
    l*=2
assert len(out)==77 and sum(x[2] for x in stats[:-1])==11684
assert digest(out)=='9b64cd21d585e2e48fd0ecc13d9bcd0b43e3e5b2208b63b347bff56cf1b1d5a3'
```

Next useful mathematical step: root refinement and actual sign adjudication at retained scales, rather than treating increasing finite-window length as global separation. Author has that direction in progress; this audit preserves the author's ownership. No claim or formal review binding established.
