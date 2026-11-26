# PREFIX-1114 independent integer-window audit and unimodular tail chart

2026-11-27 Asia/Shanghai. Driver lane, original author EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 retained. Author source 1af1b1acc240cb357002faadf8ee6617bc81809e:research_notes/portable_direct/2026-11-27_r6_prefix1114_signed_interval_newton.md. Shared exposure: arithmetic verification and additional coordinate reduction, not independent discovery of the analytic jet. Parent audit 1b13c2949147d39e05fdb8edb3b1ecf2c30c0719. Stage46 and P000 scope unchanged. Mother B_fix,odd(32) open.

## Exact scope
Inherit the author's density correspondence, strict sign/monotonicity, E=400000 remainder for m>=10^8 and exact coefficient boxes R,C,D given below. The interval Newton inclusion itself follows directly from MVT: for t* and x in I subset I0, V contains F(x), J contains F' throughout I0 and 0 not in J, so t* in I intersect (x-V/J). The inclusion is valid even when x=t*. This does not independently validate anchor evaluations, analytic derivative bounds or inherited jet formulas. No high-scale CT evaluation.

## Independent window audit
L(x)=R0*x+C0+D0/x-E/x^2 is convex on the positive range here: L''(x)=2(D0*x-3E)/x^4 >=0. U(x)=R1*x+C1+D1/x+E/x^2 is also convex. Thus the full L midpoint tangent and full U endpoint chord enclose the band; these use the varying remainder directly, instead of the author's constant remainder relaxation. Sum integer heights via signed floor sums. The recurrence used in the prior Driver audit counts by height, after extracting signed quotient terms: H=floor((a(n-1)+b)/m), S=nH-S(H,a,m,m-b+a-1) on reduced 0<=a,b<m, plus extracted terms. H=0 terminates. Zero strip excludes all scales; bisection gives exact singleton decisions. Width bound <1 on each window is independently checked.

Actual local Python Fraction/integer run: 23104 signed small-case floor sum checks; 74 windows, 3320 nodes, 16 pairs; SHA256 compact ordered JSON 7936a388e04dd6d37bc750d3e85c5095ac5d809ff7cb698dfd5213d43539df3e matches author. Last 5 (window,nodes,pairs): (70,3,0),(71,1,0),(72,197,1),(73,587,3),(74,2329,12). Exclusive endpoint 1888946593147858085478400000000; certified scales 1888946593147858085478299999984. First candidate m=422424091400218872775160084324 exceeds the preceding Driver extended endpoint 3602879701896396800000000. Consequently all 305 prior unresolved scales (not merely the original author's 77) are now unambiguous conditional on the new boxes. No claim that the 16 new candidates are true zeros.

## Additional exact reduction: unimodular coordinate chart
Take q=56505807154768046103245061979, p=1211486580314330366421489540415, s=94369914397405283120805209915, t=2023294429981812160895126974156. These are differences of retained lattice pairs, and q*t-s*p=-1 by exact integer multiplication. Fix (m0,j0) as the first retained pair. Every integer (m,j) has unique integer coordinates (a,b): (m,j)=(m0,j0)+a(q,p)+b(s,t). Let r,c be box midpoints, dr,dc half-widths, e=r*m+c-j, e0=r*m0+c-j0, dq=r*q-p. Then b=q*(e-e0)-dq*(m-m0) since q*(r*s-t)-s*dq=1. For any candidate in [l,h], e lies in [-D1/l-err,-D0/h+err] where err=dr*h+dc+E/l^2. Evaluating the four corners of this rectangle in (m,e) gives a rigorous integer bound on b. For each b enumerate only ceil((l-m0-b*s)/q)<=a<=floor((h-m0-b*s)/q), then test original exact band. This covers all lattice pairs independently of the adaptive sieve; the choice of a basis from previously found candidates does not compromise completeness because its determinant is a unit. No general efficiency or all-scale theorem asserted.

Actual local run for [10^29,1888946593147858085478400000000-1]: b=-5..6, exactly 380 lattice pairs checked, 16 survive, same full digest as 74-window sieve. Coordinate pairs:
(0,0),(1,1),(3,2),(4,2),(5,3),(6,3),(7,3),(8,4),(9,4),(10,4),(11,5),(12,5),(13,5),(14,5),(14,6),(15,6).
This supplies a compact exact chart for the remaining high-scale ambiguities. It is not a claim that chart discovery alone independently resolves the analytic anchor. Use author ongoing sign adjudication and higher-order remainder research; avoid competing task claim.

## Reproduction: local executed algorithms (combined)
```python
from fractions import Fraction as F
from math import lcm, floor, ceil
import json,hashlib
G=10**65; E=400000
R=[F(x,G) for x in (2144003672040464398327479053201895915383511059209519307682385452026,2144003672040464398327479053201895915383511059209519307682386376698)]
C=[F(x,G) for x in (9914101043768065462450064423603705069195427225553607117376644335915,9914101043768065462450064423603705069195427225553607117377301358636)]
D=[F(x,G) for x in (969086265964154881996259248069036009606517377079184794750212468563,969086265964154881996259248069036009606517377079184794815184644871)]
def fs(n,m,a,b):
    if not n:return 0
    q,a=divmod(a,m);r,b=divmod(b,m)
    y=(a*(n-1)+b)//m
    ans=q*n*(n-1)//2+r*n
    return ans+n*y-fs(y,a,m,m-b+a-1) if y else ans
def affine(a,b,l,h):
    b+=a*l; m=lcm(a.denominator,b.denominator)
    return fs(h-l+1,m,int(a*m),int(b*m))
def band(x,i):return R[i]*x+C[i]+D[i]/x+F((-1 if i==0 else 1)*E,x*x)
def strip(l,h):
    if l==h:return floor(band(l,1))-ceil(band(l,0))+1
    assert l*D[0]>=3*E
    x=F(l+h,2)
    al=R[0]-D[0]/x**2+2*E/x**3
    bl=band(x,0)-al*x
    au=(band(h,1)-band(l,1))/(h-l)
    bu=band(l,1)-au*l
    return affine(au,bu,l,h)+affine(-al,-bl,l,h)+h-l+1
def isolate(l,h):
    stack=[(l,h)]; pts=[]; nodes=covered=0
    while stack:
        a,b=stack.pop(); cnt=strip(a,b);nodes+=1
        assert cnt>=0
        if cnt==0: covered+=b-a+1;continue
        if a==b:
            lo,hi=ceil(band(a,0)),floor(band(a,1));assert cnt==hi-lo+1
            pts.extend((a,j) for j in range(lo,hi+1));continue
        mid=(a+b)//2;stack.extend(((mid+1,b),(a,mid)))
    assert covered+len({m for m,j in pts})==h-l+1
    return nodes,pts
for n in range(1,9):
    for m in range(1,9):
        for a in range(-9,10):
            for b in range(-9,10):
                assert fs(n,m,a,b)==sum((a*i+b)//m for i in range(n))
l=10**8;stats=[];pts=[]
for k in range(74):
    h=2*l-1
    assert (R[1]-R[0])*h+C[1]-C[0]+(D[1]-D[0])/l+F(2*E,l*l)<1
    n,z=isolate(l,h);pts+=z;stats.append((k+1,n,len(z)));l*=2
digest=hashlib.sha256(json.dumps(pts,separators=(',',':')).encode()).hexdigest()
assert digest=='7936a388e04dd6d37bc750d3e85c5095ac5d809ff7cb698dfd5213d43539df3e'
assert len(pts)==16 and pts[0][0]>3602879701896396800000000
assert sum(s[1] for s in stats)==3320
q,p=56505807154768046103245061979,1211486580314330366421489540415
s,t=94369914397405283120805209915,2023294429981812160895126974156
m0,j0=422424091400218872775160084324,9056788031204260215311859264449
assert q*t-s*p==-1
r=sum(R)/2;c=sum(C)/2;dr=(R[1]-R[0])/2;dc=(C[1]-C[0])/2
dq=r*q-p;e0=r*m0+c-j0
l=10**29;h=1888946593147858085478400000000-1
err=dr*h+dc+F(E,l*l)
emin=-D[1]/l-err;emax=-D[0]/h+err
vals=[q*(e-e0)-dq*(m-m0) for e in (emin,emax) for m in (l,h)]
blo,bhi=ceil(min(vals)),floor(max(vals));assert (blo,bhi)==(-5,6)
chart=[];tried=0;ab=[]
for b in range(blo,bhi+1):
    for a in range(ceil(F(l-m0-b*s,q)),floor(F(h-m0-b*s,q))+1):
        m,j=m0+a*q+b*s,j0+a*p+b*t;tried+=1
        if band(m,0)<=j<=band(m,1):chart.append((m,j));ab.append((a,b))
assert tried==380 and sorted(chart)==pts
print(digest,sorted(ab))
```

No native Review, Result admission, Task closure or mother-target completion in this arithmetic audit.
