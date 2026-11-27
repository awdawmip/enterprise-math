# PREFIX-1145: Fifteen-observer global section and two complete bounded fibers

Date: 2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH, own original registration verified with recovery_status r6-20261128-0747-recovery-v1 and original session_start r6-20261123-2358-session-start-own-v1. No formal CLAIM or shared task mutation. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESSES / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Sources and control

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d and same-pin Heartbeat, joint observer and residual-fidelity companions. Current account canonical main e21a9a55b474917076abfdf1be257ff5de96622f; entry blobs rechecked against that immutable commit, ACTIVE worldview and project role/current normative rules read. Predecessor e71d43a11dc63a1c73ddc1924c209a90f5aece61:research_notes/portable_direct/2026-11-28_r6_prefix1144_precision_budget_coupled_exclusion.md. Local PREFIX-1144 archive manifest checked. All eight predecessor strict exclusions replayed. The exact rows, common normal and earlier Stage46 hypotheses remain unchanged. This is an auxiliary rational observer model, not a native spatial model or native simulation.

Owner read r6-20261128-0747-owner-v1 SUCCEEDED/error=null, fixed inventory INV-c0af934aa6b2fa54f18865bb52693509 at 2026-11-27T23:48:32.453307Z, Source c13b29b6f48d6ac6f78cf873c97280eb131a5375. Total 547, LEASED filter empty. Existing independent own prefix line continued.

## Global section and proof

Use the fifteen rows of PREFIX-1144: ten earlier rows plus five rows with tightened error e_i=50014 (14400/16000/20000 radial, two 14400 coupled). Keep all twelve shared columns C and fifteen independent error coordinates. Let G=10^125, m be the integer center, e the row radii; the affine target for x=rho-r and y=c-u is T=(-G*aj*x,G*(am*y-dj*x),0,...,0). For any integer normal n, the enclosure T in m+C[-1,1]^12+diag(e)[-1,1]^15 implies
|a*x+b*y-z| <= S,
a=-G*(n[0]*aj+n[1]*dj), b=G*n[1]*am, z=n.m,
S=sum_j|n.C_j|+sum_i|n_i|e_i.
Use the predecessor 28-vertex thirteen-observer outer section as the starting set. The new common normal and sparse normals (signed maximal minors on seven selected rows of the six leading columns, extended by zero) give valid half-spaces without dropping any of the shared or error columns. This is an outer section, not the asserted exact projection. Scan 3334 nonzero/applied directions (including common normal); 15 cut at least one prior vertex, including the common normal, leaving 16 vertices. Independent replay needs only these 15 directions. Widths of rho and c are 2.545530566333355e-104 and 1.2208573853362122e-103, versus 4.41329e-103 and 2.11712e-102 in PREFIX-1143 (about 17.3-fold improvement each). No new raw moment or high-order anchor evaluation.

## Integer relation enumeration

For all L>=L0=10^114, inherited Stage46 conditions imply (p/q,h/q) belongs to the above section translated by (r,u) and Minkowski-added to [-K/L0^2,0] x [0,H/L0]. Reuse the exact integer coordinate basis V from fixture1141.json; inverse W verified integral and V*W=I. q0 and the inherited lower-denominator coverage remain unchanged. For each row (a,b,c) of V extrema of q*(a+b*rho'+c*c') over q0<=q<=Q and the convex expanded polygon occur at endpoint q and polygon vertices, giving complete integer bounds by ceil/floor. Every polygon facet inequality becomes an integer half-space after multiplication by a positive common denominator. Fix the two shortest integer coordinates and intersect exact lower/upper bounds for the third; alternatively enumerate the whole box. No floating decisions.

Q=10^70: empty box [(1,0),(-4,-1),(1,70)].
Q=3*10^70: box [(1,1),(-12,-1),(1,211)], 2532 points, 12 outer combinations, no surviving points.
Q=10^71: box [(1,6),(-42,-1),(1,706)], 177912 points, 252 outer combinations, 3 surviving lattice points, 2 with gcd(p,q)=1. Independent full enumeration and exact half-space check reproduced this. The two primitive triples in (q,p,h) order are:
(62079791971705189204794035436605825930158816418360040693738986967303276,1330993019468440671869632869922937779517033736978478837798186206096678811,6154653303835867869133124301877937360900024576109790456020116619328591316)
(93871880411373781997215425136755177131565090239253104802992826618837333,2012616563033287283272726722291430475714611929666527661925778699410423874,9306553075668718304006670171183123413480453141804037903848202063692667812).

Under the inherited Stage46 and anchor conditions, b-a>=q>=62079791971705189204794035436605825930158816418360040693738986967303276 for all L>=10^114. The first unexcluded fixed dyadic windows (base 10^8) for triple and close pair are respectively 3.4658371176510186e136 and 4.542742026847543e141 (32 times PREFIX-1144 in each case), using inherited curvature bounds and unchanged lower-scale coverage. The continuous integer endpoint remains 4.72478e43. No claim of unbounded separation.

## Complete bounded fibers: new obstruction

For each remaining primitive triple use x=p/q-r,y=h/q-u with zero scale expansion. Solve the 15 equalities in the full U=[C,diag(e)] system retaining 27 bounded coordinates. The 15 pivot columns below are invertible; the twelve free values are rational numbers with denominator 10^12. Floating LP only proposes them. Exact solve gives slack 1-max|z_i| = 0.1991790549828928 and 0.44062865250874445; both strictly >19/100. Since all error coordinates are positive, U has full row rank. An interior cube point maps to an interior point of the affine outer zonotope: for sufficiently small perturbation of T simply change the corresponding independent error coordinates while retaining shared ones. Thus *every* support direction of the same fifteen-observer affine outer model fails to exclude these two targets at zero scale error, not merely the 3334 scanned normals. This establishes a local information limit of that model; it neither establishes actual shared nonlinear spectral feasibility nor actual double anomalies.

## Reproduction

Run the following standard-library replay in the verified PREFIX-1144 execution archive directory, retaining verify1144.py and all its immutable predecessor fixtures (fixture1141.json, extra_radial1142.json, fiber1142.json, extra_radial1144_tight.json, extra_coupled1144_tight.json, fiber1144_alltight.json, predecessor compact verifiers). Exact rows and common normal are also recorded in PREFIX-1144 paper. Main scan section1145.py used Bareiss minors, clipping and exact third-coordinate interval enumeration. The compact replay below uses recursive determinants, boundary-pair intersection and every coordinate triple, then verifies both complete bounded fibers. Actual replay output: widths 2.545530566333355e-104 1.2208573853362122e-103; witness slacks 0.1991790549828928 0.44062865250874445; PASS 177912 3 2 62079791971705189204794035436605825930158816418360040693738986967303276 3.4658371176510186e+136 4.542742026847543e+141. This is a second arithmetic implementation by the same author, not independent reviewer acceptance. Inherited analytic anchor/Stage46 not independently re-proved.

```python
from fractions import Fraction as F
from itertools import combinations,product
from math import ceil,floor,gcd,lcm
import runpy
D=runpy.run_path('verify1144.py'); A=D['A']; V,W,q0,hull,d0,solve=[A[k] for k in ('V','W','q0','hull','d0','solve')]
G,L,K,H,aj,am,dj,r,u,m,e,C=[D[k] for k in ('G','L','K','H','aj','am','dj','r','u','m','e','C')]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
def det(M):
 if not M:return 1
 return sum((-1)**i*x*det([row[:i]+row[i+1:] for row in M[1:]]) for i,x in enumerate(M[0]) if x)
patterns=[(0,1,2,5,7,12,14),(0,1,2,5,8,12,14),(0,1,2,5,9,12,14),(0,1,2,5,10,11,14),(0,1,2,5,10,12,14),(0,1,2,5,11,12,14),(0,1,2,10,11,12,13),(0,1,2,10,11,12,14),(0,1,2,10,11,13,14),(0,1,2,10,12,13,14),(0,1,2,11,12,13,14),(0,1,10,11,12,13,14),(0,2,10,11,12,13,14),(1,2,10,11,12,13,14)]
def norm(I):
 M=[[c[i] for i in I] for c in C[:6]];v=[(-1)**j*det([row[:j]+row[j+1:] for row in M]) for j in range(7)];g=gcd(*v);assert g
 n=[0]*15
 for i,x in zip(I,v):n[i]=x//g
 assert all(dot(n,c)==0 for c in C[:6]);return n
def edges(P):
 E=[(v-y,x-w,(v-y)*x+(x-w)*y) for (x,y),(w,v) in zip(P,P[1:]+P[:1])];assert all(a*x+b*y<=z for a,b,z in E for x,y in P);return E
I=edges(D['D']['P'])
for n in [D['n']]+[norm(i) for i in patterns]:
 a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am;z=dot(n,m);S=sum(abs(dot(n,c)) for c in C)+sum(abs(x)*y for x,y in zip(n,e));I.extend([(a,b,z+S),(-a,-b,S-z)])
# Independent boundary-pair intersection, rather than iterative clipping.
P=set()
for (a,b,c),(x,y,z) in combinations(I,2):
 d=a*y-b*x
 if d:
  v,w=(c*y-b*z)/d,(a*z-c*x)/d
  if all(i*v+j*w<=k for i,j,k in I):P.add((v,w))
P=hull(P);assert len(P)==16
width=[max(v[i] for v in P)-min(v[i] for v in P) for i in range(2)];assert width[0]<F(255,10**106) and width[1]<F(123,10**105)
print('widths',*[float(x) for x in width])
HP=hull([(x+r-a,y+u+b) for (x,y),a,b in product(P,(0,K/L**2),(0,H/L))]);E=edges(HP)
Q=10**71;box=[]
for a,b,c in V:
 vals=[q*(a+b*x+c*y) for q,(x,y) in product((q0,Q),HP)];box.append((ceil(min(vals)),floor(max(vals))))
assert box==[(1,6),(-42,-1),(1,706)]
# Convert exact rational half-spaces to integer inequalities and check every coordinate triple.
J=[]
for a,b,z in E:
 row=[a*W[1][i]+b*W[2][i]-z*W[0][i] for i in range(3)];den=lcm(*(x.denominator for x in row));J.append([int(x*den) for x in row])
WW=[list(map(int,w)) for w in W];assert all(F(x)==y for row,w in zip(WW,W) for x,y in zip(row,w))
assert all(dot(v,w)==(i==j) for i,v in enumerate(V) for j,w in enumerate(zip(*WW)))
lines=[];points=[];tested=0
for n in product(*(range(a,b+1) for a,b in box)):
 tested+=1;q=dot(WW[0],n)
 if q0<=q<=Q and all(dot(v,n)<=0 for v in J):
  p,h=dot(WW[1],n),dot(WW[2],n);points.append((q,p,h))
  assert all(a*p+b*h<=z*q for a,b,z in E)
  if gcd(p,q)==1:lines.append((q,p,h))
lines.sort();assert tested==177912 and len(points)==3 and len(lines)==2
assert [q for q,p,h in lines]==[62079791971705189204794035436605825930158816418360040693738986967303276,93871880411373781997215425136755177131565090239253104802992826618837333]
# Exact full-fiber witnesses, with no floating LP dependency.
nums=[[800820944339,800820944339,-800820944339,800820944339,-800820944339,800820944339,800820944339,800820944339,-250008457833,44143132850,3412305571,-637214215],[-559371344493,-559371344493,559371344493,-559371344493,559371344493,-559371344493,-559371344493,-559371344493,47676780832,43275706526,4609457786,43201878969]]
U=C+[[e[i] if i==j else 0 for i in range(15)] for j in range(15)];piv=[0,1,2,3,4,5,15,16,19,20,22,23,24,25,26];free=[i for i in range(27) if i not in piv];B=[[U[j][i] for j in piv] for i in range(15)]
for (q,p,h),v in zip(lines,nums):
 x,y=F(p,q)-r,F(h,q)-u;T=[-G*aj*x,G*(am*y-dj*x)]+[F(0)]*13;z=[F(0)]*27
 for i,j in zip(free,v):z[i]=F(j,10**12)
 rhs=[T[i]-m[i]-sum(z[j]*U[j][i] for j in free) for i in range(15)]
 for i,j in zip(piv,solve(B,rhs)):z[i]=j
 assert all(m[i]+sum(z[j]*U[j][i] for j in range(27))==T[i] for i in range(15));slack=1-max(map(abs,z));assert slack>F(19,100);print('witness',q,float(slack))
q=lines[0][0];L3=L2=10**8
while L3<=d0*q*q/(4*400000):L3*=2
while L2<=q*q:L2*=2
print('PASS',tested,len(points),len(lines),q,float(L3),float(L2))
```

## Next

Do not repeat the fifteen-observer support scan as an exclusion route for these two candidates. Check earlier radial/coupled observation rows for avoidable quantization/arithmetic payments using PREFIX-1144's independent grids; add genuinely new constraints if needed. Retain exact interior witnesses as counterexamples to claimed separation in this unchanged affine outer model. Independent review, inherited anchor exit confirmation, unbounded strict separation and mother objective B_fix,odd(32) remain open.
