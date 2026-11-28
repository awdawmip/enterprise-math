# PREFIX-1147 — Tight fifteen-observer section and exact denominator search

2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESS / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED. No formal CLAIM or shared task execution mutation.

## Inputs and provenance
Predecessor: da7a8d8f8a5f205c2f4499db084881a2b8b03c0c:research_notes/portable_direct/2026-11-28_r6_prefix1146_historical_precision_release.md; prior section 9febc74fc2c7b0ce140c2433c2e6925a83093648. All 225 items of PREFIX1146_SHA256SUMS checked against the attached execution archive. No new raw moment or anchor evaluations. Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and same-pin joint/Heartbeat/residual contracts read; current global entries verified at 5031855ac26f03e5fff0468c6f98317959174981; current portable/continuation and method rules read. Auxiliary algebraic parameter coordinates, not native spatial dynamics.
Own registration r6-20261123-2358-session-start-own-v1; recovery r6-20261128-0954-recovery confirms own managed session unclosed, custody not revoked, no execution authority. Owner read r6-20261128-0954-owner-read SUCCEEDED/error=null, INV-00eddf7e852c36d28c7fd1d0016a3d9d, as of 2026-11-28T01:54:24.868720Z, Source ab8611bcf4a0d76f7b9887eac2c130885d07acf3, total 547, LEASED filter empty.

## Proposition and argument
Use the exact tightened 15 rows from PREFIX-1146, with 12 shared columns C and 15 independent errors e. Write x=rho-r, y=c-u. For any integer n, true parameters obey |a*x+b*y-z|<=S with a=-G*(n[0]*aj+n[1]*dj), b=G*n[1]*am, z=n.m, S=sum_j|n.C_j|+sum_i|n_i|e_i. This follows directly from the inherited global affine observation inclusion and the support of the joint bounded generator box. Construct the signed maximal minors of the six leading columns restricted to seven observer coordinates; cofactor identity cancels those six columns exactly while all other terms are paid. Intersect all new valid inequalities with PREFIX-1145's original outer section; no nesting assumption on rounded observer models.

Actual Bareiss scan: 4551 nonzero sparse normals with at least one point row, plus the repeated PREFIX-1146 common direction (4552 applications); 46 effective clipping operations (each operation imposes both sides); final 20 vertices. Widths rho=1.5293290030899936e-106, c=7.336544841403801e-106, about 166-fold narrower than PREFIX-1145. Independent recursive-minor verification reconstructed the same vertices from only 20 directions and boundary-pair intersections, then independently enumerated using different slicing axes. No floating arithmetic in certification.

Under inherited Stage46, for L>=10^114 a real near-integer pair has primitive line (q,p,h), gcd(p,q)=1, q>=q0 (inherited), 0<=rho-p/q<=K/L^2, 0<=h/q-c<=H/L. Take exact convex hull of translated section and signed rectangle at L0. In unimodular integer coordinates n=V(q,p,h), bounds from extrema at q0,Q and hull vertices enclose every candidate. Each edge becomes a homogeneous integer inequality after positive denominator clearing; intersect the remaining integer coordinate interval by signed floor and ceiling. Thus enumeration is complete, including boundaries. The inverse is checked exactly.

Q=10^71: box [1,4]x[-41,-1]x[1,701], 164 outer loops, no points.
Q=3*10^71: box [1,12]x[-124,-1]x[1,2105], 1488 outer loops, no points.
Q=10^72: box [1,42]x[-415,-1]x[1,7019], 122341170 potential coordinate triples, 17430 outer loops, 2 points, 1 primitive line. Cross-check using 294798 outer loops (different slicing axes), exact same two points.

Primitive (q,p,h):
863851794646735552533804481332297621060190068702869012547694593695364655
18521014198213462105599188567226509018578192364506298927813001962187365171
85643139789681174860642353301200169168579250525165753948553380295288632902

Other point (gcd(q,p)=19):
957723675058109334531019906469052798191755158942122117350687420314201988
20533630761246749388871915289517939494292804294172826589738780661597789045
94949692865349893164649023472383292582059703666969791852401582358981300714

Hence under inherited Stage46/anchor conditions, for all L>=10^114, b-a>=q>=863851794646735552533804481332297621060190068702869012547694593695364655. This is a finite denominator exclusion uniform over the unbounded scale tail. Existing curvature and lower-scale coverage give first not-excluded fixed dyadic windows (base 10^8): 8.872543021186608e138 (triple; 128x PREFIX-1146) and 1.162941958872971e144 (sqrt-spacing pair; 64x). Continuous integer endpoint remains 4.72478e43.

## Full bounded fiber
Using the same 15-row affine system, the remaining primitive line at zero scale payment has exact rational realization T=m+Uz with U=[C,diag(e)], all 27 coefficients strictly inside [-1,1], 1-max|z_i|=0.026242539851944694 (strictly >0.026). Since U has full row rank from positive independent errors, T is interior. No support direction of this tightened affine outer model alone excludes the candidate. This does not assert nonlinear or true spectral attainability. The witness is reconstructed exactly from 12 free rational coordinates below. The LP was a proposal only; all equations and bounds are verified exactly.

## Reproduction
Run from the PREFIX-1146 execution archive, whose exact rows and reconstructors are also given in its fixed paper. The following compact standard-library verifier was executed; it rebuilds a sufficient section from 20 directions, rechecks earlier exclusion through verify1146.py, computes the exact search and reconstructs the fiber without LP. Primary program section1147.py and full outputs are included in the local execution bundle; no new independent reviewer or analytic anchor exit verification.

```python
from fractions import Fraction as F
from itertools import combinations,product
from math import ceil,floor,gcd,lcm
import json,runpy
R=runpy.run_path('verify1146.py'); D=R['D']; A=D['A']
G,L,K,H,aj,am,dj,r,u,m,e,C=[R[k] for k in ('G','L','K','H','aj','am','dj','r','u','m','e','C')]
V,W,q0,hull,d0,solve=[A[k] for k in ('V','W','q0','hull','d0','solve')]
dot=D['dot']; det=D['det']
patterns=[(0, 1, 2, 5, 6, 8, 11), (0, 1, 2, 4, 5, 10, 12), (0, 1, 2, 4, 5, 10, 14), (0, 1, 2, 4, 5, 11, 14), (0, 1, 2, 4, 5, 12, 14), (0, 1, 2, 4, 6, 10, 12), (0, 1, 2, 5, 6, 8, 12), (0, 1, 2, 5, 6, 9, 12), (0, 1, 2, 5, 8, 11, 12), (0, 1, 2, 5, 10, 12, 14), (0, 1, 2, 5, 11, 12, 14), (0, 1, 2, 8, 11, 12, 14), (0, 1, 3, 5, 6, 9, 12), (0, 1, 3, 5, 6, 10, 12), (0, 1, 4, 5, 6, 10, 12), (0, 1, 5, 8, 11, 12, 14), (0, 2, 4, 5, 10, 12, 14), (0, 2, 5, 6, 8, 11, 12), (1, 2, 4, 5, 10, 12, 14), (1, 2, 5, 6, 8, 11, 12)]
# Independently compute signed cofactors by recursive expansion, verify each supplied normal.
I=D['edges'](D['P'])
for p in patterns:
 M=[[c[i] for i in p] for c in C[:6]];v=[(-1)**j*det([row[:j]+row[j+1:] for row in M]) for j in range(7)];g=gcd(*v);assert g
 n=[0]*15
 for i,x in zip(p,v):n[i]=x//g
 assert all(dot(n,c)==0 for c in C[:6]);a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am;z=dot(n,m);S=sum(abs(dot(n,c)) for c in C)+sum(abs(x)*y for x,y in zip(n,e))
 I.extend([(a,b,z+S),(-a,-b,S-z)])
# Reconstruct using intersections of all relevant supporting lines; no clipping or dependency on computed vertices except selecting sufficient directions.
P=set()
for (a,b,c),(x,y,z) in combinations(I,2):
 d=a*y-b*x
 if d:
  v,w=(c*y-b*z)/d,(a*z-c*x)/d
  if all(i*v+j*w<=k for i,j,k in I):P.add((v,w))
P=hull(P);assert len(P)==20
assert [max(v[i] for v in P)-min(v[i] for v in P) < b for i,b in enumerate((F(153,10**108),F(734,10**108)))]==[True,True]
print('widths',*[float(max(v[i] for v in P)-min(v[i] for v in P)) for i in range(2)])
HP=hull([(x+r-a,y+u+b) for (x,y),a,b in product(P,(0,K/L**2),(0,H/L))]);E=D['edges'](HP)
Q=10**72;box=[]
for a,b,c in V:
 vals=[q*(a+b*x+c*y) for q,(x,y) in product((q0,Q),HP)];box.append((ceil(min(vals)),floor(max(vals))))
assert box==[(1,42),(-415,-1),(1,7019)]
assert all(dot(v,w)==(i==j) for i,v in enumerate(V) for j,w in enumerate(zip(*W)))
cs=[(tuple(map(int,W[0])),Q),(tuple(-int(x) for x in W[0]),-q0)]
for a,b,z in E:
 v=[a*W[1][i]+b*W[2][i]-z*W[0][i] for i in range(3)];den=lcm(*(x.denominator for x in v));v=[int(x*den) for x in v];g=gcd(*v);cs.append((tuple(x//g for x in v) if g else tuple(v),0))
# Different slicing axes: n1,n3 fixed; n2 exact integer interval.
points=[];outer=0
for x,z in product(range(1,43),range(1,7020)):
 outer+=1;lo,hi=box[1]
 for (a,b,c),d in cs:
  t=d-a*x-c*z
  if b>0:hi=min(hi,t//b)
  elif b<0:lo=max(lo,-((-t)//b))
  elif t<0:break
  if lo>hi:break
 else:
  for y in range(lo,hi+1):
   q,p,h=map(int,[dot(w,(x,y,z)) for w in W]);assert q0<=q<=Q and all(a*p+b*h<=v*q for a,b,v in E);points.append((q,p,h))
lines=sorted((q,p,h) for q,p,h in points if gcd(q,p)==1);assert len(points)==2 and lines==[(863851794646735552533804481332297621060190068702869012547694593695364655,18521014198213462105599188567226509018578192364506298927813001962187365171,85643139789681174860642353301200169168579250525165753948553380295288632902)]
print('independent',outer,'points',points,'lines',lines,flush=True)
q,p,h=lines[0];x,y=F(p,q)-r,F(h,q)-u;T=[-G*aj*x,G*(am*y-dj*x)]+[F(0)]*13
U=C+[[e[i] if i==j else 0 for i in range(15)] for j in range(15)];piv=[0,1,2,3,4,5,15,16,19,20,22,23,24,25,26];free=[i for i in range(27) if i not in piv];B=[[U[j][i] for j in piv] for i in range(15)]
nums=[-973757460137,-973757460137,973757460137,-973757460137,973757460137,-973757460137,-973757460137,-973757460137,-973757460137,-973757460137,528862732465,245651424229];z=[F(0)]*27
for i,j in zip(free,nums):z[i]=F(j,10**12)
rhs=[T[i]-m[i]-sum(z[j]*U[j][i] for j in free) for i in range(15)]
for i,j in zip(piv,solve(B,rhs)):z[i]=j
assert all(m[i]+sum(z[j]*U[j][i] for j in range(27))==T[i] for i in range(15));slack=1-max(map(abs,z));assert slack>F(26,1000);print('witness',float(slack))
L3=L2=10**8
while L3<=d0*q*q/(4*400000):L3*=2
while L2<=q*q:L2*=2
print('PASS',float(L3),float(L2))
```

Executed output (end):
```
widths 1.5293290030899936e-106 7.336544841403801e-106
independent 294798 points (two exact points above) lines (one exact primitive line above)
witness 0.026242539851944694
PASS 8.872543021186608e+138 1.162941958872971e+144
```

## Next
Test the one certified interior fiber against new information, not more support directions in the same model. Prioritize assessing correlated residual bounds or new radial/coupled raw observations with precision-budget separation. Preserve original quantization and anchor; inherited Stage46 analytic/anchor exit and independent review pending; unbounded final separation and B_fix,odd(32) remain open.
