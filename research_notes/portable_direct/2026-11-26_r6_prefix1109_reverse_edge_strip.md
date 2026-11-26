# PREFIX-1109 -- Reverse edge observation: recycle exact large-scale endpoints to close all 128 uncertain rows

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_AUXILIARY_COMPUTATION / NOT_REVIEWED. Continuation of the own R6 Activity RA-0ABD84561C86E53067DB0322, EM-DIRECT-780BBE / TASK_RESEARCH; original registration r6-20261123-2358-session-start-own-v1 returned SUCCEEDED, execution_authorized=false. New read-only LEASED query r6-20261126-1948-owner-read-v1 was RUNNING at last read before publication. No new claim, run, shared task mutation, review or acceptance.

## Frozen inputs and source links

P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint/time companions. Same Stage46 six-axis X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations Link {O,e1} blocked without renormalization, exactly two negative steps. Keep full signed joint Cell equality, port, phase and ordered branch multiplicity in original carrier. Only certified radial observer D_m(k)=L[x^m(1-x)^k] is used here; no new native propagation or physical residual attribution.
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md (strict normalized infinite suffix monotonicity for m>=280000,k>=21m).
- 60f5d76fb61beaefbd9c479a0e96c9429c379513:research_notes/portable_direct/2026-11-26_r6_prefix1100_centered_beta_dual.md (three previously certified exact rows at 10^20,10^21,10^22).
- 7e95625df3a8c21b6d370246065d51469afa6345:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.md (effective sign band E=400000).
- bd6e81d3baba1aa8bcea7caec629814475fe5ab6:research_notes/portable_direct/2026-11-26_r6_prefix1107b_real_window_sieve.md (coefficient boxes).
- 373ebdb904c3c2467718832e2ed354eb6c16712f:research_notes/portable_direct/2026-11-26_r6_prefix1108_adaptive_box_sieve.md (128 uncertain rows and exact adaptive sieve).

## 1. Reverse observation theorem (new)

Let f(m)=rho*m+c+d/m, E=400000. Inherit 1107 strict sign D_m(k)=sign(k-f(m)) for E/m^2<=|k-f(m)|<=2, m>=10^8, and 1097 monotonicity. For any such m set a=floor(f(m)-E/m^2), z=ceil(f(m)+E/m^2). Both are in the 21m monotone cone by the inherited rho,c,d bounds, both offsets lie in the indicated band, and D_m(a)<0<D_m(z). Therefore a<=K_last(m)<=z-1. In particular
    K_last(m)-E/m^2 <= f(m) <= K_last(m)+1+E/m^2.
The weak inequalities are sufficient and safe even when a true observation is zero. The exact integer K is thus a linear strip in the three unknown coefficients, NOT merely a prediction from them. With c in [c0,c1] and d in [t0,t1], it yields
    (K-c1-t1/m-E/m^2)/m <= rho <= (K+1-c0-t0/m+E/m^2)/m.
Intersect every such strip projection with the existing rho interval. This is certified reverse information flow from the already proven high-scale signed BRC observation, with residual E/m^2 explicitly paid. It does not replace the original density, solve for a new model, or treat K as exact f. General width <=1/m+(c1-c0)/m+(t1-t0)/m^2+2E/m^3. Multiple exact rows may sharpen beyond this by intersection.

## 2. Exact actual result

The three source rows:
m=10^20, K=2144003672040464398426
m=10^21, K=21440036720404643983373
m=10^22, K=214400367204046439832847.

Original 1107b coefficient boxes (integer endpoints divided by 10^30) retained for c,d:
rho [21440036720404643983243551290966,21440036720404643983306198520807]
c [99141010437680654620437916203756,99141010437680654628564001195910]
d [9690862659641548432988461360525,9690862659641549206936415331527].
New rho exact endpoints:
2144003672040464398327478589895623193453714350297178240358450753063584668473/100000000000000000000000000000000000000000000000000000000000000000000000
857601468816185759330994359582492773815182095717343374338078680461545579/40000000000000000000000000000000000000000000000000000000000000000000.
Width approximately 7.309060608741085e-23, a factor 857.1173943485794 smaller than 1107b. No new anchor generation or density calculation.

Reconstruct the exact 128 old candidates by the 1108 sieve and verify compact JSON SHA256 c3169c9517f4722b6db3b848b76931ff5d6d3334966f0a790a226636e7d1e5d9; visited 7554 nodes. At each candidate (m,j), evaluate the refined band [L,U] exactly as in 1108. Every j lies outside the band. If j<L then K=j; if j>U then K=j-1, since j is the only possible integer in the old band and the new band is nested. All 128 signs are thereby determined, with exact gap from the refined closed band >10^-12 (minimum displayed 1.6833054688566221e-12). All 128 resolved K equal the old midpoint floor prediction; no overrides. This closes every row in [10^8,64*10^9), including previously unresolved rows. No CT sign fallback.

## 3. Extend the actual sieve

Use the refined rho box with unchanged c,d and E. In the next four disjoint left-closed right-open windows the exact local Fraction sieve returned:
[64000000000,128000000000): 1 visited node, 0 candidates;
[128000000000,256000000000): 217 nodes, 3 candidates;
[256000000000,512000000000): 565 nodes, 8 candidates;
[512000000000,1024000000000): 1951 nodes, 28 candidates.
Total 2734 new nodes, 39 new candidates. Width U-L<1/8 everywhere in the stated total range (exact inequality). The first new pair is (148554233862,3185008229072). The replay produces all 39 pairs in order.

The following single rational formula works for every m in [100000000,1024000000000) except those 39 candidates:
  K_last(m) = floor((42880073440809287966549644888518*m + 198282020875361309249001917399666 + 19381725319283097639924876692052/m)/(2*10^30)).
Its rho coefficient 21440036720404643983274822444259/10^30 is strictly inside the refined box; the c,d coefficients are their old midpoints. For each certified row the entire band and this chosen approximation lie between the same consecutive integers. Old zero-candidate rows also satisfy this by nesting. At every remaining candidate j the neighboring j-1 and j+1 retain strict opposite signs by the inherited sign-band theorem, so K is j-1 or j, including exact zero at j. This is a finite compressed theorem, not a claim that the 39 are genuine zero or CT fallback rows.

Thus [10^8,128*10^9) is completely certified (127900000000 integer rows). Across the entire [10^8,1024*10^9) range, 1023899999961 rows are certified, 39 unresolved. Increase over 1108 =960000000089 certified rows. The old 128 are all closed. Local code executed exact Fraction/integer arithmetic with full old-list hash and every new window; floats for display only. The replay below is built from the immutable 1108 functions and equivalent executed extension, not claimed separately executed as this combined remote Markdown file. No new native propagation, anchor computation, CT sign call, or independent review.

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


Rold=R[:]
rows=[(10**20,2144003672040464398426),(10**21,21440036720404643983373),(10**22,214400367204046439832847)]
for m,k in rows:
    R=[max(R[0],(k-C[1]-T[1]/m-F(E,m*m))/m),
       min(R[1],(k+1-C[0]-T[0]/m+F(E,m*m))/m)]
    assert R[0]<=R[1]
assert (Rold[1]-Rold[0])/(R[1]-R[0])>857
assert R[1]-R[0]<F(731,10**25)
print("rho width",float(R[1]-R[0]),"improvement",float((Rold[1]-Rold[0])/(R[1]-R[0])))
print("rho exact",*[str(r) for r in R])
Rnew=R[:]; R=Rold
windows=[(10**8,2*10**8-1),(2*10**8,10**9-1),(10**9,2*10**9-1),(2*10**9,4*10**9-1),(4*10**9,8*10**9-1),(8*10**9,16*10**9-1),(16*10**9,32*10**9-1),(32*10**9,64*10**9-1)]
old=[];vis=0
for l,h in windows:
    _,v,_,p=isolate(l,h); old+=p;vis+=v
assert len(old)==128 and vis==7554
assert hashlib.sha256(json.dumps(old,separators=(',',':')).encode()).hexdigest()=="c3169c9517f4722b6db3b848b76931ff5d6d3334966f0a790a226636e7d1e5d9"
R=Rnew
for m,j in old:
    lo=R[0]*m+C[0]+T[0]/m-F(E,m*m)
    hi=R[1]*m+C[1]+T[1]/m+F(E,m*m)
    assert hi-lo<1 and not lo<=j<=hi
    k=j if lo>j else j-1
    fhat=sum(Rold)*m/2+sum(C)/2+sum(T)/(2*m)
    assert k==fhat.numerator//fhat.denominator
    assert max(lo-j,j-hi)>F(1,10**12)
r_mid=F(21440036720404643983274822444259,D)
assert R[0]<=r_mid<=R[1]
allnew=[]
for l,h,n_expected,v_expected in [(64*10**9,128*10**9-1,0,1),(128*10**9,256*10**9-1,3,217),(256*10**9,512*10**9-1,8,565),(512*10**9,1024*10**9-1,28,1951)]:
    _,v,_,p=isolate(l,h)
    assert len(p)==n_expected and v==v_expected
    allnew+=p
    print("extension",l,h,v,len(p),p)
assert (R[1]-R[0])*1024*10**9+(C[1]-C[0])+(T[1]-T[0])/10**8+F(2*E,10**16)<F(1,8)
assert len(allnew)==39
print("certified",1024*10**9-10**8-len(allnew))
```

## 5. Next

Consume the 39 candidate pairs directly. The limiting uncertainty is now the width of the reverse edge strip, not the analytic E/m^2 for the new scales. Investigate stronger reverse strips using the *actual certified rational normalized signed observation intervals* at adjacent large-scale rows, rather than rounded decimal displays, and the 1107 linear remainder inequality; this may further improve rho or directly tighten correlated coefficient support. If insufficient, regenerate the higher precision anchors as planned. Keep all exact row certificates and don't recompute the closed range. Uniform Diophantine separation, exact zero, remaining spectral zeros, c2=0 and mother B_fix,odd(32) remain open.
