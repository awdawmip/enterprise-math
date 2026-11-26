# PREFIX-1115 independent finite threshold audit and adaptive convergent chart

2026-11-27 Asia/Shanghai. RESEARCH_DRIVER lane, original author EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 preserved. Source ddf71410e78ccd4f8eee59e8d96d8bab94ce03e5:research_notes/portable_direct/2026-11-27_r6_prefix1115_signed_jet_threshold_order.md. Parent Driver b8c935ee2c4fc63032ef75756dfbdefd10b07cc9. Shared source exposure: independent arithmetic implementation and coordinate method, not independent analytic discovery. No new claim, native Review or Result acceptance. Stage46/P000 and mother B_fix,odd(32) unchanged.

## Review and exact scope
Inherit the author's signed density correspondence, global last-negative monotonicity, sign rule for E/m^2 <= |j-f(m)| <=2, E=400000, m>=10^8, and supplied coefficient intervals (8000 and 8400). Signed derivative transport is valid by MVT for the complete signed derivative if the supplied intervals rigorously enclose it; intersection with the original interval preserves enclosure. Threshold ordering theorem valid: negative at a later disjoint threshold forces rho>=its lower threshold, hence rho>the earlier upper threshold; nonnegative at an earlier one forces rho<=its upper threshold. At most n+1 cut patterns; binary search requires a terminating negative/nonnegative oracle, not just an approximate sign. 8400 outer command exit is unconfirmed in author report; this audit does not re-execute or independently validate analytic anchor, jet coefficients or inherited sign premises.

Independent local exact Python Fraction run using midpoint tangent of L=R0*m+C0+D0/m-E/m² and chord of U=R1*m+C1+D1/m+E/m²; both convex since D0*m>=3E. Euclidean floor sum (signed normalization and y=a*n+b transpose) checked against 23104 brute cases. On a block [l,h], affine lower al*m+bl and upper au*m+bu count via sum(floor(upper)+floor(-lower)+1); zero count excludes the block; recursively bisect all nonzero counts and test exact singleton bands. Checked width <1 in each window and coverage. All 90 author 8000 windows reproduced exactly: 5170 nodes, 22 candidates, SHA256 c000cf55b3d47848c40c44c1054616a8de93606fb5033268f57bcc2d19ee96e5. Exact sorted threshold index order [13,1,11,9,7,21,6,19,2,5,17,4,3,15,14,22,12,20,10,18,8,16]; all threshold intervals strictly inside common rho box, disjoint. 8400 boxes nested; signs along this order 14 negative then 8 positive, matching author. No remaining ambiguity in original 90 windows conditional on boxes.

## New method: candidate-free convergent chart
Previously a unimodular chart was inferred from known candidates. Now take r,c midpoint of the R,C boxes, and successive convergents p/q,t/s of rational r, so det=q*t-s*p=±1. Every (m,j) in Z² equals a(q,p)+b(s,t) for unique integer a,b. Set e=r*m+c-j and dq=r*q-p. Exact b=(q*c+dq*m-q*e)/det. For all candidate integer pairs on [l,h], put err=dr*h+dc+E/l² (dr,dc halfwidths). Then e in [-D1/l-err,-D0/h+err] because D0>0 and m>0. Evaluate four corners of this rectangle to get ceil(min b), floor(max b). For each such b, enumerate ceil((l-b*s)/q)<=a<=floor((h-b*s)/q) and test original band. This includes every candidate; no guessed candidate or slope approximation is needed. Choose consecutive convergents minimizing the rigorous upper count max(0,bhi-blo+1)*(floor((h-l)/q)+1). All rational convergents finite; no asymptotic efficiency asserted. Each selected chart covers all integers independently of floor-sum sieve.

## Actual results
Convergent chart over all 90 old 8000 windows checked only 544 integer pairs; reproduced all 22 and exact digest. 8400 boxes on those same windows: 513 tests, no candidates. Extend 8400 boxes by another ten doubling windows [123794003928538027489912422400000000,126765060022822940149670320537600000000). Floor-sum nodes by window 91..100: [5,5,3,3,1,245,1441,5247,19281,78361]. Candidate counts [0,0,0,0,0,1,6,22,81,332], 442 total. Independent chart checks [6,5,6,6,8,7,14,33,119,444], total 648, all 442 exact pairs agree. Digest 82eb8fcf442e49134b6d8703dee9bb15d247a22b333e787cd1c3744d1698ff21. First remaining m=7757516269187633236376884843293826946, j=166321433670519293441295926909297619632. Thus the contiguous unambiguous interval from 10^8 extends up to this first remaining m (exclusive), and all scales in the extended interval except 442 are unambiguous, conditional on 8400 coefficients and inherited analytic claims. The 442 are uncertainty candidates, not actual zeros. Chart reduces work on these ten windows from 104592 recursive nodes to 648 lattice checks (different operation types, not walltime benchmark).

## Reproduction
The following compact chart checker is the same arithmetic as the locally executed chart, with functions parameterized rather than global; the exact input boxes and digest are embedded. It can reproduce all candidate lists; no dependence on prior candidate list or external package.
```python
from fractions import Fraction as F
from math import floor,ceil
import json,hashlib
G=10**85;E=400000
B0=[(214400367204046439832747905320189591538351105920951930768238591471336985753828331576226,214400367204046439832747905320189591538351105920951930768238591471337016618243377672837),(991410104376806546245006442360370506919542722555360711737697284896267798454119146866295,991410104376806546245006442360370506919542722555360711737697284896271170423247861515800),(96908626596415488199625924806903600960651737707918479478269855624901489595100026049591,96908626596415488199625924806903600960651737707918479478269855625221421002362182677574)]
B1=[(214400367204046439832747905320189591538351105920951930768238591471337001196109386645552,214400367204046439832747905320189591538351105920951930768238591471337001196656728356815),(991410104376806546245006442360370506919542722555360711737697284896269484458469127177428,991410104376806546245006442360370506919542722555360711737697284896269484518264379180719),(96908626596415488199625924806903600960651737707918479478269855625061452448312226656203,96908626596415488199625924806903600960651737707918479478269855625061458121669367665141)]
assert all(a<=c<=d<=b for (a,b),(c,d) in zip(B0,B1))
def run(box,start,end):
 R,C,D=[[F(x,G) for x in p] for p in box]
 r=sum(R)/2;c=sum(C)/2;dr=(R[1]-R[0])/2;dc=(C[1]-C[0])/2
 n,d=r.numerator,r.denominator;pp,qq,p,q=0,1,1,0;conv=[]
 while d:
  a,n,d=n//d,d,n%d;pp,p=p,a*p+pp;qq,q=q,a*q+qq;conv.append((q,p))
 points=[];checks=0
 for k in range(start,end):
  l=10**8*2**k;h=2*l-1
  assert (R[1]-R[0])*h+C[1]-C[0]+(D[1]-D[0])/l+F(2*E,l*l)<1
  err=dr*h+dc+F(E,l*l);elo=-D[1]/l-err;ehi=-D[0]/h+err
  best=None
  for (s,t),(q,p) in zip(conv,conv[1:]):
   if not q or not s:continue
   det=q*t-s*p;assert abs(det)==1
   vals=[(q*c+(q*r-p)*m-q*e)/det for m in (l,h) for e in (elo,ehi)]
   blo,bhi=ceil(min(vals)),floor(max(vals))
   cost=max(0,bhi-blo+1)*((h-l)//q+1)
   if best is None or cost<best[0]:best=(cost,q,p,s,t,blo,bhi)
  _,q,p,s,t,blo,bhi=best;z=[]
  for b in range(blo,bhi+1):
   for a in range(ceil(F(l-b*s,q)),floor(F(h-b*s,q))+1):
    m,j=a*q+b*s,a*p+b*t;checks+=1
    if R[0]*m+C[0]+D[0]/m-F(E,m*m)<=j<=R[1]*m+C[1]+D[1]/m+F(E,m*m):z.append((m,j))
  points+=sorted(z)
 return points,checks
def digest(p):return hashlib.sha256(json.dumps(p,separators=(',',':')).encode()).hexdigest()
p0,c0=run(B0,0,90);p1,c1=run(B1,0,90);p2,c2=run(B1,90,100)
assert (len(p0),c0,len(p1),c1,len(p2),c2)==(22,544,0,513,442,648)
assert digest(p0)=='c000cf55b3d47848c40c44c1054616a8de93606fb5033268f57bcc2d19ee96e5'
assert digest(p2)=='82eb8fcf442e49134b6d8703dee9bb15d247a22b333e787cd1c3744d1698ff21'
```
No new analytic coefficient computation, exact-zero oracle, all-scale theorem or native admission.

## Additional exact threshold audit on extended candidate bank

Actual second run over the 442 new candidates: every threshold interval is strictly inside the 8400 rho box and pairwise disjoint in sorted order. Minimum consecutive gap 6.540646997948378e-80; maximum width 1.7144199221828455e-105 (display approximations of exact rational values). Therefore at most 443 joint negative/nonnegative patterns rather than 2^442, and at most 9 oracle decisions if a terminating exact sign oracle becomes available. A rho refinement may settle the cut directly; exact-zero decision and full-scale separation remain open.
Reproduce by appending:
```python
R,C,D=[[F(x,G) for x in z] for z in B1]
thresholds=sorted(((F(j)-C[1]-D[1]/m-F(E,m*m))/m,(F(j)-C[0]-D[0]/m+F(E,m*m))/m) for m,j in p2)
assert all(R[0]<l<=u<R[1] for l,u in thresholds)
assert all(u<l2 for (_,u),(l2,_) in zip(thresholds,thresholds[1:]))
print(float(min(l2-u for (_,u),(l2,_) in zip(thresholds,thresholds[1:]))),float(max(u-l for l,u in thresholds)))
```
