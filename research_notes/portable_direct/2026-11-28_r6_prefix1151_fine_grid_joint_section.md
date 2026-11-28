# PREFIX-1151 — Fine-grid joint section and adaptive integer exhaustion

2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH, own original registration r6-20261123-2358-session-start-own-v1 verified through recovery metadata, no active runs or new CLAIM. Independent unclaimed continuation. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED. Global entries verified at d7e598a4cb5605476e048665e382435e8d8ae650; frozen Source P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d with joint-preservation, heartbeat and residual-fidelity companions. Auxiliary spectral algebra, not native spatial geometry. Owner query r6-20261128-1348-owner-read SUCCEEDED/error=null, control Source 0010ddf1c341ac3d7db316e15fc65cb5b72ed507, INV-d6b08e6d1102a611e3f4420108bcb578 as_of 2026-11-28T05:48:46.389940Z, 547 tasks, LEASED filter empty. No shared task mutation.

## Inputs and exact new result
Predecessor b982a36886e65d3342ae094289df7fa212bfd85b:research_notes/portable_direct/2026-11-28_r6_prefix1150_final_grid_refinement.md, blob 5221a6bb805839fa5dd4f9e39b974fcbad5311dc, read back. Exact attachment PREFIX-1150-execution-evidence.zip SHA256 b884dee58f25bac8a00b477d5fc0d16ac0e7e82c72fe14516c8bb9fba655b35e; PREFIX1150_SHA256SUMS verified locally. Use grid1150.json, section1149.json, fixture1141.json and inherited verifier chain; no new raw moment or anchor calculation. All thirteen refined moment rows and the two rescaled point rows are reconstructed by verify1150.py.

At G=10^140, for each seven-row set containing point index 0 or 1, compute the primitive signed cofactor normal n for the first six common generators. With a=-G(n0 aj+n1 dj), b=G n1 am, z=n.m and S=sum_j |n.C_j|+sum_i |n_i|e_i, intersect the inherited PREFIX-1149 polygon with |a x+b y-z|<=S, where x=rho-r, y=c-u. This follows by taking the linear functional of the complete bounded shared-coefficient model. All twelve common columns and all independent errors are paid; the six annihilated columns have exactly zero contribution. Do not assert the new rounding model nests the old one. Exact Bareiss/cofactor clipping: 4551 nonzero directions, 255 effective clipping applications, 18 vertices. Only nine cofactor patterns, listed below, plus the old polygon suffice to reconstruct that same section using recursive determinants and boundary-pair intersections. Both implementations executed. Widths rho 5.764595737007676e-116 and c 2.5917971390647517e-111, respectively 1.1326e6 and 121.84 times narrower than PREFIX-1149. Exact upper bounds 577/10^118 and 260/10^113.

For L>=L0=10^114 inherit 0<=rho-p/q<=K/L^2 and 0<=h/q-c<=H/L. The Minkowski sum HP of the translated joint polygon and [-K/L0^2,0] x [0,H/L0] contains every candidate (p/q,h/q). Both scale payments are monotone; K/L0^2 approximately 9.69086e-228 and H/L0 approximately 1.93817e-113. No sign is dropped. Choose a maximum determinant triple of vertices of HP, use the predecessor observation-adaptive norm and exact rational LLL from the earlier integer basis; 34 iterations. V below has an exact integral inverse W. For q0<=q<=Q, each coordinate n_i of V(q,p,h) lies between ceil(min) and floor(max) of q(a_i+b_i t_x+c_i t_y) at q endpoints and HP vertices: for fixed q the extrema are at vertices, and for fixed vertex the function is linear in q. Conversely every integer n gives an integer (q,p,h)=Wn. Check q bounds and all HP edges a p+b h<=z q, and gcd(q,p)=1, exactly. This proves complete coverage of the stated necessary candidate set.

At Q=10^74,3*10^74,10^75 the integer box is empty; at Q=3*10^75 the full box has six points and one satisfies linear bounds but none is primitive; at Q=10^76 box [-4,0] x [-4,6] x [-5,-1] has 275 points, 51 satisfy bounds and 27 are primitive. Interval elimination used 25 outer iterations at Q=10^76; independent full enumeration agreed. Exact smallest unexcluded q=3048142332814919528589209213982978583698564309667098435985031648401009046730. Conditional on Stage46 and inherited anchor assumptions, for all L>=10^114, b-a>=q>=that number. First unexcluded dyadic windows 7.442828536787015e145 and 9.755464219737476e150 (1024 and 512 times PREFIX-1150). Continuous endpoint unchanged 4.72478e43.

## Limit and next
27 candidates pass the sparse outer section only; no full bounded-fiber feasibility or infeasibility has been established for them. Direct reuse of the old floating LP pivot formulation for the new grid produced HiGHS Status 2: Model error; no mathematical inference from that failure. Next use an exact rank-revealing/row-scaled pivot or joint parameter-scale variables with correctly signed payments; verify rational feasible witnesses or dual support certificates, starting with the minimum q. This targets genuine new information rather than repeating sparse directions. Anchor exit, independent review, unbounded final separation and B_fix,odd(32) remain open.

## Executed compact independent arithmetic
Extract PREFIX-1150-execution-evidence.zip into a directory; verify its manifest; save this exact code as verify1151_compact.py (SHA256 e0f8f623be0251fa4fc186d32e61126134eb7a3f0af52bcd7411034cc722fbef). It reconstructs the entire new section and directly exhausts the complete 275-coordinate box; output: PASS compact 18 5.764595737007676e-116 2.5917971390647517e-111 275 51 27 3048142332814919528589209213982978583698564309667098435985031648401009046730 7.442828536787015e+145 9.755464219737476e+150.

```python
from fractions import Fraction as F
from itertools import combinations,product
from math import ceil,floor,gcd
import json,runpy
R=runpy.run_path('verify1150.py'); D=R['D']; G=R['G']; m,e,C=R['m'],R['e'],R['C']; det,dot=R['det'],R['dot']
K,H,aj,am,dj,r,u=[F(D[k]) for k in ('K','H','aj','am','dj','r0','u')]; L=D['L']; q0=int(D['q0']); hull=R['R']['R']['hull']; d0=F(D['d'][0])
def edges(P):
 E=[(v-y,x-w,(v-y)*x+(x-w)*y) for (x,y),(w,v) in zip(P,P[1:]+P[:1])]; assert all(a*x+b*y<=z for a,b,z in E for x,y in P); return E
I=edges([tuple(map(F,v)) for v in json.load(open('section1149.json'))['vertices']])
patterns=[(0,1,8,9,11,12,13),(0,1,8,9,11,12,14),(0,1,8,9,11,13,14),(0,1,8,10,11,13,14),(0,1,8,10,12,13,14),(0,1,8,11,12,13,14),(0,1,9,11,12,13,14),(0,8,9,11,12,13,14),(1,8,9,11,12,13,14)]
for p in patterns:
 M=[[c[i] for i in p] for c in C[:6]]; v=[(-1)**j*det([row[:j]+row[j+1:] for row in M]) for j in range(7)]; g=gcd(*v); assert g
 n=[0]*15
 for i,x in zip(p,v): n[i]=x//g
 assert all(dot(n,c)==0 for c in C[:6]); a=-G*(n[0]*aj+n[1]*dj); b=G*n[1]*am; t=dot(n,m); s=sum(abs(dot(n,c)) for c in C)+sum(abs(x)*y for x,y in zip(n,e)); I.extend([(a,b,t+s),(-a,-b,s-t)])
P=set()
for (a,b,c),(x,y,z) in combinations(I,2):
 d=a*y-b*x
 if d:
  v,w=(c*y-b*z)/d,(a*z-c*x)/d
  if all(i*v+j*w<=k for i,j,k in I): P.add((v,w))
P=hull(P); assert len(P)==18
width=[max(v[i] for v in P)-min(v[i] for v in P) for i in range(2)]; assert width[0]<F(577,10**118) and width[1]<F(260,10**113)
HP=hull([(x+r-a,y+u+b) for (x,y),a,b in product(P,(0,K/L**2),(0,H/L))]); E=edges(HP)
V=[[-18670489244415526628670988648058192392855,871625478636614240142029981713599616357,-173419898766955140270530248765443456],[282253062467612140459328615128743493399042,-13165247778750783416788072350772772970091,104228734251457865218082271657973912],[-26773059956723882016587924821313399517573,1248386911958539243749815831398419130942,76645608378358867422181077118852499]]
solve=R['R']['R']['solve']; W=list(zip(*(solve(V,[int(j==i) for j in range(3)]) for i in range(3)))); assert all(v.denominator==1 for w in W for v in w); W=[list(map(int,w)) for w in W]; assert all(dot(v,w)==(i==j) for i,v in enumerate(V) for j,w in enumerate(zip(*W)))
Q=10**76; box=[]
for a,b,c in V:
 vals=[q*(a+b*x+c*y) for q,(x,y) in product((q0,Q),HP)]; box.append((ceil(min(vals)),floor(max(vals))))
assert box==[(-4,0),(-4,6),(-5,-1)]; pts=[]; tested=0
for n in product(*(range(a,b+1) for a,b in box)):
 tested+=1; q,p,h=[dot(w,n) for w in W]
 if q0<=q<=Q and all(a*p+b*h<=z*q for a,b,z in E): pts.append((q,p,h))
lines=sorted(v for v in pts if gcd(v[0],v[1])==1); assert tested==275 and len(pts)==51 and len(lines)==27
q=lines[0][0]; assert q==3048142332814919528589209213982978583698564309667098435985031648401009046730
L3=L2=10**8
while L3<=d0*q*q/(4*400000): L3*=2
while L2<=q*q: L2*=2
print('PASS compact',len(P),*[float(v) for v in width],tested,len(pts),len(lines),q,float(L3),float(L2))
```
