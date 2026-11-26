# PREFIX-1113 — Direct correlated density jet, inverse-scale coefficient recovery, and extended integer windows

2026-11-26. EM-DIRECT-780BBE / TASK_RESEARCH; RA-0ABD84561C86E53067DB0322. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / NOT_REVIEWED.

Frozen science unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d; Stage46 X6 chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link{O,e1} blocked without renormalization, exactly two negatives. Keep full Cell, port, signed phase, ordered branch multiplicity in the parent BRC joint carrier. Use its already proved auxiliary observer D_m(k)=L[x^m(1-x)^k], not a new physical propagation or classical comparison. Mother B_fix,odd(32) open.

## Sources and scope

- PREFIX-1096 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md (derivative formulas, certified local root).
- PREFIX-1107 7e95625df3a8c21b6d370246065d51469afa6345:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.md; f6903fef5f9c2eae033eb4524c62bc67b437e3d5:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.py (jet and tail proof, effective E=400000).
- PREFIX-1108 373ebdb904c3c2467718832e2ed354eb6c16712f:research_notes/portable_direct/2026-11-26_r6_prefix1108_adaptive_box_sieve.md (sieve).
- PREFIX-1111 e4ebedecb64b01b33e832d4e7779b3b91fa26097 and 308fe4a28beb9dfadaccc1171514035cb95bc4d0 (anchor grid recovery, earlier window, reproduction wrapper).
- PREFIX-1112 009811fe2c80ca95a1a480fa300bb02f74c31246:research_notes/portable_direct/2026-11-26_r6_prefix1112_quadratic_joint_reverse.md (joint polytope and slope).
- Actual local inputs from attached PREFIX-1112 execution archive: replay.py SHA256 a905181441adf83cedf6f2bf296fd55b16691fe142168e20c9ce74140bd72f1f; joint_result.json dd10d2ea74bbddb23f8ecccd41e1278619a66ec70480ec7517b0ee20d0153a3e. Both match parent manifest and immutable note. No prior high-scale observation recomputed.

## 1. Direct recovery rather than another scale increase

The 1112 inverse procedure left d at width 7.73947953971002e-16. The frozen density is g(x)=constant*J(t)*F(t), t=sqrt(36*x), J=t^6/[(t^2-16)^3(t^2-4)^3]. Use the 1112 certified slope box to locate t at the root b=1/(1+rho). Build the same six signed linear components P_i(t) from four Frobenius series and two homogeneous components, truncated at n=200. The exact 66 signed Laurent terms, 28-to-7 elimination hash 333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312 and four 201-term basis recurrences are rebuilt by the actual parent replay.py. No change of carrier.

Let a_i be true anchor coefficients, a_i^0 the rounded centers, r_i their rigorous individual error bounds. The anchor dual inherited from 1100/1111 supplies |sum (a_i-a_i^0) v_i|<=dual(v) for every fixed rational vector v, using the same uncertain six measured right sides through the inverse matrix and rounding. For j=0..4 compute exact outward grid enclosures P_i^(j)(t) in [v_i-w_i,v_i+w_i] on the complete root interval. Then

 |F^(j)(t)-sum a_i^0 v_i| <= dual(v) + sum (|a_i^0|+r_i) w_i + T_j.

Here T_j pays all omitted terms. This inequality follows by adding/subtracting sum a_i v_i and using the exact dual bound, then triangle inequality only for root-interval variation and tail. No independence of anchor errors assumed. This is a scoped auxiliary observation of the retained signed BRC carrier.

For each basis exponent lambda, p=2*lambda+2*201, Tmax=127/100. Inherited coefficient tail bound 64*T_lambda*2^-n gives at derivative j a first term 64*T_lambda*2^-201*(p falling j)*Tmax^(p-j). Ratios bounded by q_j=Tmax^2/2*((p+2-j+1)/(p-j+1))^j<1. Thus divide the first term by 1-q_j and pay the polynomial readout row by Leibniz with exact absolute row derivative norms. This proves all derivative tails for the entire interval, not samples.

At the exact root F(t)=0. The computed interval contains 0; using the inherited exact root fact set its constant term to zero. Compose truncated formal jets with t(x+h)=t*(1+36*h/t^2)^(1/2) through degree 4 and multiply by J(t(x+h)). All denominators exclude zero; the first coefficient is strictly negative. The resulting jet coefficients are g^(j)(b)/j! up to a common positive factor. Ratio cancels that factor. Let r_j=g^(j)(b)/g'(b), v=b(1-b), L=1-2b, A=-v*r_2/2. Inherited exact identities:
 c=(1-A)/b-2;
 d=-(c+2)*A+r_2/2*(A*L-(c+3)*v+A^2)+r_3/6*v*(2*L+3*A)+r_4/8*v^2.
No use of a numerical fitted crossing or independent propagation. The new jet enclosures are contained in the 1112 c,d boxes. This independently recovers d rather than paying the finite-m interpolation O(1/M) error from 1112.

## 2. Actual computation and exact endpoint certificate

Re-executed parent anchor_dual([5200,5600,6000,6400]); all grouped exact integer divisions, previous box and floor recovery assertions passed. Used 10^80 outward grid for interval arithmetic, exact integer square root on scaled rational root bounds, all n<=200 basis terms, exact rational dual and geometric tails. The root interval was computed using exact 1112 slope fractions. No new high-scale CT signs. The last-line widths below are display only. Endpoints are integers divided by 10^65:
rho:
2144003672040464398327479053201895915383511059205534267009916916214
2144003672040464398327479053201895915383511059210197732368843911261
c:
9914101043768065462450064423603705069195427223725835702541366890385
9914101043768065462450064423603705069195427227358928449222727898668
d:
969086265964154881996259248069036009606517198695813510593558216221
969086265964154881996259248069036009606517555410313270831834289680

Widths rho 4.663465358926995e-47 (unchanged), c 3.633092746681361e-44 (2.589014412518063e15-fold), d 3.567144997602383e-42 (2.1696565586518144e26-fold). Normalized derivative ratio widths: r2 7.525260373987222e-44, r3 1.3344855829474124e-41, r4 2.3334548094663995e-39. The first density jet coefficient enclosure (common factor removed) at 10^65:
[-1368786681290847096476201583917176569095811213154789352011205933565145184,-1368786681290847096476201583917176569095811212931950879580449901428422275].
F^(j) widths for j=0..4 before exact root substitution: [6.325150673311774e-37,1.4217817642615371e-36,4.4347508021761093e-36,1.566003156214805e-35,5.766708154491107e-35]. The leading uncertainty in these bounds is variation across the existing root enclosure evaluated by per-component interval Horner, not the series tail. For j=4, dual=2.247870419200972e-37, root interval variation=2.8608753730535436e-35, tail=6.611430240490135e-58. Next useful precision improvement: signed joint derivative bound for the root interval variation rather than per-component wrapping; then refine the root itself by direct dual-based signed density.

## 3. Exact integer windows

E=400000 from 1107. For every m>=10^8 and integer j potentially ambiguous, use inherited sign theorem and global last-negative monotonicity: j in [rho_l*m+c_l+d_l/m-E/m^2,rho_u*m+c_u+d_u/m+E/m^2]. Coefficient box midpoints rounded down to integer numerator at grid 10^65 are
r=2144003672040464398327479053201895915383511059207865999689380413737
s=9914101043768065462450064423603705069195427225542382075882047394526
t=969086265964154881996259248069036009606517377053063390712696252950.
They are interior to the certified boxes. For each scale outside the band candidates, K_last(m)=floor((r*m+s+t/m)/10^65), by the inherited strict sign boundary and monotonicity. The band width is <1 throughout the tested range. No claim about exact zero at retained candidates.

Using 1108's tangent/secant affine envelope and exact signed Euclidean floor sum, re-sieved [10^8,1801439850948198400000000), 54 doubling windows, 11684 nodes, 77 candidate pairs, SHA256 of compact JSON ordered pairs 9b64cd21d585e2e48fd0ecc13d9bcd0b43e3e5b2208b63b347bff56cf1b1d5a3. Outward 65-decimal slope endpoints give IDENTICAL full results to exact parent slope fractions (actually executed separate replay). The first candidate is (207957228264351034193960,4458610610261256681284249). Therefore entire continuous prefix [10^8,207957228264351034193960) is now certified with the new unified formula, and all but 77 scales in the larger range are certified (1801439850948198299999923 scales). Separate replay starting at old 1111 endpoint 1073741824000000000 reached 140737488355328000000000, 17 windows, 45 nodes, zero candidates. These are finite, author-verified, conditional on inherited density correspondence and global sign lemmas; no independent mathematical review.

Last four windows, inclusive right endpoint:
112589990684262400000000..225179981368524799999999 : 155 nodes, 1 candidate
225179981368524800000000..450359962737049599999999 : 757 nodes, 5 candidates
450359962737049600000000..900719925474099199999999 : 2267 nodes, 15 candidates
900719925474099200000000..1801439850948198399999999 : 8361 nodes, 56 candidates.

## 4. Standalone exact window checker

The following is a compact transcription of the actually executed rounded-window algorithm; no dependency on private local data. It reproduces the finite lattice certificate from the displayed outward boxes. The actual local rounded replay used the same recurrence and compared its entire JSON to the exact-parent run.

```python
from fractions import Fraction as F
from math import lcm
import json,hashlib
G=10**65; E=400000
R=[F(x,G) for x in (2144003672040464398327479053201895915383511059205534267009916916214,2144003672040464398327479053201895915383511059210197732368843911261)]
C=[F(x,G) for x in (9914101043768065462450064423603705069195427223725835702541366890385,9914101043768065462450064423603705069195427227358928449222727898668)]
T=[F(x,G) for x in (969086265964154881996259248069036009606517198695813510593558216221,969086265964154881996259248069036009606517555410313270831834289680)]
def fs(n,m,a,b):
    q,a=divmod(a,m);ans=q*n*(n-1)//2
    q,b=divmod(b,m);ans+=q*n
    while True:
        if a>=m:q,a=divmod(a,m);ans+=q*n*(n-1)//2
        if b>=m:q,b=divmod(b,m);ans+=q*n
        y=a*n+b
        if y<m:return ans
        n,b=divmod(y,m);m,a=a,m
def sf(l,h,a,b):
    w=lcm(a.denominator,b.denominator)
    return fs(h-l+1,w,int(a*w),int((a*l+b)*w))
def band(m):
    return R[0]*m+C[0]+T[0]/m-F(E,m*m),R[1]*m+C[1]+T[1]/m+F(E,m*m)
def strip(l,h):
    x=F(l+h,2)
    al=R[0]-T[0]/x**2;bl=C[0]+2*T[0]/x-F(E,l*l)
    au=R[1]-T[1]/(l*h);bu=C[1]+T[1]*F(l+h,l*h)+F(E,l*l)
    return sf(l,h,au,bu)+sf(l,h,-al,-bl)+h-l+1
def isolate(l,h):
    stack=[(l,h)];pts=[];nodes=covered=0
    while stack:
        a,b=stack.pop();cnt=strip(a,b);nodes+=1;assert cnt>=0
        if cnt==0:covered+=b-a+1;continue
        if a==b:
            lo,hi=band(a);jl=-((-lo.numerator)//lo.denominator);jh=hi.numerator//hi.denominator
            assert cnt==jh-jl+1;pts.extend((a,j) for j in range(jl,jh+1));continue
        mid=(a+b)//2;stack.extend([(mid+1,b),(a,mid)])
    assert covered+len({a for a,j in pts})==h-l+1
    return nodes,pts
l=10**8;new=[];nodes=windows=0
while l<10**24:
    h=2*l-1
    assert (R[1]-R[0])*h+C[1]-C[0]+(T[1]-T[0])/l+F(2*E,l*l)<1
    n,p=isolate(l,h);new+=p;nodes+=n;windows+=1;l*=2
assert (windows,nodes,len(new),l)==(54,11684,77,1801439850948198400000000)
assert new[0]==(207957228264351034193960,4458610610261256681284249)
assert hashlib.sha256(json.dumps(new,separators=(',',':')).encode()).hexdigest()=='9b64cd21d585e2e48fd0ecc13d9bcd0b43e3e5b2208b63b347bff56cf1b1d5a3'
print(l-10**8-len(new))
```

## 5. Reproduction of the jet calculation

Use actual parent replay.py from the 1112 execution archive (hash above), and joint_result.json with exact 1112 bounds. The following core is a compact transcription of the actual jet.py (archived separately); use Fraction exact operations and outward grid rounding. The original local code also emits each derivative payment and asserts c,d containment.

```python
from replay import *
from math import isqrt,floor,ceil
G=10**80
class I:
    def __init__(self,a,b=None):
        self.a=F(floor(F(a)*G),G);self.b=F(ceil(F(a if b is None else b)*G),G)
        assert self.a<=self.b
    @staticmethod
    def cast(x):return x if isinstance(x,I) else I(x)
    def __add__(self,x):
        x=I.cast(x);return I(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,x):return self+-I.cast(x)
    def __rsub__(self,x):return I.cast(x)+-self
    def __mul__(self,x):
        x=I.cast(x);v=[u*w for u in (self.a,self.b) for w in (x.a,x.b)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=I.cast(x);assert x.a*x.b>0
        return self*I(1/x.b,1/x.a)
    def __rtruediv__(self,x):return I.cast(x)/self
    def __pow__(self,n):
        assert n>=0;v=I(1)
        for _ in range(n):v*=self
        return v
def fall(n,j):return prod(range(n-j+1,n+1)) if n>=j else 0
def dp(p,j):return [p[n]*fall(n,j) for n in range(j,len(p))]
def horner(p,t):
    v=I(0)
    for a in reversed(p):v=v*t+a
    return v
Tmax=F(127,100);degree=2*(N+2+10)
def norm(p,j):return sum(abs(v)*Tmax**i for i,v in enumerate(dp(p,j)))
cc,rad,dual=anchor_dual([5200,5600,6000,6400])
boxes=json.load(open('joint_result.json'))['bounds']
rl,ru=map(F,(boxes[0]['lo'],boxes[0]['hi']))
blo,bhi=1/(1+ru),1/(1+rl);b=I(blo,bhi)
lo=isqrt(floor(36*blo*G*G));hi=isqrt(floor(36*bhi*G*G))+1
t=I(F(lo,G),F(hi,G))
assert F(5,4)<t.a<=t.b<Tmax and t.a*t.a<=36*blo<=36*bhi<=t.b*t.b
pp=[];tails=[]
rowp=[[F(rr[i//2]) if i%2==0 else F(0) for i in range(2*len(rr)-1)] for rr in nums]
rowbound=[sum(norm(p,j) for p in rowp) for j in range(5)]
for a,z,h,err,T0 in basis:
    p=[F(0)]*(degree+1);off=int(2*a)
    for n in range(N+1):
        for i,v in enumerate(z[n]+[h[0][n],h[1][n]]):
            for k,w in enumerate(nums[i]):p[off+2*(n+k)]+=v*w
    pp.append(p);tail=[]
    for j in range(5):
        n=N+1;power=off+2*n
        ratio=Tmax*Tmax/2*F(power+2-j+1,power-j+1)**j;assert ratio<1
        tail.append(64*T0*F(1,2)**n*fall(power,j)*Tmax**(power-j)/(1-ratio))
    tails.append(tail)
for j in range(2):
    p=[F(0)]*(degree+1)
    for k,w in enumerate(nums[7+j]):p[2*(k+j)]=F(w)
    pp.append(p);tails.append([F(0)]*5)
Fs=[]
for j in range(5):
    vals=[horner(dp(p,j),t) for p in pp]
    mids=[(v.a+v.b)/2 for v in vals];widths=[(v.b-v.a)/2 for v in vals]
    center=sum(a*v for a,v in zip(cc,mids));ar=dual(mids)
    tw=sum((abs(a)+r)*w for a,r,w in zip(cc,rad,widths))
    tail=sum((abs(a)+r)*sum(comb(j,k)*rowbound[k]*tr[j-k] for k in range(j+1)) for a,r,tr in zip(cc,rad,tails))
    total=ar+tw+tail;Fs.append(I(center-total,center+total))
assert Fs[0].a<=0<=Fs[0].b;Fs[0]=I(0)
def muljet(a,b):return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(5)]
def binomhalf(n):return prod(F(1,2)-i for i in range(n))/factorial(n)
R0=t*t;u=[I(0)]+[t*binomhalf(i)*(36/R0)**i for i in range(1,5)]
pw=[I(1)]+[I(0)]*4;val=[I(0)]*5
for j in range(5):
    val=[a+Fs[j]/factorial(j)*b for a,b in zip(val,pw)];pw=muljet(pw,u)
poly=[comb(3,i)*R0**(3-i)*36**i if i<=3 else I(0) for i in range(5)]
for v in (4,16):poly=muljet(poly,[comb(i+2,2)*36**i/(v-R0)**(i+3) for i in range(5)])
jets=muljet(poly,val);assert jets[1].b<0
r2,r3,r4=[jets[j]*factorial(j)/jets[1] for j in (2,3,4)]
v=b*(1-b);L=1-2*b;A=-v*r2/2;c=(1-A)/b-2
d=-(c+2)*A+r2/2*(A*L-(c+3)*v+A*A)+r3/6*v*(2*L+3*A)+r4/8*v*v
for x,box in [(c,boxes[1]),(d,boxes[2])]:
    assert F(box['lo'])<=x.a<=x.b<=F(box['hi'])
    print(floor(x.a*10**65),ceil(x.b*10**65))
```

Actual local jet.py hash 4f744ed8b8c9110ec12e5927034b19a4222ecafe4d88cb4b7e416e0ceb7ee82d; jet_result.json 8a9474950fd07c4637f0f75b01429899a8ac7de7780e82bf2bd3b0290e58c637; jet.log bc3540f6d05dfc86b4e8aceaf429cb54779bb9aa076417e9a8fb516374577b16. Full local original execution code and JSON evidence will accompany this report as a ZIP, separate from the compact transcriptions. The compact scripts were not separately executed as transcribed; actual original/rounded window scripts were executed.

## 6. Current control and next question

Own registration original r6-20261123-2358-session-start-own-v1 SUCCEEDED; scope TASK_RESEARCH independent, not CLAIM. Owner list r6-20261126-2345-owner-read-v1 SUCCEEDED/error=null, fixed as-of 2026-11-26T15:46:24.809521Z, Source b5bd8b79c1a9d8cd2c7290537612bd0fa5870eee, LEASED filter empty, next_cursor null. No new CLAIM, shared Task mutation, Result, or independent review.

Next: close the 77 remaining coefficient uncertainty points with direct signed root refinement (preserve joint anchor dual and signed derivative cancellations); then develop a cubic reverse and explicit higher-order asymptotic remainder if useful. Remaining all-scale arithmetic separation, exact zero and remaining spectral zeros are open. No new physical residual attribution or P000 change.
