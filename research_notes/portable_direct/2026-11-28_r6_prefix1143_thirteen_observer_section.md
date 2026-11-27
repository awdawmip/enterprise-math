# PREFIX-1143: Thirteen-observer global section, exact lattice search and bounded-fiber witnesses

2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH, continuing the original own managed registration (recovery metadata confirmed nonrevoked, not closed; no formal claim or shared execution-state change). Status AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESSES / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Fixed inputs and evidence
P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d, unchanged; current P000/worldview, joint observer and portable protocol read. The account entry blobs matched immutable main 42afa4b2e0ef3aadfc881da5ebd53c3cd6ad6c10. Predecessor a3ede9ce612c4f08d420937b56559812ea62ca32:research_notes/portable_direct/2026-11-28_r6_prefix1142_high_radial_joint_exclusion.md (contains exact 13-observation rows and common normal, compact verifier). Reuse fd5b29757feda778fdc120f85ecb32c1b67cb847:research_notes/portable_direct/prefix1141/fixture1141.json and 9514c30135e1d76bdb5581e2b4d1fccdaf491f3f:research_notes/portable_direct/prefix1141/verify1141_compact.py. Previous local archive manifest checked; previous verifier replayed, including all eight PREFIX-1141 candidates and seven strict exclusions. No new anchor or original moment evaluation. No independent revalidation of the inherited Stage46/analytic anchor enclosure; the starting outer polygon and affine transfer are inherited. Auxiliary rational observer coordinates, not native spatial dimensions or a native simulation.

## Proposition and proof
Let P0 be the outward grid polygon of the PREFIX-1141 fixture, translated by reference (r,u), and use the exact thirteen observer rows from PREFIX-1142. For each integer n, define a=-G*(n[0]*aj+n[1]*dj), b=G*n[1]*am, z=n.m, S=sum_j|n.C_j|+sum_i|n_i|e_i. The true translated parameter belongs to every slab |a*x+b*y-z|<=S, by the inherited affine transfer with all shared columns and all independent errors retained. In particular select any seven observation indices and take the signed six-by-six cofactors of the first six common residual columns restricted to these indices, then pad by zero; these are valid support directions. The proof uses only membership of the true point in the original joint outer model, not an equivalence between the sparse projection and bounded fiber.

Intersect P0 with the predecessor common normal and all nonzero such normals having at least one of indices 0,1 and at least one new radial index 10,11,12. Actual exact Bareiss search: 1109 directions including the common normal, 28 active cuts, 28 vertices. Widths rho=4.4132922074266645e-103, c=2.11712261983678e-102 (about 16.24x narrower than PREFIX-1140's last displayed widths). The independent verifier below uses the common normal and 27 selected coordinate patterns, recursively expanded determinants, and pairwise exact boundary intersections (not polygon clipping); it returns the same 28-vertex polygon widths and enumeration results. The intersection is an outer enclosure, not claimed to be the full projection of the joint model.

Let L0=10^114. For all L>=L0 the inherited necessary parameter relation is (p/q,h/q) in (P+(r,u))+[-K/L0^2,0]x[0,H/L0]. The Minkowski sum is the convex hull of all vertex plus rectangle-corner sums. Apply the inherited integer unimodular V with inverse W. Every n_i=q*(V_i0+V_i1*(p/q)+V_i2*(h/q)) lies between extrema at q endpoints q0,Q and polygon vertices: a bilinear expression achieves its extrema there by successive affine optimization. For Q=10^70 exact bounds are [-1,2]x[-5,-1]x[1,73], 1460 integer points. Invert all and test q0<=q<=Q and all convex hull edge inequalities; retain gcd(q,p)=1. 15 points, eight primitive relations. Q=2*10^69: 14 grid points, no survivors. Under inherited Stage46 conditions (including inherited q0 lower bound), every genuine pair for L>=10^114 satisfies b-a>=q>=qmin=2532589569295322764098535066051372650923023384793416365730762294908651. First unexcluded dyadic windows from inherited thresholds (base 10^8): triple 6.769213120412146e133, close pair 8.872543021186608e138, each twice PREFIX-1142. Continuous integer endpoint 4.72478e43 unchanged; unbounded strict separation and B_fix,odd(32) open. This does not prove sharpness for the genuine spectrum.

## Full bounded fiber
For each of the eight candidate relations use T=(-G*aj*(p/q-r), G*(am*(h/q-u)-dj*(p/q-r)),0,...,0), U=[C,diag(e)] (25 columns). Choose the inherited ten pivots and three new independent error axes. Solve the exact 13x13 system for the pivot coefficients after fixing the twelve free coefficients at the stored integers divided by 10^12. The proposals were obtained by scaled floating LP, but the exact rational witness is checked by all 13 equations and all 25 bounds. This proves all eight are feasible in the complete affine outer model even with zero scale error. In increasing q order, exact slack 1-max|z_i| displayed as 0.6632616667539015, 0.052803054837365325, 0.10289227188010626, 0.33224265996476143, 0.335634236914, 0.4192097766145074, 0.40944982545197034, 0.019998553868737824; all strictly >19/1000. Therefore no support direction in the same thirteen-observer outer model can exclude them. The witness allows independent enclosure errors; it is not a claim of true nonlinear density or exact BRC coefficient feasibility.

## Reproduction
Save the embedded code in the PREFIX-1142 paper as verify1142_compact.py beside the two fixed predecessor files, and the following as verify1143_compact.py. The local executed verifier used the equivalent predecessor JSON-backed verifier via a two-line shim, with the same rows/normal (the embedded code in the prior paper has identical inputs); the new verifier's exact boundary intersections, exhaustive enumeration and rational witness checks all passed. No floating LP is required for replay.

```python
# Python stdlib only. Inputs: fixture1141.json, verify1141_compact.py,
# predecessor verify1142_compact.py extracted from PREFIX-1142 paper.
from fractions import Fraction as F
from itertools import combinations,product
from math import ceil,floor,gcd
import runpy
D=runpy.run_path('verify1142_compact.py'); A=D['D']; G,L,K,H,aj,am,dj,r,u,m,e,C,n=[D[k] for k in ('G','L','K','H','aj','am','dj','r','u','m','e','C','n')]
V,W,q0,hull,solve,d0=[A[k] for k in ('V','W','q0','hull','solve','d0')]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def det(M):
 if not M:return 1
 return sum((-1)**i*x*det([row[:i]+row[i+1:] for row in M[1:]]) for i,x in enumerate(M[0]) if x)
def norm(I):
 R=[[c[i] for i in I] for c in C[:6]];v=[(-1)**j*det([row[:j]+row[j+1:] for row in R]) for j in range(7)];g=gcd(*v);assert g
 out=[0]*13
 for i,x in zip(I,v):out[i]=x//g
 assert all(dot(out,c)==0 for c in C[:6]);return out
patterns=[(0,1,2,3,5,6,10),(0,1,2,3,5,6,11),(0,1,2,3,5,10,12),(0,1,2,3,5,11,12),(0,1,2,3,6,11,12),(0,1,2,4,5,6,10),(0,1,2,4,5,6,11),(0,1,2,4,5,6,12),(0,1,2,4,5,10,12),(0,1,2,4,5,11,12),(0,1,2,4,6,11,12),(0,1,2,5,6,7,10),(0,1,2,5,6,7,11),(0,1,2,5,6,7,12),(0,1,2,5,6,8,11),(0,1,2,5,6,8,12),(0,1,2,5,6,9,12),(0,1,2,5,6,10,12),(0,1,2,5,6,11,12),(0,1,2,5,7,11,12),(0,1,2,6,7,11,12),(0,1,3,5,6,10,12),(0,1,3,5,6,11,12),(0,1,4,5,6,11,12),(0,1,5,6,7,11,12),(0,2,5,6,7,11,12),(1,2,5,6,7,11,12)]
def edges(P):
 return [(v-y,x-w,(v-y)*x+(x-w)*y) for (x,y),(w,v) in zip(P,P[1:]+P[:1])]
P0=[(x-r,y-u) for x,y in A['P']];I=edges(P0)
for z in [n]+[norm(i) for i in patterns]:
 a=-G*(z[0]*aj+z[1]*dj);b=G*z[1]*am;t=dot(z,m);S=sum(abs(dot(z,c)) for c in C)+sum(abs(x)*y for x,y in zip(z,e));I.extend([(a,b,t+S),(-a,-b,S-t)])
# Independent intersection of all boundary pairs, not iterative clipping.
P=set()
for (a,b,c),(x,y,z) in combinations(I,2):
 d=a*y-b*x
 if d:
  v,w=(c*y-b*z)/d,(a*z-c*x)/d
  if all(i*v+j*w<=k for i,j,k in I):P.add((v,w))
P=hull(P);assert len(P)==28
print('widths',*[float(max(v[i] for v in P)-min(v[i] for v in P)) for i in range(2)])
HP=hull([(x+r-a,y+u+b) for (x,y),a,b in product(P,(0,K/L**2),(0,H/L))]);E=edges(HP);assert all(a*x+b*y<=z for a,b,z in E for x,y in HP)
Q=10**70;box=[]
for a,b,c in V:
 vals=[q*(a+b*x+c*y) for q,(x,y) in product((q0,Q),HP)];box.append((ceil(min(vals)),floor(max(vals))))
assert box==[(-1,2),(-5,-1),(1,73)];lines=[];count=0
for v in product(*(range(a,b+1) for a,b in box)):
 q,p,h=map(int,[dot(w,v) for w in W])
 if q0<=q<=Q and all(a*p+b*h<=z*q for a,b,z in E):
  count+=1
  if gcd(q,p)==1:lines.append((q,p,h))
lines.sort();assert count==15 and len(lines)==8
assert lines[0][0]==2532589569295322764098535066051372650923023384793416365730762294908651
nums=[[-336738332985,336738332985,336738332985,336738332985,-336738332985,-336738332985,-336738332985,336738332985,13844727741,336738332985,-336738332985,-234602721092],[947196944417,-947196944417,-947196944417,-947196944417,-947196944417,-947196944417,947196944417,-947196944417,-69880537239,-947196944417,947196944417,707184361527],[897107727413,-897107727413,-897107727413,897107727413,-897107727413,-897107727413,897107727413,897107727413,121817872466,897107727413,-897107727413,503041642916],[-667757338957,667757338957,667757338957,-667757338957,-667757338957,-667757338957,-667757338957,-667757338957,-622575228154,-667757338957,667757338957,-66859203402],[-664365763086,664365763086,664365763086,664365763086,-664365763086,-664365763086,664365763086,664365763086,273755120423,664365763086,-664365763086,-664365763086],[580790222928,-580790222928,-580790222928,-580790222928,-580790222928,-580790222928,580790222928,-580790222928,-45987199010,-580790222928,580790222928,438419164903],[590550174083,-590550174083,-590550174083,590550174083,-590550174083,-590550174083,590550174083,590550174083,167891318176,590550174083,-590550174083,292917320085],[980001444544,-980001444544,-980001444544,980001444544,-980001444544,-980001444544,980001444544,980001444544,882385976155,980001444544,-980001444544,129883018474]]
U=C+[[e[i] if i==j else 0 for i in range(13)] for j in range(13)];piv=A['D']['pivot']+[22,23,24];free=[i for i in range(25) if i not in piv];B=[[U[j][i] for j in piv] for i in range(13)]
for (q,p,h),v in zip(lines,nums):
 x,y=F(p,q)-r,F(h,q)-u;T=[-G*aj*x,G*(am*y-dj*x)]+[F(0)]*11;z=[F(0)]*25
 for i,j in zip(free,v):z[i]=F(j,10**12)
 rhs=[T[i]-m[i]-sum(z[j]*U[j][i] for j in free) for i in range(13)]
 for i,j in zip(piv,solve(B,rhs)):z[i]=j
 assert all(m[i]+sum(z[j]*U[j][i] for j in range(25))==T[i] for i in range(13));slack=1-max(map(abs,z));assert slack>F(19,1000);print('witness',q,float(slack))
q=lines[0][0];L3=L2=10**8
while L3<=d0*q*q/(4*400000):L3*=2
while L2<q*q:L2*=2
print('PASS',q,float(L3),float(L2))
```

## Next
The eight witnesses establish a concrete information bottleneck for the full current affine observer model. Use the two already calculated k=14400 coupled-moment raw integers to build the two pending rows, or tighten independent residual payments by an actual shared analytic bound. Test the smallest candidate first and preserve old row data; no further normal search in the unchanged model is useful for these eight. Independent mathematical review and inherited anchor exit remain pending. Owner query r6-20261128-0550-owner-read-v1 was RUNNING at the last pre-publication read; no formal claim or task mutation attempted; reconcile original read only.
