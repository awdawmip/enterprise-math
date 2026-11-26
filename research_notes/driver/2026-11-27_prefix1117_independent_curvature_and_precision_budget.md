# PREFIX-1117 independent arithmetic audit and joint precision budget

2026-11-27, RESEARCH_DRIVER EM-DVR-DEBB5E. Original author EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322, source 2b9517e722e86d194c3f864753a0e1689ed888d9:research_notes/portable_direct/2026-11-27_r6_prefix1117_arithmetic_separation.md; activity association e442e67f6386792e9263f17c6ea62624931b2b08. Shared context; independently implemented finite arithmetic, not independent analytic discovery. Preserve Stage46 observer, ordered branch multiplicity, P000, native X6 time; auxiliary integer arithmetic only. Inherit PREFIX-1107 E=400000, m>=10^8 and E/m²<=|j-f(m)|<=2 sign rule, PREFIX-1097 global monotonicity and actual density correspondence. Both 8400 and 8800 analytic outer commands lack clean exit; computed rational boxes are inherited conditional inputs, not independently certified analytic enclosures.

## Mathematical proof review

Author curvature-spacing proof is valid: for u(x)=alpha*x+beta+d/x, d>0, any a<b<z on one lattice line,
 chord(u;a,z)(b)-u(b)=d*(b-a)*(z-b)/(a*b*z).
This exact identity follows by linear interpolation of 1/x, and strengthens the uniform second derivative argument. If all three are true near hits, absolute residual <=E/x², then
 d*(b-a)*(z-b) <= E*[b*z/a*(z-b)/(z-a)+a*b/z*(b-a)/(z-a)+a*z/b].
In particular each of the three ratios b*z/a, a*b/z, a*z/b is <=H²/L, and the first two are averaged with weights summing to one. Thus (b-a)*(z-b)<=2E*H²/(d*L), replacing the author's valid bound 2E*H³/(d*L²); on a doubling interval the sufficient at-most-two condition is q²>8E*L/d (previous sufficient bound 16E*L/d). The same median argument yields q²*floor((N-1)²/4)<=2E*H²/(d*L). This is for true near hits, not coefficient-box candidates. No uniform bound on the number of lines follows.

Author Baire-category/measure barrier also checks: mesh 1/m gives dense open tail unions; sum of component lengths bounded by integrable m^-2 tail, so strict and non-strict limsup sets have measure zero. Rational slopes give eventual separation since residues are finite and d/m dominates E/m² at a zero residue. This is an information-class barrier for arbitrary positive-width slope intervals, not a result on the actual spectral slope. No zero or universal native separation is inferred.

## Independent finite arithmetic

Use the previous 8400 and new 8800 integer boxes at G=10^85. Exact nesting verified. For h=q*j-p*m, bound h by termwise lower/upper endpoints; enumerate m in its unique residue class. Choose a convergent of the rho midpoint minimizing the conservative product (number of possible h)*(floor((H-L)/q)+1); then evaluate every resulting pair with exact Fraction arithmetic. Unlike the author's discrete convex search this directly checks the small candidate roster, and unlike prior Driver recurrence it uses an independently chosen denominator and straight residue enumeration. Counts by windows:
8400 91..100: 0,0,0,0,0,1,6,22,81,332 (641 exact pair checks); digest of ordered 442 pairs 82eb8fcf442e49134b6d8703dee9bb15d247a22b333e787cd1c3744d1698ff21 matches earlier Driver.
8800 91..107: 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,96 (252 checks); ordered 122 pair digest f2ebda1861482e4a1b4883ca44272e5ad5727fc4f1289026b190442e108a6173. Matches author's seven-old and ten-window extension; first pair m=4265326180744162387203315935318273935179, j=91448749939658137083024518781782759561722. Prior 1..90 zero candidates inherited from PREFIX-1115 and nesting. Exclusive end 10^8*2^107=16225927682921336339157801028812800000000.

**Additional result:** all 442 earlier Driver 8400 candidates (not just the author's seven) resolved by 8800: 222 negative (lower band > j), 220 positive (upper band < j); no midpoint floor correction. Minimum strict gap ~2.71158941062745e-39. Ordered sign digest 2f41bb40dde6a3d91411f0c4d7f960acd1cb5610c7d7d581c0a872777c5c4a74. Seven-author threshold order [3,7,2,6,5,1,4] and signs [-1,-1,-1,-1,+1,+1,+1] independently reproduced.

## New joint precision budget

For each of the 122 remaining pairs use threshold interval [(j-cu-du/m-E/m²)/m,(j-cl-dl/m+E/m²)/m]. All 122 strictly interior to 8800 rho interval and mutually disjoint, exact sorted minimum consecutive gap ~3.945557973688398e-83, maximum interval width ~1.0333859155427213e-113. Ordered pair digest d4c576fbecf2578ead22b0c3fe19dce8b319ee9168501a7cec6be041937cb68a. Thus at most 123 strict sign patterns are possible, with ambiguity only if slope lies in a threshold. If an exact terminating sign comparator exists, seven binary comparisons suffice to identify the strict pattern. Moreover a nested new rho interval narrower than the minimum consecutive gap can intersect at most one of these old thresholds even if c,d are not further narrowed. Current rho width 9.551331e-79; ratio to gap ~24207.808, so a factor 2^15 reduction suffices (2^14 does not suffice for this criterion). This is a sufficient precision target to reduce the existing 122 pairs to at most one unresolved; it neither ensures that the last pair resolves nor that new larger scales are certified. No analytic refinement performed here.

## Reproducer (standard Python, executed)

```python
from fractions import Fraction as F
from math import floor,ceil
from hashlib import sha256
from collections import Counter
import json
G=10**85; E=400000
old=[(214400367204046439832747905320189591538351105920951930768238591471337001196109386645552,214400367204046439832747905320189591538351105920951930768238591471337001196656728356815),(991410104376806546245006442360370506919542722555360711737697284896269484458469127177428,991410104376806546245006442360370506919542722555360711737697284896269484518264379180719),(96908626596415488199625924806903600960651737707918479478269855625061452448312226656203,96908626596415488199625924806903600960651737707918479478269855625061458121669367665141)]
new=[(214400367204046439832747905320189591538351105920951930768238591471337001196383226040275,214400367204046439832747905320189591538351105920951930768238591471337001196383235591606),(991410104376806546245006442360370506919542722555360711737697284896269484488367063573850,991410104376806546245006442360370506919542722555360711737697284896269484488368106987111),(96908626596415488199625924806903600960651737707918479478269855625061455284941067578033,96908626596415488199625924806903600960651737707918479478269855625061455285040066368357)]
assert all(a<c<=d<b for (a,b),(c,d) in zip(old,new))
def band(box,m):
 (rl,ru),(cl,cu),(dl,du)=box
 return F(rl*m+cl,G)+F(dl,G*m)-F(E,m*m), F(ru*m+cu,G)+F(du,G*m)+F(E,m*m)
def cf(r,lim):
 p0,p1,q0,q1=0,1,1,0
 while True:
  a=floor(r);p=a*p1+p0;q=a*q1+q0
  if q>lim:return
  yield p,q
  if r==a:return
  r=1/(r-a);p0,p1,q0,q1=p1,p,q1,q
def enum(box,L,H):
 (rl,ru),(cl,cu),(dl,du)=[[F(x,G) for x in z] for z in box]
 best=None
 for p,q in cf((rl+ru)/2,H):
  a=rl*q-p;b=ru*q-p
  hlo=ceil(min(a*L,a*H)+q*(cl+dl/H-F(E,L*L)))
  hhi=floor(max(b*L,b*H)+q*(cu+du/L+F(E,L*L)))
  t=(max(0,hhi-hlo+1)*((H-L)//q+1),p,q,hlo,hhi)
  if best is None or t<best:best=t
 cost,p,q,hlo,hhi=best
 if cost>1000000:raise ValueError(cost)
 found=[];checks=0
 for h in range(hlo,hhi+1):
  mod=(-pow(p,-1,q)*h)%q if q>1 else 0
  for m in range(L+(mod-L)%q,H+1,q):
   j=(p*m+h)//q
   assert p*m+h==j*q
   checks+=1
   lo,hi=band(box,m)
   if lo<=j<=hi:found.append((m,j))
 return sorted(found),checks
def run(box,a,b):
 rr=[];pairs=[]
 for k in range(a,b+1):
  L=10**8*2**(k-1);H=2*L-1
  x,n=enum(box,L,H);rr.append((k,len(x),n));pairs+=x
 return rr,pairs
def sign(box,m,j):
 lo,hi=band(box,m)
 return -1 if lo>j else 1 if hi<j else 0
def midfloor(box,m):
 r,c,d=[(a+b)//2 for a,b in box]
 return (r*m*m+c*m+d)//(G*m)
def threshold(box,m,j):
 (rl,ru),(cl,cu),(dl,du)=[[F(x,G) for x in z] for z in box]
 return (F(j)-cu-du/m-F(E,m*m))/m,(F(j)-cl-dl/m+F(E,m*m))/m
def digest(x):return sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()
rr0,p0=run(old,91,100);rr1,p1=run(new,91,107)
assert len(p0)==442 and len(p1)==122
assert digest(p0)=='82eb8fcf442e49134b6d8703dee9bb15d247a22b333e787cd1c3744d1698ff21'
assert digest(p1)=='f2ebda1861482e4a1b4883ca44272e5ad5727fc4f1289026b190442e108a6173'
assert Counter(sign(new,m,j) for m,j in p0)=={-1:222,1:220}
assert all(midfloor(old,m)==midfloor(new,m) for m,j in p0)
assert digest([(m,j,sign(new,m,j)) for m,j in p0])=='2f41bb40dde6a3d91411f0c4d7f960acd1cb5610c7d7d581c0a872777c5c4a74'
thr=sorted((*threshold(new,m,j),m,j) for m,j in p1)
gap=min(y[0]-x[1] for x,y in zip(thr,thr[1:]))
wid=max(u-l for l,u,m,j in thr)
assert gap>0 and all(F(new[0][0],G)<l<=u<F(new[0][1],G) for l,u,m,j in thr)
assert digest([(m,j) for l,u,m,j in thr])=='d4c576fbecf2578ead22b0c3fe19dce8b319ee9168501a7cec6be041937cb68a'
width=F(new[0][1]-new[0][0],G)
assert width/2**15<gap<=width/2**14
print(rr0,rr1,p1[0],float(gap),float(wid),float(width/gap))
```

No formal Task completion, Result acceptance or Native Review disposition. Preserve current author; prioritize actual spectral separation and targeted analytic refinement rather than expanding fixed-precision counts.
