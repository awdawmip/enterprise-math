# PREFIX-1150 — Final observer grid refinement and common separation

Date: 2026-11-28. Continuation of EM-DIRECT-780BBE / TASK_RESEARCH (own managed recovery metadata verified: original registration r6-20261123-2358-session-start-own-v1, no runs, not closed/revoked). Independent unclaimed science; no shared task mutation. Author analytic proof and exact rational auxiliary computation, conditional Stage46/anchor application, NOT_REVIEWED. Global rules snapshot 59a2e3f9e6f0b7d9c6c5ecfc06cf1107da318eda; current control source 23a0ef5b0c0c562242c184a95ba28237188a80b9. Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d and companion joint-preservation, heartbeat and residual-fidelity contracts retained. This is auxiliary spectral algebra, not a native spatial representation.

## Source and exact inputs
Predecessor 9744b7cf86a405fb47bb14868c533e81b1106232:research_notes/portable_direct/2026-11-28_r6_prefix1149_rebased_joint_section.md (blob 8537b3807f0b008bea851c117d12458ee814696e). Prior raw resolution 4d1a6dcf25ba4920f56a185337de1803e42a82f9:research_notes/portable_direct/2026-11-28_r6_prefix1148_raw_resolution_refinement.md. Use the exact PREFIX-1149-execution-evidence.zip, SHA256 fe1c274d7c5a0c16351fbbacca285025df1edb080adc02135967a905b98fb70e; its PREFIX1149_SHA256SUMS was checked against the extracted inputs. It includes anchor_compact.json, fixture1141.json, refine1148.json, rebase1149.json, fixture1149_compact.json, the five pre-existing row files and verify1149_compact.py. All existing raw moments and row coefficients are reused, not re-generated. The inherited anchor exit proof and independent mathematical review remain unresolved.

## Precision refinement lemma and result
Old grid G0=10^125, new G=10^140, raw Hraw=10^150, internal J=10^155. For a radial/coupled row with exact rational (already certified at J) coefficient vector w and raw integer v, use unrounded center M=w.cc-(2v+1)/(2 Hraw), and the twelve common coefficients B_j=w.W_j (six) and w_i dr_i (six). The actual common anchor coefficients remain bounded by one. For row error delta=(35/36)^k times channel factor [1 for channel 0, 6^(j+1)/(j+1) for j=1,2] +1/(2 Hraw)+10^-180+1205/J, define integer m=floor(G M), C_j=floor(G B_j), e=ceil(G delta)+13. Proof: each of the center and twelve generator floor errors has absolute value <1, each generator coefficient has absolute value <=1, so the additional 13 units cover their entire signed sum by the triangle inequality. This is a valid outer enclosure at any positive integer G. The two existing point-observation rows are deliberately NOT refined: multiply their integer centers, generators and error radii by G/G0, preserving the original normalized rows exactly. No assumption of nesting between independently rounded outer enclosures is required. Intersect with inherited constraints.

All 13 row centers, generator coordinates and payments at G0 were reconstructed and matched the exact PREFIX-1148 row data. At G=10^140 the 15 integer payments, in original order, are:
[778398383415451144000000000000000,1239925114392458660351977000000000000000,452309625412190153,5776346847707,73768470,16971,67843,956,14,14,14,14,14,14,14].
For the seven final rows the normalized error decreases by exactly 10^15 (14*10^-125 to 14*10^-140); for the other six moment rows the remaining analytic-tail term limits improvement. Point-observation errors unchanged. No new raw moments or anchor computations.

## Exact exclusion
Use inherited L0=10^114, K,H,aj,am,dj,r,u. For n with support I=(0,3,5,6,8,11,12), take signed 6x6 cofactors of the first six shared generators restricted to I, divide by gcd, extend by zero. Then n.C_j=0 for j<=6 exactly. Pay all others and all independent errors in S=sum_j |n.C_j|+sum_i |n_i| e_i. Let a=-G(n0 aj+n1 dj), b=G n1 am, z=n.m, x=p/q-r, y=h/q-u. From inherited true parameters rho,c satisfying signed necessary bounds 0<=rho-p/q<=K/L^2 and 0<=h/q-c<=H/L, the candidate must satisfy
a x+b y-z <= S+max(0,-a)K/L^2+max(0,b)H/L,
z-a x-b y <= S+max(0,a)K/L^2+max(0,-b)H/L.
Both RHS nonincreasing for L>=L0, so a strict violation at L0 suffices for every such L.

The predecessor's first tested cofactor pattern separates ALL 30 primitive candidates; no further pattern search necessary. Exact rational ratio >407 for every candidate; displayed min 407.1371777736978, max 13777.004659200655. The independent verifier recursively expands determinants instead of Bareiss and re-exhausts the predecessor 540-coordinate box: 39 lattice points, 30 primitive relations, identical list. It independently reconstructs all refined rows and checks the new JSON. All assertions passed. Thus conditional on the inherited Stage46 and anchor premises, for every L>=10^114, b-a>=q>10^74. First unexcluded fixed dyadic windows by inherited formulas: 7.268387242956069e142 (triple) and 1.9053641054174757e148 (sqrt pair); both four times the previous value. The continuous integer endpoint stays 4.72478e43. No unbounded final separation or B_fix,odd(32) proof is claimed.

## Reproduction
Extract the exact predecessor archive and save the following compact verifier as verify1150_replay.py. It uses the predecessor compact verifier to independently recover the 30 primitive candidates, reconstructs the 15 rows at G, and verifies the same fixed cofactor certificate. The actually executed local scripts grid1150.py (SHA256 3a810919bba56a64f081e392aa20ee14ff0cbb455c4adee7e411d2c53f8d202a) and verify1150.py (SHA256 f6238cf6f8fc08de638f5f43043015c77accf98519103467f275acb3d29f956d) also compare the derived grid1150.json (SHA256 f52698d4e130b349b55f64a2f98482732d31099c380b313908a544ea2f4361e6). The replay below is the same independent arithmetic with the redundant comparison to the new JSON omitted; it does not require that derived file.

```python
from fractions import Fraction as F
from math import floor,ceil,gcd
import json,runpy
R=runpy.run_path('verify1149_compact.py')
D=R['R']['D']; lines=R['lines']; assert len(lines)==30
G=10**140; oldG=D['G']; kappa=G//oldG; E=json.load(open('refine1148.json')); A=json.load(open('anchor_compact.json'))
c=[F(int(v),10**120) for v in A['center']]; W=[[F(int(v),10**140) for v in row] for row in A['weighted_columns_rows']]; t=[F(int(v),10**140) for v in A['rounding_radii']]
assert all(abs(c[i])+sum(abs(v) for v in W[i])+t[i]<1 for i in range(6))
rows=[v for f in ('radial1146_low.json','coupled1146.json','radial1146_high.json','extra_radial1144_tight.json','extra_coupled1144_tight.json') for v in json.load(open(f))]
m=[v*kappa for v in D['m'][:2]]; e=[v*kappa for v in D['e'][:2]]; C=[[v*kappa for v in col[:2]] for col in D['cols']]
for row,obs in zip(rows,E['rows']):
 k,j=row['k'],row.get('channel',0);assert (k,j)==(obs['k'],obs['channel']); a=list(map(F,row['row'])); b=sum(x*y for x,y in zip(a,c))-F(2*int(obs['raw'])+1,2*10**150)
 v=[sum(a[i]*W[i][l] for i in range(6)) for l in range(6)]+[a[i]*t[i] for i in range(6)]
 tail=F(35,36)**k*(F(6**(j+1),j+1) if j else 1); err=tail+F(1,2*10**150)+F(1,10**180)+F(1205,10**155)
 assert floor(b*oldG)==obs['m'] and [floor(x*oldG) for x in v]==obs['cols'] and ceil(err*oldG)+13==obs['error']
 m.append(floor(G*b));e.append(ceil(G*err)+13)
 for col,x in zip(C,v):col.append(floor(G*x))
I=(0,3,5,6,8,11,12)
def det(M):
 if not M:return 1
 return sum((-1)**i*x*det([row[:i]+row[i+1:] for row in M[1:]]) for i,x in enumerate(M[0]) if x)
M=[[col[i] for i in I] for col in C[:6]]; n0=[(-1)**j*det([row[:j]+row[j+1:] for row in M]) for j in range(7)]; g=gcd(*n0);assert g
n=[0]*15
for i,x in zip(I,n0):n[i]=x//g
def dot(a,b):return sum(x*y for x,y in zip(a,b))
assert all(dot(n,col)==0 for col in C[:6]); S=sum(abs(dot(n,col)) for col in C)+sum(abs(x)*y for x,y in zip(n,e));z=dot(n,m)
K,H,aj,am,dj,r,u=[F(D[k]) for k in ('K','H','aj','am','dj','r0','u')]; L=D['L']; a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am
rat=[]
for q,p,h in lines:
 v=a*(F(p,q)-r)+b*(F(h,q)-u)-z
 P=S+max(0,-a)*K/L**2+max(0,b)*H/L; M=S+max(0,a)*K/L**2+max(0,-b)*H/L
 ratio=max(v/P,-v/M); assert ratio>407;rat.append(ratio)
Q=10**74;d0=F(D['d'][0]);L3=L2=10**8
while L3<=d0*Q*Q/(4*400000):L3*=2
while L2<=Q*Q:L2*=2
print('PASS: 30/30, minimum ratio',float(min(rat)), 'maximum',float(max(rat)), 'Q',Q,'first unexcluded windows',float(L3),float(L2))
print('exact L3,L2',L3,L2)
```

Actual local verifier log SHA256 077bc10288186856825636ac24f977ad8ef27bd132c999dc234edb43f431eb57. Output:
PASS compact 25 6.529117480054215e-110 3.1579443554981587e-109 540 39 30 53102590994133180630926292345110267863622958364367639094454561109869586225 0.017424661288406626 1.8170968107390172e+142 4.763410263543689e+147
PASS: 30/30, minimum ratio 407.1371777736978 maximum 13777.004659200655 Q 100000000000000000000000000000000000000000000000000000000000000000000000000 first unexcluded windows 7.268387242956069e+142 1.9053641054174757e+148

## Next
Rebuild the global parameter section with all useful new fine-grid normals, intersect the historical section, rebase via PREFIX-1149 observer-adapted unimodular coordinates, then enlarge Q. Do not re-run raw moment or anchor calculations just to reproduce this exclusion. Compare individual normalized tail payments and the two unrefined point rows before further grid increase. The new section width and candidates above 10^74 are not yet computed. Independent review, inherited anchor exit and mother target remain open. Owner query r6-20261128-1250-owner-read still RUNNING at draft observation; no protected state changed.
