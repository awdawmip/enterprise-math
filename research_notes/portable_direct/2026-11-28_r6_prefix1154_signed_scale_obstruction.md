# PREFIX-1154 — refined joint section and signed-scale obstruction

2026-11-28. Author: EM-DIRECT-780BBE / TASK_RESEARCH, original own registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, RA-0ABD84561C86E53067DB0322. No formal CLAIM or shared Task mutation. Owner inventory r6-20261128-1650-owner-read SUCCEEDED/error=null, INV-98709a40b61c81a3f544ef3ccb67edeb, as_of 2026-11-28T08:50:49.568183Z, Source 0715e998d07e46122502804d1aaa047d58ef2190, 547 tasks, LEASED filter empty, Source and event issue unchanged at completion. No execution authority inferred. Global entry verified at c7523728fe4602a2139c728ca644b96767972617; frozen P000 V5 and companions f42f2906d77f24085c123f3ccfe9667d41caa96d. Auxiliary spectral algebra; no native spatial promotion. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESSES / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Input and theorem

Continuation of [PREFIX-1153](https://github.com/awdawmip/enterprise-math/blob/59e745926a4ef00e9161f16d0e45979e6b180d8d/research_notes/portable_direct/2026-11-28_r6_prefix1153_point_observer_precision.md), exact blob c98733b0192de286358b39cd69086f4a80f587d6. Input attached PREFIX-1153-execution-evidence.zip SHA256 b77d6a86cfa259f87cca7ad1ee76caa076f46439ef145d672c15efd0998cc71a; inherited PREFIX1153_SHA256SUMS verified. point1153.json SHA256 e63d78a63e887a1fb1dee9e53366c9bebc92ce2d4ded717d963672fe5d605280; fixture1141.json cb38649b5a98a767b9658c9792af8d21f66b1c2f9290d1e7160b6cc602b6481a; verify1151_compact.py e0f8f623be0251fa4fc186d32e61126134eb7a3f0af52bcd7411034cc722fbef. Same 15 rows, 12 common residual columns, final grid G=10^140, frozen 9600 anchor, no new raw moments or anchor computation. All claims about exceptional integers inherit Stage46, anchor, q0, affine transfer and signed scale conditions, not newly proved here.

Intersect the old parameter polygon with the new inequalities |n dot (A x + B y - m)| <= sum_j |n dot C_j| + sum_i |n_i| e_i. Here x=rho-r, y=c-u, A=(-G aj,-G dj,0,...), B=(0,G am,0,...). For each seven-coordinate set meeting {0,1}, construct n from signed six-row minors; all six leading columns cancel and every remaining direction is paid. Scan 4551 nonzero directions, 99 effective clips, 18 vertices; the same nine patterns as PREFIX-1151 suffice to reconstruct the new section by pairwise boundary intersection. Widths rho 2.2022765859596603e-124 and c 1.0563396681613945e-123. This is an outer section, not an assertion of equality to the full fiber. Exact rational LLL in the maximum-triangle observation metric (46 iterations) gives integer V and W=V^-1 verified. For q in [q0,Q], (p/q,h/q) must lie in the polygon shifted by (r,u) and the rectangle [-K/L^2,0] x [0,H/L] with L=10^114. Each integer coordinate V(q,p,h) is bounded by extrema at q0,Q and polygon vertices; hence full enumeration at Q=10^79 is only the five points n1=0,n2=1,-2<=n3<=2. Three pass all constraints and gcd(q,p)=1; no others. Minimum q=6239409291311791014567645871419543547794851440134183503028222922087402635765205. Thus b-a>=q>=q_min for L>=10^114 under inherited hypotheses. First unexcluded dyadic triple and pair windows 3.121748550315992e152 and 4.0917382598701773e157 by inherited formulas.

## Distinguish scale uncertainty from observer uncertainty

For each remaining line let v=A(p/q-r)+B(h/q-u)-m and U=[C,diag(e)]. With zero scale all three are excluded by exact rows of an inverse 15-column pivot matrix. Ratios 9.125877942188089e14, 5.312149457537903e14, 2.597724718309435e14. At L=10^114 retain s=-AK/(2L^2), t=BH/(2L). The equation v-s-t=[U,s,t]z with |z_j|<=1 has strict rational witnesses for all three: slacks 0.2221059507685677, 0.884811253918, 0.490603091067. This proves the signed-scale affine outer model cannot separate these lines at the inherited worst-case scale, not actual spectral attainability. Floating LP used only to find free coefficients, exact rational inverse and equality checks certify all witnesses.

For n oriented so n dot v>0, signed support of v in U[-1,1]+[0,2s]+[0,2t] is at most S(n)+2 max(0,n dot s)+2 max(0,n dot t). Each added nonnegative term decreases monotonically with L. Using exact rows of the zero-scale pivot inverse, sufficient L multipliers 2,2,8 give strict ratios 1.7235020691706595,1.0032460043636287,1.9624123642699398. Consequently **L>=8*10^114 implies b-a>=q>10^79**, under the same inherited assumptions. This additional scale-dependent bound does not replace the uniform q_min result on smaller L. No assertion that the thresholds are minimal.

Next: use scale-dependent rational candidate domains rather than uniformly charging L=10^114; investigate exact one-sided critical scales and extension of q search at larger L. At small L the three signed-scale witnesses remain a model obstruction. Continuous terminal 4.72478e43 unchanged; anchor exit, independent review, unbounded separation and B_fix,odd(32) remain open.

## Reproduction

Run the following compact verifier in the extracted PREFIX-1153 evidence directory. It reconstructs the nine-direction polygon, exact five-point exhaustive search, zero-scale separation, full signed witnesses and monotone scale thresholds using rational arithmetic. No LP needed. Local executed compact1154.py SHA256 d00a260c1cde61daeaac658d980bf4431d8526e728d38afd696f602f93a404b6. Full scan, LLL, LP witness discovery, independent verification, and logs are retained in PREFIX-1154-execution-evidence.zip. The code's output floats are display only.

```python
from fractions import Fraction as F
from itertools import combinations,product
from math import ceil,floor,gcd
import json,runpy
R=runpy.run_path('verify1151_compact.py');D=R['D'];G=10**140;L=D['L'];K,H,aj,am,dj,r,u,q0,hull,d0,solve,dot,det=[R[k] for k in ('K','H','aj','am','dj','r','u','q0','hull','d0','solve','dot','det')];E=json.load(open('point1153.json'));m,e,C=[E[k] for k in ('m','e','cols')];N=len(m)
I=R['edges'](R['P'])
for p in R['patterns']:
 M=[[c[i] for i in p] for c in C[:6]];v=[(-1)**j*det([row[:j]+row[j+1:] for row in M]) for j in range(7)];g=gcd(*v);assert g
 n=[0]*N
 for i,x in zip(p,v):n[i]=x//g
 assert all(dot(n,c)==0 for c in C[:6]);a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am;t=dot(n,m);s=sum(abs(dot(n,c)) for c in C)+sum(abs(x)*y for x,y in zip(n,e));I.extend([(a,b,t+s),(-a,-b,s-t)])
P=set()
for (a,b,c),(x,y,z) in combinations(I,2):
 d=a*y-b*x
 if d:
  v,w=(c*y-b*z)/d,(a*z-c*x)/d
  if all(i*v+j*w<=k for i,j,k in I):P.add((v,w))
P=hull(P);width=[max(v[i] for v in P)-min(v[i] for v in P) for i in range(2)];assert len(P)==18 and width[0]<F(221,10**126) and width[1]<F(106,10**125)
HP=hull([(x+r-a,y+u+b) for (x,y),a,b in product(P,(0,K/L**2),(0,H/L))]);J=R['edges'](HP)
V=[[-7005584517397982387461258577015113490885477944,326752449560228026278178134938036046452486534,3475123344296718609334826729277527],[10947604889949676181987698266906954418766147471,-510615025177438714072478611334354213249885298,-1563917276331192346885724204278202],[-24101837165649804171836012477060437034988247956,1124150927586941320571023037139872437752224965,-11006138005005896817776376970873142]]
W=list(zip(*(solve(V,[int(j==i) for j in range(3)]) for i in range(3))));assert all(v.denominator==1 for w in W for v in w);W=[list(map(int,w)) for w in W];assert all(dot(v,w)==(i==j) for i,v in enumerate(V) for j,w in enumerate(zip(*W)))
Q=10**79;box=[]
for a,b,c in V:
 vals=[q*(a+b*x+c*y) for q,(x,y) in product((q0,Q),HP)];box.append((ceil(min(vals)),floor(max(vals))))
assert box==[(0,0),(1,1),(-2,2)];pts=[]
for n in product(*(range(a,b+1) for a,b in box)):
 q,p,h=[dot(w,n) for w in W]
 if q0<=q<=Q and all(a*p+b*h<=z*q for a,b,z in J):pts.append((q,p,h))
lines=sorted(v for v in pts if gcd(v[0],v[1])==1);assert len(pts)==len(lines)==3 and lines[0][0]==6239409291311791014567645871419543547794851440134183503028222922087402635765205
U=C+[[e[i] if i==j else 0 for i in range(N)] for j in range(N)];A=[-G*aj,-G*dj]+[0]*(N-2);B=[0,G*am]+[0]*(N-2)
def scale(l):return [[-v*K/(2*l*l) for v in A],[v*H/(2*l) for v in B]]
def inverse(cols,piv):
 M=[[cols[j][i] for j in piv] for i in range(N)];MI=[solve(M,[int(i==j) for i in range(N)]) for j in range(N)];MI=list(zip(*MI));assert all(dot(row,cols[j])==int(i==k) for i,row in enumerate(MI) for k,j in enumerate(piv));return MI
p0=[5,0,14,15,16,17,18,19,3,21,22,23,1,4,2];p1=[5,0,14,15,16,17,18,19,3,21,28,23,1,4,2];s,t=scale(L);U1=U+[s,t];free=[j for j in range(29) if j not in p1];M0=inverse(U,p0);M1=inverse(U1,p1)
a,b=777894049231,115188746082
freevals=[[-a,-a,-a,a,a,-a,-a,-a,-a,702025880919,a,-a,a,-a],[-b,-b,-b,b,b,-b,-b,-b,-b,b,b,-b,b,-b],[0,0,0,0,0,0,-509396908933,-509396908933,163061254883,-157274755222,-509396908933,0,0,-509396908933]]
for line,vals,k in zip(lines,freevals,[2,2,8]):
 q,p,h=line;v=[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,m)];n=max(M0,key=lambda n:abs(dot(n,v))/sum(abs(dot(n,c)) for c in U));sup=sum(abs(dot(n,c)) for c in U);val=abs(dot(n,v));assert val>sup
 z=[F(0)]*29
 for j,x in zip(free,vals):z[j]=F(x,10**12)
 v1=[a-b-c-sum(z[j]*U1[j][i] for j in free) for i,(a,b,c) in enumerate(zip(v,s,t))]
 for j,row in zip(p1,M1):z[j]=dot(row,v1)
 assert max(map(abs,z))<1 and all(sum(a*b[i] for a,b in zip(z,U1))==v[i]-s[i]-t[i] for i in range(N))
 sign=1 if dot(n,v)>0 else -1;supk=sup+2*sum(max(0,sign*dot(n,c)) for c in scale(k*L));assert val>supk
 print('q',q,'zero ratio',float(val/sup),'signed slack',float(1-max(map(abs,z))),'k',k,'ratio',float(val/supk))
q=lines[0][0];L3=L2=10**8
while L3<=d0*q*q/(4*400000):L3*=2
while L2<=q*q:L2*=2
print('PASS',len(P),*[float(x) for x in width],box,len(lines),float(L3),float(L2),'q>10^79 for L>=8*10^114')
```
