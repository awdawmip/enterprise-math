# PREFIX-1114 — Signed interval-Newton root refinement and anchor-rounding separation

2026-11-27 Asia/Shanghai. Continuation of EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / NOT_REVIEWED.

## Frozen scope and sources

P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint relation observer preservation remain unchanged. Stage46 X6 chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link{O,e1} blocked without renormalization, exactly two negatives. Retain Cell, port, signed phase, ordered branch multiplicity in parent BRC joint carrier. The following is an auxiliary certified observation of the same signed carrier, not new physical propagation. Mother B_fix,odd(32) open.

- Parent c152e7e760402a273759bffb745e362da20adc43:research_notes/portable_direct/2026-11-26_r6_prefix1113_correlated_density_jet.md (signed density jet, exact 1113 boxes, derivative tails, adaptive lattice sieve).
- PREFIX-1112 009811fe2c80ca95a1a480fa300bb02f74c31246:research_notes/portable_direct/2026-11-26_r6_prefix1112_quadratic_joint_reverse.md.
- PREFIX-1107 7e95625df3a8c21b6d370246065d51469afa6345:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.md; inherited E=400000 for m>=10^8 and strict sign condition; global last-negative monotonicity as in parent. No change to those hypotheses.
- Actual parent attachment PREFIX-1113-execution-evidence.zip, all 15 manifest entries checked. replay.py SHA256 a905181441adf83cedf6f2bf296fd55b16691fe142168e20c9ce74140bd72f1f; joint_result.json dd10d2ea74bbddb23f8ecccd41e1278619a66ec70480ec7517b0ee20d0153a3e; jet.py 4f744ed8b8c9110ec12e5927034b19a4222ecafe4d88cb4b7e416e0ceb7ee82d; jet_result.json 8a9474950fd07c4637f0f75b01429899a8ac7de7780e82bf2bd3b0290e58c637. These are the actual inputs, matching the parent immutable paper.

## 1. New lemma and proof

Let F(t)=sum_i a_i P_i(t) denote the inherited six-component signed density, with full analytic tails paid as in 1113. Its exact zero t*=sqrt(36/(1+rho)) belongs to a closed interval I0. An interval D enclosing F'(t) for every t in I0 excludes zero. At any rational x in a current I subset I0, calculate a rigorous point enclosure V of F(x) via the joint anchor dual. If V=[center-e,center+e], with e=dual(v)+sum_i (|a_i^0|+r_i) w_i+T0, then it includes the true signed sum, by adding/subtracting the fixed rational vector v and applying the dual and the individual coefficient/tail bounds. The widths w_i enclose evaluation of the truncated component at that point. By the real mean value theorem, 0=F(x)+F'(xi)(t*-x) for some xi between t* and x, hence t* belongs to I intersect (x-V/D). Interval arithmetic uses outward rounding. If x=t*, the same inclusion holds. Repeating intersects intervals and preserves the root. This is a contraction only when the computed width shrinks, not a universal contraction claim.

At a fixed point the root-box variation is removed before the joint signed evaluation. This is substantially different from treating every component as independently varying over the entire root box. The parent signed derivative interval (entire parent t enclosure, not point samples) was strictly negative:
[-956923360093658265195807702676004510690411555514682321144296368797707397141,-956923360093658265195807702676004510690411555372504144718142656896980201632]/10^65.
The inherited true F is the same for both new anchor combinations, so this interval remains valid. The original parent t box was evaluated on a 10^80 outward grid; the new 10^140 box is contained in it. Set x=floor(G*(l+h)/2)/G where G=10^140. Endpoints are grid multiples and x belongs to I. Convert t to b=t^2/36 and rho=1/b-1 with outward intervals, intersect parent rho. Recompute c,d with the unchanged density-jet identities (1113); all c,d containment assertions against 1112 pass, and the resulting 7200 boxes are nested in the 6400 boxes.

## 2. Precision diagnosis and actual computation

Three real executions of the root and density calculation: (a) first 10^80 grid attempt did not contract and failed the too-strict rho containment assertion after outward conversion; (b) 10^140 grid with exact grid-center selection, parent 10^50 anchor rounding: rho width 3.7300197333511024e-47; (c) same 6400 anchor and changed only anchor center rounding from 10^50 to 10^85, retaining exact absolute dr in the dual and each individual radius: rho width 2.512546130337598e-50. The anchor solve uses the same six measured right sides, full inverse, and error payment. Rounding scale is not measurement precision. Original rounding drift at 10^50 was a substantial avoidable error. With the 6400 anchor and improved rounding the actual F(x) dual payment was 3.392712937400942e-42; point evaluation rounding and truncation each <1e-65 (outward 65-grid report). The resulting t width 7.090877031299314e-52; c width 1.7853173650065907e-47; d width 1.7654768853848908e-45. 57 windows, 331 nodes through 14411518807585587200000000, one candidate (8518857217561415047828429,182644611560400871798065423); all 77 previous candidates absent. The earlier failed attempt is not a certificate.

Then actual new anchor [6000,6400,6800,7200], rounding 10^85, outward interval G=10^140, 201 terms per basis. All grouped integer divisions, 100-digit anchor grid recovery, elimination matrix SHA256 333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312, and original six coefficient containment assertions passed. True root enclosure from the first interval Newton step remained unchanged on two more steps. F(x) dual payment 1.2485912079764749e-51, t width 2.6095950000724613e-61. Actual widths rho 9.246709243777377e-60, c 6.570227203864888e-57, d 6.497217630688416e-55. Relative to 1113 widths: factors about 5.043e12, 5.530e12, 5.490e12. The final outward endpoints (integer /10^65) are:
rho: 2144003672040464398327479053201895915383511059209519307682385452026 .. 2144003672040464398327479053201895915383511059209519307682386376698
c: 9914101043768065462450064423603705069195427225553607117376644335915 .. 9914101043768065462450064423603705069195427225553607117377301358636
d: 969086265964154881996259248069036009606517377079184794750212468563 .. 969086265964154881996259248069036009606517377079184794815184644871
t: 126659995644219604163996478285389021613125848769777025941085294724 .. 126659995644219604163996478285389021613125848769777025941085320821.
The 65-grid endpoints, rather than floating width display, are used by the finite sieve.

## 3. Real Stage46 integer window certificate

Use E=400000 and the inherited strict sign and tail monotonicity lemmas. For each integer m>=10^8 all possible ambiguity j belongs to [rho_l*m+c_l+d_l/m-E/m^2,rho_u*m+c_u+d_u/m+E/m^2]. For all m outside the candidates, K_last(m)=floor((r*m+s+t/m)/10^65), where r,s,t are floor midpoints of the exact boxes:
r=2144003672040464398327479053201895915383511059209519307682385914362
s=9914101043768065462450064423603705069195427225553607117376972847275
t=969086265964154881996259248069036009606517377079184794782698556717.

Replayed the full adaptive exact floor-sum sieve, 74 doubling windows [10^8,1888946593147858085478400000000), 3320 nodes, 16 candidate pairs, 1888946593147858085478299999984 certified scales. All 77 old candidates and the one 6400-stage candidate are closed by the new box. First remaining pair (422424091400218872775160084324,9056788031204260215311859264449). Continuous no-exception prefix [10^8,422424091400218872775160084324), count 422424091400218872775060084324. Last 3 windows contain 1,3,12 candidates, with 197,587,2329 nodes. Compact ordered candidate-pair JSON SHA256 7936a388e04dd6d37bc750d3e85c5095ac5d809ff7cb698dfd5213d43539df3e. These are conditional on inherited correspondence and sign theorems; no high-scale CT evaluation or independent review.

## 4. Reproduction: exact window checker (compact transcription of actual root_7200_window.py)

```python
from fractions import Fraction as F
from math import lcm
import json,hashlib
G=10**65; E=400000
R=[F(x,G) for x in (2144003672040464398327479053201895915383511059209519307682385452026,2144003672040464398327479053201895915383511059209519307682386376698)]
C=[F(x,G) for x in (9914101043768065462450064423603705069195427225553607117376644335915,9914101043768065462450064423603705069195427225553607117377301358636)]
T=[F(x,G) for x in (969086265964154881996259248069036009606517377079184794750212468563,969086265964154881996259248069036009606517377079184794815184644871)]
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
while l<10**30:
    h=2*l-1
    assert (R[1]-R[0])*h+C[1]-C[0]+(T[1]-T[0])/l+F(2*E,l*l)<1
    n,p=isolate(l,h);new+=p;nodes+=n;windows+=1;l*=2
assert (windows,nodes,len(new),l)==(74,3320,16,1888946593147858085478400000000)
assert new[0]==(422424091400218872775160084324,9056788031204260215311859264449)
assert hashlib.sha256(json.dumps(new,separators=(',',':')).encode()).hexdigest()=='7936a388e04dd6d37bc750d3e85c5095ac5d809ff7cb698dfd5213d43539df3e'
print(l-10**8-len(new))
```

## 5. Reproduction: exact root and jets (compact transcription of actual root_7200.py)

Use parent actual replay.py and joint_result.json, jet_result.json identified above. Copy replay.py to replay_hi.py, change exactly the anchor_dual assignment scale=10**50 to scale=10**85 (retain dr and all dual arithmetic, original containment checks). All other code unchanged. Actual modified replay_hi.py SHA256 be00e8fbb17499166e7015ff20dcd85a97e9eb4acb4965ed7cc97bf7ca74ffdb. The compact checker below is derived from the parent compact jet and the actually executed interval Newton patch; it has not separately been run as transcribed, unlike the archived actual scripts.
```python
from replay_hi import *
from math import isqrt,floor,ceil
G=10**140
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
cc,rad,dual=anchor_dual([6000,6400,6800,7200])
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
# Point enclosure and interval Newton.  Parent jet_result.json contains the
# rigorous signed F' box over the whole parent t interval.
D0=10**65
oldjet=json.load(open('jet_result.json'))
slope=I(*[F(int(x),D0) for x in oldjet['F_jets'][1]])
assert slope.b<0
for it in range(3):
    x=F(floor((t.a+t.b)*G/2),G)
    vals=[horner(p,I(x)) for p in pp]
    mids=[(v.a+v.b)/2 for v in vals]
    widths=[(v.b-v.a)/2 for v in vals]
    center=sum(a*v for a,v in zip(cc,mids))
    ar=dual(mids)
    rounding=sum((abs(a)+r)*w for a,r,w in zip(cc,rad,widths))
    tail=sum((abs(a)+r)*rowbound[0]*tr[0] for a,r,tr in zip(cc,rad,tails))
    total=ar+rounding+tail
    fx=I(center-total,center+total)
    image=I(x)-fx/slope
    t=I(max(t.a,image.a),min(t.b,image.b))
b=t*t/36;rho=1/b-1
rho=I(max(rho.a,rl),min(rho.b,ru))
print('rho',floor(rho.a*D0),ceil(rho.b*D0))
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

## 6. Exact execution evidence references

Actual local root_hi.py 7a8b23f4b84314ea9571d5c4c01c110487f198ce10adea7a4903244824ef7cb2; root_hi_result.json 067ceb5da8d4f7de7261eb63d77c970171a75c1f644d2889e176b4299419a0f4; root_window_result.json 5ce611b13cfe08eaf4ffeaca7b32a252937caf8529d2743d8f2dfce52fd1e2b5. Actual root_7200.py a0c74dfabef977e97c4eac2a84ebf45bcbcafb7fa036a9d711a2d13dbef4a896; root_7200.log a9cdde502b86693e98e07e24c3313fbbd753d81665e19d15e8eeeabe004aee39; root_7200_result.json fb00d7d59fba7fcc6965973802256d4c0ce6ea3c308739e8fa155526fd81a0e2; root_7200_window.py 13930c33a0de7f3c478579d05b0fb9c908f49812d39fc8e53f0e0e478774c126; root_7200_window_result.json b7d9f7629cea677a6b9707b61f643912fa82f03e1e67e8b87a475b23360a42d1. Full original local inputs/scripts/logs/results to accompany response in ZIP. No raw credentials included.

Control: original own registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, no live claim conferred. Current owner filter r6-20261127-0051-leased-read-v1 SUCCEEDED/error=null, as_of 2026-11-26T16:52:41.261623Z, Source 160ad7b22629739e2591d6c0c406131857e6f41f, LEASED empty, next_cursor null. No new claim, no shared Task change. Independent author research only.

Next: resolve 16 remaining candidates, develop signed derivative variation estimate F^(j)(x)+[-B_j*radius,B_j*radius] using rigorous joint F^(j+1) bounds rather than per-component interval wrapping. With sufficient anchor precision this is a reusable enclosure technique. More importantly, investigate arithmetic separation and higher-order signed boundary expansion rather than repeated finite window growth alone. All-scale separation, exact-zero decisions, remaining spectral zeros and mother target open.
